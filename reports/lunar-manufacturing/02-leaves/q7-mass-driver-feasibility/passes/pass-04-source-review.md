---
pass: 4
kind: source-review
leaf: q7-mass-driver-feasibility
date: 2026-05-25
status: done
---

# Pass 4 — Source Review (tier-stratified)

Per-tier review depth: Tier S full claim-by-claim, Tier A medium, Tier B per-figure quote review, Tier C/D scalar, Tier E not reviewed. Eighteen extracts reviewed; one (Tier S Acta Astronautica 1980) was not fully fetched and is reviewed at the bibliographic-anchor level.

## Tier S — full claim-by-claim review

### wright-kuznetsov-kloesel-2011 (Tier S)

The 2011 IEEE / NASA peer-reviewed reanalysis is the load-bearing modern primary source for the q7 BAU pessimism.

| Claim | Quote | Verdict | Reasoning |
|---|---|---|---|
| velocity-budget | "Velocity required to reach L2 is 2.53 km/sec from the equatorial site near 33.10° E longitude" | Consistent | q7.c1's 2.4 km/s escape is for direct cislunar; Wright's 2.53 km/s to L2 includes the boost to L2. Compatible — different mission profiles. |
| energy-per-shot | "E = ½(2 kg)(2.53 km/s)² = 6.40 MJ × 3 (33% efficiency) = 19.2 MJ" | Consistent | q7 kinetic-energy derivation matches at matched parameters. The 33% net efficiency is q7's Wright-anchored midpoint. |
| efficiency-decomposition | "33% total efficiency, decomposed as ~50% motor + ~66% power conversion + remaining losses; SCR packaging mass dominates" (Wright extract verbatim) | Consistent | The extract gives the decomposition as ~50% motor + ~66% power conversion + remaining losses, yielding 33% net. Per Codex pass-4 audit, an earlier draft of this row misquoted as "~7% power conversion" — corrected. Wright's net 33% remains the TRL-grounded anchor regardless of the per-stage decomposition. |
| flywheel-storage | "Assuming 20 kW of the AFSPSS were dedicated for LEML launch, it would take 16 minutes... to store the energy" | Novel supporting | Wright's flywheel approach (vs q7's capacitor bank approach) is an alternative pulsed-power architecture not derived in q7. Adds an option not in q7's calc; flag for future consideration. |
| earth-construction-dependency | "Initial LEML construction will not depend on ISRU, i.e., will require materials and equipment from earth" | Novel supporting | This is the key assumption that makes Wright's negative cost-benefit valid: BAU realistically assumes Earth-built construction, which is what q7's "lunar construction multiplier" partially captures. Wright is *more* pessimistic than q7's BAU because Wright doesn't allow any ISRU offset. |
| negative-verdict | "The conclusion, however, is not as favorable for LEML as originally suggested" | Consistent | Wright's negative cost-benefit conclusion aligns with q7's BAU pessimism. The load-bearing modern primary source. |

**Summary:**

| Verdict | Count |
|---|---|
| Consistent | 4 |
| Different conclusion | 0 |
| Novel supporting | 2 |
| Merits investigation | 0 |
| Not relevant | 0 |

**Overall**: Wright et al. 2011 is the strongest single source supporting q7's BAU pessimism and the strongest counter-evidence to the 1979 NASA SP-428 optimism. Critical for the report's synthesis.

### nasa-mass-drivers-iii-1979 (Tier S)

