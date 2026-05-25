---
pass: 2
kind: calc
leaf: q3-isru-feasibility
date: 2026-05-25
status: done
sources_sealed: true
---

# Pass 2 — Calc (sources sealed)

## Method

First-principles derivation of the materials × processes × TRL feasibility
matrix. The Python script ([pass-02-calc.py](pass-02-calc.py)) computes:

1. Regolith oxygen mass fraction from oxide-phase decomposition (canonical
   composition assumptions, *not* drawn from any source extract).
2. Thermodynamic energy floor per kg O2 to liberate from each oxide via
   Gibbs free energy at ~1600 K (Ellingham-style).
3. Process-by-process feasibility judgement: operating temperature,
   wall-plug energy, Earth-import dependencies, and a three-regime TRL
   decomposition (TAI-compression / BAU / stall).

Sources sealed means: I did not consult `sources/*/extract.md` while
deriving any of the numbers below. Pass 3 reconciles.

## Assumptions

**Regolith composition (canonical, will reconcile in pass 3):**

| Phase     | Mare basalt (wt%) | Highland anorthosite (wt%) | Polar PSR (wt%) |
|-----------|------------------:|---------------------------:|----------------:|
| SiO\(_2\) | 45.0 | 45.5 | 45.0 |
| Al\(_2\)O\(_3\) | 12.0 | 21.0 | 20.0 |
| FeO | 18.0 | 6.0 | 7.0 |
| MgO | 10.0 | 10.0 | 10.0 |
| CaO | 11.0 | 14.5 | 14.0 |
| TiO\(_2\) | 4.0 | 0.5 | 0.7 |
| Ilmenite (vol%) | 7.5 | 0.5 | 0.7 |
| H\(_2\)O volatiles | — | — | 0.1-5.0 (uncertain) |

**Thermodynamic data:** \(\Delta G_f\) for each oxide at ~1600 K from
standard Ellingham-diagram intercepts:

| Oxide | \(\|\Delta G_f\|\) (kJ/mol oxide) |
|---|---:|
| SiO\(_2\) | 700 |
| Al\(_2\)O\(_3\) | 1300 |
| FeO | 180 |
| MgO | 500 |
| CaO | 550 |
| TiO\(_2\) | 750 |

**Process families considered:**
- Ilmenite H\(_2\) reduction (FeTiO\(_3\) + H\(_2\) → Fe + TiO\(_2\) + H\(_2\)O)
- Carbothermal reduction (SiO\(_2\) + 2 C → Si + 2 CO; closed-loop CH\(_4\)/H\(_2\)O recovery)
- Molten regolith electrolysis (whole-silicate melt, inert anode)
- FFC Cambridge molten-salt electrolysis (oxide pellets in CaCl\(_2\) bath)
- Vapor-phase pyrolysis (solar-thermal at >2000°C)
- Polar ice extraction + H\(_2\)O electrolysis (the only lunar-derivable H\(_2\) route)
- Sintering / vacuum casting (structural, not O\(_2\) producing)

## Derivation

### Oxygen content of regolith

For an oxide \(M_xO_y\) at weight fraction \(w\), the oxygen mass fraction
contributed to bulk regolith is

\[
f_O(\text{oxide}) = w \cdot \frac{y \cdot M_O}{x \cdot M_M + y \cdot M_O}.
\]

Summing over the six dominant oxides gives bulk oxygen mass fractions
**Mare 42.3%**, **Highland 43.8%**, **Polar 43.2%** — i.e., every
silicate phase carries 41-44% O by mass, *independent of region*. This is
why any whole-regolith oxygen process is geographically agnostic.

### Thermodynamic floor per oxide

For each oxide, the minimum energy to dissociate per kg O\(_2\) is

\[
E_{\min} = \frac{2 \cdot \|\Delta G_f\|}{n_O} \cdot 31.25\;\text{mol O}_2/\text{kg} \cdot \frac{1}{3600}\;\text{kWh/kJ}.
\]

Results: SiO\(_2\) 6.08, Al\(_2\)O\(_3\) 7.52, FeO 3.12, MgO 8.68, CaO 9.55,
TiO\(_2\) 6.51 — all in kWh/kg O\(_2\).

### Whole-regolith MRE energy floor (mare basalt feedstock)

Mass-weighted across mare oxides: **floor = 6.5 kWh/kg O\(_2\)** as a
*pure-oxide lower bound under ideal Gibbs dissociation*. Total O liberated
from 1 kg mare regolith = **423 g**.

