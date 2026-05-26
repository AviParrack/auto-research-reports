---
pass: 5
kind: consistency
leaf: q6-orbital-demand
date: 2026-05-26
status: done
---

# Pass 5 — Consistency (cross-leaf)

Reading sibling-leaf claims.yaml files (q1, q3, q4 reviewed at run
start; q5 and q7 in-flight per parallel-execution caveat — those
contradictions caught by post-batch cross-consistency pass). Looking
for direct contradictions and time-horizon / framework mismatches.

## Q1 — Earth launch cost (reviewed)

Q1's claims describe Starship cost trajectory over 2026-2040: $107-466/kg
under partial-reuse central scenario, with refurbishment cost as the
dominant variable. Musk's $10/kg target outside the calc envelope;
SatBase 2026 shows Falcon 9 list prices rising at $500/kg/year.
Industrial-explosion / TAI compression hypothetically lowers to $15-25/kg.

### Intersection with q6 — the critical coupling

| Topic | q1 position | q6 position | Verdict |
|---|---|---|---|
| Time horizon | 2026-2040 | 2026-2040 (stall / BAU / TAI-C regimes) | **Consistent** — same horizon |
| Stall regime | Implied "pessimistic" $354-780/kg | Stall demand ~1,400 t/yr LEO total — Earth launch trivially supplies | **Consistent** — high-cost-low-demand coupling |
| BAU regime | $107-466/kg under demonstrated 30-reuse partial scenario | BAU demand ~143,000 t/yr LEO average (SDC-dominated) | **Consistent** — moderate launch cost supports modest orbital DC deployment |
| TAI-C regime | $15-25/kg under industrial compression (q1.c7) | TAI-C demand ~2.86 Mt/yr LEO — exceeds plausible Earth-launch capacity by ~7× | **Consistent and the lunar-manufacturing-thesis trigger** — cheap launch enables TAI-C demand, but TAI-C demand structurally requires lunar-sourced supply |
| Musk $10/kg aspiration | Outside operational envelope without TAI compression (q1.c3) | Implies TAI-C SDC scenario; lunar-sourced bulk-mass becomes the supply-side mechanism (q6.c6) | **Consistent** — Musk's aspirational cost target implies TAI-C demand regime |
| Falcon 9 prices rising $500/kg/year | Naive Starship-drives-prices-down thesis contradicted (q1.c5) | BAU SDC deployment economics depend on Starship achieving the $200/kg threshold; if list prices stay above $1,000/kg, BAU SDC deployment slips toward stall | **Merits investigation** — q1.c5 is a partial counter-signal to my BAU adoption assumption |

**No direct contradictions.** Strong qualitative coupling: q1's
acceleration-regime framework (BAU partial-reuse / industrial-
compression / no-progress) maps directly onto q6's stall / BAU /
TAI-C regimes. The q1↔q6 coupling Avi flagged for this run is now
explicit: launch cost determines which q6 regime obtains, and the
demand response is highly non-linear. q6.c6's lunar-manufacturing
necessary-but-not-sufficient conclusion is the direct cross-leaf
implication of q1.c7's TAI compression scenario.

### Flag: SatBase price-trend signal

q1.c5's $500/kg/year structural list-price increase is a partial
counter-signal to my BAU SDC adoption rate. If list prices to commercial
customers remain on the rising trend, then the $200/kg Starship cost
threshold for SDC viability becomes harder to reach in market terms.
The q6.c2 BAU 50 GW SDC deployment may shift toward the lower end
(closer to 10-20 GW). Q8 synthesis should engage this — list-price
vs internal-cost is the critical distinction.

## Q3 — ISRU feasibility (reviewed)

Q3's claims establish materials feasibility for lunar manufacturing:
LCH4 impossible (no bulk carbon), LH2 polar-gated (VIPER late 2027),
structural OK, LOX abundant. Acceleration-regime decomposition
identical structure to q6's.

### Intersection with q6 — supply side of q6.c6

| Topic | q3 position | q6 position | Verdict |
|---|---|---|---|
| Acceleration regimes | TAI-C / BAU / stall identical framework (q3.c8) | Same three-regime framework (q6.c2, q6.c4, q6.c7) | **Consistent — methodological alignment** |
| LCH4 propellant | No bulk lunar carbon source (q3.c5) | Mars cargo demand requires LCH4 propellant — must be Earth-sourced or asteroid-retrieved | **Consistent** — q3's structural negative result implies q6's Mars-bound propellant has earth-sourced methane component |
| LOX propellant | High feasibility (q3.c9) | LOX is ~70-80% of propellant mass (q6 inherits from q3.c14 aerospace-america extract); the dominant lunar-sourceable propellant fraction | **Consistent — strong corroboration of q6.c5 depot demand being partially lunar-supplyable** |
| Structural mass | Sintered regolith TRL 5 / vacuum casting feasible (q3.c7, q3.c9) | q6.c6 splits SDC mass into ~50% bulk-mass-half (lunar-sourceable structure, radiators, sintered shielding) + ~50% compute-half (Earth-launch-only) | **Consistent — q3 supplies the materials feasibility for q6's bulk-mass-half lunar-sourcing argument** |
| Silicon for SBSP panels | MRE coproduct + carbothermal Si (q3.c9) | SBSP panel mass dominated by Si substrate; lunar-sourced Si addresses a substantial fraction of q6.c4's TAI-C 500 kt SBSP mass | **Consistent — lunar Si is a TAI-C-conditional supply mechanism for SBSP** |
| Aluminum for structure | Medium feasibility (FFC Cambridge, chlorine-bottlenecked) (q3.c6, q3.c9) | Al + Ti structural elements for orbital DC + SBSP — partially lunar-sourceable | **Consistent — caveat on Al chlorine dependency carries forward** |
| TRL trajectory | Regime-conditional, not calendar-dependent (q3.c8) | Same framework adopted for SBSP TRL and SDC adoption rate (q6.c2, q6.c4) | **Consistent — q6 inherits q3's methodological position** |

