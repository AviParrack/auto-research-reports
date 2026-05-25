---
pass: 1
kind: research
leaf: q3-isru-feasibility
date: 2026-05-25
status: done
---

# Pass 1 — Research: Lunar ISRU Sources Gathered

Twelve source extracts saved under `sources/`. The collection covers the four
production-route families (molten regolith electrolysis, ilmenite hydrogen
reduction, carbothermal reduction, FFC Cambridge / molten-salt electrolysis),
lunar regolith composition (Mare vs Highland, Apollo + Chang'e-5),
polar-ice prospecting status (PRIME-1, VIPER), and propellant context.

## Sources

| Slug | Type | What it bears on |
|---|---|---|
| [nasa-sanders-2025](../sources/nasa-sanders-2025/extract.md) | gov-doc | NASA TRL progression 2019-2025: carbothermal at TRL 5; IPEx excavator at TRL 5; 20 g O₂/kWh-thermal, 20% O₂/regolith yield |
| [sierra-space-carbothermal-2024](../sources/sierra-space-carbothermal-2024/extract.md) | press | Sierra Space carbothermal reactor TRL-6 at JSC Sept 2024 — highest-TRL lunar oxygen demonstration to date |
| [lyon-industries-isru-2026](../sources/lyon-industries-isru-2026/extract.md) | review | 2026 status synthesis: "oxygen ready, water not." MRE TRL 4-6 (Lunar Resources + Blue Origin), carbothermal TRL 6 (Sierra), H₂ reduction TRL 5-6 for equatorial sites |
| [lunarpedia-ilmenite](../sources/lunarpedia-ilmenite/extract.md) | reference | Ilmenite reduction chemistry (FeTiO₃ + H₂ → Fe + TiO₂ + H₂O), temperature 1050°C, mare-only feedstock constraint |
| [lunarpedia-ffc-cambridge](../sources/lunarpedia-ffc-cambridge/extract.md) | reference | FFC Cambridge chemistry; per-tonne yields (anorthite → 460 kg O₂ + 193 kg Al + 201 kg Si + 144 kg Ca); chlorine Earth-import dependency |
| [helios-project](../sources/helios-project/extract.md) | post | Helios Project MRE demonstrator with ispace; lunar demo targeting 2025-2027 (slipped); $6M+ funding |
| [aerospace-america-propellant](../sources/aerospace-america-propellant/extract.md) | post | LOX = 70-80% of propellant mass (key for propellant ISRU strategy); polar-ice uncertainty quantification |
| [arxiv-simulant-2601](../sources/arxiv-simulant-2601/extract.md) | paper | H₂ reduction yields by feedstock: ilmenite 1.10 wt%, highland 0.02 wt%, polar 0.01 wt% — establishes feedstock-dependent yield |
| [wustl-lunar-soil](../sources/wustl-lunar-soil/extract.md) | reference | Canonical bulk composition: O 41-45%, plus Si/Al/Ca/Fe/Mg/Ti at 98-99% of mass; mare/highland mineralogy split |
| [schreiner-mre-model](../sources/schreiner-mre-model/extract.md) | paper | MRE specific energy ~21 kWh/kg O₂ (process) to 50-150 kWh/kg O₂ (wall-plug); 100 kg O₂/yr per kg reactor mass; inert anode key advance |
| [sanders-prime1-viper](../sources/sanders-prime1-viper/extract.md) | gov-doc | PRIME-1 launched IM-2 Feb 2025; VIPER cancelled then re-issued, late-2027 landing target. Polar prospecting gate not yet closed. |
| [changee5-volatiles](../sources/changee5-volatiles/extract.md) | paper | Chang'e-5 mare basalt composition (FeO 22.2%, TiO₂ 5.7%); KREEP-volatile question not closed |

## What's covered

- **All major oxygen-production routes:** MRE (Sadoway/Schreiner/Helios/Lunar
  Resources), H₂ reduction of ilmenite (NASA + university programs),
  carbothermal (Sierra Space), FFC Cambridge (Metalysis/lunar-adaptation),
  vapor pyrolysis (solar thermal review referenced via lyon-industries).
- **Structural metals:** Fe + Si as MRE co-products; Al via FFC Cambridge of
  anorthite; Ti via ilmenite reduction or FFC Cambridge of ilmenite.
- **Lunar regolith composition:** Mare vs Highland canonical figures + Chang'e-5
  ground-truth.
- **Polar-ice / hydrolox dependency:** PRIME-1 outcome + VIPER status.
- **Propellant context:** LOX mass fraction makes oxygen-only ISRU 75-80%
  effective for propellant production even without local fuel.

## What's NOT covered (consider future iteration)

- TransAstra optical mining (referenced in Metzger 2023 from q4 but not yet
  primary-extracted)
- Sowers tent sublimation papers (referenced in q4)
- Kornuta 2019 thermal mining (referenced in q4)
- Direct primary fetch of Schreiner-Sibille parametric paper (PDF behind 403)
- Direct primary fetch of NASA Sanders 2025 NTRS PDF (binary fetch failed;
  used press summary + Lyon Industries 2026 synthesis as proxy)
- Metzger's specific 2021/2023 economics papers as primary fetch (q4 already
  has those; consistency pass will cross-link)

## Next pass

Pass 2 (calc) — sources sealed. First-principles materials × processes ×
TRL feasibility matrix from physical chemistry, regolith composition, and
energy budgets only.
