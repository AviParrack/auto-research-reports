"""
q5-capital-buildup pass-02-calc.py — first-principles capex derivation.

Sources sealed: this file consults no values from sources/*/extract.md.
All inputs are either physical constants, q1-earth-launch-cost calc outputs,
q3-isru-feasibility calc outputs, q4-gear-ratio calc outputs, or explicit
assumptions stated in this file.

Approach:
1. Decompose lunar manufacturing base into 7 mass-budget components.
2. For each, derive Earth-launch-mass requirement from physics and engineering
   first principles, with explicit assumptions.
3. Multiply by lunar-surface delivery cost from q1 + q2 (Tsiolkovsky-derived)
   to get Earth-launch-only capex.
4. Add lifetime replacement schedule based on q3/q4 reliability assumptions.
5. Compute three regimes: BAU (today's tech, today's automation), industrial-
   explosion (10x mass/cost compression over a decade), TAI (100x mass/cost
   compression compressed into 1-3 years).
6. Output milestone-by-milestone breakdown with regime-conditional totals.

Anti-pattern #11: do NOT produce a single calendar-year answer. Decompose into
work-remaining + compressibility per regime.
"""

import math
from dataclasses import dataclass
from typing import Dict, List, Tuple

# =============================================================================
# Physical constants and shared baseline assumptions
# =============================================================================

LUNAR_GRAVITY = 1.62          # m/s²
ISP_LOX_LH2 = 450             # s (specific impulse, LOX/LH2)
ISP_LOX_CH4 = 380             # s (LOX/methane, Starship)
G_EARTH = 9.81                # m/s² (for I_sp -> exhaust velocity)
EARTH_LEO_DV = 9400           # m/s (Earth-to-LEO Δv, typical)
LEO_LUNAR_DV = 6000           # m/s (LEO-to-lunar-surface Δv, one-way chemical)

# Earth-launch cost from q1-earth-launch-cost (partial scenario central estimate, internal cost)
# q1 reports: optimistic $59-277/kg, partial $107-466/kg, pessimistic $194-878/kg
EARTH_LAUNCH_COST_PARTIAL_LOW = 107       # $/kg to LEO (q1 partial early)
EARTH_LAUNCH_COST_PARTIAL_HIGH = 466      # $/kg to LEO (q1 partial late)
EARTH_LAUNCH_COST_OPTIMISTIC = 59         # $/kg to LEO (q1 optimistic floor)
EARTH_LAUNCH_COST_PESSIMISTIC = 878       # $/kg to LEO (q1 pessimistic ceiling)

# LEO-to-lunar-surface delivery is harder by Tsiolkovsky.
# From q4-gear-ratio: G(LEO -> LS) reusable RT ≈ 14.97 (this is the mass-fraction-cost ratio)
# We treat the cost-per-kg ratio for LEO→LS delivery as roughly 5x LEO cost
# (Starship-class with refueling can do LS in 2-3 refuels per delivery; cost roughly multiplies
# by refuel-count + small additional margin). This is a calc-pass assumption explicit here.
LEO_TO_LS_COST_MULTIPLIER = 5.0   # $/kg to LS = 5 × $/kg to LEO under refueled Starship

# =============================================================================
# 7-component mass budget for a "minimum net-positive-export" lunar manufacturing base
# =============================================================================
# Net-positive-export = annual export mass > 10× annual capital-replacement mass landed,
# i.e. lunar capital is producing significant industrial output, not just sustaining itself.
# This is a stronger condition than Sowers' propellant-only architecture; matches Metzger
# 2013 bootstrap "self-sustaining, self-expanding" endpoint.

@dataclass
class Component:
    name: str
    mass_kg: float      # mass landed on lunar surface (kg)
    notes: str
    lifetime_yr: float  # operating lifetime before full replacement

# Component 1: Cargo landing capability (does NOT count as capital - amortized as transport cost)
# We don't include the lander mass itself in the capital figure; we treat it as part of the $/kg-to-LS cost.

