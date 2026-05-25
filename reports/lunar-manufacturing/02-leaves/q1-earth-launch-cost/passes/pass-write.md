---
pass: 6
kind: write
leaf: q1-earth-launch-cost
date: 2026-05-25
status: reviewed
audited: pending
---

# Earth launch cost to LEO, 2026-2040

## Why this question matters

The root question of this report is whether lunar manufacturing becomes cheaper than Earth launch for orbital infrastructure. The cost per kilogram to deliver bulk mass from Earth to low Earth orbit — \\(L_p\\) in Metzger's competitiveness framework [metzger-2023] — is the denominator of that comparison. Every conclusion about lunar viability is conditional on a specific assumption about Earth launch cost. A projection that puts \\(L_p\\) near Musk's claimed \$10/kg target makes lunar manufacturing structurally hard; a projection that leaves \\(L_p\\) at current Falcon 9 levels (\$7,000/kg rideshare per [satbase-2026-falcon9], down to ~\$2,720/kg for dedicated launches at full payload utilisation) makes lunar comparatively easy. The leaf's job is to bound \\(L_p\\) with a defensible range.

## Where it fits

This leaf feeds three places. The gear-ratio leaf (q4) uses \\(L_p\\) as the denominator in its launch-normalized cost formulation. The lunar-ascent-cost leaf (q2) is the matched numerator that gets compared against this leaf's \\(L_p\\). The synthesis leaf (q8) consumes both as the central crossover comparison. The orbital-demand leaf (q6) interacts indirectly: aggressive demand projections usually assume cheap Starship economics, so a pessimistic q1 implies a pessimistic q6.

## Headline

A first-principles cost-per-kg model spanning three operational scenarios produces internal-cost projections of \$59-878/kg by 2030-2035, depending on Starship reuse count, refurb rate, and operational era. The partial-reuse central scenario (30 reuses, 100t payload, 15% refurb rate, \$1M ops per launch) lands at **\$107-466/kg internal cost**, with **\$215-930/kg customer list price** at a 2× margin (rising further if SpaceX retains pricing power). Musk's frequently cited \$10/kg target [musk-10kg-target] is not derivable from these assumptions without sub-2% refurb rates AND zero-margin pricing AND TAI-grade ground-ops automation. Confidence in the partial-scenario range is **medium-high**; in the optimistic floor (\$59/kg internal), **medium**; in Musk's \$10/kg target, **low — aspirational, not derivable**.

## The cost model

Starship cost per launch decomposes as:

\\[ C_{\\text{launch}} = \\frac{C_{\\text{hardware}}}{N_{\\text{reuse}}} + C_{\\text{propellant}} + r \\cdot C_{\\text{hardware}} + C_{\\text{ops}} \\]

Where \\(C_{\\text{hardware}}\\) is the build cost of the full stack (booster + ship), \\(N_{\\text{reuse}}\\) is the number of reuse cycles, \\(C_{\\text{propellant}}\\) is methalox cost per launch, \\(r\\) is the refurbishment rate as a fraction of build cost per cycle, and \\(C_{\\text{ops}}\\) is per-launch ground-handling and operations. The cost per kilogram to LEO is \\(C_{\\text{launch}} / m_{\\text{payload}}\\). Full derivation in [pass-02-calc.py](pass-02-calc.py) and [pass-02-calc.md](pass-02-calc.md).

Three published anchors constrain the parameters. The Shotwell 2017 statement [shotwell-2017-refurb] put refurbishment at "substantially less than half" of new-build cost when Falcon 9 was first reused; this is the upper bound on \\(r\\), consistent with the 30% early-era assumption. The B1076 milestone in March 2026 [b1076-34-reuses-2026] demonstrates 34 reuses on a single Falcon 9 first stage, which validates the partial scenario's 30-reuse count as operationally achievable. SatBase's February 2026 pricing review [satbase-2026-falcon9] anchors the current customer-facing price at \$7,000/kg rideshare and \$74M dedicated, with explicit SpaceX guidance that rideshare rates will rise \$500/kg/year structurally.

## Three operational scenarios

| Scenario | Reuses | Payload | Refurb era | Internal \$/kg | List \$/kg (calc + 2x margin) |
|---|---|---|---|---|---|
| Optimistic | 100 | 150t | 8% late | \$59-277 | \$120-555 |
| Partial | 30 | 100t | 15% mid | \$107-466 | \$215-930 |
| Pessimistic | 10 | 50t | 30% early | \$194-878 | \$390-1,755 |

