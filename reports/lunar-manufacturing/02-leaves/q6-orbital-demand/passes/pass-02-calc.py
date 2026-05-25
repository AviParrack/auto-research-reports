"""
q6 calc — sources sealed.

First-principles demand decomposition for cislunar / LEO 2026-2040 by use case:
  1. Space-based data centers (SDC) — AI compute → orbital mass
  2. Space-based solar power (SBSP) — kg/kW × GW deployed
  3. Orbital propellant depots — ship cadence × propellant per ship
  4. Lunar/Mars deep-space missions — cargo cadence × payload per ship
  5. Satellite servicing & debris mitigation — per-payload mass

Three acceleration regimes bracket each estimate: TAI-C, BAU, stall.
Per anti-pattern #11, calendar dates are conditional — use as scenarios
not predictions.

No source extracts consulted — pass 3 (reconcile) compares.
"""

import math


# ============================================================
# Module 1 — Space-based data centers
# ============================================================

def sdc_mass_demand(gw_deployed_by_2040: float, mass_per_mw_t: float = 40.0):
    """
    Mass demand for orbital data centers.

    Args:
      gw_deployed_by_2040: aggregate GW capacity in orbit by 2040
      mass_per_mw_t: tonnes of orbital infrastructure per MW of compute
        capacity, including compute hardware, solar panels, radiators,
        structure, station-keeping propellant tanks. First-principles
        decomposition: 20 t compute + 8 t solar + 8 t radiators + 4 t
        structure = 40 t/MW (mid). Range 30-50 t/MW from independent
        engineering analyses.

    Returns:
      total mass (t) and per-year rate over 15 years.
    """
    total_t = gw_deployed_by_2040 * 1000.0 * mass_per_mw_t  # GW→MW→t
    annual_avg_t = total_t / 15.0  # 2026-2040 ≈ 15 years
    return total_t, annual_avg_t


# Per-MW mass breakdown (first-principles):
#  Compute hardware: 20 t (GPUs + memory + interconnects + rack at GPU
#    density ~50 GPU/m² with ~1 kW/GPU thermal envelope; ~10 GPU/kW; thus
#    ~10 kg/kW server hardware including racks and PSU at server-grade)
#  Solar panels: 8 t (1 MW continuous in LEO requires ~3 MW peak panel;
#    state of art ~6 kg/kW peak panel, ~5 kg/kW for advanced)
#  Radiators: 8 t (100-200 m² per 100 kW; deployable structures at
#    ~5 kg/m² → 5,000-10,000 kg per MW; midpoint 7-8 t)
#  Structure + station-keeping: 4 t (booms, attitude control,
#    propellant tanks for drag compensation)
#  Total: 40 t/MW central; range 30-50 t/MW

# Three regimes for GW-deployed-by-2040:
SDC_REGIMES = {
    "stall": {
        "gw_by_2040": 0.5,  # ~10 demonstration satellites at 50 MW each
        "rationale": "Starcloud + Axiom + Kepler operational; no scaling. "
                     "Niche-only deployment per Cote/peraspera lower bound.",
    },
    "bau": {
        "gw_by_2040": 50.0,  # ~5% of US data center growth captured
        "rationale": "Modest hyperscaler adoption; orbit captures a few "
                     "percent of new build. Aligned with luminix 30-40% "
                     "viability by 2032-35 partially materializing.",
    },
    "tai_c": {
        "gw_by_2040": 1000.0,  # ~50% of projected US AI demand
        "rationale": "SpaceX/xAI 1M-satellite 100 GW filing scaled by 10× "
                     "via TAI-grade compression. Marcy 100 GW US demand "
                     "fully orbital captured. Industrial-explosion regime.",
    },
}


# ============================================================
# Module 2 — Space-based solar power
# ============================================================