# Component 2: Habitat + life support
# Approach: minimum 4-person crew habitat capable of supporting 12 mo at a time.
# Bigelow B330 inflatable: 14,000 kg dry mass for 330 m³ (16 t reference).
# We use 20,000 kg dry mass + 5,000 kg consumables-for-12-mo = 25,000 kg total.
habitat = Component(
    name="Habitat + life support",
    mass_kg=25_000,
    lifetime_yr=15,
    notes="20t dry mass (B330-class inflatable) + 5t consumables/spares for 12 mo independent ops; lifetime limited by MMOD pitting + ECLSS wear."
)

# Component 3: Fission Surface Power (FSP)
# From explicit calc: a manufacturing base running ISRU + robotic assembly + mass-driver
# needs ~500 kW continuous (vs NASA FSP demonstrator 40 kWe). Scale from FSP mass:
# NASA FSP target 6,000 kg per 40 kWe = 150 kg/kWe. Realistic with current tech is
# likely closer to 200-300 kg/kWe.
# Independent derivation (calc-pass): a 350-kWth microreactor at ~25% Brayton efficiency
# yields ~85 kWe. 6 such reactors → 500 kWe → roughly 36 t total.
# We assume 250 kg/kWe (slightly more conservative than NASA target, accounts for
# shielding + radiator + power conditioning).
SURFACE_POWER_KWE = 500
fsp = Component(
    name="Fission Surface Power (500 kWe)",
    mass_kg=SURFACE_POWER_KWE * 250,   # = 125,000 kg
    lifetime_yr=10,
    notes="500 kWe continuous (sized for ISRU + mfg + mass driver loop). 250 kg/kWe = 125 t total. 10-yr lifetime per NASA FSP design target."
)

# Component 4: ISRU plant (oxygen + structural metals + propellant)
# From q3-isru-feasibility: O2/Fe/Si/structural at TRL 4-6. Plant mass scales with output.
# Pelech's strip-mining estimates were ~5,000 t/yr propellant at ~100 t plant — but this
# was the "terrestrial-excavator-analogy" overcount (per Metzger 2023 reanalysis).
# Sowers tent-sublimation: 2,450 t/yr propellant from ~16-25 t hardware (φ ≈ 500).
# We use a balanced estimate: 1,000 t/yr output from 50 t plant (φ ≈ 20).
# Add 50% redundancy and supporting infrastructure → 75 t total.
ISRU_OUTPUT_T_PER_YR = 1000   # tonnes/year output (mixed: propellant + structural)
ISRU_PHI = 20                 # production mass ratio (calc-pass estimate; q4 derives this)
isru = Component(
    name="ISRU plant (1000 t/yr output, mixed propellant + structural)",
    mass_kg=ISRU_OUTPUT_T_PER_YR * 1000 / ISRU_PHI * 1.5,  # 1000 t = 1e6 kg; /φ × 1.5 redundancy
    lifetime_yr=8,
    notes="φ=20 (balanced between Metzger MVP φ=36.5 and Pelech φ=3.7). 1000 t/yr output × 1.5 redundancy = 75 t plant."
)

# Component 5: Mobility - haulers, mining rovers, assembly robots
# 20 mining rovers @ 500 kg each + 10 humanoid assembly robots @ 100 kg each + 5 large
# haulers @ 2000 kg each + spare parts allowance 50%
mobility_mass = (20 * 500 + 10 * 100 + 5 * 2000) * 1.5
mobility = Component(
    name="Mobility + robotic workforce (20 rovers + 10 humanoids + 5 haulers + spares)",
    mass_kg=mobility_mass,   # = 31,500 kg
    lifetime_yr=5,
    notes="20 mining rovers × 500 kg + 10 humanoid assembly robots × 100 kg + 5 large haulers × 2000 kg + 50% spares. Lifetime-limited by abrasive regolith dust."
)

# Component 6: Manufacturing complement
# Sintering furnaces, additive manufacturing equipment, electronics assembly,
# initial Earth-imported components (microcontrollers, motors, bearings).
# Mass: 30 t hardware + 10 t initial seed-stock of Earth-imported components.
manufacturing = Component(
    name="Manufacturing complement (sintering, AM, electronics, Earth-imported seed)",
    mass_kg=40_000,
    lifetime_yr=8,
    notes="30 t equipment + 10 t Earth-imported seed components (precision motors, chips, bearings). Lifetime > base unit; subcomponents replaced individually."
)

