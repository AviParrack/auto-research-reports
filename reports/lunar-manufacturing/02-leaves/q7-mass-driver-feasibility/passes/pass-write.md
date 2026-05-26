---
pass: 6
kind: write
leaf: q7-mass-driver-feasibility
date: 2026-05-25
status: done
---

# Q7 — Lunar Mass Driver Feasibility

## Motivation

The question of when lunar manufacturing beats Earth launch for orbital infrastructure turns, in the late era, on a single architectural choice. Chemical rockets ascending from the lunar surface are punished by a propellant-use ratio of approximately fourteen at LEO (q4.c1) — meaning fourteen kilograms of propellant must move for each kilogram of product delivered. The mass driver was proposed in the 1970s by Gerard O'Neill and Henry Kolm as the way around that arithmetic: an electromagnetic launcher fixed to the lunar surface that fires bulk material into cislunar space using solar or fission electricity rather than imported chemical fuel. The 1979 NASA SP-428 Phase II reference design (Kolm, Fine, Mongeau, Williams) projected $3.137 billion 1979 dollars for operational capability by mid-1985. That target was not met. Forty years later, no operational lunar mass driver exists.

In 2025-2026 the concept has returned to public discourse: Elon Musk's "Project TERAFAB" announcements, Casey Handmer's May 2026 engineering brief, Phil Metzger's affirmative reception of the strategic pivot (q7.c14, q7.c10 — for the engineering specifics — and the broader Tier-B source-review). Whether that revival reflects a genuine engineering possibility or another false dawn determines whether the report's headline crossover — q2.c5's $50/kg late-era lunar-to-LEO via mass driver + SEP — is the realistic architecture or an aspirational anchor.

## Where it fits

This leaf provides the engineering feasibility analysis for the mass-driver line in q2's lunar-ascent cost spectrum. Three sibling leaves feed in: **q4** (gear-ratio) establishes that mass driver + SEP transfer is structurally required to reach LEO economically; **q3** (ISRU feasibility) confirms that raw basalt projectiles do not depend on refined-product maturity, so the mass driver's projectile material is high-TRL; **q2** (lunar-ascent-cost) integrates the mass-driver line into the overall lunar-to-LEO cost spectrum. The downstream synthesis is **q8** (crossover): when does lunar manufacturing beat Earth launch? The mass driver's availability — its capital, throughput, cycle life, and the regime of acceleration governing its construction — sets when (or whether) the crossover lands in the report's planning window.

## Headline answer

A lunar mass driver lands in the report's headline architecture **only under industrial-explosion or TAI-grade compression of capital and engineering timelines**. Under business-as-usual (BAU), the first-principles capital cost for a 1 Mt/yr operational system lands at approximately **\$1,242 billion** dominated by the multi-kilometer track at $800M/m lunar-construction-multiplied EMALS pricing. Time to Mt-scale operational under BAU is **20-30 years**, with sequential engineering milestones (Earth-based 100-launch demonstrator → sub-scale lunar prototype → kt-scale pilot → Mt-scale operational) each requiring physical lead-times that BAU compressibility cannot collapse. Under industrial explosion (~10× capital compression), the figures land at **\$127B / ~6 years**. Under TAI-grade automation (~100× compression), the figures are **\$13.3B / ~1.5 years** — within striking distance of q2.c5's $10B capital assumption.

**Confidence: medium-low.** The kinematic and energy-budget derivations are high-confidence physics; the capital cost components are low-confidence sourced-prior estimates. The regime-compression factors are speculative scenario priors. The Codex pass-2 audit appropriately downgraded the calc's confidence on these terms.

The implication for the report: **q2.c5's $50/kg late-era headline is conditional on TAI-grade economics, not derivable under BAU**. In any time horizon shorter than ~25 years under BAU progress, chemical rockets dominate the lunar-to-LEO architecture regardless of mass-driver availability. The "crossover happens late" framing in the synthesis must specify the acceleration regime it assumes.

