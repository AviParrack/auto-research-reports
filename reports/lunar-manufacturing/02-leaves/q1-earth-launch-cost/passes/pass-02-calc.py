#!/usr/bin/env python3
"""
First-principles derivation of Starship cost per kg to LEO over the operational
lifetime of the program (2026-2040). SOURCES SEALED — we do not use Musk's
claimed $10/kg target nor Citigroup's $100/kg forecast. We derive from:

  - Reported Starship hardware build cost (~$90M total stack, ~$45M booster
    + ~$45M ship — consistent across multiple SpaceX statements over 2024-2026)
  - Methalox propellant cost (~$1M per Starship launch; ~3,400t propellant @
    LOX $0.10/kg + LCH4 $0.50/kg gives ballpark figure)
  - Refurbishment cost per reuse cycle (Falcon 9 historical scaling)
  - Launch site amortization + ground ops
  - Vehicle reuse cycle count (the dominant scaling variable)

Output: a cost-per-kg model with explicit assumptions, swept across three
scenarios (Musk-optimistic / partial-reuse / operational-ceiling).
"""

# --------------------------------------------------------------------------
# Hardware costs
# --------------------------------------------------------------------------
# Build cost in $M, conservative end of public estimates
BOOSTER_BUILD_COST_M = 45  # $M
SHIP_BUILD_COST_M = 45     # $M
TOTAL_STACK_COST_M = BOOSTER_BUILD_COST_M + SHIP_BUILD_COST_M  # $90M

# Refurbishment cost as % of new-build cost (per reuse cycle).
# Falcon 9 historical: rose from ~40% in 2017 to ~10% by 2024 as processes matured.
# Starship at scale: assume similar trajectory.
REFURB_RATE = {
    "early":   0.30,  # 2026-2028 era, learning curve
    "mid":     0.15,  # 2028-2032, mature operations
    "late":    0.08,  # 2032+, scale economies
}

# --------------------------------------------------------------------------
# Propellant costs
# --------------------------------------------------------------------------
# Per Musk public statements: ~3,400t propellant per launch, mostly LOX.
# Methane: ~$0.50/kg industrial-scale (Henry Hub-linked + liquefaction)
# LOX: ~$0.10/kg industrial-scale (large-scale air separation)
LOX_KG = 2700          # kg, ~80% of propellant load (CH4-rich combustion gives this ratio)
LCH4_KG = 700
LOX_COST_PER_KG = 0.10
LCH4_COST_PER_KG = 0.50
PROPELLANT_COST_PER_LAUNCH = (LOX_KG * LOX_COST_PER_KG + LCH4_KG * LCH4_COST_PER_KG) * 1000
# = (2700 * 0.10 + 700 * 0.50) * 1000 = $620,000 — but Musk has stated $1M;
# probably includes margin + losses. Use $1M for conservatism.
PROPELLANT_COST_PER_LAUNCH = 1_000_000

# --------------------------------------------------------------------------
# Operations costs per launch
# --------------------------------------------------------------------------
# Per Falcon 9 historical: launch operations ~$2-5M per flight at maturity.
# Starship cadence target is higher → per-launch ops cost should be lower
# (more launches over same fixed infrastructure). Range: $0.5M to $2M.
OPS_COST_PER_LAUNCH_M = {
    "early":   2.0,
    "mid":     1.0,
    "late":    0.5,
}

# --------------------------------------------------------------------------
# Reuse cycles (the dominant variable)
# --------------------------------------------------------------------------
# Three scenarios:
#  - Optimistic: 100 reuses per stack (Musk target, comparable to aircraft cycles)
#  - Partial: 30 reuses (between Falcon 9's ~25 and aspirational)
#  - Pessimistic: 10 reuses (where Falcon 9 sits on average as of 2024)
REUSE_SCENARIOS = {
    "optimistic":   100,
    "partial":       30,
    "pessimistic":   10,
}

# --------------------------------------------------------------------------
# Payload capacity
# --------------------------------------------------------------------------
# Reusable payload to LEO. Block 2 Starship target: 150t. Conservative: 100t.
# Early Block 1: ~50t reported.
PAYLOAD_KG = {
    "optimistic":   150_000,  # 150t Block 2 reusable
    "partial":      100_000,  # 100t Block 2 derated
    "pessimistic":   50_000,  # Block 1 reusable
}

# --------------------------------------------------------------------------
# Compute cost per kg per scenario
# --------------------------------------------------------------------------