This is the thermodynamic floor for an ideal process. Real MRE reactors
operate at 5-10× this floor due to: (a) melt activities (oxides interact
non-ideally in molten silicate, raising the effective \(\Delta G\)),
(b) alloy formation at the cathode (Fe-Si alloy is slightly more stable
than separated metals), (c) anode overpotential (~0.5 V at practical
current density), (d) Joule heating losses in the bath, (e) heat-to-melt
sensible heat at 1600°C, and (f) balance-of-plant ancillaries. Codex
audit (May 2026) flagged this distinction explicitly; the floor should
not be read as a reactor energy prediction.

### Process feasibility matrix

| Process | Region | T (°C) | kWh/kg O\(_2\) (wall) | TRL 2026 | TRL 2030 (TAI-C) | TRL 2030 (stall) |
|---|---|---:|---:|---:|---:|---:|
| Ilmenite H\(_2\) reduction | mare | 1050 | 15-30 | 5 | 8 | 5 |
| Carbothermal reduction | any | 1700 | 50 | 6 | 8 | 6 |
| Molten regolith electrolysis | any | 1600 | 60 | 4 | 7 | 4 |
| FFC Cambridge electrolysis | any | 900 | 40 | 4 | 6 | 4 |
| Vapor-phase pyrolysis | any | 2500 | 150 | 3 | 5 | 3 |
| Polar ice + electrolysis | polar | 200 | 80 | 4 | 7 | 4 |
| Sintering / vacuum casting | any | 1100 | — | 5 | 8 | 5 |

(TRL 2026 estimates are derived from public demonstration cadence and
NASA SBIR program landscape, not from any sealed source — pass 3 will
reconcile against the NASA Sanders 2025 progress report and other
extracts.)

### Materials × best route

| Material | Best lunar route | TRL 2026 (best) | Earth imports steady-state |
|---|---|---:|---|
| O\(_2\) | Carbothermal (Sierra TRL 6) | 6 | small — CH\(_4\) makeup (closed loop) |
| Fe | MRE coproduct or ilmenite reduction | 5 | minimal |
| Si | MRE coproduct or carbothermal | 6 | minimal |
| Al | FFC Cambridge on anorthite | 4 | chlorine (structural import) |
| Ti | FFC Cambridge on ilmenite | 4 | chlorine |
| Mg | MRE coproduct (minor) | 4 | minimal |
| Glass | Vacuum sintering + vapor pyrolysis | 5 | minimal |
| Structural blocks | JPL Sinterator + 3D sintered regolith | 5 | minimal |
| LOX propellant | Any O\(_2\) process | 6 | makeup gases |
| LH\(_2\) propellant | Polar ice → electrolysis (only route) | 4 | none if VIPER closes resource question |
| LCH\(_4\) propellant | No bulk lunar carbon | n/a | ALL carbon imported (or no-go) |

### Earth-import dependency taxonomy

- **Low import (steady-state):** Ilmenite H\(_2\) reduction, carbothermal,
  MRE, vapor pyrolysis, sintering, polar ice. Each needs a small initial
  charge (H\(_2\), CH\(_4\), or O\(_2\) seed) plus periodic replacement of
  refractory hardware; none requires bulk consumables ongoing.
- **High import (structural):** FFC Cambridge — chlorine for the CaCl\(_2\)
  electrolyte. Chlorine is trace on the Moon; aggressive salt recycling
  required for lunar-economic operation. This is a hard structural
  difference and the reason MRE is preferred for whole-regolith Si + Fe +
  Al even though FFC has cleaner separation of individual metals.
- **No lunar route at bulk scale (architectural blocker for LCH\(_4\)):**
  Bulk carbon. Lunar carbon in regolith is solar-wind-implanted at ppm
  levels — not minable for bulk propellant. Polar PSR craters may hold
  trapped CO and CO\(_2\) ices at meaningful (kg-per-tonne-regolith) local
  scale, but the resource is prospecting-limited and exhaustible. LCH\(_4\)
  propellant is therefore not a bulk lunar ISRU product under any
  acceleration regime; carbon must come from Earth import, asteroid
  retrieval, or limited polar volatiles. This is the strongest *negative*
  feasibility result of the calc.

## Acceleration-regime TRL decomposition (anti-pattern #11)

This decomposition is a regime-conditional framework, not a first-
principles derivation. It is the q3 deliverable for q4/q8 cross-leaf
synthesis: q4's gear-ratio framework depends on which regime obtains.
Codex audit flagged the regime numbers (10× cadence, TRL 8 by 2028-2030)
as unsupported by the thermodynamic calc; that flag is accepted — the
specific rates below are illustrative, not measured.

