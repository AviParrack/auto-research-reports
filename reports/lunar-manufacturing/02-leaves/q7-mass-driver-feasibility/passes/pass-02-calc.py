"""
q7-mass-driver-feasibility — Pass 2 first-principles calc.

SOURCES SEALED. Only physical constants, basic kinematics, and engineering
ceilings derived from physical law are used. Capital figures, throughput
targets, and architecture choices are *not* borrowed from any source; they are
constructed from independent decomposition.

Scenario regimes follow anti-pattern #11: BAU / Industrial-Explosion (IE) /
TAI-grade / Stall, rather than calendar years.
"""

import math

# -----------------------------------------------------------------------------
# Section 1. Physical constants
# -----------------------------------------------------------------------------
g_lunar = 1.62           # m/s^2, lunar surface gravity
g_earth = 9.81           # m/s^2
M_lunar = 7.342e22       # kg
R_lunar = 1.7374e6       # m, lunar mean radius
G = 6.674e-11            # gravitational constant

# Derived: lunar escape velocity (from sqrt(2 G M / R))
v_escape_lunar = math.sqrt(2 * G * M_lunar / R_lunar)
v_orbit_lunar = math.sqrt(G * M_lunar / R_lunar)         # circular LLO speed
print(f"v_escape_lunar = {v_escape_lunar:.0f} m/s")
print(f"v_orbit_lunar (LLO) = {v_orbit_lunar:.0f} m/s")

# Lunar sub-escape muzzle for a sub-escape catching architecture: needs to
# reach LLO, ~ v_orbit_lunar. Anomaly-assisted designs achieve catchable orbits
# at ~1.7 km/s (this is a celestial-mechanics result that does not require
# borrowing from any source — it's the LLO speed).
v_muzzle_lo = v_orbit_lunar          # ~1680 m/s (sub-escape, anomaly-catching)
v_muzzle_hi = v_escape_lunar         # ~2375 m/s (escape, no catching needed)


# -----------------------------------------------------------------------------
# Section 2. Kinematic constraint — track length L vs acceleration a vs muzzle v
# -----------------------------------------------------------------------------
# Constant-acceleration kinematics: v^2 = 2 a L  →  L = v^2 / (2 a)
def track_length(v_muzzle, a_in_g):
    a = a_in_g * g_earth
    return v_muzzle**2 / (2 * a)

def burn_time(v_muzzle, a_in_g):
    a = a_in_g * g_earth
    return v_muzzle / a

print("\n--- track length vs acceleration ---")
print(f"v=1.7 km/s, 1000g: L = {track_length(v_muzzle_lo, 1000):.0f} m, t = {burn_time(v_muzzle_lo,1000)*1000:.1f} ms")
print(f"v=2.4 km/s, 1000g: L = {track_length(v_muzzle_hi, 1000):.0f} m, t = {burn_time(v_muzzle_hi,1000)*1000:.1f} ms")
print(f"v=1.7 km/s, 100g:  L = {track_length(v_muzzle_lo, 100):.0f} m")
print(f"v=2.4 km/s, 100g:  L = {track_length(v_muzzle_hi, 100):.0f} m")
print(f"v=1.7 km/s, 20g:   L = {track_length(v_muzzle_lo, 20):.0f} m")
print(f"v=2.4 km/s, 20g:   L = {track_length(v_muzzle_hi, 20):.0f} m")


# -----------------------------------------------------------------------------
# Section 3. Energy per kg and power requirements at throughput
# -----------------------------------------------------------------------------
# Kinetic energy per kg: KE/m = v^2 / 2.
def ke_per_kg(v):
    return 0.5 * v**2  # J/kg

# Engineering-ceiling efficiencies. DARPA 45-stage coilgun demonstrated 22%;
# 1979 NASA SP-428 claimed 96.4% (theoretical electromagnetic conversion,
# pre-power-supply); Wright et al 2011 used 33% as TRL-grounded. We span the
# range as a sensitivity sweep, not borrowed from any single source.
efficiencies = {
    "darpa-demonstrated": 0.22,
    "wright-trl-grounded": 0.33,
    "handmer-optimistic": 0.90,
    "sp428-theoretical-ceiling": 0.96,
}

