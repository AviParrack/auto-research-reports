---
source: metzger-2023-economics
tier: S
reviewed_pass: 4
reviewed_by: claude+codex
---

# Source Review: Metzger 2023 — Economics of In-Space Industry

## Summary

| Verdict | Count |
|---|---|
| Consistent | 3 |
| Novel supporting | 1 |
| Merits investigation | 1 |
| Different conclusion | 0 |
| Not relevant | 2 |

## Claim 1: "Gear ratio (G) and production mass ratio (φ) are the most important factors determining competitiveness"
**Quote:** Abstract.
**Verdict:** Consistent
**Why:** This framework is owned by q4-gear-ratio (claims q4.c1-q4.c14). For q5, it provides the structural decomposition of capex into capital mass × launch cost. Our calc uses φ = 20 as a midpoint between Pelech's 3.7 and Sowers' 534.

## Claim 2: "(x + G)/φ + ω + ξ < 1/Γ" (competitiveness condition)
**Quote:** Eq. 8.
**Verdict:** Not relevant (to q5 directly)
**Why:** This is the competitiveness condition q4 derives in depth. q5 inherits the cost-decomposition substrate but does not directly use the inequality.

## Claim 3: "Tent sublimation TEAs yield φ in the hundreds (Kornuta 442, Sowers 534)"
**Quote:** Table 2.
**Verdict:** Novel supporting
**Why:** For q5, the φ ≈ 534 anchor explains how Sowers can claim a $4B capex with a much smaller ISRU plant mass than our 75 t baseline. The tent-sublimation architecture is fundamentally different from strip-mining — passive sublimation reduces active hardware mass dramatically. This is the single most important supporting data point for the architecture-not-optimism explanation of the 3-order-of-magnitude anchor spread (q5.c15).

## Claim 4: "Strip-mining φ estimates cluster around the breakeven with substantial spread: Jones 22.2, Charania-DePascuale 26.5, Bennett 43.4, Pelech 3.7"
**Quote:** Table 2.
**Verdict:** Consistent
**Why:** Our calc's φ = 20 sits inside this cluster (Jones-like). The φ = 3.7 Pelech outlier is explained by Metzger as artifact of terrestrial-excavator analogies. Direct evidence for the φ range used in our calc.

## Claim 5: "M_K (capital mass) depends critically on whether the design uses terrestrial-excavator analogies (overestimates) or space-engineered hardware"
**Quote:** Re-analysis of Pelech (Section 6.x).
**Verdict:** Consistent
**Why:** Reinforces the Codex critique on our pass-02 calc that the 75 t ISRU plant could be larger; but also reinforces that purpose-engineered space hardware can be substantially lighter than terrestrial analogues. Both directions of the M_K uncertainty are captured.

## Claim 6: "Long-term reliability of the lunar capital is the primary remaining concern"
**Quote:** Conclusion.
**Verdict:** Merits investigation
**Why:** Reliability is the load-bearing variable our calc handles weakly (5-yr/8-yr/10-yr placeholder lifetimes — see q5.c9). Direct evidence that the lifetime knob deserves more focused analysis; merits a follow-up tree node on lunar-capital-reliability.

## Claim 7: "Pessimistic published TEAs (Charania-DePascuale G ≈ 65, Jones G ≈ 42) used SLS-class pricing for capital transport. With commercial launch G drops by an order of magnitude"
**Quote:** Section 6.1-6.2.
**Verdict:** Consistent
**Why:** Direct evidence for the SLS-vs-commercial-launch architectural reframe that explains part of the MacDonald $1T vs our BAU $150-400B gap. Reinforces q5.c4 framing of regime-conditional outcomes.

## Cross-reference

- Already extracted in q4-gear-ratio leaf as canonical source for the gear-ratio framework.
- For q5: serves as the dimensional-analysis substrate for capex decomposition.
- Cross-leaf consistency: q4's claims about gear ratio and φ are reused in q5 without re-derivation.
- Codex anti-hallucination check: all quoted text appears verbatim or is paraphrase clearly labelled.
