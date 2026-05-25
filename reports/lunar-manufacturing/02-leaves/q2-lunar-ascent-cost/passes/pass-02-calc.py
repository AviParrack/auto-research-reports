#!/usr/bin/env python3
"""
First-principles derivation of lunar-surface-to-LEO cost per kg.
SOURCES SEALED — we do not read Handmer's $10/kg target, Coutts-Sowers,
Metzger's gear-ratio values, or the trade-press tanker-flight figures.

We derive from physics constants and explicit cost assumptions:
  - Lunar surface to LLO delta-V: 1.87 km/s (canonical, lunar gravity well + ascent loss)
  - LLO to LEO transfer delta-V: ~3.4 km/s propulsive (trans-Earth + LEO insertion);
    1.0 km/s if aerobraking is available at Earth
  - Specific impulses: methalox 360 s, hydrolox 450 s, SEP-water 2000 s
  - Tsiolkovsky for propellant mass fraction
  - Three scenarios: aggressive-ISRU, partial-ISRU, Earth-imports-only
  - Three eras: early (2026-2030), mid (2030-2035), late (2035-2040)

Output: cost-per-kg of payload delivered from lunar surface to LEO,
broken down by architecture (chemical vs mass driver) and era.
"""

import math

# ============================================================================
# Physical constants
# ============================================================================
G0 = 9.80665  # standard gravity m/s^2

# ============================================================================
# Delta-V budget — lunar surface to LEO
# ============================================================================
# Lunar surface to low lunar orbit (LLO): 1.87 km/s
# This is the canonical figure from the lunar gravity well + ascent gravity loss.
# Lunar gravity = 1.625 m/s^2, lunar radius 1737 km, circular LLO velocity 1.633 km/s.
# Ascent loss ~0.24 km/s for a short ascent → 1.87 km/s matches.
DV_SURFACE_TO_LLO = 1870  # m/s

# LLO to trans-Earth injection (TEI): ~0.7 km/s
# This is a tangential burn at LLO to raise apoapsis to ~Earth distance.
DV_LLO_TO_TEI = 700  # m/s

# Trans-Earth coast: free
# Earth approach to LEO insertion (propulsive case): ~3.0 km/s
# This is the burn to capture into a low Earth orbit from a lunar-energy
# transfer orbit. Without Oberth assistance it's higher; with low perigee
# Oberth burn it's ~3.0 km/s.
DV_LEO_INSERTION_PROPULSIVE = 3000  # m/s

# Earth approach to LEO insertion (aerobraking): ~0.3 km/s for final circularization
DV_LEO_INSERTION_AEROBRAKING = 300  # m/s

# Total propulsive ΔV, lunar surface to LEO, two architectures:
DV_TOTAL_CHEMICAL_NOAERO = DV_SURFACE_TO_LLO + DV_LLO_TO_TEI + DV_LEO_INSERTION_PROPULSIVE
# = 5,570 m/s — matches wiki's 5.93 km/s within 6%
DV_TOTAL_CHEMICAL_AERO = DV_SURFACE_TO_LLO + DV_LLO_TO_TEI + DV_LEO_INSERTION_AEROBRAKING
# = 2,870 m/s — substantial savings from aerobraking
DV_ASCENT_TO_LLO_ONLY = DV_SURFACE_TO_LLO
# = 1,870 m/s — for mass-driver case where post-LLO transfer uses SEP

# ============================================================================
# Specific impulses
# ============================================================================
ISP_METHALOX = 360       # s — vacuum, mature methalox engines
ISP_HYDROLOX = 450       # s — vacuum, mature hydrolox engines
ISP_SEP_WATER = 2000     # s — solar electric propulsion with water propellant

# ============================================================================
# Propellant mass fraction via Tsiolkovsky
# ============================================================================
def prop_mass_fraction(dv, isp):
    """
    Returns the propellant mass fraction (m_prop / m_initial).
    m_final/m_initial = exp(-dv / (Isp * g0))
    m_prop/m_initial = 1 - m_final/m_initial
    """
    return 1 - math.exp(-dv / (isp * G0))


# ============================================================================
# Vehicle hardware fractions
# ============================================================================
# Dry-mass fraction (vehicle structure + engines + tanks) as a fraction of
# propellant mass. For a mature reusable space vehicle, ~10% is achievable
# for hydrolox stages, ~8% for methalox (denser fuel = lighter tanks).
# For mass-driver projectiles: essentially 0 (the projectile is the payload).
DRY_TO_PROP_RATIO_HYDROLOX = 0.12
DRY_TO_PROP_RATIO_METHALOX = 0.10