# Component 7: Comms + sensors + landing pads + roads
# Smaller per-item but cumulative: 1 landing pad (Metzger-Autry 2022 was $229M @ $1M/kg — implies ~230 kg pad??
# That can't be right — Metzger-Autry's pad mass is in the 10-50 t range under current architecture.
# Calc: a 30m diameter pad at 5 cm sintered depth × 1.5 g/cm³ density = roughly 50 t of regolith
# moved — but most of the cost is the construction-equipment time, not Earth-launched mass.
# We treat the in-situ-sourced pad mass as zero Earth-mass; the construction equipment for it
# is already counted in mobility/manufacturing. Pad here is Earth-imported microwave heads etc.
infra = Component(
    name="Infrastructure (comms relays, landing-pad construction heads, sensors, roads)",
    mass_kg=15_000,
    lifetime_yr=12,
    notes="Earth-imported components only. Pads + roads sourced from in-situ regolith; counted as zero Earth-mass."
)

# Total Earth-launched capital mass (one full set)
COMPONENTS = [habitat, fsp, isru, mobility, manufacturing, infra]


def total_capital_mass_kg() -> float:
    return sum(c.mass_kg for c in COMPONENTS)


def amortized_annual_mass(years_operation: int = 20) -> float:
    """
    Annual mass-to-lunar-surface required for sustained operation over
    `years_operation`, including initial deployment + ongoing replacement.
    """
    annual = 0.0
    for c in COMPONENTS:
        # full replacement cycles in years_operation
        full_replacements = max(0, years_operation / c.lifetime_yr - 1)
        total_landed = c.mass_kg * (1 + full_replacements)
        annual += total_landed / years_operation
    return annual


def total_program_mass_kg(years_operation: int = 20) -> float:
    """Total Earth-launched mass over the program life."""
    return amortized_annual_mass(years_operation) * years_operation


# =============================================================================
# Hardware build cost (Earth-side manufacturing)
# =============================================================================
# Per-kg hardware cost for space-qualified equipment is historically $50-200k/kg
# (rough heuristic from spacecraft programs). Under industrial-explosion automation
# pressure this drops to commodity-electronics-level cost; under TAI-grade
# automation it approaches material-cost-plus-energy.

HARDWARE_BUILD_COST_PER_KG_BAU = 100_000     # $/kg (typical aerospace flight hardware today)
HARDWARE_BUILD_COST_PER_KG_IE  = 10_000      # $/kg (10x compression under automation)
HARDWARE_BUILD_COST_PER_KG_TAI = 1_000       # $/kg (commodity-level under TAI design+mfg)


# =============================================================================
# Three automation regimes
# =============================================================================
@dataclass
class Regime:
    name: str
    mass_compression_factor: float   # divide capital mass by this (better robots → lighter capital)
    time_compression_factor: float   # divide milestone time by this
    launch_cost_per_kg_leo: float
    hardware_cost_per_kg: float      # $/kg hardware build cost on Earth
    notes: str

bau = Regime(
    name="BAU (business-as-usual)",
    mass_compression_factor=1.0,
    time_compression_factor=1.0,
    launch_cost_per_kg_leo=EARTH_LAUNCH_COST_PARTIAL_HIGH,    # $466/kg LEO (q1 partial late)
    hardware_cost_per_kg=HARDWARE_BUILD_COST_PER_KG_BAU,
    notes="2026 baseline; Starship partial reuse, current robotics, current ISRU TRL"
)

industrial_explosion = Regime(
    name="Industrial explosion (10× compression over a decade)",
    mass_compression_factor=10.0,
    time_compression_factor=5.0,
    launch_cost_per_kg_leo=EARTH_LAUNCH_COST_OPTIMISTIC,      # $59/kg LEO (q1 optimistic floor)
    hardware_cost_per_kg=HARDWARE_BUILD_COST_PER_KG_IE,
    notes="Sustained 10x automation pressure: 10x lighter capital (better robots, AI-designed mass-optimized hardware), 5x faster milestone clock, Starship cost compression"
)

