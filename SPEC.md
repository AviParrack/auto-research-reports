---
name: Auto-Research
status: spec
inspired-by: Steve Newman's Centaur Era report on orbital data centers
---

# Auto-Research — Spec

A multi-pass, multi-model research engine that builds living explorable reports. Born from reverse-engineering Newman's auto-research after the Centaur Era post. The thesis:

> **Newman's failure mode is paragraph-by-paragraph narrative without cross-section logic. The fix is structural, not exhortative: a claim graph as the substrate, a typed question DAG, first-principles calculation that doesn't trust sources by default, point-by-point source reviews against every major figure, dual-model tag teams at every writing step, and a fully traceable git-committed pass log.**

If P2 (first-principles calc) and P3 (source reconciliation) are nailed, you eat Newman's lunch even with a simpler tree.

---

## Core Concepts

### The Pass
A **pass** is one re-entrant walk through the report's current state. Passes have a `focus` (intake | tree | leaf | source-review | consistency | synthesis | audit) and can target specific leaves or sources. Passes never blow away prior work — they read current state, write new artifacts, update indices, commit, and (in cloudflare mode) push.

**The skill is the engine. The user is the conductor.** Between passes the user can:
- Delete drifted questions
- Seed new questions or guidance for the next pass
- Resolve flagged contradictions
- Approve depth-N+ tree expansions

The engine runs each pass; the user punctuates with judgement.

### The Tag Team
Every writing step is a Claude→GPT loop:
1. **Claude proposes** (writes the artifact)
2. **GPT critiques** (writes `audit-claude.md` alongside, claim-keyed)
3. **Claude responds** (updates artifact or rebuts, claim-by-claim)
4. **Unresolved disagreements** flagged for the user

If GPT unreachable → flag in metadata, continue, mark audits as `unaudited`. Never blocks.