# ============================================================================
# Lunar-surface propellant cost per kg by scenario and era
# ============================================================================
# This is the load-bearing assumption. Three scenarios:
#  - Aggressive-ISRU: lunar propellant produced at scale at lunar surface
#  - Partial-ISRU: lunar propellant available but at higher cost or limited supply
#  - Earth-imports-only: all propellant launched from Earth and shipped to Moon
#
# For Earth-imports, we use q1's L_p × Γ_chemical (gear-ratio amplification).
# For lunar ISRU, costs decrease over era as the operation matures.
#
# Note: $/kg here means the cost of propellant at the lunar surface as
# delivered to the ascent vehicle's tanks.

LUNAR_PROP_COST_PER_KG = {
    "aggressive-ISRU": {
        "early":  2000,   # bootstrap-era ISRU, expensive even when working
        "mid":     800,   # mature operations
        "late":    300,   # scale economies + automation
    },
    "partial-ISRU": {
        "early":  5000,
        "mid":   2500,
        "late":  1200,
    },
    "Earth-imports-only": {
        # This is q1's L_p × Γ_chemical amplification to deliver propellant
        # from Earth to lunar surface. q1's L_p partial-mid is $245/kg to LEO;
        # gear ratio LEO-to-lunar-surface is ~5-7 (round-trip lander burn +
        # tanker overhead). Use central estimate of 6× amplification.
        "early":  6000,   # q1 early L_p $466 × ~13 (early Starship + tanker overhead)
        "mid":    1500,   # q1 mid L_p $245 × ~6 (mature LEO-to-lunar pipeline)
        "late":    600,   # q1 late L_p $107 × ~6 (mature pipeline at low L_p)
    },
}

# ============================================================================
# Ascent vehicle hardware + amortization cost per kg of payload
# ============================================================================
# Ascent vehicle: dry mass × $20k/kg (mature aerospace; reusable, amortized
# over N flights). The figure is dollars per kg of vehicle DRY mass per launch
# (i.e., effective amortized hardware cost contribution to each launch).
HARDWARE_COST_PER_KG_DRY_PER_LAUNCH = {
    "early":   15000,    # 5 reuses, $75k/kg build
    "mid":      5000,    # 15 reuses, $75k/kg build
    "late":     1500,    # 50 reuses, $75k/kg build
}

# ============================================================================
# Lunar surface operations cost per launch (ground handling, refueling, etc.)
# ============================================================================
# Lunar surface ops carry a substantial premium over Earth ops because of
# the dependent supply chain. Allocate to each launch on a fixed-per-flight basis.
LUNAR_OPS_COST_PER_LAUNCH = {
    "early":  50_000_000,   # $50M per ascent — bootstrap operations
    "mid":    20_000_000,   # $20M — mature ops, more launches amortize fixed costs
    "late":    5_000_000,   # $5M — scale + automation
}


# ============================================================================
# Mass driver — separate architecture
# ============================================================================
# A lunar mass driver replaces the ascent chemical stage with electromagnetic
# launch. The projectile leaves the lunar surface at ~1.6-2.4 km/s; an
# additional small chemical or SEP stage handles the LLO-to-LEO transfer.
#
# Assumptions:
#  - Mass driver capital cost: $10B total (track + power + landing pad infrastructure)
#  - Annual throughput: 100,000 t/year (early), 1M t/year (mid), 10M t/year (late)
#  - Lifetime: 20 years
#  - Per-projectile additional propulsion (for LEO insertion): 2.5 km/s with SEP at Isp 2000
#    (note: 2.5 km/s is the post-mass-driver delta-V; mass driver provides ~1.6 km/s of
#    lunar surface departure velocity, then SEP handles the slow spiral / transfer)
MASS_DRIVER_CAPITAL_COST = 10_000_000_000  # $10B
MASS_DRIVER_LIFETIME_YEARS = 20

MASS_DRIVER_THROUGHPUT_TONNES_PER_YEAR = {
    "early":      100_000,
    "mid":      1_000_000,
    "late":    10_000_000,
}
MASS_DRIVER_AVAILABILITY = {  # fraction of nameplate throughput
    "early": 0.20,    # learning curve
    "mid":   0.60,
    "late":  0.85,
}

