---
pass: 2
kind: calc
leaf: q1-earth-launch-cost
date: 2026-05-25
agent: claude-opus-4-7
sources_sealed: true
audited: pending
---

# Pass 2 — First-principles Starship cost/kg derivation (q1)

A bottom-up cost-per-launch model swept across three operational scenarios (optimistic 100-reuse / partial 30-reuse / pessimistic 10-reuse) and three era assumptions (early/mid/late). Sources sealed — Musk's $10/kg targets and Citigroup's $100/kg forecast were not consulted.

The Python derivation: [pass-02-calc.py](pass-02-calc.py). Captured stdout: [pass-02-calc-output.txt](pass-02-calc-output.txt).

## Cost decomposition per launch

A Starship launch's cost is approximately:

\\[ C_{\\text{launch}} = \\frac{C_{\\text{hardware}}}{N_{\\text{reuse}}} + C_{\\text{propellant}} + r \\cdot C_{\\text{hardware}} + C_{\\text{ops}} \\]

Where:
- \\(C_{\\text{hardware}}\\) = total stack build cost (~$90M for booster + ship)
- \\(N_{\\text{reuse}}\\) = number of reuse cycles per stack
- \\(C_{\\text{propellant}}\\) = methalox propellant cost per launch (~$1M; ~3,400t at LOX/LCH4 industrial prices)
- \\(r\\) = refurbishment rate (% of build cost per reuse cycle): 30% early, 15% mid, 8% late
- \\(C_{\\text{ops}}\\) = launch-site ops and ground handling per flight: $2M early, $1M mid, $0.5M late

Cost per kg to LEO is then \\(C_{\\text{launch}} / m_{\\text{payload}}\\), with payload sweeping 50 → 100 → 150 t across the scenarios.

## Results

| Scenario | Reuses | Payload (t) | Era | $/kg (first-principles cost) |
|---|---|---|---|---|
| Optimistic | 100 | 150 | early | $277/kg |
| Optimistic | 100 | 150 | mid | $151/kg |
| Optimistic | 100 | 150 | late | $59/kg |
| Partial | 30 | 100 | early | $466/kg |
| Partial | 30 | 100 | mid | $245/kg |
| Partial | 30 | 100 | late | $107/kg |
| Pessimistic | 10 | 50 | early | $878/kg |
| Pessimistic | 10 | 50 | mid | $440/kg |
| Pessimistic | 10 | 50 | late | $194/kg |

## What the math shows

1. **Refurbishment cost dominates at high reuse counts**, not hardware amortization. At 30+ reuses, the per-launch hardware contribution drops below $30/kg on a 100t payload. Refurbishment at 15% of build cost contributes ~$135/kg. To break below $100/kg the refurbishment rate must compress to <5% of build cost.

2. **Musk's claimed $10/kg list price is not derivable** from these first-principles assumptions without zero-margin pricing. Even the most aggressive operational scenario (100 reuses, 150t payload, 8% refurb, $0.5M ops) lands at ~$60/kg internal cost. List price with typical aerospace margin (2-3×) would be $120-180/kg.

3. **The partial-reuse central scenario lands at $107-466/kg** depending on era. This is the most defensible 2030-2035 estimate given current operational uncertainty.

4. **The pessimistic scenario ($194-878/kg) implies no improvement over Falcon 9**. At 10 reuses on Block 1 hardware with early operational costs, Starship's effective $/kg is in Falcon 9 list-price territory. This is the "operational ceiling" scenario.

## Industrial-explosion sensitivity (modulo TAI)

The compressible variables under sustained automation pressure are:
- **Refurbishment labor and time** — could collapse 10× with full robotic refurbishment. Drives refurb rate from 8% toward 1-2%.
- **Launch cadence** — could rise 10× as ground handling automates, amortizing fixed infrastructure faster.
- **Ground-ops cost** — could collapse 5× as launch-site operations automate.

Combined effect on optimistic-scenario: cost compresses from $60/kg to roughly $15-25/kg. Even under TAI conditions, the path to $10/kg requires the additional step of accepting zero or negative margin during market-capture phase.

## What 2026 evidence tells us about which scenario we're in

The research-pass evidence shows Falcon 9 list prices *rising* at $500/kg/year through 2026. Starship has not yet operationalized at scale enough to pull market list prices down. Two possibilities:

- **(A) Cost crossover happens later in the decade**: Starship begins commercial service at scale around 2028-2030; list prices begin falling after Starship operates at internal cost < Falcon 9's marginal cost.
- **(B) Cost crossover happens never**: Starship operates but at the partial/pessimistic scenario, never below current Falcon 9 economics. Market list prices stabilize at $1,000-3,000/kg through 2040.

Neither (A) nor (B) reproduces the Musk-optimistic public narrative. The "$10/kg by 2030" target requires both technical and commercial breakthroughs simultaneously.

## Carry to reconcile

The reconcile sub-pass should:
1. Compare the partial scenario ($107-466/kg by 2030-2035) to Citigroup's $100/kg-by-2040 forecast and Musk's $10/kg target.
2. Identify which TEAs (Metzger 2023 used $30-2000/kg) used which scenarios.
3. Check whether the gap between internal cost and list price persists in Starship era or collapses.

## Anti-pattern check

- ✓ Sources sealed — no Musk or Citigroup numbers used
- ✓ Math shown explicitly via Python; not handwaved
- ✓ Conditional framing — three scenarios with assumptions
- ✓ Industrial-explosion sensitivity flagged separately, not as point estimate
- ✓ Voice register dry: "the math shows", not "remarkably" or "is huge"