| Claim | Quote | Verdict | Reasoning |
|---|---|---|---|
| design-target | "10.5 kg payloads at 4 Hz launch frequency, 2,400 m/sec velocity, and 10,000 m/sec² acceleration" | Consistent | q7's kinematic derivation reproduces these parameters at identical inputs. |
| length-and-power | "488-meter total length and required 125 megawatts of power" | Consistent | At 42 kg/s × 2400 m/s, kinetic power = 121 MW; SP-428's 125 MW matches within 4%, accounting for storage and recovery overhead. |
| claimed-efficiency | "96.4% efficiency" | Merits investigation | This is the load-bearing 1979 number whose interpretation determines whether modern systems can match historical projection. q7 treats it as electromagnetic-conversion-only; SP-428 calls it system efficiency. Per Codex pass-3 audit, my interpretation is inference, not source-supported. Worth a dedicated re-extraction. |
| system-mass | "Total: 3,130,000 kg" | Novel supporting | The 1979 system mass is 3,130 tonnes (3.13 Mt-mass = 3.13 × 10⁶ kg; per Codex pass-4 audit my earlier shorthand "3.13 Mt" was ambiguous between metric tons and millions of tonnes — the value is 3,130 metric tons). At $1000/kg lunar-surface-shipping × 3.13 × 10⁶ kg = $3.13B Earth-launch cost alone — exactly matching the 1979 $3.137B figure, which strongly suggests the 1979 capital projection assumed effectively zero net launch cost (a TAI-grade-effective assumption). |
| capital-cost | "Required $3.137 billion (1979 dollars)" | Different conclusion | 1979 $3.137B vs q7 BAU $1,242B is a 100× disagreement at face value. Inflated to 2026, the 1979 figure is ~$13B — close to q7's TAI-grade compressed number. This is the structural q7 finding: 1979's projection was a TAI-grade-equivalent that BAU did not realize. |
| scr-bottleneck | "Current devices carried package masses from 50 to more than 1000 times heavier than the silicon wafer masses" | Consistent | q7's discussion of pulsed-power as a binding engineering subsystem aligns with SP-428's identification of SCR mass as the dominant constraint of its era. |
| operational-target | "Baseline scenario projected operational capability by mid-1985... not met" | Consistent (historical record) | The 1985 target was not met; q7's BAU framing acknowledges this. |

**Summary:**

| Verdict | Count |
|---|---|
| Consistent | 4 |
| Different conclusion | 1 |
| Novel supporting | 1 |
| Merits investigation | 1 |
| Not relevant | 0 |

**Overall**: NASA SP-428 1979 is the canonical historical reference. The structural disagreement on capital cost ($3.137B 1979 vs $1.24T BAU 2026) is fully attributable to the engineering-compression assumptions, but the *reason* the 1979 compression did not materialize is a question SP-428 itself does not address.

### oneill-kolm-acta-1980 (Tier S)

Bibliographic anchor only; full PDF not fetched in this session.

| Claim | Verdict | Reasoning |
|---|---|---|
| primary-publication-bibliographic | Consistent | Acta Astronautica 7(11): 1229-1238, November 1980 — peer-reviewed primary canonical source confirmed via O'Neill Wikipedia and SP-428 cross-reference. |
| mass-driver-1-prototype | Consistent | MD-1 33g / 40 m/s prototype documented across multiple corroborating sources. |
| mass-driver-2-progression | Novel supporting | MD-2 design at 500 g, achieved 5000 m/s² and 112 m/s — the historical trajectory anchor. |

**Overall**: Tier-S bibliographic anchor confirmed; deeper review awaits PDF fetch in a future iteration.

### pearson-lunar-elevator-2005 (Tier S)

The canonical alternative architecture; NIAC Phase II final report.

| Claim | Quote | Verdict | Reasoning |
|---|---|---|---|
| feasibility-verdict | "Technically feasible within the prevailing state of the art using existing commercially available materials" | Novel supporting | Establishes that a non-mass-driver path exists for the same mission. q7's c13 captures this. |
| material | "Commercially available mass-produced high-strength para-aramid fibres (such as Kevlar and M5 fiber)" — carbon nanotubes NOT required | Novel supporting | Material specification matters: M5 fiber is real-world deployable. |
| ribbon-spec | "30mm by 0.023mm... supports 2,000 kg... 100 cargo vehicles of 580 kg each" | Novel supporting | Concrete engineering parameters for the alternative architecture. |
| climber-energy | "10 kW at the surface to under 100 W at seven percent of the distance to L1" | Novel supporting | Energy budget for the elevator is dramatically lower than for a mass driver (no kinetic launch energy required). |
| latitude-constraint | "With M5 fiber at half its stress limit... reaches about 36 degrees latitude" | Novel supporting | Practical deployment constraint. |
| post-2005-progress | "LiftPort company reported in 2019 that the project had achieved no progress beyond the lunar elevator company's conceptualized design" | Consistent | The 14-year gap from feasibility study to zero commercial follow-on is a strong historical signal that the binding constraint is capital and program commitment. |

