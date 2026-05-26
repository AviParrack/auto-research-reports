---
pass: 6
kind: write
leaf: q6-orbital-demand
date: 2026-05-25
status: drafting
audited: pending
---

# Orbital demand for structural mass and propellant, 2026-2040

## Why this question matters

The lunar-manufacturing thesis is, at the root, a supply-side proposition: that lunar regolith can deliver bulk mass to cislunar space more cheaply than Earth launch can. A supply story is only interesting if there is a demand story to meet it. If 2026-2040 cislunar demand is anemic — measured in thousands of tonnes per year — Earth launch alone trivially supplies it and the lunar-manufacturing thesis dies for lack of customers, not for lack of feasibility. If demand is explosive — measured in millions of tonnes per year — Earth launch capacity becomes the binding constraint and lunar-sourced bulk mass becomes structurally necessary. The q8 synthesis pivots on which of these worlds materialises, and the answer is regime-dependent in a way that no single 2040 number can capture.

## Where it fits

This leaf interlocks with three others. With q1 (Earth launch cost): launch cost determines which demand regime obtains, because demand for orbital infrastructure is highly elastic in \(L_p\), the cost-per-kg to LEO [metzger-2023-economics]. With q5 (lunar base capital buildup): the capex case for standing up lunar manufacturing is downstream of whether the LEO + cislunar market is large enough to absorb its output — synthesis-level reasoning that q6's regime decomposition supplies as input. With q2 (lunar ascent cost): the demand total here splits between a lunar-supplyable bulk-mass fraction (structure, radiators, silicon, sintered shielding) and an Earth-launch-bound compute-hardware fraction, with propellant occupying a partially lunar-derivable middle ground per q6.c8. That split governs how much of q6's headline number lunar manufacturing can actually claim.

## Headline

Projected 2026-2040 LEO + cislunar structural mass and propellant demand spans **three orders of magnitude across acceleration regimes**, not three orders of magnitude across calendar years. Under stall, cumulative 15-year demand is approximately **20,000 t** (~1,400 t/yr average), dominated by satellite servicing carry-over and demonstration-scale SDC. Under BAU, cumulative demand reaches approximately **2,150,000 t** (~143,000 t/yr), with space-based data centres (SDC) at 50 GW deployed by 2040 driving roughly **93%** of the total. Under TAI-compression, cumulative demand reaches approximately **42,900,000 t** (~2.86 Mt/yr), with SDC at 1,000 GW deployed driving roughly **93%** of the total and exceeding plausible Earth-launch throughput by approximately **an order of magnitude** [introl-2026-orbital-dc, marcy-2026-arxiv]. SBSP, propellant depots, lunar surface cargo, Mars cargo, and satellite servicing together remain 1-2 orders of magnitude below SDC across all three regimes. The regime identity — set by AI compute demand and launch cost — not the calendar year, determines feasibility. McCalip's 3.2× whole-project cost-multiple skepticism [mccalip-quote-fomo] and Handmer's 2× per-token inference premium [handmer-quote-gpus-orbit] bracket the BAU-to-TAI-C transition.

## Demand by use case

### Space-based data centres

SDC is the dominant sector under any regime that includes meaningful orbital compute deployment. The first-principles mass-intensity decomposition gives approximately **40 t/MW continuous compute** (range 30-55 t/MW), with components: 5-10 t/MW compute hardware, 15-25 t/MW solar panels (peak-to-continuous corrected at ~3×), 5-10 t/MW radiators, and 5-10 t/MW structure and station-keeping [pass-02-calc.md]. The mid-line is cross-corroborated by two independent engineering analyses, peraspera's 30-50 t/MW [peraspera-2025-orbital-compute] and luminix's 42 t/MW [luminix-2026-sdc], within ±25%.

Deployed power by 2040 spans regimes:

| Regime | GW deployed by 2040 | Mass total (15 yr) | Annual average |
|---|---:|---:|---:|
| Stall | 0.5 GW | 20,000 t | 1,333 t/yr |
| BAU | 50 GW | 2,000,000 t | 133,333 t/yr |
| TAI-C | 1,000 GW | 40,000,000 t | 2,666,667 t/yr |

The TAI-C 1,000 GW figure draws on the SpaceX/xAI January 2026 FCC filing for up to 1 million satellites projecting 100 GW, scaled by an industrial-compression factor that captures roughly half of Marcy's projected US 2035 AI demand at 100 GW [marcy-2026-arxiv, introl-2026-orbital-dc]. The BAU 50 GW figure corresponds to roughly 5% of US data centre growth captured by orbit, broadly aligned with Luminix's 30-40% viability assessment by 2032-35 partially materialising.

Cote's bandwidth-ceiling argument — that global orbital comms capacity tops out at ~500-800 Tbps versus 5-20 Tbps per ground-based DC — caps the TAI-C SDC scenario at perhaps ~200 GW rather than the 1,000 GW headline if optical inter-satellite links and training-workload routing do not mitigate it [cote-2026-orbital-dc, pickard-2026-orbital-dc]. This is a factor-of-5 sensitivity within the existing regime uncertainty rather than a regime-killer; the Codex audit (pass-03) correctly flagged that the OISL mitigation argument is not source-settled.

### Space-based solar power

SBSP mass scales approximately as **5 kg/kW at the satellite**, between Mankins's SPS-ALPHA target of ~1 kg/kW under mass production and the 2015 state-of-art of ~6.7 kg/kW [caltech-sspd-mankins-niac]. The Mankins reference point of 80,000 t for a 4 GW system anchors the calculation. By regime:

| Regime | GW deployed by 2040 | Mass total (15 yr) |
|---|---:|---:|
| Stall | 0 GW | 0 t |
| BAU | 5 GW | ~25,000 t |
| TAI-C | 100 GW | ~500,000 t |

BAU 5 GW deployment assumes strategic-autonomy demand — China's 2028 1 km array, Aetherflux's Q1 2027 launch, and 1-2 commercial GEO stations — rather than full commercial LCOE competitiveness against terrestrial solar [orbysa-2026-sbsp, spaceambition-2026-sbsp]. Confidence is medium per pass-03 audit, which flagged that BAU 5 GW is plausible-but-not-source-settled; full commercial competitiveness remains conditional on launch cost crossing the $100-200/kg threshold from NASA OTPS [nasa-otps-sbsp-2024].

### Propellant depots

Depot annual throughput scales with the number of outbound interplanetary or HLS-class Starships refuelled per year. Per Musk's 8-tanker estimate (the operational lower bound; NASA cites 16) and ~100 t/tanker payload [handmer-2025-propellant-stability, wiki-propellant-depot], each refuelled Starship consumes approximately **800 t/yr** of propellant from the depot.

| Regime | Outbound ships/yr | Depot throughput |
|---|---:|---:|
| Stall | 0 | 0 t/yr |
| BAU | 10 | 8,000-16,000 t/yr |
| TAI-C | 200 | 160,000-320,000 t/yr |

The Kornuta-Metzger 450 t/yr near-term *lunar-derived* propellant demand figure [kornuta-2019-clpa, metzger-2023-economics, ida-demand-drivers] sits as roughly 5.6% of BAU's 8,000 t/yr all-source total. The framing distinction — lunar-derived versus all-source — is the source of an apparent factor-of-18 discrepancy between Kornuta-Metzger and the BAU regime number; the two are consistent once the scope mismatch is resolved.

### Lunar surface cargo

