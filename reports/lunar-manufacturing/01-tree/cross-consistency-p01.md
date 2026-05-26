---
pass: cross-consistency
batch: p01
date: 2026-05-26
leaves_scanned: [q1-earth-launch-cost, q2-lunar-ascent-cost, q3-isru-feasibility, q4-gear-ratio, q5-capital-buildup, q6-orbital-demand, q7-mass-driver-feasibility]
agent: claude-opus-4-7
audited: pending
---

# Cross-consistency pass — p01 (all 7 leaves)

The leaves were run in two batches under different protocols: q1+q4 first, then q2+q3 in parallel, then q5+q6+q7 in parallel under the new tier hierarchy. Per-leaf sub-pass 5 only checks against siblings that were reviewed at *its* start time, so contradictions between simultaneously-running leaves remained unflagged until this pass.

The framework holds. The two parallel batches both produced claims compatible with the BAU / industrial-explosion / TAI / stall regime decomposition. Within-regime numbers converge across leaves; cross-regime claims are explicit about the regime they belong to. The contradictions are scope-mismatches and regime-conditional dependencies, not analytical disagreements.

## Topic clusters scanned

| Cluster | Leaves touching | Outcome |
|---|---|---|
| Mass-driver capital cost | q2, q7 | Resolved conditional (regime-bound) |
| Mass-driver $/kg to LEO | q2, q7 | Scope-aligned via SEP transfer |
| Base + mass-driver capex stacking | q5, q7 | Additive — recorded |
| Propellant chemistry (LCH4/H2/LOX) | q2, q3 | Polar-ice-gate dependency |
| φ-threshold (Metzger) | q3, q4 | Cumulative multi-year clears it |
| SEP architectural requirement | q2, q4 | Consistent |
| Aerobraking dominance | q2, q4 | Consistent |
| BAU/IE/TAI/stall framework | q1, q3, q4, q5, q6, q7 | Consistent |
| Launch list-price vs internal-cost | q1, q6 | Regime-coupling — flagged |
| Public-figure positions (Musk, Handmer, Metzger, Shotwell, Bezos) | q1, q2, q5, q6, q7 | Consistent within scope |
| Cycle-life gap | q7 | Single-leaf finding; affects q2 headline |

## Resolved conditional dependencies

### Mass-driver capital cost — q2.c5 vs q7.c6/c8/c12

q2.c5 assumes **$10B capital** for the mass driver, yielding its **$50/kg late-era headline**. q7's independent first-principles BAU derivation lands at **$1,242B** — a 124× difference. q7.c8 also lands at **$127B under industrial explosion** and **$13.3B under TAI-grade compression**.

**Resolution:** q2.c5's $10B is achievable only under TAI-grade compression of the BAU baseline. The 1979 NASA SP-428 figure inflated to 2026 dollars (~$13B) also lands at q7's TAI endpoint — meaning the 1979 study was already describing a compressed-economics envelope that 46 years of historical engineering did not realize. Q2's $50/kg headline is therefore implicitly **TAI-conditional**, not "available by 2040." Q7.c11 makes this explicit: "the root question's answer depends on mass driver availability ONLY in the late-era / TAI-grade regimes."

**No revision to q2.c5 required** — the claim is internally accurate as a conditional. **Synthesis must surface this conditioning.**

### Mass-driver $/kg to LEO — q2.c5 vs q7.c7

q2.c5 reports $50/kg for the full lunar-surface-to-LEO chain (including SEP transfer leg). q7.c7 reports **$125/kg BAU to LLO only** (does not include SEP transfer to LEO).

**Resolution:** Different scopes. q7.c7 explicitly notes the exclusion. Under matched scopes (TAI compression for capital, LLO→LEO via SEP), q2 and q7 are consistent within an order of magnitude. The $125/kg LLO figure under BAU + SEP transfer (Γ_LEO drop from 14 to ~1 per q4.c12) would put the BAU full-chain figure around $150-200/kg, broadly aligned with q2's BAU range.

### Lunar-base + mass-driver capex stacking — q5.c4 ↔ q7.c6

**Scope-mismatch resolution required for synthesis.** q5's base capex ($150-400B BAU) covers habitat + fission power + ISRU plant + mobility + manufacturing complement + infrastructure — the **net-positive-export base**. q7's mass-driver capex ($1,242B BAU) covers the **mass-driver launch system** independently — track + drive coils dominate at 96%. The two scopes are **additive components of a full architecture**, not alternative framings of "the same number."