**Summary:**

| Verdict | Count |
|---|---|
| Consistent | 1 |
| Different conclusion | 0 |
| Novel supporting | 5 |
| Merits investigation | 0 |
| Not relevant | 0 |

**Overall**: Pearson NIAC 2005 is the canonical non-mass-driver alternative. The 2005-2025 historical record (zero commercial follow-on) is the strongest evidence that the root question may not depend on mass-driver-yes/no — there is a competing architecture with arguably easier engineering, also under-developed.

## Tier A — medium review (key claims, scalar verdicts)

### janhunen-2024-gravity-anomalies (Tier A — credentialed preprint)

**Overall verdict:** novel supporting.

**Two-sentence summary:** Janhunen's mascon-orbit result substantially relaxes the catcher-engineering problem (9-day catching window vs sub-second hyperbolic intercept) and lowers the muzzle-velocity requirement by ~30% (1.7 km/s vs 2.4 km/s). The modern engineering envelope has moved toward sub-escape + orbital tug.

**Key claims:**

- "A passive projectile can remain in lunar orbit for up to 9 Earth days" → **Novel supporting**. Relaxes the catching engineering problem.
- "Approximately 1.7 km/s (orbital speed)" rather than 2.4 km/s escape → **Novel supporting**. ~50% kinetic energy reduction.
- "Passive projectiles can be made entirely from lunar material" → **Novel supporting**. Supports closed-loop ISRU + mass driver.

### aiaa-2025-4123-mass-driver-tech (Tier A — peer-reviewed conference)

**Overall verdict:** merits investigation (paywalled — full review awaits PDF fetch).

**Two-sentence summary:** AIAA 2025-4123 is the most recent peer-reviewed primary source on lunar mass-driver sizing and would be the appropriate anchor for the q7 calc. Currently captured only at the abstract / search-summary level.

**Key claims:**

- Railgun vs coilgun trade for sensitive vs raw payloads → **Novel supporting**. Architectural choice not in q7 calc but worth surfacing.
- Modeling outputs system mass, size, power, energy for specific payloads → **Merits investigation**. The specific numbers would be the strongest possible anchor.

### dsiac-hypervelocity-2015 (Tier A — peer-reviewed DoD technical)

**Overall verdict:** consistent.

**Two-sentence summary:** DSIAC 2015 anchors the engineering ceiling of demonstrated EM launch: 32 MJ muzzle energy for ONR EMRG, Mach 7.5 (~2.5 km/s), 7.2 km/s electric light-gas gun at 10% efficiency. The three identified bottlenecks (barrel wear, high-g loading, pulsed-power supplies) align with q7's load-bearing variables.

**Key claims:**

- "Phase I proof-of-concept at 32 megajoules of muzzle energy" → **Consistent**. Earth-demonstrated benchmark; lunar 1 Mt/yr system needs ~315 MJ per shot (10× scale-up).
- "Compact pulsed power supplies for volume-constrained systems continue to be a challenge" → **Consistent**. Supports q7's pulsed-power-as-engineering-bottleneck framing (Codex pass-3 audit accepted: DSIAC does NOT provide the specific 2 kJ/kg or $10/kJ number).
- "Adapting EMRG technology to a land-based system the size of a tank may prove unachievable" → **Novel supporting**. Engineering-scale-limit caveat. The lunar mass driver is ~1000× larger scale than EMRG; the DSIAC concern is non-trivial.

### kolm-l5-news-1980 (Tier A — popular aerospace press, credentialed)

**Overall verdict:** consistent.

**Two-sentence summary:** Kolm's 1980 L5 News update on Mass Driver 2 progress and the "$1/lb to L-5" headline. Same author-network and number-set as NASA SP-428; not independent triangulation.

**Key claims:**