The dominant variable is the refurbishment rate, not hardware amortization. At 30+ reuses, the per-launch hardware contribution drops to ~\$3M (\$30/kg on 100t payload). Refurbishment at 15% of build cost contributes ~\$13.5M per launch (\$135/kg) — roughly four times the hardware amortization. To break below \$100/kg internal cost requires refurbishment compression to under 5% of build cost.

## Comparing first-principles to public projections

The Citigroup 2040 forecast cites \$100/kg to LEO as the operator cost target. This sits inside the optimistic-late corner of the calc envelope. The wccftech-reported alternative projection of \$1,600/kg full-reuse early Starship dropping to \$100-150/kg long-term [musk-10kg-target] follows the same arc through the partial scenario into the optimistic floor. Both are consistent with the framework when read as moderate-bullish industry estimates.

Musk's \$10/kg target falls outside the calc envelope for any era-and-scenario combination. The arithmetic Musk himself supplies (\$10/kg total with propellant at one-third ≈ \$3.33/kg) implies hardware fully amortized to ~\$0/launch and ops cost under \$100k/launch, both of which require operational compression beyond Falcon 9 historical scaling. Under industrial-explosion-grade automation pressure (refurb labor compressing tenfold, cadence rising tenfold, ground-ops compressing fivefold), the internal-cost figure could approach \$15-25/kg. Customer pricing at \$10/kg additionally requires zero or negative margin during a market-capture phase.

## Trade-press evidence versus engineering projections

A counter-anchor to the bullish projections: SatBase documents that 2026 Falcon 9 rideshare prices are *rising* at \$500/kg/year, with SpaceX publicly attributing this to inflation, capacity constraints, and structural pricing policy [satbase-2026-falcon9]. Two readings reconcile this with optimistic Starship projections:

- **Sharp transition reading:** Falcon 9 list prices stay elevated through 2028-2029, then drop sharply when Starship enters commercial service at scale below Falcon 9 marginal cost. The cited \$1,600/kg early-Starship figure anchors the post-transition price level.
- **Operational ceiling reading:** Starship operates at the partial-or-pessimistic scenario through 2040, never achieves the cadence required for substantial cost compression, and market prices stabilize at current Falcon 9 levels plus inflation.

Both readings remain compatible with the calc framework. Distinguishing them empirically requires watching the operational trajectory of Starship through 2027-2029 — payload throughput, reliability metrics, refurb cycle time.

## Industrial-explosion sensitivity

The compressible variables under sustained automation pressure are refurbishment labor, launch cadence, and ground-operations cost. Each could compress 5-10× under TAI-grade conditions, dropping the optimistic-scenario internal cost from \$59/kg to \$15-25/kg. Musk's \$10/kg target sits just beyond this compressed envelope and requires either zero-margin pricing or sub-2% refurb — both achievable under the most aggressive industrial-explosion conditions. The point estimate becomes less meaningful than the bracket: the cost trajectory is highly sensitive to non-linear automation effects, so any single \$/kg projection should be read as conditional on the assumed acceleration regime.

## Confidence

- Cost-decomposition formula and Tsiolkovsky-anchored payload mathematics: **high** — physics and aerospace finance fundamentals
- Refurb-rate range (30/15/8%): **medium** — anchored by Shotwell 2017 only at the upper end; mid- and late-era figures are extrapolation
- Reuse-count scenarios (10/30/100): **medium-high** — partial scenario directly demonstrated by B1076; optimistic 100 is unevidenced extrapolation
- Customer-facing list price projection: **medium** — depends on margin assumption (2-3×) which itself depends on competitive dynamics
- Trajectory through 2040: **low-to-medium** — sharp-transition versus operational-ceiling readings remain unresolved empirically

## Limitations

The calc uses Falcon 9-anchored assumptions to project Starship economics. Starship is a different vehicle architecture with full-system reuse (booster + ship), heat-shield wear, methalox propellant, and tower-catch recovery. Specific quantitative predictions about Starship-specific operational behavior require Starship-specific data once it operates at scale. Citigroup's 2040 figure was not directly fetched from the primary BusinessWire source; the citation here is secondhand. The reasonable next-pass action is to fetch the primary source and extract the analyst assumption set.

Margin assumptions (2-3× from internal cost to list price) reflect typical aerospace economics. Under a SpaceX-internal-use-only regime (Starship launching only SpaceX payloads), the relevant cost is internal; under a SpaceX-as-launch-provider regime, it's list price. The question of which regime persists into the 2030s is itself uncertain.
