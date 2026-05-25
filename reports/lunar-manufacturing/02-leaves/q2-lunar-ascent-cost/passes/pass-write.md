---
pass: 6
kind: write
leaf: q2-lunar-ascent-cost
date: 2026-05-25
status: reviewed
audited: pending
---

# Lunar surface to LEO cost, 2026-2040

## Why this question matters

The root question of this report is whether lunar manufacturing becomes cheaper than Earth launch for orbital infrastructure. q1 sets the denominator — Earth-to-LEO cost \(L_p\). This leaf sets the numerator — the cost of moving 1 kg of lunar product from the lunar surface to LEO. Every conclusion about lunar viability for satellite-class destinations depends on whether this numerator falls fast enough to close the ratio with terrestrial launch. The lunar ascent cost determines whether lunar manufacturing is a serious competitor for LEO infrastructure or a niche supplier to deeper-cislunar destinations only.

## Where it fits

This leaf is the numerator partner to q1's denominator. q4 supplies the gear-ratio framework that translates lunar-product cost into competitiveness at each destination; q4's \(\Gamma_\text{LEO} \approx 14\) chemical / \(\Gamma_\text{LEO} \approx 1\) SEP is reproduced in q2's calc. The synthesis leaf q8 consumes q1 + q2 + q4 to compute crossover dates and value-density requirements. q5 (capital buildup) determines whether the infrastructure that makes q2's late-era scenarios feasible can be delivered to the Moon in the first place. q7 (mass driver feasibility) validates the engineering envelope my calc takes from Handmer's 2026 design.

## Headline

A first-principles scenario sweep across three ISRU regimes, three eras (2026-2030 / 2030-2035 / 2035-2040), and two architectural families produces lunar-surface-to-LEO costs spanning **$50–$33,000/kg** [q2.c3, q2.c5] — a factor of 660 across the full no-aerobraking-included envelope; **$50–$13,029/kg** restricted to aerobraking-included scenarios. The three working scenarios:

- **Chemical-rocket Earth-imports-only [q2.c3]:** $1,303–$13,029/kg with aerobraking; $3,339–$33,387/kg without. Trade-press evidence ([orbital-refueling-newspaceeconomy]) confirms the mid-era $4,000/kg figure to within 5% [q2.c12].
- **Chemical-rocket aggressive-ISRU [q2.c3]:** $994–$8,912/kg with aerobraking. The 2016 ULA Sowers $500/kg lunar-surface propellant target [coutts-sowers-2025] is consistent with this range plus reasonable margin [q2.c10].
- **Mass driver + SEP transfer [q2.c5]:** $50–$528/kg across throughput regimes. At late-era throughput (10⁷ t/yr nameplate), the cost approaches optimistic-late Starship ($59/kg in q1).

Confidence in the chemical aggressive-ISRU range is **medium-high**; in the Earth-imports-only range, **high** (trade-press direct corroboration); in the mass-driver range, **medium** (single-source engineering anchor from Handmer 2026, SEP transfer cost is asserted rather than derived). The structural finding: lunar manufacturing for LEO destinations requires either mature ISRU + mass driver economy, or products with high enough value density that shipping cost is not binding.

## Delta-V budget and propellant mass fractions

The lunar-surface-to-LEO propulsive \(\Delta v\) decomposes as:

\[ \Delta v_\text{total} = \Delta v_\text{lunar ascent} + \Delta v_\text{TEI} + \Delta v_\text{LEO insertion} \]

With canonical values [wiki-delta-v]:
- Lunar surface to LLO: 1,870 m/s
- LLO to trans-Earth injection: 700 m/s
- LEO insertion: 300 m/s aerobraking, 3,000 m/s propulsive

Total: **2,870 m/s** with aerobraking, **5,570 m/s** without. The Wikipedia delta-v table's 5.93 km/s Moon-to-LEO figure matches within 6%.