**Strong corroboration.** q3 is the supply-side foundation for q6.c6's
lunar-sourced-bulk-mass argument. The match between regime frameworks
is methodological alignment — both leaves apply anti-pattern #11's
acceleration-regime decomposition with the same TAI-C / BAU / stall
labels and broadly-consistent regime characterizations.

The structural-mass-from-sintering (q3.c7) and Si-from-MRE (q3.c9)
findings directly enable q6.c6's "bulk-mass-half lunar-sourceable"
claim. Without q3's affirmation that these materials are TRL-feasible
at the relevant horizons, q6.c6 would have to retreat to "compute
hardware is Earth-launch-only and there's no lunar supply for the rest
either." With q3's affirmation, the necessary-but-not-sufficient framing
holds: lunar sourcing covers half the SDC mass budget.

## Q4 — Gear ratio (reviewed)

Q4 establishes the gear-ratio framework: ~35× threshold at GTO under
Metzger's model; tent sublimation φ=442-534 exceeds by order of
magnitude; LEO is structurally hardest (Γ ≈ 14 chemical, ≈ 1 with SEP).

### Intersection with q6 — demand-elasticity-cost on Metzger's model

| Topic | q4 position | q6 position | Verdict |
|---|---|---|---|
| Metzger 2023 framework | φ_threshold ≈ 35 at GTO under mid-parameters (q4.c6) | q6.c8 references Kornuta-Metzger 450 t/yr near-term demand as one sub-segment of BAU LEO refueling | **Consistent — q6 inherits Metzger's economic framework for the lunar-derived propellant sub-market** |
| LEO Γ ≈ 14 chemical | Structurally hardest cislunar destination (q4.c1) | q6's BAU depot demand assumes Starship architecture handles the LEO-to-cislunar transit; under chemical-only this is expensive | **Consistent** — q6 inherits the architectural assumption from q1/q2 |
| LEO Γ ≈ 1 with SEP | SEP makes LEO viable at maturity (q4.c12) | q6.c5 depot demand at 8,000-160,000 t/yr scale presupposes economic transit; SEP is the long-horizon enabling architecture | **Consistent — SEP is the post-2030 transit architecture aligned with TAI-C** |
| TAI compression of M_K | If automation compresses capital mass 10×, φ rises proportionally (q4.c10) | Same mechanism in q6.c2 TAI-C scenario: industrial-explosion mass production reduces SBSP kg/kW toward Mankins SPS-ALPHA 1 kg/kW target | **Consistent — same TAI mechanism applied to different cost levers** |
| Demand sub-segments | q4 references Kornuta GTO + reusable lander + Mars refueling segments | q6.c5 / q6.c8 partition same segments within the 8,000 t/yr BAU depot demand | **Consistent — segment taxonomy alignment** |
| Demand-elasticity-cost coupling | q4 establishes per-kg feasibility threshold; demand sub-segments populate it | q6 establishes per-year demand magnitude; couples to q4 viability threshold via Wright's-law scale economics | **Novel cross-leaf integration** — q4's φ_threshold and q6's regime decomposition together describe both viability and scale dimensions |

**No contradictions.** Strong integration: q4 establishes the
viability-per-kg threshold; q6 establishes the demand-per-year
magnitude. Together they cover both dimensions of the lunar-
manufacturing economic question. q8 synthesis should integrate
explicitly.

## Q5, Q7 — parallel siblings (in-flight at run start)

Per pass-leaf.md parallel-execution caveat, q5-capital-buildup and
q7-mass-driver-feasibility were in-flight at q6's run start.
Contradictions between q6 and these siblings will be caught by the
post-batch `--pass cross-consistency` pass.

Cross-leaf topics where q5/q7 likely intersect:
- **q5 industrial-explosion-compression / TAI-acceleration topics**:
  q6.c6's TAI-C demand scenario should be consistent with q5's
  capital-buildup compression scenarios. Cross-validate.
- **q7 capital-cost-mass-driver / TAI-compression-em-launch**: if
  mass-driver delivers cheap lunar-to-LEO ascent (sub-$100/kg per q2),
  then the q6.c6 lunar-sourced-bulk-mass-supply argument becomes
  operationally easier under TAI-C. Mass-driver feasibility shifts the
  supply-side capacity for q6 demand.

## Headline consistency finding

No direct contradictions with q1, q3, q4 (the three reviewed siblings).
Strong methodological alignment on the acceleration-regime framework
(stall / BAU / TAI-C) across q3, q4, and now q6. The q1↔q6
demand-elasticity-cost coupling Avi requested is explicit and
operational in q6.c2 + q6.c6.

One flagged item:
- **q1.c5 Falcon 9 list-price rising $500/kg/year is a partial counter-
  signal to BAU SDC adoption rates**. The internal cost vs list price
  distinction matters for which q6 regime materializes in commercial
  terms. Flag for q8 synthesis.

## Topics added to q6 contradictions_with[]

None at this time. q5, q7 cross-consistency to be assessed in the
post-batch pass.