**TAI-compression scenario (TAI-C):** Demonstration cadence rises ~10×.
Each MRE/carbothermal iteration that took 18 months collapses to 6-10
weeks. Earth-feedback via CLPS missions tightens to 2-3 lunar
demonstrations per year. Capital-mass compression (the q4 lever) cuts
plant dry-mass by 5-10×. Under this regime:
- Carbothermal and MRE reach **TRL 8** (flight-demo'd, returning product
  to Earth orbit or to depot) by 2028-2030.
- Sintering-based structural fabrication reaches **TRL 8** for habitat-
  scale outputs by 2030.
- FFC Cambridge reaches **TRL 6** if the chlorine recycling problem is
  solved by TAI-grade chemistry optimisation.

**Business-as-usual (BAU):** NASA budget constrained, Artemis slips ~1
year per calendar year. CLPS delivers O2-ISRU demos but no product flow.
- Carbothermal reaches **TRL 7** by 2030, TRL 8 by 2035-2040.
- MRE reaches **TRL 6-7** by 2030, TRL 8 by 2035-2040.
- FFC Cambridge stays at lab + simulant-pellet level; lunar TRL 4.

**Stall (50-year-Apollo-drought analog):** Political will collapses.
- Carbothermal stuck at TRL 6 indefinitely (Sierra Sept 2024 demo
  becomes the high-water mark for the decade).
- MRE stuck at TRL 4. Helios + Lunar Resources lose funding; lab work
  continues but no lunar surface deployment.
- No lunar product flow at any horizon. q4's cost numerator becomes
  meaningless because no product exists to ascend.

The q3 deliverable for q4/q8 synthesis is therefore:

> Under TAI-C or BAU, O\(_2\) and Fe + Si bulk-mass ISRU are TRL-feasible
> by 2030-2035 with structural Al + Ti following 5-10 years behind.
> Under stall, q4's gear-ratio framework has no economic referent.
> The acceleration regime, not the calendar year, determines feasibility.

## Results — derived claims for claims.yaml

1. Every silicate region of the Moon (Mare, Highland, Polar) carries 41-44%
   oxygen by mass; whole-regolith O\(_2\) processes are geographically
   agnostic.
2. The thermodynamic floor for whole-regolith MRE on mare basalt is
   6.5 kWh/kg O\(_2\); wall-plug operation is realistic at 40-150 kWh/kg
   O\(_2\) depending on process.
3. Carbothermal reduction is the highest-TRL lunar O\(_2\) process as of
   2026 (TRL 6, Sierra Space Sept 2024); MRE and ilmenite reduction sit at
   TRL 4-5.
4. The only lunar-derivable rocket-fuel hydrogen route is polar ice
   electrolysis; the resource is geologically prospecting-limited (PRIME-1
   incomplete; VIPER target 2027).
5. Lunar methane propellant has no native carbon source at bulk scale;
   LCH\(_4\) is not a lunar ISRU product under any regime.
6. FFC Cambridge electrolysis is the cleanest route to individual structural
   metals (Al, Ti) but the chlorine electrolyte is a structural Earth-import
   dependency that MRE avoids.
7. Sintering / 3D-printed regolith reaches structural-mass output at
   TRL 5-8 across regimes; this is the route for habitat-scale structural
   elements distinct from refined metals.
8. The TRL trajectory for every process is acceleration-regime dependent,
   not calendar-year dependent. Under stall, no process advances beyond
   2024 baseline; under TAI-C, several reach TRL 8 by 2028-2030.

## Confidence

- **High:** Oxygen mass fraction of regolith (basic stoichiometry, robust to
  any plausible composition error within bounds).
- **High:** Thermodynamic floor calculation per oxide (textbook physical
  chemistry, error bands narrow).
- **Medium:** Wall-plug energy estimates per process (literature-anchored
  ranges, will reconcile in pass 3).
- **Medium:** Current TRL assignments (Sierra Space TRL 6 is public; MRE
  TRL 4 is consensus; ilmenite TRL 5 is approximate).
- **Low-medium:** Acceleration-regime trajectories (qualitatively grounded
  but quantitative TRL-advancement rates per regime not externally
  validated).
- **High:** No-lunar-carbon-at-bulk-scale conclusion (compositional fact;
  not in dispute).

## Plots — skipped

The deliverable is a categorical feasibility matrix, not a numerical
sensitivity sweep. No plot would clarify what the table already shows.
Reserved visualisation for q8 synthesis where cross-leaf comparison
demands it.

## Next pass

Pass 3 (reconcile): open `sources/*/extract.md`, compare derived claims
against the literature evidence, update `claims.yaml` evidence arrays,
flag any disagreements.