def cost_per_kg(reuses, payload_kg, era="mid"):
    """
    Total cost per launch / payload mass to LEO.

    Cost components per launch:
      = (hardware amortization) + propellant + refurbishment + operations
      = (TOTAL_STACK / N_reuses) + prop + (refurb_rate × TOTAL_STACK) + ops
    """
    hardware_amortized = (TOTAL_STACK_COST_M * 1_000_000) / reuses
    refurb_cost = REFURB_RATE[era] * (TOTAL_STACK_COST_M * 1_000_000)
    ops_cost = OPS_COST_PER_LAUNCH_M[era] * 1_000_000
    total_launch_cost = hardware_amortized + PROPELLANT_COST_PER_LAUNCH + refurb_cost + ops_cost
    return total_launch_cost / payload_kg


print("=" * 76)
print("FIRST-PRINCIPLES STARSHIP COST/kg DERIVATION (sources sealed)")
print("=" * 76)

print(f"""
Assumptions:
  Hardware build cost: ${TOTAL_STACK_COST_M}M per stack
  Propellant cost per launch: ${PROPELLANT_COST_PER_LAUNCH/1e6:.2f}M (methalox)
  Refurbishment rate: {REFURB_RATE['early']*100:.0f}% (early) / {REFURB_RATE['mid']*100:.0f}% (mid) / {REFURB_RATE['late']*100:.0f}% (late)
  Operations cost: ${OPS_COST_PER_LAUNCH_M['early']}M / ${OPS_COST_PER_LAUNCH_M['mid']}M / ${OPS_COST_PER_LAUNCH_M['late']}M per launch
""")

print(f"{'Scenario':<14} {'Reuses':>8} {'Payload':>10} {'Era':>8} {'$/kg':>10}")
print("-" * 60)
for scenario, reuses in REUSE_SCENARIOS.items():
    payload = PAYLOAD_KG[scenario]
    for era in ["early", "mid", "late"]:
        cpk = cost_per_kg(reuses, payload, era)
        print(f"{scenario:<14} {reuses:>8d} {payload:>10,d} {era:>8} ${cpk:>9.0f}")
    print()

print("=" * 76)
print("INTERPRETATION (first-principles, no Musk/Citigroup numbers)")
print("=" * 76)
print("""
1. THE DOMINANT VARIABLE IS REFURBISHMENT COST, not hardware amortization.
   At 30+ reuses, hardware amortization drops below $3M/launch ($30/kg on a
   100t payload). Refurbishment at 15% of build cost ($13.5M/launch) is 4-5x
   that. To get below $100/kg, refurbishment rate must reach <5% of build cost.

2. EVEN UNDER MUSK'S 100-REUSE TARGET WITH MATURE OPERATIONS (8% refurb,
   $0.5M ops, 150t payload), first-principles cost is ~$60/kg. This is
   *cost*, not list price. Margin and risk premium typically add 2-3x to
   reach customer price. So Musk's claimed $10/kg list price requires either
   (a) further compression of refurb to <2%, or (b) accepting near-zero
   margin for years to capture market share.

3. UNDER THE PARTIAL-REUSE SCENARIO (30 reuses, 100t, mid-era 15% refurb,
   $1M ops), first-principles cost is ~$175/kg. List price probably
   $400-600/kg after margin. This is the most defensible 2030-2035 central
   estimate.

4. UNDER THE PESSIMISTIC SCENARIO (10 reuses, 50t Block 1, early 30% refurb,
   $2M ops), first-principles cost is ~$700/kg. List price $1,500-2,000/kg.
   Effectively no improvement over Falcon 9 today.

5. INDUSTRIAL-EXPLOSION SENSITIVITY (modulo TAI): the levers under
   automation pressure are refurbishment time/labor (could collapse 10x
   with full robotic refurb), launch cadence (could rise 10x), and
   ground-ops cost (could collapse 5x). Combined: optimistic-scenario cost
   could drop another 3-5x to ~$15-25/kg. This still doesn't reach Musk's
   $10/kg without zero-margin pricing.

6. WHAT THE 2026 EVIDENCE SAYS: Falcon 9 list price is RISING ($500/kg/yr).
   Starship has not yet pulled list prices down. Until Starship operates at
   $/kg below Falcon 9's marginal cost (~$629/kg internal), the market
   pressure for list-price reduction is missing. The transition could be
   sudden once it happens.
""")
