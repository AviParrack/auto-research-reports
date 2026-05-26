---
synthesis_version: v1
date: 2026-05-26
leaves_consumed: [q1, q2, q3, q4, q5, q6, q7]
cross_consistency: 01-tree/cross-consistency-p01.md
---

# Synthesis context — lunar-manufacturing v1

## Root question

**When does lunar surface manufacturing become cheaper than Earth launch for orbital infrastructure?**

## Per-leaf headlines

### q1 — Earth launch cost (reviewed, confidence medium-high)

Starship cost-per-kg to LEO under three operational scenarios (2030-2035 mature operations): optimistic **$59-277/kg**, partial **$107-466/kg** (demonstrated by B1076 34-reuse milestone), pessimistic **$194-878/kg**. Dominant variable is refurbishment rate, not hardware amortization. Musk's $10/kg target sits outside the calc envelope unless TAI-grade compression AND zero-margin pricing both occur. **Falcon 9 list prices rising at $500/kg/yr** (Feb 2026 baseline $7,000/kg rideshare) — Starship has not yet pulled market prices down. Citigroup $100/kg by 2040 fits the optimistic-late corner.

Under TAI/IE compression: optimistic case drops to $15-25/kg internal.

### q2 — Lunar ascent cost (reviewed, confidence medium-high)

Lunar-surface-to-LEO cost spans **$50-$13,029/kg** across realistic aerobraking-included scenarios:
- chemical Earth-imports-only $1,303-$13,029/kg
- chemical aggressive-ISRU $994-$8,912/kg
- mass-driver + SEP $50-$528/kg

Architectural choice (aerobraking vs propulsive; mass-driver vs chemical) more economically consequential than propellant chemistry. **Only mass-driver+SEP at late-era throughput closes within 2× of q1 optimistic-late ($50 vs $59/kg).** Trade-press evidence: $4,000/kg per HLS mission matches calc's Earth-imports-only mid-era $4,162/kg within 5%.

q2.c5 mass-driver $50/kg headline assumes $10B capital — **TAI-conditional per q7 reconciliation**.

### q3 — ISRU feasibility (reviewed, confidence medium-high)

**O₂, Fe, Si, structural mass, LOX propellant — TRL 4-6 in early 2026.**
- Carbothermal reduction TRL 6 (Sierra Space JSC demo Sept 2024)
- MRE TRL 4-6 (multiple programs)
- Ilmenite reduction TRL 5-6 (mare-specific)
- Al/Ti via FFC Cambridge structurally Earth-import-bound on chlorine (MRE preferred for lunar)
- **LH2 via polar-ice electrolysis: geological gate pending VIPER (late-2027)**
- **LCH4 structurally impossible** — no bulk lunar carbon; this is a compositional fact, not a TRL question
- Sintering / vacuum-casting TRL 5 closes structural-mass loop (habitats, depots, radiation shielding)

TRL trajectory is acceleration-regime-dependent, not calendar-year-dependent (BAU/IE/TAI/stall framework).

### q4 — Gear-ratio competitiveness (reviewed, confidence high)

Approximately **35× φ-threshold** for lunar absolute advantage at GTO under Metzger's mid-range. LEO structurally harder: Γ ≈ 14 chemical, ≈ 1 with SEP. Tent sublimation (φ = 442-534 published TEAs) exceeds threshold by ~order of magnitude; strip mining clusters at/near threshold. **Threshold is model-contingent, not universal physics.** Industrial-explosion / TAI automation compressing capital mass puts even pessimistic ISRU far above threshold.

q4.c12: **SEP with molecular water at Isp 2000s drops Γ_LEO from 14 to ~1** — the architectural difference between LEO being structurally unreachable and viable.

### q5 — Capital buildup (reviewed, confidence medium)