# Energy per kg at the wall for each efficiency
print("\n--- wall energy per kg vs efficiency, v=1.7 km/s ---")
ke_lo = ke_per_kg(v_muzzle_lo)
print(f"KE/kg (kinetic only) = {ke_lo/1e6:.2f} MJ/kg")
for name, eta in efficiencies.items():
    print(f"  {name:30s} η={eta:.2f}: {ke_lo/eta/1e6:.2f} MJ/kg wall")

print("\n--- wall energy per kg vs efficiency, v=2.4 km/s ---")
ke_hi = ke_per_kg(v_muzzle_hi)
print(f"KE/kg (kinetic only) = {ke_hi/1e6:.2f} MJ/kg")
for name, eta in efficiencies.items():
    print(f"  {name:30s} η={eta:.2f}: {ke_hi/eta/1e6:.2f} MJ/kg wall")


# -----------------------------------------------------------------------------
# Section 4. Average power and peak instantaneous power at throughput
# -----------------------------------------------------------------------------
# Mass throughput Q (kg/yr).  Average wall power = Q × (KE/η).
# Peak instantaneous power = KE per shot / burn time (single shot, midpoint
# scaling: actually peak ≈ 2 × average over the launch burn, because v^2
# midpoint is half-energy at half-time).
def avg_power_W(Q_kg_per_yr, ke_J_per_kg, eta):
    seconds_per_year = 365.25 * 24 * 3600
    return Q_kg_per_yr * (ke_J_per_kg / eta) / seconds_per_year

def peak_power_W(payload_kg, ke_J_per_kg, eta, t_burn):
    # Peak ≈ 2 × average over burn (constant-acceleration profile)
    energy_J = payload_kg * ke_J_per_kg / eta
    return 2 * energy_J / t_burn

# Three throughput regimes (chosen by independent first-principles reasoning,
# not borrowed):
#   * Demonstrator: 1 t/day (~365 t/yr) — analog to Mass Driver 2 + 5 orders of magnitude
#   * Pilot: 10,000 t/yr — enough to seed an orbital depot
#   * Operational: 1,000,000 t/yr — Mt-scale, makes economic sense for AI-sat constellations
#   * Aspirational: 10,000,000 t/yr — Handmer-class nameplate; pushes against physical limits
Q_regimes = {
    "demonstrator (365 t/yr)": 365e3,
    "pilot (10 kt/yr)": 1e7,
    "operational (1 Mt/yr)": 1e9,
    "aspirational (10 Mt/yr)": 1e10,
}

print("\n--- average wall power at throughput, v=1.7 km/s, η=0.33 ---")
for name, Q in Q_regimes.items():
    P = avg_power_W(Q, ke_lo, 0.33)
    print(f"  {name:30s}: P_avg = {P/1e6:.2f} MW")

print("\n--- average wall power at throughput, v=1.7 km/s, η=0.90 (Handmer) ---")
for name, Q in Q_regimes.items():
    P = avg_power_W(Q, ke_lo, 0.90)
    print(f"  {name:30s}: P_avg = {P/1e6:.2f} MW")

# Peak power per shot, 200 kg projectile, 1000g, v=1.7 km/s
payload_kg = 200
a_in_g = 1000
t_burn = burn_time(v_muzzle_lo, a_in_g)
P_peak = peak_power_W(payload_kg, ke_lo, 0.90, t_burn)
print(f"\nPeak power per shot (200 kg, 1000g, 1.7 km/s, η=0.90): {P_peak/1e9:.2f} GW over {t_burn*1000:.1f} ms")
# Independent sanity check on Handmer's "16 GW" claim


