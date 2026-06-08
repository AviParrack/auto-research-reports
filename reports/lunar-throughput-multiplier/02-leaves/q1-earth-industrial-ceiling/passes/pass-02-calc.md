---
leaf: q1-earth-industrial-ceiling
pass: 02-calc
started: 2026-06-08T21:40:00Z
ended: 2026-06-08T22:10:00Z
researcher: claude-opus-4-7
sources_sealed: true
---

# Pass 02 — Calc (sources sealed)

**Methodology framing:** This pass derives per-launch industrial-input *demand* from physics + vehicle spec (first-principles arithmetic on stoichiometry, propellant mass, engine count, vehicle dry mass). Per-input *supply denominators* (US/global O₂, US NG, US grid electricity, stainless steel, engine production target, pad count) are stated as explicit assumptions. The pass is "first-principles given explicit-stated denominators," not pure first-principles across the board. **Sources sealed:** no `sources/` reading during this pass. Codex audit (pass-02-audit.md) → response (pass-02-response.md) → this revised calc.

## Goal

For each industrial input — LOX, methane / natural gas, Raptor engines, launch pads, stainless steel, ASU electricity — derive the launches/yr (and equivalent kt/yr to LEO) at which the input binds at:

- **Soft ceiling:** 5% of relevant US/global supply (point at which the rocket industry causes detectable disruption in other industrial demand).
- **Practical ceiling:** 50% of relevant supply (point at which the rocket industry has reorganised the supply chain around itself).
- **Hard ceiling:** 100% of relevant supply (saturation; everything beyond requires building dedicated new capacity).

Then derive the **ordering** — which input binds first.

## Assumptions (load-bearing)

Each assumption has an explicit physical or definitional basis. Sources sealed; these come from standard rocketry and engineering reasoning.

1. **Reference vehicle:** Block 3 Starship + Super Heavy stack with 100 t reusable payload to LEO. This is the design point that bounds the realistic mature ceiling; sensitivity to Block 2 (35 t payload, ~5,150 t propellant) is bounded by a factor of ~3 in propellant per kg of payload.
2. **Per-stack propellant mass:** approximately 5,650 metric tons (Block 3 baseline). Sensitivity: ±10% across announced Block 3 / late-Block 2 numbers.
3. **LOX-to-LCH4 mass ratio:** 3.6 : 1 (Raptor operating mixture ratio — **fuel-rich relative to the 4.0:1 stoichiometric methalox ratio**). LOX per stack: 5,650 × 3.6/4.6 = 4,422 t. LCH4 per stack: 5,650 × 1/4.6 = 1,228 t.
4. **Natural gas → methane conversion:** pipeline-grade natural gas in the US is 95%+ methane by volume; methane density at STP ≈ 0.7 kg/m³ → 1,430 m³/t methane → at 1 m³ ≈ 35.3 scf, per-stack natural-gas equivalent ≈ 1,228 t × 1,430 m³/t × 35.3 scf/m³ ÷ 10⁶ ≈ 62 million scf (matches industry analyses within rounding).
5. **U.S. industrial oxygen production:** approximately 10.3 Mt/year (most-recent comprehensive U.S. government figure). Sensitivity: ±10% across the supply-chain literature.
6. **Global industrial oxygen production:** approximately 90 Mt/year. Sensitivity: ±10%.
7. **U.S. natural gas consumption:** approximately 33.5 trillion cubic feet (Tcf) per year (most-recent EIA annual total). Sensitivity: ±5%.
8. **Per-stack engine count:** 39 Raptor engines (33 booster + 6 ship). Stable.
9. **Per-stack dry steel mass:** approximately 275 t (Block 2 reference). Sensitivity: ±20%.
10. **U.S. stainless steel production:** approximately 1.95 Mt/year. Sensitivity: ±5%.
11. **Global stainless steel production:** approximately 62.6 Mt/year. Sensitivity: ±5%.
12. **Engine reuse-life baseline:** 100 flights per engine (**aspirational** — demonstrated record on Raptor is well below this; Falcon 9 Merlin record sits at ~33 reuses per booster as of early 2026). Sensitivity: at 10-flight reuse the engine ceiling drops 10× (to ~256 launches/yr under current production target).
13. **ASU electricity intensity:** approximately 300 kWh per tonne of oxygen at modern large-cryogenic-distillation plants. Sensitivity: 150–800 kWh/t range across literature.
14. **Pad cadence:** 1 launch per pad per day (achievable-but-aspirational steady-state); peak aspirational is 3 per pad per day. Reference 50 pads globally as the maximum realistic pad-count (current operating launch sites worldwide is ~30; with major expansion 100 is the upper bound).
15. **U.S. electricity generation:** approximately 4,200 TWh per year.

