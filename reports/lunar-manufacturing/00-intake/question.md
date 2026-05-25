# Root Question

**When does lunar surface manufacturing become cheaper than Earth launch for orbital infrastructure?**

## Why this question

Earth-to-LEO launch costs are falling fast (Starship trajectory: projections range from $10/kg to $300/kg by 2040 depending on reusability and cadence). Lunar manufacturing has been proposed as a long-term cheaper source of structural mass for orbital infrastructure (data centers, power plants, propellant depots) because the moon's escape velocity is ~2.4 km/s versus Earth's ~9.4 km/s.

The crossover point — when (if ever) it becomes cheaper to ship a kilogram from the lunar surface to LEO than from Earth's surface to LEO — is the central economic question of cislunar industrial development. Newman's framing (cost crossovers determine which workloads migrate to space) applies here at the manufacturing layer.

## Scope notes

- **Subject:** bulk structural mass (steel, aluminium, silicon, oxygen, propellant), not high-precision electronics
- **Time horizon:** 2026-2040
- **Comparison:** Earth-launched costs, not orbital manufacturing costs
- **Inclusions:** capital and time-to-first-export in the comparison, not just steady-state $/kg
- **Key economic variable identified during intake:** Metzger's *gear ratio* — lunar capital must produce ≥35× its mass in product to be viable. This is the dominant lever, not raw $/kg of either side.

## Seed sources (gathered during intake pass)

These are the high-priority sources future leaf passes should fetch, extract, and Source Review:

### Canonical academic
- **Metzger et al. (2023)** — *Economics of In-Space Industry and Competitiveness of Lunar-Derived Rocket Propellant*, Acta Astronautica. The "gear ratio" framing and the 35× threshold come from here. arXiv 2303.09011.
- **NASA NTRS** — *Cost Breakeven Analysis of Lunar In-Situ Propellant Production*. Estimated 35-year breakeven (≈7 Mars missions). [ntrs.nasa.gov/citations/20205007564](https://ntrs.nasa.gov/api/citations/20205007564/downloads/ISRU-Paper3-Final.pdf)
- **AIAA 2025** — *Cost-Benefit Analysis of Lunar Mass Driver Technologies*. doi:10.2514/6.2025-4123

### Industry / analysis
- **Andrew McCalip** (Varda Space) — public orbital/lunar economics calculator at andrewmccalip.com. Notable claim: "physics doesn't immediately kill it, but the economics are savage."
- **PwC** — *Lunar Market Assessment* (ESA): $93-127B revenue by 2050, $72-88B cumulative infra investment 2026-2050. 70-80% of lunar infra cost is transportation 2026-2035.
- **CSIS** — *Cracking the Code on the Lunar Economy*.

### Public figures to Source Review
- **Philip Metzger** (UCF / NASA, planetary scientist) — gear-ratio framing, ISRU economics
- **Andrew McCalip** (Varda) — orbital and lunar economics analyst
- **Gerard O'Neill** (legacy) — mass driver originator; modern analyses derive from his work
- **Elon Musk** — Starship cost projections (claims as low as $10/kg)
- **George Sowers** (Colorado School of Mines) — lunar propellant
- **Robert Zubrin** — typically Mars-first, skeptical of lunar industrial path

### Mass driver / lunar gravity anomalies
- arxiv 2410.09616 — *Launching mass from the Moon helped by lunar gravity anomalies* (2024)

## Methodology notes

The intake pass focused on scoping; no claims have been written to claims.yaml yet. Leaf passes will fetch each cited source into `02-leaves/{leaf}/sources/{slug}/extract.md` before any claim can cite it.

The tree (v1) decomposes the question into 8 nodes covering: Earth launch cost trajectory (q1), lunar ascent cost (q2), ISRU feasibility (q3), gear ratio (q4), capital buildup (q5), orbital demand (q6), mass driver feasibility (q7, constraint), and synthesis crossover (q8). See `01-tree/tree.yaml`.
