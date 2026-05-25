---
source: kornuta-2019-clpa
tier: S
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: Kornuta 2019 — Commercial Lunar Propellant Architecture

## Summary

| Verdict | Count |
|---|---|
| Consistent | 4 |
| Novel supporting | 1 |
| Merits investigation | 0 |
| Not relevant | 0 |

## Claim 1: 450 t/yr near-term annual demand

**Quote:** "near term annual demand of 450 metric tons of lunar derived
propellant equating to 2450 metric tons of processed lunar water
generating $2.4 billion of revenue annually."

**Verdict:** Consistent

**Why:** q6.c8 explicitly uses this figure. The 450 t/yr is the
foundational quantitative anchor for cislunar propellant demand in the
academic literature; Metzger 2023 adopts it as the baseline for the
economic-viability calculation.

## Claim 2: Reusable-lander market segment

**Quote:** Lunar reusable landers traveling surface to orbit are a
near-term segment.

**Verdict:** Consistent

**Why:** Aligns with q6.c5's BAU depot demand decomposition — Artemis
HLS reusable-lander operations are the principal Artemis-era depot
customer at ~10 ships/yr × 8 tankers × 100 t = 8,000 t/yr in my model.
Kornuta's reusable-lander segment is one of two-three sub-segments
within that total.

## Claim 3: Mars refueling market segment

**Quote:** Interplanetary vehicles refueled in cislunar space before
Mars departure benefit from lunar propellant.

**Verdict:** Consistent

**Why:** This segment dominates my TAI-C 160 kt/yr depot throughput
(Musk Mars cadence × 8 tankers/ship). Kornuta's recognition of this
segment in 2019 anticipated the TAI-C scenario that Marcy / SpaceX/xAI
2026 filings now operationalize.

## Claim 4: GEO-from-LEO refueling segment

**Quote:** GEO and beyond missions refueled in LEO benefit from
lower-Δv lunar propellant access.

**Verdict:** Consistent

**Why:** Aligns with marketsandmarkets-2026-osam refueling-segment
growth ($2.4B→$5.1B 2023-2030). q6.c13 captures the related satellite-
servicing market.

## Claim 5: Technical + economic feasibility

**Quote:** Both technical feasibility and economic competitiveness are
established at the architecture level.

**Verdict:** Novel supporting

**Why:** Kornuta's 36-author conclusion of joint technical-and-economic
feasibility is the strongest possible support for q6's premise that
demand exists at scale — feasibility-of-supply unlocks feasibility-of-
demand via Metzger's elastic-feedback mechanism.

## Anti-hallucination check

- All quotes appear in `extract.md` ✓
- The 450 t/yr figure is the canonical citation, cross-validated across
  IDA D-13219, Metzger 2023, and ADS/REACH metadata.
- Direct PDF not parseable; full text behind paywall. Future iteration
  should hand-extract customer-segment tables and architecture diagrams.

## Notes

Kornuta 2019 is the foundational demand-side source for cislunar
propellant. Its widespread citation in subsequent literature (Metzger
2023, IDA 2020) makes it the canonical anchor for q6's BAU depot
demand figures. The 450 t/yr figure is the most-defensible single
quantitative datum for near-term cislunar propellant demand.
