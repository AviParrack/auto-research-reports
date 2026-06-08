# Anti-Patterns — read before every pass

These are the structural countermeasures against Newman's narrative-over-logic failure mode (Centaur Era footnote 11). Each pass must check against these. They are non-negotiable.

## 1. Narrative over logic
**Don't:** Write a compelling paragraph-by-paragraph story and call it a report.
**Do:** Build the claim graph first (`claims.yaml`). Prose is rendered *from* the graph, never invents claims absent from it.
**Check:** Every factual statement in the prose must trace to a claim ID in `claims.yaml`.

## 2. Source borrowing in calculations
**Don't:** Let the calc pass crib numbers from existing sources and dress them up as derived.
**Do:** P2 calc seals sources. Build from first principles, physical constants, and explicit assumptions. Only P3 reconcile compares to sources.
**Check:** The calc pass file must explicitly list its assumptions and derive from them. Any borrowed number is flagged.

## 3. Single-model echo chamber
**Don't:** Trust Claude's first draft as ground truth.
**Do:** Every writing step is a Claude+GPT tag team. GPT critiques claim-by-claim; Claude responds; unresolved → the user.
**Check:** Every pass file has a sibling `pass-{NN}-audit.md` written by GPT (or marked `unaudited` if GPT unreachable).

## 4. Hidden cross-section contradictions
**Don't:** Let two leaves assert opposing things without surfacing the conflict.
**Do:** P5 consistency pass extracts all claims across all leaves, groups by topic, flags contradictions. Each contradiction is a required-resolution item.
**Check:** Before synthesis, `consistency-flags.yaml` must be empty or every flag must have a `resolved_by` field.

## 5. Hallucinated sources
**Don't:** Cite a paper or expert without having actually fetched and read the source.
**Do:** Every cited source has an `extract.md` file *fetched* via WebFetch before it can appear as evidence in any claim.
**Check:** Every `evidence.source` slug in claims.yaml must correspond to a folder under `sources/` with a non-empty extract.md.

## 6. Drift from root question
**Don't:** Let the tree grow into tangents.
**Do:** Tree pass evaluates every node for "does this directly feed the root answer?" Deprecate drift.
**Check:** Termination predicate (2) — "explain how the analysis relates to each key source" — fails if any node is unconnected.

## 7. Mechanical academic register
**Don't:** Write "However," / "Furthermore," / "Moreover," / "It is important to consider" — the LLM transition slop.
**Do:** Short sentences. Varied openers. Concrete first, abstract second.
**Check:** Run a grep for the slop words at end of write pass.

## 8. Over-hedging
**Don't:** "Some researchers suggest that perhaps it might be the case that..."
**Do:** Confidence is categorical: high | medium | low | speculative. Stated once, then commit to the claim.
**Check:** Every claim has exactly one confidence field. Prose says "this is low-confidence" once at most.

## 9. Bury-the-lead synthesis
**Don't:** Build up to the answer in paragraph 7.
**Do:** First 200 words of every synthesis must deliver the headline answer.
**Check:** Open the synthesis file. Read the first 200 words. Does a stranger know what we concluded?

## 10. Resistance to correction
**Don't:** Ignore `notes/` (user comments) when re-writing.
**Do:** Every write/synthesis pass starts by reading `notes/` and any GPT audit files. Human and machine corrections are first-class inputs.
**Check:** The pass file must explicitly acknowledge what notes it incorporated (or why it disagreed).

## 11. Naive calendar-year timelines
**Don't:** Write "realistic by 2040+" or "won't happen before 2050" as if calendar time were the binding variable. Calendar dates are nearly meaningless across most planning horizons — AI/automation could compress a century into a decade, or progress could stall for half a century like the 50-year post-Apollo lunar drought.

**Do:** Decompose into *what stands in the way* — list the engineering steps, mass budget, capital requirements, regulatory gates, technology readiness — then opine about how compressible each step is.

Frame timelines conditionally:
- "Requires N major engineering milestones, each of which involves [X, Y, Z]. Under business-as-usual progress this is *~2N decades*; under sustained industrial explosion or TAI-level automation the bottleneck collapses to *capital allocation and physical lead-times for hardware*, plausibly compressing to *~N years or less*. The downside scenario is a stall (precedent: 50-year post-Apollo lunar inactivity)."
- Or simply: "Decades of work modulo TAI; weeks to months in a full intelligence explosion; stalled indefinitely if political will doesn't materialise."

The point is to make the *uncertainty about the timeline itself* visible. Decoupling "how much work is left" from "how fast we will do that work" is the move.

**Check:** Grep for `\b20[34]\d\b` and `\b20[5-9]\d\b` in any leaf write or synthesis output. Every hit needs to be wrapped in conditional framing or replaced with a step-count + acceleration-sensitivity discussion. Pure calendar predictions are bugs.

## 12. Answer-first without motivation
**Don't:** Open a leaf write or synthesis report with the headline answer and dive straight into derivation. The reader needs to know *why this question matters*, *where it sits in the bigger picture*, and *what they should take from it* before being asked to follow detail.

**Do:** Every leaf write opens with three short sections (or paragraphs) before the headline:
- **Why this question matters** — what decision does answering it inform, what changes about the bigger picture if the answer flips
- **Where it fits** — which sibling leaves provide input, which downstream synthesis depends on it
- **Headline answer** — then the result, with confidence

The "lead with the take" rule is preserved — the headline still appears in the first ~200 words — but the *200 words before it* set context. Without that, the leaf reads as math homework rather than research.

**Check:** Open the leaf write. Read only the first paragraph. Does a stranger who has never seen the rest of the report know what this question is for? If not, add motivation.

## 13. Editorial / news-headline voice in academic deliverables
**Don't:** "X is real but contingent." "Y is the dominant lever." "Z refutes the framing that A." "Surprisingly, B." These intensify, dramatise, and editorialise. They belong in news copy or blog posts.

**Do:** Use maximal-rigor academic register. Factual, informative, declarative. Quantitative where possible. No "real" (implies a claim against unreality), no "huge", no "matters more than", no "the framing", no "surprisingly". State the data and let the data carry the implication.

**Before:** "The popular '≥35× threshold' is real but contingent. Tent sublimation already exceeds the threshold by an order of magnitude."

**After:** "The 35× threshold reported in Metzger (2023) is the production-mass-ratio value at which the model's MVP design achieves absolute advantage at GTO under the specified cost assumptions; it varies with destination, financing structure, and architecture choices. Tent sublimation studies (Kornuta 2019, Sowers 2021) report production-mass-ratio values of 442 and 534 respectively."

The second version says more (specifies what makes it "contingent" — destination, financing, architecture; gives citations; says the actual numbers). It also commits to less rhetorical loading.

**Check:** Grep the write for these editorialising verbs/adjectives and either remove or replace with quantitative substance:
- "is real", "is huge", "matters", "the dominant", "the bottleneck", "refutes", "surprisingly", "remarkably", "notably", "importantly"
- "the popular X", "the common framing", "Y is what makes Z work"

## Voice anti-patterns (additional)

These apply to all *prose* output (synthesis, leaf write passes, README drafts):
- No em-dash overuse
- No "it's not X, it's Y" cadence
- No safety-speak / over-disclaimers
- Lead with the take, not the methodology
- Visual variety: mix prose, bullets, tables, callouts; don't write 4 paragraphs of identical structure

If the user has a project-specific style guide (e.g. a `STYLE.md` in the repo root, or skill-specific instructions in CLAUDE.md), read and apply that overlay on top of these anti-patterns. The defaults above are universal; per-project voice is layered on.
