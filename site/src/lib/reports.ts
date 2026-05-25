import fs from 'node:fs';
import path from 'node:path';
import yaml from 'js-yaml';
import matter from 'gray-matter';

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

export interface Leaf {
  id: string;
  question: string;
  status: 'open' | 'researching' | 'drafting' | 'reviewed' | 'done';
  passes_status: Record<string, 'pending' | 'in_progress' | 'done' | 'needs_rerun'>;
  last_pass: number;
  claims: Claim[];
  body?: string;
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
      leaves.push({ ...leafMeta, claims, body });
    }
  }

  return { slug, meta, tree, leaves };
}

export function loadAllReports(): Report[] {
  return listReportSlugs().map(loadReport);
}

export function getLeafBySlug(report: Report, leafId: string): Leaf | undefined {
  return report.leaves.find((l) => l.id === leafId);
}

export function getNodeChildren(tree: Tree, parentId: string): TreeNode[] {
  return tree.nodes.filter((n) => n.parent === parentId);
}
