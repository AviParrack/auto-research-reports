---
pass: 3
kind: reconcile
leaf: q7-mass-driver-feasibility
date: 2026-05-25
status: done
---

# Pass 3 — Reconcile: Derived numbers vs source claims

Sources now unsealed. For each derived q7 claim, this pass compares against the 18 source extracts in `sources/`. Disagreements are surfaced explicitly; agreements provide triangulation; novel facts in sources (not derived) are added to the claim graph.

## Headline reconciliation

The picture across the corpus splits along a clean fault line:

| Source group | Verdict on mass-driver feasibility timeline | Verdict on capital |
|---|---|---|
| 1970s-80s O'Neill/NASA primary (SP-428, Kolm L5 News, O'Neill-Kolm Acta 1980) | Operational by mid-1980s | $3.1B (1979 $) ≈ $13B (2026 $) |
| 2011 NASA / IEEE reanalysis (Wright et al.) | "Not as favorable as originally suggested" | Negative cost-benefit vs Ares-V |
| Modern industry voice (Peterkin / General Atomics) | Next milestone = 100-launch Earth demo | No capital commitment |
| Modern engineer-advocate (Handmer 2026) | Decades unless Earth-launch supply binds | $2-4B reactor; total unenumerated |
| Modern strategic principal (Musk 2026) | "I want to live long enough to see it" | No funded program |
| Modern academic (Metzger) | Affirmative paradigm validation | No quantitative claim |
| Trade press (Science Array, etc.) | 2040s-2050s "calendar timeline" | $10-100/kg target headline |

The q7 calc's BAU verdict ($1.2T, 20-30 yr) sits between the 1970s-80s optimism ($13B 2026-$, mid-1980s ops) and the 2011 NASA pessimism (negative cost-benefit at even small scales). The 1979 NASA SP-428 figure inflated to 2026 dollars is ~$13B — strikingly close to q7's TAI-grade compression number, but BAU-impossible. **The reconciliation: the 1970s-80s "$1/lb to L5" headline was a TAI-grade projection avant la lettre — it requires aggressive engineering compression that did not happen between 1979 and 2025.**

## Per-claim reconciliation

### q7.c1 (lunar escape and LLO velocities, mascon-orbit)

- **Sources agree:** [lunarpedia-mass-drivers](../sources/lunarpedia-mass-drivers/extract.md) (2.4 MJ/kg @ 2 km/s), [janhunen-2024-gravity-anomalies](../sources/janhunen-2024-gravity-anomalies/extract.md) (1.7 km/s LLO with mascon-assisted 9-day catching window), [handmer-mass-driver-2026](../sources/handmer-mass-driver-2026/extract.md) (1.6 km/s muzzle to LLO).
- **q7 calc:** 2,375 m/s escape, 1,679 m/s LLO; both derived from GM/R kinematics.
- **Verdict:** consistent. Janhunen's mascon-orbit result substantially relaxes the catcher engineering problem and the modern engineering envelope has moved toward sub-escape + orbital tug, away from the O'Neill / SP-428 escape-velocity-to-L5 architecture.

### q7.c2 (kinematic track-acceleration trade)

- **Sources agree:** [lunarpedia-mass-drivers](../sources/lunarpedia-mass-drivers/extract.md) (2g→100km, 20g→10km, 200g→0.5km — same v²/2a kinematics), [handmer-mass-driver-2026](../sources/handmer-mass-driver-2026/extract.md) (128m main track at 1000g, 1.6 km/s — checks out).
- **Verdict:** consistent. This is hard kinematics; no source can disagree.

### q7.c3 (efficiency range)

- **Sources span the range:** [coilgun-wiki-engineering](../sources/coilgun-wiki-engineering/extract.md) (DARPA 45-stage demonstrated 22%), [wright-kuznetsov-kloesel-2011](../sources/wright-kuznetsov-kloesel-2011/extract.md) (33% TRL-grounded), [nasa-mass-drivers-iii-1979](../sources/nasa-mass-drivers-iii-1979/extract.md) (96.4% claimed, electromagnetic-conversion only), [handmer-mass-driver-2026](../sources/handmer-mass-driver-2026/extract.md) (assumes ~90% driver efficiency).
- **Disagreement triangulation:** The 1979 NASA 96.4% figure is the theoretical electromagnetic-conversion ceiling, NOT net system efficiency. Wright et al. 2011 explicitly use 33% as the TRL-grounded net, including SCR power conversion (~7%) and ~50% motor losses. Handmer's 90% is closer to the SP-428 figure than to Wright; presumably similar electromagnetic-ceiling treatment.
- **Verdict:** q7's 22-90% sensitivity range correctly spans the literature; the 50% midpoint-of-aspirational is a conservative net-system assumption. Consistent with the careful framing.