## Body

### Kinematics and energy budget

Lunar escape velocity is 2,375 m/s; lunar low orbit (LLO) circular speed is 1,679 m/s — both derived from the lunar mass (7.342×10²² kg) and radius (1,737.4 km) via $v_{\text{esc}} = \sqrt{2GM/R}$ and $v_{\text{LLO}} = \sqrt{GM/R}$. Janhunen's 2024 result on mass-concentration gravity anomalies (arXiv:2410.09616) shows that projectiles launched at LLO speed can be caught from stable nine-day mascon-assisted orbits at equatorial nearside sites, eliminating the need to reach escape velocity and reducing the kinetic energy per kilogram by approximately fifty percent (1.41 MJ/kg at LLO vs 2.82 MJ/kg at escape).

The track length-acceleration trade is hard kinematics. For $v^2 = 2aL$, a muzzle velocity of 1.7 km/s requires 144 m of track at 1000 g, 1.4 km at 100 g, or 7.2 km at 20 g. The Handmer 2026 design lands at the 1000 g / 144 m / LLO-speed end of this envelope. Modern engineering work has converged toward sub-escape muzzle velocities with orbital tug catching, away from the 1970s O'Neill / NASA SP-428 escape-velocity-to-L5 architecture (q7.c1, q7.c2).

### System efficiency and power

Net system efficiency spans a substantial range. The DARPA 45-stage coilgun, the most-recently-documented multi-stage coilgun in the engineering literature, achieved 22 percent efficiency. Wright, Kuznetsov, and Kloesel (2011 IEEE / NASA, the load-bearing modern peer-reviewed reanalysis) used 33 percent as TRL-grounded. Handmer's 2026 engineer-advocate brief assumes 90 percent driver efficiency. The 1979 NASA SP-428 chapter claimed 96.4 percent system efficiency — a figure modern reviewers interpret as electromagnetic-conversion-only, not net system efficiency, though the SP-428 chapter itself does not explicitly limit its scope (q7.c3, source-review of nasa-mass-drivers-iii-1979 with the "Merits investigation" flag).

At 50 percent net efficiency (a conservative low-end-of-aspirational assumption — not the arithmetic midpoint), the wall energy per kg is 2.82 MJ/kg at LLO speed. At one Mt/yr operational throughput the average wall power is approximately 89 MW; at the 10 Mt/yr Handmer aspirational nameplate it rises to 894 MW. Peak instantaneous power per 200 kg shot at 1000 g is approximately 6.6 GW over 171 milliseconds — Handmer's 16 GW figure includes the loaded sled at 1000 kg total mass rather than the unencumbered 200 kg projectile baseline. Both are internally consistent within their architectural framing (q7.c4).

### Pulsed-power and capacitor bank

Energy storage per shot at 200 kg / 1.7 km/s / 90 percent driver efficiency is approximately 315 MJ. At defense-grade pulsed-power capacitor energy density (~2 kJ/kg from the broader pulsed-power engineering literature, not specifically the DSIAC source despite the qualitative pulsed-power-bottleneck framing), the per-shot capacitor mass is approximately 157 metric tonnes; with 5× redundancy and $10/kJ at scale plus Earth-to-Moon shipping, the bank capex is approximately $0.8 billion. This is a sub-dominant cost line. At one Mt/yr throughput (5 million shots per year, one shot every 6.3 seconds) the capacitor bank must recycle within ~6 seconds — well within state-of-art power-electronics switching, though thermal load, pulse shaping, and the cycle-life requirement (separate consideration below) are not addressed by switching speed alone (q7.c5).

### Capital cost decomposition (BAU)

Component-by-component first-principles estimate for a 1 Mt/yr, 100 g track (1.5 km), η=0.50 architecture. Lunar construction multiplier is 200× Earth-construction baseline (a sourced-prior with wide uncertainty range: plausibly 50× to 1000×).

