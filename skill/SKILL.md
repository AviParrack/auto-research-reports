---
name: auto-research
description: "Multi-pass agentic research engine. Builds living explorable reports across re-runnable passes. Use when the user says 'auto-research', '/auto-research', 'run a pass', 'start a new report', or wants to build a structured multi-pass research report with question DAG, claim graphs, source reviews, and Claude+GPT dual-model synthesis. Defeats Newman's narrative-over-logic failure mode through claim-graph substrate, first-principles calc that doesn't trust sources by default, point-by-point source reviews against major figures, and tag-team writing at every step."
argument-hint: "[--report SLUG] [--pass intake|tree|leaf|source-review|consistency|synthesis|audit] [--leaf SLUG] [--message TEXT]"
metadata:
  version: 1.0.0
  spec: SPEC.md
---

# Auto-Research

A re-runnable, multi-pass research engine. The engine reads the current state of a report, runs one focused pass over it, commits, deploys (cloudflare push OR localhost rebuild), and exits. The user punctuates passes with judgement — deleting drifted questions, seeding new ones, resolving flagged contradictions.

**Read the spec first:** [`SPEC.md`](../SPEC.md) at the repo root. It defines the data primitives, pass types, and anti-patterns. This skill operationalizes that spec.

## Where everything lives

This skill ships *inside* the `auto-research-reports` repo. All paths in this file are repo-relative.

- **Spec:** `SPEC.md` (repo root)
- **Skill body:** `skill/SKILL.md` (this file) + `skill/references/`
- **Site code:** `site/` (Astro)
- **Reports:** `reports/{slug}/`
- **Scripts:** `scripts/`

If the skill is installed at `~/.claude/skills/auto-research/` (symlinked or copied), repo-relative paths resolve via the user's current working directory — every pass should start with the user in the repo root.

## Deploy modes (read at intake; persist in meta.yaml)

| `deploy.mode` | What the post-pass step does |
|---|---|
| `cloudflare` | `scripts/deploy.sh --mode cloudflare "msg"` → git add, commit, push. Cloudflare Pages auto-rebuilds. Requires push access to the origin remote. |
| `local` | `scripts/deploy.sh --mode local "msg"` → git add, commit (no push). Calls `scripts/serve-local.sh` to rebuild `site/dist/` and serve on `http://localhost:4321/`. Browser auto-opens the report page. |

The `mode` is set during intake and read from `reports/{slug}/meta.yaml` on every subsequent pass. A single repo can mix modes per report.

## Workflow — every invocation

1. **Parse arguments.** Expect `--report SLUG --pass KIND [--leaf SLUG] [--message TEXT]`.
   - If `--report` is missing and only one report exists, default to it.
   - If `--pass` is missing, ask the user which pass to run (or infer from context).
2. **Read state.** Open `reports/{slug}/meta.yaml`, `01-tree/tree.yaml`, and any relevant leaf/synthesis files. Read `feedback.md` and `notes/` — prior user comments are first-class input.
3. **Pre-pass hooks.** Read the relevant `references/pass-{kind}.md` for the pass type. That file is the procedure.
4. **Execute pass.** Following the pass-specific reference, do the work. All writing follows `references/claude-gpt-protocol.md` (Claude writes → GPT critiques → Claude responds). All output guards against `references/anti-patterns.md`.
5. **Update indices.** Bump `meta.yaml:current_pass`, update `last_updated`, update affected leaf statuses, update tree node `last_touched_pass`.
6. **Append to pass-log.jsonl.** One line: pass_id, focus, kinds, started, ended, models, outcome, commit-hash-placeholder.
7. **Commit + deploy.** Read `meta.yaml.deploy.mode` and call `scripts/deploy.sh --mode <mode> "<message>"`. The script handles both cloudflare-push and local-serve.
8. **Report back to the user.** Concise summary: what changed, what's flagged, what to run next. Include the live URL (cloudflare) or localhost URL (local).

## Pass dispatch

| `--pass` value | Reference file | When |
|---|---|---|
| `intake` | `references/pass-intake.md` | Once, at report start |
| `tree` | `references/pass-tree.md` | Refine tree, propose new nodes, prune drifted |
| `leaf` | `references/pass-leaf.md` | Full pipeline on one leaf (research → write) |
| `source-review` | `references/pass-other.md` | Per-figure point-by-point review (the steelman trawl) |
| `consistency` | `references/pass-other.md` | Cross-leaf adversarial claim check |
| `cross-consistency` | `references/pass-leaf.md` | Post-parallel-batch contradiction scan |
| `synthesis` | `references/pass-synthesis.md` | Claude+GPT dual reports + debate + consensus |
| `audit` | `references/pass-other.md` | Walk every claim, every source, every calc |

