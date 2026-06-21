import fs from 'node:fs';
import path from 'node:path';
import yaml from 'js-yaml';
import matter from 'gray-matter';
import { renderMath } from './reports';

/**
 * Auto-Model data layer — sibling to reports.ts.
 *
 * A "model" is a physical supply-chain model under ../models/{slug}/. The site
 * reads the on-disk YAML/Markdown and renders an interactive Sankey + tabs
 * (Inputs, Companies, Idiot Index, Energetic Idiot Index, References).
 *
 * Same discipline as auto-research: every number is a claim that carries EITHER
 * an evidence.source (→ citation) OR evidence.estimate (→ labelled estimate).
 * All parsing soft-fails so a half-written YAML never kills the build.
 */

const MODELS_DIR = path.resolve(process.cwd(), '../models');

export { renderMath };

export interface Evidence {
  source?: string;        // slug under sources/  → clickable citation
  ref?: string;           // locator inside the source
  estimate?: boolean;     // true → labelled principled estimate (no external source)
  note?: string;
}

export interface SummaryStat {
  key: string;
  label: string;
  value: string;
  note?: string;
}

export interface ModelMeta {
  slug: string;
  product: string;
  question?: string;
  unit_of_analysis?: string;
  boundary?: string;
  status: string;
  scaffold?: boolean;
  current_pass?: number;
  created?: string;
  last_updated?: string;
  models?: { primary?: string; critic?: string };
  deploy?: { mode?: string; cloudflare_project?: string };
  termination?: Record<string, boolean>;
  summary?: SummaryStat[];
}

export interface Entity {
  id: string;
  name: string;
  url?: string;
  role?: string;
  location?: string;
  note?: string;
  revenue_usd?: number;
  revenue_note?: string;
  dossier?: string;     // company-dossier slug, if one exists → internal link
  tier?: string;
}

export interface Maker {
  name?: string;       // free-text maker name
  entity?: string;     // OR an entity id → resolves to a company dossier link
  url?: string;
}

export interface FlowNode {
  id: string;
  label: string;
  stage?: string;
  entity?: string;
}

export interface FlowEdge {
  from: string;
  to: string;
  value_usd?: number;
  throughput?: string;
  energy_mj?: number;
  evidence?: Evidence;
}

export interface InputItem {
  id: string;
  component: string;
  stage?: string;
  pct_of_mass?: string;
  pct_of_value?: string;
  evidence?: Evidence;
  what_it_is?: string;
  how_made?: string;
  makers?: string[];    // entity ids → resolve to company dossier links
}

export interface MarketStat {
  label: string;
  value: string;
  evidence?: Evidence;
}

export interface MarketPoint {
  year: number;
  value_usd_b: number;
  projected?: boolean;
}

export interface MarketData {
  headline?: string;
  unit?: string;
  series: MarketPoint[];
  series_evidence?: Evidence;
  stats: MarketStat[];
}

export interface IndexSide {
  label: string;
  value_usd?: number;
  value_mj?: number;
  evidence?: Evidence;
}

export interface IdiotRow {
  id: string;
  product: string;
  entity?: string;
  numerator: IndexSide;
  denominator: IndexSide;
  ratio?: number;
  confidence?: string;
  note?: string;
}

export interface EnergeticRow {
  id: string;
  product: string;
  entity?: string;
  actual: IndexSide;
  floor: IndexSide;
  ratio?: number;
  confidence?: string;
  note?: string;
}

export interface CompanyDossier {
  slug: string;
  name: string;
  url?: string;
  role?: string;
  location?: string;
  tier?: string;
  scaffold?: boolean;
  body: string;
}

export interface ReviewSummary {
  consistent: number;
  novelSupporting: number;
  meritsInvestigation: number;
  differentConclusion: number;
  notRelevant: number;
  total: number;
}

export interface ModelSource {
  slug: string;
  title?: string;
  url?: string;
  authors?: string[];
  year?: number | string;
  type?: string;
  tier?: string;
  topics?: string[];
  scaffold?: boolean;
  reviewed: boolean;
  reviewSummary?: ReviewSummary;
  body: string;
}

export interface GlossaryEntry {
  term: string;
  symbol?: string;
  definition: string;
  category?: string;
}

export interface Model {
  slug: string;
  meta: ModelMeta;
  flow: { unit?: string; nodes: FlowNode[]; edges: FlowEdge[] };
  entities: Record<string, Entity>;
  inputs: InputItem[];
  idiotIndex: IdiotRow[];
  energeticIndex: EnergeticRow[];
  companies: CompanyDossier[];
  sources: ModelSource[];
  glossary: GlossaryEntry[];
  market: MarketData | null;
}