- "Operate in an evacuated, four-inch caliber tube at an acceleration of 500 gee" (MD-2 design) → **Consistent**. The trajectory MD-1 (33g, 40 m/s) → MD-2 (500g, 112 m/s) is the demonstrated-engineering arc.
- "$1 per pound, assuming only ten years of operation" → **Consistent** with SP-428's $3.137B / 600 kt/yr / 10-yr amortization → ~$0.5/kg.

## Tier B — per-figure quote review

### Robert Peterkin (General Atomics EMS)

**Roles:** Director of Operations, General Atomics Electromagnetic Systems (the firm that built U.S. Navy EMALS aircraft catapult).
**Relevance:** The most credentialed industry-engineering voice publicly advocating lunar EM launch.

| Quote | Source | Verdict | Reasoning | Severity |
|---|---|---|---|---|
| "A not-too-distant future lunar economy will make use of these lunar resources to resupply, repair, and refuel spacecraft in lunar orbit at lower cost than delivering terrestrial resources from Earth's deep gravitational well." (AFOSR 2023) | sources/peterkin-general-atomics-2023 | **Supports** | Aligns with the q4 (gear-ratio) framework: lunar capital becomes net-positive when launch costs to orbit are reduced. q7's BAU verdict makes this conditional on Mt-scale operational; Peterkin does not specify a timeline. | low |
| "The U.S. government should fund an evolution of the existing electromagnetic aircraft launch system, now operating reliably on the U.S. Navy's Gerald R. Ford nuclear aircraft carrier." (Space.com 2024) | sources/peterkin-general-atomics-2023 | **Supports** | Aligns with q7's M1 milestone definition (Earth-based scale-up of operational EMALS to lunar-relevant velocity). | low |
| "To prove viability, we need to demonstrate that this approach can achieve a lunar orbit speed for at least 100 launches without needing to replace launcher components." (Space.com 2024) | sources/peterkin-general-atomics-2023 | **Supports** | Direct identification of M1 milestone. Note: 100 launches is ~5 orders of magnitude below operational cycle life requirement; q7.c10 reframes this as "next demonstrator, not operational system." | medium |

**Overall:** Peterkin's positions are sober, engineering-grounded, and align with q7's framing of next-milestone-not-deployment. He is the most credentialed industry voice and his views support the structural claim that this is a serious engineering R&D path rather than fantasy.

### Elon Musk

**Roles:** SpaceX CEO, Tesla CEO, xAI founder.
**Relevance:** Primary commercial-strategic principal whose Project TERAFAB commitment shapes the modern capital-mobilization picture.

| Quote | Source | Verdict | Reasoning | Severity |
|---|---|---|---|---|
| "I want to live long enough to see the mass driver on the moon" (Giga Texas, March 2026) | sources/musk-mass-driver-tweet-2026 | **Supports** | Reframed: a personal-lifetime-horizon statement aligns with q7's "decades-scale" BAU framing — Musk himself is not predicting near-term operational deployment. | low |
| "Path to Petawatts is Mass drivers on Moon" (X, May 2026) | sources/musk-mass-driver-tweet-2026 | **Mixed** | The strategic framing (TW-scale orbital infrastructure requires lunar mass drivers) aligns with Handmer's 100-TW threshold and q7's regime analysis. The specific "Path to Petawatts" claim requires aspirational throughput beyond Handmer's 10 Mt/yr nameplate, which q7 places at 40-60+ yr BAU. | medium |
| "500 to 1000 TW/year of AI satellites into deep space" (Giga Texas, March 2026) | sources/musk-mass-driver-tweet-2026 | **Different conclusion** (was "Contradicts our analysis" — softened per Codex pass-4 audit on Newman taxonomy + mass-intensity-assumption dependence) | At a reasonable kg-per-kW of satellite (~1-10 kg/kW), 500-1000 TW/yr ≈ 10⁹-10¹⁰ kg/yr ≈ 100-1000× Handmer's 10 Mt/yr nameplate. The mass-intensity conversion is itself an assumption; under aggressively low kg-per-kW (≤0.1 kg/kW for ultra-thin film satellites) the gap closes. q7's BAU and IE regimes do not reach this scale; only TAI-or-beyond does. | high |
| "Per-kilogram costs could drop to approximately $500 — a 90% reduction" (Giga Texas paraphrase, March 2026) | sources/musk-mass-driver-tweet-2026 | **Mixed** | q7 derives BAU $125/kg LLO + SEP leg, suggesting BAU late-era lunar-to-LEO is in the few-hundred-$/kg range — within striking distance of Musk's $500/kg. But Musk's framing as "90% reduction from current methods" is rhetorical, not derived. | low |

