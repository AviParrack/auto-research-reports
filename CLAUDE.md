# Claude — read this first

You're in the `auto-research-reports` repo. This file orients you when a user opens this repo in Claude Code (or any other Claude-driven environment) and asks for help.

## What this repo is

A re-runnable, multi-pass research engine. The user describes a research question; you build a structured report folder (claim graph, source reviews, dual-model synthesis), one pass at a time, with the report rendered as a live webpage. The engine ships with the skill that drives it.

The full design lives in [`SPEC.md`](SPEC.md). Read that first if you're going to do anything substantive.

## The skill

The Claude Code skill that orchestrates everything lives at [`skill/SKILL.md`](skill/SKILL.md). Its pass-specific procedures live in [`skill/references/`](skill/references/).

**If the user has installed the skill** (see [`INSTALL.md`](INSTALL.md) — symlinks `skill/` into `~/.claude/skills/auto-research/`), they can invoke it directly with `/auto-research --pass intake` or by saying "start an auto-research report on X."

**If they haven't installed it,** you can still drive the workflow manually. Just:
1. Read [`skill/SKILL.md`](skill/SKILL.md) for the orchestrator's workflow.
2. Read the relevant [`skill/references/pass-{kind}.md`](skill/references/) for the pass type they want to run.
3. Execute the procedure step-by-step.

The skill body and references are the spec for how the engine behaves. Everything below is shortcut orientation so you don't have to read everything before doing useful work.

## What to do when the user asks for something

| User says | You do |
|---|---|
| "Start a new auto-research report on X" | Read [`skill/references/pass-intake.md`](skill/references/pass-intake.md). Run the intake pass. Confirm deploy mode (cloudflare or local) before scaffolding. |
| "Run a pass on report Y" | Read the report's `reports/Y/meta.yaml`. Ask which pass type. Read the relevant `skill/references/pass-{kind}.md`. Execute. |
| "Continue where we left off" | Open `reports/Y/pass-log.jsonl` (last entry) and `reports/Y/feedback.md`. Pick up from there. |
| "How does the engine work?" | Point them at [`SPEC.md`](SPEC.md) and offer a tight summary. |
| "Add my own research project" | Same as intake — `scripts/new-report.py --slug ... --question "..." --deploy-mode {cloudflare|local}`, then fill in the tree. |

## Deploy modes — read meta.yaml every time

Every report's `reports/{slug}/meta.yaml` has a `deploy.mode` field: `cloudflare` or `local`. **Always read this before running a deploy step.**

- `cloudflare` → `scripts/deploy.sh --mode cloudflare "msg"` (commit + push, Pages auto-rebuilds)
- `local` → `scripts/deploy.sh --mode local "msg"` (commit + rebuild + serve on `http://localhost:4321/`)

A single repo can mix modes per-report. Both modes render every report on the same site at `/{slug}/` — only the host differs.

If `deploy.mode` is missing on an old report (pre-this-revision), default to `cloudflare` — that matches the historical behaviour.

## Prerequisites (warn the user if missing)

- **Node 22+** for the Astro site (`node --version`)
- **Python 3** for the helper scripts
- **OpenAI Codex CLI** (`npm install -g @openai/codex` + `codex login`) OR `OPENAI_API_KEY` env var — the Claude+GPT tag team needs one of these. If both are missing, the engine continues but marks audits as `unaudited`. Tell the user.
- **For cloudflare mode only:** push access to the origin remote, and a Cloudflare Pages project pointed at this repo with build command `cd site && npm install && npm run build`, output dir `site/dist`, `NODE_VERSION=22`.
- **For local mode only:** just Node 22+ and Python 3. No internet required after the initial `npm install`.

## File layout (so you don't have to grep)

```
SPEC.md                  ← full design doc, read first for substantive work
CLAUDE.md                ← this file
INSTALL.md               ← skill installation steps
README.md                ← user-facing intro
skill/
  SKILL.md               ← the orchestrator skill
  references/            ← one file per pass type + protocol + schemas
scripts/
  ask-gpt.py             ← Claude→GPT bridge (Codex CLI / OpenAI API)
  new-report.py          ← scaffold a fresh report folder
  deploy.sh              ← mode-aware commit + push/serve
  serve-local.sh         ← build + serve on localhost (local mode)
  commit-and-deploy.sh   ← legacy cloudflare-only deploy (kept for back-compat)
site/                    ← Astro app — multi-tenant routing at /{slug}/
reports/{slug}/          ← one folder per report; data lives here
```

## Voice

There's no project-specific style guide bundled — write in the user's voice or whatever style guide they point you at. The skill's [`anti-patterns.md`](skill/references/anti-patterns.md) is universal (mechanical transitions, bury-the-lead, narrative-over-logic, etc.) and applies to all prose output.

If the user adds a `STYLE.md` at the repo root, the synthesis pass will read it as an overlay. Otherwise default to clear, declarative academic register.

## When in doubt

Read [`SPEC.md`](SPEC.md). Then read the relevant pass reference. The procedures are spelled out — follow them.
