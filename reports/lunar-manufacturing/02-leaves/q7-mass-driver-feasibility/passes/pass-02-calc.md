---
pass: 2
kind: calc
leaf: q7-mass-driver-feasibility
date: 2026-05-25
status: done
sources_sealed: true
---

# Pass 2 — Calc: Lunar Mass Driver First-Principles

**Sources sealed.** No q7 source extract is read here. The calc is built from (a) physical-law derivations (kinematics, energy, gravity), and (b) **sourced priors** from the broader engineering and economics literature (efficiency ceilings, EMALS analogue, capacitor energy density, electricity premia, mass-to-lunar-surface delivery cost). The kinematic and energy-budget arithmetic is genuinely first-principles; the cost components are sourced priors with explicit sensitivity sweeps. Per Codex pass-2 audit, the original "first-principles only" framing was overstated and has been corrected. See `pass-02-response.md` for full audit response.

Anti-pattern #11 governs the regime structure: BAU, Industrial Explosion (IE), TAI-grade, Stall. Calendar dates are not used.

## Assumptions

**Physical (laws of physics):**
- Lunar gravity $g_{\text{lunar}} = 1.62$ m/s²; lunar mass $M = 7.342 \times 10^{22}$ kg; lunar radius $R = 1737.4$ km.
- Derived lunar escape velocity $v_{\text{esc}} = \sqrt{2GM/R} = 2375$ m/s.
- Derived LLO speed $v_{\text{LLO}} = \sqrt{GM/R} = 1679$ m/s.
- Constant-acceleration kinematics: $v^2 = 2aL$, so track length $L = v^2 / (2a)$.

**Engineering-ceiling efficiencies (sensitivity range, not borrowed):**
- DARPA 45-stage coilgun demonstrated: $\eta = 0.22$.
- TRL-grounded (Wright et al. 2011 method, not the result): $\eta = 0.33$.
- Aspirational engineer-advocate (Handmer 2026 method): $\eta = 0.90$.
- Theoretical electromagnetic-conversion ceiling: $\eta = 0.96$.

**Economic priors (independently estimated, not borrowed):**
- Mass-to-lunar-surface delivery cost: $1000/kg (conservative q1-q2 framing).
- Lunar electricity: $0.50/kWh (Earth-rate ~$0.10 × ~5× lunar premium).
- EMALS per-meter Earth construction cost: ~$4M/m.
- Lunar construction multiplier: 100-1000× Earth; we use 200× (100× material premium × 2× design complexity).
- Defense-grade pulsed power capacitors: ~2 kJ/kg, ~$10/kJ at scale.

## Derivation

### Section 1: Kinematic envelope

The track length-acceleration trade is hard kinematics: for v = 1.7 km/s, a 1000g (~10,000 m/s²) acceleration profile requires a 144 m track; 100g needs 1.4 km; 20g needs 7.2 km. For v = 2.4 km/s the lengths roughly double. This is the inescapable trade between length and acceleration — for a fixed muzzle velocity, you either build a short track that beats the projectile hard, or a long track and treat it gently.

Janhunen's 2024 result (mascon-assisted catching) lets us aim at LLO (1.68 km/s) instead of escape (2.38 km/s), saving ~50% in kinetic energy per kg. This is celestial mechanics, not source-borrowed.

| Profile | Track length | Burn time |
|---|---|---|
| 1000 g, v=1.7 km/s | 144 m | 171 ms |
| 1000 g, v=2.4 km/s | 287 m | 242 ms |
| 100 g, v=1.7 km/s | 1.4 km | 1.7 s |
| 100 g, v=2.4 km/s | 2.9 km | 2.4 s |
| 20 g, v=1.7 km/s | 7.2 km | 8.6 s |
| 20 g, v=2.4 km/s | 14.4 km | 12 s |

### Section 2: Wall energy and average power

Kinetic energy per kg at 1.7 km/s is 1.41 MJ/kg; at 2.4 km/s, 2.82 MJ/kg. Wall energy is KE divided by net system efficiency $\eta$. Sensitivity sweep:

| Velocity | $\eta = 0.22$ | $\eta = 0.33$ | $\eta = 0.90$ |
|---|---|---|---|
| 1.7 km/s | 6.4 MJ/kg | 4.3 MJ/kg | 1.6 MJ/kg |
| 2.4 km/s | 12.8 MJ/kg | 8.5 MJ/kg | 3.1 MJ/kg |

Average wall power at throughput $Q$ (kg/yr), with $\eta = 0.50$ (a conservative low-end-of-aspirational assumption — NOT the arithmetic midpoint of 0.33 and 0.90, which is 0.615; per Codex audit):

| Throughput | Avg wall power, v=1.7 km/s, η=0.50 |
|---|---|
| Demonstrator: 365 t/yr | 0.033 MW |
| Pilot: 10 kt/yr | 0.89 MW |
| Operational: 1 Mt/yr | 89.4 MW |
| Aspirational: 10 Mt/yr | 894 MW |

For a 200 kg projectile launched in 171 ms at 1.7 km/s and $\eta = 0.50$, peak instantaneous power is **6.6 GW** (constant-acceleration profile: peak = 2× average over burn). At $\eta = 0.90$ this drops to 3.7 GW. This sets the capacitor-bank / flywheel pulsed-power requirement.

### Section 3: Pulsed-power capacitor bank

Energy stored per shot at 200 kg, 1.7 km/s, $\eta = 0.90$: ~315 MJ. At 2 kJ/kg defense-grade capacitor energy density, this is ~157 t of capacitors per shot. At $10/kJ, the per-shot capacitor cost is ~$3.1M. Throughput at 1 Mt/yr × 200 kg/shot = 5 million shots/yr, one shot every 6.3 s. The capacitor bank needs to recycle in ~6 s, well within state-of-art for power-electronics switching.

A 5× redundancy capacitor bank capacity = ~785 t mass × $1000/kg lunar surface premium = ~$0.8B for capacitors + shipping. This is a sub-dominant cost line, not the binding constraint.

### Section 4: Capital cost (BAU regime)

Independent component-by-component decomposition for a 1 Mt/yr, 100g track (1.4 km), $\eta = 0.50$ architecture:

| Component | Capex (BAU) | Reasoning |
|---|---|---|
| Track + drive coils | $1200B | 1500 m × $800M/m (EMALS × 200× lunar multiplier) — bottom of range |
| Reactor (200 MW class) | $3B | $2B Earth-built + $1B Earth-to-Moon shipping (1000 t) |
| Capacitor bank (5× redundancy) | $0.8B | Per Section 3 |
| Projectile manufacturing plant | $6B | $1B plant + 5kt seed × $1000/kg |
| Catcher / orbital tug | $0.15B | 50 t at 3× lunar surface premium |
| Foundation / anchor / regolith burial | $2B | Lunar surface construction |
| Control / instrumentation | $0.5B | |
| Construction labor (3-year build) | $30B | $10B/yr peak human-and-robot integration |
| **Total** | **$1242B** | |

**The track is the dominant cost line by a wide margin** — ~95% of total under the BAU lunar construction multiplier. This is the load-bearing variable. Under TAI-grade automation, ISRU-built drive coils and modular pre-fab assembly compress this by ~100×.

### Section 5: Per-kg amortized cost

Lifetime: 20 years. Throughput: 1 Mt/yr → 20 Mt total over operational lifetime.

| Component | Per-kg, BAU |
|---|---|
| Capex amortized | $62.12/kg |
| Annual power × $0.50/kWh | $0.39/kg |
| O&M (5%/yr of capex) | $62.12/kg |
| **Total** | **$124.64/kg** |

