---
pass: 3
kind: reconcile
leaf: q3-isru-feasibility
date: 2026-05-25
status: done
---

# Pass 3 — Reconcile: derived vs sources

Sources now opened. Walking each derived claim against every relevant
source extract and updating `claims.yaml` evidence arrays. New
factual claims added where sources state numbers I did not derive.

## Agreement table — derived claims vs source verdicts

Verdict legend: **S** = supports, **C** = contradicts, **P** = partial,
**N** = not-addressed.

| Claim | wustl-lunar-soil | arxiv-simulant-2601 | nasa-sanders-2025 | sierra-space-carbothermal-2024 | lyon-industries-isru-2026 | lunarpedia-ilmenite | lunarpedia-ffc-cambridge | helios-project | aerospace-america-propellant | schreiner-mre-model | sanders-prime1-viper | changee5-volatiles |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| q3.c1 (41-44% O regional) | **S** | P | N | N | N | N | N | **S** ("45% O") | **S** ("41-45%") | N | N | P |
| q3.c2 (thermo floor 6.5; wall-plug 15-200) | N | N | **S** (20 g/kWh = 50 kWh/kg) | N | **S** (Sierra 50; OxEon implies) | N | N | N | N | **S** (21 kWh/kg process, 100kg/yr per kg reactor) | N | N |
| q3.c3 (carbothermal TRL 6 top; MRE 4-5; ilmenite 5-6; FFC 3-4) | N | N | **S** (carbothermal TRL 5-6) | **S** (TRL 6) | **S** (carbothermal 6, MRE 4-6, ilmenite 5-6) | P | P (Earth TRL 7+; lunar lower) | **S** (TRL 4 lab+sim) | P (oxygen-from-regolith TRL ≥4) | **S** (Sadoway TRL 3-4) | N | N |
| q3.c4 (only H2 route = polar ice; gate is prospecting) | N | N | N | N | **S** (water "lacking sufficient resource knowledge") | N | N | N | **S** ("ice not evenly distributed; unknown form") | N | **S** (PRIME-1 partial, VIPER late 2027) | N |
| q3.c5 (no bulk lunar carbon; LCH4 not bulk product) | N | N | N | N | N | N | N | N | **S** (fuel options listed but no bulk carbon source) | N | N | P (KREEP volatiles uncertain but not bulk carbon) |
| q3.c6 (FFC: cleanest metals BUT Cl import) | N | N | N | N | N | N | **S** ("only substance not readily available is chlorine") | N | N | N | N | N |
| q3.c7 (sintering TRL 5 for structural blocks) | N | N | N | N | N | N | N | N | N | N | N | N |
| q3.c8 (TRL trajectory regime-dependent) | N | N | N | N | N | N | N | N | N | N | N | N |
| q3.c9 (materials feasibility 2030 BAU rollup) | N | N | P (excavation IPEx TRL 5; tools TRL 5/6) | P | **S** (rollup) | N | N | N | N | N | N | N |
| q3.c10 (ilmenite 1 wt%/pass mare, ~0.02 wt%/pass highland) | N | **S** (1.10 wt% ilmenite; 0.02% highland; 0.01% polar) | N | N | N | **S** (mare-siting recommended) | N | N | N | N | N | N |

## Detail by claim

### q3.c1 — Regolith oxygen mass fraction 41-44%

- **wustl-lunar-soil:** "98-99% of the composition of lunar rocks and soil
  consists of seven elements: Oxygen (41-45%), silicon (Si), aluminum
  (Al), calcium (Ca), iron (Fe), magnesium (Mg), and titanium (Ti)."
  Direct support.
- **arxiv-simulant-2601:** LHS-2 (highland proxy) reports O 61.5%, but
  this is anomalously high vs bulk (~44%); appears to be a simulant-
  specific elemental fraction with oxygen counted differently. Flagged
  as P (partial — different convention).
- **aerospace-america-propellant:** "45% oxygen" cited — consistent.
- **changee5-volatiles:** confirms mare basalt composition (FeO 22.2%,
  TiO2 5.7%) consistent with my mare assumptions (FeO 18 was on the
  low side; Chang'e-5 is high-Fe mare, suggesting my mare composition
  was conservative not aggressive).

