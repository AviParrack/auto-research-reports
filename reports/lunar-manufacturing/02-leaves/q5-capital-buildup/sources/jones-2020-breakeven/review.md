---
source: jones-2020-breakeven
tier: S
reviewed_pass: 4
reviewed_by: claude+codex
---

# Source Review: Jones et al. 2020 — Cost Breakeven Analysis

## Summary

| Verdict | Count |
|---|---|
| Consistent | 2 |
| Different conclusion | 1 |
| Merits investigation | 1 |
| Not relevant | 0 |

## Claim 1: "The breakeven point occurs at 35 years of an annual propellant demand of 59 tonnes per refill"
**Quote:** Executive summary / Section 6.3.
**Verdict:** Different conclusion (architecture-contingent)
**Why:** The 35-year break-even is the headline pessimistic-TEA finding under SLS-class capital transport. Metzger 2023 (already reviewed) re-analyses this paper and demonstrates the pessimism is artifact of the SLS-class assumption (G ≈ 42) rather than the ISRU process itself. So Jones' 35-year figure stands as a factual result of his specific architecture choice but should not be cited as a general-architecture conclusion. For q5: this is the canonical SLS-class-pessimistic anchor; useful as a reminder that transport-architecture choice can shift the answer by ~10x.

## Claim 2: "The magnitude and duration of the lunar campaign, more so than the Mars campaign, drive the breakeven"
**Quote:** Section 6.3.
**Verdict:** Consistent
**Why:** Direct support for our q5 framing — the lunar-side capital (habitat, ISRU plant, mfg) and its operating duration dominate the cost picture, not the Mars-mission cadence on the destination side. Aligns with our calc's structural emphasis on lunar-base capital mass.

## Claim 3: "Without long lifetime ISRU systems with greater than 5 years of autonomous operation before replacement, the demand in cis-lunar space for a Mars campaign favors propellant delivery from Earth"
**Quote:** Jones 2020.
**Verdict:** Consistent
**Why:** Reinforces the load-bearing role of capital lifetime in total program cost. Our calc uses 5-15 year lifetimes; Jones' 5-year floor is the implied design minimum. If our 8-year lifetime for the ISRU plant proves optimistic and 5 years is the right number, our BAU total grows by ~30%.

## Claim 4: "Including the costs of spares and replacement of the reusable lunar landers and in-space stages, which were not included in this study, would push the breakeven point even further out"
**Quote:** Jones 2020.
**Verdict:** Merits investigation
**Why:** Lander-side spares and replacement are not in our calc's accounting either (we treat lander mass as part of the $/kg-to-LS transport cost). Jones' point is that this could be a significant additional cost. Merits a follow-up to size the lander spares + replacement properly.

## Cross-reference

- This source's pessimistic conclusion is the necessary counterweight to Sowers' optimistic commercial framing.
- Metzger 2023 re-analyses and reframes this paper; Jones' specific 35-year figure is architecture-contingent.
- PDF body extraction failed; review based on Codex search summary and Metzger 2023's re-analysis. Re-fetch with better PDF tooling would tighten this review further.