**Overall:** Musk's positions span the realistic-to-aspirational spectrum. The "live long enough" framing is consistent with q7's BAU; the "Path to Petawatts" / 500-1000 TW/yr is contradicted by q7's BAU and IE regimes — it requires TAI-grade or beyond. The strategic commitment from SpaceX is a meaningful signal for capital mobilization, but the specific numerical commitments are not engineering-grounded.

### Phil Metzger (UCF, ex-NASA Swamp Works)

**Roles:** University of Central Florida planetary scientist; co-founder NASA KSC Swamp Works; author of the canonical 2023 production-mass-ratio framework for lunar manufacturing economics (q4 anchor source).
**Relevance:** The leading academic voice on lunar manufacturing economics. His stance on whether mass drivers are part of the realistic architecture is load-bearing.

| Quote | Source | Verdict | Reasoning | Severity |
|---|---|---|---|---|
| "In case you weren't paying attention, in the past 48 hours, the world's greatest Von Braunian (Elon) has embraced O'Neillianism. Lunar manufacturing. Mass drivers. Massive industry outside a planetary gravity field. All this and Mars, too." (X, late 2025) | sources/metzger-twitter-2025 | **Supports (qualitative)** | Affirmative reception from the academic anchor. Does not address engineering feasibility timeline or capital — purely paradigm-level. Metzger's q4 framework treats lunar manufacturing economics as conditional on mass throughput; mass driver availability is one path to high throughput. | low |

**Overall:** Metzger's enthusiasm is a qualitative paradigm-level signal, not a numerical engineering judgment. The fact that the leading academic on lunar manufacturing economics does not push back is meaningful evidence that the strategic pivot has academic validation. But Metzger does not endorse any specific timeline or capital projection.

## Tier C — scalar verdict + one paragraph

### handmer-mass-driver-2026 (Tier C, also Tier B as public figure)

**Verdict:** Consistent. **Confidence:** medium-high.

