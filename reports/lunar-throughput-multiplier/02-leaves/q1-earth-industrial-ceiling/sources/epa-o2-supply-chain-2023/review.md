---
source: epa-o2-supply-chain-2023
tier: S
reviewed_pass: 6
reviewed_by: claude+gpt
---

# Source Review: EPA Oxygen Supply Chain Profile (March 2023)

## Summary

| Verdict | Count |
|---|---|
| Consistent | 1 |
| Different conclusion | 0 |
| Novel supporting | 0 |
| Merits investigation | 1 |
| Not relevant | 0 |

## Claim 1: U.S. industrial oxygen production ~10.3 Mt/yr (2019 data)

**Quote (from `extract.md`):** "Total US O2 production: ~10.3 Mt/year" — most recent comprehensive EPA figure, 2019 data.
**Cited in q1 calc as:** assumption #5 (US LOX denominator) and supports claims q1.c1, q1.c7.
**Verdict:** Consistent — but with retrieval caveat.
**Why:** The 10.3 Mt/yr figure is industry-consensus across multiple secondary citations (workspace SDC anchor, EIA-adjacent reports, market research like Mordor/Future Market Insights). The Air Liquide Baytown announcement (3.29 Mt/yr from one new facility in Texas) is internally consistent: scaling one TX facility's capacity at ~32% of *current* total US capacity matches a $10.3 Mt/yr-class national baseline.

## Claim 2 (merits investigation): Industrial O₂ vs merchant LOX vs rocket-grade LOX

**Quote:** *Not directly extracted because PDF fetch failed; this is a Codex-audit-flagged caveat.*
**Verdict:** Merits investigation
**Why:** The EPA figure is *total* industrial oxygen production, not the rocket-relevant subset (merchant liquid oxygen, with storage, transport, and load-rate capacity). The actual rocket-LOX bottleneck is somewhere below the bulk-O₂ ceiling but not quantified in this retrieval. Future re-pass should fetch the EPA HTML or use USGS / Industrial Gas Association breakdown.

## Methodological flag

The PDF returned binary streams via WebFetch during pass-01-research. The 10.3 Mt/yr figure rests on the workspace SDC anchor's prior compilation citing the EPA, not a fresh primary retrieval. **Tier S claim citation is methodologically weaker than intended.** Re-pass should attempt the HTML or alternative-primary-source fetch.
