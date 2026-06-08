---
leaf: q1-earth-industrial-ceiling
pass: 02c-planetary-ceilings
prompted_by: Avi feedback 2026-06-09 ("really really looking for these fundamental constraints, you know, post-singularity still holds")
started: 2026-06-09T01:00:00Z
ended: 2026-06-09T01:40:00Z
researcher: claude-opus-4-7
---

# Pass 02c — Planetary ceilings: the constraints that hold post-singularity

## Why this exists

Avi pushed past the v2 recalc with two further demands:

1. **The Handmer thesis.** Casey Handmer / Terraform Industries argues that solar PV is heading toward absolute abundance — cheap enough that synthetic methane (via Sabatier from atmospheric CO₂ + electrolytic H₂) outcompetes fossil natural gas. If that's right, then "synthetic-methane electricity" is not a willingness-to-scale issue, it's just a solar-PV-deployment issue. **What is the solar-PV-area constraint at cosmic-rocket scale?**

2. **The actual physics ceiling.** Not "50× current industry," not "30% of US grid" — those are demand-observations. The true post-singularity ceiling is when **you start overheating Earth, or you tile half the planet with solar panels, or the atmosphere fills with rocket exhaust faster than it scrubs.** What does that look like? At what LEO mass-flux does it bind?

This pass answers both questions with first-principles arithmetic. The Handmer thesis turns out to be approximately right: the solar-PV-area ceiling for Earth chemical-rocket cosmic throughput sits ~100-1,000× above cosmic Tt/yr scale, not below it. The truly hard ceilings are atmospheric chemistry (q2) and waste heat from non-solar energy supply.

## The Handmer / Terraform thesis, explicitly stated

Casey Handmer's argument (Terraform Industries blog, multiple posts 2022-2026):
- Solar PV is on a learning curve toward extreme cheapness — already $0.10-0.30/W installed at utility scale and falling.
- "Solar PV is a thousand times more productive than plants" — i.e., per m² it converts ~1,000× more solar energy to useful work than photosynthesis.
- "Its fundamental inputs, sunlight and air, are essentially unlimited on any scale meaningful to the next few centuries of growth and development."
- The combination of cheap PV + direct-air-capture CO₂ + electrolytic H₂ + Sabatier reaction produces synthetic methane at projected $4-5/MMBtu long-term — competitive with fossil natural gas.
- Therefore: hydrocarbon supply is not constrained by fossil reserves; it scales with solar deployment.

This thesis has a substantial deficit: Handmer does not address waste-heat, atmospheric chemistry, or large-area land-use externalities at scale. We model them here.

## Per-kg-LEO energy budget (synthetic-propellant architecture)

In the Handmer-architecture (synthetic methane via electrolysis + Sabatier; LOX as byproduct):

```
Per Block-3 Starship launch:
  LCH4 needed: 1,228 t
  LOX needed:  4,422 t
  Payload to LEO: 100 t

Sabatier methane synthesis:
  Per kg CH4: 0.5 kg H2 input (stoichiometric from CO2 + 4H2 -> CH4 + 2H2O)
  Per kg H2 via electrolysis: ~50 kWh (state-of-the-art electrolyser)
  ==> 25 kWh/kg CH4 from electrolysis

Sabatier reaction itself: exothermic; produces process heat. Net energy input
  ~= electrolysis energy.

Liquefaction (cooling LCH4 to ~111 K): ~10% Carnot work overhead on energy
  budget. Net: ~27.5 kWh/kg LCH4 at SOTA.

LOX byproduct: water electrolysis (2 H2O -> 2 H2 + O2) produces 8 kg O2 per kg H2.
  Per kg CH4 (0.5 kg H2 input): 4 kg O2 byproduct.
  Combustion needs: 3.6 kg O2 per kg CH4 (Raptor operating ratio).
  ==> O2 byproduct EXCEEDS combustion need by ~11%. LOX is effectively free.

Per kg LEO mass:
  12.28 kg LCH4 / kg LEO
  ==> 12.28 kg * 27.5 kWh/kg = ~338 kWh/kg LEO at synthesis stage
  ==> ~0.34 MWh/kg LEO of grid electricity for full propellant supply

End-to-end energy (including combustion losses, ground systems, launch ops):
  ~5 MWh/kg LEO (rough; chemical rockets are bad heat engines, ~10x synthesis energy)
```