/** Internal link to an entity's company dossier if it has one, else its external
 *  URL. Returns null if neither exists. external=true means open in a new tab. */
export function entityLink(model: Model, id?: string): { href: string; external: boolean } | null {
  if (!id) return null;
  const e = model.entities[id];
  if (!e) return null;
  const hasDossier = e.dossier && model.companies.some((c) => c.slug === e.dossier);
  if (hasDossier) return { href: `/models/${model.slug}/companies/${e.dossier}/`, external: false };
  if (e.url) return { href: e.url, external: true };
  return null;
}

function safeYamlLoad<T = any>(filePath: string, fallback: T): T {
  try {
    if (!fs.existsSync(filePath)) return fallback;
    const parsed = yaml.load(fs.readFileSync(filePath, 'utf8'), { json: true });
    return (parsed ?? fallback) as T;
  } catch (err: any) {
    console.warn(`[models] YAML parse failed for ${filePath}: ${err?.message || err}`);
    return fallback;
  }
}

function safeMatter(filePath: string): { data: Record<string, any>; content: string } {
  const text = fs.readFileSync(filePath, 'utf8');
  try {
    return matter(text);
  } catch (err: any) {
    console.warn(`[models] frontmatter parse failed for ${filePath}: ${err?.message || err}`);
    const m = text.match(/^---\n[\s\S]*?\n---\n?/);
    return { data: {}, content: m ? text.slice(m[0].length) : text };
  }
}

/** Parse a Newman-taxonomy verdict-count table from a review.md body. Looks for
 *  a `## Summary` markdown table; falls back to counting `**Verdict:**` lines.
 *  Mirrors auto-research's parseReviewSummary so the References tab QoL matches. */
function parseReviewSummary(body: string): ReviewSummary | undefined {
  const bucket = (raw: string): keyof Omit<ReviewSummary, 'total'> | null => {
    const x = raw.toLowerCase().trim();
    if (x.includes('consistent')) return 'consistent';
    if (x.includes('novel')) return 'novelSupporting';
    if (x.includes('merit')) return 'meritsInvestigation';
    if (x.includes('different')) return 'differentConclusion';
    if (x.includes('not relevant') || x.includes('n/a')) return 'notRelevant';
    return null;
  };
  const sum: ReviewSummary = { consistent: 0, novelSupporting: 0, meritsInvestigation: 0, differentConclusion: 0, notRelevant: 0, total: 0 };
  let found = false;
  const rowRe = /\|\s*([A-Za-z/ ]+?)\s*\|\s*(\d+)\s*\|/g;
  let m: RegExpExecArray | null;
  while ((m = rowRe.exec(body))) {
    const k = bucket(m[1]);
    if (k) { sum[k] += parseInt(m[2], 10) || 0; found = true; }
  }
  if (!found) {
    const verdicts = body.match(/\*\*Verdict:\*\*\s*([A-Za-z/ ]+)/g) || [];
    for (const v of verdicts) { const k = bucket(v.replace(/\*\*Verdict:\*\*/, '')); if (k) { sum[k] += 1; found = true; } }
  }
  if (!found) return undefined;
  sum.total = sum.consistent + sum.novelSupporting + sum.meritsInvestigation + sum.differentConclusion + sum.notRelevant;
  return sum.total > 0 ? sum : undefined;
}

export function listModelSlugs(): string[] {
  if (!fs.existsSync(MODELS_DIR)) return [];
  return fs
    .readdirSync(MODELS_DIR, { withFileTypes: true })
    .filter((e) => e.isDirectory() && !e.name.startsWith('.'))
    .filter((e) => fs.existsSync(path.join(MODELS_DIR, e.name, 'model.yaml')))
    .map((e) => e.name);
}