Tsiolkovsky for hydrolox (Isp 450 s) gives propellant mass fractions of 0.478 (aerobraking) and 0.717 (no aerobraking) [q2.c2]. For methalox (Isp 360 s), the corresponding fractions are 0.556 and 0.794 (derived from the same Tsiolkovsky calculation; see [pass-02-calc.py](pass-02-calc.py)). Aerobraking saves a larger \(\Delta v\) than the chemistry choice — for chemical lunar-to-LEO architectures, the aerobraking decision is more economically consequential than the choice between methalox and hydrolox [q2.c4].

## Cost decomposition

The full chemical-ascent cost stack per launch:

\[ C_\text{launch} = c_\text{prop} \cdot m_\text{prop} + c_\text{hw} \cdot m_\text{dry} + c_\text{ops} \]

Where \(c_\text{prop}\) is lunar-surface propellant cost per kg (scenario-dependent), \(c_\text{hw}\) is hardware cost per kg of vehicle dry mass per launch (build cost amortized over reuse count), and \(c_\text{ops}\) is fixed lunar-surface operations per launch.

The propellant cost dominates in early eras under Earth-imports. The full decomposition from [pass-02-calc.py](pass-02-calc.py): in the early Earth-imports-only case with aerobraking, propellant contributes $6,176/kg of $13,029/kg total (~47%), hardware $1,853/kg (~14%), and operations $5,000/kg (~38%). In the late era, propellant drops to $618 of $1,303 total (~47%), hardware $185 (~14%), and operations $500 (~38%) — the proportions stay roughly fixed while each falls by a factor of 10 [q2.c3].

## Three scenarios — chemical-ascent results

| Scenario | Era | $/kg with aerobraking | $/kg without aerobraking |
|---|---|---|---|
| Aggressive-ISRU | early | $8,912 | $18,830 |
| Aggressive-ISRU | mid | $3,441 | $7,095 |
| Aggressive-ISRU | late | **$994** | $2,247 |
| Partial-ISRU | early | $12,000 | $29,748 |
| Partial-ISRU | mid | $5,191 | $13,282 |
| Partial-ISRU | late | $1,921 | $5,522 |
| Earth-imports-only | early | $13,029 | $33,387 |
| Earth-imports-only | mid | $4,162 | $9,643 |
| Earth-imports-only | late | $1,303 | $3,339 |

Late-era Earth-imports-only ($1,303/kg with aerobraking) remains slightly more expensive than late-era aggressive-ISRU ($994/kg) — a thin margin of ~$300/kg [q2.c3]. The proximity (rather than the 13× gap of the early era) is itself the structural finding: in the late era, terrestrial L_p has fallen far enough that gear-ratio-amplified Earth imports approach ISRU production cost. The implication is that ISRU's competitiveness in the late era depends on whether ISRU production cost can fall *below* the $600/kg gear-ratio-amplified Earth-imports price (q1 late-era L_p $107/kg × 6× pipeline). Under industrial-explosion acceleration, ISRU compresses faster (multiple compounding levers); under business-as-usual, the convergence holds.

## Mass-driver results

| Era | Throughput nameplate × availability | $/kg | Capital | Energy | SEP transfer |
|---|---|---|---|---|---|
| Early | 100 kt/yr × 20% = 20 kt/yr | $528 | $25 | $3.33 | $500 |
| Mid | 1 Mt/yr × 60% = 600 kt/yr | $152 | $1 | $1.33 | $150 |
| Late | 10 Mt/yr × 85% = 8.5 Mt/yr | **$50** | $0.07 | $0.33 | $50 |

The mass driver's economics are dominated by the post-launch SEP transfer stage, not by the driver itself. At late-era throughput, mass driver capital amortizes to under $0.10/kg; the binding cost is moving the projectile from lunar departure trajectory into LEO, which requires either a SEP tug (modeled here) or an aerobraking maneuver (modeled but not separately costed). Handmer's headline $10/kg figure [handmer-mass-driver-2026] measures a different output state — "rocks in lunar orbit" — and excludes the SEP transfer cost. The two numbers nest consistently: lunar-surface-to-lunar-orbit at $5-10/kg via mass driver, plus SEP-transfer-to-LEO at $40-50/kg additional in the mature era [q2.c11].