NASA Artemis lunar surface cargo features a structural lander-capability gap: current planned capability ~1,500 kg/mission against multi-tonne mission objectives [nasa-m2m-cargo-2024]. The M2M architecture papers identify three resolution paths: develop a larger commercial cargo lander, use a Starship HLS-derived cargo variant, or rescope objectives [nasa-m2m-logistics-2025]. Post-Artemis-V annual cadence is approximately one landing per year under BAU; throughput therefore spans 1.5-100 t/yr depending on the chosen architectural path. Under TAI-C, with 5 Starship HLS cargo landings annually at full utilisation, throughput reaches ~500 t/yr — still small relative to SDC.

### Mars cargo (LEO transit, deep-space demand)

Musk's stated upper-bound trajectory — 20 / 100 / 500 missions per Mars window across 2028/29, 2030/31, and 2033 at 75-300 t each, with a 1 million-ton long-term colonisation target [musk-mars-1m-tons] — defines the envelope. Treated as aspirational rather than operational, this yields:

| Regime | Annual average |
|---|---:|
| Stall | 0 t/yr |
| BAU | 200 t/yr |
| TAI-C | 15,000 t/yr |

Each tonne of Mars-bound payload transits LEO via depot refuel, multiplying its effective propellant footprint by roughly an order of magnitude. The Mars-supply implications for depot demand are folded into the depot row above.

### Satellite servicing

OSAM market growth from $2.4B (2023) to $5.1B (2030) at 11.5% CAGR [marketsandmarkets-2026-osam] translates at $25-40 kg/$M revenue to ~50 t/yr (current) to ~200 t/yr (BAU 2030). Under TAI-C, with routine in-orbit assembly and active-debris-removal scaling, servicing could reach ~2,000 t/yr — still 1-2 orders of magnitude below SDC.

## The supply-side coupling to q1

Under TAI-C, SDC mass demand alone (~2.7 Mt/yr) exceeds plausible Earth-launch throughput by approximately an order of magnitude. The defensible upper bound on Earth-launch capacity is approximately **400,000 t/yr to LEO**, calculated as ~200 active reusable Starships × 10 flights/yr × 200 t per flight — and this is itself an aggressive parameterisation [pass-02-calc.md]. The shortfall under TAI-C is structural rather than cyclical.

The q1↔q6 demand-elasticity-cost coupling resolves as follows. Under TAI-C, lunar-sourced bulk mass — structure, radiators, sintered shielding, silicon for solar panels — covers approximately half the SDC mass budget. The other half — compute hardware (GPUs, memory, networking, PSUs) — remains Earth-launch-bound regardless, because the Moon cannot supply it. Lunar manufacturing is therefore architecturally **necessary but not sufficient** under TAI-C: it relaxes a binding supply-side constraint on the bulk-mass half, but the high-value compute half remains Earth-launch-bound. McCalip's BAU cost-critique does not directly engage with the TAI-C necessity logic; the conditional framing matters [mccalip-quote-fomo, pass-03-audit.md].

## Industry positioning

As of February 2026, the orbital data centre industry has multiple operational deployments and aggressive mega-constellation FCC filings: Starcloud-1 (60 kg, NVIDIA H100, November 2025), Axiom Space (2 nodes, January 2026), Kepler Communications (10 satellites, 300 kg each, January 2026), SpaceX/xAI's January 2026 filing for up to 1M satellites projecting 100 GW, Blue Origin's Project Sunrise for ~52,000 satellites, and Starcloud's filing for 88,000 satellites with a 5 GW hypercluster vision [introl-2026-orbital-dc, starcloud-factories-2026, bisnow-2026-bluemoon-sunrise, fortune-2026-bezos-musk]. Public-figure positions bracket a 1.6× cost-multiple range: Handmer's 2× per-token premium (profitable for SpaceX-integrated architecture), McCalip's 3.2× cost multiple (failed economics outside FOMO), Metzger's exponential-AI-conditional optimism, Bezos's "beat terrestrial cost in next couple decades" commitment via Project Sunrise [handmer-quote-gpus-orbit, mccalip-quote-fomo, metzger-quote-orbital-dc, bezos-orbital-dc-statement]. The viability range maps approximately to BAU (McCalip) versus TAI-C (Handmer, Metzger, Bezos).

