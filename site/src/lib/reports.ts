import fs from 'node:fs';
import path from 'node:path';
import yaml from 'js-yaml';
import matter from 'gray-matter';
import katex from 'katex';
import { marked } from 'marked';

/**
 * Render mixed prose + LaTeX math.
 *  - Pre-renders \(..\) as inline KaTeX HTML
 *  - Pre-renders \[..\] as display KaTeX HTML
 *  - $$..$$ also goes to display KaTeX
 *  - Runs the rest through marked (inline by default)
 * Used for glossary defs, source extracts, tooltip payloads. Server-side
 * rendering avoids the marked-strips-\( problem.
 */
export function renderMath(text: string, opts: { inline?: boolean } = {}): string {
  const inline = opts.inline ?? true;
  // Source `.md` files arrive with either single-backslash (`\[`, `\(`, `\frac`)
  // or double-backslash (`\\[`, `\\(`, `\\frac`) delimiters and commands —
  // depending on how the upstream writer escaped them. Accept both shapes
  // and collapse `\\` → `\` inside the captured expression before handing
  // it to KaTeX.
  const normalize = (expr: string) => expr.replace(/\\\\/g, '\\').trim();
  // 1. Display delimiters \[..\] / \\[..\\]
  let s = text.replace(/\\{1,2}\[([\s\S]+?)\\{1,2}\]/g, (_, expr) =>
    katex.renderToString(normalize(expr), { throwOnError: false, displayMode: true })
  );
  // 2. $$..$$ (still normalize body for embedded \\frac etc.)
  s = s.replace(/\$\$([\s\S]+?)\$\$/g, (_, expr) =>
    katex.renderToString(normalize(expr), { throwOnError: false, displayMode: true })
  );
  // 3. Inline delimiters \(..\) / \\(..\\)
  s = s.replace(/\\{1,2}\(([\s\S]+?)\\{1,2}\)/g, (_, expr) =>
    katex.renderToString(normalize(expr), { throwOnError: false, displayMode: false })
  );
  // 4. Run remaining through marked
  return inline ? marked.parseInline(s) as string : marked.parse(s) as string;
}

const REPORTS_DIR = path.resolve(process.cwd(), '../reports');

export type Confidence = 'high' | 'medium' | 'low' | 'speculative';

export type NodeType = 'leaf' | 'synthesis' | 'constraint';
export type NodeStatus = 'open' | 'researching' | 'answered' | 'deprecated';

export interface TreeNode {
  id: string;
  parent: string;
  depth: number;
  type: NodeType;
  question: string;
  status: NodeStatus;
  answer: string | null;
  confidence: Confidence | null;
  leaf_path?: string;
  created_by: 'agent' | 'avi';
  created_pass: number;
  last_touched_pass: number;
  children: string[];
  flags?: string[];
}

export interface Tree {
  root: {
    id: 'root';
    question: string;
    answer: string | null;
    status: NodeStatus;
  };
  nodes: TreeNode[];
}

export interface Meta {
  slug: string;
  root_question: string;
  status: 'in_progress' | 'done';
  current_pass: number;
  created: string;
  last_updated: string;
  models: { primary: string; critic: string };
  termination: { root_answered: boolean; all_figures_reviewed: boolean };
}

export interface Claim {
  id: string;
  text: string;
  type: 'factual' | 'derived' | 'estimate';
  evidence: Array<{ source: string; ref: string; verdict: 'supports' | 'contradicts' | 'partial' }>;
  confidence: Confidence;
  derivation_path?: string;
  audit: {
    gpt: { status: 'passed' | 'flagged' | 'unaudited'; audit_file?: string; notes?: string };
    human: { status: 'noted' | 'unnoted'; comment_file?: string };
  };
}

export type SourceTier = 'S' | 'A' | 'B' | 'C' | 'D' | 'E';

export interface SourceMeta {
  slug: string;
  title?: string;
  url?: string;
  year?: number | string;
  authors?: string[];
  type?: string;
  body: string;
  // Tier-hierarchy metadata (spec: source-tiers.md). Older sources won't have these.
  tier?: SourceTier;
  peerReviewed?: boolean;
  venue?: string;
  topics?: string[];
  publicFigure?: string;
  date?: string;
}