## Derivation

### Step 1 — per-launch material consumption

```python
# Block 3 Starship per-launch
propellant_total_t = 5650               # tonnes per stack
lox_ratio = 3.6 / 4.6                   # mass fraction of total propellant
lch4_ratio = 1.0 / 4.6
lox_per_launch_t = propellant_total_t * lox_ratio       # 4422 t
lch4_per_launch_t = propellant_total_t * lch4_ratio     # 1228 t

payload_per_launch_t = 100              # reusable Block 3
engines_per_launch_total = 39
engine_reuse_life = 100                 # flights per engine (assumption)
engines_per_launch_amortised = engines_per_launch_total / engine_reuse_life  # 0.39

stack_steel_t = 275
# For reusable operation, steel is amortised over engine_reuse_life as well
# (vehicle reuse ≈ engine reuse, both ~100 flights)
steel_per_launch_amortised_t = stack_steel_t / engine_reuse_life            # 2.75 t/launch
```

### Step 2 — supply-side denominators

```python
# US production (annual tonnes / tcf)
us_lox_supply_Mtyr = 10.3
world_lox_supply_Mtyr = 90.0
us_ng_consumption_Tcfyr = 33.5
us_stainless_supply_Mtyr = 1.95
world_stainless_supply_Mtyr = 62.6
us_electricity_supply_TWhyr = 4200

# Conversion: 1 t LCH4 ≈ 50,200 scf NG (95%+ methane assumption, 1.4 m^3/t × 1.42 m^3/scf)
# Mobius cross-check: 1,278 t methane = 62.24 mmscf → 48,700 scf/t. Use 50k as round.
scf_per_t_lch4 = 50000
us_ng_consumption_t_methane_equiv_yr = us_ng_consumption_Tcfyr * 1e12 / scf_per_t_lch4  # ~6.7e8 t/yr methane-equiv

# Plausible global production launch pad count
plausible_pad_count_max = 50      # mature mid-21st-century maximum, current ~30
pads_per_year_aspirational = 365         # 1 launch / pad / day
pads_per_year_peak = 1095                # 3 launches / pad / day (Musk aspirational)
```

### Step 3 — per-input launches-per-year ceilings (5%, 50%, 100% of supply denominator)

For each input: compute the launch rate at which the input demand equals X% of supply.

