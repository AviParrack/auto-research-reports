---
slug: revell-2025-ozone
title: "Near-future rocket launches could slow ozone recovery"
url: "https://www.nature.com/articles/s41612-025-01098-6"
fetched: 2026-06-09
fetcher: claude
tier: S
type: paper
peer_reviewed: true
venue: "npj Climate and Atmospheric Science 8(1):212"
authors: ["Laura E. Revell", "et al."]
year: 2025
date: 2025-06-09
topics: [rocket-ozone-depletion, srm-chlorine, black-carbon-stratospheric, launch-rate-thresholds]
---

## Abstract

Revell et al. (2025) used a coupled chemistry-climate model to project the impact of rocket launches on stratospheric ozone recovery over the period through 2030. The paper builds two scenarios: a "conservative" projection of 884 launches per year and an "ambitious" 2,040 launches/year. Both scenarios use a fuel mix dominated by current trajectories (mixed solid-rocket-motor + kerosene + emerging methalox). Ozone depletion in the ambitious scenario reaches −0.29% annual-mean near-global total column, with Antarctic springtime ozone loss of 3.9%. The conservative scenario shows −0.17% annual near-global depletion. Both depletion estimates depend strongly on the current/projected fuel mix, with solid-rocket-motor chlorine and kerosene/hypergolic black carbon as the dominant agents. The authors note that current FAA/FCC licensing rates suggest the conservative scenario may be exceeded before 2030. **Crucially: methalox-specific scenarios are explicitly identified as a research gap** — the paper does not model what happens if the fleet transitions to pure methalox.

## Key claims

- launch-rate-conservative: "884 launches per year" → −0.17% near-global ozone annual mean.
- launch-rate-ambitious: "2,040 launches per year" → −0.29% near-global; **−3.9% Antarctic springtime ozone**.
- chlorine-from-SRM: dominant ozone-destroying mechanism, from solid rocket motor propellant.
- black-carbon-stratospheric: kerosene/hypergolic BC produces secondary ozone loss via stratospheric warming.
- methalox-uncertainty: "uncertainty about large-scale deployment effects" for methalox (LNG) specifically.
- antarctic-vs-global: Antarctic spring loss substantially larger than global average (chlorine activation on polar stratospheric clouds).
- timing: conservative scenario may be exceeded before 2030 at current licensing rates.

## Reviewer notes

This is the foundational tier-S paper for q2's ozone-binding analysis at the few-thousand-launches/yr scale. Key for our analysis: the paper's projections are at the **current fuel mix**, which includes large solid-rocket-motor contribution. Pure-methalox scenarios (which Starship-dominated futures would represent) eliminate the chlorine pathway and dramatically reduce BC; the residual ozone impact comes from stratospheric H2O perturbation, NOx from launch and reentry, and ablation-aerosol effects. **The paper does not establish a methalox-only ceiling. That requires separate first-principles calc.** Cross-reference with Ryan 2022 emission factors (LH2/methalox produce H2O but no BC, no Cl) and Murphy 2023 (reentry metals are independent of propellant choice).