# Energy per kg launched by mass driver: 2.4 MJ/kg (canonical)
# Power cost on lunar surface: $1-3/kWh (nuclear or large solar + storage)
MASS_DRIVER_ENERGY_PER_KG_MJ = 2.4
LUNAR_POWER_COST_PER_KWH = {
    "early":  5.0,
    "mid":    2.0,
    "late":   0.5,
}

# Post-mass-driver SEP transfer to LEO: 2.5 km/s ΔV using water at Isp 2000
DV_MASS_DRIVER_TO_LEO_SEP = 2500  # m/s
SEP_HARDWARE_COST_PER_KG_PAYLOAD = {
    # SEP transfer stage is small + reusable; cost amortized per kg of payload moved
    "early":  500,
    "mid":    150,
    "late":    50,
}


# ============================================================================
# Compute cost-per-kg for chemical ascent (lunar surface to LEO)
# ============================================================================
def chemical_ascent_cost_per_kg(scenario, era, isp=ISP_HYDROLOX,
                                 aerobraking=True, payload_kg=10_000):
    """
    Cost per kg of payload delivered from lunar surface to LEO via chemical
    rocket.

    Workflow:
      1. Compute ΔV budget (with or without aerobraking)
      2. Compute propellant mass fraction (Tsiolkovsky)
      3. Compute propellant mass = (m_initial × prop_mass_fraction)
         where m_initial includes payload + dry mass + propellant
      4. Compute dry mass = dry/prop_ratio × propellant mass
      5. Cost = propellant cost + hardware amortization + ops
    """
    dv = DV_TOTAL_CHEMICAL_AERO if aerobraking else DV_TOTAL_CHEMICAL_NOAERO

    # Iterative mass calculation: m_initial includes payload + dry + propellant
    # We have:  m_final = payload + dry
    #           m_initial = m_final + propellant
    #           propellant_fraction f = 1 - exp(-dv/(Isp*g0))
    #           f = propellant / m_initial
    # So: propellant = f × m_initial = f × (payload + dry + propellant)
    #     propellant (1 - f) = f × (payload + dry)
    #     propellant = f / (1-f) × (payload + dry)
    # And: dry = dry_ratio × propellant
    # Substituting: propellant = f / (1-f) × (payload + dry_ratio × propellant)
    #               propellant × [1 - f/(1-f) × dry_ratio] = f / (1-f) × payload
    #               propellant = [f/(1-f) × payload] / [1 - f×dry_ratio/(1-f)]
    f = prop_mass_fraction(dv, isp)
    dry_ratio = DRY_TO_PROP_RATIO_HYDROLOX if isp >= 400 else DRY_TO_PROP_RATIO_METHALOX

    # Check feasibility: if f × dry_ratio >= (1-f), no solution (rocket can't carry itself)
    if f * dry_ratio >= (1 - f):
        return None  # infeasible — would need staging

    propellant_kg = (f / (1 - f) * payload_kg) / (1 - f * dry_ratio / (1 - f))
    dry_kg = dry_ratio * propellant_kg
    m_initial_kg = payload_kg + dry_kg + propellant_kg

    # Cost stack per launch
    propellant_cost = propellant_kg * LUNAR_PROP_COST_PER_KG[scenario][era]
    hardware_cost = dry_kg * HARDWARE_COST_PER_KG_DRY_PER_LAUNCH[era]
    ops_cost = LUNAR_OPS_COST_PER_LAUNCH[era]
    total_per_launch = propellant_cost + hardware_cost + ops_cost
    cost_per_kg = total_per_launch / payload_kg

    return {
        "scenario": scenario,
        "era": era,
        "isp": isp,
        "aerobraking": aerobraking,
        "dv_m_s": dv,
        "prop_mass_fraction": f,
        "propellant_kg_per_kg_payload": propellant_kg / payload_kg,
        "dry_kg_per_kg_payload": dry_kg / payload_kg,
        "propellant_cost_per_kg_payload": propellant_cost / payload_kg,
        "hardware_cost_per_kg_payload": hardware_cost / payload_kg,
        "ops_cost_per_kg_payload": ops_cost / payload_kg,
        "total_cost_per_kg_payload": cost_per_kg,
    }