The result is dominated by capex amortization and O&M, each ~$62/kg. Power is sub-dominant. This is the BAU first-principles per-kg cost for delivering bulk mass to LLO; it does NOT yet include the SEP transfer leg from LLO to LEO (which is what q2.c5's $50/kg headline includes).

### Section 6: Regime sensitivity

| Regime | Track | Reactor mass-cost | Caps | Plant | Construction | Time to ops | Total capex | Per-kg amortized |
|---|---|---|---|---|---|---|---|---|
| BAU | 1.0× | 1.0× | 1.0× | 1.0× | 1.0× | 20 yr | $1242B | $62/kg |
| IE | 0.1× | 0.3× | 0.3× | 0.3× | 0.1× | 6 yr | $127B | $6.3/kg |
| TAI | 0.01× | 0.05× | 0.1× | 0.05× | 0.02× | 1.5 yr | $13.3B | $0.66/kg |
| Stall | 1.0× | 1.0× | 1.0× | 1.0× | 1.0× | never | $1242B | N/A |

The compression factors are illustrative scenario priors (not externally validated). They reflect the structural intuition that aggressive automation reduces capex mostly via reduced human-hours and reduced Earth-launch dependency: TAI-grade ISRU drops the track-per-meter cost ~100× because most drive-coil mass can be built locally rather than shipped from Earth.

### Section 7: Discrete engineering milestones

| Milestone | Spec | BAU | IE | TAI | Stall |
|---|---|---|---|---|---|
| M1: Earth demo at 1.7 km/s, 100 launches | Cycle life + velocity validation | 2-4 yr | 6 mo | weeks | never |
| M2: Sub-scale lunar prototype | 5-50 t mass, 100 m track, 100 kg payload | 5-8 yr | 18 mo | 6 mo | never |
| M3: Pilot kt-scale operational | 1-10 kt/yr, 10⁴-10⁵ cycle life | 10-15 yr | 3 yr | 1 yr | never |
| M4: Mt-scale operational | 1 Mt/yr, ISRU-supplied projectiles | 20-30 yr | 6 yr | 1.5 yr | never |
| M5: 10 Mt-scale nameplate | Project TERAFAB-class | 40-60+ yr | 10 yr | 2-3 yr | never |

M1 is the load-bearing pre-deployment milestone. The closest historical analog is the Navy EMRG program (32 MJ muzzle energy, Mach 7.5, cancelled 2021 after ~$500M over cycle-life and barrel-wear issues). A re-attempted Earth demonstrator at lunar-relevant velocity (1.7 km/s = Mach 5 in air) and 100-launch cycle life would address the most critical engineering uncertainty — and is the milestone Peterkin (General Atomics) explicitly identifies as the next required demo. Under BAU this is 2-4 years; under IE it compresses to months; under TAI it compresses to weeks; under Stall it never happens (the EMRG cancellation precedent suggests political will is the binding variable).

### Section 8: q2-q7 coupling — the load-bearing contradiction

**q2.c5 derives lunar-surface-to-LEO via mass driver + SEP at $50/kg (late-era) assuming $10B capital amortized over 20 years and 10 Mt/yr × 85% availability.** This first-principles q7 calc independently lands at $1242B BAU, $127B IE, $13.3B TAI. **q2's $10B capital assumption is reachable only under TAI-grade compression** — the BAU and IE regimes both produce capex that is 10-100× higher.

This means:
- q2's $50/kg headline is conditional on TAI-grade economics.
- Under BAU, the late-era lunar-to-LEO cost via mass driver is q7's $125/kg LLO + q2's SEP transfer leg (whose value the reconcile pass will explicitly bridge — not derived in this calc). The total is materially higher than $50/kg.
- The report's headline crossover claim depends critically on the acceleration regime assumed.

This is a flagged q2-q7 contradiction to be resolved in reconcile pass and surfaced in cross-consistency. The structural framing is right: the answer is regime-dependent, and the q2 headline implicitly assumes TAI. Better to make this explicit in the write pass.

**Cycle-life gap (Codex audit, accepted as high-severity load-bearing risk):** At 1 Mt/yr × 200 kg/shot, 5 million shots/yr × 20 yr lifetime = 100 million shots. At 10 Mt/yr (q2's nameplate assumption), 1 billion shots over 20 years. State-of-art demonstrated cycle life for EM launchers is ~100-1000 shots (Navy EMRG was cancelled with much less, see DSIAC 2015 source). This 5-7 orders of magnitude gap between demonstrated and required cycle life is the most under-discussed engineering risk in the mass-driver literature and binds independently of capital cost or TAI compression.

### Section 9: Dependence of the root answer

The root question — when does lunar manufacturing beat Earth launch? — depends on mass driver availability in the following structured way:

- **Under BAU / current trajectory:** mass drivers do not reach Mt-scale operational in any time horizon shorter than ~25 years; in any time window shorter than that, chemical rockets dominate the architecture regardless of mass-driver availability. The root question's answer collapses to whether the chemical-aggressive-ISRU late-era ($994/kg, q2.c3) can beat Starship-optimistic-late ($59/kg, q1). It cannot; lunar manufacturing does not beat Earth launch for bulk mass under BAU.
- **Under industrial explosion:** mass drivers reach Mt-scale in ~6 years from program start. Per-kg amortized cost at LLO drops to ~$6/kg + ~$5-10/kg SEP transfer = ~$11-16/kg to LEO. This is competitive with optimistic Starship ($59/kg) and beats partial-reuse Starship ($107/kg). Lunar manufacturing for orbital infrastructure becomes economic.
- **Under TAI-grade acceleration:** mass drivers reach Mt-scale in ~1.5 years; per-kg ~$1-5/kg. Lunar manufacturing dominates Earth launch by a substantial margin for bulk orbital infrastructure.
- **Under stall:** never reached; the question is moot.

The root answer depends on mass driver availability *only in the late-era / TAI-grade regimes*. In early-mid BAU eras, chemical rockets dominate by an order of magnitude regardless of mass driver availability.

## Result

**Headline first-principles verdict** (medium confidence on numerical specifics; high confidence on structural framing):

| Quantity | Value |
|---|---|
| Per-kg amortized cost to LLO (BAU, 1 Mt/yr, 20 yr life) | **$62/kg capex + $62/kg O&M + $0.4/kg power = $125/kg** |
| Per-kg amortized cost (IE) | $6.3/kg amortized capex |
| Per-kg amortized cost (TAI) | $0.66/kg amortized capex |
| Total capex (BAU) | $1240B (track-dominated at $1200B / 96% of total) |
| Total capex (IE) | $127B |
| Total capex (TAI) | $13.3B (within striking distance of q2's $10B assumption) |
| Time to Mt-scale operational (BAU) | 20-30 yr |
| Time to Mt-scale operational (IE) | ~6 yr |
| Time to Mt-scale operational (TAI) | ~1.5 yr |
| Time to Mt-scale operational (Stall) | never |
| Earliest critical milestone (M1, Earth demo) | 2-4 yr BAU |
| q2-q7 capital reconciliation | q2's $10B requires TAI-grade compression of q7's $1240B BAU |

**Confidence:** medium-high on the kinematic and power-budget calculations (these are physical-law derivations); medium on the engineering-ceiling efficiency assumptions; low-medium on the capital cost components (particularly the lunar construction multiplier of 200×, which is highly speculative); **speculative on the regime compression factors and on the M1-M5 milestone timelines (Codex audit accepted both as unsupported scenario priors)**.

**Load-bearing variables:**
1. **Lunar construction cost multiplier** (200× is a low-confidence midpoint; range plausibly 50×-1000×). This single variable swings the BAU capex from ~$300B to ~$6T.
2. **Net system efficiency** (22% to 90%). At the low end, energy budget is 4× higher, requires 4× larger reactor.
3. **TAI compression factors** (track 100×, construction 50×). These are scenario priors; if compression is only 10×, the TAI capex rises to ~$100B and the q2 headline collapses.
4. **q2-q7 capital coupling.** q2's $50/kg headline depends on q7's TAI-grade capex; the report's "crossover happens late" framing depends on which acceleration regime is assumed for the headline.
5. **Cycle life (Codex audit-added).** 100M-1B shot operational lifetime vs ~1000 shots demonstrated. This is independent of capital and compression — if no engineering path is found to 10⁶+ cycle life, no level of capital allocation makes the system operational.
6. **Catcher / orbit-insertion engineering** (Codex audit-added). The calc does not model launch angle dispersion, abort handling, or catcher ΔV; these are out-of-scope for q7 but would benefit from a future q7.1 sub-leaf.

**Next pass:** reconcile. Now read sources/*/extract.md and compare derived numbers to source claims. Expected disagreements: Handmer's $2-4B reactor figure vs q7's $3B (good agreement); 1979 NASA SP-428 capex projection $3.137B vs q7's $1242B BAU (huge disagreement — discuss historical optimism vs modern Wright et al. 2011 negative verdict).
