---
pass: 6
kind: write
leaf: q3-isru-feasibility
date: 2026-05-25
status: drafting
audited: pending
---

# Which materials can the Moon provide?

## Why this question matters

The lunar-manufacturing thesis is structured as a cost comparison: lift mass
from Earth at q1's per-kilogram figure, or lift product mass from the Moon at
q2's per-kilogram figure, normalised by q4's gear ratio. None of that
comparison is meaningful if the Moon cannot produce the materials the
orbital-infrastructure roadmap requires. Q3 is the feasibility gate. If a
material class — structural metals, oxygen, propellant — cannot be extracted
from lunar regolith at a workable technology readiness level under one of the
plausible 2026-2040 acceleration regimes, then q2's cost numerator describes
the price of shipping nothing. If the gate opens, q4's framework binds and
the lunar manufacturing question becomes one of execution rather than
chemistry.

## Where it fits

This leaf provides the materials constraint for q4 (gear ratio synthesis) and
q8 (crossover synthesis), and is consumed by q2 (lunar ascent cost) for the
specific question of whether lunar-produced LOX is available to fuel chemical
ascent vehicles. Q1 (Earth launch cost) and q4 both reference "lunar ice
ground truth" as an open question; q3.c4 closes that pointer with the
PRIME-1 and VIPER prospecting status. Q5 (capital buildup) inherits q3's
process maturity verdicts as inputs to engineering milestone counts.

## Headline answer

**Oxygen, iron, silicon, structural mass, and liquid oxygen propellant are
producible from lunar regolith at TRL 4 to 6 at the time of writing (early
2026, under what looks like a business-as-usual trajectory so far), with
multiple demonstrated processes** [sierra-space-carbothermal-2024],
[nasa-sanders-2025], [schreiner-mre-model], [lyon-industries-isru-2026].
Carbothermal reduction sits at TRL 6 after Sierra Space's
vacuum-chamber demonstration at NASA JSC in September 2024 [sierra-space-
carbothermal-2024]. Molten regolith electrolysis sits at TRL 4-6 across the
Sadoway laboratory, Helios Project, Lunar Resources, and Blue Origin
programmes [helios-project], [schreiner-mre-model], [lyon-industries-
isru-2026]. Ilmenite hydrogen reduction is operationally mature for mare
sites at TRL 5-6 [lyon-industries-isru-2026], [arxiv-simulant-2601].

**Aluminium and titanium have a viable route through molten-salt
electrolysis (FFC Cambridge) but face a structural Earth-import dependency
on chlorine** [lunarpedia-ffc-cambridge]. Whole-regolith molten-oxide
electrolysis (Sadoway / Schreiner) avoids this dependency and produces
iron-silicon alloys directly [schreiner-mre-model] at the cost of less clean
metal separation.

**Hydrogen propellant has exactly one lunar route — polar-ice electrolysis —
and the binding gate is geological** [sanders-prime1-viper], [aerospace-
america-propellant]. The OxEon solid-oxide electrolyser is at TRL 5
[lyon-industries-isru-2026]; what remains uncertain is the resource itself.
PRIME-1 launched on IM-2 in February 2025 with limited drilling opportunity
due to landing-attitude issues, and VIPER's late-2027 delivery via Blue Moon
will be the first comprehensive south-pole ice mapping [sanders-prime1-viper].

**Methane propellant has no bulk lunar carbon route**, full stop
[first-principles-calc]. Bulk regolith carbon is solar-wind-implanted at
ppm levels and not minable for propellant. Polar-PSR craters may hold
trapped CO and CO2 ices at meaningful local scale [changee5-volatiles],
but the resource is prospecting-limited and exhaustible. Any architecture
that depends on lunar-native methalox at scale is structurally blocked
by lunar chemistry, not by TRL.

The TRL trajectory beyond 2026 depends sharply on which acceleration regime
obtains. Under TAI-grade automation compression, carbothermal and MRE
plausibly reach TRL 8 (flight-demonstrated with product return) within a
few years of present; under business-as-usual, the same milestones land
roughly a decade later; under a half-century stall analogous to the
post-Apollo lunar drought, processes remain at their 2024-2026 baselines
indefinitely and there is no product flow at any horizon
[first-principles-calc].

## Feasibility matrix

The full materials × process × Earth-import-dependency picture:

