---
source: metzger-2023-economics
tier: S
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: Metzger 2023 — Economics of In-Space Industry

## Summary

| Verdict | Count |
|---|---|
| Consistent | 3 |
| Novel supporting | 1 |
| Merits investigation | 1 |
| Not relevant | 0 |

## Claim 1: 450 t/yr near-term lunar-derived propellant demand

**Quote:** "near-term annual demand of 450 metric tons of lunar derived
propellant equating to 2,450 metric tons of processed lunar water"
generating ~$2.4B/yr in revenue.

**Verdict:** Consistent

**Why:** q6.c8 reproduces this figure as the lunar-derived sub-segment
of BAU 8,000 t/yr LEO refueling. The 5.6% interpretation is mine; the
450 t/yr figure is jointly attributed to Kornuta 2019 (from which Metzger
adopts) and Metzger 2023.

## Claim 2: Gear-ratio + production-mass-ratio framework

**Quote:** Gear ratio Γ for capital transport and production mass ratio
φ for capital mass per lifetime product mass are the two dominant
levers; threshold ~35× at GTO under mid-parameters.

**Verdict:** Consistent with q4-gear-ratio (parallel leaf, reviewed);
not directly engaged by q6.

**Why:** q6's demand decomposition is downstream of Metzger's
viability framework. The 35× threshold lives in q4; q6 inherits the
conclusion that ISRU is competitive under reasonable parameter
assumptions and asks "how much demand exists if it is?"

## Claim 3: Demand-elastic feedback

**Quote:** Cheaper in-space propellant lowers cost of all downstream
space activities, expanding the propellant market itself.

**Verdict:** Novel supporting

**Why:** Metzger's mechanism is exactly the q1↔q6 demand-elasticity-cost
coupling I derived (q6.c2 regime range, q6.c6 lunar-manufacturing
necessary-but-not-sufficient). His paper provides the formal economic
framework I'd not have surfaced from first-principles alone. Strong
support for the qualitative direction of q6.c6.

## Claim 4: GTO as dominant near-term market

**Quote:** Geosynchronous transfer orbit servicing is the most
economically attractive near-term propellant market because it saves
spacecraft mass already targeted at high-value orbits.

**Verdict:** Consistent

**Why:** Metzger's GTO-dominance claim is structurally consistent
with my BAU regime allocating depot demand across Artemis HLS + GEO
servicing + occasional deep-space. The GTO sub-segment within my
8,000 t/yr BAU depot total likely matches Kornuta's 450 t/yr lunar-
derived figure (cross-check in q6.c8).

## Claim 5: Competitiveness conditional on gear ratio + production mass

**Quote:** Commercial competitiveness depends on achieving sub-threshold
gear ratio and production mass ratio — not on the propellant chemistry
itself.

**Verdict:** Merits investigation

**Why:** This is q4's domain rather than q6's, but it raises a question
that q6 should engage: does the demand scenario in TAI-C (160 kt/yr
depot throughput) require a different gear-ratio threshold than the
BAU 8 kt/yr scenario? Larger throughput plausibly reduces unit cost
via Wright's-law learning, which would relax the threshold — a
demand-side feedback into q4's parameter set. Flag for q8 synthesis.

## Anti-hallucination check

- All quotes appear in `extract.md` ✓
- The 450 t/yr near-term demand and gear-ratio framework are accurately
  attributed to Metzger 2023 in q6.c8 and (cross-leaf) q4 claims
- Direct PDF text was not parseable via WebFetch; key figures
  cross-validated across IDA D-13219, Kornuta 2019, and ResearchGate
  abstract. Flagged in extract.md "Reviewer notes."

## Notes

Metzger 2023 is the most load-bearing single source for q6's
qualitative-direction conclusions. The demand-elastic-feedback
mechanism is the analytical core of the lunar-manufacturing thesis
under TAI-C. Future iteration should hand-extract the gear-ratio
parameter tables from the original PDF; the framework structure is
solid, but precise threshold values for our regimes would benefit
from primary access.
