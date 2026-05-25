---
pass: 2
kind: calc
leaf: q2-lunar-ascent-cost
date: 2026-05-25
agent: claude-opus-4-7
sources_sealed: true
audited: pending
---

# Pass 2 — First-principles lunar-surface-to-LEO cost/kg derivation (q2)

A bottom-up cost-per-kg-payload model spanning three ISRU scenarios (aggressive / partial / Earth-imports-only) and three eras (early 2026–2030, mid 2030–2035, late 2035–2040), under two architectural families:

- **Chemical ascent** with hydrolox (Isp 450 s) propulsion, both aerobraking and propulsive Earth capture variants
- **Mass driver** electromagnetic launch from the lunar surface combined with SEP transfer for Earth-side approach

Sources sealed — Handmer's $10/kg target, Coutts-Sowers Starship cost, Metzger's Γ values, and trade-press tanker counts not consulted during derivation.

The Python derivation: [pass-02-calc.py](pass-02-calc.py). Captured stdout: [pass-02-calc-output.txt](pass-02-calc-output.txt).

## Delta-V budget

| Leg | ΔV (m/s) | Notes |
|---|---|---|
| Lunar surface to LLO | 1,870 | Lunar gravity well + ascent loss; canonical |
| LLO to trans-Earth injection | 700 | Tangential apoapsis-raise burn |
| Earth approach to LEO (propulsive) | 3,000 | Oberth-assisted at low perigee |
| Earth approach to LEO (aerobraking) | 300 | Final circularization only after atmospheric capture |
| **Total chemical, aerobraking** | **2,870** | |
| **Total chemical, no aerobraking** | **5,570** | Matches Wikipedia's 5.93 km/s within 6% |

Aerobraking saves ~2.7 km/s of propulsive ΔV at the cost of adding a heat shield and reentry-survivable structure. This is the **dominant architectural lever** — larger than the choice between methalox and hydrolox.

## Propellant mass fractions (Tsiolkovsky)

\\[ f_{\\text{prop}} = 1 - \\exp\\left(-\\frac{\\Delta v}{I_{\\text{sp}} \\cdot g_0}\\right) \\]

| Chemistry | ΔV (m/s) | f_prop |
|---|---|---|
| Hydrolox (Isp 450 s), aerobraking | 2,870 | 0.478 |
| Hydrolox (Isp 450 s), no aerobraking | 5,570 | 0.717 |
| Methalox (Isp 360 s), aerobraking | 2,870 | 0.556 |
| Methalox (Isp 360 s), no aerobraking | 5,570 | 0.794 |

At ΔV 5,570 m/s with methalox, the propellant fraction is nearly 80% — the rocket is mostly fuel and structurally inefficient. Hydrolox with aerobraking gives a manageable 48% propellant fraction.

## Cost decomposition per launch

The full cost stack per launch:

\\[ C_{\\text{launch}} = C_{\\text{prop}} \\cdot m_{\\text{prop}} + C_{\\text{hw}} \\cdot m_{\\text{dry}} + C_{\\text{ops}} \\]

Where:
- \\(C_{\\text{prop}}\\) = lunar-surface propellant cost per kg (varies by scenario + era)
- \\(m_{\\text{prop}}\\) = propellant mass per launch (Tsiolkovsky × initial mass)
- \\(C_{\\text{hw}}\\) = hardware cost per kg of vehicle dry mass per launch (build cost amortized over N reuses)
- \\(m_{\\text{dry}}\\) = vehicle dry mass (12% of propellant mass for hydrolox stage)
- \\(C_{\\text{ops}}\\) = fixed per-launch operations cost on the lunar surface

For a 10 t payload reference vehicle, the initial mass is solved iteratively because dry mass scales with propellant mass:

\\[ m_{\\text{prop}} = \\frac{f / (1-f) \\cdot m_{\\text{payload}}}{1 - f \\cdot \\rho / (1-f)} \\]

where ρ is the dry-mass-to-propellant ratio (0.12 for mature hydrolox).

## Scenario assumptions

| Variable | Aggressive-ISRU early/mid/late | Partial-ISRU early/mid/late | Earth-imports-only early/mid/late |
|---|---|---|---|
| Lunar prop cost ($/kg) | 2000 / 800 / 300 | 5000 / 2500 / 1200 | 6000 / 1500 / 600 |
| HW cost per kg dry per launch ($) | 15,000 / 5,000 / 1,500 | (same) | (same) |
| Lunar ops cost per launch ($M) | 50 / 20 / 5 | (same) | (same) |

The Earth-imports-only scenario applies a gear-ratio amplification to q1's terrestrial Earth-to-LEO cost: terrestrial L_p × ~6× to land propellant on the Moon. Early-era amplification is higher (~13×) because the Earth-to-lunar-surface pipeline is itself immature.

