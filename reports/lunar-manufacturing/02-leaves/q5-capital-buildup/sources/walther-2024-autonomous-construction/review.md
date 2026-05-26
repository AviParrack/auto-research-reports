---
source: walther-2024-autonomous-construction
tier: S
reviewed_pass: 4
reviewed_by: claude+codex
---

# Source Review: Walther et al. 2024 — Autonomous Construction with In-Situ Boulders

## Summary

| Verdict | Count |
|---|---|
| Consistent | 1 |
| Novel supporting | 2 |
| Not relevant | 1 |

## Claim 1: "Construction throughput approximately 174-193 m² per operational day"
**Verdict:** Novel supporting
**Why:** Provides a concrete throughput benchmark for autonomous lunar construction using one excavator. Useful for sizing the mobility/construction component of our calc and for projecting M7 (manufacturing complement operational) timing under different fleet sizes. For our 31.5 t mobility fleet, 20 rovers × 175 m²/day ≈ 3,500 m²/day throughput aggregate — well above the rate needed to build a few quarter-ring blast shields and landing pads in a single year.

## Claim 2: "1,440-1,520 operational hours to build a quarter-ring blast shield segment"
**Verdict:** Novel supporting
**Why:** Direct evidence that even with a single excavator, lunar surface construction is achievable in tens-of-days timescales rather than years. Supports IE-regime time-compression for the construction-phase milestones (M3 habitat deployment, M4 FSP installation, M5 ISRU plant pilot) which all involve some surface construction.

## Claim 3: "An excavator capable of operating in the lunar environment needs to be developed"
**Verdict:** Consistent
**Why:** Confirms the hardware-development is not yet at deployment TRL — consistent with our calc's BAU baseline assumption that we are at TRL 4-6 for these components.

## Claim 4: "Autonomous path planning using A* algorithm, greedy targeting, payload management, and terrain slope constraint enforcement"
**Verdict:** Not relevant (technical detail)
**Why:** Algorithm-stack details. Useful as evidence that the autonomy problem is well-bounded and solvable, but no direct numerical claims for q5.

## Cross-reference

- The in-situ-boulders-only construction path is the lowest-mass option for surface infrastructure — uses zero Earth-imported regolith or processed materials.
- Most useful as evidence that the construction-throughput problem is bounded and tractable, not as a direct cost benchmark.
- Pairs with Metzger-Autry 2022/2023 to bracket "what does lunar construction cost as a function of fleet design choice."
- Codex anti-hallucination check: all quoted text appears verbatim in the extract.md.