| Material | Best lunar route | TRL 2026 | Earth import (steady state) | Where it lives |
|---|---|---:|---|---|
| O\(_2\) | Carbothermal (Sierra TRL 6) | 6 | Small (CH\(_4\) makeup, closed loop) | Any region |
| LOX propellant | Any O\(_2\) process, liquefied + cryo-stored | 6 | Same as O\(_2\) above | Any region |
| Fe (iron) | MRE coproduct or ilmenite reduction | 5 | Minimal | Mare for ilmenite; any for MRE |
| Si (silicon) | MRE coproduct or carbothermal | 5 | Minimal | Any region |
| Al (aluminium) | FFC Cambridge on anorthite | 4 | Chlorine (structural) | Highland for anorthite |
| Ti (titanium) | FFC Cambridge on ilmenite | 4 | Chlorine (structural) | Mare for ilmenite |
| Mg | MRE coproduct (minor) | 4 | Minimal | Any region |
| Glass | Vacuum sintering, vapor pyrolysis | 5 | Minimal | Any region |
| Structural blocks | Sinterator / 3D-print sintered regolith | 5 | Minimal | Any region |
| LH\(_2\) propellant | Polar ice → water electrolysis | 4 | None if VIPER closes resource question | Polar PSR craters |
| LCH\(_4\) propellant | No bulk lunar carbon | n/a | All carbon imported (or no-go) | n/a |

[lunarpedia-ffc-cambridge], [schreiner-mre-model], [lyon-industries-isru-2026]

## Process discussion

### Oxygen — three competing routes, all advancing

Three production routes compete for the lunar oxygen prize. **Carbothermal
reduction** [sierra-space-carbothermal-2024], [nasa-sanders-2025] heats
regolith with hydrogen and carbon in a closed loop. The chemistry is
SiO\(_2\) + 2C → Si + 2CO followed by 2CO + 6H\(_2\) → 2CH\(_4\) + 2H\(_2\)O,
with the carbon recovered via Sabatier. Sierra Space demonstrated a single
reactor producing the equivalent of 140 kg O\(_2\) per year at vacuum-chamber
conditions in August-September 2024, and NASA's broader programme reports
>20 g O\(_2\) per kilowatt-hour thermal with >20 percent oxygen yield by
mass after five consecutive melt operations [nasa-sanders-2025]. The
energy footprint is approximately 50 kWh per kg O\(_2\) wall-plug, with the
process operating around 1700°C [first-principles-calc].

**Molten regolith electrolysis** [schreiner-mre-model], [helios-project]
takes the whole silicate matrix into a 1600°C melt and applies a current
across an inert anode. Sadoway-style chemistry produces O\(_2\) at the
anode and an iron-silicon alloy at the cathode. Schreiner and Sibille's
parametric model gives approximately 100 kg O\(_2\) per year per kilogram
of reactor mass at 21 kWh per kg O\(_2\) process-only specific energy. The
inert anode is the central twenty-first-century advance over earlier MRE
proposals that needed sacrificial carbon electrodes. The Helios Project (with
ispace and the Israel Space Agency) and Lunar Resources (with Blue Origin)
are the active commercial programmes; the Sadoway laboratory and several
NASA BIG Idea Challenge teams populate the academic side.

**Ilmenite hydrogen reduction** [lunarpedia-ilmenite], [arxiv-simulant-2601]
is the highest-yield-per-process route for mare regions where ilmenite
(FeTiO\(_3\)) is present at roughly 7-12 vol%. The reaction at 1050°C is
FeTiO\(_3\) + H\(_2\) → Fe + TiO\(_2\) + H\(_2\)O, with the water electrolysed
to recover hydrogen and produce oxygen. TPR measurements on simulant give
approximately 1 wt% apparent oxygen yield on pure ilmenite and approximately
0.02 wt% on highland regolith (q3.c10, [arxiv-simulant-2601]) — a roughly
50× yield gap that makes ilmenite reduction structurally mare-specific. The hydrogen is recovered in a
closed loop, so the Earth import is a small initial inventory plus periodic
makeup.

A fourth route, **vapor-phase pyrolysis** at 2000-2500°C via solar
concentrator, is at TRL 3 and operates without consumables or electrolytes
but at the cost of severe thermal inefficiency [first-principles-calc].
It is included in the taxonomy but is not on the near-term roadmap.

### Iron and silicon — coproducts, not bottlenecks

Both metals are direct coproducts of MRE [schreiner-mre-model] and of
ilmenite reduction (which produces iron metal alongside TiO\(_2\) byproduct)
[lunarpedia-ilmenite]. Neither material requires a dedicated extraction
campaign. The integration question is which alloys can be produced at what
purity from the cathode product mix; Schreiner reports Fe-Si alloys with
Ca + Al recoverable in more sophisticated cell designs.