## Results — chemical ascent with aerobraking

| Scenario | Era | Total $/kg | Propellant | Hardware | Ops |
|---|---|---|---|---|---|
| Aggressive-ISRU | early | **$8,912** | $2,059 | $1,853 | $5,000 |
| Aggressive-ISRU | mid | **$3,441** | $824 | $618 | $2,000 |
| Aggressive-ISRU | late | **$994** | $309 | $185 | $500 |
| Partial-ISRU | early | **$12,000** | $5,147 | $1,853 | $5,000 |
| Partial-ISRU | mid | **$5,191** | $2,573 | $618 | $2,000 |
| Partial-ISRU | late | **$1,921** | $1,235 | $185 | $500 |
| Earth-imports-only | early | **$13,029** | $6,176 | $1,853 | $5,000 |
| Earth-imports-only | mid | **$4,162** | $1,544 | $618 | $2,000 |
| Earth-imports-only | late | **$1,303** | $618 | $185 | $500 |

## Results — chemical ascent, no aerobraking

| Scenario | Era | Total $/kg | Propellant | Hardware | Ops |
|---|---|---|---|---|---|
| Aggressive-ISRU | early | $18,830 | $7,279 | $6,551 | $5,000 |
| Aggressive-ISRU | mid | $7,095 | $2,912 | $2,184 | $2,000 |
| Aggressive-ISRU | late | $2,247 | $1,092 | $655 | $500 |
| Partial-ISRU | early | $29,748 | $18,197 | $6,551 | $5,000 |
| Partial-ISRU | mid | $13,282 | $9,099 | $2,184 | $2,000 |
| Partial-ISRU | late | $5,522 | $4,367 | $655 | $500 |
| Earth-imports-only | early | $33,387 | $21,836 | $6,551 | $5,000 |
| Earth-imports-only | mid | $9,643 | $5,459 | $2,184 | $2,000 |
| Earth-imports-only | late | $3,339 | $2,184 | $655 | $500 |

Without aerobraking, costs are 2–3× higher across the board. Aerobraking is the load-bearing architectural choice. Only the late-era Earth-imports-only no-aerobraking case ($3,339/kg) falls below the $5,000/kg level; every other no-aerobraking scenario (except late-era aggressive-ISRU at $2,247/kg) sits above it.

## Results — mass driver + SEP transfer

| Era | Throughput (kg/yr) | Total $/kg | Capital | Energy | SEP transfer |
|---|---|---|---|---|---|
| Early | 2.0 × 10⁷ | **$528** | $25 | $3.33 | $500 |
| Mid | 6.0 × 10⁸ | **$152** | $1 | $1.33 | $150 |
| Late | 8.5 × 10⁹ | **$50** | $0 | $0.33 | $50 |

Mass driver economics are dominated by **post-launch SEP transfer cost**, not the mass driver itself. The driver's capital amortization collapses rapidly once throughput exceeds ~10⁸ kg/yr; the energy cost is negligible at any throughput; but the SEP stage required to insert payload into LEO (from the mass-driver's ~1.6 km/s lunar departure velocity) is a separate vehicle with its own amortization.

## What the math shows

1. **Aerobraking is the dominant architectural lever.** Saves a factor of 2–3× on chemical-ascent cost. Without it, every chemical scenario through mid-era sits above $7,000/kg; late-era aggressive-ISRU ($2,247/kg) and Earth-imports-only ($3,339/kg) are the only no-aerobraking cases below $5,000/kg.