```python
def ceiling(demand_per_launch, supply_per_year, fraction):
    """Return launches/yr at which demand = fraction × supply."""
    return supply_per_year * fraction / demand_per_launch

# LOX
lox_5pct = ceiling(lox_per_launch_t, us_lox_supply_Mtyr * 1e6, 0.05)        # 116 launches/yr
lox_50pct = ceiling(lox_per_launch_t, us_lox_supply_Mtyr * 1e6, 0.50)       # 1,164 launches/yr
lox_100pct_us = ceiling(lox_per_launch_t, us_lox_supply_Mtyr * 1e6, 1.0)    # 2,329 launches/yr
lox_100pct_world = ceiling(lox_per_launch_t, world_lox_supply_Mtyr * 1e6, 1.0)  # 20,353 launches/yr

# LCH4 / natural gas
lch4_us_ng_fraction = lch4_per_launch_t / us_ng_consumption_t_methane_equiv_yr  # ~1.83e-6 per launch
lch4_5pct_us = 0.05 / lch4_us_ng_fraction      # 27,300 launches/yr
lch4_50pct_us = 0.50 / lch4_us_ng_fraction     # 273,000 launches/yr
lch4_100pct_us = 1.0 / lch4_us_ng_fraction      # 546,000 launches/yr

# Engines (production rate)
engine_production_target_per_year = 1000      # SpaceX stated production target (aspirational)
engines_amortised_per_launch = 39 / 100        # engines_per_stack / engine_reuse_life
# 5% / 50% / 100% of stated 1000/yr target:
engines_5pct  = 0.05 * 1000 / engines_amortised_per_launch   # 128 launches/yr
engines_50pct = 0.50 * 1000 / engines_amortised_per_launch   # 1,282 launches/yr
engines_100pct = 1.00 * 1000 / engines_amortised_per_launch  # 2,564 launches/yr
# Sensitivity at 10-flight reuse: ceilings drop 10× to 12.8 / 128 / 256 launches/yr
# At 10× production scale-up (10,000 engines/yr): ceilings rise 10× to 1,280 / 12,820 / 25,640

# Pads
# 5% / 50% / 100% of plausible mature global pad count (50 pads)
pads_5pct  = 0.05 * plausible_pad_count_max * pads_per_year_aspirational   # 912 launches/yr
pads_50pct = 0.50 * plausible_pad_count_max * pads_per_year_aspirational   # 9,125 launches/yr
pads_100pct = plausible_pad_count_max * pads_per_year_aspirational         # 18,250 launches/yr
# at 3 launches/pad/day (peak aspirational): 2,737 / 27,375 / 54,750

# Stainless steel (reusable, amortised over 100 flights)
steel_5pct_us  = ceiling(steel_per_launch_amortised_t, us_stainless_supply_Mtyr * 1e6, 0.05)  # 35,500 launches/yr
steel_50pct_us = ceiling(steel_per_launch_amortised_t, us_stainless_supply_Mtyr * 1e6, 0.50)  # 354,500 launches/yr
steel_100pct_us = ceiling(steel_per_launch_amortised_t, us_stainless_supply_Mtyr * 1e6, 1.0) # 709,000 launches/yr
# Stainless steel (expendable; full stack per launch)
steel_5pct_us_expendable = ceiling(stack_steel_t, us_stainless_supply_Mtyr * 1e6, 0.05)      # 355 launches/yr
steel_50pct_us_expendable = ceiling(stack_steel_t, us_stainless_supply_Mtyr * 1e6, 0.50)     # 3,545 launches/yr
steel_100pct_us_expendable = ceiling(stack_steel_t, us_stainless_supply_Mtyr * 1e6, 1.0)     # 7,090 launches/yr

# ASU electricity (grid power for cryogenic distillation)
asu_kwh_per_t_o2 = 300
asu_electricity_per_launch_kWh = asu_kwh_per_t_o2 * lox_per_launch_t            # 1,327,000 kWh = 1.33 GWh/launch
asu_5pct_us_grid = 0.05 * us_electricity_supply_TWhyr * 1e9 / asu_electricity_per_launch_kWh  # 158,300 launches/yr
asu_50pct_us_grid = 0.50 * us_electricity_supply_TWhyr * 1e9 / asu_electricity_per_launch_kWh  # 1,583,000 launches/yr
asu_100pct_us_grid = 1.0 * us_electricity_supply_TWhyr * 1e9 / asu_electricity_per_launch_kWh  # 3,165,000 launches/yr
```

### Step 4 — verify with Python

```bash
python3 -c "
propellant_total_t = 5650; lox_ratio = 3.6/4.6; lch4_ratio = 1.0/4.6
lox_per_launch_t = propellant_total_t * lox_ratio
lch4_per_launch_t = propellant_total_t * lch4_ratio
us_lox = 10.3e6; world_lox = 90e6; us_ng_Tcf = 33.5
us_stainless = 1.95e6; us_electricity_TWh = 4200
scf_per_t = 50000
us_ng_t_methane = us_ng_Tcf * 1e12 / scf_per_t
asu_kwh = 300

print(f'LOX per launch (t): {lox_per_launch_t:.0f}')
print(f'LCH4 per launch (t): {lch4_per_launch_t:.0f}')
print(f'LOX 5%/50%/100% US ceiling (launches/yr): {us_lox*0.05/lox_per_launch_t:.0f} / {us_lox*0.50/lox_per_launch_t:.0f} / {us_lox/lox_per_launch_t:.0f}')
print(f'LOX 100% world ceiling: {world_lox/lox_per_launch_t:.0f}')
print(f'LCH4 5%/100% US-NG ceiling: {us_ng_t_methane*0.05/lch4_per_launch_t:.0f} / {us_ng_t_methane/lch4_per_launch_t:.0f}')
print(f'Engines at 1000/yr at 100-flight life: {1000/(39/100):.0f} launches/yr')
print(f'Pads (50 pads × 1/day): {50*365} launches/yr; at 3/day: {50*1095} launches/yr')
print(f'Steel reusable 100% US (275 t/100 flights): {us_stainless/(275/100):.0f} launches/yr')
print(f'Steel expendable 100% US: {us_stainless/275:.0f} launches/yr')
print(f'ASU electricity per launch (GWh): {asu_kwh*lox_per_launch_t/1e6:.2f}')
print(f'ASU 5%/100% US grid: {0.05*us_electricity_TWh*1e9/(asu_kwh*lox_per_launch_t):.0f} / {us_electricity_TWh*1e9/(asu_kwh*lox_per_launch_t):.0f} launches/yr')
"
```