export interface ReviewSummary {
  consistent: number;
  novelSupporting: number;
  meritsInvestigation: number;
  differentConclusion: number;
  notRelevant: number;
  total: number;
}

export interface ReviewData {
  hasReview: boolean;
  reviewPath?: string;
  reviewedPass?: number | string;
  reviewedBy?: string;
  date?: string;
  summary?: ReviewSummary;
}

export interface PassArtifact {
  filename: string;
  kind: string; // "research" | "calc" | ...
  body: string;
}

export interface Leaf {
  id: string;
  question: string;
  status: 'open' | 'researching' | 'drafting' | 'reviewed' | 'done';
  passes_status: Record<string, 'pending' | 'in_progress' | 'done' | 'needs_rerun'>;
  last_pass: number;
  claims: Claim[];
  body?: string;
  sources: SourceMeta[];
  passArtifacts: PassArtifact[];
}

export interface Report {
  slug: string;
  meta: Meta;
  tree: Tree;
  leaves: Leaf[];
}

export function listReportSlugs(): string[] {
  if (!fs.existsSync(REPORTS_DIR)) return [];
  return fs
    .readdirSync(REPORTS_DIR, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name);
}

/** YAML loader that survives malformed input — the report-side Claude is editing
 *  YAML files in parallel, so we treat parse errors as soft-fail (warn + empty)
 *  rather than killing the entire build. js-yaml's `json` mode also relaxes
 *  duplicate-key strictness, which has bitten q2 once already. */
function safeYamlLoad<T = any>(filePath: string, fallback: T): T {
  try {
    const text = fs.readFileSync(filePath, 'utf8');
    const parsed = yaml.load(text, { json: true });
    return (parsed ?? fallback) as T;
  } catch (err: any) {
    console.warn(`[reports] YAML parse failed for ${filePath}: ${err?.message || err}`);
    return fallback;
  }
}

/** Frontmatter loader that survives malformed YAML headers. gray-matter
 *  embeds its own strict js-yaml; if the report-side writes an unquoted URL
 *  with a colon (real failure mode seen 2026-05-26), the whole build dies.
 *  Soft-fail to empty frontmatter + raw body. */
function safeMatter(filePath: string): { data: Record<string, any>; content: string } {
  const text = fs.readFileSync(filePath, 'utf8');
  try {
    return matter(text);
  } catch (err: any) {
    console.warn(`[reports] frontmatter parse failed for ${filePath}: ${err?.message || err}`);
    // Strip the malformed frontmatter block manually so the body still renders
    const m = text.match(/^---\n[\s\S]*?\n---\n?/);
    return { data: {}, content: m ? text.slice(m[0].length) : text };
  }
}

