---
leaf: q1-earth-industrial-ceiling
pass: 03-reconcile
started: 2026-06-08T22:30:00Z
ended: 2026-06-08T22:55:00Z
researcher: claude-opus-4-7
---

# Pass 03 — Reconcile

Sources unsealed. Compare derived numbers from pass-02-calc.md to what extracts in `sources/` say. Update `claims.yaml`.

## Agreement table

| Derived claim | Calc value | Source value(s) | Verdict |
|---|---|---|---|
| **LOX per Block 3 launch** | 4,422 t | Wikipedia Block 3: 5,650 t × (3.6/4.6) = 4,422 t exact | **Consistent** |
| **LCH4 per Block 3 launch** | 1,228 t | Wikipedia Block 3: 5,650 t × (1/4.6) = 1,228 t exact | **Consistent** |
| **Per-launch propellant (Block reference)** | 5,650 t Block 3 baseline; ±20% across Blocks | Mobius: 4,600 t (Block 1); SDC: 4,900 t (Block 2); Wiki: 5,150 t (Block 2), 5,650 t (Block 3); ranged | **Consistent** with documented Block sensitivity |
| **LOX:LCH4 mass ratio** | 3.6:1 (operating; fuel-rich) | Mobius: 3.6:1; Wikipedia Raptor: 3.6 mixture ratio; SDC: same | **Consistent**; Codex audit corrected my characterisation (4.0:1 is stoichiometric, 3.6:1 is fuel-rich) — fixed in calc |
| **US O₂ production ~10.3 Mt/yr** | assumed | SDC anchor → EPA 2023, 2019 data: 10.3 Mt/yr; Air Liquide Baytown adds 3.29 Mt/yr to TX subset (consistent scale) | **Consistent** — but primary EPA PDF did not fetch; cite via SDC anchor with **medium confidence** |
| **Global O₂ production ~90 Mt/yr** | assumed | SDC anchor → Mordor Intelligence: 88-92 Mt/yr (2025-26) | **Consistent**, single secondary source — **medium confidence** |
| **US NG consumption ~33.5 Tcf/yr** | assumed (EIA) | EIA Navigator: 33.52 Tcf/yr (2025 data released May 2026) | **Consistent** — primary government data, high confidence |
| **Per-launch NG equivalent ~62 mmscf** | derived | Mobius: "62.24 mmscf" per launch | **Consistent** |
| **US stainless production ~1.95 Mt/yr** | assumed | GMK Center 2024: 1.95 Mt | **Consistent**, primary trade-data |
| **Global stainless ~62.6 Mt/yr** | assumed | GMK Center 2024: 62.621 Mt | **Consistent** |
| **Raptor production target ~1,000/yr** | assumed | Wikipedia Raptor: "800 to 1,000 rocket engines each year" target | **Consistent** with stated SpaceX target — aspirational |
| **Engine reuse-life 100 flights** | assumed | Wikipedia: aspirational "1,000 flights"; Falcon 9 record 33 (B1067 33 flights, SDC anchor) | **Documented aspirational** — my 100-flight assumption is between Falcon 9 record (33) and Raptor aspirational (1,000) |
| **ASU energy intensity ~300 kWh/t O₂** | assumed | Thunder Said Energy: 150-800 kWh/t range; SDC anchor: 200-500 kWh/t modern cryogenic | **Consistent** within stated range; mid-low value |
| **ASU capex ~$200/(t/yr) capacity** | not used directly | Thunder Said Energy: ~$200/Tpa; Air Liquide Baytown: $850M / 3.29 Mt/yr = $258/(t/yr); Linde Starbase (SDC): $100M / 0.73 Mt/yr ≈ $137/(t/yr) | **Consistent** with $137-258/(t/yr) range |
| **Plausible mature global pad count ~50** | assumed | SDC: ~5 Starship pads by 2027; current global active launch sites ~30 | **Consistent within OOM**; 50 is modest expansion from current ~30 sites |
| **Aspirational pad cadence 1-3 launches/day** | assumed | SDC: Musk "Starship launches every hour within 3 years"; Falcon 9 record 45 hr pad turnaround | **Consistent** as the aspirational range |
| **Musk aspirational target 10,000 ships/yr** | flagged | Benzinga Jan 2026: Musk "Maybe as high as 10,000 ships per year" production | **Consistent** — direct primary quote |
| **Handmer trajectory 10⁶ t/yr LEO** | flagged | Handmer 2021 blog: "Eventually, it could exceed 1,000,000 T/year" | **Consistent** — direct primary quote |
| **Handmer 67k launches/yr for 1 TW orbital solar** | not used directly | Handmer 2026 mass-driver post: "67,000 launches per year… with just seven or eight pads… a fleet of perhaps 10 boosters and a few hundred Starships" | **Novel supporting** — independently bounds the q1 ceiling at ~67k launches/yr from a different demand-side direction |

## Disagreements

**No substantive disagreements found.** All derived numbers reconcile with the source extracts within the documented Block-2/Block-3 sensitivity range and the explicit aspirational-vs-current overlay on the engine and pad parameters. The qualitative ordering (LOX binds first; engines second; pads third; methane / steel / ASU power not binding at the cadences analysed) is corroborated by every source that touches on it.

## Notable cross-references

1. **Handmer's "67,000 launches/yr for 1 TW orbital solar"** is a useful independent triangulation. At 100 t/launch this is 6.7 Mt/yr to LEO, which sits comfortably below my derived 1-100 Mt/yr ceiling but above the LOX hard ceiling (~2,300 launches/yr from current US O₂). So serving 1 TW of orbital solar annually requires building dedicated LOX capacity (per the calc's "dedicated ASUs × 1,350" line for 100 Mt/yr scale). Handmer treats this as plausible.

2. **Musk's 10,000 ships/yr** is a *production target* not a *flight target*. At 100-flight reuse, 10,000 ships/yr of production supports 1,000,000 launches/yr in steady-state (after fleet replacement). My derived ceilings show LOX binds at ~2,300 launches/yr from current US O₂; reaching 10⁶ launches/yr requires ~1,350 Baytown-class ASUs (~$1.1T capex) plus ~2,700 pads. **Musk's 10,000-ships target is bounded by LOX, not by ship production.**

3. **The SDC anchor's "2,660 launches/yr LOX hard ceiling"** is from a Block-2 baseline (3,870 t LOX/launch); my Block-3 calc gives 2,330 launches/yr. Different Blocks; same OOM; **consistent**.

## Resolution

- **Hold** all derived numbers and the qualitative ordering. No re-derivation needed.
- **Promote** Handmer's 67k-launches-for-1-TW-orbital-solar from "context" to "evidence" — it bounds the realistic plausible-demand-end of the question.
- **Promote** Musk's 10k-ships/yr as a public-figure target that the calc shows is LOX-bound, not production-bound. This is a load-bearing factual claim for tier-B source review.
- **Flag for source-review pass:** the EPA O2 PDF retrieval failure means our most-load-bearing US-LOX-supply number rests on a secondary citation. A re-pass should fetch the EPA HTML or use the alternative USGS / industrial-gas-association primary data.

## claims.yaml — new entries

Adding 11 claims to `claims.yaml`. Each is `derived` from pass-02-calc.md and reconciled with at least one source from the research pass. All audit.gpt entries refer to pass-02-audit.md and pass-02-response.md.

## Next sub-pass

`--pass leaf --leaf q1-earth-industrial-ceiling --sub source-review` — per-tier review with verdict taxonomy.
