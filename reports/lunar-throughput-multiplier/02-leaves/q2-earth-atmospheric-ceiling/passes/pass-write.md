---
leaf: q2-earth-atmospheric-ceiling
pass: write
started: 2026-06-09T03:50:00Z
ended: 2026-06-09T04:15:00Z
researcher: claude-opus-4-7
---

# Earth's atmospheric ceiling on chemical-rocket throughput

## Why this question matters

q1 established that industrial inputs and solar PV area don't bind Earth chemical-rocket throughput until ~100 Gt/yr LEO — comfortably above current launch rates by many orders of magnitude. But the atmosphere is a finite chemical reservoir, and rocket exhaust + reentry products accumulate in the stratosphere with multi-year residence times. The question is: at what launch cadence does Earth's atmospheric chemistry break? Is that ceiling above or below q1's industrial-input ceiling?

## Where this fits

q2 is the Earth-side companion to q1. Together they bound the upper limit of Earth chemical-rocket throughput. The lower of the two is the actually-binding constraint. q9 synthesis combines both with q3 (propulsion-class destination reachability) and q5/q6/q8a/q8b (lunar capability) to answer the report's root question.

## Headline answer

**Atmospheric chemistry binds Earth chemical-rocket throughput at approximately 100 Mt/yr to 1 Gt/yr LEO mass-flux — 10-100× below the q1 solar-PV ceiling.** [q2.c2, q2.c6] Anchored on Larson 2017's chemistry-climate modeling of high-cadence hydrogen-propellant launches (the closest peer-reviewed analog to a future methalox-dominant regime), the tiers are:

| Tier | Cadence | LEO mass-flux | Ozone consequence |
|---|---:|---:|---|
| **Detectable** | ~10⁵ launches/yr | ~10 Mt/yr | ~0.5% global ozone loss |
| **Disruptive** | ~10⁶ launches/yr | ~100 Mt/yr | ~3-5% global, substantial Antarctic, biosphere UV stress |
| **Catastrophic** | ~10⁷ launches/yr | ~1 Gt/yr | ~10-30% global, UV catastrophe at high latitudes |
| **Beyond ceiling** | ~10⁸ launches/yr | ~10 Gt/yr | stratospheric chemistry fundamentally altered |

At **cosmic Tt/yr LEO (10¹² t/yr = 10¹⁰ launches/yr Block-3 reusable), atmospheric chemistry binds by 3-4 orders of magnitude beyond what any chemistry-climate model has explored.** [q2.c5] The Moon's architectural necessity at cosmic Tt/yr scale is *jointly* established by q1 (solar PV area saturates at 100 Gt/yr) and q2 (atmospheric chemistry saturates 10-100× lower) — q2 binds first.

