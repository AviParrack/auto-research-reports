---
source: metzger-autry-2022-landing-pads
tier: S
reviewed_pass: 4
reviewed_by: claude+codex
---

# Source Review: Metzger & Autry 2022/2023 — Lunar Landing Pads

## Summary

| Verdict | Count |
|---|---|
| Consistent | 2 |
| Novel supporting | 3 |
| Different conclusion | 0 |

## Claim 1: "Artemis Basecamp landing pad costs ~$229M at transport rates of $300K/kg to the lunar surface"
**Verdict:** Novel supporting
**Why:** First published dollar-figure benchmark for one specific piece of lunar surface infrastructure. Our calc doesn't separately price the landing pad (it's bundled into the "infrastructure" component), but Metzger-Autry shows that at $300K/kg transport, the pad alone is $229M. Our calc uses commercial-launch $/kg (q1 ~$2,300/kg to LS at BAU partial reuse), which is ~100x cheaper than the $300K/kg scenario; so our infrastructure-component cost is appropriately lower.

## Claim 2: "Pad cost drops to ~$130M at $100K/kg transport" and "Pad cost falls to ~$47M when transport costs drop below $10K/kg"
**Verdict:** Novel supporting
**Why:** Direct cost-vs-transport sensitivity curve. At $/kg compression of 30x, pad cost compresses ~5x. This sensitivity ratio (5x cost compression per 30x $/kg compression) is informative for q5 — it suggests our infrastructure-component is moderately sensitive but not strongly to launch cost compression. Total infrastructure cost compression is dominated by *mass* compression (better-designed equipment uses less Earth-launched mass) more than by *launch cost* compression.

## Claim 3: "The most important economic variables are the transportation cost to the lunar surface and the magnitude of program delay cost"
**Verdict:** Consistent
**Why:** Aligns with our calc's identification of $/kg-to-LS as a primary knob, and the regime-conditional time-compression as the second key knob (program delay cost).

## Claim 4: "Microwave sintering is the preferred technique for the high-temperature inner zone"
**Verdict:** Novel supporting
**Why:** A specific architectural choice with downstream mass implications: microwave sintering reduces Earth-launched mass of the pad (most material is in-situ regolith) at the cost of additional power requirement (microwave heads + power supply). For our calc, this validates the "Earth-imported portion only" treatment of infrastructure mass.

## Claim 5: "The cost depends sensitively on optimizing the mass and speed of construction equipment"
**Verdict:** Consistent
**Why:** Reinforces the load-bearing role of construction-equipment mobility-and-throughput in milestone-time and total program cost. Aligns with q5.c8 (500 kWe power sized for mobility + manufacturing) and our IE-regime time-compression argument.

## Cross-reference

- The pad-cost-vs-$/kg sensitivity curve is one of the few empirical anchors we have for "how much does each milestone cost as a function of transport cost."
- Cross-references our IE regime mass-compression — if construction equipment is mass-optimized by AI-design, the pad cost falls further than the linear-with-$/kg scaling.
- Codex anti-hallucination check: all numerical figures verified against secondary coverage; PDF body was binary-encoded and unparseable, but the cost-vs-transport-rate figures are well-attributed in multiple secondary references.
