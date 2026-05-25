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

export interface SourceMeta {
  slug: string;
  title?: string;
  url?: string;
  year?: number | string;
  authors?: string[];
  type?: string;
  body: string;
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

export function loadReport(slug: string): Report {
  const dir = path.join(REPORTS_DIR, slug);
  const meta = yaml.load(fs.readFileSync(path.join(dir, 'meta.yaml'), 'utf8')) as Meta;
  const tree = yaml.load(fs.readFileSync(path.join(dir, '01-tree/tree.yaml'), 'utf8')) as Tree;

  const leavesDir = path.join(dir, '02-leaves');
  const leaves: Leaf[] = [];
  if (fs.existsSync(leavesDir)) {
    for (const entry of fs.readdirSync(leavesDir, { withFileTypes: true })) {
      if (!entry.isDirectory()) continue;
      const leafDir = path.join(leavesDir, entry.name);
      const leafYaml = path.join(leafDir, 'leaf.yaml');
      if (!fs.existsSync(leafYaml)) continue;
      const leafMeta = yaml.load(fs.readFileSync(leafYaml, 'utf8')) as Omit<Leaf, 'claims' | 'body'>;
      const claimsPath = path.join(leafDir, 'claims.yaml');
      const claims: Claim[] = fs.existsSync(claimsPath)
        ? ((yaml.load(fs.readFileSync(claimsPath, 'utf8')) as Claim[]) ?? [])
        : [];
      const reportPath = path.join(leafDir, 'passes/pass-write.md');
      let body: string | undefined;
      if (fs.existsSync(reportPath)) {
        body = matter(fs.readFileSync(reportPath, 'utf8')).content;
      }

      // Sources: each subdir of sources/ with an extract.md
      const sourcesDir = path.join(leafDir, 'sources');
      const sources: SourceMeta[] = [];
      if (fs.existsSync(sourcesDir)) {
        for (const sEntry of fs.readdirSync(sourcesDir, { withFileTypes: true })) {
          if (!sEntry.isDirectory()) continue;
          const extractPath = path.join(sourcesDir, sEntry.name, 'extract.md');
          if (!fs.existsSync(extractPath)) continue;
          const parsed = matter(fs.readFileSync(extractPath, 'utf8'));
          sources.push({
            slug: sEntry.name,
            title: (parsed.data as any).title,
            url: (parsed.data as any).url,
            year: (parsed.data as any).year,
            authors: (parsed.data as any).authors,
            type: (parsed.data as any).type,
            body: parsed.content,
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
          const parsed = matter(fs.readFileSync(path.join(passesDir, pEntry), 'utf8'));
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
  return (yaml.load(fs.readFileSync(p, 'utf8')) as GlossaryEntry[]) ?? [];
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