### q7.c4 (average and peak wall power)

- **Sources agree:** [handmer-mass-driver-2026](../sources/handmer-mass-driver-2026/extract.md) (450 MW average / 16 GW peak at 10 Mt/yr nameplate). q7's derived 894 MW average at 10 Mt/yr, 6.6 GW peak per shot at 1000g.
- **Disagreement:** Handmer's 16 GW peak is ~2.4× q7's 6.6 GW. Source of disagreement: Handmer's "peak" is at the *midpoint of the acceleration*, which under a constant-acceleration profile is when both current and induced EMF are maximal. q7's "peak" is the average-over-burn × 2 (constant-acceleration profile). These are different operational definitions — Handmer's number measures instantaneous power-supply demand at midpoint; q7's measures shot-averaged peak. Both are internally consistent.
- **Disagreement:** Handmer 450 MW vs q7 894 MW at 10 Mt/yr. Source: Handmer uses η=0.90 driver efficiency; q7 uses η=0.50. At η=0.90, q7's number drops to 497 MW (close to Handmer's 450 MW). Reconciled at the efficiency assumption.
- **Verdict:** consistent at matched efficiency assumptions. Handmer's specific reactor sizing (450 MW) is internally consistent with his 90% efficiency claim; q7's 894 MW is the conservative-efficiency variant.

### q7.c5 (capacitor bank)

- **Sources partial:** [dsiac-hypervelocity-2015](../sources/dsiac-hypervelocity-2015/extract.md) identifies "compact pulsed power supplies for volume-constrained systems continue to be a challenge" — supports q7's framing that this is engineering work. ONR EMRG demonstrated 32 MJ muzzle energy; q7 needs ~315 MJ per shot (10× larger).
- **q7 derived:** ~157 t capacitors per shot at 2 kJ/kg, ~$3.1M per shot, $0.8B bank with 5× redundancy.
- **Verdict:** consistent. No source provides an independent lunar mass-driver capacitor bank capex figure; q7's number is independently derived from DSIAC engineering parameters. Handmer 2026 flags this as "pulsed-power infrastructure may dominate system mass and cost" — qualitatively consistent with q7's identification of pulsed power as a sub-dominant ($0.8B / $1242B) but non-trivial cost line.

### q7.c6 (BAU capex decomposition)

This is the load-bearing reconciliation. The capex figures span 3 orders of magnitude across sources:

| Source | Total capex | Throughput target | Vintage |
|---|---|---|---|
| NASA SP-428 1979 | $3.137B (1979 $) ≈ $13B (2026 $) | 42 kg/s = 1.3 Mt/yr | 1979 optimism |
| Kolm L5 News 1980 (derivative) | Same — $1/lb at 600 kt/yr × 10 yr ⇒ ~$13B amortized | 600 kt/yr | 1980 |
| Wright et al. 2011 | Not enumerated; conclusion is "not favorable" | Small-payload, low-cycle | 2011 TRL-grounded |
| Handmer 2026 | Reactor $2-4B; total unenumerated | 10 Mt/yr nameplate | 2026 sketch |
| Science Array trade press | $10-100/kg target headline | Late-era only | 2026 trade |
| **q7 derived (BAU)** | **$1,242B** | **1 Mt/yr** | **First-principles + sourced priors, 2026** |
| q7 derived (TAI) | $13.3B | 1 Mt/yr | TAI-compressed |

The convergence of (a) 1979 NASA SP-428 inflated to ~$13B (2026), (b) q7 TAI-grade compressed at $13.3B, and (c) q2.c5's $10B capital assumption is striking. **All three numbers refer to the same architectural feasibility envelope; the 1979 figure was a TAI-grade-effective projection that assumed engineering compression that historically did not occur.** Wright et al. 2011 is the load-bearing modern reanalysis that re-derived using TRL-grounded subsystems and reached the opposite conclusion.

- **Verdict:** q7's BAU figure ($1,242B) is two orders of magnitude above the 1979/Handmer literature anchors and one order of magnitude above the q2.c5 assumption. The discrepancy is fully attributable to the lunar construction multiplier and TAI compression assumptions. The 1979 baseline assumed ISRU-built drive coils as a near-term capability — which is precisely what would only become available under TAI-grade automation. The historical record (1979→2025 with operational mass driver not built) suggests the BAU number is closer to reality than the 1979 number.

### q7.c7 (per-kg amortized BAU)