export function loadModel(slug: string): Model {
  const dir = path.join(MODELS_DIR, slug);
  const meta = safeYamlLoad<ModelMeta>(path.join(dir, 'model.yaml'), { slug, product: slug, status: 'scaffold' } as ModelMeta);
  meta.slug = meta.slug || slug;

  const flow = safeYamlLoad<{ unit?: string; nodes: FlowNode[]; edges: FlowEdge[] }>(
    path.join(dir, 'flow.yaml'),
    { nodes: [], edges: [] },
  );
  flow.nodes = Array.isArray(flow.nodes) ? flow.nodes : [];
  flow.edges = Array.isArray(flow.edges) ? flow.edges : [];

  const entities = safeYamlLoad<Record<string, Entity>>(path.join(dir, 'entities.yaml'), {});
  for (const [id, e] of Object.entries(entities)) (e as Entity).id = id;

  const inputs = safeYamlLoad<InputItem[]>(path.join(dir, '01-inputs/inputs.yaml'), []);
  const idiotIndex = safeYamlLoad<IdiotRow[]>(path.join(dir, 'idiot-index.yaml'), []);
  const energeticIndex = safeYamlLoad<EnergeticRow[]>(path.join(dir, 'energetic-index.yaml'), []);
  const glossary = safeYamlLoad<GlossaryEntry[]>(path.join(dir, 'glossary.yaml'), []);

  // Companies: 02-companies/{slug}/dossier.md
  const companies: CompanyDossier[] = [];
  const compDir = path.join(dir, '02-companies');
  if (fs.existsSync(compDir)) {
    for (const entry of fs.readdirSync(compDir, { withFileTypes: true })) {
      if (!entry.isDirectory()) continue;
      const dossierPath = path.join(compDir, entry.name, 'dossier.md');
      if (!fs.existsSync(dossierPath)) continue;
      const parsed = safeMatter(dossierPath);
      const d = parsed.data as any;
      companies.push({
        slug: entry.name,
        name: d.name || entry.name,
        url: d.url,
        role: d.role,
        location: d.location,
        tier: typeof d.tier === 'string' ? d.tier.toUpperCase() : undefined,
        scaffold: d.scaffold === true,
        body: parsed.content,
      });
    }
    companies.sort((a, b) => a.name.localeCompare(b.name));
  }

  // Sources: model-level shared registry sources/{slug}/extract.md
  const sources: ModelSource[] = [];
  const srcDir = path.join(dir, 'sources');
  if (fs.existsSync(srcDir)) {
    for (const entry of fs.readdirSync(srcDir, { withFileTypes: true })) {
      if (!entry.isDirectory()) continue;
      const extractPath = path.join(srcDir, entry.name, 'extract.md');
      if (!fs.existsSync(extractPath)) continue;
      const parsed = safeMatter(extractPath);
      const d = parsed.data as any;
      const reviewPath = path.join(srcDir, entry.name, 'review.md');
      let reviewed = false;
      let reviewSummary: ReviewSummary | undefined;
      if (fs.existsSync(reviewPath)) {
        reviewed = true;
        reviewSummary = parseReviewSummary(safeMatter(reviewPath).content);
      }
      sources.push({
        slug: entry.name,
        title: d.title,
        url: d.url,
        authors: Array.isArray(d.authors) ? d.authors : undefined,
        year: d.year,
        type: d.type,
        tier: typeof d.tier === 'string' ? d.tier.toUpperCase() : undefined,
        topics: Array.isArray(d.topics) ? d.topics : undefined,
        scaffold: d.scaffold === true,
        reviewed,
        reviewSummary,
        body: parsed.content,
      });
    }
    sources.sort((a, b) => (a.title || a.slug).localeCompare(b.title || b.slug));
  }

  const market = safeYamlLoad<MarketData | null>(path.join(dir, 'market.yaml'), null);
  if (market && !Array.isArray(market.series)) market.series = [];
  if (market && !Array.isArray(market.stats)) market.stats = [];

  return { slug, meta, flow, entities, inputs, idiotIndex, energeticIndex, companies, sources, glossary, market };
}

export function loadAllModels(): Model[] {
  return listModelSlugs().map(loadModel);
}

/** Build a d3-sankey payload from the flow graph. Ribbon weight = value_usd.
 *  Resolves each node's entity URL so nodes are click-through. */
export function buildSankeyPayload(model: Model) {
  const nodes = model.flow.nodes.map((n) => {
    const e = n.entity ? model.entities[n.entity] : undefined;
    const link = entityLink(model, n.entity);
    return {
      id: n.id,
      label: n.label,
      stage: n.stage || '',
      entity: n.entity || '',
      entityName: e?.name || '',
      revenue: e?.revenue_usd ?? null,
      revenueNote: e?.revenue_note || '',
      href: link?.href || '',          // dossier (internal) if it exists, else external url
      external: link?.external ?? true,
    };
  });
  const known = new Set(nodes.map((n) => n.id));
  const links = model.flow.edges
    .filter((e) => known.has(e.from) && known.has(e.to))
    .map((e) => ({
      source: e.from,
      target: e.to,
      value: typeof e.value_usd === 'number' && e.value_usd > 0 ? e.value_usd : 1,
      valueUsd: e.value_usd ?? null,
      throughput: e.throughput || '',
      energyMj: e.energy_mj ?? null,
      cited: !!e.evidence?.source,
      sourceSlug: e.evidence?.source || '',
      note: e.evidence?.note || '',
    }));
  return { nodes, links };
}

export function entityFor(model: Model, id?: string): Entity | undefined {
  return id ? model.entities[id] : undefined;
}