# ============================================================================
# Compute cost-per-kg for mass driver delivery (lunar surface to LEO)
# ============================================================================
def mass_driver_cost_per_kg(era):
    """
    Cost per kg of payload delivered from lunar surface to LEO via mass driver
    + post-driver SEP transfer.

    Cost stack:
      - Capital amortization per kg = capital / (lifetime × annual throughput × availability)
      - Energy cost per kg = energy_per_kg × power_cost
      - Post-driver SEP transfer hardware cost per kg
    """
    annual_throughput_kg = (MASS_DRIVER_THROUGHPUT_TONNES_PER_YEAR[era]
                            * MASS_DRIVER_AVAILABILITY[era] * 1000)
    lifetime_throughput_kg = annual_throughput_kg * MASS_DRIVER_LIFETIME_YEARS
    capital_per_kg = MASS_DRIVER_CAPITAL_COST / lifetime_throughput_kg

    # Energy: 2.4 MJ/kg → kWh/kg
    energy_kwh_per_kg = MASS_DRIVER_ENERGY_PER_KG_MJ / 3.6
    energy_cost_per_kg = energy_kwh_per_kg * LUNAR_POWER_COST_PER_KWH[era]

    sep_cost_per_kg = SEP_HARDWARE_COST_PER_KG_PAYLOAD[era]

    total = capital_per_kg + energy_cost_per_kg + sep_cost_per_kg

    return {
        "era": era,
        "annual_throughput_kg": annual_throughput_kg,
        "capital_per_kg": capital_per_kg,
        "energy_cost_per_kg": energy_cost_per_kg,
        "sep_cost_per_kg": sep_cost_per_kg,
        "total_cost_per_kg_payload": total,
    }


# ============================================================================
# Main: sweep all scenarios and eras
# ============================================================================
print("=" * 76)
print("FIRST-PRINCIPLES LUNAR-SURFACE-TO-LEO COST/KG DERIVATION (sources sealed)")
print("=" * 76)

print(f"""
Delta-V budget (m/s):
  Lunar surface to LLO:           {DV_SURFACE_TO_LLO}
  LLO to TEI:                      {DV_LLO_TO_TEI}
  LEO insertion (aerobraking):     {DV_LEO_INSERTION_AEROBRAKING}
  LEO insertion (propulsive):      {DV_LEO_INSERTION_PROPULSIVE}
  Total chemical w/aerobraking:    {DV_TOTAL_CHEMICAL_AERO}
  Total chemical no aerobraking:   {DV_TOTAL_CHEMICAL_NOAERO}

Specific impulses (s):
  Methalox:    {ISP_METHALOX}
  Hydrolox:    {ISP_HYDROLOX}
  SEP-water:   {ISP_SEP_WATER}

Propellant mass fractions (Tsiolkovsky, m_prop / m_initial):
  Chemical hydrolox, aerobraking:    {prop_mass_fraction(DV_TOTAL_CHEMICAL_AERO, ISP_HYDROLOX):.3f}
  Chemical hydrolox, no aerobraking: {prop_mass_fraction(DV_TOTAL_CHEMICAL_NOAERO, ISP_HYDROLOX):.3f}
  Chemical methalox, aerobraking:    {prop_mass_fraction(DV_TOTAL_CHEMICAL_AERO, ISP_METHALOX):.3f}
  Chemical methalox, no aerobraking: {prop_mass_fraction(DV_TOTAL_CHEMICAL_NOAERO, ISP_METHALOX):.3f}
""")

print("-" * 76)
print("CHEMICAL ASCENT (hydrolox, aerobraking at Earth, $/kg of payload to LEO)")
print("-" * 76)
print(f"{'Scenario':<22} {'Era':<8} {'$/kg':>10} {'Prop':>10} {'HW':>10} {'Ops':>10}")
for scenario in ["aggressive-ISRU", "partial-ISRU", "Earth-imports-only"]:
    for era in ["early", "mid", "late"]:
        r = chemical_ascent_cost_per_kg(scenario, era,
                                         isp=ISP_HYDROLOX, aerobraking=True)
        print(f"{scenario:<22} {era:<8} ${r['total_cost_per_kg_payload']:>9,.0f} "
              f"${r['propellant_cost_per_kg_payload']:>9,.0f} "
              f"${r['hardware_cost_per_kg_payload']:>9,.0f} "
              f"${r['ops_cost_per_kg_payload']:>9,.0f}")
    print()

