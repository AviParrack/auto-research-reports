---
source: handmer-mass-driver-2026
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: Handmer "How to build a lunar mass driver" (May 2026)

## Summary

| Verdict | Count |
|---|---|
| Consistent | 4 |
| Different conclusion | 1 |
| Novel supporting | 1 |
| Merits investigation | 1 |
| Not relevant | 0 |

## Claim 1: 200 kg per shot at 1 t/3 s cadence
**Quote (from extract):** "Per-shot payload: ~200 kg of moon rocks per launch... 1 tonne every 3 seconds."
**Verdict:** Consistent
**Why:** Matches my mass-driver throughput assumption directly. q2.c11 carries this anchor.

## Claim 2: 128 m main track, 1000 g acceleration tolerance
**Source content (verbatim from extract's "Mass Driver Length & Acceleration" block):** "Track length: 128 m" and "Acceleration tolerance: ~1000 g for monolithic rock projectiles". The companion direct quote in the extract reads "If rocks can survive 1000 gs of acceleration (they can) then the launch track need only be 128 m long."
**Verdict:** Consistent
**Why:** Engineering envelope check — well within demonstrated mass driver acceleration regimes (Wikipedia's 5,600 g theoretical envelope is much higher). Captured in q2.c11.

## Claim 3: 2.4 MJ/kg energy at 90% driver efficiency
**Quote:** "Kinetic power: 450 MW (assuming 90% driver efficiency)."
**Verdict:** Consistent
**Why:** 450 MW / (1 t/3 s) = 1.35 MJ/kg kinetic; at 90% efficiency the input is 1.5 MJ/kg. The 2.4 MJ/kg canonical Lunarpedia figure assumes higher launch velocity or more losses — both estimates are physically consistent and order-of-magnitude matched.

## Claim 4: $10/kg "rocks in lunar orbit" assumed product price
**Quote:** "$10/kg is the assumed price for 'rocks in lunar orbit' delivered to customers."
**Verdict:** Different conclusion
**Why:** Handmer's $10/kg is **assumed**, not derived. My calc says lunar-surface-to-LEO is $50/kg at late-era mass-driver scale — and Handmer's figure is to lunar orbit, not LEO. The two prices are for different destinations. Captured in q2.c11 and the reconcile pass disagreement-1.

## Claim 5: $2-4B reactor cost, 10× lunar-build premium
**Quote:** "Estimated reactor cost: $2-4 billion on Earth; a 450+ MW lunar reactor estimated at ~10x Earth operating costs."
**Verdict:** Novel supporting
**Why:** My calc lumped capital at $10B aggregate. Handmer's breakdown ($2-4B Earth-built reactor × 10 = $20-40B lunar reactor, plus track + infrastructure) suggests my $10B figure may be low by 2-4×. Carried to q2.c11 with the explicit caveat that the $10B is my extrapolation.

## Claim 6: "$500/kg launch cost is only 5% of total satellite deployment cost"
**Quote:** "At even $500/kg, launch cost is only 5% of the total satellite deployment cost, so a lunar mass driver is unlikely to drastically improve the economics of space-based AI."
**Verdict:** Merits investigation
**Why:** This is a strong claim about the commercial irrelevance of cheap launch for high-value payloads. Important for the synthesis pass (q8) — it implies that even if lunar mass driver achieves $10/kg, it doesn't transform the satellite economy unless launched mass dominates total cost. Bulk material applications (lunar regolith for shielding, water for propellant) are different.

## Anti-hallucination check

All quotes above appear verbatim in [extract.md](extract.md). No hallucinated content.