### The Tree
A typed DAG, not a flat list. Node types:
- **Root** — the original question
- **Leaf** — atomic factual sub-question; answered with a leaf report
- **Synthesis** — combines leaves into intermediate conclusion
- **Constraint** — structural blocker (Newman's "Side Chapters")

Tree grows mid-pass: agents propose new nodes; one level of autonomous expansion; deeper requires the user's explicit gate.

### Termination
A leaf is done when (1) the leaf question has an answer with ≥3 cited supports, and (2) every cited source has a Source Review tagging its position vs the leaf's answer.

A report is done when (1) the root question has an answer, and (2) every major public figure on the topic has a Source Review on file.

This is Newman's twin-predicate, encoded.

---

## Deploy modes

Auto-Research supports two deployment modes. The skill prompts at intake; the choice persists in `meta.yaml.deploy.mode`. Both modes render every report on the same site at `/{slug}/`.

| Mode | What happens after each pass | When to use |
|---|---|---|
| **`cloudflare`** | `git add + commit + push` to the origin remote. Cloudflare Pages auto-rebuilds. Site lives at your custom domain or `*.pages.dev`. | Public sharing, multi-device access, default for a forked/cloned repo with a Cloudflare project attached. |
| **`local`** | `git add + commit` (no push). `scripts/serve-local.sh` builds the static site and serves it at `http://localhost:4321/`. Opens the report URL automatically. | Private research, no public surface, offline work, no GitHub/Cloudflare required. |

A single repo can mix modes per-report. The site code is identical; only the deploy step differs.

---

## Folder Structure

```
auto-research-reports/                # repo root
  SPEC.md                             # this file
  CLAUDE.md                           # orientation for any Claude agent in this repo
  INSTALL.md                          # how to wire the skill into Claude Code
  README.md                           # user-facing intro

  skill/                              # the Claude Code skill (ships with repo)
    SKILL.md                          # the orchestrator
    references/                       # one file per pass type + protocol + schemas

  scripts/
    ask-gpt.py                        # Claude→GPT bridge (Codex CLI + OpenAI API fallback)
    new-report.py                     # scaffolds a fresh report folder
    deploy.sh                         # mode-aware commit + push/serve
    serve-local.sh                    # build site + serve on localhost (local mode)

  site/                               # Astro app — reads from reports/, generates static HTML
    src/pages/[report]/index.astro    # dynamic per-report routing

  reports/{slug}/                     # data — one folder per report
    meta.yaml                         # current state, pass count, model versions, deploy config
    00-intake/
      question.md                     # the original root question
      seed-sources/                   # anything seeded at start

    01-tree/
      tree.yaml                       # canonical question DAG (current)
      history/v{N}.yaml               # every snapshot with diff + reason
      growth-log.md                   # human-readable: who added what, why

    02-leaves/{leaf-slug}/
      leaf.yaml                       # question, status, required-passes status
      claims.yaml                     # claim graph: id, text, evidence, confidence, audit
      passes/
        pass-{NN}-{kind}.md           # research / calc / reconcile / source-review / consistency / write
        pass-{NN}-audit.md            # GPT critique of corresponding Claude pass
      sources/{source-slug}/
        extract.md                    # structured notes from this source
        review.md                     # point-by-point Source Review
      notes/                          # user comments, claim-keyed

    03-synthesis/v{N}/
      claude-v1.md                    # Claude writes from current state (isolated)
      gpt-v1.md                       # GPT writes from same (isolated)
      diff.md                         # style-vs-substance triage
      debate.md                       # if substantive disagreement
      consensus.md                    # extracted agreement points
      claude-v2.md                    # Claude rewrites from consensus
      gpt-v2.md                       # GPT rewrites from consensus

    feedback.md                       # user's run-level notes (fed into next run)
    pass-log.jsonl                    # one line per pass; full audit trail
```

---

## Primitives (file schemas)

### `meta.yaml`
```yaml
slug: orbital-data-centers
root_question: "When does orbital AI compute reach parity with terrestrial?"
status: in_progress
current_pass: 7
created: 2026-05-25
last_updated: 2026-05-26T03:14:00Z
models:
  primary: claude-opus-4-7
  critic: gpt-5-pro
deploy:
  mode: cloudflare | local            # required — set at intake
  cloudflare_project: orbital-data-centers   # only when mode=cloudflare
  url: https://orbital-data-centers.example.com   # set after first deploy
  last_deploy: 2026-05-26T03:14:00Z
termination:
  root_answered: false
  all_figures_reviewed: false
```

### `tree.yaml`
```yaml
root:
  id: root
  question: "..."
  answer: null
  status: open

nodes:
  - id: q1
    parent: root
    depth: 1
    type: leaf | synthesis | constraint
    question: "..."
    status: open | researching | answered | deprecated
    answer: "..."           # one-line current best answer
    confidence: high | medium | low | speculative
    leaf_path: 02-leaves/q1-gpu-life/
    created_by: agent | user
    created_pass: 3
    last_touched_pass: 7
    children: [q1.1, q1.2]
    flags: [needs_human_gate, drifted, contested]
```

### `leaf.yaml`
```yaml
id: q1-gpu-life
question: "..."
status: drafting | reviewed | done
claims_file: claims.yaml
passes_status:
  research: done
  calc: done
  reconcile: needs_rerun
  source-review: in_progress
  consistency: pending
  write: pending
last_pass: 5
contradictions_with: [q3-thermal]   # set by consistency pass
```

### `claims.yaml`
```yaml
- id: q1.c1
  text: "Orbital GPU permanent failure rate is 4-7%/year."
  type: factual | derived | estimate
  evidence:
    - source: nasa-iss-electronics-2023
      ref: section-4-table-2
      verdict: supports
    - source: patel-2024-ai-bottlenecks
      ref: para-12
      verdict: contradicts        # disagreement is data, not a bug
  confidence: medium
  derivation_path: passes/pass-02-calc.md   # only if type: derived
  audit:
    gpt:
      status: passed | flagged | unaudited
      audit_file: passes/pass-04-audit.md
      notes: "GPT flagged: NASA paper is for ISS racks, not orbital GPUs"
    human:
      status: noted | unnoted
      comment_file: notes/user-2026-05-26.md
```

### `pass-NN-audit.md` (Codex critique)

Each `pass-NN-{kind}.md` written by Claude has a sibling `pass-NN-{kind}-audit.md` written by Codex (or `pass-{kind}-audit.md` for the `write` kind). Site renders these as verdict-card threads in the Pass Log conversation view.

**Forward standard (use for all new audits):**

Body begins with `[codex cli ok]` header line, optionally followed by a ` ```yaml ... ``` ` fence (both stripped before parsing). The payload is YAML:

```yaml
overall:
  verdict: pass | pass_with_caveat | weak | contradicted | fail
  summary: "1-2 sentence headline."

findings:
  - target: "c1"                 # claim id, section name, or topic slug
    target_kind: claim | section | topic
    verdict: supports | partial | weak | unsupported | contradicted | pass | fail
    quote: "..."                 # optional verbatim from audited artifact
    reason: "..."                # 1-3 sentence reasoning
    severity: low | medium | high   # optional

notes:                            # optional cross-cutting issues (severity-tagged)
  - issue: "..."
    severity: low | medium | high
```

**Legacy shapes the renderer tolerates:**

- **A — claims array:** `claims: [{id, verdict, quote, reason}, ...]` — each entry rendered as a claim card.
- **B — section-verdict strings + flat notes:** top-level `key: verdict-string` pairs plus a flat `notes: [{issue, severity}]` array.
- **C — topic-keyed claims map:** `claims: { topic_slug: {verdict, notes}, ... }` plus top-level sibling sections.
- **D — key→array-of-strings:** top-level `key: [string, string, ...]` shape, rendered as labeled bullet block.

The renderer parses with `js-yaml`, walks the tree, and emits adaptive finding cards. **Consistency-check passes (`pass-NN-consistency.md`) are not audits** — they are Claude's own cross-leaf prose and render as plain markdown.

### `pass-NN-response.md` (Claude rebuttal)

Sibling of every audit. Claude reads the Codex audit and responds point-by-point. The renderer aggregates accept/dispute tallies per pass — they drive the lower bar on each pass-log entry.

**Convention:** use `## Accepted` and `## Disputed` H2 headings. One bullet per finding inside each section. Parenthetical suffixes on the heading are fine.

```markdown
## Accepted (will downgrade)

- **claim-id (verdict): "..."** — short reasoning + what changes.

## Disputed / clarified

- **claim-id**: why Codex's critique misreads the claim, with the clarification.
```

Synonyms the renderer also recognises: `## Conceded` → accept, `## Rejected` / `## Rebutted` → dispute. Other H2 headings (`## Confirmed`, `## What to carry forward`, `## Updated stance`) are informational and not counted.

**Render:** the log page builds two stacked bars per pass — a verdict bar (Codex tallies) on top, an accept/dispute bar (Claude actions) below. Text strip underneath: `codex: ✓N ~N ✗N | claude: ↻N acc · ⇄N disp`.

### Source tier hierarchy (canonical)

Every source gathered in the research sub-pass gets tier-assigned at gather time. Review depth, volume targets, and site rendering all key off the tier. Canonical definitions live in [`skill/references/source-tiers.md`](skill/references/source-tiers.md); per-tier `review.md` schemas in [`skill/references/schemas.md`](skill/references/schemas.md).

| Tier | What | Review depth | Volume target |
|---|---|---|---|
| **S** | Peer-reviewed primary papers; foundational papers; gov tech reports; field-central books | Full claim-by-claim review | 10-50+ (read all relevant) |
| **A** | Peer-reviewed reviews + meta-analyses; major conference proceedings; credentialed-group preprints | Medium review (key claims + verdict) | 10-30 |
| **B** | **Public figures** (politicians, tech execs, founders, prominent commentators) | Quote/claim review per figure | 5-20 figures × 1-5 quotes |
| **C** | Industry trade press; expert blogs/Substacks; podcasts; corporate white papers | Scalar verdict + one paragraph | 3-15 |
| **D** | Mainstream press; non-public-figure social media | Scalar verdict + flag if conflicts higher tier | 3-15 |
| **E** | Wikipedia; derivative summaries; orientation reads | Not reviewed; not stored under `sources/` | As needed |

**Extract schema (context-overload mitigation):** `sources/{slug}/extract.md` body is `## Abstract` (150-300 words) + `## Key claims` (3-7 anchored bullets) + `## Reviewer notes` (50-150 words) — not raw full text. Optional `raw.md` alongside for tier S/A only.

### Cross-consistency pass

When 2+ leaves run concurrently, each leaf's sub-pass 5 only sees siblings that were `reviewed` at *its* start time — contradictions between simultaneously-running siblings go unflagged. Solution: a `--pass cross-consistency` invocation that runs after any parallel batch and scans claim-graph contradictions across all reviewed leaves. Lightweight (claims-only, no full prose), Codex-audited, writes `01-tree/cross-consistency-pNN.md`. Spec in [`skill/references/pass-leaf.md`](skill/references/pass-leaf.md).

### `pass-log.jsonl`
```jsonl
{"pass_id":"p001","focus":"intake","started":"2026-05-25T20:00:00Z","ended":"2026-05-25T20:18:00Z","models":["claude"],"outcome":"tree v1 created with 8 leaves","commit":"a3f8c2"}
{"pass_id":"p002","focus":"leaf:q1-gpu-life","kinds":["research","calc"],"models":["claude","gpt"],"outcome":"5 claims added, 1 flagged by GPT","commit":"b7d4e1"}
```

### Source Review verdict taxonomy

Fixed verdicts borrowed from Newman:
- **Consistent** — agrees with our analysis
- **Different conclusion** — we considered, disagree, here's why
- **Novel** — new info we hadn't used; integrate
- **Merits investigation** — flag, possibly spawns a tree node
- **Not relevant** — out of scope

Summary table at top with category counts. Each claim quoted verbatim, verdict-tagged, linked to internal leaf claims.

---

## Pass Types

### P0. Intake (once)
- User provides root question + optional seed sources
- Skill prompts for deploy mode (cloudflare | local)
- Initial scoping research (web search, training knowledge survey)
- Tree v1 generated (5-10 leaves typical)
- Site skeleton scaffolded
- First commit + deploy (cloudflare push OR local build+serve)
- **Site is live in <15 minutes** with question, tree, empty-state leaf pages

### P1. Tree (re-runnable)
- For each open leaf: is it well-formed? Does it feed the root?
- Propose new sub-questions (autonomous depth+1, user gate beyond)
- Flag drifted Qs for user to delete
- Updates tree.yaml, snapshots to history/
- Commits + redeploys

### P2. Leaf (re-runnable per leaf, parallelizable across leaves)
Six sub-passes, executed in order; each can re-run independently:
1. **research** — gather candidate sources; web search + extract
2. **calc** — first-principles derivation, sources sealed (no peeking)
3. **reconcile** — compare calc vs sources; disagreements → flagged
4. **source-review** — per source, point-by-point with verdict taxonomy
5. **consistency** — claim graph for this leaf checked against sibling leaves
6. **write** — leaf report, rendered from claims.yaml

Each sub-pass is a Claude+GPT tag team. claims.yaml updated incrementally.

### P3. Source Review (re-runnable per source)
For each major public figure / source on the topic, spawn full Source Review. Run automatically for every source cited; run explicitly on user's request for figures not yet cited (the steelman trawl).

### P4. Consistency (re-runnable)
Cross-leaf adversarial pass. Extracts all claims across all leaves, groups by topic, flags contradictions. Generates required-resolution list — surfaced to user via flagged gates or routed back as new tree nodes.

### P5. Synthesis (re-runnable)
1. Claude writes claude-v1 from current state (no GPT peek)
2. GPT writes gpt-v1 from current state (no Claude peek)
3. Diff agent triages: style differences vs substantive disagreements
4. **If only style:** publish both, no debate
5. **If substance:** invoke debate flow → debate.md → consensus.md
6. Claude writes claude-v2 from consensus
7. GPT writes gpt-v2 from consensus

Tab-switch on the site: claude-v2 / gpt-v2 / debate-transcript / claude-v1 / gpt-v1 (older).

### P6. Audit (re-runnable, mandatory before declaring done)
- Walk every claim, check evidence still resolves
- Walk every source URL, verify reachable
- Re-derive every calc independently
- GPT does adversarial pass on whole report
- Output audit-{N}.md with claim-keyed flags
- Updates audit status in claims.yaml

---

## The Live Webpage

**Astro + MDX + Tailwind.** Renders the same way in both deploy modes:
- React components for the structural pieces (tree nav, tabs, margin footnotes, audit overlay)
- MDX so leaves can embed structured tables + calc code blocks
- Pagefind for client-side search

**Rendered pages (per report at `/{slug}/`):**
- `/{slug}/` — root question, answer (latest), tree-as-nav, pass timeline scrubber
- `/{slug}/tree` — the DAG visualized
- `/{slug}/leaves/{leaf}` — leaf report, with claims annotated by audit status
- `/{slug}/sources/{source}` — source review with verdict table
- `/{slug}/synthesis` — tab-switch between Claude-v2 / GPT-v2 / debate / older versions
- `/{slug}/audit` — claim-keyed audit dashboard
- `/{slug}/log` — pass-log timeline

The root `/` page lists every report in `reports/`.

**Margin footnotes (the tracing UI):**
Each claim gets a margin annotation with:
- audited & passed
- audited & flagged
- unaudited
- has user comment
- Hover/click → expand to show GPT audit text + human comment thread + commit link

Sources, audits, and human comments are all just markdown files in the report folder; the site reads them.

**Deploy rhythm:**

| Mode | Per-pass behaviour |
|---|---|
| `cloudflare` | Commit + push. Cloudflare Pages auto-rebuilds. ~30s from commit to live. |
| `local` | Commit (no push). `serve-local.sh` rebuilds `site/dist/` and serves on `localhost:4321`. Browser auto-refresh on next page load. |

---

## Anti-Patterns (the things you are explicitly designing against)

From Newman's footnote 11 + general LLM failure modes:

1. **Narrative over logic.** Countered by: claims.yaml as substrate, prose rendered from it; cross-leaf consistency pass.
2. **Source borrowing in calculations.** Countered by: P2 calc runs with sources sealed; only P3 reconciles.
3. **Single-model echo chamber.** Countered by: Claude+GPT tag team at every writing step.
4. **Hidden inconsistencies between sections.** Countered by: P4 consistency pass; claim-keyed extraction.
5. **Hallucinated sources.** Countered by: every source URL fetched and stored as extract.md before citation allowed.
6. **Drift from root question.** Countered by: termination predicate explicitly checks tree relevance.
7. **Mechanical academic register.** Countered by: explicit anti-pattern grep before save.
8. **Over-hedging.** Countered by: confidence levels are categorical (high/medium/low/speculative), not weasel words.
9. **Bury-the-lead synthesis.** Countered by: synthesis must lead with answer in first 200 words.
10. **Resistance to correction.** Countered by: human comments are first-class artifacts; passes are required to read `notes/` before re-writing.
11. **Naive calendar-year timelines.** Countered by: decompose work-remaining + acceleration sensitivity rather than "by 2040" framings.
12. **Answer-first without motivation.** Countered by: leaf writes open with why-this-matters + where-it-fits before the headline.
13. **Editorial / news-headline voice.** Countered by: maximal-rigor declarative register; quantitative substitution for editorialising verbs.

Full anti-pattern reference: [`skill/references/anti-patterns.md`](skill/references/anti-patterns.md).

---

## Privacy

Anything in a `notes/private/` subfolder is gitignored. Anything marked `private: true` in frontmatter is stripped before commits in cloudflare mode. In local mode there is no public surface — privacy concerns are moot since nothing leaves the machine.