## Confidence per finding

- **SDC mass intensity ~40 t/MW (q6.c1):** *high* — first-principles engineering decomposition cross-corroborated by two independent analyses
- **Three-regime demand bracket 20 kt / 2.15 Mt / 42.9 Mt over 15 years (q6.c2):** *medium-high* — the framework is robust; regime GW targets are scenario inputs, not first-principles derivations
- **SDC dominates all other sectors by >7× under BAU and TAI-C (q6.c3):** *medium-high* — robust across reasonable variation in mass-per-MW and GW-deployed assumptions
- **SBSP 5 kg/kW × 0-100 GW regime range (q6.c4):** *medium* — BAU 5 GW deployment is strategic-niche rather than commercial-LCOE; confidence downgraded per pass-03 audit
- **Propellant depot 800 t/yr per refuelled Starship (q6.c5):** *medium-high* — Musk-8 is the lower-bound architectural commit; NASA-16 doubles the figure
- **Lunar-sourced bulk mass necessary-not-sufficient under TAI-C (q6.c6):** *medium* — conditional on TAI-C demand scenario obtaining; framing not a source-settled resolution
- **Stall regime fails for lack of demand (q6.c7):** *high* — at ~1,400 t/yr Earth launch alone trivially fulfills it
- **450 t/yr Kornuta-Metzger as lunar-derived sub-segment of BAU LEO depot (q6.c8):** *medium* — the 5.6% interpretation is the author's; sources support the underlying 450 t/yr figure
- **Industry deployment census as of Feb 2026 (q6.c9):** *high* — operational filings and trade-press corroboration
- **Public-figure cost-multiple bracket 2×-3.2× (q6.c10):** *high* — direct quotes
- **Musk Mars-cadence envelope as TAI-C upper bound (q6.c11):** *medium* — aspirational, not operational
- **NASA Artemis cargo gap and resolution paths (q6.c12):** *high*
- **OSAM market $2.4B→$5.1B at 11.5% CAGR (q6.c13):** *medium*
- **Cote bandwidth ceiling ~200 GW SDC fallback (q6.c14):** *medium* — depends on OISL and training-workload assumptions not fully source-settled

## Limitations

The TAI-C demand scenario rests on three load-bearing aspirational positions: Marcy's 100 GW US AI demand projection by 2035, the SpaceX/xAI 1M-satellite FCC filing materialising at face value, and Musk's stated 1,000-ship-per-window Mars cadence by 2033. Each is plausible under industrial-compression conditions; none is operationally committed. If any of the three slips, the TAI-C regime number compresses by a factor of 2-5.

SDC and SBSP are both speculative at scale. The 2026 industry has 60-300 kg demonstration satellites, not gigawatt hyperclusters. The transition from demonstration to BAU 50 GW SDC (a factor of ~10^6 in deployed mass) requires sustained capital, regulatory clearance for mega-constellations, and demonstrated economics that cross the McCalip-Handmer cost-multiple bracket on the Handmer side. SBSP additionally requires launch cost crossing the $100-200/kg threshold.

Propellant depot demand depends on Starship reaching operational maturity for orbital refuel. As of writing this is not yet demonstrated end-to-end; the 8,000 t/yr BAU depot throughput presupposes that the architecture works.

Five of seven tier-S source PDFs were not fully parseable via WebFetch during pass-04 source review; reviewed against abstracts and secondary aggregators. Hand-extraction of primary PDFs is a future-pass action item flagged for q8 synthesis.

The q6.c6 necessary-but-not-sufficient framing is the leaf's most consequential conclusion for the report root question. It is conditional on the TAI-C scenario obtaining; under BAU the conclusion is weaker (lunar manufacturing relaxes a soft supply constraint rather than a hard one), and under stall the conclusion does not apply at all.