export function loadReport(slug: string): Report {
  const dir = path.join(REPORTS_DIR, slug);
  const meta = safeYamlLoad<Meta>(path.join(dir, 'meta.yaml'), {} as Meta);
  const tree = safeYamlLoad<Tree>(path.join(dir, '01-tree/tree.yaml'), { root: { id: 'root', question: '', answer: null, status: 'open' }, nodes: [] } as Tree);

  const leavesDir = path.join(dir, '02-leaves');
  const leaves: Leaf[] = [];
  if (fs.existsSync(leavesDir)) {
    for (const entry of fs.readdirSync(leavesDir, { withFileTypes: true })) {
      if (!entry.isDirectory()) continue;
      const leafDir = path.join(leavesDir, entry.name);
      const leafYaml = path.join(leafDir, 'leaf.yaml');
      if (!fs.existsSync(leafYaml)) continue;
      const leafMeta = safeYamlLoad<Omit<Leaf, 'claims' | 'body'>>(leafYaml, {} as any);
      const claimsPath = path.join(leafDir, 'claims.yaml');
      const claims: Claim[] = fs.existsSync(claimsPath)
        ? safeYamlLoad<Claim[]>(claimsPath, [])
        : [];
      const reportPath = path.join(leafDir, 'passes/pass-write.md');
      let body: string | undefined;
      if (fs.existsSync(reportPath)) {
        body = safeMatter(reportPath).content;
      }

      // Sources: each subdir of sources/ with an extract.md
      const sourcesDir = path.join(leafDir, 'sources');
      const sources: SourceMeta[] = [];
      if (fs.existsSync(sourcesDir)) {
        for (const sEntry of fs.readdirSync(sourcesDir, { withFileTypes: true })) {
          if (!sEntry.isDirectory()) continue;
          const extractPath = path.join(sourcesDir, sEntry.name, 'extract.md');
          if (!fs.existsSync(extractPath)) continue;
          const parsed = safeMatter(extractPath);
          const d = parsed.data as any;
          sources.push({
            slug: sEntry.name,
            title: d.title,
            url: d.url,
            year: d.year,
            authors: d.authors,
            type: d.type,
            body: parsed.content,
            tier: typeof d.tier === 'string' ? d.tier.toUpperCase() as SourceTier : undefined,
            peerReviewed: typeof d.peer_reviewed === 'boolean' ? d.peer_reviewed : undefined,
            venue: d.venue,
            topics: Array.isArray(d.topics) ? d.topics : undefined,
            publicFigure: d.public_figure,
            date: d.date,
          });
        }
      }

      // Pass artifacts: each pass-NN-kind.md in passes/
      const passesDir = path.join(leafDir, 'passes');
      const passArtifacts: PassArtifact[] = [];
      if (fs.existsSync(passesDir)) {
        for (const pEntry of fs.readdirSync(passesDir)) {
          if (!pEntry.endsWith('.md')) continue;
          const m = pEntry.match(/^pass-\d+-(.+)\.md$/);
          const kind = m ? m[1] : pEntry.replace('.md', '');
          const parsed = safeMatter(path.join(passesDir, pEntry));
          passArtifacts.push({ filename: pEntry, kind, body: parsed.content });
        }
        passArtifacts.sort((a, b) => a.filename.localeCompare(b.filename));
      }

      leaves.push({ ...leafMeta, claims, body, sources, passArtifacts });
    }
  }

  return { slug, meta, tree, leaves };
}

export function loadAllReports(): Report[] {
  return listReportSlugs().map(loadReport);
}

export interface GlossaryEntry {
  term: string;
  symbol?: string;
  definition: string;
  category?: string;
}

export function loadGlossary(slug: string): GlossaryEntry[] {
  const p = path.join(REPORTS_DIR, slug, 'glossary.yaml');
  if (!fs.existsSync(p)) return [];
  return safeYamlLoad<GlossaryEntry[]>(p, []);
}

/** Parse a Newman-taxonomy verdict-count table from review.md body.
 *  Looks for `## Summary` followed by a markdown table; falls back to
 *  scanning `**Verdict:**` lines if the summary table is missing.
 *  Returns null if no verdict signal is found. */
