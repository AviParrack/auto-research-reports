#!/usr/bin/env python3
"""
q3-isru-feasibility — Pass 2 calc (sources sealed).

First-principles materials × processes × TRL feasibility matrix.

We derive (a) which materials are extractable from lunar regolith,
(b) the thermodynamic energy floor for each route, (c) which inputs
must be imported from Earth in steady state, (d) the TRL decomposition
under TAI-compression vs stall regimes.

Sources sealed: this pass uses only physical chemistry, regolith
composition assumptions (loaded as canonical numbers from training
knowledge, not from any sources/ file), and TRL framework as the
NASA 1-9 ladder.

Outputs:
- Feasibility matrix as a table printed to stdout
- Energy budgets per (material, process) pair
- Earth-import accounting
- Acceleration-regime decomposition

No plots — the result is a categorical matrix, not a numerical
sensitivity sweep where a plot would clarify.
"""

from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------
# 1. Regolith composition (canonical first-principles assumptions)
# ---------------------------------------------------------------
#
# All composition figures are oxide weight percents. These are
# canonical Apollo-derived averages from training knowledge; we are
# NOT consulting Apollo sample compendia or the Lunar Sourcebook
# directly in this pass. Pass 3 will reconcile against measured
# values.

MARE_BASALT = {
    # weight percent of major oxide phases
    "SiO2":  45.0,   # silicate matrix
    "Al2O3": 12.0,   # plagioclase
    "FeO":   18.0,   # pyroxene + olivine + ilmenite
    "MgO":   10.0,   # olivine + pyroxene
    "CaO":   11.0,   # plagioclase + pyroxene
    "TiO2":   4.0,   # ilmenite-dominated (highly variable: 0.5-10)
    # ilmenite (FeTiO3) is ~52.6 wt% TiO2 — 4 wt% TiO2 implies ~7.5 wt%
    # ilmenite, which converts to ~6-8 vol% depending on density.
    # (Codex audit correction May 2026.)
    "ilmenite_vol_pct": 7.5,
}

HIGHLAND_ANORTHOSITE = {
    "SiO2":  45.5,
    "Al2O3": 21.0,
    "FeO":    6.0,
    "MgO":   10.0,
    "CaO":   14.5,
    "TiO2":   0.5,
    "ilmenite_vol_pct": 0.5,  # very low
}

POLAR_REGOLITH = {
    # Compositionally similar to highland anorthosite but with
    # 0.1-5 wt% water-equivalent volatiles (PSR shadowed craters)
    "SiO2":  45.0,
    "Al2O3": 20.0,
    "FeO":    7.0,
    "MgO":   10.0,
    "CaO":   14.0,
    "TiO2":   0.7,
    "ilmenite_vol_pct": 0.7,
    "H2O_volatile_wt_pct_range": (0.1, 5.0),  # uncertain
}


def regolith_oxygen_mass_fraction(comp: dict) -> float:
    """Fraction of regolith mass that is oxygen, from oxide phases.

    For each oxide we compute molar mass and the O fraction within it,
    then weight by mass percentage.
    """
    # Molar masses (g/mol)
    M = {"Si": 28.09, "Al": 26.98, "Fe": 55.85, "Mg": 24.31,
         "Ca": 40.08, "Ti": 47.87, "O": 16.00}
    oxide_o_frac = {
        "SiO2":  2 * M["O"] / (M["Si"]      + 2*M["O"]),
        "Al2O3": 3 * M["O"] / (2*M["Al"]    + 3*M["O"]),
        "FeO":   1 * M["O"] / (M["Fe"]      + M["O"]),
        "MgO":   1 * M["O"] / (M["Mg"]      + M["O"]),
        "CaO":   1 * M["O"] / (M["Ca"]      + M["O"]),
        "TiO2":  2 * M["O"] / (M["Ti"]      + 2*M["O"]),
    }
    total_o = 0.0
    for oxide, wt_pct in comp.items():
        if oxide in oxide_o_frac:
            total_o += (wt_pct / 100.0) * oxide_o_frac[oxide]
    return total_o


# ---------------------------------------------------------------
# 2. Thermodynamic energy floors
# ---------------------------------------------------------------
#
# Gibbs free energies of formation for the dominant oxides at 1600 K
# (close to MRE operating temperature 1600°C = 1873 K, but 1600 K
# adequate for order-of-magnitude work).
#
# ΔG_f values (kJ/mol of oxide) at ~1600 K, from standard
# thermodynamic tables (Ellingham diagram intercepts):
#   SiO2:   -700
#   Al2O3:  -1300 (per Al2O3)
#   FeO:    -180
#   MgO:    -500
#   CaO:    -550
#   TiO2:   -750
#
# Per kg of O2 produced (32 g/mol O2 → 31.25 mol O2 per kg), the
# thermodynamic minimum energy to liberate oxygen from oxide is
# |ΔG_f / n_O| × n_O2 × 2 (factor of 2 because n_O = 2 n_O2).
# We compute this for each oxide.

