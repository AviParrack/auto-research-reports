---
pass: 5
kind: consistency
leaf: q3-isru-feasibility
date: 2026-05-25
status: done
---

# Pass 5 — Consistency (cross-leaf)

Reading sibling-leaf claims.yaml files (q1 reviewed, q4 reviewed; q2
in flight — skipped per cross-leaf protocol). Looking for direct
contradictions and time-horizon / framework mismatches.

## Q1 — Earth launch cost (reviewed)

Q1's claims describe Starship cost trajectory over 2026-2040: $107-466
per kg under partial-reuse central scenario, with refurbishment cost
as the dominant variable. Musk's $10/kg target not derivable from
Falcon-9-anchored assumptions. Industrial-explosion / TAI compression
hypothetically lowers to $15-25/kg.

### Intersection with q3

| Topic | q1 position | q3 position | Verdict |
|---|---|---|---|
| Time horizon | 2026-2040 | 2026-2040 (TAI-C / BAU / stall regimes) | **Consistent** — same horizon, q3 makes the regime decomposition explicit which q1 partially does |
| TAI-C compression framework | "industrial-explosion / TAI-grade automation pressure" with 10× refurbishment compression, 10× cadence (q1.c7) | TAI-C regime with ~10× demonstration cadence (q3.c8) | **Consistent** — same framework, same compression magnitude |
| BAU baseline | Partial scenario $107-466/kg early-to-late 2030s | BAU: carbothermal TRL 7 by 2030, TRL 8 by 2035-2040 (q3.c8) | **Consistent** — paired trajectories |
| Stall scenario | Implied "pessimistic" $354-780/kg | Explicit stall: processes stuck at 2024 baseline (q3.c8) | **Consistent** — q3 more explicit; q1 less so |
| Falcon 9 list prices rising $500/kg/year | q1.c5 (rideshare specifically per Codex flag) | n/a | **Not relevant** |

**No contradictions.** Both leaves use the TAI-C / BAU / stall framing
implicitly; q3 makes the regimes explicit and applies them to TRL
trajectory rather than just cost trajectory.

## Q4 — Gear ratio (reviewed)

Q4 establishes the gear-ratio framework: lunar capital must produce
roughly 35-50 kg/kg at GTO under Metzger's cost model, with closer
destinations easier and LEO requiring SEP architecture. Tent
sublimation exceeds threshold by order of magnitude; strip mining is
marginal.

### Intersection with q3

| Topic | q4 position | q3 position | Verdict |
|---|---|---|---|
| Gear ratio threshold φ ~35 | Contingent on Metzger's model + destination + financing (q4.c6) | MRE productivity 100 kg/yr/kg reactor mass (q3.c13) plausibly clears φ=35 over lifetime; instantaneous derated phi=10-20 (q3.c13b) | **Consistent** — q3 confirms MRE clears q4's threshold under multi-year integration |
| TAI sensitivity | "If automation compresses M_K by 10×, φ rises proportionally" (q4.c10) | Capital-mass compression listed as q4 lever in q3 calc | **Consistent** — same mechanism |
| Tent sublimation φ = 442-534 | Quoted from Kornuta + Sowers in Metzger 2023 (q4.c7) | Not directly addressed in q3 (tent sublimation is a process route I didn't primary-fetch) | **Compatible** — q3's process taxonomy includes "vapor pyrolysis" as solar-thermal, which is a tent-sublimation cousin |
| LEO chemical-only structurally hard | "Γ_LEO ≈ 14 makes LEO structurally unreachable for chemical-only" (q4.c9) | Carbothermal + MRE produce LOX at TRL 6 / 4, but q3 doesn't address delivery destination | **Compatible** — q3 is materials feasibility; delivery is q2 / q4 / q8 |
| Whether the threshold is attainable | "Yes, with established technology choices, at most cislunar destinations" (q4) | Yes — multiple processes at TRL 4-6, scaling under BAU/TAI-C (q3.c3, q3.c9, q3.c13b) | **Consistent** |
| Bottleneck framing | "Ground-truth on lunar ice deposits (q3), reliability in lunar dust, and access to public-private financing" (q4) | Polar ice prospecting gate (q3.c4); reliability and financing not directly addressed | **Consistent** — q4 already cites q3 as the ice-prospecting source |

**One important corroboration.** Q4 cites "ground-truth on lunar ice
deposits (open question for the geology)" as one of three remaining
bottlenecks — pointing directly to q3 as the source. My q3.c4
(polar prospecting gate after PRIME-1 + VIPER 2027) closes the loop.

**No contradictions.** Q4's gear-ratio framework and q3's materials
feasibility matrix are compatible; q3 provides the input (which
materials are available at which TRL) and q4 consumes it (gear ratio
threshold conditional on availability).

## Q2 — Lunar ascent cost (in flight, NOT read)

Per the leaf brief, I am NOT reading q2's in-flight artifacts. The
cross-leaf check on q2 must be deferred to a later pass after q2
completes its leaf run. Expected interaction: q2 provides the cost
numerator for lunar-to-LEO delivery; q3 provides the materials
feasibility gate that determines whether there's anything to ascend.

**Forward note for synthesis pass:** if q2 concludes that lunar
ascent cost is dominated by mass-driver vs chemical-rocket choice,
q3's carbothermal-LOX-at-TRL-6 result strongly suggests chemical rocket
ascent is viable in 2030s with locally-produced LOX. If q2's cost
trajectory diverges from this, that's a contradiction to surface.

## Hidden contradictions check

Walked through each q3 claim against q1 + q4 looking for hidden
contradictions:

- **q3.c1 (regolith O 41-44%):** No conflict. Composition not addressed
  in q1/q4.
- **q3.c2 (thermo floor 6.5; wall-plug 15-200):** No conflict. Energy
  costs not addressed in q1/q4.
- **q3.c3 (TRL distribution):** Compatible with q4's "established
  technology choices" framing.
- **q3.c4 (polar ice gate):** Corroborated by q4 ("ground-truth on
  lunar ice deposits").
- **q3.c5 (no LCH4 bulk):** No conflict. Q1 / q4 don't address methane.
- **q3.c6 (FFC Cl import):** No conflict.
- **q3.c7 (sintering TRL 5):** No conflict.
- **q3.c8 (regime trajectory):** Same framework as q1.c7 + q4.c10.
- **q3.c9 (materials rollup):** No conflict.
- **q3.c10 (mare vs highland yield):** No conflict.
- **q3.c11-c14 (factual additions):** No conflict.

## Summary

**No contradictions with any reviewed leaf.** Q3's framework is fully
compatible with q1 (cost trajectory) and q4 (gear ratio framework),
and q4 already points to q3 as the source for the lunar-ice
ground-truth question. The TAI-C / BAU / stall regime decomposition
applied in q3 (anti-pattern #11) matches the same framework q1 and q4
use implicitly.

**Forward sync:** When q2 closes its leaf, run a follow-up consistency
check on q2-q3 interactions specifically about whether chemical rocket
ascent with locally-produced LOX is viable in 2030s (q3's
carbothermal-TRL-6 result favours this).

No `contradictions_with` entries added to leaf.yaml.

## Next pass

Pass 6 (write): render the leaf report from claims.yaml.