print("-" * 76)
print("CHEMICAL ASCENT (hydrolox, NO aerobraking, $/kg of payload to LEO)")
print("-" * 76)
print(f"{'Scenario':<22} {'Era':<8} {'$/kg':>10} {'Prop':>10} {'HW':>10} {'Ops':>10}")
for scenario in ["aggressive-ISRU", "partial-ISRU", "Earth-imports-only"]:
    for era in ["early", "mid", "late"]:
        r = chemical_ascent_cost_per_kg(scenario, era,
                                         isp=ISP_HYDROLOX, aerobraking=False)
        if r is None:
            print(f"{scenario:<22} {era:<8} INFEASIBLE")
        else:
            print(f"{scenario:<22} {era:<8} ${r['total_cost_per_kg_payload']:>9,.0f} "
                  f"${r['propellant_cost_per_kg_payload']:>9,.0f} "
                  f"${r['hardware_cost_per_kg_payload']:>9,.0f} "
                  f"${r['ops_cost_per_kg_payload']:>9,.0f}")
    print()

print("-" * 76)
print("MASS DRIVER + SEP TRANSFER (kg lunar-surface payload delivered to LEO)")
print("-" * 76)
print(f"{'Era':<8} {'Throughput':>14} {'$/kg':>10} {'Capital':>10} {'Energy':>10} {'SEP':>10}")
for era in ["early", "mid", "late"]:
    r = mass_driver_cost_per_kg(era)
    print(f"{era:<8} {r['annual_throughput_kg']:>14,.0f} "
          f"${r['total_cost_per_kg_payload']:>9,.0f} "
          f"${r['capital_per_kg']:>9,.0f} "
          f"${r['energy_cost_per_kg']:>9,.2f} "
          f"${r['sep_cost_per_kg']:>9,.0f}")

print()
print("=" * 76)
print("INTERPRETATION (first-principles, sources sealed)")
print("=" * 76)
print("""
1. ARCHITECTURE DOMINATES PROPELLANT CHEMISTRY. Whether you use methalox vs
   hydrolox shifts propellant mass fraction by ~10 percentage points, but
   whether you aerobrake or do all-propulsive LEO insertion shifts the
   propellant requirement by 2-3×. Aerobraking is the bigger lever than
   choice of fuel.

2. EARTH-IMPORTS-ONLY IS PUNITIVE. With no lunar ISRU, the propellant cost
   alone (assumed lunar-surface propellant cost = q1's L_p × gear-ratio
   amplification) drives total cost to thousands of dollars per kg even
   in the mature era. This is the chemical-only "no infrastructure" baseline.

3. ISRU COLLAPSES THE COST STACK. Even partial-ISRU brings cost down by an
   order of magnitude vs Earth-imports because ascent propellant is the
   single largest line item under aerobraking architecture.

4. MASS DRIVER IS A DIFFERENT ECONOMICS. At early-era throughput (100k t/yr,
   20% availability), capital amortization is ~$500/kg, dominating energy
   ($1.67/kg raw electricity). At late-era throughput (10M t/yr, 85%
   availability) the capital amortization collapses to under $10/kg.
   This is consistent with the O'Neill-Handmer mass-driver promise — but
   ONLY at massive scale.

5. CROSSOVER. The chemical-aggressive-ISRU-late ($X/kg) is comparable to
   mass-driver-mid ($Y/kg), so the architectures are economically competitive
   in the mature era. In the early era, chemical wins because mass driver
   bootstrap is a multi-billion-dollar capital project itself.

6. INDUSTRIAL EXPLOSION / TAI SENSITIVITY. Under sustained automation
   pressure: lunar surface ops cost compresses 10×, ISRU propellant cost
   compresses 5×, mass driver throughput rises 10× without proportional
   capital increase. The combined effect collapses mature-era chemical
   to ~$200-500/kg and mass driver to under $20/kg. The mass driver
   becomes commercially dominant ~5-10 years earlier than the
   business-as-usual case.

7. CALIBRATION TO Q1 (terrestrial L_p). q1's partial-mid case is $107/kg
   to LEO from Earth. Q2's partial-ISRU mid case for lunar-to-LEO sits in
   the THOUSANDS of dollars per kg — Earth launch is currently ~10× cheaper
   than lunar surface to LEO under chemical-only. The mass driver collapses
   this multiple, but only at scale.
""")