# Molar mass of O2 = 32 g/mol → 1 kg O2 = 31.25 mol O2

OXIDE_DGF_KJMOL = {  # at ~1600 K
    "SiO2":   700.0,   # |ΔG_f| per mole oxide
    "Al2O3": 1300.0,
    "FeO":    180.0,
    "MgO":    500.0,
    "CaO":    550.0,
    "TiO2":   750.0,
}
OXIDE_N_O = {  # moles of O per mole oxide
    "SiO2":  2, "Al2O3": 3, "FeO": 1, "MgO": 1, "CaO": 1, "TiO2": 2,
}


def thermo_floor_kwh_per_kg_o2(oxide: str) -> float:
    """Minimum energy (kWh) per kg O2 to dissociate oxide → metal + O.

    n_O2 per mole oxide = OXIDE_N_O[oxide] / 2
    Energy per mole O2 = ΔG_f / (n_O / 2) = 2 * ΔG_f / n_O
    Per kg O2 = (2 * ΔG_f / n_O) * 31.25 mol/kg / 3600 kJ/kWh
    """
    dgf = OXIDE_DGF_KJMOL[oxide]
    n_O = OXIDE_N_O[oxide]
    kj_per_mol_o2 = 2 * dgf / n_O
    kj_per_kg_o2 = kj_per_mol_o2 * 31.25
    return kj_per_kg_o2 / 3600.0


# ---------------------------------------------------------------
# 3. Process taxonomy
# ---------------------------------------------------------------

@dataclass
class Process:
    name: str
    feedstock_region: str         # "mare" | "highland" | "any" | "polar"
    feedstock_phase: str          # which mineral phase reacts
    operating_T_C: int
    products: list                # primary outputs
    earth_imports_steady_state: list  # consumables that must be imported
    energy_kwh_per_kg_o2_process: float  # process-only, excludes Carnot losses
    energy_kwh_per_kg_o2_wallplug: float  # incl. heating losses, ancillaries
    trl_now_2026: int
    trl_2030_compressed: int      # under TAI / sustained demonstration cadence
    trl_2030_stall: int           # 50-year-Apollo-style stall
    notes: str = ""

