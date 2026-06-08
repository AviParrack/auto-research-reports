# Feedback — lunar-throughput-multiplier

Avi-keyed notes for future passes. Most recent at top.

## 2026-06-08 — q1 leaf v1 finished, Avi pushed back hard on framing

The q1 v1 result ("LOX binds at 50-500× current global supply") is a demand-observation, not a supply-side ceiling. Current LOX industry is sized to current demand, not to a hard production ceiling. Saying "X is 50× current industry" doesn't establish that X is unreachable; it's the same epistemic move as saying "100M cars/year is impossible because in 1900 nobody made cars."

The real question is: **what are the fundamental (physics, thermodynamics, geography, materials) constraints on scaling each input, separately from willingness-to-scale?** Specifically:

- **LOX:** ASU is just air separation. Atmosphere is unlimited. Minimum work of separation is thermodynamic (~50 kWh/t O₂ theoretical, vs 150-800 kWh/t practical). At Tt/yr cosmic scale, electricity for ASU is ~1 TW continuous — comparable to current US grid. Is electricity the real binding constraint?
- **Methane:** Natural gas reserves finite but huge (~200× current annual consumption); methane can also be synthesised from CO₂+H₂ (Terraform Industries). Not fundamentally binding.
- **Engines:** Automotive does 80M engines/yr. No fundamental ceiling on engine manufacturing at scale.
- **Pads:** Geographic constraint — equatorial coast with downrange ocean. Earth has substantial coastline. Soft.
- **Steel:** Iron is 4th most abundant crustal element. No fundamental scarcity.
- **Helium:** Truly scarce, ~30 kt/yr global. **THIS** might be the only fundamentally-binding industrial input.
- **Argon co-production:** ASUs co-produce N₂ and Ar. At extreme scale, the Ar market saturates — could constrain ASU build-out unless you dump Ar.

The required q1 rebuild:
1. Distinguish "current industry size" (not a ceiling) from "willingness-to-scale" (capital + time, no physical ceiling) from "fundamental limits" (the real ceiling).
2. The atmospheric ceiling (q2's territory) is likely the *first* fundamental binding constraint on Earth chemical-rocket throughput, not LOX.
3. Tt/yr cosmic-scale conclusion may need to be softened from "impossible from Earth chemical" to "requires civilizational-scale capital and lead-time, AND probably saturates atmospheric chemistry well before saturation of industrial inputs."

Action: q1 calc + write re-pass with the fundamental-vs-willingness distinction. Add a new claim (q1.c12 or similar) capturing the framing correction. Update the binding-input ordering: helium is probably the only truly-physically-scarce industrial input; everything else is willingness-to-scale modulo electricity at extreme scale.

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