def sbsp_mass_demand(gw_deployed_by_2040: float, kg_per_kw: float = 5.0):
    """
    Mass demand for SBSP satellites.

    Args:
      gw_deployed_by_2040: aggregate GW capacity in orbit by 2040
      kg_per_kw: mass intensity. Mankins SPS-ALPHA target ~1 kg/kW with
        mass-production scaling. State-of-art (2015) was 6.7 kg/kW.
        Mid-line estimate 5 kg/kW for 2030s deployment if SPS-ALPHA-class
        modular advances materialize but mass-production scaling is
        incomplete.

    Returns:
      total mass (t) and annual rate.
    """
    total_t = gw_deployed_by_2040 * 1e6 * kg_per_kw / 1000.0  # GW→kW→kg→t
    annual_avg_t = total_t / 15.0
    return total_t, annual_avg_t


SBSP_REGIMES = {
    "stall": {
        "gw_by_2040": 0.0,  # Demonstrations only, no operational scale
        "rationale": "No operational SBSP. Caltech SSPD-1 type "
                     "demos only. NASA OTPS conditions not met.",
    },
    "bau": {
        "gw_by_2040": 5.0,  # 1-2 operational GEO stations + China 1 km array
        "rationale": "China's 2028 1 km array + 1-2 commercial GEO stations "
                     "(Aetherflux Q1 2027 demos scaling to ~GW class by "
                     "late-2030s). Orbysa Q1 2027 + Caltech / Aetherflux "
                     "US programs delivering operational.",
    },
    "tai_c": {
        "gw_by_2040": 100.0,  # Mankins SPS-ALPHA at scale + ESA SOLARIS
        "rationale": "Mass-produced modular SBSP becomes viable under "
                     "$100-200/kg launch + TAI-grade automation per NASA "
                     "OTPS. ESA SOLARIS first operational ~2040. China "
                     "scales beyond demo. 100 GW captures ~10% of US "
                     "marginal grid demand.",
    },
}


# ============================================================
# Module 3 — Orbital propellant depots
# ============================================================

def depot_propellant_demand(starship_cadence_per_year: float,
                             tankers_per_ship: float = 8.0,
                             tanker_payload_t: float = 100.0):
    """
    Annual depot propellant demand from cislunar / interplanetary
    refueling.

    Args:
      starship_cadence_per_year: number of interplanetary or HLS-class
        Starships requiring orbital refuel each year.
      tankers_per_ship: tanker flights per refuel (Musk 8; NASA 16;
        midpoint 12 for stable mid-estimate)
      tanker_payload_t: usable propellant delivered per tanker, after
        boiloff and orbital insertion losses (Wikipedia depot/Handmer
        analysis: ~100 t for current Starship tanker spec).

    Returns:
      annual propellant tonnage routed through depots.
    """
    return starship_cadence_per_year * tankers_per_ship * tanker_payload_t


DEPOT_REGIMES = {
    "stall": {
        "ships_per_year": 0,  # No depot architecture deployed
        "rationale": "No orbital refueling architecture. NASA Artemis "
                     "uses single-launch missions; no Starship HLS at "
                     "scale; no Mars architecture.",
    },
    "bau": {
        "ships_per_year": 10,  # ~Annual Artemis HLS + commercial GEO ferry
        "rationale": "Artemis V-X (one HLS/year) + few commercial GEO "
                     "refuel customers + occasional deep-space mission. "
                     "10 ships/yr × 8 tankers × 100 t = 8,000 t/yr.",
    },
    "tai_c": {
        "ships_per_year": 200,  # Mars cadence at 2033 Musk schedule
        "rationale": "Mars cadence at Musk's 2033 'up to 500 missions per "
                     "window' figure annualized (≈200/yr). Each requires "
                     "8 tankers. 200 × 8 × 100 = 160,000 t/yr at depot.",
    },
}


# ============================================================
# Module 4 — Lunar/Mars deep-space cargo
# ============================================================

# These are the *terminal* deep-space mass figures (lunar surface,
# Mars surface, Mars orbit). LEO propellant demand to support them is
# captured separately in DEPOT_REGIMES.