PROCESSES = [
    Process(
        name="Ilmenite H2 reduction",
        feedstock_region="mare",
        feedstock_phase="ilmenite (FeTiO3)",
        operating_T_C=1050,
        products=["O2 (via H2O electrolysis loop)", "Fe metal sponge", "TiO2 byproduct"],
        earth_imports_steady_state=[
            "H2 makeup (small — recycled via electrolysis; initial charge ~kg per kg/yr O2)",
        ],
        # Process energy: bond enthalpy of FeTiO3 + H2 reaction at 1050°C
        # is relatively favorable; dominated by sensible heat to 1050°C.
        # Ilmenite is ~31% O, but only Fe-O bond is broken (Ti stays as TiO2),
        # so effective n_O per mole ilmenite = 1, not 3.
        # Effective thermo floor for the FeO portion: ~1.0 kWh/kg O2.
        # Real process: 10-15 kWh/kg O2 due to thermal losses + electrolyzer.
        energy_kwh_per_kg_o2_process=2.5,
        energy_kwh_per_kg_o2_wallplug=15.0,
        trl_now_2026=5,
        trl_2030_compressed=8,    # compressed: lunar demo by 2028 + product flow
        trl_2030_stall=5,         # stall: never gets past current lab+sim demo
        notes="Highest-TRL O2 process. Mare-only. Low yield by mass (only ~0.5-2 wt% O2 per regolith due to low ilmenite vol pct), so requires high throughput. Co-produces Fe + TiO2 of structural interest.",
    ),
    Process(
        name="Carbothermal reduction",
        feedstock_region="any",
        feedstock_phase="silicate matrix (whole regolith)",
        operating_T_C=1700,
        products=["O2 (via CO + Sabatier loop)", "Si metal", "Fe metal"],
        earth_imports_steady_state=[
            "CH4 makeup (closed loop with Sabatier; small ongoing import)",
            "Reactor liner refractory replacements (long lead-time, low rate)",
        ],
        # Carbothermal: SiO2 + 2C → Si + 2CO; 2CO + 6H2 → 2CH4 + 2H2O
        # Effective energy: dominated by sensible heat to 1700°C + endothermic
        # reduction. Sierra Space demo: >20 g O2/kWh-thermal = 50 kWh/kg O2
        # thermal. Wall-plug for solar-concentrator: similar.
        energy_kwh_per_kg_o2_process=10.0,
        energy_kwh_per_kg_o2_wallplug=50.0,
        trl_now_2026=6,           # Sierra Space TRL-6 Sept 2024 demo
        trl_2030_compressed=8,    # CLPS lunar demo by 2028
        trl_2030_stall=6,         # stays at lab-vacuum-chamber level
        notes="Highest TRL for whole-regolith oxygen. Region-agnostic. Co-produces Si + Fe. Closed-loop carbon recovery via Sabatier means small Earth import once primed.",
    ),
    Process(
        name="Molten Regolith Electrolysis (MRE)",
        feedstock_region="any",
        feedstock_phase="silicate matrix (whole regolith, no beneficiation)",
        operating_T_C=1600,
        products=["O2", "Fe-Si alloy", "Al (if Ca/Al phases isolated)"],
        earth_imports_steady_state=[
            "Inert anode replacements (rare-earth oxide ceramics, low rate)",
            "Reactor structural refractory replacements (low rate)",
        ],
        # Process energy: thermo floor from FeO + SiO2 dissociation at 1600°C.
        # Schreiner-style models: 21 kWh/kg O2 process; 50-150 kWh/kg
        # wall-plug including thermal losses.
        # Sourced from physical chemistry: mean ΔG for FeO + SiO2 + Al2O3 +
        # MgO + CaO weighted by mass = ~6 kWh/kg O2 (floor); plus reactor
        # heating + Joule losses → ~50 kWh/kg wall-plug.
        energy_kwh_per_kg_o2_process=15.0,
        energy_kwh_per_kg_o2_wallplug=60.0,
        trl_now_2026=4,           # Sadoway lab; Helios; Lunar Resources
        trl_2030_compressed=7,    # CLPS demo + scaled prototype
        trl_2030_stall=4,         # never leaves the lab
        notes="No halide electrolyte (vs FFC). Inert anode is key advance. Whole-regolith input means no beneficiation losses. Critical for highland/polar where ilmenite is sparse.",
    ),
    Process(
        name="FFC Cambridge electrolysis",
        feedstock_region="any (best with sintered pellets)",
        feedstock_phase="any oxide pellet (anorthite for Al, ilmenite for Ti)",
        operating_T_C=900,
        products=["O2", "Ti / Al / Si / Fe / Ca (depending on feedstock)"],
        earth_imports_steady_state=[
            "Chlorine for CaCl2 makeup (Cl is trace on Moon; this is the structural bottleneck)",
            "Anode refractories",
        ],
        # Lower operating T than MRE; energy similar order of magnitude
        # because dominated by electrochemistry not heating.
        # Estimated 5-10 kWh/kg O2 process, 30-50 kWh/kg wall-plug.
        energy_kwh_per_kg_o2_process=8.0,
        energy_kwh_per_kg_o2_wallplug=40.0,
        trl_now_2026=4,           # Metalysis terrestrial Gen 4 cells (TRL 7+ for Earth);
                                  # lunar-config: TRL 3-4 (sintered simulant pellets only)
        trl_2030_compressed=6,    # if chlorine recycling problem solved
        trl_2030_stall=4,         # halide management remains a research problem
        notes="Lowest operating T → easier hardware. But CaCl2 bath is the structural import. Salt recycling determines lunar viability. Best route for direct Al + Ti metallurgy if Cl supply solved.",
    ),
    Process(
        name="Vapor-phase pyrolysis (solar-thermal)",
        feedstock_region="any",
        feedstock_phase="silicate matrix",
        operating_T_C=2500,
        products=["O2", "metal vapors (Fe, Si, Mg) — condensed separately"],
        earth_imports_steady_state=[
            "Optical surfaces (mirrors/lenses) replacement (low rate)",
        ],
        # High T means high thermo cost but no electrolyzer.
        # Direct dissociation of SiO2 vapor → Si + O at >2000°C.
        # Theoretical floor: ~10 kWh/kg O2. Practical with concentrator
        # losses: 100-200 kWh/kg.
        energy_kwh_per_kg_o2_process=20.0,
        energy_kwh_per_kg_o2_wallplug=150.0,
        trl_now_2026=3,           # lab-scale only
        trl_2030_compressed=5,    # if Sierra-class concentrator hardware reaches Moon
        trl_2030_stall=3,
        notes="No consumables, no electrolytes. But energy-intensive and metal vapors hard to separate cleanly.",
    ),
    Process(
        name="Polar ice extraction + electrolysis",
        feedstock_region="polar (PSR craters)",
        feedstock_phase="H2O ice in shadowed regolith",
        operating_T_C=200,         # below ice sublimation point with vacuum
        products=["O2", "H2 (the only lunar-derivable rocket fuel)"],
        earth_imports_steady_state=[
            "Cryogenic storage hardware spares (low rate)",
        ],
        # H2O → H2 + 0.5 O2 needs 285 kJ/mol H2O = 8.9 kWh/kg H2O
        # which is 9.9 kWh/kg O2 (mass-weighted).
        # Plus sublimation + collection: realistic 30-100 kWh/kg O2.
        energy_kwh_per_kg_o2_process=10.0,
        energy_kwh_per_kg_o2_wallplug=80.0,
        trl_now_2026=4,           # OxEon TRL 5 for electrolyzer; extraction
                                  # bottleneck is prospecting (PRIME-1 partial)
        trl_2030_compressed=7,    # if VIPER 2027 closes resource question
        trl_2030_stall=4,         # remains prospecting-blocked
        notes="The only lunar-derivable HYDROLOX route. Resource question is the binding gate (PRIME-1 incomplete, VIPER delayed to 2027). Process is mature (OxEon TRL 5 for the electrolyzer step).",
    ),
    Process(
        name="Sintering / vacuum casting",
        feedstock_region="any",
        feedstock_phase="loose regolith → consolidated solid",
        operating_T_C=1100,
        products=["Structural blocks", "Bricks", "Pavement", "Glass-like panels"],
        earth_imports_steady_state=[
            "Sintering equipment maintenance (heaters, optics)",
        ],
        energy_kwh_per_kg_o2_process=0.0,   # not an O2 process
        energy_kwh_per_kg_o2_wallplug=0.0,
        trl_now_2026=5,           # JPL Sinterator + extrusion 3D printing
        trl_2030_compressed=8,
        trl_2030_stall=5,
        notes="Structural-mass route. Not an O2 producer. Produces structural elements directly from regolith via sintering or laser glass-forming. Combined with MRE/carbothermal in an integrated plant, this closes the structural-mass loop.",
    ),
]