function parseReviewSummary(body: string): ReviewSummary | undefined {
  const bucketLabel = (raw: string): keyof ReviewSummary | null => {
    const x = raw.toLowerCase().trim().replace(/[-_]/g, ' ');
    if (x.includes('consistent')) return 'consistent';
    if (x.includes('novel')) return 'novelSupporting';
    if (x.includes('merits')) return 'meritsInvestigation';
    if (x.includes('different')) return 'differentConclusion';
    if (x.includes('not relevant')) return 'notRelevant';
    return null;
  };
  const result: ReviewSummary = {
    consistent: 0, novelSupporting: 0, meritsInvestigation: 0,
    differentConclusion: 0, notRelevant: 0, total: 0,
  };
  let found = false;
  // Pass 1: Summary table — rows like "| Consistent | 3 |"
  const summaryStart = body.search(/^##\s+Summary/mi);
  if (summaryStart >= 0) {
    const slice = body.slice(summaryStart, summaryStart + 1500);
    const rowRe = /\|\s*([A-Za-z][A-Za-z\s\-_]*?)\s*\|\s*(\d+)\s*\|/g;
    let m: RegExpExecArray | null;
    while ((m = rowRe.exec(slice)) !== null) {
      const key = bucketLabel(m[1]);
      if (!key || key === 'total' as any) continue;
      result[key] += parseInt(m[2], 10);
      found = true;
    }
  }
  // Pass 2: fallback — count `**Verdict:** X` occurrences (handles single-claim Tier C/D shape)
  if (!found) {
    const verdictRe = /\*\*Verdict:?\*\*\s*([^\n*]+)/gi;
    let m: RegExpExecArray | null;
    while ((m = verdictRe.exec(body)) !== null) {
      const key = bucketLabel(m[1]);
      if (!key || key === 'total' as any) continue;
      result[key]++;
      found = true;
    }
  }
  if (!found) return undefined;
  result.total = result.consistent + result.novelSupporting + result.meritsInvestigation + result.differentConclusion + result.notRelevant;
  return result;
}

/** Load a per-leaf source review file (if present) and parse its verdict summary. */
export function loadSourceReview(reportSlug: string, leafId: string, sourceSlug: string): ReviewData {
  const reviewPath = path.join(REPORTS_DIR, reportSlug, '02-leaves', leafId, 'sources', sourceSlug, 'review.md');
  if (!fs.existsSync(reviewPath)) return { hasReview: false };
  const parsed = safeMatter(reviewPath);
  const d = parsed.data as any;
  return {
    hasReview: true,
    reviewPath,
    reviewedPass: d.reviewed_pass,
    reviewedBy: d.reviewed_by,
    date: d.date,
    summary: parseReviewSummary(parsed.content),
  };
}

/** Build a compact tooltip payload that can be inlined as JSON in pages. */
export function buildTooltipPayload(report: Report): {
  glossary: Array<{ term: string; symbol?: string; html: string }>;
  sources: Array<{ slug: string; title?: string; year?: any; authors?: string[]; url?: string; snippet: string }>;
} {
  const glossary = loadGlossary(report.slug).map((g) => {
    const sym = g.symbol ? `<strong style="color:var(--color-accent-soft)">${g.symbol}</strong> &mdash; ` : '';
    return {
      term: g.term,
      symbol: g.symbol,
      // Pre-render math server-side so tooltip body doesn't need client KaTeX
      html: sym + renderMath(g.definition, { inline: true }),
    };
  });

  const seenSources = new Map<string, any>();
  for (const leaf of report.leaves) {
    for (const s of leaf.sources) {
      if (seenSources.has(s.slug)) continue;
      // Snippet = first ~280 chars of extract body
      const stripped = s.body.replace(/^#\s+[^\n]+\n+/, '').trim();
      const snippet = stripped.length > 280
        ? stripped.slice(0, stripped.lastIndexOf(' ', 280)) + '…'
        : stripped;
      seenSources.set(s.slug, {
        slug: s.slug,
        title: s.title,
        year: s.year,
        authors: s.authors,
        url: s.url,
        snippet,
      });
    }
  }
  return { glossary, sources: [...seenSources.values()] };
}

export function getLeafBySlug(report: Report, leafId: string): Leaf | undefined {
  return report.leaves.find((l) => l.id === leafId);
}

export function getNodeChildren(tree: Tree, parentId: string): TreeNode[] {
  return tree.nodes.filter((n) => n.parent === parentId);
}

/**
 * Build a Mermaid graph definition from the tree. Renders top-down.
 * Each node is keyed by id with the short id as label. Color coded by type
 * + completion. Clicking a node navigates to the leaf detail page (the
 * `click` directive is interpreted by Mermaid at render time).
 */
/** Convert a slug like "q1-earth-launch-cost" → "Earth launch cost".
 *  Known acronyms (matching glossary symbols) are upper-cased. */
const ACRONYMS = new Set([
  'isru', 'leo', 'llo', 'geo', 'gto', 'dro', 'eml1', 'ls', 'tai', 'trl',
  'wacc', 'imf', 'sep', 'lox', 'lh2', 'tea', 'rll', 'otv',
]);
function naturalTitleFromSlug(slug: string): string {
  const words = slug.replace(/^q\d+-/, '').split('-');
  return words
    .map((w, i) => {
      if (ACRONYMS.has(w.toLowerCase())) return w.toUpperCase();
      return i === 0 ? w.charAt(0).toUpperCase() + w.slice(1) : w;
    })
    .join(' ');
}

export function buildMermaidTree(report: Report, slug: string): string {
  const lines = ['graph TD'];
  // Style class definitions — bold text, accent fills by status
  lines.push("  classDef root fill:#fafaf7,stroke:#c4622d,stroke-width:2.5px,color:#1a1a1a,font-weight:bold;");
  lines.push("  classDef leaf fill:#fafaf7,stroke:#4a4a4a,stroke-width:1px,color:#1a1a1a,font-weight:bold;");
  lines.push("  classDef leafDone fill:#e8f3ee,stroke:#2d6a4f,stroke-width:1.5px,color:#1a1a1a,font-weight:bold;");
  lines.push("  classDef leafInProg fill:#fef3e3,stroke:#d97706,stroke-width:1.5px,color:#1a1a1a,font-weight:bold;");
  lines.push("  classDef synthesis fill:#f0efe9,stroke:#4a4a4a,stroke-width:1px,color:#1a1a1a,font-weight:bold;");
  lines.push("  classDef constraint fill:#fafaf7,stroke:#9ca3af,stroke-width:1px,stroke-dasharray:4 3,color:#1a1a1a,font-weight:bold;");

  // Root node — short label only (full question lives in title attribute)
  lines.push(`  root["Root question"]`);
  lines.push(`  click root "/${slug}/" "${escapeMermaid(report.tree.root.question)}"`);
  lines.push(`  class root root;`);

  // Each top-level node
  for (const node of report.tree.nodes) {
    const leaf = report.leaves.find((l) => l.id === node.id);
    const subPasses = leaf ? Object.entries(leaf.passes_status) : [];
    const doneCount = subPasses.filter(([, v]) => v === 'done').length;
    const totalCount = subPasses.length;

    const safeId = node.id.replace(/[^a-zA-Z0-9]/g, '_');
    // Natural-language title + done/total progress
    const title = naturalTitleFromSlug(node.id);
    const progress = totalCount > 0 ? `  (${doneCount}/${totalCount})` : '';
    const labelText = `"${escapeMermaidLabel(title + progress, 32)}"`;
    lines.push(`  ${safeId}[${labelText}]`);

    // Edge from parent
    const parentSafeId = node.parent === 'root' ? 'root' : node.parent.replace(/[^a-zA-Z0-9]/g, '_');
    lines.push(`  ${parentSafeId} --> ${safeId}`);

    // Click action → leaf detail page
    lines.push(`  click ${safeId} "/${slug}/leaves/${node.id}/" "${escapeMermaid(node.question)}"`);

    // Style class
    let cls = 'leaf';
    if (node.type === 'synthesis') cls = 'synthesis';
    else if (node.type === 'constraint') cls = 'constraint';
    else if (doneCount === totalCount && totalCount > 0) cls = 'leafDone';
    else if (doneCount > 0) cls = 'leafInProg';
    lines.push(`  class ${safeId} ${cls};`);
  }
  return lines.join('\n');
}

function truncateForMermaid(s: string, max: number): string {
  const t = s.replace(/[`"]/g, "'");
  return t.length > max ? t.slice(0, max - 1) + '…' : t;
}

/** Cleans label text for inside Mermaid double-quoted node text. */
function escapeMermaidLabel(s: string, max: number): string {
  const t = s
    .replace(/[`<>]/g, '')      // strip backticks + HTML brackets
    .replace(/"/g, "'")          // double → single quote to stay inside the wrapper
    .replace(/\s+/g, ' ')        // collapse whitespace
    .trim();
  return t.length > max ? t.slice(0, max - 1) + '…' : t;
}

function escapeMermaid(s: string): string {
  return s.replace(/"/g, '&quot;').slice(0, 200);
}
