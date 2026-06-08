# Tree growth log

## v1 → v2 (pass 2, tree-pass) — 2026-06-08

Driven by Avi's feedback after intake. Source: conversation transcript, `feedback.md`.

### Deprecated
- **q4-lunar-power-ceiling** — Avi: "the lunar power ceiling is relatively less interesting since in principle solar is sort of scalable beyond any limit that we would need to contend with. I don't think I'm interested in trying to answer this question." Power becomes an *input* to q6 (driver throughput = f(P, v_e, duty, cycle, thermal)), not a leaf in its own right.
- **q7-receiver-infrastructure** — Avi: "you could just launch vehicles that have their own propulsion systems… It could just tuck into a sub part of some other analysis." Catcher infrastructure becomes a brief subsection inside q6; the propulsion-class analysis that subsumes it lives in q3.

Both deprecated nodes remain in `tree.yaml` with `status: deprecated` per the spec's "deprecate, don't delete" convention. Their leaf folders are retained for git history but will not be filled in.

### Expanded
- **q3-earth-destination-reachability** — was: chemical-rockets-only, Earth-side only. Now: propulsion × origin × destination matrix. Four propulsion classes (chemical methalox primary; ion / electric; nuclear thermal; nuclear pulse propulsion). Both Earth-launched and Moon-launched cargo. Starship-like regime is the load-bearing baseline; the exotic regimes are future-regime sensitivities.
- **q6-mass-driver-throughput** — was: first-principles power → throughput for one driver. Now: same calc *plus* parallelization (N drivers when single-driver cycle-life binds) *plus* brief catcher/receiver subsection (the deprecated-q7 content folded in). Casey Handmer's May 2026 post (pulsed power buffer as the main machine) is the primary external anchor.

### Split
- **q8-moon-as-supplier** (v1) → **q8a-moon-propellant-for-earth-launched** + **q8b-moon-propellant-for-moon-launched** (v2). Avi: "We should compare the case where the Moon uses all its propellant production to increase the mass throughput from the Moon. And we should look separately at the case where the Moon uses its propellant production to supplement mass throughput from Earth and see what that looks like." The two allocations are genuinely different optimization problems and the synthesis comparison is the interesting answer.

### Unchanged
- q1-earth-industrial-ceiling
- q2-earth-atmospheric-ceiling
- q5-lunar-materials-ceiling
- q9-synthesis-cosmic-multiplier (dependency list updated to reflect new tree)

### Tree shape after v2
- 7 active nodes (q1, q2, q3, q5, q6, q8a, q8b) + 1 synthesis (q9)
- 2 deprecated (q4, q7) retained for history
- All depth 1; no depth-2 expansion yet
