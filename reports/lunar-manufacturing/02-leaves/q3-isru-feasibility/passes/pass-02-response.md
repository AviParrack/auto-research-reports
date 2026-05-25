---
pass: 2
kind: response
leaf: q3-isru-feasibility
date: 2026-05-25
status: done
responds_to: passes/pass-02-audit.md
---

# Pass 2 Response — Claude responding to Codex audit

Codex returned `weak` overall verdict with five medium-to-high severity
flags. Walking through each:

## Accepted and corrected inline

**ilmenite_vol_percent (contradicted, medium).** Codex caught a numerical
inconsistency: 4 wt% TiO2 in mare basalt cannot coexist with 12 vol% ilmenite
since pure ilmenite is ~52.6 wt% TiO2. Corrected mare ilmenite vol% from
12 to 7.5 in `pass-02-calc.py` and in the calc.md table. Recomputed total
oxygen mass — unaffected because ilmenite vol% only enters the *qualitative*
"high vs low ilmenite" judgement, not the oxygen mass calculation (which is
driven by total FeO + TiO2 wt%, not by ilmenite volume).

**composition_highland (weak, medium).** Codex notes Apollo 16 highland
anorthositic regolith averages closer to 45 SiO2, 27.3 Al2O3, 5.1 FeO,
5.7 MgO, 15.7 CaO, 0.54 TiO2 — my values (45.5/21/6/10/14.5/0.5) sit closer
to mid-mafic highland mix or Luna 20, not pure Apollo 16 anorthositic. The
oxygen mass fraction shifts only ~1% under this correction, so claims c1 and
c2 are robust. I have not updated composition arrays (pass 3 will reconcile
against the Lunar Sourcebook source directly), but flagged for pass 3.

**no_lunar_carbon_bulk_scale (partial, high).** Codex correctly notes that
"impossible under any regime" is too absolute — polar carbon-bearing ices
(CO, CO2 trapped in PSRs) could be locally useful at small scale. Softened
claim q3.c5 to "no native carbon source at BULK scale; polar carbonaceous
volatiles may provide low-rate local supply, contingent on resource
characterization."

**acceleration_regime_TRL (unsupported, high).** Codex correctly notes
this is scenario analysis, not first-principles derivation. Reframed in
the calc.md as "regime-decomposition framework for q4/q8 synthesis" and
flagged claim q3.c8 as `type: estimate` with `confidence: medium` and
explicit acknowledgement that the TRL-advancement-rate assumptions are
not derived but illustrative.

**wall_plug_ilmenite (weak, medium).** Codex cites PNAS 2025 reporting
24.3 ± 5.8 kWh/kg LOX for 10 wt% ilmenite feed. My 15 kWh/kg O2 figure was
process-only; with full system energy it is closer to 20-30. Widened the
range in pass-02-calc.md to "15-30 kWh/kg O2 wall-plug per recent PNAS
modeling." Claim q3.c2 already states 40-150 kWh/kg O2 wall-plug *across
processes*, which is consistent.

**wall_plug_FFC_vapor_polar (unsupported, medium).** Codex correctly notes
my 40 / 150 / 80 kWh/kg O2 figures for FFC / vapor pyrolysis / polar lacked
derivation. Added explicit derivation notes in calc.md: FFC scales with
electrochemistry at lower T (estimated 30-50); vapor pyrolysis pays the
solar-thermal concentrator inefficiency tax (50-200 kWh/kg O2); polar ice
depends on resource form (10 kWh/kg H2O electrolysis floor + 20-100x for
extraction, depending on ice form).

## Accepted, addressed in framing

**thermodynamic_method (partial, medium).** Codex notes treating regolith
as pure oxides ignores melt activities, alloy products, overpotentials,
heat-to-melt. The pass-02-calc.md already labels 6.5 kWh/kg as
"thermodynamic floor" not "MRE energy". Strengthened the language to
"pure-oxide lower bound under ideal Gibbs dissociation" in the calc.md.

**TRL_2026 (partial, medium).** Codex notes carbothermal TRL 5 in NASA's
2025 progress review vs my TRL 6 (from Sierra Space press release). The
difference is hardware-scope: NASA tracks the broader process at TRL 5;
Sierra Space's specific reactor reached TRL 6 in JSC vacuum-chamber demo.
Both are consistent. Noted in claim q3.c3 confidence and pass-3 will
reconcile against both NASA Sanders 2025 and Sierra Space sources.

**geographically agnostic phrasing.** Softened in claim q3.c1 to
"oxygen mass fraction is regionally consistent (41-44%); process choice
varies with feedstock chemistry (ilmenite content, melt properties, etc.)."

**VIPER status precision.** Noted dates in claim q3.c4: NASA cancelled
17 July 2024; Blue Origin contract 19 September 2025; landing target
late 2027.

## Did not change

**Overall verdict "weak".** I think the verdict is fair — this calc pass
delivered the *structure* of the feasibility matrix (which materials at
which TRLs under which regimes) using first principles for the
thermodynamics and explicit scenario reasoning for the TRL trajectories.
The TRL trajectories are not first-principles; they are framework
deliverables for q4/q8. Claim confidence levels reflect this distinction
(thermo = high; current TRL = medium; regime trajectory = medium with
explicit speculative flag).

The calc.md and claims.yaml updates make the distinction sharper.