- **Sources partial:** [sciencearray-mass-drivers](../sources/sciencearray-mass-drivers/extract.md) ($10-100/kg target). q2.c5 derives $50-528/kg across throughput regimes. q7's BAU $125/kg sits between the two; the sciencearray $100/kg upper-bound matches q7's BAU midpoint. The sciencearray $10/kg lower-bound matches q7's IE compressed range.
- **Verdict:** consistent with the optimistic-to-realistic literature range; BAU sits at the realistic end, IE at the optimistic end.

### q7.c8 (regime sensitivity)

- **Sources:** no direct source provides a regime-decomposed capex. [musk-mass-driver-tweet-2026](../sources/musk-mass-driver-tweet-2026/extract.md) ($500/kg target, 500-1000 TW/yr) and [handmer-mass-driver-2026](../sources/handmer-mass-driver-2026/extract.md) ($10/kg "rocks in lunar orbit") both bracket the TAI-grade end. [wright-kuznetsov-kloesel-2011](../sources/wright-kuznetsov-kloesel-2011/extract.md) implicitly anchors the BAU pessimism.
- **Verdict:** the regime framing is q7's contribution to the literature, not a source-borrowed claim. The TAI-grade endpoint converges on the literature's optimistic figures; the BAU endpoint converges on the 2011 NASA pessimism.

### q7.c9 (milestones)

- **Sources:** [peterkin-general-atomics-2023](../sources/peterkin-general-atomics-2023/extract.md) explicitly identifies M1 ("100 launches at lunar orbit speed without replacing components") as the next demonstration. [spinlaunch-status-2025](../sources/spinlaunch-status-2025/extract.md) reports a 10,000g survival demo in August 2025 but no operational kinetic launcher despite $150M+ and a decade — sober historical precedent for the M2→M3 BAU gap.
- **Verdict:** M1 is consistent with Peterkin's industry-engineering framing. The M3-M5 progression is q7's scenario construction. The SpinLaunch trajectory provides historical anchor: a decade of $150M+ private investment has not delivered operational kinetic launch, which is consistent with q7's BAU M2-M3 estimate of 10-15 years total.

### q7.c10 (cycle-life gap — Codex audit-added)

- **Sources support:** [dsiac-hypervelocity-2015](../sources/dsiac-hypervelocity-2015/extract.md) (Navy EMRG cancelled after $500M; barrel wear is the primary railgun failure mode at high cycle counts), [coilgun-wiki-engineering](../sources/coilgun-wiki-engineering/extract.md) (DARPA 45-stage at 22% efficiency despite engineering investment; magnetic saturation and ringing limit cycle life), [handmer-mass-driver-2026](../sources/handmer-mass-driver-2026/extract.md) ("sintered magnet blocks 9 m long under 1000g shear and oscillating tension fatigue is not obviously feasible"; magnet cooling).
- **Verdict:** strong consistency. The cycle-life gap is the binding engineering risk and no source contradicts this characterization. Handmer's explicit acknowledgment that the magnet-fatigue issue is "not obviously feasible" is the strongest single-source corroboration.

### q7.c11 (root-question dependence)

- **Sources implicit:** [pearson-lunar-elevator-2005](../sources/pearson-lunar-elevator-2005/extract.md) provides the alternative architecture (lunar elevator at M5 fiber, NIAC Phase II feasible). [janhunen-2024-gravity-anomalies](../sources/janhunen-2024-gravity-anomalies/extract.md) provides the energy-budget revision (sub-escape catching).
- **Verdict:** consistent with the literature; the lunar elevator alternative means the root answer does not strictly depend on mass-driver-yes/no, which q7.c11 implicitly acknowledges via the BAU verdict (chemical rockets dominate under any short horizon regardless of mass-driver availability).

## Novel factual claims (added from sources, not derived in calc)

### q7.c12 (NEW factual)

**Text:** The 1979 NASA SP-428 Mass Drivers III chapter projected $3.137 billion (1979 dollars) for a baseline operational lunar mass driver by mid-1985, with 42 kg/s throughput, 96.4% claimed system efficiency, and 488 m total length. Inflated to 2026 dollars, this is approximately $13 billion. The 1985 operational target was not met; no operational lunar mass driver has been built in the intervening 40 years. The 2011 Wright et al. NASA / IEEE peer-reviewed reanalysis with TRL-grounded subsystems reached a negative cost-benefit conclusion: "the conclusion, however, is not as favorable for LEML as originally suggested."

**Source:** [nasa-mass-drivers-iii-1979](../sources/nasa-mass-drivers-iii-1979/extract.md), [wright-kuznetsov-kloesel-2011](../sources/wright-kuznetsov-kloesel-2011/extract.md).