2. **Earth-imports-only is punitive in early/mid eras but converges with ISRU in late era.** This is counterintuitive but follows from the gear-ratio assumption: as terrestrial L_p drops (q1's late-era $107/kg), the lunar-delivered propellant cost drops faster than aggressive-ISRU's late-era $300/kg target. The crossover happens once Earth-to-lunar logistics become mature enough that terrestrial propellant outcompetes nascent lunar ISRU.

3. **Mass driver beats chemical in late era at scale.** At 10M t/yr throughput, mass-driver $/kg ($50) is lower than chemical-aggressive-late ($994). The gap is 20× — large enough that any infrastructure-built case would prefer the mass driver. At early-era throughput, the mass driver is competitive with chemical-aggressive-mid ($528 vs $3,441), but the bootstrap cost of getting the mass driver to the Moon (not modeled here — see q5) shifts the comparison.

4. **The architectural fan is wide.** Best case (mass driver late) to worst case (Earth-imports-only no-aerobraking early) is **$50/kg to $33,000/kg** — a factor of 660×. The choice of architecture and the maturity of the lunar economy matter far more than the choice of fuel chemistry.

5. **Mass driver becomes commercially dominant only at >10⁹ kg/yr throughput.** At Handmer's headline 10⁷ t/yr (= 10¹⁰ kg/yr), the capital amortization is essentially free. But to GET to that throughput requires a working mass driver, which costs ~$10B to install. The 20-year amortization assumption is aggressive; longer amortization at lower throughput would push the early-era $/kg up significantly.

## Industrial-explosion sensitivity (modulo TAI)

The compressible variables under sustained automation pressure are:

- **Lunar surface ops cost**: could compress 10× with full robotic operations (e.g., early-era $5,000/kg → $500/kg, saving $4,500/kg in early-era chemical scenarios)
- **ISRU propellant cost**: could compress 5× as automation drives scale economies in ice extraction + electrolysis
- **Hardware amortization**: could compress 3× as on-Moon manufacturing replaces Earth-imported parts
- **Mass driver throughput**: could rise 10× without proportional capital increase as the design is replicated and standardized

Combined effect on **chemical aggressive-ISRU late** with TAI: drops from $994/kg to roughly $150–250/kg.

Combined effect on **mass driver mid-era**: drops from $152/kg to roughly $30/kg, becoming commercially viable a decade earlier than business-as-usual.

The mass driver becomes the commercially dominant architecture under any sustained-automation scenario; under business-as-usual, chemical retains the operational advantage through 2035 simply because the mass driver requires its own multi-billion-dollar capital project to bootstrap.

## Calibration to q1 (terrestrial L_p)

q1's partial-mid Starship cost is $107/kg from Earth to LEO. q2's partial-ISRU mid case for lunar-surface to LEO is $5,191/kg — roughly **48× more expensive than terrestrial launch at the comparable era**. Under aggressive-ISRU late, the lunar-side cost is $994/kg; against q1's partial-late $107/kg that is approximately **9× more expensive**, and against q1's optimistic-late $59/kg approximately **17× more expensive**. Mass driver late ($50/kg) is comparable to optimistic-late Starship ($59/kg) — the crossover destination, within a factor of two of terrestrial parity.

This is the structural framing: lunar manufacturing competitiveness for orbital infrastructure requires either (a) a fully mature ISRU + mass driver economy in the late era, or (b) products with sufficient value density that lunar shipping cost is not the binding constraint.

## What to carry to reconcile

The reconcile sub-pass should:

1. Compare the aggressive-ISRU-late $/kg ($994/kg with aerobraking) against Coutts-Sowers's lunar-surface propellant price target ($500/kg) and Sowers's original ULA price point.
2. Compare the mass-driver-mid $/kg ($152) and mass-driver-late ($50) against Handmer's assumed $10/kg product price. Identify the gap and whether Handmer's number is achievable at his stated throughput.
3. Check whether Metzger's Γ_LEO ≈ 14 chemical / Γ_LEO ≈ 1 SEP-return values are consistent with our derived propellant mass fractions.
4. Identify whether the late-era convergence between Earth-imports-only and aggressive-ISRU is real or an artefact of the gear-ratio assumption.

## Anti-pattern check

- ✓ Sources sealed — no Handmer, Coutts-Sowers, Metzger, or trade-press numbers used in derivation
- ✓ Math shown explicitly via Python; not handwaved
- ✓ Conditional framing — three scenarios × three eras × two architectures
- ✓ Industrial-explosion sensitivity flagged separately, not as point estimate
- ✓ Voice register dry: "the math shows", not "remarkably" or "is huge"
- ⚠ The lunar-prop-cost assumptions in the Earth-imports scenario use q1's L_p × an amplification factor — this is borderline source-borrowing, but the L_p itself is q1's derived result, not a Musk/Citigroup claim, so I judge it acceptable
- ⚠ Mass driver capital cost of $10B is a thumb-in-the-air estimate; sensitivity to ±5× would shift early-era $/kg by ±$25 (still small relative to total)
- ⚠ **Codex flagged (severity high):** many load-bearing inputs (ΔV components, Isp values, dry-mass ratios, lunar prop costs, hardware $/kg/reuse, lunar ops cost, mass driver capital, SEP transfer cost) are asserted-as-priors rather than derived. Honest framing: this is **a scenario model with first-principles-justified priors**, not a from-axioms derivation. The Tsiolkovsky algebra and table arithmetic do check; the headline numbers inherit the assumption set.
- ⚠ **Codex flagged (severity high):** the chemical ascent vehicle is amortized as reusable, but its return leg to the lunar surface is not separately modeled. This understates hardware cost if the vehicle is expendable, or omits the return propellant + cycle-time cost if reusable. Both ends bias the result — flagged for reconcile pass and downstream synthesis.
- ⚠ **Codex flagged (severity high):** the SEP transfer cost ($500/$150/$50 per kg by era) is asserted, not derived from SEP Isp + ΔV + power + reusability. Since the SEP cost dominates mass-driver early-era totals, the mass-driver result is sensitive to this assumption. Flagged for source-review (Metzger's SEP architecture provides one anchor) and a possible calc v2.
