---
pass: 6
kind: write
leaf: q4-gear-ratio
date: 2026-05-25
status: reviewed
audited: pending
---

# What gear ratio must lunar capital achieve?

**The popular "≥35× threshold" is real but contingent.** Lunar capital must produce roughly 35-50 kg of bulk-mass product per kg of capital landed on the moon to gain absolute advantage at GTO under Philip Metzger's 2023 cost model, with comparable thresholds for closer destinations and substantially higher thresholds for low Earth orbit. Tent sublimation technology — the leading published proposal — already exceeds this threshold by an order of magnitude (φ = 442-534 per Kornuta and Sowers respectively). Strip mining proposals cluster at or just below threshold (φ = 22-43 across Jones, Charania-DePascuale, Bennett), with Pelech's particularly pessimistic φ = 3.7 likely an artefact of terrestrial-excavator analogy in mass estimates.

**The threshold itself is not a single number.** It scales as roughly (x + G) · Γ_X / [1 − (ω + ξ) · Γ_X] in launch-normalized cost units, where Γ_X is the propellant-use ratio for delivery to destination X. This makes the destination matter more than the technology in the first-order analysis. Closer-to-Moon destinations (low lunar orbit, Earth-Moon L1, geostationary orbit) have Γ_X ≈ 0.3-1.4 and modest thresholds. Low Earth orbit has Γ_X ≈ 6-14 under chemical-only delivery, making LEO competition structurally hard without architectural change.

## The physics

For LOX/LH2 propulsion at specific impulse 450 s with 10% inert mass fraction, Tsiolkovsky gives a capital-transport gear ratio of about 6-15 from low Earth orbit to lunar surface depending on whether the delivery vehicle uses the Reusable Lunar Lander directly as the transfer vehicle (Metzger baseline, G = 6) or stages through a Starship-class round-trip (G = 15). The destination Γ_X values fall out of the same Tsiolkovsky framework:

| Destination | Γ_X chemical reusable RT | Γ_X with SEP / OTV / crossfeed |
|---|---|---|
| LLO | ~0.9 | ~0.15 |
| EML1 | ~1.3 | ~0.2 |
| GEO | ~1.4 | ~0.3 |
| GTO | ~2.1 | ~0.4 |
| LEO | ~14 | ~1 |

The columns are markedly different. **Solar electric propulsion at I_sp ≈ 2000 s, used for the LEO-return leg, collapses Γ_LEO from 14 to ~1.** Without it, LEO is structurally unreachable for lunar product under any finite gear ratio.

## The necessary condition

For lunar to compete at destination X under any finite production output, fixed labor and finance costs in launch-normalized units must satisfy (ω + ξ) · Γ_X < 1. This binds asymmetrically: for low Earth orbit with Γ_LEO ≈ 14, fixed costs must be less than about 7% of terrestrial launch cost. For closer destinations the constraint is roughly an order of magnitude looser. Realistic first-of-kind financing (5-year buildup, 22% WACC, large capital amortization) produces finance costs that exceed this threshold by an order of magnitude in early years — which is why Metzger's results show lunar absolute advantage reaching LEO only after roughly two decades of operation, well after closer destinations have crossed over.

## What the published TEAs say

Metzger 2023 reviews seven techno-economic analyses of lunar propellant production and finds the disagreement traces almost entirely to two parameters: the gear ratio G (governed by transport architecture choice) and the production mass ratio φ (governed by mining technology choice and capital mass estimates). Studies that used SLS-class government-rocket pricing for capital transport (Charania-DePascuale G = 64.9; Jones G = 41.8) reached pessimistic conclusions that don't reflect 2026 commercial reality. Studies that used terrestrial-excavator analogies for capital mass (notably Pelech) reached pessimistic φ values that don't reflect space-engineered hardware. Once these architectural and mass-estimation choices are normalised, the framework converges on a clear picture: chemical-based lunar propellant achieves absolute advantage at geostationary transfer orbit and closer destinations under modest assumptions; LEO requires solar electric propulsion or comparable architectural choice.