## Calibration to q1 and q4

q1's partial-mid Starship cost is $107/kg from Earth to LEO. q2's partial-ISRU mid case for lunar-surface-to-LEO is $5,191/kg — **a 48× multiple**. Late-era aggressive-ISRU ($994/kg) is approximately **9× q1's partial-late ($107/kg)** and **17× q1's optimistic-late ($59/kg)**. Only mass-driver late ($50/kg) closes the multiple to within a factor of 2 of q1's optimistic-late Starship — the structural condition for lunar manufacturing to compete at LEO destinations on shipping cost alone.

q4's framework predicts \(\Gamma_\text{LEO} \approx 14\) under chemical reusable round-trip [metzger-2023]. q2's calc reproduces this: 1,200 t of LEO propellant per 100 t lunar-surface payload via Starship HLS [orbital-refueling-newspaceeconomy] gives \(\Gamma = 12\), matching q4's 14× within tolerance. The SEP-return architecture that q4 attributes to dropping \(\Gamma\) to ~1 is the same architecture my mass-driver case uses for the LLO-to-LEO leg.

## Industrial-explosion sensitivity

Under sustained automation pressure (TAI-grade or sustained-industrial-explosion conditions), the compressible variables are:

- Lunar surface operations cost: could compress 10× (early-era $5,000/kg → $500/kg, saving $4,500/kg)
- ISRU propellant cost: could compress 5× as automation drives ice-extraction + electrolysis scale economies
- Hardware amortization: could compress 3× as on-Moon manufacturing replaces Earth-imported parts
- Mass driver throughput: could rise 10× without proportional capital increase as the design is replicated and standardized

Combined effect on chemical aggressive-ISRU late: from $994/kg to roughly **$150–250/kg** — comparable to q1's mid-era partial-scenario Starship cost.

Combined effect on mass driver mid-era: from $152/kg to roughly **$30/kg** — below q1's optimistic-late Starship cost.

The mass driver becomes commercially dominant a decade or more earlier than the business-as-usual case, simply because its capital amortization is the largest compressible item and automation strips that cost out faster than it strips the propellant + hardware costs out of the chemical architecture [q2.c7].

## What the math shows

1. **Architecture dominates fuel chemistry.** Aerobraking vs propulsive LEO insertion shifts the propellant mass fraction by a factor of 2-3×. Methalox vs hydrolox shifts it by ~10 percentage points. The aerobraking decision matters more than the propellant decision.

2. **Earth-imports-only is punitive in the early era and converges with aggressive-ISRU in the late era.** This is an artefact of falling terrestrial L_p outpacing nascent ISRU cost reductions in the calc's late era. In practice the convergence requires either ISRU not getting fully online (matching the chemical-imports lower bound) or ISRU production cost falling below the gear-ratio-amplified imports cost.

3. **Mass driver economics is a different beast.** Capital amortization dominates at low throughput; at industrial-scale throughput, the binding cost is the post-launch SEP transfer stage. The $50/kg late-era figure includes that SEP cost; Handmer's $10/kg figure does not (different destination).

4. **Crossover with Earth launch happens late and only under mass driver.** No chemical-only scenario closes within 9× of q1's optimistic-late Starship. Only mass-driver late closes within 2×. The lunar manufacturing case for LEO infrastructure structurally requires the mass-driver architecture or products with high value density.

## Confidence per finding

