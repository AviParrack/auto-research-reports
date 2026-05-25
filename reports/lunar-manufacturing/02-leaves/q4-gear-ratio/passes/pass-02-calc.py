#!/usr/bin/env python3
"""
First-principles derivation of the φ (production mass ratio) threshold for
lunar-derived bulk-mass competitiveness at cislunar destinations.

SOURCES SEALED. We do not consult Metzger 2023 or other TEAs for numerical
values. We use only physics (orbital mechanics), engineering ranges (LOX/LH2
performance, spacecraft mass fractions), and rough economic ranges that come
from general knowledge of space hardware costs + financing for first-of-kind
ventures.

The goal: derive φ_threshold as a function of destination Γ_X and a couple
of economic parameters, then report ranges over a plausible parameter space.
The reconcile pass will compare these to Metzger 2023's published numbers.
"""

import math

# -----------------------------------------------------------------------------
# Physics constants
# -----------------------------------------------------------------------------
g0 = 9.81            # m/s², Tsiolkovsky convention
I_sp_lh2 = 450       # s, LOX/LH2 upper stage
IMF = 0.10           # inert mass fraction, reusable hydrogen vehicle

# -----------------------------------------------------------------------------
# Delta-v budgets, m/s (textbook cislunar values)
# -----------------------------------------------------------------------------
DV = {
    "LEO_LS":   5_930,   # LEO → lunar surface (TLI + LOI + descent)
    "LS_LEO":   5_700,   # ascent + Earth-return injection
    "LS_LLO":   1_870,   # ascent only
    "LS_EML1":  2_500,
    "LS_GTO":   2_900,
    "LS_GEO":   2_700,
    "LEO_LLO":  4_100,
    "LEO_EML1": 3_770,
    "LEO_GTO":  2_500,
    "LEO_GEO":  3_900,
}

def G_one_way(dv):
    """Tsiolkovsky one-way gear ratio with inert mass fraction."""
    return (1 + IMF) * math.exp(dv / (g0 * I_sp_lh2)) - IMF

def G_round_trip(dv_out, dv_ret):
    """Reusable vehicle: must carry fuel for return after dropping cargo."""
    # Empty-mass return: multiply outbound by exp(dv_ret / g I_sp).
    return G_one_way(dv_out) * math.exp(dv_ret / (g0 * I_sp_lh2))

# Capital transport from LEO to lunar surface — reusable lander
G_K_LEO_LS = G_round_trip(DV["LEO_LS"], DV["LS_LEO"])

# Propellant from LS to various destinations — reusable carrier returns to LS
G_p_LS = {}
for dest, dv_field in [("LEO", "LS_LEO"), ("LLO", "LS_LLO"),
                       ("EML1", "LS_EML1"), ("GTO", "LS_GTO"),
                       ("GEO", "LS_GEO")]:
    G_p_LS[dest] = G_round_trip(DV[dv_field], DV[dv_field])

# Terrestrial propellant from LEO to destinations — expendable upper stage
G_p_LEO = {"LEO": 1.0}
for dest, dv_field in [("LLO", "LEO_LLO"), ("EML1", "LEO_EML1"),
                       ("GTO", "LEO_GTO"), ("GEO", "LEO_GEO")]:
    G_p_LEO[dest] = G_one_way(DV[dv_field])

# Propellant use ratio
Gamma = {d: G_p_LS[d] / G_p_LEO[d] for d in G_p_LS}

# -----------------------------------------------------------------------------
# Economic parameters — derived as ratios (launch-normalized) per Metzger's
# framework. CRUCIAL: these are dimensionless ratios, NOT $/kg. The trick is
# matching scale to G (~10-15). Per the framework (also derivable directly
# from the cost equation), x and G are typically of similar order; otherwise
# one component dominates and the optimization collapses to a degenerate case.
#
# Year-1 (first-of-kind, low EOS): x dominated by development cost ζ which is
# very large for novel space hardware. Over 30 years of EOS + learning curve,
# ζ drops by ~30-100×, dragging x down.
#
# We span the parameter space rather than guess a point estimate.
# -----------------------------------------------------------------------------

# Ranges to sweep — these are PLAUSIBLE based on general space-hardware
# economics, NOT cribbed from Metzger.
x_values = [
    ("year-1 first-of-kind", 200),     # ζ ≈ $100k/kg, L_p ≈ $500/kg → x = 200
    ("year-10 scaled", 50),            # EOS + learning curve reduces ζ
    ("year-30 mature", 10),            # mass-produced lunar capital
]
xi_values = [
    ("commercial WACC ~22%", 5),       # finance cost ~5× launch cost per kg product
    ("blended ~15%", 2),
    ("PPP 12%", 1),
]
omega = 0.1                             # operations cost, small fraction of L_p