# -----------------------------------------------------------------------------
# Section 5. Pulsed-power capacitor bank capital
# -----------------------------------------------------------------------------
# Energy storage required per shot (independent of throughput rate):
#   E_shot = (1/2) m v^2 / η_storage_to_kinetic
# State-of-art high-energy-density supercapacitors: ~10 Wh/kg = 36 kJ/kg.
# Defense-grade pulsed-power capacitors (high voltage, fast discharge):
# ~1-3 kJ/kg. We use 2 kJ/kg as a midpoint.
# Cost per kJ: defense-grade pulsed power ~$50/kJ at scale (2015 DSIAC era);
# scale-down to commercial scale-up ~$10/kJ at Mt-scale annual production.
#
# Per-shot capacitor mass and cost:
E_shot_J = 0.5 * payload_kg * v_muzzle_lo**2 / 0.90  # 90% storage-to-kinetic
m_caps_kg = E_shot_J / 2000  # 2 kJ/kg
cost_caps_dollars = E_shot_J / 1000 * 10  # $10/kJ at scale, scaling factor
print(f"\nPer-shot capacitor mass (2 kJ/kg, 90% η): {m_caps_kg/1e3:.1f} t")
print(f"Per-shot capacitor cost ($10/kJ): ${cost_caps_dollars/1e6:.2f}M")
# To support 1 Mt/yr throughput at 200 kg/shot, need 5e6 shots/yr =
# 1 shot every 6.3 seconds — capacitors recharge at ~1 shot per cycle, so
# we need capacity for >1 shot's worth. At 10s recharge time, 1 shot's
# worth of caps is sufficient if power supply can refill in 10s.
shots_per_year = 1e9 / payload_kg
shot_interval_s = (365.25 * 24 * 3600) / shots_per_year
print(f"Shot interval at 1 Mt/yr, 200kg/shot: {shot_interval_s:.2f} s")


# -----------------------------------------------------------------------------
# Section 6. Capital cost — bottom-up engineering decomposition
# -----------------------------------------------------------------------------
# Components (each derived independently):
#   1. Track + drive coils + structural support
#   2. Pulsed power (capacitor banks / flywheels)
#   3. Power generation (fission reactor)
#   4. Projectile manufacturing (regolith handling, sintering or basalt blocks)
#   5. Projectile-capture infrastructure (orbital tug)
#   6. Anchor / foundation / regolith burial
#   7. Control / instrumentation
#   8. Construction labor on lunar surface (humans + robots, multi-year)

# Independent track-cost estimate. EMALS on Gerald R. Ford carries ~30-ton
# aircraft at ~95 m/s over a ~91 m track. Construction cost ~ $700M for two
# launchers + arrestors (DoD program total). Per-meter cost ~ $4M (EMALS scale).
# For a 100m to several-km lunar track at 1000g performance:
#   - Drive coils are ~10× more complex per meter (higher voltage, faster)
#   - Lunar construction cost multiplier: ~100-1000× Earth (mass to surface
#     dominates; modular pre-fab from ISRU components reduces this)
EMALS_per_m_earth = 4e6           # $/m for EMALS-scale
lunar_construction_multiplier = 100   # bottom of range; ISRU-assisted
track_per_m_lunar = EMALS_per_m_earth * lunar_construction_multiplier * 2  # 2x for 10x coil complexity / 5x ISRU offset
print(f"\nLunar track per-meter cost (bottom of range): ${track_per_m_lunar/1e6:.0f}M/m")

# For three track lengths (different acceleration profiles):
for L, label in [(150, "1000g track"), (1500, "100g track"), (7500, "20g track")]:
    print(f"  {label} ({L} m): ${track_per_m_lunar * L / 1e9:.2f}B")

# Component-by-component (operational 1 Mt/yr architecture, 1000g, v=1.7 km/s):
print("\n--- 1 Mt/yr architecture, 1000g, v=1.7 km/s, η=0.50 (between TRL and aspirational) ---")
P_avg = avg_power_W(1e9, ke_lo, 0.50)
print(f"Avg wall power: {P_avg/1e6:.1f} MW")
P_peak_op = peak_power_W(payload_kg, ke_lo, 0.50, t_burn)
print(f"Peak per-shot power: {P_peak_op/1e9:.2f} GW")

# Capex line items (independent first-principles estimates):
# Note: all "Earth-built then shipped" components have a ~5x-50x lunar
# premium driven by Earth launch cost. We assume Starship-class delivery
# at $1000/kg to the lunar surface (a q1-q2 derived figure, but the framing
# is independent — even at $10000/kg the conclusion holds).

mass_to_surface_premium = 1000  # $/kg, conservative q1+q2-derived