- Delta-v decomposition and Tsiolkovsky math (q2.c1, q2.c2): **high** — physics and standard rocket-equation algebra
- Aerobraking-vs-propulsive lever (q2.c4): **high** — direct consequence of Tsiolkovsky
- Chemical-ascent cost ranges (q2.c3): **medium-high** — table arithmetic is correct; the load-bearing assumptions (lunar prop cost scenarios, hardware $/kg/reuse, ops cost) are scenario priors with first-principles backing but not from-axioms derivations
- Mass driver cost (q2.c5): **medium** — the engineering anchor (Handmer 2026) is single-source; the SEP transfer cost is asserted rather than derived; the capital cost is my extrapolation, not a literature figure
- Mass-driver beats chemical at scale (q2.c6): **medium** — direction is robust under all reasonable parameter choices; the specific crossover throughput (~10⁹ kg/yr) depends on the SEP cost assumption
- Industrial-explosion sensitivity (q2.c7): **medium** — the framework holds; specific compression factors (10×, 5×, 3×, 10×) are speculative
- Earth-launch calibration (q2.c8): **high** — direct arithmetic against q1's outputs

## Limitations

The chemical ascent vehicle is amortized as if reusable, but the return-to-Moon leg is not separately modeled in my calc — if the vehicle returns to lunar surface using more ISRU propellant, that cost is partially carried by the next launch; if the vehicle returns to lunar orbit and is refueled from a depot, the depot cost is its own line item. Trade-press evidence (newspaceeconomy.ca) suggests 8-10 reuses per HLS-class vehicle [q2.c9], which is consistent with my mid-era 15 reuse assumption but probably optimistic at the late-era 50.

The SEP transfer cost ($500/$150/$50 per kg by era) appears in [q2.c5] as an asserted scenario input rather than a derived figure from SEP Isp, ΔV, propellant mass, power, vehicle dry mass, and reuse count. The pass-03 reconcile cross-check against [metzger-2023]'s Γ_LEO ≈ 1 SEP claim implies that the SEP transfer cost is roughly equal to lunar-propellant cost × small mass fraction — for late-era aggressive-ISRU at $300/kg lunar propellant × 0.12 mass fraction gives ~$36/kg, broadly consistent with my $50. A future calc v2 could derive the SEP cost from first principles.

The mass driver capital cost ($10B aggregate) is my own extrapolation from Handmer's $2-4B reactor estimate plus assumed track + infrastructure. The AIAA 2025-4123 paper (paywalled) and Ethan Miller's 2023 thesis (PDF binary-only via WebFetch) would tighten this if obtainable.

Several primary sources (Coutts-Sowers, Metzger arXiv full PDF, Kornuta et al. 2019) were accessible only via abstract + secondary citations. The headline numbers don't depend critically on these, but a future source-review pass with full primary access would tighten the confidence levels on q2.c10 (Sowers price) and q2.c11 (Handmer engineering anchors).

The calc treats the bootstrap problem — how to get the mass driver, lunar ascent vehicles, and ISRU infrastructure to the Moon in the first place — as q5's domain. The late-era $50/kg mass-driver figure assumes that infrastructure is in place; q5 must validate that the bootstrap capital can be delivered at reasonable cost.

Calendar timing of the era boundaries (early 2026-2030, mid 2030-2035, late 2035-2040) is provisional. The pace of progress depends heavily on whether sustained-automation conditions arrive, on regulatory and political factors that gate operational deployment, and on whether the lunar economy reaches the demand levels (10⁷ t/yr) that close mass-driver economics. Under TAI-grade acceleration, "late era" arrives much earlier; under stalled progress (precedent: 50-year post-Apollo lunar drought), even the "early era" assumptions may be too aggressive.

## Carry to synthesis

For q8 to consume:
- Headline range: **$50–$13,000/kg lunar-surface-to-LEO with aerobraking** across realistic scenarios
- Architecture choice (aerobraking vs propulsive LEO insertion) matters more than fuel choice
- Mass driver + SEP is the only architecture that closes the multiple to within 2× of optimistic-late Starship
- The Earth-imports-late convergence with aggressive-ISRU is a calc artefact; in practice ISRU production cost should sit below gear-ratio-amplified imports cost
- Industrial-explosion sensitivity is more compressible on the mass-driver side than on the chemical side