LUNAR_SURFACE_CARGO_REGIMES = {
    "stall": {
        "tons_per_year_by_2040": 0,  # No Artemis V; program slips out
        "rationale": "Artemis program slips; no operational surface "
                     "cargo flow.",
    },
    "bau": {
        "tons_per_year_by_2040": 30,  # Approx 1 lander × 30 t midpoint
        "rationale": "1-2 Starship HLS cargo per year (each ~100 t to "
                     "surface; only ~30 t actual delivered after BAU "
                     "schedule slip and partial utilization). NASA M2M "
                     "cargo lander 1.5 t × few flights + commercial.",
    },
    "tai_c": {
        "tons_per_year_by_2040": 500,  # Industrial buildup beginning
        "rationale": "5 Starship HLS cargo/year fully utilized. Lunar "
                     "industry buildup beginning. Matches Musk cadence "
                     "framework for 2033/35 window if compressed.",
    },
}

MARS_CARGO_REGIMES = {
    "stall": {
        "tons_per_year_avg_2026_2040": 0,
        "rationale": "No operational Mars cargo. Starship Mars demos "
                     "stay demos.",
    },
    "bau": {
        "tons_per_year_avg_2026_2040": 200,  # First crew cargo + early window 1
        "rationale": "First 2028/29 window with 5-20 ships × 75 t × "
                     "0.6 success rate / 26 month cadence ≈ 200 t/yr avg.",
    },
    "tai_c": {
        "tons_per_year_avg_2026_2040": 15000,  # Multi-window 100-500 ship cadence
        "rationale": "Musk envelope: 2030/31 window 100 ships × 150 t = "
                     "15,000 t per window; 2033 window 500 ships × 300 t = "
                     "150,000 t per window. Averaged over 2026-2040: "
                     "100-200 ships/window × ~150 t/ship / 26 months ≈ "
                     "15,000 t/yr.",
    },
}


# ============================================================
# Module 5 — Satellite servicing & debris mitigation
# ============================================================

# OSAM market is currency-denominated not mass-denominated; convert
# via assumption that servicing-mass per servicing-dollar is roughly
# constant across architecture choices.

SERVICING_REGIMES = {
    "stall": {
        "annual_mass_t": 50,  # Current ~$2-3B market × 25 kg/$M = 50 t/yr
        "rationale": "Current OSAM market scale. ADR + occasional "
                     "robotic servicing; not architecturally significant.",
    },
    "bau": {
        "annual_mass_t": 200,  # $5B market × 40 kg/$M; some refuel/assembly mass
        "rationale": "MarketsAndMarkets $5.1B by 2030; expanded refuel + "
                     "assembly contribute meaningful per-mission mass.",
    },
    "tai_c": {
        "annual_mass_t": 2000,  # Routine large-structure assembly at orbit
        "rationale": "Routine in-orbit assembly + ADR at SpaceX/Blue "
                     "Origin mega-constellation scale demands order of "
                     "magnitude more mass throughput.",
    },
}


# ============================================================
# Aggregator
# ============================================================