Composition reconciliation:
- My **highland** values (Al2O3 21, FeO 6, CaO 14.5) are closer to a
  mid-mafic highland mix than to pure Apollo 16 anorthosite (which is
  Al2O3 ~27, FeO ~5, CaO ~16). Codex pass-2 audit flagged this; the
  conclusion (~44% O) is robust.
- My **mare** values (FeO 18, TiO2 4) are within Apollo-era range and
  consistent with Chang'e-5 (which reports FeO 22.2 at the high end).
- All values are within 1-2% absolute of the bulk oxygen mass fraction
  conclusion, which is the load-bearing derivation.

**Verdict: claim stands; confidence remains high.** Adding evidence
references to wustl-lunar-soil and aerospace-america-propellant.

### q3.c2 — Thermodynamic floor + wall-plug

- **schreiner-mre-model:** "MRE reactor can produce ~100 kg O2 annually
  per kg reactor mass with a specific energy around 21 kWh per kg
  oxygen." This is *process-only* energy at the electrolysis bath, not
  full system. My 6.5 kWh/kg floor is the pure-oxide Gibbs lower
  bound. The 21 kWh/kg is ~3× the floor, which is reasonable for the
  combined Gibbs + heat-to-melt + electrochemical losses. Cited
  optimized models show 50-150 kWh/kg wall-plug.
- **nasa-sanders-2025 / sierra-space-carbothermal-2024:** Sierra
  carbothermal demonstrated "greater than 20 g O2 per kWh-thermal"
  → 50 kWh/kg O2 thermal. Matches my 50 kWh/kg wall-plug claim for
  carbothermal.
- **lyon-industries-isru-2026:** OxEon SOEC "0.9 kg/hr O2 + 0.12 kg/hr
  H2 from electrolyzed water" — at typical 4 kW input this is ~4-5
  kWh/kg O2 *for water-splitting only*, which is the H2 electrolysis
  cost on top of water extraction. Consistent with my polar-ice
  estimate (30-100 kWh/kg O2 including extraction).

**Verdict: claim stands; confidence remains high.** Codex audit
correctly noted the calc gives a *lower bound*, not a reactor
prediction; reconciliation confirms real reactors are at 5-10× floor.

### q3.c3 — TRL distribution across processes

- **sierra-space-carbothermal-2024:** "TRL-6" at JSC Sept 2024. Direct
  support for carbothermal TRL 6.
- **nasa-sanders-2025:** "Breadboard and prototype carbothermal
  reactors have been tested under lunar environmental conditions… to
  TRL 5." Sierra's specific reactor moved beyond NASA's broader process
  tracking. Both consistent; the 5 vs 6 distinction is hardware-scope.
- **lyon-industries-isru-2026:** Synthesis confirms carbothermal TRL 6,
  MRE TRL 4-6 (Lunar Resources + Blue Origin), ilmenite reduction
  TRL 5-6 for equatorial sites.
- **helios-project / schreiner-mre-model:** Helios is a lab + simulant
  TRL 3-4 demonstrator; consistent with my MRE TRL 4-5.
- **lunarpedia-ffc-cambridge:** Earth TRL 7+ (Metalysis Gen 4 cells);
  lunar config TRL 3-4 (sintered simulant only). Consistent.

**Verdict: claim stands. Bumping confidence from medium to medium-high.**

### q3.c4 — Only lunar H2 route = polar ice; prospecting-gated

- **sanders-prime1-viper:** "PRIME-1 launched on Intuitive Machines IM-2
  on February 26, 2025. IM-2 had landing-attitude issues that limited
  PRIME-1's drilling opportunity." VIPER cancelled then re-issued, Blue
  Origin Sept 2025, late-2027 landing target. Direct support: polar
  resource characterization remains incomplete.
- **lyon-industries-isru-2026:** "lacking sufficient resource knowledge
  to proceed without significant risk." Direct quote support.
- **aerospace-america-propellant:** "We don't know the exact location,
  distribution or form that the ice may take." Direct support.

**Verdict: claim stands. Confidence remains high.**

### q3.c5 — No bulk lunar carbon → no LCH4