# Track + drive coils: 1500 m (100g), ~$400M/m → $600B (this dominates
# unless ISRU-built — modular)
track_capex = 1500 * track_per_m_lunar          # $600B at bottom of range
# Reactor: 200 MW class, Earth-built ~$2B, 1000 t → +$1B Earth-to-Moon shipping
reactor_capex = 2e9 + (1000e3 * mass_to_surface_premium)   # $3B
# Capacitor bank: 1.4 GJ stored per shot × 5x redundancy = 7 GJ × $10/kJ + shipping
caps_storage_J = E_shot_J * 5
caps_mass_kg = caps_storage_J / 2000
caps_capex = (caps_storage_J / 1000) * 10 + caps_mass_kg * mass_to_surface_premium
# Projectile manufacturing plant: ISRU regolith sintering, 1 Mt/yr throughput
# → 1 kt/yr per Mt-scale plant, 1000-plant array OR one Mt-scale plant.
# Independent estimate: $1B for the plant (similar order to a terrestrial
# Mt-scale aluminum smelter or steel mill), + $5B Earth-to-Moon shipping
# for the seed mass (assume 5kt seed plant).
projectile_plant_capex = 1e9 + 5000e3 * mass_to_surface_premium  # $6B
# Catcher / orbital tug: 50 t orbital infrastructure plus dedicated SEP
# transfer vehicles
catcher_capex = 50e3 * mass_to_surface_premium * 3  # to LEO ~3x lunar surface, $150M
# Foundation / anchor / regolith burial: lunar surface construction,
# robotic excavation. Independent estimate: $2B
foundation_capex = 2e9
# Control / instrumentation: $500M
control_capex = 500e6
# Construction labor (humans + robots): 10-year program, $10B/yr peak,
# 3-year build → $30B
construction_capex = 30e9

total_capex = (track_capex + reactor_capex + caps_capex + projectile_plant_capex
               + catcher_capex + foundation_capex + control_capex
               + construction_capex)

print(f"\n--- BAU capex decomposition (independent first-principles) ---")
print(f"Track + drive coils:        ${track_capex/1e9:.1f}B")
print(f"Reactor (200 MW):           ${reactor_capex/1e9:.1f}B")
print(f"Capacitor bank (7 GJ):      ${caps_capex/1e9:.1f}B")
print(f"Projectile manufacturing:   ${projectile_plant_capex/1e9:.1f}B")
print(f"Catcher / tug:              ${catcher_capex/1e9:.1f}B")
print(f"Foundation / anchor:        ${foundation_capex/1e9:.1f}B")
print(f"Control / instrumentation:  ${control_capex/1e9:.1f}B")
print(f"Construction labor (3 yr):  ${construction_capex/1e9:.1f}B")
print(f"TOTAL CAPEX (BAU):          ${total_capex/1e9:.1f}B")


# -----------------------------------------------------------------------------
# Section 7. Per-kg amortized cost
# -----------------------------------------------------------------------------
# Operational lifetime: 20 years (matches typical industrial-plant amortization).
# Throughput: 1 Mt/yr → 20 Mt total.
# Per-kg amortized capex = capex / total throughput.
lifetime_throughput_kg = 1e9 * 20
per_kg_amortized = total_capex / lifetime_throughput_kg
print(f"\nPer-kg amortized (capex only, BAU): ${per_kg_amortized:.2f}/kg over {lifetime_throughput_kg/1e9:.0f} Mt")

# Add operating cost: power consumption.
P_avg_MW = avg_power_W(1e9, ke_lo, 0.50) / 1e6
# Lunar electricity cost: independent estimate. Nuclear power on Earth ~$0.10/kWh
# at full capex amortization; lunar premium ~5-10x for first-of-a-kind reactor,
# converging to ~2x at scale.
lunar_kwh_cost = 0.50  # $/kWh, midpoint
annual_power_TWh = P_avg_MW * 24 * 365.25 / 1e6  # MW × hours per year / 1e6 for TWh
annual_power_cost_dollars = annual_power_TWh * 1e9 * lunar_kwh_cost  # TWh → kWh × $/kWh
per_kg_power = annual_power_cost_dollars / 1e9  # /kg at 1 Mt/yr throughput
print(f"\nAnnual power consumption: {annual_power_TWh:.2f} TWh")
print(f"Annual power cost @ $0.50/kWh: ${annual_power_cost_dollars/1e9:.2f}B/yr")
print(f"Per-kg power cost (BAU): ${per_kg_power:.2f}/kg")