Each reference file is self-contained — read only the one(s) you need for the current pass.

## The Claude+GPT tag team contract

Claude is the orchestrator. Codex/GPT is a tool Claude calls for adversarial critique at each writing step. See `references/claude-gpt-protocol.md` for the full protocol. Short version:
1. Claude writes the artifact (e.g., a calc pass file).
2. Claude invokes **`scripts/ask-gpt.py`** which calls the **OpenAI Codex CLI** (`codex exec`) — bills against the user's ChatGPT subscription if logged in. Falls back to OpenAI API (`OPENAI_API_KEY`) only if Codex CLI is unavailable.
3. Save the critique to `pass-{NN}-audit.md` alongside the artifact.
4. Claude reads the audit, responds claim-by-claim — either updates the artifact or rebuts in the response file.
5. Unresolved disagreements → flag for the user.

If GPT unreachable (Codex CLI not installed AND no API key) → flag in `meta.yaml.gpt_outages[]`, mark new claims `audit.gpt.status: unaudited`, continue. Never block.

## Anti-patterns (always check before commit)

Read `references/anti-patterns.md` before each pass. The listed structural countermeasures defeat Newman's narrative-over-logic failure mode. Most important:

- **Claims live in `claims.yaml`, prose is rendered from them.** Never let prose introduce a claim not in the graph.
- **P2 calc seals sources.** First-principles only.
- **Every cited source has an `extract.md` before it can appear as evidence.** No hallucinated citations.
- **Cross-leaf consistency pass is mandatory before synthesis.** Inconsistencies are required-resolution items, not stylistic problems.
- **Confidence levels are categorical** (high/medium/low/speculative). No weasel words.

## Termination criteria (when to stop running passes)

From the spec — Newman's twin predicate:
- **Leaf done:** answer has ≥3 cited supports AND every cited source has a Source Review on file.
- **Report done:** root has an answer AND every major public figure on the topic has a Source Review.

These are mechanical checks. Compute them at the end of each pass and update `meta.yaml.termination`.

## Examples

### Starting a new report
```
User: "auto-research --pass intake. Topic: when will fusion power be cheaper than fission for grid baseload"
```
- Skill: read `references/pass-intake.md`
- Prompt the user briefly for: scope notes, time horizon, seed sources, **deploy mode**
- Generate slug, scaffold `reports/{slug}/` folder, write meta.yaml + question.md
- Run scoping research (web search), produce tree v1 (5-10 leaves)
- Commit + deploy according to chosen mode
- Report: "Tree v1 created with 7 leaves. Site live at {url}. Suggested next: run `--pass leaf --leaf q1-...`"

### Running a leaf
```
User: "auto-research --report lunar-manufacturing --pass leaf --leaf q1-bulk-mass-cost"
```
- Skill: read `references/pass-leaf.md`
- Execute six sub-passes in order (research, calc, reconcile, source-review, consistency, write), each with Claude+GPT tag team
- Update claims.yaml, leaf.yaml, render leaf report
- Commit + deploy per sub-pass (six commits, six site rebuilds)
- Report: "Leaf done. 12 claims, 8 cited sources reviewed. 1 contradiction with q2 leaf — flagged for consistency pass."

### User seeds guidance between passes
```
User: "auto-research --report lunar-manufacturing --pass tree --message 'I think we're missing the political economy of who controls lunar resources. Add that branch.'"
```
- Skill: read `references/pass-tree.md`
- Inject the user's guidance, propose new tree nodes, write to growth-log.md, update tree.yaml
- Commit + deploy

## Troubleshooting

- **GPT unreachable:** Check `OPENAI_API_KEY` env var or run `codex login`. Skill continues with audits marked `unaudited`.
- **Push fails (cloudflare mode):** Check `gh auth status`. Auth issues won't block local commits — re-push later.
- **Cloudflare not deploying:** Confirm GitHub → Cloudflare Pages connection in Cloudflare dashboard. Build settings: root blank, build command `cd site && npm install && npm run build`, output dir `site/dist`, `NODE_VERSION=22`.
- **Local server not starting:** Check `node --version` (need 22+). Run `cd site && npm install` once before first pass.
- **Local port in use:** `serve-local.sh` defaults to `4321`. Override with `AUTO_RESEARCH_PORT=5173 scripts/serve-local.sh ...`.
- **Tree drift:** If passes keep adding tangential branches, run `--pass tree --message "tighten to root question, prune anything not directly cited in synthesis"`.