The May 2026 engineering brief is the load-bearing modern engineer-advocate source. Headline design (128 m, 1000g, 200 kg/shot, 10 Mt/yr nameplate, $2-4B reactor) cross-checks against q7's kinematics at η=0.90. The "$10/kg rocks in lunar orbit" headline is contingent on 10 Mt/yr operational, which q7 BAU does not reach in <40 years. Handmer is explicit that this requires Earth-launch supply-constraint (>100 TW/yr deployment) as the economic forcing function. Importantly, Handmer flags "sintered magnet blocks 9 m long under 1000g shear and oscillating tension fatigue is not obviously feasible" — the strongest single-source corroboration of q7's cycle-life-gap finding. Conflicts with higher tier? No — aligns with Wright et al. 2011 negative cost-benefit when both are read carefully (Handmer's $10/kg headline depends on TAI-grade scale, which Wright et al. would not have validated).

### handmer-moon-factories-2026 (Tier C)

**Verdict:** Consistent. **Confidence:** medium.

The February 2026 strategic-economic-framing post precedes the May engineering brief. Establishes the AI-demand-as-economic-forcing-function frame. Does not address engineering feasibility directly. Useful for the public-figure-positions claim.

### sciencearray-mass-drivers (Tier C)

**Verdict:** Mixed. **Confidence:** medium.

Trade-press synthesis with the canonical $10-100/kg target headline. The 2040s-2050s calendar timeline violates anti-pattern #11. Provides aspirational anchor consistent with q7's IE-to-TAI regime endpoints but does not constitute independent triangulation. Per Codex pass-3 audit accepted: this is weak triangulation, not consistency.

### spinlaunch-status-2025 (Tier C)

**Verdict:** Consistent. **Confidence:** high.

Documents a sober historical analog: $150M+ private capital, decade of development, August 2025 10,000g survival demo, April 2025 strategic pivot to chemical rockets. The trajectory is consistent with q7's BAU M2-M3 estimate. Per Codex pass-3 audit accepted: this is a "broad cautionary analogue," not specific validation of the 10-15 year estimate.

## Tier E — not reviewed

- [lunarpedia-mass-drivers](../sources/lunarpedia-mass-drivers/extract.md) — community wiki, orientation only
- [coilgun-wiki-engineering](../sources/coilgun-wiki-engineering/extract.md) — Wikipedia, orientation only
- [mass-driver-wiki](../sources/mass-driver-wiki/extract.md) — Wikipedia, orientation only

These provide the canonical 2.4 MJ/kg energy figure and engineering-ceiling efficiency data that informs q7 calc parameter ranges; per the source-tiers rule, they do not appear as primary evidence in claims.yaml.

## Summary table

| Tier | Source | Overall verdict | Severity-weighted notes |
|---|---|---|---|
| S | wright-kuznetsov-kloesel-2011 | consistent + novel supporting | Load-bearing modern primary, anchors BAU pessimism |
| S | nasa-mass-drivers-iii-1979 | different conclusion + merits investigation | Canonical historical reference; 96.4% efficiency claim merits dedicated re-extraction |
| S | oneill-kolm-acta-1980 | bibliographic anchor | Full PDF not fetched; future iteration |
| S | pearson-lunar-elevator-2005 | novel supporting | Establishes alternative architecture |
| A | janhunen-2024-gravity-anomalies | novel supporting | Substantially eases catching engineering; 50% energy reduction |
| A | aiaa-2025-4123-mass-driver-tech | merits investigation | Paywalled; should be re-extracted with library access |
| A | dsiac-hypervelocity-2015 | consistent | Engineering-bottleneck framing; specific number priors are from broader pulsed-power lit |
| A | kolm-l5-news-1980 | consistent | Same author-network as SP-428; not independent |
| B | peterkin (3 quotes) | supports | Sober, engineering-grounded, aligned with q7 framing |
| B | musk (4 quotes) | mixed (1 contradicts) | "500-1000 TW/yr" is q7-contradicted at high severity; other quotes within q7 envelope |
| B | metzger (1 quote) | supports (qualitative) | Affirmative paradigm-level; no numerical commitment |
| C | handmer-mass-driver-2026 | consistent | Load-bearing engineer-advocate; explicit cycle-life caveat |
| C | handmer-moon-factories-2026 | consistent | Strategic framing only |
| C | sciencearray-mass-drivers | mixed | Aspirational; weak triangulation |
| C | spinlaunch-status-2025 | consistent | Historical analog for BAU M2-M3 |
| E | (3 wiki sources) | not reviewed | Orientation only |

**Highest-severity flag:** Musk's 500-1000 TW/yr AI satellite capacity claim is contradicted by q7 in all regimes except aspirational-TAI-or-beyond. This will be a load-bearing point in the write pass — the difference between Musk-stated and q7-feasible capacities is 1-3 orders of magnitude.

**Merits investigation candidates** for tree-pass:
1. AIAA 2025-4123 deep re-extraction (paywalled).
2. O'Neill-Kolm Acta Astronautica 1980 full PDF fetch.
3. NASA SP-428 1979 96.4% efficiency claim — what subsystems does it cover?
4. Janhunen 2024 catcher-engineering details (what tug ΔV is needed for the 9-day catching window?).
5. The post-2005 lunar elevator stall (Pearson NIAC) — what specifically blocked commercial follow-on?

**Cycle-life gap as a sub-leaf candidate:** worth spawning a q7.1 sub-leaf to investigate the specific engineering paths to 10⁶-10⁹ shot cycle life. This is the binding constraint per q7.c10 and per source-review-confirmed Handmer flag.

## Next pass

Pass 5 (consistency) — compare q7 claims to sibling leaves (q1 / q2 / q3 / q4 reviewed at run start; q5 / q6 not yet reviewed and excluded per the parallel-execution caveat).
