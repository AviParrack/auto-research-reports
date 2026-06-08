# Feedback — lunar-throughput-multiplier

Avi-keyed notes for future passes. Most recent at top.

## 2026-06-08 — after intake (drove tree v2)

Substantive scoping revisions to apply across all leaf passes:

1. **Earth destination reachability (q3) must cover four propulsion classes.** Primary regime: chemical methalox (Starship-like). Future regimes: ion / electric, nuclear thermal rocket, nuclear pulse propulsion. Apply symmetrically to Moon-launched cargo. Output as a propulsion × origin × destination matrix.

2. **Lunar power is not a binding constraint** (q4 deprecated). "Solar is in principle scalable beyond any limit that we would need to contend with." Treat power as an input variable inside q6, not a leaf.

3. **Mass driver throughput (q6) must include parallelization.** If single-driver cycle-life binds, the response is to build N drivers. Quantify what N is required to hit 1 Mt/yr, 100 Mt/yr, 10 Gt/yr, 1 Tt/yr throughput targets. Anchor against Casey Handmer's May 2026 mass driver post (pulsed power buffer / switches / thermal loop as the main machine; rail secondary).

4. **Receiver / catcher infrastructure is not its own question** (q7 deprecated). Mass-driver-launched payloads can carry their own propulsion (ion / chemical / NTR / NPP) for capture. Fold a brief discussion (1-2 paragraphs) into q6; the full propulsion-class analysis lives in q3.

5. **Moon-propellant allocation is two separate questions** (q8 split into q8a / q8b):
   - **q8a:** Moon supplies propellant to LEO for Earth-launched cargo. Earth pays no propellant tax to interplanetary.
   - **q8b:** Moon supplies propellant to Moon-launched cargo. Moon launches its own interplanetary missions (mass-driver-boosted, NTR ascent, or fully-propulsive chemical from regolith).
   - The synthesis (q9) compares the two allocations per destination.

## Anti-patterns explicitly relevant to this report (carried into every leaf pass)

- **#11 (calendar dates):** decompose timelines into work-remaining + acceleration sensitivity. No "by 2040" framing.
- **#2 (source borrowing in calc):** all throughput numbers derive first-principles in P2 calc; only P3 reconciles to sources.
- **#9 (bury-the-lead):** every synthesis leads with the per-destination delta in first 200 words.
- **#13 (editorialising):** state the data, don't dramatise.