**Bottom line: in the Handmer-Terraform synthetic-propellant architecture, ~338 kWh of solar PV electricity per kg of LEO mass.** Combustion energy is released in the atmosphere (relevant to waste heat) but the grid demand is much smaller.

## Solar-PV area ceiling

How much of Earth's land area must be covered in solar PV to supply cosmic and post-cosmic LEO throughput? At 20% PV efficiency and 24% capacity factor (~global average), one km² of solar PV produces ~420,000 kWh/yr.

| Solar-PV deployment | km² covered | Avg power (TW) | Annual energy (TWh/yr) | LEO mass throughput (t/yr) | × cosmic Tt/yr |
|---|---:|---:|---:|---:|---:|
| 0.1% of land | 149,000 | 7.2 | 62,600 | 0.185 Tt/yr | 0.2× |
| **1% of land** | **1.49 M** | **71.5** | **626,000** | **1.85 Tt/yr** | **~2×** |
| 5% of land (~10 Saharas) | 7.45 M | 358 | 3.13 M | 9.3 Tt/yr | ~9× |
| 20% of land | 29.8 M | 1,430 | 12.5 M | 37 Tt/yr | ~37× |
| **50% of land** | **74.5 M** | **3,580** | **31.3 M** | **93 Tt/yr** | **~93×** |
| 100% of land | 149 M | 7,150 | 62.6 M | 185 Tt/yr | ~185× |
| **50% land + 50% accessible ocean** | **165 M** | **7,900** | **69.3 M** | **205 Tt/yr** | **~205×** |
| 100% land + 100% accessible ocean | 330 M | 15,800 | 138 M | 410 Tt/yr | ~410× |

**Key findings:**

- **Cosmic Tt/yr LEO requires ~0.5% of land area tiled with solar PV.** That's about the area of Saudi Arabia. Plausible.
- **At Avi's "half of Earth tiled" threshold of concern (50% land + 50% accessible ocean ≈ 200 Tt/yr LEO):** the cosmic Tt/yr scale fits comfortably within this, by a factor of ~200×.
- **The maximum tile-everything ceiling (100% land + 100% accessible ocean) is ~400 Tt/yr LEO.** Beyond this, solar PV area is genuinely exhausted.

So **in a solar-abundance regime, the solar-PV-area ceiling for Earth chemical-rocket throughput sits at ~100-400× cosmic Tt/yr scale**. Cosmic Tt/yr requires only ~0.5% of land — a fraction comparable to the current global footprint of paved roads.

## Waste-heat ceiling (non-solar energy regime)