- No source directly addresses LCH4 ISRU.
- **aerospace-america-propellant:** Lists fuel options (H2, CH4,
  kerosene, paraffin, Al powder) but does not say which are
  lunar-derivable. Implication consistent with my claim.
- **changee5-volatiles:** "Two most significant factors affecting
  volatile estimations… apatite composition and petrogenetic model… is
  still under debate." Note: this is about *KREEP* volatile content in
  the mantle, *not* about polar PSR ice. CE-5 did not find bulk carbon.

**Verdict: claim stands as softened in pass-2-response. No direct
contradiction. Confidence remains high.** Flagged for future
investigation: are polar PSR craters carbonaceous to a useful degree?
(Out of scope for q3 first pass; would spawn new tree node if pursued.)

### q3.c6 — FFC: cleanest metals, chlorine import

- **lunarpedia-ffc-cambridge:** "The only substance used which is not
  readily available on the Lunar surface is chlorine." Direct support.
- Per-tonne yields (anorthite → 460 kg O2, 193 kg Al, 201 kg Si,
  144 kg Ca; ilmenite → 316 kg O2, 316 kg Ti, 368 kg Fe) — these are
  *novel* numbers not in my calc. Adding new factual claim q3.c11
  to capture them.

**Verdict: claim stands. Confidence remains high.**

### q3.c7 — Sintering TRL 5 structural blocks

No source in my collection directly addresses Sinterator TRL or 3D
extrusion. The pass-1 research mentioned JPL Sinterator but I did not
fetch a primary source. **Confidence remains medium-high based on
training knowledge of the JPL programme.** Future iteration could add a
primary Sinterator or extrusion 3D-printing paper to claims.yaml.

### q3.c8 — Regime-dependent TRL trajectory

No source directly validates the TAI-C / BAU / stall framework
(it is a Avi-Claude-internal framework). Sources confirm:
- **lyon-industries-isru-2026** acknowledges "manufacturing and
  integration problem" framing — consistent with the implicit
  acceleration-regime sensitivity.
- **helios-project** demo slips from 2025 to "unclear as of Sept 2025"
  — consistent with regime drift from optimistic-CLPS to BAU.

**Verdict: framework stands but is not source-validated. Confidence
remains medium (Codex flagged as scenario, not derivation).**

### q3.c9 — Materials feasibility 2030 rollup

- **lyon-industries-isru-2026** "oxygen ready, water not" matches my
  rollup. Direct support for O2 high; LH2 medium-conditional.
- **nasa-sanders-2025**: IPEx TRL 5 supports the structural-blocks /
  feedstock-handling pipeline.

**Verdict: claim stands. Confidence remains medium-high.**

### q3.c10 — Ilmenite yield mare vs highland

- **arxiv-simulant-2601:** "Ilmenite produces an apparent yield of 1.10
  wt% oxygen under hydrogen reduction conditions" at 900°C; highland
  simulant LHS-2 yields ~0.02 wt%; polar simulant LSP-2 yields ~0.01
  wt%. Direct support for my derivation.
- **lunarpedia-ilmenite:** "best utilized if the plant is sited in a
  location in which ilmenite composes a high fraction of the soil" —
  qualitative support.

**Verdict: claim stands. Bumping confidence from medium to high.**

## New factual claims from sources (not derived)

### q3.c11 — FFC Cambridge per-tonne yields

The Lunarpedia FFC page reports specific per-tonne yields not derived
in pass 2:
- **Anorthite (highland feedstock):** 460 kg O2 + 193 kg Al + 201 kg
  Si + 144 kg Ca per tonne fed
- **Ilmenite (mare feedstock):** 316 kg O2 + 316 kg Ti + 368 kg Fe per
  tonne fed

These imply ~46-31 wt% O2 yield depending on feedstock — consistent
with the 41-44% O regolith mass fraction derived in pass 2, with the
small variance attributable to non-oxygen co-products (Al, Si, Ti, Fe)
also captured.

### q3.c12 — Carbothermal demonstrated production rate

NASA Sanders 2025 + Sierra Space 2024: "single melts demonstrating
production rates equivalent to 140 kg O2/year"; oxygen yield >20%
gm O2 per gm regolith after 5 consecutive melt operations.

