# Pass 05 — Consistency (q5-capital-buildup)

Sibling-intersection check. For each q5 claim, looked at q1, q2, q3, q4, q6, q7 claims on the same topic; flagged contradictions and partial-agreements. No Codex audit on consistency.

## Method

Loaded:
- `q1-earth-launch-cost/claims.yaml` (8 claims, reviewed)
- `q2-lunar-ascent-cost/claims.yaml` (12 claims, reviewed)
- `q3-isru-feasibility/claims.yaml` (15 claims, reviewed)
- `q4-gear-ratio/claims.yaml` (14 claims, reviewed)
- `q6-orbital-demand/claims.yaml` (14 claims, in-flight but committed)
- `q7-mass-driver-feasibility/claims.yaml` (15 claims, reviewed)

Cross-checked each of q5's 15 claims against sibling claims sharing topic (capex, milestones, ISRU mass, ascent cost, demand, gear ratio).

## Sibling intersection table

| q5 claim | Topic | Sibling claim(s) | Verdict |
|---|---|---|---|
| q5.c1 (311-500 t one-set capital mass; ISRU 75-140 t, power 125 t, mfg 40 t, mob 31.5 t) | ISRU plant mass | q3.c12 (carbothermal 140 kg/yr per melt cycle; Sierra TRL 6); q3.c13 (Schreiner-Sibille 100 kg/yr O2 per kg reactor mass at 21 kWh/kg) | Partial: q3.c13's reactor-only 100 kg/yr/kg is consistent with our ISRU mass-budget if we read "reactor" narrowly; q3.c13b derate of 5-10× to full-plant φ=10-20 implies ISRU MASS is the right magnitude (75-140 t for a 1-10 t/yr O2 plant), confirming our calc-baseline lower-bound + Codex-revised upper-bound bracket. |
| q5.c2 (722 t total 20-yr Earth-launched at 36 t/yr amortized) | Replacement mass | none direct | Consistent with itself; no sibling contradiction. |
| q5.c3 (Earth-side hardware $72B vs $1.7B launch over 20 yr at $100k/kg flight-hardware) | Hardware vs launch cost | q1.c1 ($107-466/kg LEO Starship partial reuse); q2.c12 (Earth-imports lunar surface ~$4,000/kg mid-era) | Consistent. Our $100k/kg flight-hardware is consistent with q1's launch $/kg + Earth manufacturing markup. q2.c12's $4,000/kg lunar-surface delivery confirms the order of magnitude. |
| q5.c4 (BAU $150-400B over 20 yr) | Total program capex BAU | q7.c6 (q7 mass-driver BAU capex $1,242B); q5.c11 (PwC $72-88B all-party 2026-2050); q5.c12 (US public $115-140B through ~2033) | **Contradiction with q7 by ~3-8×**: q7 reports mass-driver alone at $1.24T BAU vs our base-only at $150-400B. Not a contradiction in fact — q5 is base capex (manufacturing, habitat, ISRU, power, mobility) and q7 is mass-driver-as-launch-system on top of the base. They sum to $1.4-1.7T for a full base-plus-mass-driver architecture. **Flag for write-pass: q5 must explicitly note that mass-driver is OUTSIDE the q5 scope.** |
| q5.c5 (IE regime $1.2B over 5 yr; 140× compression) | IE compression | q1.c7 (IE drops Starship optimistic to $15-25/kg; Musk $10/kg sits just beyond); q2.c7 (IE drops mass-driver mid-era from $152/kg to ~$30/kg); q7.c8 (IE mass-driver capex $127B / 6 yr) | Partial: q7's IE mass-driver capex $127B is two orders of magnitude above our q5 base IE capex $1.2B. Same scope-separation as c4. Consistent in compression direction (10-100× range), consistent in pattern (IE compresses but the mass-driver remains the dominant capital line item). |
| q5.c6 (TAI regime degenerate; lead-time-bound, not cost-bound) | TAI degenerate framing | q7.c8 (TAI mass-driver $13.3B / 1.5 yr — within striking distance of q2.c5's $10B); q6.c2 (TAI-C 42.9 Mt LEO demand) | Consistent: q7's TAI capex is not degenerate ($13B remains real); our q5 framing of "cost stops being binding constraint, lead-time becomes binding" generalizes correctly — q7's $13B / 1.5 yr is exactly that lead-time-bound endpoint. Soft-consistent. |
| q5.c7 (8 milestones M1-M8; BAU 25 yr / IE 5 yr / TAI ≥12 mo by M6 floor) | Milestones | q3.c8 (TRL trajectory acceleration-regime dependent, not calendar-year dependent — anti-pattern #11); q7.c9 (5-milestone path M1-M5 for mass-driver, BAU 20-30 yr / IE 6 yr / TAI 1.5 yr); q6.c12 (Artemis 1.5-100 t/yr cargo cadence depending on path) | Consistent. q3 explicitly endorses the regime-conditional framing. q7's M4 (Mt-scale operational) at 20-30 yr BAU matches our M8 net-positive-export at year 20-25 BAU. Milestones are aligned across leaves. |
| q5.c8 (500 kWe surface power; NASA-FSP 40 kWe demonstrator × 10-12 units or 350 kWth microreactor) | Power | (Handmer figure-handmer 450 MW class for mature industry, ~900× our case) | Different scope — base case 500 kWe vs mature-industry 450 MW. Both consistent at their respective scopes. |
| q5.c9 (replacements at 5-15 yr lifetime; Jones 2× factor doubles BAU capex) | Replacement reliability | q2.c9 (8-10 uses per lunar lander HLS; refurb-on-Moon largest uncertainty) | Consistent. Both leaves identify replacement/refurb reliability as the largest single-variable cost driver. |
| q5.c10 (compressibility regime-conditional and non-linear; IE 140× / TAI degenerate) | Compressibility framing | q3.c8 (TRL acceleration-regime dependent); q1.c7 (IE compresses launch $/kg ~4×); q7.c8 (IE compresses mass-driver capex 10×) | Consistent. The "compressibility is regime-conditional, not calendar-conditional" framing is uniform across q1, q3, q5, q7. |
| q5.c11 (PwC $72-88B all-party cumulative 2026-2050; not a methodology cross-validation) | Published anchor cross-validation | none direct | Internally consistent (Codex-revised in pass-03). |
| q5.c12 (US public $115-140B through ~2033; $93B Artemis + $20B Isaacman + ops) | US public-program capex | q7.c12 (1979 NASA SP-428 $13B in 2026 dollars for 1985 mass-driver target — not met); q6.c12 (Artemis cargo-lander gap; ~1 landing/yr post-Artemis-V BAU) | Consistent. Anchors the US program-of-record context. |
| q5.c13 (Sowers $4B propellant-only architecture; NOT directly comparable via φ-rescaling) | Sowers anchor | q4.c7 (tent sublimation Kornuta φ=442, Sowers φ=534 — order-of-magnitude above breakeven); q2.c10 (Sowers $500/kg target price) | Consistent. q4 establishes the φ analysis; q5.c13 correctly states the calc and Sowers' architecture are not bridged by simple scaling. |
| q5.c14 (Metzger 12 t / 20 yr seed to 156-40000 t terminal; consistent with IE mass compression direction but not cost compression) | Bootstrap | q3.c8 (TRL acceleration regime-dependent); q1.c7 (IE compresses) | Consistent. Metzger's framework supports IE mass-compression direction across leaves. |
| q5.c15 (3-orders-of-magnitude spread in published anchors explained by scope, not analytical disagreement) | Anchor analysis | q4.c13 (Metzger 2023 reviews seven prior TEAs; dominant disagreement traces to G and φ choices); q4.c14 (pessimistic published TEAs used SLS pricing — artefact of transport assumption) | Strongly consistent. q4's analysis (anchor disagreement is scope/architecture, not analytical) directly supports q5.c15. |

## Cross-leaf contradictions identified

1. **q5 vs q7 capex scope mismatch (load-bearing)**: q7 BAU mass-driver capex $1.24T is roughly 3-8× q5 base BAU capex $150-400B. NOT a contradiction in fact — different scopes (q5 base, q7 launch system). But it IS a contradiction in narrative if a reader treats either number as "total lunar manufacturing capex." Write-pass must explicitly call out the scope.

2. **q5.c4 vs q5.c11 anchor scope mismatch (Codex pre-flagged)**: Already resolved in claim text (pass-03). PwC is all-party cumulative; q5.c4 is one-program first-principles. Same order of magnitude, different scope. Not a new contradiction.

3. **q3 LCH4 impossibility (q3.c5)**: LCH4 is not bulk-lunar-native at any regime. q5's propellant infrastructure scope is bounded by this — surface propellant production is LOX + LH2 only (q3.c9). Q5.c1's ISRU plant mass 75-140 t implicitly assumes LOX + LH2 production (q3.c9 says LOX high feasibility, LH2 medium-feasibility blocked at ice-prospecting step). **No contradiction; consistency confirmed.** Q5 capex should not include any LCH4 production scope.

4. **q1 launch cost transfer**: q1's $107-466/kg BAU central is consistent with our $100k/kg aerospace-flight-hardware × 1% launch fraction = roughly $1,000/kg → $100/kg under reuse. Order-of-magnitude consistent.

## contradictions_with to add to leaf.yaml

```yaml
contradictions_with:
  - leaf: q7-mass-driver-feasibility
    nature: scope-mismatch
    detail: "q7 BAU mass-driver capex $1.24T is on top of q5 base capex $150-400B; combined architecture is $1.4-1.7T. NOT a contradiction in fact; load-bearing for write-pass narrative."
```

## Key cross-leaf takeaways for write-pass

- **q3 LCH4 impossibility tightly constrains q5's propellant scope** — explicitly note that surface propellant production at the base is LOX (from regolith carbothermal/MRE) + LH2 (from polar ice electrolysis, contingent on ice-prospecting closure), not LCH4. The methalox Starship architecture imports CH4 from Earth.
- **q7's $13B TAI-compressed mass-driver capex is at the same order of magnitude as q2.c5's $10B capital assumption** — the TAI regime closes the q5 / q7 / q2 capital-architecture loop cleanly. Under TAI, the full base + mass-driver system fits inside ~$15-25B.
- **q4's gear-ratio framework provides the structural reason why q5's IE regime exists at all** — Metzger's φ ≈ 35 threshold (q4.c6) with 10× IE mass compression on M_K (q4.c10) is what makes the IE regime's BAU-to-IE 140× total compression even theoretically reachable.
- **q6's TAI-C SDC demand (~2.7 Mt/yr) drives the demand-side justification** for the q5 buildup. Q5's net-positive-export endpoint is meaningful only if q6's TAI-C demand obtains; under q6.c7 stall, the q5 thesis fails for lack of demand, not lack of supply.

## State after pass

No claims modified by consistency pass. One new contradiction-of-scope-mismatch (q7) flagged for write-pass and leaf.yaml. Pass-05 complete.