q5.c15 and q5.c4 describe q5's calc as the "full-scope" estimate for a net-positive-export base, which can read as "everything." Synthesis must explicitly use the phrasing **"base + mass-driver launch system"** for the combined BAU $1.4-1.7T figure and **"base only"** for q5's $150-400B in isolation. Without that disambiguation the headline reads as if q5 alone is the answer.

Under TAI compression, q5's ~$1.2B IE base + q7's $13B TAI mass driver + q2's $10B converge to a full TAI architecture in the **$15-25B** range. The TAI-side reconciliation has lower load-bearing because q7.c6/c8's BAU $1.242T anchor is itself low-confidence speculative — the cross-leaf scope-claim should preserve that uncertainty rather than treating $1.242T as a decisive anchor.

**Recorded** in q5.leaf.yaml.contradictions_with on first surface. Q7 mass driver is itself conditional on q3's basalt-projectile feasibility (q3 confirms structural materials route independent of refined-ISRU maturity).

## Cross-leaf dependencies synthesis must surface

### Propellant chemistry — q2 hydrolox depends on q3 polar-ice gate

q2's aggressive-ISRU chemical scenarios use **hydrolox propellant** (q2.c2: "chemical hydrolox ascent (Isp 450 s)"). q3.c4 says the only lunar-derivable rocket-fuel hydrogen route is **polar-ice electrolysis**, with the binding gate being geological characterization pending VIPER (late-2027). q3.c5 confirms **LCH4 is structurally impossible** as bulk lunar product — q2 did not rely on lunar methane, so this is not a contradiction.

**Synthesis implication:** q2's aggressive-ISRU $994/kg late-era figure assumes the polar-ice gate clears by VIPER's late-2027 mission. Under a stall scenario where VIPER slips further or polar ice is unminable, q2's aggressive-ISRU column collapses to its Earth-imports-only column ($1,303-13,029/kg). Stall regime for q2 ≈ stall regime for q3.

### List-price-vs-internal-cost gates q6 BAU demand — cross-pass inference

**This is a cross-pass inference flagged for q8, not a finding inside q6's claims.yaml.** q6.c2 brackets BAU demand between McCalip's 3.2× cost-multiple skepticism and Handmer's 2× cost-premium optimism, and q6.c10 explicitly notes those positions map BAU vs TAI-C. q6.leaf.yaml's flagged_for_avi notes the q1-q6 coupling. The specific "$1,000/kg through 2030 → 10-20 GW" sensitivity is **synthesis-pass inference**, not encoded in q6.c1-c14.

q1.c5 establishes the structural counter-signal: Falcon 9 list prices **rising** at $500/kg/yr (Feb 2026 baseline $7,000/kg rideshare) vs q1.c1's $107-466/kg internal cost under partial-reuse. The 10-15× gap between internal cost and list price is what creates the regime ambiguity.

**Synthesis implication (to be developed in q8):** the BAU regime in q6 is conditional on which side of the internal-vs-list gap propagates to demand-driver decisions. If commercial list prices stay above $1,000/kg through 2030 (q1.c5 + competitive dynamics), BAU SDC demand likely compresses. The TAI-C regime is unaffected because it is gated by internal cost (SpaceX-internal use) and AI compute growth, not by commercial list pricing — so the **regime split is sharper than smooth interpolation would suggest.** q8 should make the list-price-vs-internal-cost regime split explicit rather than treating BAU as a single demand curve.

### φ-threshold cleared under multi-year integration ONLY

q4.c6 reports Metzger's φ ≈ 35 threshold for lunar absolute advantage at GTO. q3.c13 reports Schreiner-Sibille MRE reactor-only productivity at 100 kg O2/yr/kg reactor mass. q3.c13b is explicit: **full-plant instantaneous phi after 5-10× balance-of-plant derating is 10-20/yr — which does NOT clear 35.** Only **cumulative multi-year integration** (decade-scale operation) clears it. Year-1 economics depend on financing structure, not steady-state ISRU performance.

Synthesis must preserve the **"multi-year integration"** qualifier — shortening to "MRE clears φ threshold" without that qualifier overstates the case. Consistent with q4.c4's threshold formula and q4.c10's structural framing (compression of M_K via automation lifts φ headroom above the threshold).

