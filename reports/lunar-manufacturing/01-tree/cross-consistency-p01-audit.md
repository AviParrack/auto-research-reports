---
pass: cross-consistency
batch: p01
date: 2026-05-26
auditor: codex
audit_target: cross-consistency-p01.md
---

[codex cli ok]

```yaml
overall:
  verdict: pass_with_caveat
  summary: "Most cross-consistency resolutions are supported. Main caveats: q5+q7 capex stacking is directionally right but needs scope wording, and the q1↔q6 list-price coupling is weaker than the artifact claims because q6 claims do not explicitly encode the commercial-list-price threshold."

findings:
  - target: "mass-driver-capital"
    target_kind: "section"
    verdict: pass_with_caveat
    quote: "q7.c8: BAU ($1,242B / 20-30 yr), Industrial Explosion ($127B / 6 yr), TAI-grade ($13.3B / 1.5 yr)... q2's $50/kg headline is achievable only under TAI-grade compression"
    reason: "The TAI-conditional framing is accurate per q7.c8 and q7.c11. Caveat: q2.c5 itself only says '$10B capital assumption' and 'late-era'; the conditioning is cross-leaf synthesis, not explicit in q2."
    severity: medium

  - target: "q2-hydrolox-q3-polar"
    target_kind: "section"
    verdict: pass
    quote: "q2.c2: Under chemical hydrolox ascent (Isp 450 s)... q3.c4: The only lunar-derivable rocket-fuel hydrogen route is polar-ice electrolysis."
    reason: "q2 does use hydrolox, and q3 explicitly makes polar ice the lunar hydrogen gate. The dependency is valid."
    severity: low

  - target: "no-lch4-contradiction"
    target_kind: "section"
    verdict: pass
    quote: "q3.c5: LCH4 is therefore not a BULK lunar-native ISRU product... q2 only mentions methalox as a comparison to hydrolox."
    reason: "q2 does not assume bulk lunar methane; it only compares methalox/hydrolox as propellant choices. The artifact is right that this is not a contradiction."
    severity: low

  - target: "q5-q7-capex-stacking"
    target_kind: "section"
    verdict: pass_with_caveat
    quote: "q5.c1 base components: habitat, fission power, ISRU plant, mobility, manufacturing complement, infrastructure. q7.c6: BAU capital decomposition for a 1 Mt/yr... mass driver lands at approximately $1,242B total."
    reason: "The additive framing is supported by component scope: q5 costs the base and q7 costs the mass-driver launch system. q5 leaf metadata also explicitly says q7 is on top. Caveat: claims like q5.c4/q5.c15 call q5 a 'total' or 'full-scope' net-positive-export base, so synthesis should say 'base-only + mass-driver launch system' to avoid ambiguity."
    severity: medium

  - target: "list-price-vs-internal-cost"
    target_kind: "section"
    verdict: weak
    quote: "q6.c2: McCalip 3.2x cost-multiple skepticism and Handmer 2x cost-premium optimism bracket the BAU-to-TAI-C transition."
    reason: "q6 is explicit that demand is regime/cost-sensitive, but claims.yaml does not explicitly say BAU demand assumes q1 internal-cost-level pricing propagates to commercial list prices. The artifact's specific '$1,000/kg through 2030' and '10-20 GW' quote is not present in q6 claims or leaf.yaml; leaf.yaml only flags the coupling generally."
    severity: medium

  - target: "missed-contradictions"
    target_kind: "section"
    verdict: pass_with_caveat
    quote: "q3.c13b: full-plant phi of 10-20 per year... cumulative over plant lifetime: phi >> 35; q4.c6: Metzger's phi ≈ 35 threshold..."
    reason: "I did not find a hard missed contradiction in the claim texts. The closest missed caveat is q3↔q4 phi wording: instantaneous phi 10-20 does not clear 35; only cumulative multi-year integration does. The artifact captures this, but synthesis must not shorten it to 'clears phi threshold' without the multi-year qualifier."
    severity: low

notes:
  - issue: "q7.c6 has low confidence and q7.c8 is speculative. The artifact should preserve that uncertainty when using $1.242T BAU and $13.3B TAI as decisive reconciliation anchors."
    severity: medium
  - issue: "The q6 list-price coupling should be downgraded from 'captured by q6' to 'cross-pass inference flagged for q8'; otherwise it overclaims what q6 claims.yaml says."
    severity: medium
  - issue: "No bulk lunar methane assumption was found in q2 claims.yaml."
    severity: low
```

## Claude response

Three medium-severity calibrations accepted and fixed inline in cross-consistency-p01.md:

- **q5+q7 capex stacking** — added explicit "base + mass-driver launch system" / "base only" disambiguation language; added acknowledgement that q7.c6/c8 are themselves low-confidence speculative anchors.
- **List-price-vs-internal-cost** — reframed from "captured by q6" to "cross-pass inference flagged for q8 synthesis." The specific $1000/kg/2030 threshold is now labeled as synthesis-pass inference, not q6 claim.
- **φ-threshold** — strengthened wording to make explicit that instantaneous phi 10-20 does NOT clear 35; ONLY cumulative multi-year integration does. Synthesis must preserve the multi-year qualifier.

Three lower-severity findings (q2-hydrolox-q3-polar pass; no-lch4-contradiction pass; missed-contradictions pass) — no changes needed.

The audit overall verdict pass_with_caveat is accepted. Cross-consistency artifact is ready for synthesis consumption.
