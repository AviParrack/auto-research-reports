---
company: synopsys
name: "Synopsys (the EDA duopoly)"
url: "https://www.synopsys.com/"
tier: B
role: "EDA tools + IP — the design rail"
location: "Sunnyvale, CA, USA"
revenue_usd: 6500000000
scaffold: false
---

## Overview

Every leading-edge chip is designed on EDA software. **Synopsys (~38%) + Cadence
(~36%) = ~74%** of the EDA market — a duopoly chokepoint with ~80–85% recurring
revenue and near-100% retention ([analysis](/models/silicon-stack/sources/snps-cdns-duopoly/)).

## The design rail

- **Arm** and third-party PHY/SerDes IP add royalties of **~1–4% of chip revenue**.
- A **3nm design NRE is $400–600M+** (EDA + IP + verification + headcount), resolving into a **~$15M mask set** — amortized to a few hundred $/wafer over volume ([cost breakdown](/models/silicon-stack/sources/siliconanalysts-3nm-cost/)).

## Position in the chain

This is a **parallel rail**, not an upstream supplier: design value is amortized per-die NRE, not a per-wafer cash cost. Feeds the [photomask set → TSMC](/models/silicon-stack/inputs/). See the [Overview Sankey](/models/silicon-stack/).