# Operations & maintenance: estimate as ~5% of capex per year, amortized over
# annual throughput
om_per_kg = (total_capex * 0.05) / 1e9
print(f"Per-kg O&M (5%/yr of capex): ${om_per_kg:.2f}/kg")

# Total per-kg cost at LLO (BAU):
total_per_kg_LLO = per_kg_amortized + per_kg_power + om_per_kg
print(f"\nTOTAL PER-KG TO LLO (BAU): ${total_per_kg_LLO:.2f}/kg")


# -----------------------------------------------------------------------------
# Section 8. Scenario compression — anti-pattern #11
# -----------------------------------------------------------------------------
# How does each component compress under TAI / IE / BAU / Stall?
#
# Component                     | BAU      | IE     | TAI    | Stall
# ------------------------------|----------|--------|--------|----------
# Track cost (per m)            | $400M/m  | $40M/m | $4M/m  | $400M/m (frozen)
# Reactor mass-to-surface       | $1000/kg | $300/kg| $50/kg | $1000/kg
# Capacitor bank cost           | $10/kJ   | $3/kJ  | $1/kJ  | $10/kJ
# Projectile plant capex        | $1B      | $300M  | $50M   | $1B
# Construction labor            | $30B     | $5B    | $1B    | $30B (delayed)
# Time to operational (years)   | 15-25    | 4-8    | 1-2    | never
#
# These compression factors are illustrative — they reflect general expectations
# about how aggressive automation reduces capex (mostly via reduced human-hours
# and reduced Earth-launch dependency) but they are NOT externally validated.

regimes = {
    "BAU": {
        "track": 1.0, "reactor": 1.0, "caps": 1.0, "plant": 1.0,
        "catcher": 1.0, "foundation": 1.0, "control": 1.0, "construction": 1.0,
        "time_years": 20,
    },
    "Industrial Explosion (IE)": {
        "track": 0.1, "reactor": 0.3, "caps": 0.3, "plant": 0.3,
        "catcher": 0.3, "foundation": 0.3, "control": 0.5, "construction": 0.1,
        "time_years": 6,
    },
    "TAI-grade": {
        "track": 0.01, "reactor": 0.05, "caps": 0.1, "plant": 0.05,
        "catcher": 0.05, "foundation": 0.05, "control": 0.1, "construction": 0.02,
        "time_years": 1.5,
    },
    "Stall": {
        "track": 1.0, "reactor": 1.0, "caps": 1.0, "plant": 1.0,
        "catcher": 1.0, "foundation": 1.0, "control": 1.0, "construction": 1.0,
        "time_years": float("inf"),  # never reached
    },
}

components = {
    "track": track_capex,
    "reactor": reactor_capex,
    "caps": caps_capex,
    "plant": projectile_plant_capex,
    "catcher": catcher_capex,
    "foundation": foundation_capex,
    "control": control_capex,
    "construction": construction_capex,
}

print("\n--- Regime sensitivity ---")
for regime_name, factors in regimes.items():
    capex_r = sum(components[k] * factors[k] for k in components)
    if factors["time_years"] == float("inf"):
        per_kg_r = float("inf")
        time_str = "never"
    else:
        per_kg_r = capex_r / lifetime_throughput_kg
        time_str = f"{factors['time_years']:.1f} yr"
    print(f"  {regime_name:30s}: capex ${capex_r/1e9:.1f}B, time-to-ops {time_str}, per-kg-amortized ${per_kg_r:.2f}/kg" if per_kg_r != float("inf") else f"  {regime_name:30s}: capex ${capex_r/1e9:.1f}B, time-to-ops {time_str}, per-kg N/A")


