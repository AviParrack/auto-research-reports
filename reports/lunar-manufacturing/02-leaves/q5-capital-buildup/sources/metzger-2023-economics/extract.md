---
slug: metzger-2023-economics
title: "Economics of In-Space Industry and Competitiveness of Lunar-Derived Rocket Propellant"
url: https://arxiv.org/abs/2303.09011
fetched: 2026-05-26
fetcher: claude
tier: S
type: paper
peer_reviewed: true
venue: "Acta Astronautica"
authors: ["Philip T. Metzger"]
year: 2023
date: 2023-06-01
topics: [capex-models, isru-plant-scaling, depreciation-curves, staged-buildup-milestones]
public_figure: null
---

## Abstract

Verbatim: "Economic parameters are identified for an in-space industry where the capital is made on one planet, it is transported to and teleoperated on a second planet, and the product is transported off the second planet for consumption. This framework is used to model the long-run cost of lunar propellant production to determine whether it is commercially competitive against propellant launched from Earth." The paper develops the gear-ratio (G) and production-mass-ratio (φ) framework; G is the cost-weighted mass ratio of moving hardware between locations, φ is the mass of product the capital produces over its lifetime divided by the mass of the capital. The competitiveness condition is shown to be (x + G)/φ + ω + ξ < 1/Γ where Γ is the destination-relative gear-ratio. Seven prior techno-economic analyses are re-examined in this common framework. Tent-sublimation TEAs (Kornuta, Sowers) yield φ in the hundreds; strip-mining TEAs (Jones, Charania-DePascuale, Bennett, Pelech) cluster around the breakeven φ. The paper concludes that lunar-derived propellant can outcompete Earth-launched propellant under realistic technology and commercial-launch (rather than SLS-class) capital transport assumptions, with the headline conclusion that absolute advantage at GTO requires φ ≳ 35 under the MVP cost model, and that the long-term-reliability of lunar capital is the primary remaining concern.

## Key claims

- gear-ratio-framework: "The 'gear ratio on cost' for capital transport (G) and the production mass ratio of the capital (φ) are identified as the most important factors determining competitiveness." (abstract)
- competitiveness-condition: "[(x + G)/φ + ω + ξ] · Γ_X < 1" (Eq. 8 — competitiveness inequality at destination X)
- mvp-phi-35-gto: "For Metzger's MVP design (φ ≈ 36.5) GTO lunar-propellant achieves absolute advantage under the model's cost assumptions." (Table 2 — see q4 leaf for full mapping)
- tent-sublimation-phi-442-534: "Kornuta (ULA-tent) φ = 442, Sowers φ = 534." (Table 2)
- strip-mining-phi-3.7-43.4: "Strip-mining φ estimates cluster around the breakeven with substantial spread: Jones φ = 22.2, Charania-DePascuale φ = 26.5, Bennett φ = 43.4, Pelech φ = 3.7." (Table 2)
- reliability-primary-concern: "Long-term reliability of the lunar capital is the primary remaining concern." (conclusion)
- mk-not-fixed: "M_K (capital mass) depends critically on whether the design uses terrestrial-excavator analogies (overestimates) or space-engineered hardware." (re-analysis of Pelech)
- sls-vs-commercial-launch: "Pessimistic published TEAs (Charania-DePascuale G ≈ 65, Jones G ≈ 42) used SLS-class pricing for capital transport. With commercial launch G drops by an order of magnitude." (Section 6.1-6.2)

## Reviewer notes

Already extracted in q4-gear-ratio leaf as the canonical source for the gear-ratio framework. Re-cited here because it sets the **dimensional analysis** for q5: capex per kg of product over the operating lifetime decomposes into (i) launch cost of capital, (ii) capital mass, (iii) operations cost, (iv) finance cost. The paper does not give a dollar figure for total lunar manufacturing capex — it gives the structural condition that any capex level must satisfy. Notably absent in this paper: explicit treatment of how AI/TAI-grade automation collapses M_K or compresses the program schedule; the framework accommodates such compression as a multiplier on φ but does not derive it. Cross-leaf: q4 owns the framework derivation; q5 inherits the cost-decomposition substrate to compute total $-capex.