### Aluminium and titanium — clean route, dirty input

The cleanest route to refined Al and Ti is **FFC Cambridge molten-salt
electrolysis** [lunarpedia-ffc-cambridge]. Per tonne of processed feedstock,
anorthite yields 460 kg O\(_2\) + 193 kg Al + 201 kg Si + 144 kg Ca, and
ilmenite yields 316 kg O\(_2\) + 316 kg Ti + 368 kg Fe. On Earth, Metalysis
has scaled the process for terrestrial titanium production through multiple
cell-generation iterations [lunarpedia-ffc-cambridge]. The lunar
adaptation faces one structural problem: the
CaCl\(_2\) electrolyte requires chlorine, and lunar surface chlorine is
present only at trace ppm levels in apatite. Closed-loop salt recycling
through grinding, washing, distillation, or vacuum heating is essential for
lunar economic operation. This is the binding research question that
distinguishes FFC from MRE; until it resolves, MRE is the preferred lunar
route for whole-regolith silicon and iron despite cleaner metal separation
in FFC.

### Structural mass — sintering closes the loop

Habitats, depots, pavement, and radiation shielding do not require refined
metal at all. JPL's Sinterator and extrusion 3D-printing of regolith inks
[first-principles-calc] consolidate loose regolith into structural blocks
via heat alone, at TRL 5. Integrated with an MRE or carbothermal plant, this
closes the structural-mass loop using waste heat or dedicated sintering
furnaces; no metal refining step is required for bulk structural elements.

### Propellant — oxygen yes, hydrogen maybe, methane no

LOX is 70-80% of propellant mass for any hydrolox or methalox stack
[aerospace-america-propellant], so oxygen-from-regolith captures the bulk
of the propellant prize even without local fuel. Any of the three oxygen
routes plus a cryogenic liquefaction and storage train delivers
lunar-produced LOX; this is the highest-confidence propellant ISRU result.

The hydrogen side has exactly one lunar route — polar-ice electrolysis. The
OxEon solid-oxide electrolyser is mature at TRL 5 with demonstrated
production rates of 0.9 kg/hr O\(_2\) and 0.12 kg/hr H\(_2\) from electrolysed
water [lyon-industries-isru-2026]. The remaining open gate is the resource.
A coordinated wave of prospecting missions in 2026-2028 (including
VIPER late-2027 [sanders-prime1-viper] and earlier orbital and surface
prospecting flights catalogued in [lyon-industries-isru-2026]) will
collectively close most of the lunar-ice resource-characterisation
question. Until then, q3.c4 holds the polar hydrogen route at TRL 4 with
the prospecting gate explicitly open.

Methane has no bulk lunar carbon source. Bulk regolith carbon is at ppm
levels [changee5-volatiles]; polar CO and CO\(_2\) ices may provide local
small-scale supply but cannot underwrite an architecture that needs hundreds
of tonnes of methane per launch. Any settlement architecture that depends
on lunar-native methalox is structurally blocked.

## Acceleration-regime decomposition

Calendar-year TRL projections are not informative across our planning
horizon. Decomposed by acceleration regime [first-principles-calc]:

**TAI-grade automation compression.** Demonstration cadence rises sharply.
Each laboratory iteration of MRE or carbothermal that historically took
roughly 18 months drops to weeks. Robotic CLPS missions deliver multiple
ISRU technology demonstrators per year rather than one every two. Capital
mass per plant compresses an order of magnitude as plant designs converge.
Under this regime, carbothermal and MRE plausibly reach TRL 8 (flight-
demonstrated, returning product to a depot or to Earth orbit) within a few
years of present, and structural-mass production loops follow soon after.
FFC Cambridge reaches TRL 6 if the chlorine recycling problem yields to
TAI-grade chemistry optimisation.

**Business-as-usual.** NASA budget remains constrained, Artemis schedule
slips on the order of one year per calendar year, CLPS delivers oxygen-ISRU
demonstrators without product flow. Carbothermal reaches TRL 7 around 2030
and TRL 8 by 2035-2040. MRE follows roughly the same trajectory one to two
years behind. FFC Cambridge stays at lab plus simulant-pellet level; the
lunar configuration remains at TRL 4.

