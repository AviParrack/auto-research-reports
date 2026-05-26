---
source: caltech-sspd-mankins-niac
tier: A
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: Mankins SPS-ALPHA NIAC + Caltech SSPD-1

**Overall verdict:** Consistent

**Two-sentence summary:** SPS-ALPHA is the canonical reference design
for modular SBSP and is the most-cited bracket for kg/kW mass intensity
(1-6.7 kg/kW). Caltech SSPD-1's January 2023 launch + March 2023 MAPLE
wireless power transfer milestone is empirical validation of SBSP's
technical-feasibility gate; q6.c4 inherits the kg/kW range as the
load-bearing mass-intensity assumption.

## Key claims

- **Module mass 50-200 kg, mass-produced** → Consistent. Establishes the architectural premise that SBSP scaling is module-production scaling, not single-system development. Directly motivates the 5 kg/kW intermediate figure in q6.c4.

- **System scale 1-2 GW per reference design** → Consistent. The 100 GW TAI-C scenario in q6.c4 implies ~50-100 SPS-ALPHA-class systems, which is at the upper edge of plausibility but not unprecedented in NIAC literature.

- **Mass per kW 6.7 (2015 SOA) → 1 (SPS-ALPHA target)** → Consistent. The 6.7× range bracket is preserved as q6.c4's mass-intensity uncertainty; my 5 kg/kW midpoint sits within bracket.

- **80,000 t per 4 GW reference at 20 kg/kW baseline** → Consistent and load-bearing. Mankins's most-citable figure for reasonable launch-mass demand under conservative assumptions. Cross-validates the 100 GW × 5 kg/kW = 500,000 t TAI-C scenario.

- **SSPD-1 = 50 kg launched Jan 2023; MAPLE March 2023** → Consistent. Empirical validation that wireless power transfer in orbit is no longer a paper-design barrier.

## Anti-hallucination check

Quotes appear in extract.md ✓. NIAC report is the primary source; Wikipedia SBSP entry cross-validates 6.7 kg/kW figure. SSPD-1 launch + MAPLE milestone are widely reported in Caltech press releases and SpacePolicy/IEEE coverage.

## Notes

Mankins NIAC remains the most-cited mass-intensity reference for SBSP
even 14 years post-publication. Cross-leaf consistency: q3-isru's
silicon-from-MRE conclusion partly addresses the panel mass under
lunar-sourced supply scenarios — the Si fraction of SPS-ALPHA could
in principle be lunar-derived. Flag for q8 synthesis.