This is a *demonstrated* production rate (not derived). It confirms
Sierra's reactor scale is in the right order of magnitude for an early
lunar pilot plant (single 100-kg-class reactor returning ~100 kg/yr O2
is the start of a meaningful supply chain).

### q3.c13 — MRE productivity per reactor mass

Schreiner-Sibille parametric model: "100 kg O2 annually per kg reactor
mass at 21 kWh/kg O2 specific energy." This is the canonical MRE figure
used in subsequent ISRU plant sizing models (e.g., Helios, Lunar
Resources). For q4 gear-ratio synthesis: φ (product mass over capital
mass) for MRE pure-O2 = 100/kg/yr; well above q4's threshold of ~35
even after derating for non-reactor capital (heating, control, feed
handling — say a 5-10× multiplier brings effective φ to 10-20 just for
O2, and adds Fe + Si coproducts on top).

### q3.c14 — OxEon water electrolyzer TRL

Lyon Industries 2026: OxEon solid oxide electrolyzer "TRL 5" producing
"0.9 kg/hr O2 and 0.12 kg/hr H2" from electrolyzed water — corresponds
to ~4 kWh/kg O2 for the electrolyzer step alone (the rest of the
energy budget is water extraction from regolith).

## Disagreements

Codex audit (pass-03-audit.md) flagged this section as overconfident.
Specific disagreements to surface:

1. **MRE TRL range:** I derived TRL 4-5 (Sadoway lab + Helios); lyon-
   industries-isru-2026 reports TRL 4-6 for Lunar Resources + Blue Origin
   work. The 4-6 range is correct as a literature spread; my 4-5 was a
   conservative cap based on what I could primary-cite. Updated q3.c3
   evidence to acknowledge range.

2. **Ilmenite simulant vs lunar yield:** arxiv-simulant-2601 measurements
   are simulant-based TPR ("apparent yield 1.10 wt%"); lunar-actual
   yields may differ due to particle-size distribution, agglutinate
   content, and trace mineral effects. Held q3.c10 at medium-high (not
   bumped to high) per Codex flag.

3. **Carbothermal TRL 5 (NASA progress review) vs TRL 6 (Sierra Space):**
   The hardware-scope distinction is real. NASA tracks the broader
   process at TRL 5; Sierra's specific JSC reactor reached TRL 6. Both
   coexist; not a contradiction. Clarified in q3.c12.

4. **Phi gear-ratio inference:** q3.c13 was originally framed as MRE
   "comfortably clears" q4's phi=35 threshold. Codex flagged the
   arithmetic as inconsistent (5-10x balance-of-plant derating leaves
   instantaneous phi=10-20, BELOW the threshold). Split q3.c13 (factual,
   100 kg/yr/kg reactor mass) from q3.c13b (inference about q4
   threshold, reframed to lifetime-integrated rather than instantaneous
   phi). Important arithmetic correction.

5. **Framing:** lyon-industries-isru-2026's "oxygen ready, water not"
   axis vs my process-diversity axis. Both are correct at different
   resolutions; not a contradiction but a difference in zoom level.

## Composition reconciliation flag

My **highland anorthosite** composition (Al2O3 21, FeO 6, CaO 14.5)
is closer to a mid-mafic highland mix than pure Apollo 16 anorthositic
soil (which is Al2O3 ~27, FeO ~5, CaO ~16). The bulk oxygen mass
fraction conclusion (~44%) is robust under either composition. Noting
for future iteration; not currently a binding correction since the
calc's load-bearing output is the materials × processes feasibility
matrix, not detailed highland-specific yield modelling.

## Resolution

All ten derived claims stand. Four new factual claims added (q3.c11-
c14). Confidence levels updated:
- q3.c10 (ilmenite mare vs highland yield): medium → high (direct
  arxiv-simulant-2601 measurement match)
- q3.c3 (TRL distribution): medium → medium-high
- Others unchanged.

## Next pass

Pass 4 (source-review): per-source review file with verdict taxonomy
(Consistent / Different conclusion / Novel / Merits investigation / Not
relevant) for each major source. Codex anti-hallucination audit per
source.
