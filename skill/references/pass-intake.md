# Pass: Intake

Run once, at report start. Generates the report folder skeleton + tree v1 + first deploy (cloudflare push or local serve).

## Inputs
- The user's stated root question (free text)
- Optional: seed sources, scope notes, time horizon
- **Deploy mode** — must be set during intake (cloudflare | local)
- Optional: existing report (if `--report` slug given and not yet created)

## Outputs
- `reports/{slug}/meta.yaml`
- `reports/{slug}/00-intake/question.md`
- `reports/{slug}/01-tree/tree.yaml` (v1, 5-10 leaves)
- `reports/{slug}/02-leaves/{leaf-id}/leaf.yaml` (stub per leaf)
- `reports/{slug}/pass-log.jsonl` (first entry)
- Commit + deploy according to chosen mode
- Brief report back: tree summary, live URL (cloudflare) or localhost URL (local), suggested next pass

## Procedure

### 1. Confirm scope with the user
Ask up to four short questions (use AskUserQuestion if available; otherwise inline prompts):
- "What's the time horizon you care about?"
- "Any specific angle or sub-question that matters most?"
- "Any seed sources you want me to start from?"
- "Deploy mode: (a) cloudflare — public, live updates on push; or (b) local — private, opens on localhost?"

Keep this lightweight. Scope can be refined in tree-pass; deploy mode is locked in here and rarely changes.

### 2. Decide the slug
Lowercase, hyphenated, ~3-5 words, captures the question. Examples: `lunar-manufacturing`, `fusion-grid-parity`, `agi-takeoff-shape`. Avoid generic words ("the", "of"). Check uniqueness against existing `reports/` subfolders.

### 3. Run initial scoping research
Use web search heavily. Goal: map the territory before tree generation. Look for:
- Who has written publicly about this topic recently (the future Source Review targets)
- What sub-questions does the literature already decompose into
- What are the obvious cruxes
- What's the state of empirical evidence

Save ~5-10 candidate sources you'd return to during leaf-passes (don't extract them now; that's a leaf-pass job).

### 4. Generate tree v1
5-10 top-level nodes. Mix of types:
- Mostly `leaf` (atomic factual questions)
- 1-2 `synthesis` nodes (the final integration questions)
- 0-2 `constraint` nodes (structural blockers — Newman's "Side Chapters")

Each node:
- Sharp question (not a topic — a question that has an answer)
- Slug-id (`q1-cost-curve`, `q2-feasibility`, etc.)
- `depth: 1`, `parent: root`, `status: open`, `created_by: agent`, `created_pass: 0`

**Tree quality checks before writing:**
- Does every node directly support answering the root? (Drift check.)
- Together, do they tile the space — could you answer the root if every leaf was answered?
- Are any two nodes really the same question phrased differently? (Merge.)
- Is anything too broad to be a leaf? (Split, or mark `synthesis`.)

### 5. Write the files

Use `scripts/new-report.py` with the `--deploy-mode` flag to scaffold the folder, then fill in the generated meta.yaml's `deploy.mode` field. Example:

```bash
python3 scripts/new-report.py \
  --slug fusion-grid-parity \
  --question "When does fusion power undercut fission for grid baseload?" \
  --deploy-mode cloudflare
```

The script creates the folder structure with the deploy mode persisted. After that:

```yaml
# reports/{slug}/meta.yaml (after enrichment)
slug: {slug}
root_question: "..."
status: in_progress
current_pass: 0
created: {today}
last_updated: {now-iso}
models:
  primary: claude-opus-4-7
  critic: gpt-5-pro
deploy:
  mode: cloudflare | local
  cloudflare_project: {slug}   # only when mode=cloudflare
termination:
  root_answered: false
  all_figures_reviewed: false
```

```markdown
# reports/{slug}/00-intake/question.md
# Root Question

**{root_question}**

## Why this question
...

## Scope notes
- Time horizon: ...
- ...

## Seed sources
- ...
```

```yaml
# reports/{slug}/01-tree/tree.yaml
root:
  id: root
  question: "..."
  answer: null
  status: open
nodes:
  - id: q1-...
    ...
```

For each leaf node, create `02-leaves/{leaf-id}/leaf.yaml` with all `passes_status: pending`.

### 6. Append first pass-log entry

```jsonl
{"pass_id":"p000","focus":"intake","kinds":["intake"],"started":"...","ended":"...","models":["claude"],"outcome":"Tree v1 created with N leaves: {summary}","commit":"...","artifacts":["meta.yaml","01-tree/tree.yaml","..."]}
```

### 7. Commit + deploy
Read `meta.yaml.deploy.mode` and run:

```bash
scripts/deploy.sh --mode <mode> "intake: {slug} — {short-description}"
```

The script:
- Always does `git add -A` and `git commit`
- In `cloudflare` mode: `git push` and reports the live URL placeholder
- In `local` mode: calls `scripts/serve-local.sh` to build `site/dist/` and start a server on `localhost:4321`; opens the report URL in the user's default browser

### 8. Report to the user
Concise format:
- **Slug:** `{slug}`
- **Live URL:** `https://{your-domain}/{slug}/` (cloudflare) or `http://localhost:4321/{slug}/` (local)
- **Tree:** {N} leaves, {summary in 1-2 lines}
- **Deploy mode:** {mode}
- **Suggested next:** `auto-research --report {slug} --pass leaf --leaf {first-leaf-id}` or `--pass tree --message "..."` if they want to refine

## Notes
- Don't try to answer anything yet. Intake is purely scaffolding.
- Don't extract sources during intake — that's leaf-pass work.
- Keep the tree narrow rather than wide. Better to add nodes in subsequent tree passes than to start bloated.
- Deploy mode is the one decision that's awkward to change later — confirm explicitly.