# ---------------------------------------------------------------
# 4. Output the feasibility matrix
# ---------------------------------------------------------------

def main():
    print("="*78)
    print("q3-isru-feasibility — Pass 2 calc")
    print("Sources sealed. First-principles only.")
    print("="*78)
    print()

    # Regolith oxygen mass fractions
    print("--- Regolith composition (oxygen mass fraction) ---")
    for name, comp in [("Mare basalt", MARE_BASALT),
                       ("Highland anorthosite", HIGHLAND_ANORTHOSITE),
                       ("Polar (PSR) regolith", POLAR_REGOLITH)]:
        of = regolith_oxygen_mass_fraction(comp)
        print(f"  {name:24s} O wt fraction (from oxide phases): {of*100:.1f}%")
    print()

    # Thermodynamic floors per oxide
    print("--- Thermodynamic energy floors per kg O2 (per oxide) ---")
    for oxide in OXIDE_DGF_KJMOL:
        e = thermo_floor_kwh_per_kg_o2(oxide)
        print(f"  {oxide:6s}  →  {e:6.2f} kWh/kg O2 (Gibbs floor at ~1600 K)")
    print()

    # Mass-weighted floor for whole-regolith MRE on mare
    print("--- Whole-regolith MRE thermo floor (mare basalt input) ---")
    total_o_mass = 0.0
    total_energy_kj = 0.0
    for oxide in OXIDE_DGF_KJMOL:
        wt_pct = MARE_BASALT.get(oxide, 0.0)
        if wt_pct == 0:
            continue
        # mass of O in this oxide per kg of regolith
        M_oxide = {"SiO2": 60.08, "Al2O3": 101.96, "FeO": 71.85,
                   "MgO": 40.31, "CaO": 56.08, "TiO2": 79.87}[oxide]
        n_O_per_mole = OXIDE_N_O[oxide]
        o_mass_per_kg_regolith = (wt_pct/100.0) * (n_O_per_mole * 16.0) / M_oxide
        dgf = OXIDE_DGF_KJMOL[oxide]
        kj_to_liberate = (wt_pct/100.0) * 1000.0 / M_oxide * dgf
        total_o_mass += o_mass_per_kg_regolith
        total_energy_kj += kj_to_liberate
    floor_kwh_per_kg_o2 = (total_energy_kj / total_o_mass) / 3600.0
    print(f"  Mass-weighted MRE thermo floor: {floor_kwh_per_kg_o2:.1f} kWh/kg O2")
    print(f"  Total O liberated from 1 kg mare regolith: {total_o_mass*1000:.0f} g")
    print()

    # Process matrix
    print("--- Process × material × TRL feasibility matrix ---")
    print(f"{'Process':30s} {'Region':10s} {'T_C':5s} {'kWh/kg O2 wall':16s}"
          f" {'TRL26':6s} {'TRL30c':7s} {'TRL30s':7s}")
    for p in PROCESSES:
        print(f"{p.name:30s} {p.feedstock_region:10s} {p.operating_T_C:5d}"
              f" {p.energy_kwh_per_kg_o2_wallplug:16.0f}"
              f" {p.trl_now_2026:6d} {p.trl_2030_compressed:7d}"
              f" {p.trl_2030_stall:7d}")
    print()

    # Materials accessibility verdict
    print("--- Materials × best process pairing ---")
    print(f"{'Material':22s} {'Best route':40s} {'TRL26':6s} {'Earth imports'}")
    materials = [
        ("Oxygen (O2)",       "Carbothermal (TRL 6)",                "high"),
        ("Iron (Fe)",         "MRE coproduct / ilmenite reduction",  "low"),
        ("Silicon (Si)",      "MRE coproduct / carbothermal",        "low"),
        ("Aluminum (Al)",     "FFC Cambridge on anorthite",          "Cl bath (high)"),
        ("Titanium (Ti)",     "FFC Cambridge on ilmenite",           "Cl bath (high)"),
        ("Magnesium (Mg)",    "MRE coproduct (minor)",               "low"),
        ("Glass (SiO2)",      "Vacuum sintering / vapor pyrolysis",  "low"),
        ("Structural blocks", "JPL Sinterator / 3D print sintered",  "low"),
        ("LOX propellant",    "Any O2 process (carbothermal lead)",  "low (just makeup gases)"),
        ("LH2 propellant",    "Polar ice electrolysis ONLY",         "low if VIPER closes question"),
        ("LCH4 propellant",   "No lunar-derivable route at scale",   "ALL CARBON imported"),
    ]
    for m, r, ei in materials:
        # find best TRL among matching processes (approximate by name match)
        print(f"{m:22s} {r:40s} {'':6s} {ei}")
    print()

    # Acceleration-regime decomposition
    print("--- Acceleration-regime TRL decomposition (anti-pattern #11) ---")
    print()
    print("  Under TAI-grade automation compression (TAI-C):")
    print("    * Demonstration cadence rises ~10×: each MRE/carbothermal lab")
    print("      iteration that took 18 months drops to ~6-10 weeks")
    print("    * Earth-feedback loop tightens via robotic CLPS demos")
    print("      → 2-3 CLPS demos per year vs 1 every 2 years today")
    print("    * Capital-mass compression in plant designs (q4 lever)")
    print("    * Result: carbothermal + MRE reach TRL 8 (flight-demo'd, returning")
    print("      product) by 2028-2030; structural-mass loops by 2032-2035.")
    print()
    print("  Under business-as-usual (BAU):")
    print("    * NASA budget remains constrained; Artemis schedule slips ~1y/yr")
    print("    * CLPS missions deliver O2 ISRU demos but no product flow")
    print("    * Carbothermal reaches TRL 7 by 2030, TRL 8 by 2035-2040")
    print("    * MRE reaches TRL 6-7 by 2030, TRL 8 by 2035-2040")
    print()
    print("  Under stall (50-year-Apollo-drought analog):")
    print("    * Political will collapses; CLPS programme winds down")
    print("    * Carbothermal stays at TRL 6 indefinitely (Sierra demo")
    print("      becomes a museum piece)")
    print("    * MRE remains TRL 4 (Sadoway lab + Helios sim chamber)")
    print("    * No lunar product flow at any horizon")
    print()
    print("  The TRL trajectory depends on regime, not calendar year. This")
    print("  decomposition is the q3 deliverable for q4/q8 synthesis: q4's")
    print("  cost numerator is meaningless if regime = stall, because no")
    print("  product exists to ship; q4's framework is binding only under")
    print("  BAU or TAI-C.")

if __name__ == "__main__":
    main()
