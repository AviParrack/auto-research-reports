---
pass: 4
kind: source-review-response
leaf: q7-mass-driver-feasibility
date: 2026-05-25
status: done
---

# Pass 4 — Claude's response to Codex audit

Codex verdict **weak**. Coverage is broad, most quotes are source-faithful, but one Tier-S quote (Wright efficiency decomposition) was contradicted by the extract on anti-hallucination check. Fixed inline.

## Accepted

- **wright-kuznetsov-kloesel-2011 efficiency decomposition (contradicted, high severity)**: Accepted. The extract verbatim is "~50% motor + ~66% power conversion + remaining losses." My source-review row originally read "~50% motor + ~7% power conversion losses" — this is a hallucinated paraphrase. Corrected inline to match the extract verbatim. Anti-hallucination check now passes. The structural finding (Wright's net 33% is TRL-grounded, lower than SP-428's 96.4%) is unaffected.

- **nasa-mass-drivers-iii-1979 system mass units (partial, medium)**: Accepted. The extract gives "3,130,000 kg." My shorthand "3.13 Mt" was ambiguous (Mt = metric tonne in steel/space-industry usage; not megaton). The system mass is 3,130 metric tons. Multiplication checks out at $1000/kg × 3.13 × 10⁶ kg = $3.13B. Corrected inline to use SI notation (3.13 × 10⁶ kg) and clarify.

- **oneill-kolm-acta-1980 incomplete (partial, medium)**: Accepted as a documented coverage limit. The 1980 Acta Astronautica paper PDF was not fetched; full Tier-S claim-by-claim review awaits. Carrying forward as a tree-pass merits-investigation item.

- **aiaa-2025-4123 incomplete (partial, low)**: Accepted as documented. Paywalled; full review awaits library access.

- **musk-mass-driver-tweet-2026 "Contradicts our analysis" verdict (weak, medium)**: Accepted. The "Contradicts" Newman-taxonomy label was wrong: the 500-1000 TW/yr claim contradicts q7 *conditional on* an assumed kg/kW mass intensity. Better Newman framing: "Different conclusion" with the mass-intensity assumption stated explicitly. Corrected inline.

- **Tier B taxonomy switch (low)**: Accepted. The Tier B quote-verdict shorthand ("Supports / Mixed / Contradicts our analysis") was non-Newman. The Newman taxonomy (Consistent / Different conclusion / Novel supporting / Merits investigation / Not relevant) is the stated framework; Tier B's per-quote framing is intentionally lighter ("Supports / Contradicts / Mixed / Not relevant" per the schemas.md schema for Tier B). I'll keep the lighter Tier-B framing because that's what schemas.md actually specifies for the per-figure quote review, but I'll explicitly cross-reference the Newman taxonomy in the row where the verdicts could be confusing.

- **handmer-mass-driver-2026 "Consistent" (partial, low)**: Accepted partially. The scalar verdict could be tightened to "Consistent (with caveats)" given the aspirational $10/kg headline. The caveats are present in the paragraph but the headline scalar verdict is too clean. Softening to "Consistent (engineering envelope) / Aspirational (headline economics)."

- **note on SP-428 96.4% (medium)**: Accepted. The "Merits investigation" verdict on this claim is the right call; not promoting the subsystem interpretation without re-extraction. Confirmed.

- **note on Metzger reconstruction provenance (low)**: Accepted. The Metzger quote was reconstructed after an X.com 402 fetch error. This provenance caveat appears in the extract reviewer notes but should be foregrounded in the Tier B review. Adding the caveat to the Metzger row inline.

## Disputed / clarified

- None substantively. All findings are valid in their narrow form. The Wright misquote was the high-severity hit and is fixed; the rest are tightening / framing improvements.

## What carries forward

1. Wright efficiency decomposition fixed in the source-review file.
2. SP-428 system mass units clarified (3.13 × 10⁶ kg).
3. Musk 500-1000 TW/yr reframed as "Different conclusion (with mass-intensity assumption)."
4. Handmer 2026 scalar verdict softened to "Consistent (engineering envelope) / Aspirational (headline economics)."
5. Metzger reconstruction provenance flagged inline.
6. Coverage limits on Acta Astronautica 1980 and AIAA 2025-4123 explicitly documented for tree-pass merits-investigation candidates.

The structural source-review conclusions survive: Wright et al. 2011 is the load-bearing modern Tier-S anchor for BAU pessimism; NASA SP-428 1979 is the canonical historical reference with a TAI-grade-equivalent projection; Pearson NIAC 2005 provides the alternative architecture; Peterkin is the credentialed industry voice; Musk's commercial commitment is real but the specific aspirational numbers are not engineering-grounded; Metzger provides academic paradigm-level validation; Handmer is the load-bearing engineer-advocate with explicit cycle-life caveats; SpinLaunch is the cautionary historical analog.