**Confidence:** high. Documented in two peer-reviewed NASA technical sources.

### q7.c13 (NEW factual)

**Text:** Pearson, Levin, Oldson, Wykes (NIAC Phase II Final Report, 2005) demonstrated that a lunar space elevator using commercially available M5 fiber is technically feasible — no carbon nanotubes required. A 30mm × 0.023mm M5 ribbon supports 2,000 kg at the lunar surface and 100 cargo vehicles of 580 kg each distributed along the length. This is the canonical non-mass-driver architecture for cis-lunar bulk transport. From 2005 NIAC funding to the 2019 LiftPort status update, no progress was made beyond the conceptualized design — implying the bottleneck for this alternative is also capital and program commitment rather than physics.

**Source:** [pearson-lunar-elevator-2005](../sources/pearson-lunar-elevator-2005/extract.md).

**Confidence:** high. NIAC Phase II final report.

### q7.c14 (NEW factual — public-figure positions)

**Text:** Modern public-figure positions on lunar mass drivers (mid-2020s): Elon Musk publicly committed strategic intent through "Project TERAFAB" announcements in Feb-May 2026, with aspirational figures of $500/kg and 500-1000 TW/yr of AI satellite deployment, but no funded engineering program. Phil Metzger (UCF, leading academic on lunar manufacturing economics) treated Musk's pivot as a vindication of the O'Neill paradigm. Robert Peterkin (General Atomics EMS, builder of the EMALS aircraft catapult) advocates an evolutionary path from EMALS to lunar EM launch, with the next demonstration milestone defined as "100 launches at lunar orbit speed without needing to replace launcher components."

**Sources:** [musk-mass-driver-tweet-2026](../sources/musk-mass-driver-tweet-2026/extract.md), [metzger-twitter-2025](../sources/metzger-twitter-2025/extract.md), [peterkin-general-atomics-2023](../sources/peterkin-general-atomics-2023/extract.md).

**Confidence:** medium-high. Quoted statements from named industry, academic, and commercial principals; aspirational rather than committed.

### q7.c15 (NEW factual — SpinLaunch as historical analog)

**Text:** SpinLaunch is the most-funded modern Earth-based kinetic launch development. Since 2014, ~$150M private capital has been deployed; in August 2025 the company demonstrated 10,000g acceleration survival for a 1U CubeSat. The full operational system design targets 2.1 km/s muzzle velocity with 400 kg payload. April 2025 strategic pivot: the company announced Meridian, a 280-satellite constellation, to be launched on conventional chemical rockets — implying the operational kinetic system is not on a near-term schedule. The trajectory is consistent with q7's BAU M2-M3 estimate of 10-15 years from program start to pilot-scale operational; it suggests political will and capital scale (not physics) are the binding constraints on Earth-based kinetic launch.

**Source:** [spinlaunch-status-2025](../sources/spinlaunch-status-2025/extract.md).

**Confidence:** high. Documented trade-press / company-press.

## Resolution

**For each derived q7 claim:** the calc result either matches source claims at matched assumptions (q7.c1-c5, c10) or diverges in a way fully attributable to specified-and-documented sensitivity assumptions (q7.c6-c8). No source provides evidence that *contradicts* the calc; sources provide bracketing values at the BAU and TAI-grade ends of the regime spectrum.

**For the q2-q7 capital coupling:** q2.c5's $10B assumption matches q7's TAI-grade compressed capex ($13.3B) and matches the 1979 NASA SP-428 figure inflated to 2026 dollars ($13B). The convergence is structural, not coincidental — all three are "compressed-engineering economics" projections. The BAU first-principles capex ($1,242B) is roughly 100× higher; this is the load-bearing q2-q7 disagreement that the cross-consistency pass should flag for synthesis.

**Confidence stand:** Calc claims survive the reconcile pass. Several confidence levels downgraded per the Codex audit (q7.c6, c7, c8, c9). The structural framing (regime-dependent, cycle-life-limited, alternative-architecture-available) is the load-bearing finding.

## What changes in claims.yaml

- New claims q7.c12, q7.c13, q7.c14, q7.c15 added (factual, from sources).
- Existing claims q7.c1-q7.c11 already have evidence entries pointing to `first-principles-calc`; this pass adds source-evidence entries to claims where source triangulation supports the derived number.
- See updated claims.yaml.

## Next pass

Pass 4 (source-review) — per-tier review depth: Tier S full claim-by-claim, Tier A medium, Tier B per-figure quote review, Tier C/D scalar.