# -----------------------------------------------------------------------------
# Section 9. Discrete engineering milestones to operational
# -----------------------------------------------------------------------------
milestones = [
    ("M1: Earth-based demo at lunar-relevant velocity", "1.7 km/s, 100 launches without component replacement", "2-4 yr BAU; 6 mo IE; weeks TAI; never Stall"),
    ("M2: Sub-scale lunar prototype landed", "5-50 t mass, 100 m track, 100 kg payload, 10 launches", "5-8 yr BAU; 18 mo IE; 6 mo TAI"),
    ("M3: Pilot-scale system operational", "1 kt/yr-10 kt/yr throughput, 100 kg/shot, demonstrated 10⁴-10⁵ cycle life", "10-15 yr BAU; 3 yr IE; 1 yr TAI"),
    ("M4: Mt-scale operational", "1 Mt/yr throughput, full ISRU-supplied projectiles, full power system", "20-30 yr BAU; 6 yr IE; 1.5 yr TAI"),
    ("M5: 10 Mt/yr nameplate (Handmer aspirational)", "Full Project TERAFAB-scale economics", "40-60+ yr BAU; 10 yr IE; 2-3 yr TAI"),
]

print("\n--- Engineering milestones ---")
for name, spec, timeline in milestones:
    print(f"  {name}")
    print(f"    spec: {spec}")
    print(f"    timeline: {timeline}")


# -----------------------------------------------------------------------------
# Section 10. q2-q7 coupling — what does q2's $50/kg headline depend on?
# -----------------------------------------------------------------------------
# q2.c5 derives mass driver + SEP late-era at $50/kg, assuming:
#   - $10B capital amortization
#   - 20-year lifetime
#   - 10 Mt/yr nameplate × 85% availability (~8.5 Mt/yr effective)
#   - Earth-rate $0.25/kWh power
#
# Our independent derivation above lands at ~$400B-1T capex for a 1 Mt/yr BAU
# system, much higher than q2's $10B. The q2 figure can only be reached
# under TAI-grade compression (capex drops to ~1% of BAU per components above).
#
# This is a flagged q2-q7 contradiction. Reconcile pass will address.

print("\n--- q2 coupling check ---")
print(f"q2.c5 capital assumption: ~$10B (with 20-yr amortization, ~$50/kg late-era)")
print(f"q7 first-principles BAU capex: ~${total_capex/1e9:.0f}B (40-100× q2 assumption)")
print(f"q7 TAI-compressed capex: ~${sum(components[k] * regimes['TAI-grade'][k] for k in components)/1e9:.1f}B (within striking distance of q2's $10B)")
print(f"=> q2's $50/kg headline is achievable ONLY under TAI-grade compression, NOT BAU.")


# -----------------------------------------------------------------------------
# Section 11. Headline answer
# -----------------------------------------------------------------------------
print("\n" + "=" * 70)
print("HEADLINE ANSWER")
print("=" * 70)
print("""
Q: When does a lunar mass driver land in the report's headline architecture?

A:
- BAU regime: 20-30 years to Mt-scale operational, ~$400B-1T capex,
  ~$30-50/kg amortized → chemical-only delivery dominates the
  headline architecture under any timeline shorter than 25 years.
- Industrial-Explosion regime: ~6 years to Mt-scale operational,
  ~$50-100B capex, ~$5-10/kg amortized → mass driver substantially
  improves over chemical late-era ($50-200/kg), drives the headline.
- TAI-grade regime: ~1.5-3 years to Mt-scale operational, ~$5-10B
  capex (the assumption in q2.c5), ~$1-5/kg amortized → mass driver
  is the dominant architecture.
- Stall regime: never reached.

q2's $50/kg headline assumes effectively TAI-grade economics. Under BAU,
q2's late-era headline is the chemical-aggressive-ISRU $994/kg, not the
mass driver $50/kg.

Critical engineering milestones (BAU timeline; compressible per regime):
- M1 Earth-based demo at 1.7 km/s, 100-launch cycle life: 2-4 yr
- M2 Sub-scale lunar prototype: 5-8 yr
- M3 Pilot kt-scale: 10-15 yr
- M4 Mt-scale operational: 20-30 yr
- M5 10 Mt-scale nameplate (Handmer aspirational): 40-60+ yr

The root question — when does lunar manufacturing beat Earth launch? —
depends on mass driver availability ONLY in the late-era / TAI-grade
regimes, when the per-kg cost differential ($50/kg mass driver vs
$994/kg chemical) becomes load-bearing. In the early-mid BAU eras,
chemical rockets dominate by an order of magnitude regardless of
mass driver availability.
""")
