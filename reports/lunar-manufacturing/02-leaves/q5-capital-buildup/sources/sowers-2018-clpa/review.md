---
source: sowers-2018-clpa
tier: S
reviewed_pass: 4
reviewed_by: claude+codex
---

# Source Review: Sowers 2018 — Commercial Lunar Propellant Architecture (CLPA)

## Summary

| Verdict | Count |
|---|---|
| Consistent | 2 |
| Novel supporting | 2 |
| Merits investigation | 1 |

## Claim 1: "End-state production target ~2,450 tonnes of propellant per year"
**Verdict:** Novel supporting
**Why:** The 2,450 t/yr output target is roughly 2.5x our calc's 1,000 t/yr midpoint, reflecting Sowers' commercial-scale ambition. Our calc's lower output scales the ISRU plant mass down proportionally, but the architectural difference (tent vs strip mining) is the more important factor.

## Claim 2: "Architecture stages: prospecting (precursor) → pilot plant → first production plant → multiple subsequent plants → distribution chain"
**Verdict:** Consistent
**Why:** Direct support for the staged-buildup-milestone decomposition in our calc (M1-M8). Sowers' stages map roughly to our M1 (prospecting), M2-M3 (lander/habitat), M5 (pilot ISRU), M7-M8 (multiple plants + distribution → net-positive export).

## Claim 3: "Tent sublimation as the chosen ice extraction method"
**Verdict:** Novel supporting
**Why:** Tent sublimation is the architectural choice underlying φ ≈ 534 (per Metzger 2023's classification). This is the key technical decision that yields Sowers' optimistic capex. Our calc uses a generic midpoint architecture (φ = 20); tent sublimation would shift our estimate sharply downward for the ISRU component.

## Claim 4: "Operations are fully robotic — no humans required at the mining site during normal operations"
**Verdict:** Merits investigation
**Why:** Fully-robotic operations eliminate the habitat + life support component from the M5 architecture entirely. Our calc retains the habitat (25-50 t) because we're modeling a *manufacturing base capable of net-positive export*, not propellant production alone. The robotic-only choice is appropriate for Sowers' scope but not directly transferrable to ours.

## Claim 5: "The architecture assumes commercial launch services (Falcon Heavy, Vulcan, future Starship), not SLS-class transport"
**Verdict:** Consistent
**Why:** Same commercial-launch assumption our calc uses (q1 $/kg figures). This is the basic transport-architecture decision that distinguishes Sowers' $4B from Jones' 35-year-breakeven pessimism.

## Cross-reference

- PDF body could not be parsed (10MB exceeded WebFetch limit); review based on summary content from secondary coverage and direct cross-reference to Sowers 2021.
- The architectural staging here is the most concrete published roadmap for milestone-by-milestone buildup.
- The 2,450 t/yr endpoint is the most-cited commercial-architecture output target.
- Codex anti-hallucination check: limited quote extraction due to PDF body inaccessibility; review based on title + abstract + reconstruction from Sowers 2021.
