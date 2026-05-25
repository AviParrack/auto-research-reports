---
source: coutts-sowers-2025
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: Coutts and Sowers 2025 (Sage Journals, VOI for lunar ice)

## Summary

| Verdict | Count |
|---|---|
| Consistent | 2 |
| Different conclusion | 0 |
| Novel supporting | 1 |
| Merits investigation | 1 |
| Not relevant | 0 |

## Claim 1: Starship LEO cost $30-$300/kg
**Source content (paraphrased; original is paywalled, this is from extract's "key-anchors-quoted-in-secondary-sources" block):** Starship LEO launch cost used as L_p assumption is $100/kg base case; $300/kg pessimistic (10 reuses); $30/kg optimistic (100+ reuses).
**Verdict:** Consistent
**Why:** Matches q1's optimistic-to-pessimistic range. My Earth-imports-only gear-ratio amplification uses these figures correctly.

## Claim 2: $500/kg lunar surface propellant target
**Quote (from secondary summary):** "The price ULA is willing to pay on the surface of the Moon is $500/kg for 1100 mT of propellant per year."
**Verdict:** Consistent
**Why:** Used as the maturity-era market clearing price anchor in q2.c10. My aggressive-ISRU production range ($300-2000/kg across eras) spans this.

## Claim 3: 1100 mT/yr propellant demand
**Quote:** "1100 mT of propellant per year on the lunar surface"
**Verdict:** Novel supporting
**Why:** Provides a demand-side anchor for q6 (orbital demand). My q2 calc doesn't use this directly but it's relevant to whether the ISRU operation can amortize fixed costs. Captured for q6 flagging.

## Claim 4: VOI methodology — lunar propellant has positive NPV under uncertainty
**Quote (paraphrased):** "Lunar propellant could yield positive net present value even under unfavorable conditions, making ground-based exploration economically justified."
**Verdict:** Merits investigation
**Why:** Coutts-Sowers report positive NPV; my q2 calc shows lunar-to-LEO chemical is 9-17× more expensive than terrestrial. The reconciliation: Coutts-Sowers's "lunar propellant" is delivered to cislunar destinations where Γ is O(1), not to LEO where Γ ≈ 14. Flag for q8 synthesis.

## Anti-hallucination check

The paper is paywalled and the extract relies on Sage Journals abstract + secondary citations. All quotes above are from the secondary search summaries; the primary numerical figures (cost ranges, propellant demand) should be re-verified against a direct read of the paper if it becomes accessible. Flagged in the extract's "limitations" section.
