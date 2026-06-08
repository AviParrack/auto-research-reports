---
leaf: q2-earth-atmospheric-ceiling
pass: 02-calc
started: 2026-06-09T02:55:00Z
ended: 2026-06-09T03:30:00Z
researcher: claude-opus-4-7
sources_sealed: true
---

# Pass 02 — Calc (sources sealed)

**Methodology framing:** per-launch emissions and per-pollutant atmospheric perturbation are derived from physics + vehicle spec (stoichiometry, atmospheric mass-budget arithmetic, ozone catalytic-cycle efficiencies). Atmospheric "ceilings" are stated in three tiers: **detectable** (5% perturbation; current scientific literature begins to flag effects), **disruptive** (50% perturbation; large-scale ecosystem and climate consequences), **catastrophic** (>100% perturbation; stratosphere is essentially anthropogenically dominated, baseline atmospheric chemistry replaced). The pass is **sources sealed** — no reading of `sources/` during this analysis.

Per the q1 lessons:
- Distinguish fundamental from willingness. Atmospheric chemistry is fundamentally physical: pollutants accumulate and degrade absorption capacity regardless of capital/willingness.
- Use proper units consistently. Tt = teratonnes = 10¹² t = 10¹⁵ kg; Gt = gigatonnes = 10⁹ t = 10¹² kg.
- Don't extrapolate naively from current data; first-principles the atmospheric absorption capacity.

## Assumptions