## Verified consistencies

The following frameworks/figures were independently arrived at across multiple leaves and agree within stated tolerance:

- **BAU/IE/TAI/stall regime decomposition** — used by q1, q3, q4, q5, q6, q7 with compatible (non-identical) compression factors per relevant variable
- **SEP propulsion as Γ_LEO reducer** — q2 uses it for mass driver; q4 names it as the architectural requirement; q3 says structural materials (LOX, anorthite-derived Si for solar arrays) are TRL-supportive
- **Aerobraking as dominant chemical lever** — q2 quantifies (2-3× cost reduction); q4 names as alternative to SEP
- **Earth-launch internal cost trajectory** — q1's $107-466/kg partial-reuse range is consumed unchanged by q4, q5, q6, q7 as L_p denominator
- **Lunar regolith composition** — q3 framework consistent with q4's MVP design assumptions and q7's basalt-projectile material availability
- **Public-figure quote review (tier B)** — Musk, Handmer, Shotwell, Bezos, Metzger positions scoped consistently across q1, q5, q6, q7; no figure quoted to contradictory positions across leaves

## Single-leaf findings worth amplifying

### Cycle-life gap (q7.c10)

q7 surfaces a binding engineering risk independent of capital and compression: at 1 Mt/yr × 200 kg/shot × 20 yr the system requires ~100M shots; at 10 Mt/yr (q2's nameplate), ~1B shots. Demonstrated EM-launcher cycle life is ~100-1,000 shots; the Navy EMRG program was cancelled in 2021 after ~$500M with cycle-life as binding failure mode. **The 5-7 OOM gap requires an engineering breakthrough that TAI compression alone does not deliver** — engineering breakthroughs are pre-conditioned on materials science, not just automation. This binds q2's mass-driver headline more tightly than the capital question does.

### M6 12-month floor (q5.c7)

q5 identifies that even under TAI-grade time compression, the M6 milestone (first crewed sustained 12-month occupation) is by definition a 12-month minimum. TAI compresses milestone clock but cannot collapse a milestone whose definition is the integration of 12 calendar months. **Synthesis implication:** the report's "TAI architecture in months not years" framing should explicitly carve out crewed-occupation-gated milestones from the compression curve.

## Contradictions to update in leaf.yaml.contradictions_with[]

Per-leaf updates (see next pass commit):

- **q1**: add `q6` (cost-demand list-price coupling)
- **q2**: add `q3` (polar-ice gate for hydrolox), `q7` (capital scope-conditional — already recorded indirectly via q7's contradictions_with)
- **q3**: add `q2` (polar-ice gate as q2 dependency)
- **q4**: no additions (framework leaf, consistent with all)
- **q5**: q7 already recorded; add `q3` (propellant scope dependency)
- **q6**: add `q1` (list-price-vs-internal-cost coupling), `q7` (TAI-supply assumption)
- **q7**: q2 already recorded; add `q5` (base capex stacking)

## Status

✓ **No analytical contradictions found.** All disagreements are scope-mismatches or regime-conditional dependencies.
⚠ **Two regime-coupling flags load-bearing for q8 synthesis:**
- q1 list-price-vs-internal-cost gates q6 BAU demand (sharper regime split than smooth interpolation)
- q2 hydrolox aggressive-ISRU depends on q3 polar-ice gate (VIPER late-2027)
✓ **Capital scope clarified:** BAU full architecture $1.4-1.7T; TAI full architecture $15-25B.
✓ **Engineering risk amplified:** q7 cycle-life gap binds the report's headline crossover more tightly than the capital question does.

## Implication for q8 synthesis

The crossover claim now stands on two legs:
1. **Cost** — q1 + q2 + q7 chain: lunar manufacturing beats Earth launch in the TAI-grade regime at the $50/kg vs $59/kg margin (mass driver vs optimistic-late Starship).
2. **Throughput necessity** — q6 + q1: under TAI-C, SDC demand alone exceeds Earth-launch ceiling 10×, making lunar bulk mass architecturally necessary for ~50% of the SDC mass budget regardless of cost.

Under BAU, neither leg holds: cost (mass driver doesn't reach scale) AND throughput (demand fits inside Earth-launch capacity). Under stall, demand fails (q6.c7). The two-leg framing makes the synthesis sharper than a cost-only crossover.