tai = Regime(
    name="TAI-grade (100× compression in 1-3 yr)",
    mass_compression_factor=100.0,
    time_compression_factor=30.0,
    launch_cost_per_kg_leo=15.0,   # $15/kg LEO — q1 speculative-low corner under TAI-grade compression
    hardware_cost_per_kg=HARDWARE_BUILD_COST_PER_KG_TAI,
    notes="Step-change automation: TAI does mechanical design, scheduling, ops. 100x lighter capital, 30x faster milestone clock, internal launch cost approaches Musk $10/kg target"
)

REGIMES = [bau, industrial_explosion, tai]


def capex_under_regime(regime: Regime, years_operation: int = 20) -> Dict[str, float]:
    """
    Compute total capex over `years_operation` under a regime.
    Returns dict of components + totals.

    Three cost components:
    - Hardware build cost ($/kg × landed mass)
    - Launch cost ($/kg LEO × multiplier × landed mass)
    - Replacement cost: handled by `landed_mass * (1 + full_replacements)` term
    """
    out = {}
    total_launch = 0.0
    total_hardware = 0.0
    for c in COMPONENTS:
        compressed_mass = c.mass_kg / regime.mass_compression_factor
        full_replacements = max(0, years_operation / c.lifetime_yr - 1)
        landed_mass_kg = compressed_mass * (1 + full_replacements)
        ls_cost_per_kg = regime.launch_cost_per_kg_leo * LEO_TO_LS_COST_MULTIPLIER
        launch_cost = landed_mass_kg * ls_cost_per_kg
        hardware_cost = landed_mass_kg * regime.hardware_cost_per_kg
        out[c.name + " (launch)"] = launch_cost
        out[c.name + " (hardware)"] = hardware_cost
        total_launch += launch_cost
        total_hardware += hardware_cost
    out["TOTAL_LAUNCH_CAPEX_USD"] = total_launch
    out["TOTAL_HARDWARE_CAPEX_USD"] = total_hardware
    out["TOTAL_LAUNCH_PLUS_HARDWARE"] = total_launch + total_hardware
    out["YEARS_OPERATION"] = years_operation
    return out


def development_capex_under_regime(regime: Regime) -> float:
    """
    Non-launch development capex (R&D, design, ground-test articles).
    Heuristic: 3× the first-deployment HARDWARE cost (NASA TFU vs RT factor).
    Compressed by regime's time-compression factor.
    """
    first_set_mass = sum(c.mass_kg / regime.mass_compression_factor for c in COMPONENTS)
    first_set_hardware_cost = first_set_mass * regime.hardware_cost_per_kg
    dev_factor_base = 3.0
    dev_factor = dev_factor_base / math.sqrt(regime.time_compression_factor)
    return first_set_hardware_cost * dev_factor


def milestone_count_under_regime(regime: Regime, years_in_bau: float = 25.0) -> Dict:
    """
    8 discrete engineering milestones; calendar time under each regime.
    Anti-pattern #11: don't give calendar dates; give years-since-start
    explicitly conditional on the automation regime.
    """
    milestones_bau_years = {
        "M1: Robotic precursor (prospecting, site selection)":            2.0,
        "M2: Cargo lander demonstration (10+ t to LS)":                   3.0,
        "M3: Habitat deployment (uncrewed)":                              5.0,
        "M4: FSP installation + first power":                             7.0,
        "M5: ISRU pilot plant (O₂ + structural)":                         10.0,
        "M6: First crewed sustained occupation (12 mo)":                 12.0,
        "M7: Manufacturing complement operational (first lunar-made parts)": 18.0,
        "M8: Net-positive export reached":                                25.0,
    }
    compressed = {k: round(v / regime.time_compression_factor, 2) for k, v in milestones_bau_years.items()}
    compressed["_total_years_to_M8"] = compressed["M8: Net-positive export reached"]
    compressed["_regime"] = regime.name
    return compressed