**Stall.** Political will collapses, the CLPS programme winds down.
Carbothermal stays at TRL 6 indefinitely with the Sierra September 2024
demonstration becoming the high-water mark for the decade. MRE stays at
TRL 4 as the Helios and Lunar Resources programmes lose funding. No lunar
product flow exists at any horizon, and q4's gear-ratio framework has no
economic referent.

The deliverable for cross-leaf synthesis is the framework, not the specific
calendar dates. Under TAI-compression or BAU the answer to "are the
materials available at workable TRL" is yes; under stall the answer is
no. The specific year of crossover is determined by which regime the
2026-2040 period actually traces.

## Confidence per finding

- **Regolith oxygen mass fraction 41-44% across regions** — high
  [wustl-lunar-soil], [aerospace-america-propellant], [changee5-volatiles].
- **Pure-oxide thermodynamic floor 6.5 kWh/kg O\(_2\); wall-plug 15-200
  kWh/kg O\(_2\) depending on process** — high (process-specific ranges
  from [schreiner-mre-model], [nasa-sanders-2025]).
- **Carbothermal at TRL 6; MRE at TRL 4-6; ilmenite reduction at TRL
  5-6; FFC Cambridge at TRL 3-4 in lunar configuration** — medium-high
  [sierra-space-carbothermal-2024], [nasa-sanders-2025],
  [lyon-industries-isru-2026].
- **Polar-ice electrolysis is the only lunar H\(_2\) route, prospecting-
  gated** — high [sanders-prime1-viper], [lyon-industries-isru-2026].
- **No bulk lunar carbon for methane propellant** — high
  [first-principles-calc], [aerospace-america-propellant],
  [changee5-volatiles].
- **FFC Cambridge clean metal route, chlorine import bottleneck** —
  high [lunarpedia-ffc-cambridge].
- **MRE productivity 100 kg/yr/kg reactor mass at 21 kWh/kg O\(_2\)
  process energy** — high [schreiner-mre-model].
- **Lifetime-integrated MRE phi clears q4's ~35 threshold** — medium
  (inference from q3.c13 + balance-of-plant derating; flagged in
  q3.c13b).
- **Sintering / 3D-print structural blocks at TRL 5** — medium-high
  (training-knowledge anchored on JPL Sinterator programme;
  primary source not fetched in this iteration).
- **Acceleration-regime TRL trajectory** — medium (framework defensible;
  specific regime rates are illustrative, not derived per Codex audit).

## Limitations

- **Composition reconciliation.** My highland regolith composition
  assumptions in pass-2 calc sit closer to a mid-mafic highland mix than
  to pure Apollo 16 anorthositic soil; Codex pass-2 audit flagged this
  and the relevant Lunar Sourcebook reference. The bulk oxygen mass
  fraction conclusion in q3.c1 is robust under either composition, but
  specific process yields would shift for anorthite-rich regions.
- **TPR-measured simulant yields.** The arxiv-simulant-2601 measurements of
  ilmenite reduction yield (1.10 wt% mare, 0.02 wt% highland) are
  temperature-programmed-reduction lab measurements on simulant, not
  steady-state-reactor measurements on actual lunar regolith. Operational
  yields may differ; lunar-actual ground truth is not yet available.
- **MRE has never run at scale on real lunar regolith.** All current data
  is from laboratory-scale simulant work. The first lunar-environment
  demonstration is targeted for Helios or Lunar Resources via CLPS, with
  schedules in 2026-2028 sliding under BAU conditions.
- **Polar-ice resource characterisation is incomplete.** PRIME-1's limited
  drilling on IM-2 (February 2025) and VIPER's deferral to late-2027 mean
  the lunar polar ice resource picture won't be production-ready until
  2027-2030 at the earliest under any regime.
- **CE-5 sample analysis is still in progress.** Some volatile and
  petrogenetic questions about Chang'e-5 returned material remain open
  [changee5-volatiles]; future analysis may shift the polar volatile picture.
- **Primary sources not fetched.** Three sources I would have liked to add
  as primary extracts but did not: the full Schreiner-Sibille parametric
  paper (PDF 403), the NASA Sanders 2025 progress review PDF directly
  (binary), and the Sowers / Kornuta tent sublimation papers (referenced
  via q4). Future iterations should fill these gaps.
- **Eight "merits investigation" verdicts** from source-review pass remain
  open as potential tree-node candidates (DARPA LunA-10 effect, the
  2026-2028 prospecting wave, lunar-economic salt recycling, TPR-vs-
  reactor yield gap, MRE program consolidation, niche CE-5 mineralogy,
  CLPS funding sensitivity, polar ice gap closure after VIPER).
