# Pass: Leaf

Full pipeline on one leaf node. Six sub-passes in order; each can re-run independently. Each writing sub-pass goes through Claude+GPT tag team (see `claude-gpt-protocol.md`).

## Inputs
- `--report SLUG --leaf LEAF-ID`
- The leaf's current `leaf.yaml`, `claims.yaml` (if exists), and `passes/*.md`
- The leaf's question from `tree.yaml`
- Optional `--message TEXT` — the user's guidance for this pass
- Sibling leaves (read for cross-leaf awareness, but don't write to them)

## Outputs (per sub-pass)
- New file in `02-leaves/{leaf-id}/passes/pass-NN-{kind}.md`
- Sibling audit file from GPT: `passes/pass-NN-audit.md`
- Updated `claims.yaml` (incremental)
- Updated `leaf.yaml` status fields
- Commit + deploy per sub-pass (six commits per full leaf run; deploy mode read from meta.yaml)

## Sub-pass order

### 1. research
**Goal:** Build a tiered, topic-tagged corpus of sources. Don't claim anything yet. **This is the heaviest sub-pass.**

- Read `00-intake/question.md` and `01-tree/tree.yaml` for context
- Read sibling leaves' titles (one-liner each) for awareness, but DO NOT read their content (avoid contamination)
- Gather sources across the tier hierarchy (see [`source-tiers.md`](source-tiers.md) for full definitions and volume targets):
  - **Tier S** (peer-reviewed primary, foundational papers, gov tech reports, field-central books): read all relevant — 10-50+ as topic demands
  - **Tier A** (peer-reviewed reviews, conference proceedings, credentialed preprints): 10-30
  - **Tier B** (public figures' quoted statements — politicians, tech execs, prominent commentators): 5-20 figures × 1-5 quotes each
  - **Tier C** (industry trade press, expert blogs, podcasts, corporate white papers): 3-15
  - **Tier D** (mainstream press, non-public-figure social): 3-15
  - **Tier E** (Wikipedia, derivative summaries): as needed for orientation only — NOT saved to `sources/`
- For each source (tiers S/A/B/C/D): WebFetch → extract structured notes → save as `sources/{slug}/extract.md` with full frontmatter (see [`schemas.md`](schemas.md)). Frontmatter must include `tier`, `type`, `peer_reviewed`, `venue`, `topics: [...]`, and `public_figure` for tier B sources.
- **Structured notes, not raw text dumps.** `extract.md` body is `## Abstract` (150-300 words) + `## Key claims` (3-7 bullets with anchors) + `## Reviewer notes` (50-150 words). With 50+ sources per leaf, full extracts overflow context.
- For tier S/A only: optionally save full text as `sources/{slug}/raw.md` alongside `extract.md` when deep re-review is anticipated.
- Update or create `reports/{slug}/topics.yaml` as new topic clusters emerge — topic slugs become cross-leaf metadata.
- Write `passes/pass-01-research.md`: tier-grouped source list, one-line description each, what each likely bears on. Note any tier-imbalances (e.g. "only 2 tier-S sources found — flagging for re-pass with broader query").
- Do NOT write to `claims.yaml` yet. Research gathers; claims come from calc + reconcile.

**Anti-overload check:** if a single leaf has accumulated >150 sources, pause and report — likely the scope needs splitting into sibling leaves.

**Skip Claude+GPT tag team here** — research is mechanical fetching. The validation happens in subsequent sub-passes.

### 2. calc — **SOURCES SEALED**
**Goal:** Derive answers from first principles. Don't peek at sources.

This is the most important sub-pass. Newman's reports failed here.

- Read the leaf question
- List explicit assumptions (numerical + physical + economic)
- Derive the answer using Python or explicit arithmetic, showing work
- State the derived answer with categorical confidence (high/medium/low/speculative based on how load-bearing the assumptions are)
- Write `passes/pass-02-calc.md` with:
  - Assumptions block
  - Derivation block (executable Python preferred; verify with `python3 -c "..."`)
  - Result block with confidence
- Add **derived** claims to `claims.yaml` with `type: derived`, `derivation_path: passes/pass-02-calc.md`
- **Crucially:** do NOT consult `sources/` while doing this. The point is to have an independent number.
- **Plots are optional, not required at leaf level.** If a chart genuinely clarifies the calc (sensitivity sweep, scenario fan, monotonicity demonstration), save it as `pass-02-calc.png` via matplotlib. If the derivation is a single number or a small table, skip plots — they're visual noise on a leaf page. Reserve heavier visualisation for the synthesis pass where comparison across leaves carries the chart's weight.

**Claude+GPT tag team:**
- After Claude writes the calc, invoke `scripts/ask-gpt.py` with system prompt "You are a critical reviewer of a quantitative derivation. The author claims to derive results from first principles. Check the math, check assumption plausibility, flag any step that looks borrowed from common knowledge rather than derived."
- Save audit to `passes/pass-02-audit.md`
- Claude responds, updates calc if needed

### 3. reconcile
**Goal:** Compare derived answer to what sources say.

- Now read the `sources/*/extract.md` files
- For each derived claim from calc: does each source support / contradict / partially-support / not-address?
- Update each derived claim's `evidence[]` array in `claims.yaml`
- Add **factual** claims from sources (where sources state numbers we didn't derive)
- Write `passes/pass-03-reconcile.md`:
  - Agreement table: claim → source verdicts
  - Disagreement section: where derived ≠ sources, why?
  - Resolution: do we update the derived number, downgrade confidence, or stand by our calc?
- Big disagreements → flag, potentially spawn new tree nodes

**Claude+GPT tag team:**
- Audit prompt: "You are reviewing a reconciliation between first-principles math and cited sources. For each disagreement, judge whether the author's resolution is defensible."

### 4. source-review
**Goal:** Review every source — but at depth matched to its tier. See [`source-tiers.md`](source-tiers.md) and the per-tier `review.md` schemas in [`schemas.md`](schemas.md).

- **Tier S** (full claim-by-claim review): per source, list every claim relevant to OUR leaf, quote verbatim, assign verdict from the Newman taxonomy (Consistent / Different conclusion / Novel supporting / Merits investigation / Not relevant). Summary table at top. May spawn new tree nodes via "Merits investigation."
- **Tier A** (medium review): overall verdict + 3-5 key claims with one-sentence justification each. No exhaustive claim enumeration.
- **Tier B** (quote/claim review per public figure): one `review.md` per figure, even if their quotes span multiple containers. List each quote with source pointer, verdict (Supports / Contradicts / Mixed / Not relevant), and one-paragraph reasoning. This is the "check people on what they say" output.
- **Tier C/D** (scalar verdict): one paragraph, single verdict (Consistent / Mixed / Different conclusion / Not relevant) + confidence + flag if conflicts with higher-tier finding.
- **Tier E**: not reviewed.

Sources whose `extract.md` is non-existent or empty are NOT reviewed.

**Claude+GPT tag team:** Per source for tier S/A; aggregate review pass for tier B/C/D. Codex audit checks (a) anti-hallucination — quotes actually appear in `extract.md`; (b) verdict matches the quote's content; (c) scalar verdicts at lower tiers are calibrated against the tier-S findings (no contradicting a peer-reviewed paper by handwave).

### 5. consistency
**Goal:** Check this leaf's claims against sibling leaves' claims (those already-reviewed at run start).

- Load `claims.yaml` from every sibling leaf in `02-leaves/` whose `status: reviewed`
- For each claim in THIS leaf, check: is there a sibling claim on the same topic with a different conclusion?
- If yes: add to `leaf.yaml.contradictions_with[]` and write to `passes/pass-05-consistency.md`
- **Parallel-execution caveat:** when multiple leaves run concurrently, each only sees sibling leaves that were `reviewed` at *its* start time. Contradictions between simultaneously-running siblings will NOT be caught here. They get caught by the post-batch `--pass cross-consistency` (see below).

### 6. write
**Goal:** Render the leaf report. Prose from claims, not the other way around.

- Read `claims.yaml` for this leaf
- Read `notes/` (prior user comments) — incorporate them
- Read all GPT audits — incorporate them
- Write `passes/pass-write.md` with the structure below.

**Required structure (anti-pattern #12):**

1. **Motivation** (~100 words) — why this question matters, what decision it informs. Don't open with the answer.
2. **Where it fits** (~50-100 words) — which sibling leaves feed in, which downstream synthesis depends on this. Frame the leaf in the report's overall architecture.
3. **Headline answer** (~100-200 words) — the take, lead with the bottom line, with confidence labels.
4. **Body** — subsections, each statement traceable to a claim in claims.yaml. Use math where it clarifies (KaTeX inline + display).
5. **Confidence per finding** — explicit per-claim confidence.
6. **Limitations** — what we couldn't establish; what could change the answer.

The "lead with the take" rule is preserved: headline appears in the first ~400 words. But the 200 words BEFORE it set context. Without that, the leaf reads as math homework rather than research.

**Anti-pattern check before saving:**
- Grep for "However," / "Furthermore," / "Moreover," / "It is important to consider" — replace
- Every numerical statement traces to a claim with non-empty evidence
- The opening 200 words deliver the answer (no bury-the-lead)

**Claude+GPT tag team:**
- Audit prompt: "Review this leaf report. List any factual statement not traceable to a claim in claims.yaml. List any narrative move that's mechanical (However, Furthermore, etc.). Flag burial-of-lead if the answer takes >200 words to surface."

## After all six sub-passes

- Update `leaf.yaml.status` to `reviewed` (or `done` if the user gates)
- Update `tree.yaml` node: set `answer` from the leaf's headline finding, set `confidence`, set `status: answered`
- Bump `meta.yaml.current_pass`
- Append final pass-log entry summarizing the whole leaf run
- Final commit + deploy

## Re-running individual sub-passes

If only one sub-pass needs to re-run (notes are new, sources updated, etc.):
- `auto-research --report SLUG --pass leaf --leaf LEAF-ID --sub research` (or `calc`, `reconcile`, etc.)
- Subsequent sub-passes do NOT auto-cascade — re-running calc doesn't auto-rerun reconcile. The user decides which to chase.

## Cross-consistency pass (post-parallel-batch)

**When to run:** Immediately after a parallel batch of leaf runs completes. Sub-pass 5 (consistency) only checks against sibling leaves that were `reviewed` at run start, so when 2+ leaves run concurrently, contradictions between them go unflagged.

**Invocation:** `auto-research --report SLUG --pass cross-consistency --leaves q5,q6,q7` (or omit `--leaves` to scan all currently-reviewed leaves)

**What it does:**

1. Loads `claims.yaml` from every named leaf (or all reviewed leaves)
2. Builds a topic map across all claims using `topics` metadata from `extract.md` frontmatter and `claims.yaml` text
3. For each cross-leaf topic cluster: identifies claims that disagree, where "disagree" means same topic + different numerical value (outside CI) OR opposite verdict on the same assertion
4. Codex audit on the contradiction set: are these real contradictions or artifacts of different scope?
5. Writes `01-tree/cross-consistency-pNN.md` reporting the disagreement set
6. Updates each affected leaf's `leaf.yaml.contradictions_with[]`
7. Flags critical disagreements for re-pass — if leaf X's calc result is incompatible with leaf Y's, one of them needs to re-run calc or reconcile

**Demonstrator example:** q2 (lunar-ascent-cost) ran in parallel with q3 (isru-feasibility). q2's chemical scenarios assumed methalox returns implicitly available. q3's calc concluded no bulk lunar carbon exists, so any lunar methalox requires Earth-imported CH4 — invalidating q2's "lunar-sourced methalox" cost line. Cross-consistency catches this; sub-pass 5 in either leaf did not.

**Lightweight, fast:** the pass reads only `claims.yaml` files (not full prose), so even 10+ leaves are tractable in one Codex call. Output is a contradiction matrix + reasoning, not a rewrite.