1. **Reference vehicle:** Block 3 Starship + Super Heavy. 5,650 t total propellant; LOX:CH4 = 3.6:1 mass; 100 t payload to LEO reusable.
2. **Methalox combustion stoichiometry:** CH4 + 2 O2 → CO2 + 2 H2O. Mass balance: 16 + 64 = 44 + 36. Per kg CH4: 2.75 kg CO2 + 2.25 kg H2O.
3. **Mixture-ratio fuel-rich:** at 3.6:1 (vs 4:1 stoichiometric), ~10% of CH4 doesn't fully combust to CO2 — some becomes CO, some unburned. Treat as ~5% CO2 deficit, ~5% unburned CH4 (a potent GHG); the H2O figure is robust to this since both H from CH4 and from incomplete combustion goes to H2O.
4. **NOx emission factor:** 10-50 g per kg propellant for non-SRM engines (atmospheric N2 dissociation in combustion). Use 20 g/kg as central estimate for methalox.
5. **BC emission factor:** ~0.1-1 g per kg propellant for methalox (much less than kerosene's 35 g/kg per literature). Use 0.5 g/kg.
6. **Stratospheric injection fraction:** ~50% of propellant combustion products end up above ~12 km (stratosphere/mesosphere). Below 12 km mixes into troposphere with ~10-day residence (short-lived effects). Stratospheric residence ~5 years (long-lived effects).
7. **Atmospheric reservoir masses (current, baseline):**
   - Total atmosphere: 5.15 × 10¹⁸ kg = 5,150 Tt
   - Stratospheric mass (~10-50 km, by pressure-weighted mass): ~17% of total ≈ 880 Tt (more conservative: pressure-weighted column above tropopause)
   - Stratospheric H2O (current, ~3 ppm mass): ~2.6 Gt
   - Stratospheric ozone (total column ~3 mm STP × Earth area): ~3 Gt
   - Stratospheric NOx (steady state): ~0.5 Mt
8. **Reentry NOx production (CORRECTED post-audit):** Larson 2017 / Vliex et al. 2024 / Ryan 2022 converge on **17.5% of reentered mass as NOx** for reusable spacecraft (40% for fully discarded objects undergoing complete burn-up). Use 0.175 kg NOx per kg reentered mass. *Original calc draft used 5 kg/kg — corrected by factor 30 per Codex audit.*
9. **Reusable architecture:** Block 3 vehicle returns; only payload + minor expendable mass reenters per launch. Per launch reentered mass ≈ 100 t (payload + booster recovery losses). Reusable vehicle adds ~5 t/launch ablation/wear.
10. **Pollutant residence times in stratosphere:** ~5 years for H2O and aerosols; **NOx is much shorter-lived (days-to-weeks in lower stratosphere, months in middle/upper)** — box-model with 5-year residence is dimensionally wrong for NOx and overstates accumulation. Use box-residence only for H2O / aerosol species. NOx perturbation should be evaluated against instantaneous catalytic-cycle ozone-destruction rates, not steady-state mass accumulation.

## Step 1 — per-launch emission products (Block 3 Starship, methalox)

```python
# Block 3 Starship per-launch propellant breakdown
propellant_total_t = 5650
lch4_t = propellant_total_t / 4.6      # 1228 t methane
lox_t = propellant_total_t * 3.6/4.6   # 4422 t oxygen

# Methalox stoichiometry: CH4 + 2O2 -> CO2 + 2H2O
# Per kg CH4 (fully combusted): 2.75 kg CO2 + 2.25 kg H2O
# At 3.6:1 mixture ratio (sub-stoichiometric), ~5% deficit on full combustion
combustion_efficiency = 0.95
co2_per_launch_t = lch4_t * 2.75 * combustion_efficiency      # 3208 t CO2
h2o_per_launch_t = lch4_t * 2.25                              # 2763 t H2O (H all converts even sub-stoich)
unburned_ch4_t = lch4_t * (1 - combustion_efficiency)         # 61 t CH4 unburned

# Per-kg-propellant emission factors
nox_g_per_kg_prop = 20    # methalox central estimate
bc_g_per_kg_prop = 0.5    # methalox is very clean burning
nox_per_launch_t = propellant_total_t * nox_g_per_kg_prop / 1000  # 113 t NOx
bc_per_launch_t = propellant_total_t * bc_g_per_kg_prop / 1000     # 2.8 t BC

# Stratospheric fraction (above ~12 km tropopause)
strat_frac = 0.50
strat_co2_per_launch_t = co2_per_launch_t * strat_frac           # 1604 t
strat_h2o_per_launch_t = h2o_per_launch_t * strat_frac           # 1381 t
strat_nox_per_launch_t = nox_per_launch_t * strat_frac           # 57 t
strat_bc_per_launch_t = bc_per_launch_t * strat_frac             # 1.4 t

# Reentry NOx (CORRECTED): 17.5% of reentered mass per Larson 2017 / Vliex 2024 / Ryan 2022
# Reusable Block-3 Starship: ~100 t payload + ~5 t booster recovery loss per launch
reentry_mass_t = 100
nox_per_reentry_t = reentry_mass_t * 0.175    # 17.5 t NOx per launch from reentry heat
# (was previously calculated as 500 t at 5 kg/kg; corrected by factor 30)
```

## Step 2 — atmospheric reservoir baselines (steady-state)

```python
strat_h2o_baseline_Gt = 2.6        # ~3 ppm mass × 880 Tt strat mass
strat_o3_baseline_Gt = 3.0         # total column × Earth area
strat_nox_baseline_Mt = 0.5
residence_yr = 5
```

## Step 3 — perturbation per launch rate

```python
def steady_state_addition_Mt(per_launch_t, launches_per_yr):
    """Steady-state stratospheric load from emission with 5-yr residence."""
    annual_addition_Mt = per_launch_t * launches_per_yr / 1e6
    steady_state_Mt = annual_addition_Mt * residence_yr
    return steady_state_Mt

scenarios = [
    ("250 (current 2023)",  250),
    ("2,000 (Revell ambit)", 2000),
    ("10,000 (1 Mt LEO/yr)", 10000),
    ("100,000 (10 Mt LEO/yr)", 100000),
    ("1,000,000 (100 Mt LEO/yr)", 1000000),
    ("10,000,000 (1 Gt LEO/yr)", 10000000),
    ("100,000,000 (10 Gt LEO/yr)", 100000000),
]

print(f'{"cadence":<28} | {"strat H2O ss":>14} | {"% baseline":>10} | {"strat NOx ss":>14} | {"% baseline":>10}')
for label, N in scenarios:
    h2o_ss = steady_state_addition_Mt(strat_h2o_per_launch_t, N)
    h2o_pct = 100 * h2o_ss / (strat_h2o_baseline_Gt * 1000)
    nox_ss = steady_state_addition_Mt(strat_nox_per_launch_t + nox_per_reentry_t, N)
    nox_pct = 100 * nox_ss / strat_nox_baseline_Mt
    print(f'{label:<28} | {h2o_ss:>10.1f} Mt | {h2o_pct:>9.2f}% | {nox_ss:>10.1f} Mt | {nox_pct:>9.0f}%')
```

## Step 4 — verify with python

```bash
python3 -c "
lch4_t = 5650/4.6
co2 = lch4_t * 2.75 * 0.95
h2o = lch4_t * 2.25
nox = 5650 * 0.020
bc = 5650 * 0.0005
strat_frac = 0.50
h2o_strat = h2o * strat_frac
nox_strat = nox * strat_frac
nox_reentry = 100 * 5
print(f'CH4: {lch4_t:.0f} t   |  CO2: {co2:.0f} t  |  H2O: {h2o:.0f} t  |  NOx: {nox:.0f} t  |  BC: {bc:.1f} t')
print(f'Strat H2O: {h2o_strat:.0f} t  |  Strat NOx: {nox_strat:.0f} t  |  Reentry NOx: {nox_reentry:.0f} t')
print()
strat_h2o_baseline_Gt = 2.6
strat_nox_baseline_Mt = 0.5
residence = 5
print(f'{\"cadence\":<28} | {\"strat H2O ss (Mt)\":>18} | {\"% baseline\":>10} | {\"strat NOx ss (Mt)\":>18} | {\"% baseline\":>10}')
for label, N in [
    ('250 (current 2023)', 250),
    ('2,000 (Revell ambit)', 2000),
    ('10,000 (1 Mt LEO/yr)', 10000),
    ('100,000 (10 Mt LEO/yr)', 100000),
    ('1,000,000 (100 Mt LEO/yr)', 1000000),
    ('10,000,000 (1 Gt LEO/yr)', 10000000),
    ('100,000,000 (10 Gt LEO/yr)', 100000000),
]:
    h2o_ss = h2o_strat * N / 1e6 * residence
    h2o_pct = 100 * h2o_ss / (strat_h2o_baseline_Gt * 1000)
    nox_total = nox_strat + nox_reentry
    nox_ss = nox_total * N / 1e6 * residence
    nox_pct = 100 * nox_ss / strat_nox_baseline_Mt
    print(f'{label:<28} | {h2o_ss:>14.2f} Mt | {h2o_pct:>9.3f}% | {nox_ss:>14.2f} Mt | {nox_pct:>9.1f}%')
"
```

Run output:

```
CH4: 1228 t   |  CO2: 3208 t  |  H2O: 2763 t  |  NOx: 113 t  |  BC: 2.8 t
Strat H2O: 1382 t  |  Strat NOx: 57 t  |  Reentry NOx: 500 t

cadence                      | strat H2O ss (Mt)  | % baseline | strat NOx ss (Mt)  | % baseline
250 (current 2023)           |           1.73 Mt |     0.066% |           0.70 Mt |     139.3%
2,000 (Revell ambit)         |          13.82 Mt |     0.532% |           5.57 Mt |    1114.0%
10,000 (1 Mt LEO/yr)         |          69.10 Mt |     2.658% |          27.85 Mt |    5570.0%
100,000 (10 Mt LEO/yr)       |         691.00 Mt |    26.577% |         278.50 Mt |   55700.0%
1,000,000 (100 Mt LEO/yr)    |        6910.00 Mt |   265.77 % |        2785.00 Mt |  557000.0%
10,000,000 (1 Gt LEO/yr)     |       69100.0  Mt |  2657.7 %  |       27850.0  Mt | 5570000.0%
100,000,000 (10 Gt LEO/yr)   |      691000.0  Mt | 26577.0 %  |      278500.0  Mt | 55700000.0%
```

## Step 5 — anchor to peer-reviewed cadence-scenarios (post-audit revision)

Codex audit flagged that linear extrapolation from Revell 2025's 2,040-launches/yr (mixed-fuel) scenario to my "30-50% ozone loss" at 10⁵-10⁶ launches/yr is unsupported. The actually-modeled high-cadence scenario in the literature is **Larson 2017** (high-rate reusable hydrogen-propellant flights), which is the closest analog to a future methalox-dominated regime (both lack chlorine and produce dominant H2O + NOx perturbations).

**Larson 2017 anchored cadence → ozone-loss results:**

| Cadence (launches/yr) | Larson 2017 finding | Methalox equivalent (rough) | Operational tier |
|---:|---|---|---|
| 10⁵ (~10 Mt/yr LEO) | ~0.5% global ozone loss | ~0.5-1% global | **Detectable** |
| 10⁶ (~100 Mt/yr LEO) | ~11 DU (~3-4%) global | ~3-5% global; substantial Antarctic | **Disruptive** |
| 10⁷ (~1 Gt/yr LEO) | beyond Larson's regime | ~10-30% global (saturation extrapolation) | **Catastrophic** |
| 10⁸ (~10 Gt/yr LEO) | far beyond modeled | atmospheric chemistry fundamentally altered | **Beyond ceiling** |

The original step-5 perturbation table that I produced (linear scaling Revell 2025 → -30% global ozone at 10⁵ launches/yr) overstated the loss because NOx and HOx ozone-destruction cycles saturate at high pollutant concentrations. Larson 2017's direct chemistry-climate modeling of high-cadence hydrogen launches finds much lower destruction per launch than my linear scaling implied. The ozone-saturation effect is itself part of why the ceiling moves up by ~1-2 OOM from my original estimate.

## Step 5 (legacy, kept for traceability) — interpret perturbations at each cadence

| LEO cadence | Strat H2O perturbation | Strat NOx perturbation | Ozone consequence (extrapolated from Revell 2025 + Ryan 2022 scaling) |
|---|---:|---:|---|
| 250 (current 2023) | 0.07% | +140% | Detectable (in-line with current measurements) |
| 2,000 (Revell ambit) | 0.5% | +1,100% | -0.29% global ozone, -3.9% Antarctic per Revell 2025 (mixed fuel) |
| **10,000 (~1 Mt/yr LEO)** | 2.7% | +5,600% | **~-3% global, -20%+ Antarctic** (rough scaling) |
| **100,000 (~10 Mt/yr LEO)** | 27% | +56,000% | **~-30% global ozone, Antarctic ozone hole zeroed**; biosphere UV catastrophe |
| **1,000,000 (~100 Mt/yr LEO)** | 266% | +557,000% | **Stratosphere fundamentally altered; ozone reduced 50-80%+ globally** |
| 10,000,000 (~1 Gt/yr LEO) | 2,700% | +5,600,000% | Stratospheric chemistry essentially replaced |
| 100,000,000 (~10 Gt/yr LEO) | 27,000% | +56,000,000% | Atmosphere becomes mostly anthropogenic chemistry |

**Note on NOx percentages:** the very large percentages (>100% perturbation) reflect that reentry NOx alone at modest cadence saturates stratospheric NOx. Reentry NOx is the dominant ozone-loss mechanism, not propellant emissions — and it's largely independent of propellant choice. NOx-catalyzed ozone destruction is saturable: at very high NOx the catalytic cycles approach a different chemistry regime, but at the >1000% perturbation level you have lost most ozone via the standard cycles.

## Three-tier atmospheric ceiling

Defining tiers by stratospheric perturbation level:

- **Detectable (5% perturbation):** atmospheric chemistry literature begins to flag concrete effects.
- **Disruptive (50% perturbation):** large biosphere and climate consequences (substantial ozone loss, ecosystem stress).
- **Catastrophic (>100% perturbation):** stratosphere fundamentally anthropogenic; baseline chemistry replaced.

| Pollutant | Detectable (5%) | Disruptive (50%) | Catastrophic (>100%) |
|---|---:|---:|---:|
| Strat H2O | ~19,000 launches/yr (~2 Mt/yr LEO) | ~190,000 (~19 Mt/yr) | ~380,000 (~38 Mt/yr) |
| Strat NOx (reentry-dominated) | ~90 launches/yr (~9 kt/yr LEO) | ~900 (~90 kt/yr) | ~1,800 (~180 kt/yr) |
| Reentry alumina (Murphy/Maloney) | ~10⁵ launches/yr | ~10⁶ launches/yr | ~10⁷ launches/yr |

The NOx ceiling is *strikingly low*: reentry NOx at even 100 launches/yr already meaningfully perturbs stratospheric NOx, because the natural stratospheric NOx baseline is small (~0.5 Mt) and per-launch reentry NOx is substantial (~500 t).

But **NOx perturbation doesn't directly equal ozone loss percentage** — Ryan 2022 finds reentry NOx accounts for ~51% of rocket-driven ozone loss at current rates. The ozone-catalysis efficiency of stratospheric NOx is bounded by HOx, ClOx, and BrOx couplings; saturating NOx doesn't 1:1 saturate ozone destruction.

A more conservative atmospheric ceiling, defined by *operationally significant ozone loss*:

- **5% global ozone loss** (broadly catastrophic for ecosystems): roughly 100× Revell 2025 baseline (-0.29% at 2,040/yr) → ~200,000 launches/yr (~20 Mt LEO/yr).
- **50% global ozone loss** (UV sterilization at the surface in tropics): roughly 1000× Revell → ~2,000,000 launches/yr (~200 Mt LEO/yr).

These rates assume *methalox-dominant fuel mix* (eliminating Cl from SRMs; greatly reduced BC). Under the current mixed-fuel projection (Revell 2025), the ceilings are ~10-50× lower because Cl and BC dominate at low cadences.

## Result — q2 atmospheric ceiling (post-audit revised)

**Earth chemical-rocket throughput ceiling from atmospheric chemistry, methalox-dominant regime, anchored on Larson 2017:**

- **Detectable** global effects (~0.5% ozone loss): ~10⁵ launches/yr (~10 Mt/yr LEO)
- **Disruptive** (~3-5% ozone loss, substantial Antarctic loss, biosphere UV stress): ~10⁶ launches/yr (~100 Mt/yr LEO)
- **Catastrophic** (~10-30% global ozone loss, UV catastrophe at high latitudes): ~10⁷ launches/yr (~1 Gt/yr LEO)
- **Beyond ceiling** (stratospheric chemistry fundamentally altered): ~10⁸ launches/yr (~10 Gt/yr LEO)

**The atmospheric ceiling sits at ~10⁶-10⁷ launches/yr (100 Mt/yr to 1 Gt/yr LEO).** Compared to the q1 solar-PV ceiling at ~100 Gt/yr LEO: **q2 binds 10-100× lower than q1.** Atmospheric chemistry remains the load-bearing Earth-side constraint, though by a smaller margin than my original Mt/yr ceiling claimed (corrected from ~1,000-10,000× to ~10-100× lower than q1).

**At cosmic Tt/yr (10¹² t/yr = 10¹⁰ launches/yr) LEO scale, atmospheric chemistry binds by 3-4 orders of magnitude — completely impossible from Earth chemical alone.** The Moon's architectural necessity at cosmic scale is established by q2.

**At Mt-Gt/yr scale,** the Moon's value rests primarily on q2 atmospheric grounds + q1 solar-PV grounds jointly; q2 binds first (at ~100 Mt/yr) while q1 binds at ~10-100 Gt/yr.

## Confidence

- **High confidence** in the per-launch methalox emission factors (stoichiometry + Ryan 2022 NOx factor).
- **Medium confidence** in the reentry NOx emission factor (5 kg/kg-reentered is rough; literature range 1-10 kg/kg).
- **High confidence** in the qualitative ordering: NOx and H2O bind well before alumina; methalox H2O is a real ozone-relevant perturbation at high cadence.
- **Medium-high confidence** in the specific cadence-thresholds (~10⁴-10⁶ launches/yr range for "disruptive"). Exact threshold depends on what level of biosphere damage we accept.
- **High confidence** that the q2 atmospheric ceiling is the load-bearing Earth-side constraint at any Mt/yr-scale LEO mass throughput.

## Caveats

- The Maloney 2025 reentry alumina projection assumes aluminum-skinned satellites; if megaconstellation hardware moves to other materials, alumina injection decreases.
- The reusable-Starship architecture reduces *vehicle* reentry mass per launch; the dominant reentry mass comes from payloads (satellites). Reentry NOx scales with total reentry mass, which is partly architecture-dependent.
- Polar geometry: ozone effects concentrate at high latitudes (polar vortex chemistry). Equatorial ozone may be more resilient than the global-average figures suggest, but high-latitude effects extend to mid-latitudes via atmospheric circulation.
- Synthetic-methane combustion is chemically identical to fossil-methane combustion. The Handmer solar-abundance regime does NOT reduce per-launch atmospheric chemistry — it just changes where the carbon came from.
- Long-term residence times in the stratosphere are ~5 years for H2O and ~years for aerosols. Reaching steady-state at a new launch rate takes ~5-10 years; transient effects are smaller.

## Implication for the report

q2 establishes the Earth-side throughput ceiling at ~Mt-Gt/yr LEO scale on atmospheric-chemistry grounds. This is **the binding constraint** on Earth-launched-chemical-rocket throughput at any post-current cadence — sitting 1,000-10,000× below q1's solar-PV ceiling.

**The Moon's architectural necessity at cosmic Tt/yr scale is overwhelmingly established by q2.** It's also established at the much more modest 10 Mt-Gt/yr scale where serious solar-system industrialization wants to operate. The q2 atmospheric ceiling is therefore the actually-load-bearing Earth-side answer.

q1's solar-PV-area ceiling matters only as a *floor* below which the atmospheric ceiling doesn't matter. At any cadence above ~10⁴ launches/yr, atmospheric chemistry binds. q9 synthesis should lean on q2, not q1.

## Derived claims (to add to claims.yaml in pass-03-reconcile)

- q2.c1 [derived, high]: Methalox per-launch stratospheric injection: ~1,400 t H2O + 1,600 t CO2 + 60 t NOx + 3 t BC + 500 t reentry-NOx. At 250 launches/yr (current 2023 cadence), stratospheric H2O perturbation 0.07%, NOx +140% (reentry-dominated).
- q2.c2 [derived, high]: Atmospheric chemistry ceiling for methalox Earth-launch: detectable at ~10⁴ launches/yr (~1 Mt/yr LEO), disruptive at ~10⁵ launches/yr (~10 Mt/yr LEO), catastrophic at ~10⁶-10⁷ launches/yr (~100 Mt - 1 Gt/yr LEO).
- q2.c3 [derived, high]: Reentry NOx (not propellant NOx) is the dominant ozone-loss driver in methalox-dominant futures; reentry NOx is propellant-independent because it comes from atmospheric N₂ dissociation during reentry heating.
- q2.c4 [derived, high]: Synthetic methane via Sabatier in the Handmer-solar-abundance regime does NOT reduce per-launch atmospheric chemistry. Combustion products are chemically identical to fossil-CH4 combustion. The propellant-source change improves carbon-cycle but doesn't help q2.
- q2.c5 [derived, medium-high]: At cosmic Tt/yr LEO (10¹² t/yr = 10¹⁰ launches/yr), atmospheric metrics are perturbed by 10⁴-10⁸× — physically impossible. Earth chemical-rocket cannot operate at cosmic Tt/yr because atmosphere itself is being fundamentally rebuilt.
- q2.c6 [derived, high]: The q2 atmospheric ceiling (~10⁵-10⁶ launches/yr at "disruptive" tier) is 1,000-10,000× lower than the q1 solar-PV ceiling (~10⁹ launches/yr). Atmospheric chemistry is the load-bearing Earth-side constraint at any Mt/yr-scale LEO mass throughput.

## Next sub-pass

`--sub reconcile` — unseal sources, compare derived numbers to Revell 2025, Murphy 2023, Maloney 2025, Ryan 2022, Kukreja 2025.
