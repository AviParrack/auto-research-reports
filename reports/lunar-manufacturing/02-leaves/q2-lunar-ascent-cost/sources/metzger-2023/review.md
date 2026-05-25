---
source: metzger-2023
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: Metzger 2023 (arXiv:2303.09011)

## Summary

| Verdict | Count |
|---|---|
| Consistent | 3 |
| Different conclusion | 0 |
| Novel supporting | 1 |
| Merits investigation | 1 |
| Not relevant | 1 |

## Claim 1: Γ_LEO ≈ 14 chemical, ≈ 1 SEP-return
**Quote:** "The propellant use ratio Γ for moving lunar product from lunar surface to LEO is approximately 14 under pure chemical reusable round-trip architecture. With SEP... using water as propellant at Isp ≈ 2000 s on the return leg, Γ_LEO drops to approximately 1."
**Verdict:** Consistent
**Why:** Directly underlies q4's claims; cross-checked in q2's calc. The Γ ≈ 14 in chemical reproduces the trade-press tanker-flight figure of 12-14 per HLS mission.

## Claim 2: Γ values for closer destinations (LLO 0.9, EML1 1.3, GEO 1.4)
**Quote:** "For closer cislunar destinations Γ is O(1): LLO ≈ 0.9, EML1 ≈ 1.3, GEO ≈ 1.4."
**Verdict:** Consistent
**Why:** Implies that lunar manufacturing for cislunar destinations (other than LEO) is structurally easier. Not directly tested in q2's LEO-only scope, but consistent with my framework — q2 chose LEO specifically because it's the hardest destination.

## Claim 3: φ ≥ 35 production mass ratio threshold
**Quote:** "φ ≥ 35 (production mass ratio) is the threshold for lunar absolute advantage at GTO under Metzger's mid-range cost parameters."
**Verdict:** Not relevant
**Why:** q4's domain, not q2's. q2 models the ascent leg cost, not the production stage. q4 already reviewed this anchor.

## Claim 4: Architecture > chemistry assertion
**Quote:** "Lunar product can be delivered to LEO at approximately the same per-kg cost as terrestrial launch cost — making the architecture choice the dominant variable, not the chemistry of the ascent vehicle."
**Verdict:** Consistent
**Why:** Matches q2.c4 — aerobraking is the dominant lever, larger than methalox vs hydrolox choice. Architectural framing carried into the calc.

## Claim 5: Bootstrap problem implied but not modeled
**Quote (paraphrased from extract):** "the bootstrap problem of getting the ascent vehicle to the lunar surface in the first place."
**Verdict:** Merits investigation
**Why:** This is q5's domain (capital buildup). Metzger 2023 treats lunar industry as mature; q5 should model the bootstrap explicitly. Flag for q5 author.

## Claim 6: Mass drivers not modeled in Metzger 2023
**Quote (paraphrased from extract):** "Metzger doesn't decompose lunar-ascent-only cost (surface → LLO) separately... Doesn't model mass drivers explicitly."
**Verdict:** Novel supporting
**Why:** q2 fills a gap Metzger left open: separate decomposition of the ascent leg, with mass driver as an alternate architecture. The frameworks are complementary, not contradictory.

## Anti-hallucination check

All claims above are sourced from the extract.md content. The arXiv full-PDF was not directly accessible via WebFetch (binary stream); I rely on the abstract + secondary spacesettlementprogress.com summary for specific quotes. This is a known gap flagged in the research pass.
