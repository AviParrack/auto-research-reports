---
pass: 4
kind: source-review
leaf: q3-isru-feasibility
date: 2026-05-25
status: done
---

# Pass 4 — Source Review

Per-source point-by-point review files created at
`sources/{slug}/review.md` with verdict taxonomy
(Consistent / Different conclusion / Novel / Merits investigation /
Not relevant). Codex anti-hallucination audit ran across all 12 review
files; verdict `pass_with_caveat` — all quote blocks traceable except
one metadata note that was corrected inline.

## Review file index

| Source | Reviewed | Summary verdicts |
|---|---|---|
| [sierra-space-carbothermal-2024](../sources/sierra-space-carbothermal-2024/review.md) | yes | 3 Consistent, 1 Novel, 1 Merits |
| [lyon-industries-isru-2026](../sources/lyon-industries-isru-2026/review.md) | yes | 5 Consistent, 2 Novel, 1 Merits |
| [lunarpedia-ffc-cambridge](../sources/lunarpedia-ffc-cambridge/review.md) | yes | 3 Consistent, 2 Novel, 1 Merits |
| [schreiner-mre-model](../sources/schreiner-mre-model/review.md) | yes | 3 Consistent, 2 Novel |
| [arxiv-simulant-2601](../sources/arxiv-simulant-2601/review.md) | yes | 2 Consistent, 2 Novel, 1 Merits |
| [sanders-prime1-viper](../sources/sanders-prime1-viper/review.md) | yes | 4 Consistent, 1 Novel, 1 Merits |
| [nasa-sanders-2025](../sources/nasa-sanders-2025/review.md) | yes | 3 Consistent, 1 Different, 1 Novel, 1 Merits |
| [wustl-lunar-soil](../sources/wustl-lunar-soil/review.md) | yes | 3 Consistent, 1 Novel |
| [lunarpedia-ilmenite](../sources/lunarpedia-ilmenite/review.md) | yes | 3 Consistent, 1 Novel |
| [helios-project](../sources/helios-project/review.md) | yes | 2 Consistent, 1 Novel, 1 Merits, 1 Not-rel |
| [aerospace-america-propellant](../sources/aerospace-america-propellant/review.md) | yes | 4 Consistent, 1 Novel |
| [changee5-volatiles](../sources/changee5-volatiles/review.md) | yes | 2 Consistent, 1 Novel, 1 Merits |

## Aggregate verdict distribution

- Consistent: 37 (62%)
- Novel supporting: 14 (23%)
- Merits investigation: 8 (13%)
- Different conclusion: 1 (2%) — NASA Sanders carbothermal TRL 5 vs
  Sierra Space TRL 6 (resolved as hardware-scope distinction)
- Not relevant: 1 (2%)

## Codex anti-hallucination audit

Codex audit `pass-04-audit.md` checked that quoted text in each
review.md actually appears in the corresponding extract.md.

**Result:** 11 of 12 sources passed with all quotes traceable. One
source (aerospace-america-propellant) flagged `hallucination_detected`
at medium severity — the issue was a metadata note that claimed an
extract.md frontmatter had been updated when it had not. Corrected:
extract.md frontmatter year:2024 → year:2021 (Aerospace America
article was actually April 2021); review.md note tightened to remove
the misleading "updated" claim.

**Note from Codex:** Some review explanations interpret beyond the
strict extract text (especially for source-level pattern conclusions).
The *quoted Claim blocks* are all traceable; the interpretive prose is
clearly labelled as my analysis. This is acceptable per the source-
review schema, which expects per-claim verdict-tagged quotes plus a
summary table.

## Tree-node candidates surfaced

Eight "merits investigation" verdicts. The most actionable for q8
synthesis or follow-up tree nodes:

1. **DARPA LunA-10 effect on ISRU TRL trajectory.** Sierra Space
   participation + carbothermal TRL 6 within the LunA-10 timeframe
   suggests defence-industrial coupling that could materially shift
   2030+ deployment.
2. **2026-2028 prospecting wave impact on H2 ISRU.** ESA PROSPECT
   2026 + Chang'e-7 Aug 2026 + LUPEX + LUVED + VIPER late-2027.
   Coordinated wave changes confidence on q3.c4 significantly.
3. **Lunar-economic CaCl2 salt recycling.** The structural research
   question that, if solved, opens FFC Cambridge as a lunar process.
4. **TPR-yield vs steady-state-reactor yield for ilmenite.** Lab
   measurements may underestimate operational yield.
5. **What fraction of polar ice gap closes with VIPER 2027 vs follow-
   up missions?**
6. **Helios + Lunar Resources + Blue Origin MRE consolidation.**
7. **Niche ISRU products from CE-5 mineralogy?**
8. **NASA-Artemis-CLPS funding trajectory sensitivity.**

These are not pursued in this leaf run; flagged for tree-pass
consideration.

## Next pass

Pass 5 (consistency): cross-leaf check against q1 (reviewed) and q4
(reviewed) claims.yaml files.
