---
synthesis_version: v1
diff_pass: 1
date: 2026-05-26
inputs: [claude-v1.md, codex-v1.md]
---

# Diff: claude-v1 vs codex-v1

Both writers received the same context.md and wrote independently. The diff triage rule: a difference is **substantive** if it would change what a reader does with the answer; otherwise it is style.

## Substantive agreements

Both v1s converge on the same load-bearing conclusions. A reader following either draft makes the same decisions:

- **TAI-grade compression is required for the cost crossover.** Both flag $50/kg vs $59/kg margin as TAI-conditional. Both note q2.c5's $10B capital assumption only matches q7's TAI endpoint ($13.3B), not BAU ($1,242B). Neither presents the crossover as "available by a calendar year."
- **Throughput necessity is the independent second leg under TAI-C.** Both report SDC demand ~10× Earth-launch ceiling under TAI-C, lunar bulk mass necessary for ~50% of SDC mass budget, compute hardware half remains Earth-launch-bound.
- **BAU answer is "no" on both legs.** Both note mass driver doesn't reach scale within 20-25 year horizon; demand fits inside Earth-launch capacity.
- **Stall answer is "no for lack of demand."** Both name q6.c7 — thesis collapses because the market doesn't materialize, not because supply fails.
- **Cycle-life gap is binding.** Both surface q7.c10's 5-7 OOM gap between demonstrated and required EM-launcher cycle life. Both explicitly state TAI compression does not close it; materials-science breakthrough required.
- **Polar-ice gate is a near-term empirical variable.** Both name q3.c4's VIPER dependency; both note q2 aggressive-ISRU collapses if VIPER returns unfavorable.
- **M6 12-month floor is irreducible.** Both surface q5.c7's crewed-occupation milestone as carve-out from TAI compression.
- **φ-threshold qualifier matters.** Both preserve "multi-year integration" language from q3.c13b/q4.c6; neither shortens to "MRE clears φ."
- **Chemical lunar ascent does not clear the bar.** Both state explicitly: only mass-driver+SEP closes within a factor of 2 of optimistic Starship; chemical scenarios sit an order of magnitude or more above terrestrial.
- **q1 internal-cost-vs-list-price gap creates a regime split, not a smooth curve.** Both surface as cross-pass inference; both note TAI-C is unaffected because gated by internal cost (SpaceX-internal use) and AI compute growth.
- **BAU full architecture is ~$1.4-1.7T.** Both correctly stack q5 base ($150-400B) and q7 mass driver ($1,242B BAU) as additive components rather than alternatives.
- **The framework is the deliverable; the headline number is conditional on the regime.** Both explicitly frame the answer as regime-based, not date-based.

## Style differences (same conclusion, different framing)

- **Length.** claude-v1 ~3,500 words; codex-v1 ~1,800 words. claude-v1 has a more extensive Body section with leaf-by-leaf assembly; codex-v1 tightens the cost-leg and throughput-leg sections to dense paragraphs.
- **Section headers.** claude-v1 uses sentence-case ("The two legs in detail"); codex-v1 uses Title Case ("Cost Leg: What Has To Beat What"). Cosmetic.
- **Confidence labeling.** claude-v1 lists confidence per finding at the end as a bulleted block; codex-v1 inlines `**Finding confidence:**` after each section. Both functionally equivalent.
- **Math rendering.** claude-v1 uses inline `\(\Gamma\)` notation sparingly; codex-v1 uses `\(...\)` more heavily for numerical values (`\($50/kg\)`). Both render via KaTeX; claude-v1's lighter touch is a style choice.
- **Voice.** claude-v1 occasionally uses phrasing like "the arithmetic is hard" (slightly informal); codex-v1 keeps a tighter academic register throughout. Both stay inside the maximal-rigor brief.
- **Citation density.** Both use `[leaf-id.claim-id]` inline citations comparably; no substantive difference in coverage.
- **BAU sub-regime split.** claude-v1 explicitly carves "BAU-internal-cost" vs "BAU-list-price" as two sub-regimes; codex-v1 captures the same coupling but stays at the BAU-vs-TAI-C level without the sub-regime label. The information content is the same.
- **Negative framing.** codex-v1 closes with "Lunar manufacturing does not generally become cheaper than Earth launch... The crossover occurs when the problem is recast..." which lands the negative-result framing slightly more sharply than claude-v1's restatement. claude-v1 puts the same content under "Headline restated" with slightly more architectural framing. Both deliver the same conclusion.

## Substantive disagreements

**None identified.** Where one writer surfaces a claim the other does not, the difference is omission rather than disagreement — and the omitted material is recoverable from context.md by either reader.

Specifically checked:
- Cost ranking between scenarios → identical
- TAI-grade requirement for the cost leg → identical
- TAI-C demand exceeds Earth-launch ceiling → identical (both ~10×)
- Cycle-life gap not closed by TAI → identical
- VIPER as load-bearing near-term variable → identical
- M6 floor breaks out of TAI compression → identical
- Chemical lunar ascent does not clear the bar → identical
- BAU sub-regime split → present in claude-v1, implicit in codex-v1; not a disagreement
- φ-threshold model-contingency → both note Metzger's mid-range is the canonical anchor

## Decision

Per pass-synthesis.md step 5: **no substantive disagreements → both v1s publish.** No debate phase required. The two drafts represent legitimate stylistic variation around a converged substantive answer.

The site renders both under tabs (claude-v1, codex-v1, diff, context) on the synthesis page. Avi reads either as the primary; the other serves as substantive cross-check.

## Note on the convergence itself

The convergence is itself a useful signal. Two writers, isolated from each other's drafts, working from the same per-leaf claim graph + cross-consistency findings, reach the same load-bearing conclusions in the same order. The shared substrate (claim graph + cross-consistency, not free-form prose) is doing real work here — both writers are constrained to argue from the same atomic claims, which prevents either from drifting into narrative that the underlying evidence doesn't support. The Newman failure mode (narrative drift over logical structure) is structurally prevented by the substrate; the convergence demonstrates that.