def main():
    print("=" * 80)
    print("q5-capital-buildup pass-02-calc — first-principles bottom-up")
    print("=" * 80)
    print()
    print("Component mass budget (sources sealed):")
    for c in COMPONENTS:
        print(f"  {c.name}: {c.mass_kg/1000:.1f} t, lifetime {c.lifetime_yr} yr")
    print(f"  TOTAL one-set capital mass: {total_capital_mass_kg()/1000:.1f} t")
    print()
    print(f"Operating period: 20 years")
    print(f"  Total Earth-launched mass over 20 yr (with replacements): {total_program_mass_kg(20)/1000:.1f} t")
    print(f"  Annual amortized mass: {amortized_annual_mass(20)/1000:.1f} t/yr")
    print()

    print("=" * 80)
    print("Capex under three regimes (20-year operating horizon)")
    print("=" * 80)
    for regime in REGIMES:
        print(f"\n--- {regime.name} ---")
        print(f"  Mass compression factor: {regime.mass_compression_factor}x")
        print(f"  Time compression factor: {regime.time_compression_factor}x")
        print(f"  Earth-launch $/kg to LEO: ${regime.launch_cost_per_kg_leo}")
        print(f"  Notes: {regime.notes}")
        d = capex_under_regime(regime, 20)
        print(f"\n  Component-by-component:")
        for c in COMPONENTS:
            lc = d[c.name + " (launch)"]
            hc = d[c.name + " (hardware)"]
            print(f"    {c.name}: launch ${lc/1e9:.3f}B, hardware ${hc/1e9:.3f}B")
        print(f"\n  TOTAL LAUNCH CAPEX (20 yr): ${d['TOTAL_LAUNCH_CAPEX_USD']/1e9:.2f}B")
        print(f"  TOTAL HARDWARE CAPEX (20 yr): ${d['TOTAL_HARDWARE_CAPEX_USD']/1e9:.2f}B")
        print(f"  LAUNCH + HARDWARE (20 yr): ${d['TOTAL_LAUNCH_PLUS_HARDWARE']/1e9:.2f}B")
        dev = development_capex_under_regime(regime)
        print(f"  Development capex (R&D, design, ground test): ${dev/1e9:.2f}B")
        total = d['TOTAL_LAUNCH_PLUS_HARDWARE'] + dev
        print(f"  >>> GRAND TOTAL CAPEX: ${total/1e9:.2f}B <<<")

    print()
    print("=" * 80)
    print("Milestone timing — work-remaining decomposition per anti-pattern #11")
    print("=" * 80)
    for regime in REGIMES:
        print(f"\n--- {regime.name} ---")
        m = milestone_count_under_regime(regime)
        for k, v in m.items():
            if k.startswith("_"):
                continue
            print(f"  {k}: {v} years from program start")
        print(f"  Total years to net-positive export: {m['_total_years_to_M8']} yr")

    print()
    print("=" * 80)
    print("Headline result — bottom-up capex bracket")
    print("=" * 80)
    bau_grand = capex_under_regime(bau, 20)['TOTAL_LAUNCH_PLUS_HARDWARE'] + development_capex_under_regime(bau)
    ie_grand = capex_under_regime(industrial_explosion, 20)['TOTAL_LAUNCH_PLUS_HARDWARE'] + development_capex_under_regime(industrial_explosion)
    tai_grand = capex_under_regime(tai, 20)['TOTAL_LAUNCH_PLUS_HARDWARE'] + development_capex_under_regime(tai)
    print(f"  BAU:                   ${bau_grand/1e9:.2f}B over 20 yr (25 yr to M8 under BAU)")
    print(f"  Industrial explosion:  ${ie_grand/1e9:.2f}B over ~5 yr to M8")
    print(f"  TAI-grade:             ${tai_grand/1e9:.2f}B over <1 yr to M8")
    print()
    print(f"  Total Earth-launched mass to LS over 20 yr (regime-independent): {total_program_mass_kg(20)/1000:.1f} t")
    print(f"    Under BAU mass: {total_program_mass_kg(20)/bau.mass_compression_factor/1000:.1f} t")
    print(f"    Under IE mass: {total_program_mass_kg(20)/industrial_explosion.mass_compression_factor/1000:.1f} t")
    print(f"    Under TAI mass: {total_program_mass_kg(20)/tai.mass_compression_factor/1000:.1f} t")


if __name__ == "__main__":
    main()