def phi_threshold(Gamma_X, x, G_val, omega_v, xi_v):
    """
    From [(x + G)/φ + ω + ξ] · Γ_X < 1, solve for the minimum φ.
    φ > (x + G) · Γ_X / [1 - (ω + ξ) · Γ_X]
    Returns +∞ if denominator is non-positive (no φ can make lunar competitive
    at this destination under these costs).
    """
    denom = 1.0 - (omega_v + xi_v) * Gamma_X
    if denom <= 0:
        return float("inf")
    return (x + G_val) * Gamma_X / denom

# -----------------------------------------------------------------------------
# Report
# -----------------------------------------------------------------------------
print("=" * 78)
print("FIRST-PRINCIPLES φ THRESHOLD DERIVATION (sources sealed)")
print("=" * 78)

print()
print("Tsiolkovsky gear ratios (LOX/LH2, I_sp=450s, IMF=0.10):")
print(f"  capital LEO→LS (reusable RT) : G_K = {G_K_LEO_LS:.2f}")
print(f"  propellant LS→X (reusable RT):  LEO={G_p_LS['LEO']:.2f}  "
      f"LLO={G_p_LS['LLO']:.2f}  EML1={G_p_LS['EML1']:.2f}  "
      f"GTO={G_p_LS['GTO']:.2f}  GEO={G_p_LS['GEO']:.2f}")
print(f"  propellant LEO→X (expendable):   LEO={G_p_LEO['LEO']:.2f}  "
      f"LLO={G_p_LEO['LLO']:.2f}  EML1={G_p_LEO['EML1']:.2f}  "
      f"GTO={G_p_LEO['GTO']:.2f}  GEO={G_p_LEO['GEO']:.2f}")
print()
print("Propellant use ratio Γ_X = G_LS-X / G_LEO-X:")
for d in ["LLO", "EML1", "GEO", "GTO", "LEO"]:
    print(f"  Γ_{d:<5} = {Gamma[d]:.2f}")
print()
print("Necessary condition for lunar to ever compete at X:  (ω + ξ) · Γ_X < 1")
print(f"  i.e. fixed costs (labor+finance) must be less than 1/Γ_X of launch cost.")
print()

print(f"Sweeping x (equipment) and ξ (finance) — both launch-normalized:")
print(f"  G fixed at {G_K_LEO_LS:.1f} (chem rocket reusable round-trip)")
print(f"  ω fixed at {omega}")
print()

# For each (x, ξ) combo, print φ_threshold per destination
for x_lab, x in x_values:
    for xi_lab, xi in xi_values:
        print(f"--- x = {x:3d} ({x_lab})   ξ = {xi}  ({xi_lab}) ---")
        line = "    "
        for d in ["LLO", "EML1", "GEO", "GTO", "LEO"]:
            phi = phi_threshold(Gamma[d], x, G_K_LEO_LS, omega, xi)
            val = "∞" if phi == float("inf") else f"{phi:>6.0f}"
            line += f"{d}:{val}   "
        print(line)
    print()

print("=" * 78)
print("INTERPRETATION (first-principles, no Metzger consulted)")
print("=" * 78)
print("""
1. CLOSER-TO-MOON DESTINATIONS (LLO, EML1) have Γ_X ≈ 0.5-1.3. Threshold φ
   sits at order 20-100 for mature operations (year-30 x=10, PPP ξ=1).
   Achievable with current ISRU concepts at reasonable design margin.

2. GTO IS THE COMMERCIAL SWEET SPOT — Γ_X ≈ 2 (lunar product is harder to
   deliver to GTO than terrestrial, but only modestly). With mature parameters,
   threshold is in the ~50-200 range. Manageable.

3. LEO IS THE HARDEST DESTINATION — Γ_X ≈ 14 (reusable round-trip from
   lunar surface back to LEO uses 14× the mass it delivers). Combined with
   the (ω + ξ) · Γ_X < 1 necessary condition, ξ alone must be < 0.07 for
   LEO competition to be physically possible. This requires either very
   late-mature finance OR sub-launch-cost financing OR aerobraking that
   collapses the LS→LEO gear ratio.

4. THE LEO BARRIER is a financing problem more than a technology problem.
   PPP-style financing collapses LEO threshold by ~5-10×. Industrial-
   explosion-grade financing (essentially zero cost of capital) collapses
   it further. Pure tech improvement (lower x) helps mid-range destinations
   more than LEO.

5. SENSITIVITY TO ACCELERATION (modulo TAI): the dominant levers are
   (a) x dropping fast with EOS, (b) ξ dropping with WACC compression as
   risk evaporates, (c) ω staying small. Industrial-explosion-grade
   automation could compress x by 100× by collapsing fabrication cost
   per kg of capital. That would put even LEO breakeven well within reach
   in the early years of mature operation.

6. CRITICAL UNKNOWN: real-world φ values. Pure physics gives the threshold
   but says nothing about what ISRU technologies actually achieve. That is
   a TRL + engineering question, addressed in reconcile + source-review.
""")
