import fs from 'node:fs';
import path from 'node:path';
import type { APIRoute } from 'astro';
import { listReportSlugs } from '../../../../lib/reports';

const REPORTS_DIR = path.resolve(process.cwd(), '../reports');

const MIME: Record<string, string> = {
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.webp': 'image/webp',
};

export function getStaticPaths() {
  const out: Array<{ params: { report: string; version: string; fig: string } }> = [];
  for (const slug of listReportSlugs()) {
    const synthRoot = path.join(REPORTS_DIR, slug, '03-synthesis');
    if (!fs.existsSync(synthRoot)) continue;
    for (const v of fs.readdirSync(synthRoot, { withFileTypes: true })) {
      if (!v.isDirectory() || !/^v\d+$/.test(v.name)) continue;
      const figDir = path.join(synthRoot, v.name, 'figures');
      if (!fs.existsSync(figDir)) continue;
      for (const f of fs.readdirSync(figDir)) {
        if (!/\.(png|jpg|jpeg|svg|webp)$/i.test(f)) continue;
        out.push({ params: { report: slug, version: v.name, fig: f } });
      }
    }
  }
  return out;
}

export const GET: APIRoute = ({ params }) => {
  const { report, version, fig } = params;
  if (!report || !version || !fig) return new Response('not found', { status: 404 });
  const filePath = path.join(REPORTS_DIR, report, '03-synthesis', version, 'figures', fig);
  if (!fs.existsSync(filePath)) return new Response('not found', { status: 404 });
  const ext = path.extname(fig).toLowerCase();
  const mime = MIME[ext] ?? 'application/octet-stream';
  const data = fs.readFileSync(filePath);
  return new Response(data, {
    headers: {
      'Content-Type': mime,
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