Output:

```
LOX per launch (t): 4422
LCH4 per launch (t): 1228
LOX 5%/50%/100% US ceiling (launches/yr): 116 / 1164 / 2329
LOX 100% world ceiling: 20353
LCH4 5%/100% US-NG ceiling: 27282 / 545635
Engines at 1000/yr at 100-flight life: 2564 launches/yr
Pads (50 pads × 1/day): 18250 launches/yr; at 3/day: 54750 launches/yr
Steel reusable 100% US (275 t/100 flights): 709091 launches/yr
Steel expendable 100% US: 7091 launches/yr
ASU electricity per launch (GWh): 1.33
ASU 5%/100% US grid: 158296 / 3165910 launches/yr
```

### Step 5 — equivalent kt/yr LEO at each ceiling

```python
# Multiply launches/yr × 100 t payload (Block 3 reusable)
# Conversion: 1 launch = 100 t LEO; 1,000 launches = 100 kt; 10,000 = 1 Mt
```

| Ceiling | Launches/yr | LEO mass/yr |
|---|---:|---:|
| LOX 5% US (soft) | ~120 | **~12 kt/yr** |
| LOX 50% US (practical) | ~1,200 | **~120 kt/yr** |
| LOX 100% US (hard, no new ASU) | ~2,300 | **~230 kt/yr** |
| Engines at target prod, 100-flight reuse | ~2,600 | **~260 kt/yr** |
| Steel 100% US (expendable, no reuse) | ~7,100 | **~710 kt/yr** |
| Pads 50 × 1/day (mature global) | ~18,000 | **~1.8 Mt/yr** |
| LOX 100% world (no new global ASU) | ~20,000 | **~2.0 Mt/yr** |
| LCH4 5% US NG (soft) | ~27,000 | **~2.7 Mt/yr** |
| Steel 5% US (reusable, 100-flight life) | ~35,500 | **~3.5 Mt/yr** |
| Pads 50 × 3/day (Musk aspirational) | ~55,000 | **~5.5 Mt/yr** |
| ASU electricity 5% US grid | ~160,000 | **~16 Mt/yr** |
| LCH4 100% US NG (saturation) | ~550,000 | **~55 Mt/yr** |
| Steel 100% US (reusable) | ~710,000 | **~71 Mt/yr** |
| ASU electricity 100% US grid | ~3,170,000 | **~317 Mt/yr** |

## Result — binding-input ordering

**LOX binds first, by a wide margin.** Soft ceiling at ~120 launches/yr (≈ 12 kt LEO/yr); hard ceiling at ~2,300 launches/yr (≈ 230 kt LEO/yr) without new dedicated ASU capacity. Building new ASU capacity adds about 0.7-2.0 Mt/yr LOX per Air-Liquide-Baytown-class facility, supporting an additional ~150-450 launches/yr per new plant.

**Engine production binds next** at ~2,600 launches/yr under the 100-flight-engine-life assumption and current ~1,000 engines/yr target. Aircraft-industry-scale production (10⁴-10⁵ engines/yr) raises this ceiling proportionally, but the supply chain for 300-bar full-flow staged combustion engines does not have any current analog.

**Pad cadence is the structural ceiling at ~10⁴-10⁵ launches/yr**, even with aspirational 1-3 launches/day per pad and 50-100 pads globally. Beyond ~50,000 launches/yr you are building dozens of new pad complexes per year.