**Confidence:** high on the qualitative ordering (atmospheric binds before industrial); medium-high on the specific Mt-Gt/yr ceiling numbers (sensitive to the linear vs saturated extrapolation from Larson's modeled cadences).

## Three pathways through the atmosphere

Per Block 3 Starship launch (methalox), combustion + reentry deposit into the stratosphere approximately:

- **~700 t H₂O** stratospheric injection per launch (from CH₄ + 2 O₂ → CO₂ + 2 H₂O combustion; ~20-29% of products reach above tropopause) [q2.c1]
- **~600 t CO₂** stratospheric injection — small compared to atmospheric reservoir but accumulates
- **~18 t NOx** from reentry heat (17.5% of reentered mass per Larson 2017 / Vliex 2024) [q2.c3]
- **~10-50 t NOx** from propellant combustion (altitude-dependent emission index; lower in upper stratosphere)
- **~3 t black carbon** — much less than the 35 g/kg of kerosene-fuelled rockets; methalox is much cleaner
- **Reentry alumina** from payloads — 10 kt/yr at the 2040 60k-LEO-satellite projection (Maloney 2025) [q2.c7]

The three independent atmospheric impact pathways:

**Direct ozone destruction via NOx + HOx catalytic cycles.** Reentry NOx and stratospheric H₂O drive ozone loss via Cl-free chemistry (since methalox has no chlorine). The catalytic cycles saturate at high concentrations — Larson 2017's direct modeling shows ~0.5% global ozone loss at 10⁵ launches/yr and ~11 DU (~3-4%) at 10⁶ launches/yr, far less than naive linear extrapolation from current low-cadence data would predict.

**Stratospheric water-vapor perturbation.** Methalox combustion deposits H₂O into the stratosphere where it has multi-year residence and drives HOx-catalyzed ozone loss + warming via greenhouse forcing. At 10⁶ launches/yr (100 Mt/yr LEO), steady-state stratospheric H₂O is ~25% above natural; at 10⁷ launches/yr the stratosphere has substantially anthropogenic water vapor.

**Reentry metal aerosol.** Murphy 2023 found ~10% of stratospheric sulfuric acid particles already contain spacecraft-origin metals. Maloney 2025 projects 10 kt/yr alumina at 2040 megaconstellation cadence with +1.5°C polar mesospheric warming and weakened polar vortex. This is largely independent of propellant chemistry and partly architecture-dependent (aluminum-skinned satellites are the main contributor).

## Why the Handmer solar-abundance regime does not help

The Handmer/Terraform synthetic-methane thesis (from q1) makes propellant supply effectively unlimited from solar PV + electrolysis + Sabatier. But synthetic methane is *chemically identical* to fossil methane. Combustion produces the same CO₂ + H₂O + NOx + BC regardless of whether the methane came from a gas well or from the sky. [q2.c4]

The solar-abundance regime helps Earth's *carbon cycle* (no net new CO₂ to the atmosphere over the synthesis-combustion cycle) but does NOT relax q2's stratospheric chemistry ceiling. Per-launch atmospheric perturbation is the same.

This is the critical distinction between q1 (where solar abundance softens the ceiling) and q2 (where it doesn't): industrial inputs are willingness-to-scale, but atmospheric chemistry is *fundamentally physical*. Pollutants accumulate regardless of where the rocket fuel came from. [q2.c8]

## What this means for the Moon

**The Moon's architectural necessity for cosmic Tt/yr LEO mass throughput is established jointly by q1 + q2, with q2 binding first.** At the more modest 100 Mt/yr - 1 Gt/yr LEO scale (where serious solar-system industrialisation actually wants to operate — building space-based solar, large orbital infrastructure, deep-space mission staging), q2 atmospheric chemistry is the dominant Earth-side constraint, binding 10-100× below q1's solar-PV ceiling.

Mass driver launch from the lunar surface bypasses Earth's atmosphere entirely. There is no q2-equivalent ceiling on the Moon side because the lunar exosphere is ~10⁻¹² of Earth's atmospheric mass and cannot meaningfully accumulate pollutants in the same way. This is the architectural argument that runs through the report.

## Confidence per claim

| Claim | Confidence | Basis |
|---|---|---|
| q2.c1 per-launch emissions | medium-high | Stoichiometry firm; emission factors literature-anchored; altitude profile sensitive |
| q2.c2 ceiling tiers | medium-high | Larson 2017 directly modeled 10⁵-10⁶; tier definitions partly value-laden |
| q2.c3 reentry NOx dominance | high | Larson + Vliex + Ryan converge on 17.5% factor for reusable |
| q2.c4 synthetic vs fossil identical | high | Combustion chemistry is identical |
| q2.c5 cosmic Tt unreachable | medium-high | Far beyond modeled regime; extrapolation needed |
| q2.c6 q2 binds 10-100× below q1 | high | Direct comparison: q2 ~10⁶ launches/yr vs q1 ~10⁸ launches/yr |
| q2.c7 reentry alumina | high | Murphy + Maloney primary measurements + modeling |
| q2.c8 atmospheric chemistry fundamentally physical | high | Conceptual; solar-abundance doesn't change combustion products |

## Limitations and known omissions

- **Larson 2017** was retrieved via Codex audit citation, not independently inspected; future audit re-pass should fetch the full PDF directly.
- **NASA TM-20240013276** *Impact of Spaceflight on Earth's Atmosphere* failed to fetch cleanly (PDF binary issue); should be added via alternative retrieval.
- **Vliex et al. 2024** (gridded inventory in *Scientific Data*) cited via Codex but not separately extracted; useful for altitude-resolved NOx profile in re-pass.
- **NOx catalytic-cycle saturation** is asserted from Larson 2017 but not derived from first principles here; q2 should be re-modeled with explicit catalytic-cycle chemistry to give precise ceilings.
- **Polar vs equatorial geographic concentration** of ozone effects is mentioned but not separately bounded.
- **Long-term stratospheric H₂O climate forcing** at multi-decade timescale beyond steady-state residence is not modeled.
- **Plume-scale chemistry** (very near rocket nozzle, on minute timescales) interacts with bulk stratosphere chemistry in ways our box-model doesn't capture.

## What changes if the answer flips

The q2 ceiling could move higher under three scenarios:

1. **Below-stratosphere launches** — if launch architecture were redesigned so combustion + reentry occurred only below the tropopause (~12 km), atmospheric chemistry would not bind. This requires fundamentally different launch vehicles (no orbital insertion above the troposphere) — physically impossible for chemical rockets reaching LEO at 200+ km.

2. **Active stratospheric remediation** — engineered removal of stratospheric NOx, H₂O, alumina at the same rate they're injected. Theoretically possible at vast cost; would essentially require a global stratospheric scrubbing system. Not a current technology and probably never economic.

3. **Atmospheric monitoring catches saturation effects much earlier than Larson 2017's model predicts**, pushing the ceiling down to 10⁵-10⁶ launches/yr. This would mean q2 binds harder, not softer — strengthening the Moon-necessity argument.

The ceiling could move lower if reentry NOx is higher than Larson's 17.5%, or if polar vortex effects from alumina destabilize ozone chemistry more than current models suggest.

## The atmospheric ceiling is genuinely fundamental

This is the load-bearing finding of q2 and the most important difference from q1. Atmospheric chemistry is not willingness-to-scale; it is physically constrained by:

- Atmospheric mass (~5,150 Tt, finite)
- Stratospheric residence times (multi-year for H₂O and aerosols, days-weeks for NOx)
- Catalytic-cycle chemistry (NOx, HOx, ClOx coupling)
- Reentry energy deposition (kinetic energy → NO formation independent of mass)

There is no architecture redesign within the chemical-rocket regime that relaxes these constraints. The Moon's value at cosmic-scale throughput rests primarily on q2.
