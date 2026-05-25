---
source: satbase-2026-falcon9
reviewed_pass: 4
reviewed_by: claude+codex
date: 2026-05-25
---

# Source review: SatBase Feb 2026 Falcon 9 pricing

## Summary

| Verdict | Count |
|---|---|
| Consistent | 4 |
| Novel supporting | 1 |
| Merits investigation | 1 |
| Different conclusion | 0 |
| Not relevant | 0 |

## Claims reviewed

### Claim 1 — 2026 dedicated launch price
**Quote:** "Dedicated Launch: $74 million (up from $70M)"
**Verdict:** Consistent

Anchors the q1 list-price baseline. With a typical 22.8-tonne LEO payload utilisation, this implies ~$3,240/kg amortised cost — within the optimistic-to-partial calc range. Used in [pass-03-reconcile.md] as the 2026 baseline for projecting forward.

### Claim 2 — 2026 rideshare $7,000/kg
**Quote:** "Incremental rate: $7,000/kg"
**Verdict:** Consistent

This is the customer-facing price for small payloads. Significantly above q1 calc's internal-cost estimates ($59-878/kg depending on scenario) — the gap reflects SpaceX's margin capture on rideshare, not a contradiction of the cost model.

### Claim 3 — Rideshare history shows $500/kg/year structural increase
**Quote:** "SpaceX publicly stated that it expected rideshare pricing to increase by approximately $500 per kilogram annually to keep pace with inflation."
**Verdict:** Novel supporting

This was not anchored in my initial framework — I had assumed list prices would fall over time with Starship arrival. SatBase documents that *real customer prices have risen* 2022→2026 by ~$1,500/kg, contrary to the "Starship drives prices down" narrative. Strong evidence for the operational-ceiling scenario or for a sharp transition (gradual rise → sudden collapse when Starship matures).

### Claim 4 — Capacity constraints driving pricing
**Quote:** "High demand for Sun-Synchronous Orbit (SSO)" + "delays among emerging launch providers" + "limited near-term manifest availability"
**Verdict:** Consistent

Supports the framework's prediction that list price reflects market dynamics (margin capture) more than internal cost. SpaceX has pricing power because Starship hasn't yet undercut Falcon 9 at scale. When competitors arrive (Blue Origin New Glenn at scale, Stoke, RFA) the dynamics may shift.

### Claim 5 — FAA fees rising
**Quote:** "Beginning in 2026, proposed FAA licensing changes include payload-weight-based fees. While capped (e.g., $30,000 per launch in 2026)"
**Verdict:** Merits investigation

Small effect at current cap ($30k/launch on $74M dedicated = 0.04%; on a 22.8t payload, ~$1.3/kg). But if fees scale with launch cadence growth, the cumulative regulatory burden could matter for Starship's 1000-launches/year scenario. Worth a calc-pass sensitivity in subsequent passes.

### Claim 6 — "Falcon 9 rideshare remains one of the most cost-effective paths to orbit"
**Verdict:** Consistent (with caveat)

For small payloads <200kg, true. For larger payloads, dedicated launch is more cost-effective ($/kg basis). The article's framing is correct for its rideshare audience.

## Cross-reference

- Reinforces the case for [pass-03-reconcile.md] anchor mapping ($1,600/kg cited projection → pessimistic scenario)
- Contradicts the optimistic-late timing if extrapolated naively (a 2026 price of $7,000/kg + $500/kg/year structural increase predicts 2040 price of $14,000/kg, not $100/kg)
- Resolution: the SatBase trajectory assumes *Starship doesn't arrive*. The optimistic-late scenario assumes Starship does arrive at scale. These are different worlds, not contradictory data.