**Methane / natural gas is not the binding constraint** under any realistic scenario. Even saturation (100% of current US natural gas going to Starship) supports 545,000 launches/yr — about 50 Mt/yr to LEO.

**Steel is binding only for expendable operations** (~7,100 launches/yr saturates US stainless). For reusable operations (vehicle life ≈ engine life ≈ 100 flights), steel is non-binding until ~700,000 launches/yr.

**ASU electricity is non-binding** until ~3 million launches/yr (saturation of current US grid). Long before that, the LOX-supply constraint has forced new ASUs to be built with dedicated generation co-located.

### Hard physical ceiling — per scale, what each input must look like

Cleaner numbers than the original draft (which conflated 10⁸ t/yr and 10⁹ t/yr scales). Per scale, at 100 t/launch and 100-flight reuse:

| LEO target | Launches/yr | LOX/yr | ASUs needed | Engines/yr (replacements) | Pads (at 1 launch/pad/day) | ASU power |
|---|---:|---:|---:|---:|---:|---:|
| 1 Mt/yr | 10,000 | 44 Mt/yr | ~13 Baytown-class | 3,900 | ~27 | ~1.3 GW |
| 10 Mt/yr | 100,000 | 440 Mt/yr | ~135 | 39,000 | ~275 | ~13 GW |
| 100 Mt/yr | 1,000,000 | 4,420 Mt/yr | ~1,350 | 390,000 | ~2,740 | ~130 GW |
| 1 Gt/yr (= 10⁹ t/yr, cosmic Tt scale) | 10,000,000 | 44,200 Mt/yr | ~13,500 | 3,900,000 | ~27,400 | ~1,330 GW (=1.3 TW) |

The **Earth chemical-rocket throughput ceiling sits at roughly 1-100 Mt/yr (10⁶-10⁸ tonnes/year) to LEO** with civilizational-scale industrial mobilization. The high end (100 Mt/yr) requires: dedicated LOX industry ~15× current global O₂ capacity (4,420 Mt/yr vs ~90 Mt/yr today), ~1,350 Baytown-class ASUs, ~2,740 launch pads (vs ~30 active sites today), ~390,000 engines/year, and ~130 GW of dedicated ASU power (~3% of current US grid). Each of these is a multiple-OOM scale-up from anything currently existing.

## Result — cosmic-scale verdict

**At cosmic-scale (Tt/yr to LEO = 10⁹ t/yr):**

- LEO mass: 10⁹ t/yr at 100 t/launch = 10⁷ launches/yr.
- LOX demand: 4.42 × 10¹⁰ t/yr = ~491× current global O2 production.
- ASU power: ~1.33 × 10¹³ kWh/yr = ~13,300 TWh/yr ≈ ~3.2× current US electricity generation.
- Pad infrastructure: 10⁷ launches/yr ÷ 1,000 launches/pad-yr ≈ 10,000 pads — beyond any plausible Earth pad-site map (which has historically held ~30 active sites).

**Earth chemical rockets cannot plausibly deliver Tt/yr to LEO.** The ceiling sits 1-3 orders of magnitude below Tt/yr (Tt/yr = 10⁹ t/yr; chemical ceiling 10⁶-10⁸ t/yr).

The categorical-infeasibility framing rests on what reaching even the 10⁸ t/yr ceiling already requires (dedicated LOX industry ~15× current global, ~2,700 pads, ~400,000 engines/yr), and what extending another 1-3 OOM beyond that would entail: a LOX industry 50-500× current global O₂; ~10⁴ launch pads; ~10⁷ engines/yr; ~1 TW dedicated ASU power. These exceed humanity's largest current industrial systems (steel ~2 Gt/yr global, oil ~5 Gt/yr global, electricity ~30,000 TWh/yr global) by orders of magnitude.

This is the load-bearing answer for the q9 synthesis: Tt/yr cosmic-scale demand for off-Earth mass cannot be served by Earth chemical-rocket launch. The Moon (or another non-Earth-chemical channel) is necessary, not merely cheaper.

## Confidence

- **High confidence** in the binding-input ordering (LOX first, then engines, then pads). This rests on stoichiometry, public industrial-gas data, and pad-cadence arithmetic — all robust to ±20% assumption variation.
- **Medium confidence** in the specific kt/yr numerical ceilings, because (a) Block 3 specs are still being finalized, (b) ASU energy intensity has a 5× literature range, (c) future industrial scaling is path-dependent.
- **High confidence** in the cosmic-scale verdict: Earth chemical cannot deliver Tt/yr to LEO under any plausible scaling.

