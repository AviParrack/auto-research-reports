# Root Question

**Does building a base on the Moon increase the total mass throughput humanity can deliver to elsewhere in the solar system — and at cosmic scales (Tt/yr), what constraints bind first on each side?**

## Why this question

A serious-space-industrialisation future requires moving very large quantities of mass from a gravity well into useful orbits and onwards to other parts of the solar system. Cosmic-scale interventions — a Dyson swarm, large-scale orbital industry, planetary-scale settlements — require throughputs many orders of magnitude beyond the present ~0.01 Mt/yr Earth-to-LEO figure. The central architectural question for the long arc of space expansion is whether Earth alone can scale to deliver this mass, or whether a lunar industrial base is *necessary* (not merely cheaper) because Earth runs into hard physical ceilings the Moon does not share.

Two narrower questions sit underneath:
1. **Earth's ceilings.** What bottleneck binds first as Earth-chemical-rocket throughput scales — industrial inputs, atmospheric chemistry, reentry pollution, orbital congestion? At what kt/yr or Mt/yr does each constraint bind?
2. **The Moon's ceilings.** A mature lunar industrial base launching via mass driver faces its own ceilings — power supply, regolith mining rate, Earth-shipped vitamin fraction, mass-driver cycle-life, catcher infrastructure at the destination. Where do those bind?

Then the integration: **per-destination throughput delta.** For LEO, GEO/cislunar, Mars/NEAs, the asteroid belt, outer planets, Mercury, sundivers — how does adding a mature lunar base change the kt/yr-or-Mt/yr ceiling humanity can deliver? And at cosmic scales (Tt/yr Dyson-relevant): does the Moon make that achievable when Earth alone cannot?

## Scope notes

