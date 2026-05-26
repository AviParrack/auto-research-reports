---
source: nasa-fsp-2024-glenn
tier: S
reviewed_pass: 4
reviewed_by: claude+codex
---

# Source Review: NASA FSP 2024 — Fission Surface Power Project

## Summary

| Verdict | Count |
|---|---|
| Consistent | 3 |
| Novel supporting | 1 |
| Merits investigation | 1 |

## Claim 1: "40 kWe electrical power output is the demonstrator-class target"
**Verdict:** Consistent
**Why:** Establishes 40 kWe as the baseline demonstrator scale. Our calc requires 500 kWe (a 12.5x larger system), which is acknowledged as requiring either clustering or a separate larger-scale design. The 40 kWe figure is the program-of-record's near-term target.

## Claim 2: "Mass constraint: under 6 metric tons" (40 kWe FSP target)
**Verdict:** Novel supporting
**Why:** Gives a concrete 150 kg/kWe target ratio. Our calc used 250 kg/kWe (more conservative). Codex confirmed in pass-02-audit that "later concept work also discusses roughly 10 t for 40 kWe" — i.e. actual achievement may be 250 kg/kWe, validating our estimate. The 6-t-target-vs-10-t-actual divergence is itself informative.

## Claim 3: "Three Phase 1 contracts at $5M each awarded 2022" + "Target launch pad delivery: early 2030s"
**Verdict:** Consistent
**Why:** Establishes the program-of-record FSP development timeline. Our BAU 25-yr buildup has M4 (FSP installation) at year 7 of program start — slightly ahead of NASA's "early 2030s" framing if we assume program start in 2026, which is consistent.

## Claim 4: "10-year operating lifetime without human intervention"
**Verdict:** Consistent
**Why:** Direct support for our calc's 10-yr FSP lifetime assumption (one of the few components where my lifetime number is directly anchored to a published target).

## Claim 5: "Nuclear reactors can operate in permanently shadowed areas and generate continuous power during lunar nights (14.5 Earth days)"
**Verdict:** Merits investigation
**Why:** The framing of "FSP enables lunar-night operations" is a quasi-political framing that elides the alternative (PV + storage) cost comparison. For our calc, FSP is the chosen architecture, but the cost relative to a large PV-plus-storage alternative is not separately computed. Merits a follow-up on PV-plus-storage cost for a 500-kW industrial-scale lunar operation.

## Cross-reference

- Anchors the energy-supply milestone of any sustained lunar manufacturing base.
- The 250 kg/kWe ratio used in our calc is conservative vs the 150 kg/kWe NASA target; consistent with realistic-achievable per Codex.
- Pairs with duchek-2024-fsps-falcon-heavy (350-kWth microreactor) as the larger-scale design point.
- Codex anti-hallucination check: all quoted text appears verbatim in the extract.md.