Net-positive-export base capex over 20-25 years:
- **BAU: $150-400B** (calc baseline $167B; upper bound absorbs Codex-accepted ISRU mass / mobility / mfg / dev-multiplier revisions)
- **Industrial-explosion: $1.2B / ~5 years** (140× compression — Shotwell's 5-year framing scale)
- **TAI: degenerate near-zero capex / <1 year buildup** — but M6 12-month crewed-occupation milestone is irreducible 12-month floor

8 milestones: M1 robotic precursor → M2 cargo lander → M3 uncrewed habitat → M4 fission surface power → M5 ISRU pilot → M6 first crewed sustained occupation (12-mo min) → M7 manufacturing complement → M8 net-positive export.

Combined US public-program through ~2033: **$115-140B** (Artemis $93B + Isaacman $20B + ops). Below BAU bracket because excludes manufacturing complement + net-positive endpoint.

### q6 — Orbital demand (reviewed, confidence medium-high)

Three-regime demand bracket, **three orders of magnitude apart**:
- Stall: ~20,000 t cumulative 2026-2040 (~1,400 t/yr)
- BAU: ~2,150,000 t (~143,000 t/yr) — **93% SDC at 50 GW deployed by 2040**
- TAI-C: ~42,900,000 t (~2,866,667 t/yr) — **93% SDC at 1,000 GW deployed**

SDC mass intensity ~40 t/MW continuous compute (cross-corroborated peraspera 30-50 t/MW, luminix 42 t/MW).

**Under TAI-C, SDC demand alone (~2.67 Mt/yr) exceeds plausible Earth-launch throughput (~400 kt/yr) by ~10×, making lunar bulk mass architecturally necessary for ~50% of SDC mass budget.** Other ~50% (compute hardware) stays Earth-launch-bound regardless.

q6.c14 Cote bandwidth-ceiling caveat caps TAI-C at ~200 GW factor-5 sensitivity within regime uncertainty, not a regime-killer.

### q7 — Mass-driver feasibility (reviewed, confidence medium-low)

First-principles capital cost for 1 Mt/yr operational system:
- **BAU: $1,242B / 20-30 years** (track + drive coils dominate at 96%)
- **Industrial-explosion: $127B / ~6 years**
- **TAI-grade: $13.3B / ~1.5 years** — within striking distance of q2.c5's $10B assumption
- **Stall: never reached**

q7.c11: under BAU and any horizon shorter than ~25 years, **chemical rockets dominate regardless of mass-driver availability**.

**Cycle-life gap (q7.c10, severity-high):** 1 Mt/yr × 200 kg/shot × 20 yr requires ~10⁸ shots; 10 Mt/yr requires ~10⁹. State-of-art demonstrated EM-launcher cycle life: 10²-10³. Navy EMRG cancelled 2021 after ~$500M with cycle-life as binding failure mode. **5-7 OOM gap is independent of capital cost and TAI compression; requires engineering breakthrough preconditioned on materials science, not just automation.**

The 1979 NASA SP-428 figure ($3.1B in 1979 ≈ $13B in 2026) lands at q7's TAI endpoint — meaning the 1979 study was already describing a compressed-economics envelope that 46 years of historical engineering did not realize.

## Cross-consistency findings (cross-consistency-p01.md)

**No analytical contradictions.** All disagreements are scope-mismatches or regime-conditional dependencies.

### Resolved conditional dependencies

1. **Mass-driver capital (q2.c5 vs q7.c6)**: q2's $10B assumption is achievable only under q7's TAI-grade compression ($13.3B). q2's $50/kg headline is therefore TAI-conditional, not "available by 2040." Synthesis must specify the regime.

2. **Mass-driver $/kg LEO scope (q2.c5 vs q7.c7)**: q7.c7 reports $125/kg BAU to LLO only (no SEP transfer); q2.c5 includes SEP. Different scopes, reconciled.

3. **Capex stacking (q5.c4 ↔ q7.c6)**: q5 base + q7 mass driver are **additive components of a full architecture**, not alternatives. **BAU full architecture $1.4-1.7T cumulative. TAI full architecture $15-25B.** Synthesis must use "base + mass-driver launch system" / "base only" phrasing.

### Cross-leaf dependencies for synthesis

1. **q2 hydrolox ↔ q3 polar-ice gate**: q2 aggressive-ISRU assumes hydrolox propellant from lunar polar ice. q3 says polar ice is geologically gated pending VIPER (late-2027). Stall regime for q2 ≈ stall regime for q3.

2. **q1 list-price-vs-internal-cost gates q6 BAU demand (cross-pass inference for q8)**: q1 internal cost $107-466/kg vs list price $7,000/kg rising at $500/kg/yr. q6's BAU demand projection implicitly assumes internal-cost-level pricing propagates to commercial. If list prices stay above $1,000/kg through 2030, BAU SDC demand compresses ~3×. TAI-C is unaffected because it is gated by internal cost (SpaceX-internal use) and AI compute growth, not commercial list pricing. **The regime split is sharper than smooth interpolation would suggest.**

3. **φ-threshold (q3.c13b ↔ q4.c6)**: instantaneous full-plant φ 10-20/yr does NOT clear Metzger's 35 threshold; ONLY cumulative multi-year integration does. Year-1 economics depend on financing structure. Synthesis must preserve the "multi-year integration" qualifier.

## The two-legged crossover claim

The synthesis must surface that the crossover stands on **two legs, not one**:

1. **Cost** — q1 + q2 + q7 chain: lunar manufacturing beats Earth launch in the TAI-grade regime at the **$50/kg (mass driver) vs $59/kg (optimistic-late Starship)** margin.

2. **Throughput necessity** — q6 + q1: under TAI-C, SDC demand alone exceeds Earth-launch ceiling 10×, making lunar bulk mass **architecturally necessary** for ~50% of the SDC mass budget regardless of cost.

Under **BAU**, neither leg holds: cost (mass driver doesn't reach scale), AND throughput (demand fits inside Earth-launch capacity).
Under **stall**, demand fails (q6.c7) — lunar manufacturing thesis fails for lack of demand, not lack of supply.

## Engineering risks that bind the headline more tightly than capital

- **q7.c10 cycle-life gap** — 5-7 OOM gap between demonstrated and required EM-launcher cycle life. TAI compression alone doesn't close this; requires materials-science breakthrough.
- **q5.c7 M6 12-month floor** — TAI cannot compress milestones whose definition IS a 12-month integration. Crewed-occupation-gated milestones break out of the compression curve.
- **q3.c4 polar-ice gate** — VIPER (late-2027) clearing or stalling moves q2's aggressive-ISRU column wholesale.

## Source review verdict counts (across all leaves)

Tier S: 35+ sources, full claim-by-claim review
Tier A: 30+ sources, medium review
Tier B: 25+ public figures across q1/q5/q6/q7 with per-figure quote review
Tier C: 30+ sources, scalar review
Tier D: 15+ sources, scalar review
Tier E: orientation only, not stored under sources/

Tier-B public figures triangulated: Musk, Bezos, Shotwell, Casey Handmer, Phil Metzger, Eric Berger, Andrew McCalip, Dylan Patel, Jared Isaacman, Robert Peterkin, Kim Stanley Robinson, Bill Nelson, George Sowers, Robert Zubrin, Citigroup analysts.

## Anti-patterns synthesis must avoid

- **#11 no naive calendar timelines** — frame as BAU/IE/TAI/stall regimes, not "by 2030/2040"
- **#12 motivation before answer** — root-question structure: why does this matter, what decision does it inform, then the answer
- **#13 no news-headline voice** — kill "is real but contingent", "huge", "the bottleneck", "surprisingly", "the popular X framing"
- Maximal-rigor academic register. Inline `[leaf-id]` and `[source-slug]` citations. Math via `\(...\)` and `\[...\]`.
