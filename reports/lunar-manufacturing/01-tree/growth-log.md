# Tree Growth Log

Append-only record of who added/removed/restructured tree nodes, in what pass, and why. The current tree is in `tree.yaml`; full snapshots in `history/`.

---

## Pass 1 — Intake (2026-05-25)

**Author:** agent (claude-opus-4-7)
**Trigger:** intake pass, scoping research

### Added

- `q4-gear-ratio` — new leaf. The most important addition from intake. Metzger's 2023 Acta Astronautica paper identifies capital-mass-to-product-mass ratio (≥35×) as the dominant economic variable, not raw $/kg comparison. The original hand-written tree missed this entirely.

### Renamed / sharpened

- `q1-bulk-mass-cost` → `q1-earth-launch-cost`. Slug clearer about what it measures; question reframed to demand uncertainty bands given Starship range of $10-300/kg projections by 2040.
- `q2-lunar-ascent-cost` — question sharpened to require chemical-vs-mass-driver split (literature treats these as substantially different cost curves).
- `q3-isru-feasibility` — added explicit material list (Al/Fe/Si/Ti/glass/O2/propellant) and TRL-by-2040 framing.
- `q4-capital-buildup` → `q5-capital-buildup`. Renumbered; question now demands realistic-earliest-deployment date.
- `q5-orbital-demand` → `q6-orbital-demand`. Renumbered; question now requires split by use case (data centers, solar power, depots, deep-space).
- `q6-mass-driver-vs-rocket` → `q7-mass-driver-feasibility`. Reframed from binary choice to deployment-feasibility-before-2040 question, which is the actual literature gap. AIAA 2025 paper exists; first-gen estimates are 2040+.
- `q7-synthesis-crossover` → `q8-synthesis-crossover`. Renumbered.

### Removed

None.

### Flagged for Avi

None this pass.

### Why this shape

Intake web search identified that the literature decomposes this economic question along the gear-ratio axis (capital efficiency) more than along the raw $/kg axis. The tree now has the gear-ratio leaf as its centerpiece, with the cost leaves (q1, q2) feeding into it and the buildup/demand leaves (q5, q6) framing when the gear ratio actually pays off. Mass driver question demoted to a constraint node because its 2040+ feasibility timeline puts it outside the synthesis window for most scenarios.