If energy comes from fossil, nuclear, or fusion (sources that add new heat to Earth's energy budget rather than recycling solar input), waste heat eventually warms the planet. The end-to-end energy per kg of LEO mass is ~5 MWh/kg (including chemical-rocket combustion inefficiency and ground systems).

Climate physics: 1 W/m² radiative forcing → ~0.7°C steady-state warming (at climate sensitivity of ~3°C per CO₂ doubling, which is ~4 W/m² forcing). Earth surface area is 5.1 × 10¹⁴ m². So 510 TW of anthropogenic heat distributed evenly = 1 W/m² ≈ +0.7°C.

| LEO throughput (t/yr) | Continuous power (TW) | Forcing (W/m²) | Waste-heat warming (°C) |
|---:|---:|---:|---:|
| 10⁶ (1 Mt/yr) | 0.001 | 2 × 10⁻⁶ | 1 × 10⁻⁶ |
| 10⁸ (100 Mt/yr) | 0.06 | 1 × 10⁻⁴ | 8 × 10⁻⁵ |
| 10⁹ (1 Tt/yr, cosmic) | 0.6 | 0.001 | 0.001 |
| 10¹⁰ (10 Tt/yr) | 5.7 | 0.011 | 0.008 |
| 10¹¹ (100 Tt/yr) | 57 | 0.11 | 0.08 |
| **10¹² (1 Pt/yr = 1,000 Tt/yr)** | **570** | **1.12** | **0.78** |
| 10¹³ (10 Pt/yr) | 5,700 | 11.2 | 7.8 |

**Key findings:**

- **Cosmic Tt/yr LEO produces 0.6 TW of waste heat, ~0.001°C steady-state warming.** Trivial.
- **+1°C of pure-waste-heat warming requires ~1 Pt/yr LEO (10¹² t/yr).** That's 1,000× cosmic Tt scale.
- **The Pt/yr scale is the actual hard waste-heat ceiling in a non-solar regime.** Even in the most pessimistic energy-supply scenario, this sits 1,000× above cosmic Tt/yr.

**In a solar-abundance regime, this ceiling does not apply** — solar PV doesn't add new heat to Earth; it intercepts incoming solar and converts a fraction to electricity (which is eventually re-radiated as heat anyway, but at the same total power as the intercepted solar). The waste-heat ceiling is only for fossil/nuclear/fusion energy supply.

## What does each regime *look like*?

Vignettes at increasing LEO throughput. Assumes Block-3 reusable at 100 t/launch.

### 1 Mt/yr LEO (~10,000 launches/year, ~30/day)

- About **30 active spaceports** worldwide, each averaging ~1 launch/day.
- ~10-50 dedicated propellant-synthesis plants the scale of one Air Liquide Baytown ($850M, 3.3 Mt LOX/yr).
- Solar PV demand: ~7 GW continuous (~0.0001% of land area dedicated, ~150 km²).
- Cargo throughput: ~3 t/sec average — about 1% of global air-freight cargo throughput.
- **What you see in the world:** routine launch news from 30 sites; coastal industrial clusters at each launch facility; otherwise indistinguishable from today's heavy industry. Aviation traffic far exceeds rocket traffic.

### 100 Mt/yr LEO (~1 M launches/year, ~3,000/day, ~120/hour)

- About **300-500 active spaceports**, including offshore platforms.
- Each launch every ~30 seconds globally.
- Several thousand dedicated propellant plants.
- Solar PV demand: ~700 GW continuous (~0.01% of land area, ~15,000 km² — area of Connecticut).
- Cargo throughput equals **~1× current global ocean container shipping mass-flow.**
- **What you see in the world:** launch corridors on every continent's coastline; offshore launch platforms in shipping lanes; continuous pillar-of-fire spotting from satellites looking at coastlines; airline traffic still much larger but rocket-launch becomes a recognised infrastructure category like ports.

### 1 Tt/yr LEO (cosmic scale, ~10 M launches/year, ~3-launches per second)

- About **10,000 active launch sites**, vast majority offshore platforms or low-traffic equatorial coastline.
- ~3 launches per second globally — a rocket lifting somewhere every ~0.3 seconds.
- Solar PV demand: ~70 TW continuous (~0.5% of land area, ~750,000 km² — area of Turkey or 0.5% land).
- Cargo throughput: **~10× current global container shipping; comparable to global crude oil production volume by mass.**
- **What you see in the world:** continuous trails of rocket exhaust visible from low Earth orbit; ~0.5% of Earth's land area covered in solar PV (visible from space as patches of blue-black); coastal manufacturing zones every few hundred km; failure rate at 1% = 100,000 catastrophic launch failures/year = ~270/day = several spectacular launch disasters per day.
- **Failure rate has to drop by 100-1000× from current rocket reliability** for this to be socially tolerable; that's a real architectural constraint.

### 10 Tt/yr LEO (cosmic × 10, ~10⁸ launches/year, ~3/sec)

- ~30 launches per second globally; effectively continuous launch traffic worldwide.
- Solar PV demand: 700 TW continuous (~5% of land area, ~7.5 M km² — area of Australia).
- Cargo throughput: **~100× current global container shipping; ~5× total global maritime tonnage.**
- **What you see:** dedicated launch ocean shipping lanes; Saharan-scale solar farms; offshore launch platform fleets numbering in the tens of thousands; coastal cities reshaped around launch industry; rocket-failure debris fields a planetary-scale concern.

### 100 Tt/yr LEO (cosmic × 100, post-singularity threshold)

- ~300 launches per second globally; a continuous launch every few milliseconds.
- Solar PV demand: 7,000 TW continuous (~50% of land area, ~75 M km²).
- **Avi's threshold-of-concern level: "we've tiled half the land area with solar panels."** This is the regime where the answer becomes "we're getting toward a cap."
- Cargo throughput equivalent to **the total mass humanity moves through global shipping, aviation, and rail combined × 100.**
- **What you see:** Earth tiled with solar panels and propellant plants in vast quantities; ocean equally tiled; massive industrial transformation reshaping coasts; civilization is *primarily* a launch civilization at this point.

### Maximum (100% land + 100% accessible ocean, ~400 Tt/yr)

- This is the **absolute solar-PV-area ceiling** in the Handmer-architecture.
- Every available square metre of Earth dedicated to either solar PV or launch infrastructure or rocket fuel synthesis.
- Beyond this, you cannot supply more energy from Earth's solar input without extra-planetary supply (space-based solar, lunar power-beaming).

## The truly hard ceilings (post-singularity, fundamental physics only)

| Ceiling | LEO mass-flux | × cosmic Tt | What you're saturating |
|---|---:|---:|---|
| Solar PV area (50% land + 50% ocean) | ~200 Tt/yr | ~200× | Half of Earth's land + accessible ocean tiled |
| Solar PV area (100% land + 100% ocean) | ~400 Tt/yr | ~400× | All practical solar-PV land |
| Waste heat (non-solar energy regime) +1°C | ~1 Pt/yr (= 1,000 Tt/yr) | ~1,000× | Earth's planet-heating limit from added energy |
| **Atmospheric chemistry (q2 territory)** | **TBD by q2** | **probably << 1×** | **Ozone, reentry metals, plume chemistry, stratospheric H₂O** |

**The atmospheric ceiling almost certainly binds well below cosmic Tt/yr**, based on current trajectory of ozone-impact research at ~2,000-10,000 launches/yr. The fundamental Earth-side ceiling on chemical-rocket throughput is **q2's domain, not q1's.**

## Revised conclusion for q1

**Industrial inputs are not fundamentally binding at any throughput up to ~100-400 Tt/yr LEO.** In a post-singularity solar-abundance regime, cosmic Tt/yr LEO requires:

- ~0.5% of Earth's land area tiled with solar PV (similar to current global paved-road area)
- ~70 TW continuous solar generation (about 0.06% of Earth's solar input)
- ~10,000 launch sites globally, mostly offshore platforms
- Cargo throughput ~10× current global container shipping

**None of this exceeds Earth-system limits.** Energy is not binding; PV area is not binding; waste heat is not binding. The only fundamentally-Earth-system-binding constraint is atmospheric chemistry (q2's territory) — and probably orbital congestion / Kessler cascade dynamics at this launch rate.

**The Handmer thesis is approximately correct:** solar-derived synthetic propellant scales to cosmic chemical-rocket throughput without saturating Earth's energy budget. The fundamental binding constraints are atmospheric and orbital, not energy or industrial.

**At post-singularity-mature civilization scale (10-100× cosmic Tt/yr):**
- Energy is still not binding (5-50% of land tiled with solar)
- Waste heat in non-solar regime would start binding at ~100 Tt/yr (~0.08°C from rocket waste heat alone)
- Atmospheric chemistry almost certainly long-since-binding by q2's analysis
- Orbital congestion impossible without Moon-based catcher/staging at this rate

**The truly absolute Earth-physics ceiling on chemical-rocket throughput is ~400 Tt/yr (PV area exhausted) or ~1 Pt/yr (waste heat in non-solar regime).** Beyond cosmic Tt/yr by 400×-1,000×.

## Implication for the report architecture

The Moon's necessity for cosmic-scale Tt/yr throughput **does not rest on Earth's chemical-rocket ceiling being categorically too low**. From q1's analysis alone:

- Earth chemical can supply cosmic Tt/yr LEO in a Handmer-synthetic-propellant regime.
- Earth chemical can theoretically supply 100-400× cosmic Tt/yr LEO before saturating Earth-system limits.
- The Moon's value at this scale is **not** "Earth can't do it" but rather:
  - Atmospheric chemistry (q2) may make Earth-launch socially or environmentally unacceptable well before the physical ceiling.
  - Per-kg energy cost from the Moon (mass driver, ~2.4 MJ/kg + minor capture energy) is **~100× cheaper than Earth chemical** (300+ MJ/kg-LEO end-to-end).
  - Destinations beyond LEO (Mars, NEAs, Belt, Mercury) benefit enormously from the Moon's low gravity well (q3's territory).
  - Cargo bypass of Earth's atmospheric envelope reduces pollution per kg-delivered.

**This is the v3 conclusion for q1.** The Earth chemical-rocket throughput ceiling is NOT the load-bearing case for lunar mass-driver necessity. The case rests on atmospheric chemistry (q2), interplanetary destination economics (q3, q8), and total mass-delivered-per-unit-Earth-disruption ratios.

## New claims to add to claims.yaml

- q1.c17: Per-kg-LEO energy budget in the Handmer synthetic-methane architecture is ~338 kWh/kg-LEO at SOTA electrolysis efficiency, ~5 MWh/kg-LEO end-to-end including combustion losses. Water electrolysis upstream of Sabatier co-produces enough O₂ to satisfy combustion needs (+11% surplus). LOX is effectively free in the synthetic-propellant architecture.
- q1.c18: At ~0.5% of Earth land area covered in solar PV (~750,000 km², ~area of Turkey, comparable to current global paved-road area), cosmic Tt/yr LEO mass-throughput is energetically feasible. Solar PV area is not fundamentally binding until ~100-400 Tt/yr LEO (50-100% land + ocean tiling).
- q1.c19: In a non-solar energy supply regime (fossil, nuclear, fusion), the waste-heat ceiling on Earth chemical-rocket throughput binds at ~1 Pt/yr LEO (1,000× cosmic Tt) — producing ~570 TW continuous, ~1 W/m² forcing, ~+0.78°C steady-state warming from rocket energy alone.
- q1.c20: The Moon's necessity for cosmic-Tt/yr LEO throughput does NOT rest on Earth chemical being categorically unable to deliver. From q1 alone, Earth chemical can supply cosmic Tt/yr (and 100-400× beyond) before saturating fundamental Earth-system limits. The Moon's value rests on (a) atmospheric chemistry (q2), (b) energy efficiency per kg delivered (~100× lower from lunar surface), (c) destination economics beyond LEO (q3, q8). The "Moon is necessary" argument lives in q2 + q9 synthesis, not in q1's industrial-input analysis.

## Confidence

- High confidence in the synthetic-methane energy budget arithmetic (~338 kWh/kg-LEO).
- High confidence in the LOX-as-byproduct finding (electrolysis stoichiometry).
- Medium-high confidence in the solar-PV area arithmetic at SOTA efficiency.
- High confidence in the waste-heat ceiling order-of-magnitude (~Pt/yr threshold).
- Medium confidence in the "what does it look like" vignettes — the launch-failure-rate analysis at 10⁷ launches/yr depends on assumed reliability.
- High confidence on the qualitative conclusion: Earth chemical can supply cosmic Tt/yr LEO in a solar-abundance regime; q1 does not establish lunar-necessity.

## Next action

Update claims.yaml with q1.c17-c20. Run Codex audit on this pass. Then update q1's leaf write (v3) with the planetary-ceilings framing. Or: defer write update and move to q2 (which is now clearly the load-bearing leaf for the Moon-necessity argument).