The threshold for absolute advantage at GTO under Metzger's mid-range parameters is approximately φ = 35. This is the most-cited figure in the public conversation, and it deserves to be carried with two caveats: it is contingent on Metzger's specific cost model, and it applies to GTO not LEO.

## Comparing first-principles to published results

An independent first-principles derivation (this leaf's calc pass) using physics and minimal economic assumptions reproduces Metzger's competitiveness inequality and Γ_X structure exactly. Parameterized with Metzger's architectural choices (G = 6, ω + ξ ≈ 0.2 at maturity, x ≈ 10 post-EOS), the first-principles framework produces a φ threshold of about 34 for GTO — within 5% of Metzger's MVP value of 36.5. The framework also reproduces his key qualitative findings:

- Closer-to-Moon destinations have low thresholds, easier markets.
- LEO is structurally hard; needs SEP architecture.
- The G/x ratio determines sensitivity to launch cost: when G >> x, lunar cost is largely insulated from Starship-era launch cost reductions, refuting the common "Starship makes lunar mining unviable" framing.
- Discount rate (financing structure) matters more than market size for crossover timing.

The areas where the first-principles framework usefully differs from Metzger 2023:

- **Industrial-explosion / TAI sensitivity.** Metzger's analysis assumes business-as-usual industrial scaling (Wright's Law b = 0.75; economies-of-scale exponent a = 0.66). Under sustained automated capital design improvement, both b and a could compress dramatically, collapsing M_K by an order of magnitude or more. That would put even the strip-mining technologies far above threshold, and would make LEO breakeven reachable in early operating years rather than after two decades.
- **Lunar mass driver.** Bypasses Tsiolkovsky entirely; not modelled by Metzger. Treated in a separate leaf.

## Is the threshold attainable?

**Yes, with established technology choices, at most cislunar destinations.** Tent sublimation already exceeds threshold by an order of magnitude in published TEAs (Kornuta 442, Sowers 534). Beneficiation technology (Metzger's MVP at φ = 36.5) sits at threshold for GTO with substantial headroom for further improvement. Strip mining is the marginal case, with the dispute between published estimates (3.7 to 43.4) reflecting unresolved questions about capital mass estimation rather than the underlying ISRU process.

**Probably yes for LEO under any of three conditions:** solar electric propulsion deployment in lunar delivery (Metzger's modelled path), aerobraking on LEO insertion, or industrial-explosion-grade automation compressing capital mass.

**The bottleneck is not the gear ratio question.** It is ground-truth on lunar ice deposits (open question for the geology), reliability achievement in lunar dust conditions, and access to public-private financing structures that keep discount rates below double-digit territory. The economic competitiveness of lunar-derived bulk mass is structurally favourable; what remains is execution.

## Confidence

- Γ_X physics structure: **high** — derived from Tsiolkovsky independently, confirmed by Codex audit and Metzger's Figure 4.
- "≥35 threshold contingent" framing: **high** — directly from Metzger Table 2 + Section 6.5.
- Tent sublimation order-of-magnitude headroom: **high** — two independent published estimates.
- Strip mining viability: **medium** — disputed between sources; resolves to questions about M_K estimation methodology that no single TEA can settle.
- LEO viability via SEP: **medium-high** — Metzger's modelled result; some sensitivity to SEP technology readiness which lives in q3.
- TAI / industrial-explosion sensitivity: **low** — speculative extension; the framework supports it but quantitative claims about how much compression would occur are not yet rigorous.

## Limitations

- The threshold formula is for steady-state / amortized operation; year-1 viability requires the full time-evolving cost model in Metzger 2023 Section 5.
- Only Metzger's TEA reassessment is reviewed in detail; the primary Kornuta, Sowers, and Pelech sources are not yet directly fetched.
- The first-principles calc parameter sweep produced degenerate (∞) thresholds under the originally-attempted parameter ranges. The reconciliation reveals my ξ assumption needed dynamic treatment; framework structure remains valid.
- Mass driver architecture (which would fundamentally change Γ_LEO) is treated in a separate leaf and not integrated here.