| Component | Capex (BAU) |
|---|---|
| Track + drive coils (1500 m × $800M/m) | $1,200B |
| Reactor (200 MW class, Earth-built + shipping) | $3B |
| Capacitor bank (5× redundancy) | $0.8B |
| Projectile manufacturing plant (ISRU sintering) | $6B |
| Catcher / orbital tug | $0.15B |
| Foundation / anchor / regolith burial | $2B |
| Control / instrumentation | $0.5B |
| Construction labor (3-year build, $10B/yr peak) | $30B |
| **Total** | **$1,242B** |

Track plus drive coils dominate at approximately 96 percent of total. This single component is the load-bearing variable in the BAU capex — and the primary axis along which TAI compression is expected to act (modular pre-fab assembly + ISRU-built drive coils + reduced human-hours bring the per-meter cost down by approximately two orders of magnitude under TAI; ~10× under industrial explosion) (q7.c6).

### Per-kg amortized cost

At 20-year operational lifetime and 1 Mt/yr throughput (20 Mt total), the per-kg amortized cost to LLO under BAU decomposes:

| Component | Per-kg, BAU |
|---|---|
| Capex amortized over 20 Mt lifetime throughput | $62.12/kg |
| Annual power consumption × $0.50/kWh lunar electricity | $0.39/kg |
| Operations and maintenance (5% of capex per year) | $62.12/kg |
| **Total** | **$124.64/kg** |

This is the BAU first-principles per-kg cost for delivering bulk mass to LLO. It does not include the SEP transfer leg from LLO to LEO that q2.c5 includes in its $50/kg headline — the reconcile pass deferred that bridge as an explicit reconciliation rather than an extrapolation. The figure substantially diverges from q2's $50/kg only under BAU; under TAI-grade compression the two converge structurally (q7.c7).

### Regime sensitivity

The four-regime framework (q7.c8; consistent with q1.c7, q3.c8, q4 on cross-leaf regime treatment):

| Regime | Capex compression | Total capex | Time to Mt-scale | Per-kg amortized capex |
|---|---|---|---|---|
| Business-as-usual | 1.0× baseline | $1,242B | 20-30 yr | $62/kg |
| Industrial explosion | ~10× | $127B | ~6 yr | $6.3/kg |
| TAI-grade | ~100× | $13.3B | ~1.5 yr | $0.66/kg |
| Stall | 1.0× (never built) | — | never | N/A |

The TAI-grade endpoint converges with two independent reference points: q7.c8's $13.3B sits within an order of magnitude of q2.c5's $10B capital assumption (q7.c8, q7.c11) and matches the 1979 NASA SP-428 figure inflated to 2026 dollars ($3.137B 1979 ≈ $13B 2026, per q7.c12). This convergence is consistent with the interpretation that the 1979 baseline projection implicitly assumed engineering compression that the 1979-2025 historical record did not realize. Wright et al. 2011 provided the TRL-grounded reanalysis with the negative cost-benefit verdict ("the conclusion, however, is not as favorable for LEML as originally suggested") — this is the load-bearing modern primary source supporting the BAU pessimism (q7.c12).

### Engineering milestones

Five sequential physical milestones must be crossed before operational deployment. Timelines per regime (scenario priors, not externally validated):

| Milestone | Specification | BAU | IE | TAI |
|---|---|---|---|---|
| M1 — Earth-based demonstrator | 1.7 km/s muzzle, 100 launches without component replacement | 2-4 yr | 6 mo | weeks |
| M2 — Sub-scale lunar prototype | 5-50 t mass, 100 m track, 100 kg payload, 10 launches | 5-8 yr | 18 mo | 6 mo |
| M3 — Pilot kt-scale operational | 1-10 kt/yr, 10⁴-10⁵ cycle life | 10-15 yr | 3 yr | 1 yr |
| M4 — Mt-scale operational | 1 Mt/yr, ISRU-supplied projectiles | 20-30 yr | 6 yr | 1.5 yr |
| M5 — 10 Mt-scale nameplate | Handmer aspirational, Project TERAFAB-class | 40-60+ yr | 10 yr | 2-3 yr |

