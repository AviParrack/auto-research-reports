"""
Figure generation for lunar-manufacturing synthesis v1.

Run from `03-synthesis/v1/`:
    python3 figures.py

Outputs to figures/.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

FIG_DIR = Path(__file__).parent / "figures"
FIG_DIR.mkdir(exist_ok=True)

# --------------------------------------------------------------------
# Figure 1: Cost crossover — q1 (Earth) vs q2 (lunar) across architectures
# --------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5.5))

architectures = {
    "Earth launch — pessimistic":      [878,  466,  277],
    "Earth launch — partial reuse":    [466,  287,  107],
    "Earth launch — optimistic":       [277,  168,   59],
    "Lunar chemical — Earth-imports":  [13029, 4162, 1303],
    "Lunar chemical — aggressive-ISRU":[8912, 3500,  994],
    "Lunar mass-driver + SEP":         [528,  152,   50],
}
eras = ["Early\n(2026-30)", "Mid\n(2030-35)", "Late\n(2035-40)"]
colors = {
    "Earth launch — pessimistic":      "#a44a3f",
    "Earth launch — partial reuse":    "#cd853f",
    "Earth launch — optimistic":       "#5d9c75",
    "Lunar chemical — Earth-imports":  "#7a3b8f",
    "Lunar chemical — aggressive-ISRU":"#9c6b3f",
    "Lunar mass-driver + SEP":         "#2e6da4",
}
linestyles = {
    "Earth launch — pessimistic":      "-",
    "Earth launch — partial reuse":    "-",
    "Earth launch — optimistic":       "-",
    "Lunar chemical — Earth-imports":  "--",
    "Lunar chemical — aggressive-ISRU":"--",
    "Lunar mass-driver + SEP":         "-.",
}
for arch, costs in architectures.items():
    ax.plot(eras, costs, marker="o", lw=2, label=arch,
            color=colors[arch], linestyle=linestyles[arch])

ax.set_yscale("log")
ax.set_ylabel("Cost to LEO ($/kg, log scale)")
ax.set_title("Cost-per-kg to LEO across architectures and operational eras\n(under BAU regime; TAI compression shifts every curve down ~5-10×)")
ax.axhspan(50, 60, alpha=0.18, color="green", label="Crossover band\n($50-60/kg)")
ax.grid(True, which="both", linestyle=":", alpha=0.45)
ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=8, frameon=False)
plt.tight_layout()
plt.savefig(FIG_DIR / "fig1-cost-crossover.png", dpi=150, bbox_inches="tight")
plt.close()

# --------------------------------------------------------------------
# Figure 2: Demand by use case across regimes (q6)
# --------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5.5))

regimes = ["Stall", "BAU", "TAI-C"]
# All values in cumulative kt across 2026-2040 (15 years)
sdc       = [20,   2000, 40000]    # kt
sbsp      = [0,    25,   500]      # kt
depots    = [0,    160,  3200]     # kt  (mid of 8-16 kt/yr × 15 yr / 320 kt/yr × 15 yr)
lunar_srf = [0,    0.45, 7.5]      # kt  (30 t/yr × 15 yr / 500 t/yr × 15 yr) → negligible
mars      = [0,    3,    225]      # kt  (200 t/yr × 15 yr / 15 kt/yr × 15 yr)
servicing = [0.75, 3,    30]       # kt  (50 t/yr × 15 yr / 200 t/yr / 2 kt/yr × 15 yr)

x = np.arange(len(regimes))
width = 0.55
bot = np.zeros(3)
labels_vals = [
    ("Space data centres", sdc, "#2e6da4"),
    ("Space-based solar power", sbsp, "#cd853f"),
    ("Propellant depots", depots, "#a44a3f"),
    ("Lunar surface cargo", lunar_srf, "#9c6b3f"),
    ("Mars cargo (LEO transit)", mars, "#5d9c75"),
    ("Satellite servicing", servicing, "#7a3b8f"),
]
for label, vals, c in labels_vals:
    ax.bar(x, vals, width, bottom=bot, label=label, color=c, edgecolor="white", lw=0.4)
    bot += np.array(vals)

ax.set_yscale("symlog", linthresh=10)
ax.set_xticks(x)
ax.set_xticklabels(regimes)
ax.set_ylabel("Cumulative mass demand 2026-2040 (kt, symlog scale)")
ax.set_title("Orbital mass demand by use case, by acceleration regime")
ax.axhline(6000, color="black", lw=1.5, linestyle=":", label="Earth-launch ceiling\n(15 yr × 400 kt/yr)")
ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=8, frameon=False)
ax.grid(True, axis="y", linestyle=":", alpha=0.45)
plt.tight_layout()
plt.savefig(FIG_DIR / "fig2-demand-regimes.png", dpi=150, bbox_inches="tight")
plt.close()

# --------------------------------------------------------------------
# Figure 3: Capex stacking — q5 base + q7 mass driver across regimes
# --------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.5, 5.0))

regimes = ["BAU", "Industrial\nExplosion", "TAI-grade"]
q5_base  = [275,   1.2,  0.05]   # USD billions (BAU midpoint of 150-400; TAI degenerate ~$50M)
q7_drive = [1242,  127,  13.3]   # USD billions
q2_other = [10,    5,    2]      # SEP + landers + ops; rough scaled
totals   = [q5_base[i] + q7_drive[i] + q2_other[i] for i in range(3)]

x = np.arange(len(regimes))
width = 0.55
ax.bar(x, q5_base, width, label="q5 base capex\n(habitat, power, ISRU, mfg)",
       color="#5d9c75", edgecolor="white", lw=0.4)
ax.bar(x, q7_drive, width, bottom=q5_base, label="q7 mass-driver launch system",
       color="#a44a3f", edgecolor="white", lw=0.4)
bot2 = [q5_base[i] + q7_drive[i] for i in range(3)]
ax.bar(x, q2_other, width, bottom=bot2, label="q2 SEP + landers + ops",
       color="#cd853f", edgecolor="white", lw=0.4)

for i, t in enumerate(totals):
    if t > 100:
        label = f"${t:.0f}B"
    elif t > 1:
        label = f"${t:.1f}B"
    else:
        label = f"${t*1000:.0f}M"
    ax.text(x[i], t * 1.15, label, ha="center", fontsize=10, fontweight="bold")

ax.set_yscale("log")
ax.set_xticks(x)
ax.set_xticklabels(regimes)
ax.set_ylabel("Full architecture capex ($B, log scale)")
ax.set_title("Capex stacking: lunar manufacturing full architecture across regimes\n(q5 base + q7 mass driver + q2 transit infrastructure)")
ax.set_ylim(0.01, 5000)
ax.legend(loc="upper right", fontsize=8.5, frameon=True)
ax.grid(True, axis="y", which="both", linestyle=":", alpha=0.45)
plt.tight_layout()
plt.savefig(FIG_DIR / "fig3-capex-stacking.png", dpi=150, bbox_inches="tight")
plt.close()

# --------------------------------------------------------------------
# Figure 4: The two-legged crossover — schematic
# --------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

# Cost leg (left side)
ax.text(2.5, 9.0, "LEG 1 — Cost", ha="center", fontsize=13, fontweight="bold", color="#2e6da4")
ax.text(2.5, 8.2, "$50/kg vs $59/kg margin", ha="center", fontsize=10)
ax.text(2.5, 7.7, "(mass-driver+SEP vs Starship-optimistic)", ha="center", fontsize=8, style="italic")

# Throughput leg (right side)
ax.text(7.5, 9.0, "LEG 2 — Throughput necessity", ha="center", fontsize=13, fontweight="bold", color="#a44a3f")
ax.text(7.5, 8.2, "10× Earth-launch ceiling", ha="center", fontsize=10)
ax.text(7.5, 7.7, "(TAI-C SDC demand 2.67 Mt/yr vs 400 kt/yr)", ha="center", fontsize=8, style="italic")

# Conditional gate
ax.text(5.0, 6.3, "BOTH legs are conditional on TAI-grade compression", ha="center",
        fontsize=11, fontweight="bold", color="#7a3b8f",
        bbox=dict(boxstyle="round,pad=0.5", fc="#f4e8c1", ec="#7a3b8f", lw=1.5))

# Engineering risks
ax.text(5.0, 4.5, "Binding engineering risks (regime-independent):", ha="center", fontsize=11, fontweight="bold")
ax.text(2.0, 3.7, "Cycle-life gap\n10²-10³ shots demonstrated\nvs 10⁶-10⁹ required\n(materials-science\nbreakthrough required)",
        ha="center", fontsize=9,
        bbox=dict(boxstyle="round,pad=0.4", fc="#fbeae0", ec="#cd853f", lw=1))
ax.text(5.0, 3.7, "Polar-ice gate\n(VIPER late-2027)\nq2 aggressive-ISRU\ncollapses if unfavorable",
        ha="center", fontsize=9,
        bbox=dict(boxstyle="round,pad=0.4", fc="#fbeae0", ec="#cd853f", lw=1))
ax.text(8.0, 3.7, "M6 12-month floor\n(crewed-occupation\nirreducible by TAI\ncompression)",
        ha="center", fontsize=9,
        bbox=dict(boxstyle="round,pad=0.4", fc="#fbeae0", ec="#cd853f", lw=1))

# Verdict bands
ax.text(5.0, 1.6, "Under BAU: neither leg holds (mass driver doesn't reach scale; demand fits)",
        ha="center", fontsize=10, color="#7a3b8f")
ax.text(5.0, 1.0, "Under stall: demand fails entirely (q6.c7)",
        ha="center", fontsize=10, color="#7a3b8f")
ax.text(5.0, 0.4, "Under TAI-grade compression: crossover holds on both legs",
        ha="center", fontsize=10, color="#2e6da4", fontweight="bold")

ax.set_title("Lunar manufacturing crossover: structural summary",
             fontsize=12.5, fontweight="bold", pad=15)
plt.tight_layout()
plt.savefig(FIG_DIR / "fig4-two-legs-schematic.png", dpi=150, bbox_inches="tight")
plt.close()

print("Generated 4 figures in", FIG_DIR)
for f in sorted(FIG_DIR.glob("*.png")):
    print(" -", f.name)
