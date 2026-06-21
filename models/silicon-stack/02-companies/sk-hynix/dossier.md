---
company: sk-hynix
name: "SK Hynix"
url: "https://www.skhynix.com/"
tier: B
role: "HBM memory stacks (with Samsung, Micron)"
location: "Icheon, South Korea"
revenue_usd: 30000000000
scaffold: false
---

## Overview

SK Hynix is the HBM leader — high-bandwidth memory is the back-end rail the naive
chip chain omits, yet it often **rivals or exceeds the logic-die cost** in a
finished accelerator.

## The economics

- **HBM3E ~$8–10/GB**, ~$300+ per 36 GB stack; SK Hynix 12-hi reported mid-$300s/stack, HBM4 reportedly mid-$500s ([TrendForce](/models/silicon-stack/sources/trendforce-hbm3e-price/)).
- **6–8 stacks per accelerator** (H200 = 6, some ASICs = 8) ⇒ **~$2,000–4,000 of HBM per package**.
- HBM3E prices rising ~20% for 2026 on AI demand.

## Position in the chain

Supplies HBM stacks into [TSMC CoWoS](/models/silicon-stack/companies/tsmc/) packaging alongside the logic die — see [Inputs → HBM](/models/silicon-stack/inputs/) and the [Overview Sankey](/models/silicon-stack/).