def aggregate_regime(regime: str):
    """Print all-use-case mass demand totals for a given regime."""
    print(f"\n===== REGIME: {regime.upper()} =====\n")

    # SDC
    sdc_total, sdc_annual = sdc_mass_demand(SDC_REGIMES[regime]["gw_by_2040"])
    print(f"  SDC: {SDC_REGIMES[regime]['gw_by_2040']:.0f} GW deployed by 2040")
    print(f"    Total mass to orbit: {sdc_total:,.0f} t")
    print(f"    Annual average:      {sdc_annual:,.0f} t/yr")

    # SBSP
    sbsp_total, sbsp_annual = sbsp_mass_demand(SBSP_REGIMES[regime]["gw_by_2040"])
    print(f"  SBSP: {SBSP_REGIMES[regime]['gw_by_2040']:.0f} GW deployed by 2040")
    print(f"    Total mass to orbit: {sbsp_total:,.0f} t")
    print(f"    Annual average:      {sbsp_annual:,.0f} t/yr")

    # Depots
    depot_annual = depot_propellant_demand(DEPOT_REGIMES[regime]["ships_per_year"])
    print(f"  Depots: {DEPOT_REGIMES[regime]['ships_per_year']:.0f} ships/yr refueled")
    print(f"    Annual propellant through LEO depots: {depot_annual:,.0f} t/yr")

    # Lunar surface
    lunar_annual = LUNAR_SURFACE_CARGO_REGIMES[regime]["tons_per_year_by_2040"]
    print(f"  Lunar cargo: {lunar_annual:,.0f} t/yr to surface by 2040")

    # Mars surface
    mars_annual = MARS_CARGO_REGIMES[regime]["tons_per_year_avg_2026_2040"]
    print(f"  Mars cargo: {mars_annual:,.0f} t/yr avg 2026-2040")

    # Servicing
    serv_annual = SERVICING_REGIMES[regime]["annual_mass_t"]
    print(f"  Servicing: {serv_annual:,.0f} t/yr")

    # Total LEO mass demand (excludes Mars surface since that mass
    # transits through LEO via depots already counted)
    total_leo_annual = (
        sdc_annual + sbsp_annual + depot_annual + lunar_annual + serv_annual
    )
    print(f"\n  >>> TOTAL LEO mass demand (annual avg): {total_leo_annual:,.0f} t/yr")
    print(f"  >>> TOTAL deep-space (Mars surface): {mars_annual:,.0f} t/yr extra")

    return total_leo_annual


if __name__ == "__main__":
    print("=" * 60)
    print("q6 orbital demand — first-principles decomposition")
    print("=" * 60)
    print()
    print("Assumptions sealed from sources. Three acceleration regimes:")
    print("  - stall: Apollo-drought analog, programs collapse")
    print("  - bau:   business-as-usual incremental progress")
    print("  - tai_c: TAI-compression / industrial explosion")
    print()
    print("Horizon: 2026-2040 (15 years).")

    for regime in ["stall", "bau", "tai_c"]:
        aggregate_regime(regime)

    # Sanity check: BAU's annual depot demand vs Kornuta-Metzger 450 t/yr.
    # Our 8,000 t/yr BAU figure is 18× Kornuta's near-term. Implicit
    # assumption: depot demand includes ALL LEO refueling including
    # Mars-bound Starships, not just lunar-derived propellant market.
    # Kornuta 450 t/yr was lunar-derived propellant market specifically.
    # Reconcile pass will clarify.
    print()
    print("=" * 60)
    print("Sanity checks")
    print("=" * 60)
    print()
    print("SBSP TAI-C 100 GW × 5 kg/kW = 500,000 t total over 15 yr")
    print("  → 33,000 t/yr SBSP alone. Equivalent to ~165 Starship-200t")
    print("    launches/year just for SBSP. Plausibility check:")
    print("    Mankins 80,000 t for 4 GW reference design at 20 kg/kW")
    print("    → 100 GW at 5 kg/kW = 500,000 t. Consistent.")
    print()
    print("Depot TAI-C 160,000 t/yr LEO propellant ÷ 100 t/Starship-tanker")
    print(f"  → {160000/100:.0f} tanker flights/year, ~{160000/100/365:.1f}/day.")
    print("  Plausibility: SpaceX target 1,000 ships/year production;")
    print("  this scenario uses ~1,600 tanker flights/year — broadly")
    print("  consistent with the industrial-explosion launch cadence.")
    print()
    print("SDC TAI-C 1,000 GW × 40 t/MW × 1000 MW/GW = 40,000,000 t")
    print("  → 40 Mt over 15 yr = 2.67 Mt/yr. This is at the architectural")
    print("    limit of any conceivable Earth launch program. Implies")
    print("    cheap orbital deployment requires in-space manufacturing")
    print("    (lunar-sourced structural mass) to be tractable.")
    print()
    print("This last sanity check IS the lunar-manufacturing thesis:")
    print("  under TAI-C, orbital demand exceeds plausible Earth-launch")
    print("  capacity, which is exactly the condition under which lunar")
    print("  manufacturing becomes the binding architecture.")