Peterkin (General Atomics, EMALS builder) identified M1 as the next required demonstration: "to prove viability, we need to demonstrate that this approach can achieve a lunar orbit speed for at least 100 launches without needing to replace launcher components." The closest historical analog is the Navy EMRG program (32 MJ muzzle energy, Mach 7.5, cancelled 2021 after approximately $500M over cycle-life and barrel-wear issues) — a sobering precedent. SpinLaunch, the most-funded modern private Earth-based kinetic launcher, has demonstrated 10,000 g acceleration survival for a 1U CubeSat (August 2025) after $150M+ and a decade of development, then strategically pivoted to chemical-rocket delivery for its Meridian constellation. These historical analogs are consistent with q7's BAU M2-M3 estimate of 10-15 years from program start to pilot-scale operational; political will, capital scale, and engineering closure are all binding (q7.c9, q7.c15).

### Cycle-life gap — the binding engineering risk

The single most under-discussed engineering risk in the mass-driver literature is the cycle-life gap between demonstrated and operational requirements. At 1 Mt/yr × 200 kg/shot × 20 yr lifetime, the system requires approximately 100 million shots. At 10 Mt/yr (q2's nameplate assumption), approximately one billion shots over 20 years. State-of-art demonstrated cycle life for EM launchers is approximately 100-1,000 shots — the Navy EMRG cancellation rationale cited cycle-life and barrel-wear as the binding failure modes (DSIAC 2015). Handmer's 2026 engineering brief contains the strongest single-source corroboration: "sintered magnet blocks 9 m long under 1000 g shear and oscillating tension fatigue is not obviously feasible."

This 5-7 orders of magnitude gap between demonstrated and required cycle life is independent of capital cost and TAI compression. No level of capital allocation builds an operational mass driver if the underlying engineering does not close a path to 10⁶-10⁹-shot cycle life. This gap is the most critical engineering uncertainty in the feasibility analysis, and it would benefit from a dedicated q7.1 sub-leaf in a future tree-pass (q7.c10).

### Alternative architecture: the lunar space elevator

The root question — when does lunar manufacturing beat Earth launch? — does not strictly depend on mass-driver availability. Pearson, Levin, Oldson, and Wykes (NIAC Phase II Final Report, 2005) demonstrated that a lunar space elevator using commercially available M5 fiber (Kevlar-class para-aramid) is technically feasible without requiring carbon nanotubes. A 30 mm × 0.023 mm M5 ribbon supports 2,000 kg at the lunar surface and 100 cargo vehicles of 580 kg each distributed along the length. Climbing-vehicle energy demand drops from approximately 10 kW at the surface to under 100 W at seven percent of the distance to L1. The 2005-2025 historical record — zero commercial follow-on after NIAC funding ended, LiftPort 2019 reporting "no progress beyond the lunar elevator company's conceptualized design" — is consistent with the binding constraint being capital and program commitment rather than physics (q7.c13). The lunar elevator avoids the cyclic-load fatigue, GW-scale pulsed power, and precision projectile-capture problems of a mass driver; it is the canonical alternative architecture for cis-lunar bulk transport.

### Public-figure positions (tier-B summary)

Modern public-figure positions on lunar mass drivers (mid-2020s), per q7.c14 and the source-review tier-B treatment:

- **Robert Peterkin** (General Atomics EMS, EMALS builder): credentialed industry-engineering voice; identifies the M1 milestone explicitly; advocates evolution of EMALS toward lunar EM launch as the next funded R&D step.
- **Elon Musk**: SpaceX/Tesla/xAI strategic commitment via "Project TERAFAB" (Feb-May 2026), but no funded engineering program. Aspirational figures: $500/kg, 500-1000 TW/yr of AI satellite deployment, "Path to Petawatts." Musk's personal lifetime-horizon framing ("I want to live long enough to see it") is consistent with q7's BAU decades-scale assessment. The 500-1000 TW/yr capacity claim sits 100-1000× above Handmer's 10 Mt/yr nameplate (under reasonable mass intensity assumptions) and is contradicted by q7's BAU and IE regimes; under aggressively low kg-per-kW assumptions for ultra-thin satellites the gap closes, but the figure is not engineering-grounded.
- **Phil Metzger** (UCF, canonical academic on lunar manufacturing economics, q4 anchor source): qualitative paradigm-level affirmation of Musk's pivot. Does not address engineering feasibility timeline or capital. Meaningful as a signal that the strategic pivot has academic validation.
- **Casey Handmer**: load-bearing modern engineer-advocate. The May 2026 engineering brief is the closest thing the literature has to a contemporary technical design. Headline economics are aspirational (10 Mt/yr nameplate, $10/kg "rocks in lunar orbit") but the engineering caveats are explicit ("not obviously feasible" magnet fatigue).

### Dependence of the root question

The root question's answer — when does lunar manufacturing beat Earth launch for orbital infrastructure? — depends on mass-driver availability only in the late-era / TAI-grade regimes. Under BAU and any time horizon shorter than approximately 25 years, the engineering milestones M2-M5 require sequential physical lead-times that BAU compressibility cannot collapse, so mass drivers do not reach Mt-scale operational regardless of investment level. In that case chemical rockets dominate the lunar-to-LEO architecture and the root question's answer collapses to whether chemical-aggressive-ISRU late-era ($994/kg per q2.c3) can beat Starship-optimistic-late ($59/kg per q1) — which it cannot at scale.

Under industrial explosion, mass drivers reach Mt-scale operational in approximately six years; per-kg amortized capex drops to approximately $6/kg at LLO; with the q2-derived SEP transfer leg added, the lunar-to-LEO figure is competitive with optimistic Starship and beats partial-reuse Starship. Lunar manufacturing for orbital infrastructure becomes economically rational. Under TAI-grade compression, the same milestones complete in approximately 1.5 years and the per-kg figure drops to approximately $0.66/kg amortized. Under stall, the question is moot.

The mass driver is therefore a **scenario-conditional load-bearing variable** for the report's headline crossover. The report's central architectural argument (q4 → q7 → q2 → q8) is internally consistent, but its quantitative headline is conditional on the acceleration regime the synthesis assumes (q7.c11).

## Confidence per finding

| Claim | Confidence | Reasoning |
|---|---|---|
| q7.c1: kinematic constants (escape, LLO, energy per kg) | high | First-principles physics |
| q7.c2: kinematic track-acceleration trade | high | First-principles physics |
| q7.c3: efficiency range (22-90%) | medium | Engineering ceiling sourced-priors |
| q7.c4: average and peak power | high | First-principles given efficiency assumption |
| q7.c5: capacitor bank parameters | medium | Engineering priors + first-principles arithmetic |
| q7.c6: BAU capex decomposition ($1,242B) | low | Track-per-meter sourced-prior has wide uncertainty (50×-1000×) |
| q7.c7: BAU per-kg amortized ($125/kg) | low | Inherits q7.c6 uncertainty plus O&M scenario assumption |
| q7.c8: regime sensitivity capex / time-to-ops | speculative | Compression factors are scenario priors per anti-pattern #11 |
| q7.c9: M1-M5 milestones | speculative | Scenario construction; cycle-life-gap caveat applies |
| q7.c10: cycle-life gap (100M-1B shots required, ~1000 demonstrated) | medium-high | Codex audit-surfaced; strong source corroboration (Handmer, DSIAC, Navy EMRG cancellation) |
| q7.c11: root-question dependence (regime-conditional) | medium | Structural finding; survives source-review |
| q7.c12: historical 1979-2011 NASA arc | high | Documented in primary sources |
| q7.c13: lunar elevator alternative architecture | high | Documented in NIAC Phase II report |
| q7.c14: public-figure positions | medium-high | Quoted statements verified in extracts |
| q7.c15: SpinLaunch analog | high | Documented in trade press |

## Limitations

**Numerical:**
- Track per-meter cost (200× lunar multiplier on EMALS Earth pricing) is the single most uncertain input. Plausible range 50×-1000×; the BAU capex swings from $300B to $6T across this range.
- Regime-compression factors (track 100× under TAI, construction 50×) are scenario priors with no external calibration. If TAI compression is only 10×, the TAI capex rises to $100B and the q2.c5 headline collapses.
- The Acta Astronautica 1980 O'Neill-Kolm paper and AIAA 2025-4123 paper were not fully fetched in this iteration; the latter in particular would provide the most recent peer-reviewed sizing anchor.

**Engineering:**
- The cycle-life gap (10⁶-10⁹ shots required vs ~10³ demonstrated) is the binding constraint. q7 does not derive a path to closing this gap — that should be a dedicated q7.1 sub-leaf in a future tree-pass.
- The calc derives muzzle velocity and energy budget, not full orbit-insertion engineering. Launch angle dispersion, abort handling, catcher ΔV requirements, and trajectory precision (Janhunen mascon-orbit + tug catching architecture) are out of scope here. The Handmer 2026 design flag on "velocity dispersion >10⁻⁴ makes projectiles orbital debris" requires dedicated treatment.

**Architectural:**
- The lunar space elevator alternative (Pearson NIAC 2005) is not deeply explored in this leaf. If the elevator is more easily engineered than the mass driver, the q4 → q7 → q2 chain has a competing branch.
- The mass-driver-vs-chemical-only choice in q2 is itself conditional on the regime: under BAU neither path delivers a Mt-scale lunar industry within the planning horizon, and the report's central question collapses to "Earth launch wins indefinitely."

**Methodological:**
- The "first-principles" framing in the original calc was overstated; many inputs are sourced priors. Codex pass-2 audit accepted this; the calc and write are now properly labeled.
- One Codex-flagged hallucination on a Wright efficiency quote was caught and corrected in source-review.
- The Acta Astronautica 1980 and AIAA 2025-4123 PDF fetches are pending; bibliographic anchors are in place but full Tier-S claim-by-claim review awaits.

**What could change the answer:** A breakthrough in cycle-life engineering (specifically the magnet-fatigue and barrel-wear problems flagged by Handmer 2026 and DSIAC 2015) would substantially upgrade the BAU feasibility verdict — possibly by an order of magnitude. A demonstrated kg-per-kW reduction for AI satellites to ≤0.1 kg/kW would partially reconcile Musk's 500-1000 TW/yr claim with q7's BAU envelope. A funded national-program-scale capital commitment to mass-driver engineering (comparable to the Apollo program's $250B equivalent 2026 dollars, not the EMRG program's $500M) would shift the BAU timeline toward the IE regime. None of these conditions is currently met.

## Flag for Avi

- **q2-q7 capital contradiction (load-bearing):** q2.c5's $10B mass-driver capital implicitly assumes TAI-grade engineering compression; q7.c6 explicitly enumerates the $1,242B BAU baseline. The cross-consistency / synthesis pass should foreground this. The report's headline crossover ($50/kg late-era via mass driver + SEP) is conditional on the acceleration regime — under BAU the crossover does not happen, period.
- **Cycle-life gap as candidate sub-leaf:** q7.1 should investigate specific engineering paths to 10⁶-10⁹-shot cycle life. This is the binding constraint and the most under-discussed risk.
- **Missing primary sources:** O'Neill-Kolm Acta Astronautica 1980 PDF; AIAA 2025-4123 full PDF; SP-428 efficiency-claim subsystem breakdown. All worth fetching in a future iteration.
- **Public-figure calibration:** Musk's 500-1000 TW/yr / $500/kg figures are aspirational, not engineering-grounded; the report should distinguish strategic-direction-from-principal vs. engineering-feasibility-claim.
