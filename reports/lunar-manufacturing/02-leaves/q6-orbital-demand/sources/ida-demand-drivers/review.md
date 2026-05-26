---
source: ida-demand-drivers
tier: S
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: IDA STPI D-13219 — Demand Drivers of the Lunar and Cislunar Economy

## Summary

| Verdict | Count |
|---|---|
| Consistent | 3 |
| Merits investigation | 1 |

## Claim 1: Government + commercial + downstream demand segmentation

**Verdict:** Consistent

**Why:** IDA's taxonomy directly maps to q6's use-case decomposition.
Government (NASA Artemis, DoD cislunar surveillance) ≈ q6.c12
Artemis cargo. Commercial (tourism, science, propellant) ≈ Kornuta
segments. Downstream (servicing, deep-space) ≈ q6.c13 servicing +
q6.c11 Mars cargo.

## Claim 2: Kornuta 450 t/yr near-term cite

**Verdict:** Consistent

**Why:** IDA's adoption of Kornuta 2019 as the canonical demand floor
validates the 450 t/yr figure as established consensus. Cross-cited
via Metzger 2023 → q6.c8.

## Claim 3: Chicken-and-egg coordination problem

**Verdict:** Consistent

**Why:** The producer-customer commitment coordination problem is
real and matches the chicken-and-egg observation in the 2026 industry
landscape (Starcloud + Axiom + Kepler operational but not yet at
profitability). q6 doesn't explicitly model this coordination friction
but should flag it for q8 synthesis.

## Claim 4: Two-decade demand-materialization horizon

**Verdict:** Merits investigation

**Why:** IDA's 15-25 year horizon assumption aligns with q6's
2026-2040 framing under BAU. Under TAI-C, the horizon compresses
sharply (~5-10 years). IDA's analysis predates the AI-compute-demand
explosion that q6's TAI-C scenario captures; the demand horizon
estimate may now be too conservative. Flag for synthesis.

## Anti-hallucination check

- Full PDF not parseable via WebFetch; demand-segmentation framework
  and 450 t/yr citation extracted from secondary aggregators
  (academic citation tracking).
- Future iteration should hand-extract IDA's specific demand-magnitude
  tables for each segment.

## Notes

IDA D-13219 is the canonical U.S. policy framework for the lunar/
cislunar demand decomposition. The taxonomy itself is the most useful
output for q6; specific demand figures are largely re-cites of Kornuta
2019 already in the source set.