- **Throughput calibration:** cosmic-scale (Tt/yr Dyson-relevant). Treat current ~0.01 Mt/yr as a baseline; ask where each constraint bites between 1 kt/yr and 100 Tt/yr.
- **Earth-launch architecture:** chemical rockets only (Starship-class methalox + reference RP-1/hydrolox). Exotic launch tech (launch loops, skyhooks, laser propulsion, NTP) is out of scope. Mentioned where it would change a ceiling but not analysed.
- **Moon-side scope:** Moon-as-launcher *and* Moon-as-supplier. The Moon can multiply Earth's interplanetary reach by either (a) launching cargo directly from the lunar surface via mass driver, or (b) supplying propellant/water/structure to LEO so that Earth-launched missions pay a smaller rocket-equation tax to interplanetary destinations. Both channels count.
- **Destinations:** LEO, GEO, cislunar, Earth-Sun L-points, Mars, NEAs, asteroid belt, Jovian system, Mercury orbit, sundivers, Dyson-swarm staging orbits.
- **Time framing:** no naive calendar timelines. Decompose into work-remaining + acceleration sensitivity (anti-pattern #11). Frame each ceiling as: where it bites in throughput, and conditionally how compressible the path to that ceiling is under BAU / industrial-explosion / TAI-compressed / stall regimes.
- **Cost is not the question.** Throughput, not $/kg. (The sibling report `lunar-manufacturing` already covers the cost crossover at LEO.)

## Seed sources (gathered during intake — to be extracted in leaf passes)

### Earth-side atmospheric chemistry
- **Murphy et al. (2023)** — *Metals from spacecraft reentry in stratospheric aerosol particles*, PNAS 120(43). 10% of stratospheric aerosols already contain spacecraft-origin metals. [pnas.org/doi/10.1073/pnas.2313374120](https://www.pnas.org/doi/10.1073/pnas.2313374120) / [PMC10614211](https://pmc.ncbi.nlm.nih.gov/articles/PMC10614211/)
- **NOAA CSL News (2025)** — *Within 15 years, plummeting satellites could release enough aluminum to alter winds, temps in the stratosphere*. [csl.noaa.gov/news/2025/427_0428.html](https://csl.noaa.gov/news/2025/427_0428.html)
- **Maloney et al. (2025)** — *Near-future rocket launches could slow ozone recovery*, npj Climate and Atmospheric Science. 2,040 launches/yr → -0.29% global / -3.9% Antarctic springtime ozone. [nature.com/articles/s41612-025-01098-6](https://www.nature.com/articles/s41612-025-01098-6)
- **Barker et al. (2026)** — *Radiative Forcing and Ozone Depletion of a Decade of Satellite Megaconstellation Missions*, Earth's Future. 8× increase in stratospheric Al oxides 2016-2022. [agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2025EF007229](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2025EF007229)
- **Ryan et al. (2022)** — *Impact of Rocket Launch and Space Debris Air Pollutant Emissions on Stratospheric Ozone and Global Climate*, Earth's Future. [agupubs.onlinelibrary.wiley.com/doi/10.1029/2021EF002612](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2021EF002612)
- **NASA TM-20240013276** — *Impact of Spaceflight on Earth's Atmosphere*. [ntrs.nasa.gov/citations/20240013276](https://ntrs.nasa.gov/api/citations/20240013276/downloads/NASA-TM-20240013276-V6.pdf)

### Earth-side industrial constraints (existing workspace anchor)
- **Workshop/Space/sdc/starship-launch-cadence-constraints.md** — internal compilation: LOX bottleneck at ~2,660 launches/yr from US O₂; methane, engines, pads, stainless steel scaling tables; FAA constraints; sonic boom. Cross-check with web sources during leaf pass.

### Lunar mass driver
- **Casey Handmer (May 2026)** — *How to build a lunar mass driver*. [caseyhandmer.wordpress.com/2026/05/08/how-to-build-a-lunar-mass-driver/](https://caseyhandmer.wordpress.com/2026/05/08/how-to-build-a-lunar-mass-driver/) — pulsed power is the main machine; rail is secondary.
- **NSS / O'Neill / Snyder** — *Mass Drivers III: Engineering* (NASA SP-428, 1979 lineage). [nss.org/settlement/nasa/spaceres/III-3.html](https://nss.org/settlement/nasa/spaceres/III-3.html) — 42 kg/s at 125 MW; 650 kt/yr at 49% duty; 2.4 MJ/kg energy floor.
- **arXiv 2410.09616 (2024)** — *Launching mass from the Moon helped by lunar gravity anomalies*. [arxiv.org/abs/2410.09616](https://arxiv.org/abs/2410.09616)
- **Miller (2023, SJSU)** — *Lunar Mass Driver Implementation*. [sjsu.edu/ae/docs/project-thesis/Ethan.Miller-Su23.pdf](https://www.sjsu.edu/ae/docs/project-thesis/Ethan.Miller-Su23.pdf)
- **AIAA 2025** — *Cost-Benefit Analysis of Lunar Mass Driver Technologies*. doi:10.2514/6.2025-4123

### Lunar ISRU and materials
- **Sanders / NASA NTRS (2022)** — *Plans for In Situ Resource Utilization*. [ntrs.nasa.gov/citations/20220008799](https://ntrs.nasa.gov/api/citations/20220008799/downloads/NASA%20ISRU%20Plans_Sanders_COSPAR-Final.pdf)
- **Sanders / NASA NTRS (2025)** — *Progress Review NASA Lunar ISRU*. [ntrs.nasa.gov/citations/20250003730](https://ntrs.nasa.gov/api/citations/20250003730/downloads/Progress%20Review%20NASA%20Lunar%20ISRU_Sanders.pdf)
- **Linne et al.** — *Estimating SRU operations to satisfy lunar oxygen demand*, Acta Astronautica.
- **Hybrid lunar ISRU plant** — [arxiv.org/html/2408.04936v1](https://arxiv.org/html/2408.04936v1)
- **PRIME-1, VIPER** — water-ice prospecting missions (gating the LH2 question)

### Lunar power
- **Casey Handmer** — *Powering the lunar base, version 2* (2022). [caseyhandmer.wordpress.com/2022/07/03/powering-the-lunar-base-version-2/](https://caseyhandmer.wordpress.com/2022/07/03/powering-the-lunar-base-version-2/)
- **Workshop/Space/solar-system/Lunar-Economics/full-analysis.md** — internal anchor: empirical power-scaling law (~M^0.94) from 11 real-world anchors.

### Launch loop reference (out of scope but cited)
- **Lofstrom (2009)** — 4 GW launch loop, 750 kt/yr at $3/kg theoretical. [emobility-engineering.com/lofstom-loop](https://www.emobility-engineering.com/lofstom-loop/) / [en.wikipedia.org/wiki/Launch_loop](https://en.wikipedia.org/wiki/Launch_loop)

### Cosmic scale / Dyson
- **Armstrong (Stuart)** — Mercury dismantling for Dyson swarm; ~1.3×10²³ kg Si for partial swarm.
- **Workshop/Space/dyson-swarm/strategy/all-notes.md** — internal anchor: mass driver g-load tradeoffs, Mercury-launched material assumptions.

### Anthropogenic mass anchors
- **Streeck et al. (2021)** — *Mapping in-use stocks of construction materials*. [onlinelibrary.wiley.com/doi/10.1111/jiec.13166](https://onlinelibrary.wiley.com/doi/10.1111/jiec.13166)
- **Elhacham et al. (2020)** — *Global human-made mass exceeds all living biomass*, Nature. [nature.com/articles/s41586-020-3010-5](https://www.nature.com/articles/s41586-020-3010-5)

### Public figures to Source Review (Tier B)
- Casey Handmer (Terraform Industries) — mass driver, lunar power
- Philip Metzger (UCF) — ISRU economics, regolith engineering
- Martin Elvis — space resources, fermi-paradox-at-scale arguments
- Robert Zubrin — Mars-first, skeptical of lunar industrial path
- Elon Musk — Starship cadence claims (10⁴+ launches/yr aspirational)
- Gerard O'Neill (legacy) — mass driver originator
- ToughSF / Matter Beam — launch architecture analysis

## Methodology notes

The intake pass is scaffolding only — no claims have been written to claims.yaml. Each cited source must be fetched and extracted into `02-leaves/{leaf}/sources/{slug}/extract.md` during the relevant leaf-pass before it can support a claim.

The tree v1 has 9 nodes: 3 Earth-side, 4 Moon-side (one constraint, three leaves), 1 cross-cutting, 1 final synthesis. See `01-tree/tree.yaml`.

## Anti-patterns specifically relevant to this report

- **#11 (calendar dates):** every "when" answer must decompose into engineering-work-remaining + acceleration sensitivity (BAU / industrial-explosion / TAI-compressed / stall).
- **#2 (source borrowing in calc):** throughput numbers (kg/s, kt/yr, GW) must be derived first-principles in P2 calc passes, then reconciled with sources in P3.
- **#9 (bury-the-lead):** every synthesis leads with the per-destination delta in the first 200 words.
- **#13 (editorialising):** state the data, don't dramatise. "The Moon delivers a 100× throughput multiplier at Mars" beats "remarkably, the Moon transforms our reach into the solar system."