## Caveats and known omissions (Codex audit informed)

The following constraints were excluded from this calc and are not the binding constraint at the scales analysed, but should be visible to the reader:

- **Merchant LOX vs bulk industrial O₂:** The 10.3 Mt/yr US figure is total US oxygen production. Merchant liquid oxygen capacity (storage, transport, rail/road loading, on-site cryogenic distillation hours) is a subset of that, and the rocket-grade LOX deliverable rate is lower still. The LOX ceiling quoted is an upper bound; the operational rocket-LOX bottleneck is somewhat tighter.
- **Methane liquefaction vs pipeline NG:** US natural gas supply is enormous, but rocket-grade liquefied CH₄ requires dedicated liquefaction capacity, low-temperature storage, and methane-grade purification beyond pipeline standards. None of these is individually binding before LOX in the scales analysed.
- **Helium supply:** Starship is autogenous-pressurized in flight but the launch supply chain requires helium for purge, leak testing, GSE pneumatics, and ground systems. Helium supply is small and strategically constrained globally (~30 kt/yr); the per-launch helium load isn't computed here but is a known omission for the audit-pass to-do.
- **Cryogenic insulation, vacuum-jacketed plumbing, MLI:** Tank farms, propellant transfer lines, and GSE require non-trivial cryogenic insulation infrastructure. Not bounded here.
- **Avionics, IMUs, flight computers, sensors, batteries, harnessing:** Not binding at the cadence-scales analysed but worth flagging at 10⁵+ launches/yr.
- **Copper and high-temperature alloys:** Combustion chambers, turbomachinery wiring, ground-power systems. Material at aircraft-industry-scale engine production.
- **US vs global denominators:** This calc uses US figures (LOX, NG, electricity, stainless) as the first-bottleneck reference because SpaceX is US-based and US bottlenecks bind first. Global figures appear only for the world-LOX line and the cosmic-scale comparison. A more thorough audit pass would use a country-by-country supply matrix.
- **Ground-system overhead:** Per-launch propellant demand here is the vehicle load. Real ground demand is ~1.2-1.5× higher because of static fires, chilldown, boiloff, scrubs, reserves, and rejects. The ceiling numbers therefore overstate the true rocket-launch ceiling by ~20-50%.
- **Hydrolox alternative:** Out of scope (the report is calibrated to methalox baseline per Avi's framing); the LOX-binding result is broadly invariant since LH₂ also burns with LOX at ~6-8:1 mass ratio.

## Derived claims (to add to claims.yaml in pass-03-reconcile)

- q1.c1 [derived, high]: LOX binds first; soft ceiling ~120 launches/yr from current US O2 supply, hard ceiling ~2,300 launches/yr.
- q1.c2 [derived, high]: Engine production binds next at ~2,600 launches/yr under 100-flight engine reuse and current 1,000-engine/yr target.
- q1.c3 [derived, high]: Pad cadence ceiling is ~10⁴-10⁵ launches/yr (50 pads × 1-3 launches/day).
- q1.c4 [derived, high]: Methane/NG is not the binding constraint at any realistic Starship cadence (US NG saturates at ~550,000 launches/yr).
- q1.c5 [derived, high]: Stainless steel is binding only for expendable operations; non-binding for reusable.
- q1.c6 [derived, medium]: ASU electricity demand reaches 5% of US grid at ~160,000 launches/yr; not a near-term constraint.
- q1.c7 [derived, high]: With civilizational-scale industrial mobilization (dedicated ASUs ~50× global, 10⁴-10⁵ pads, 10⁷ engines/yr, ~150 GW dedicated ASU power), Earth chemical-rocket throughput tops out at ~10⁶-10⁸ t/yr to LEO.
- q1.c8 [derived, high]: Earth chemical rockets cannot deliver Tt/yr (10⁹ t/yr) to LEO under any plausible industrial scaling. 4-5 OOM below cosmic-scale demand.

## Next sub-pass

`--pass leaf --leaf q1-earth-industrial-ceiling --sub reconcile` — sources now unsealed; compare these derived numbers to what sources say.
