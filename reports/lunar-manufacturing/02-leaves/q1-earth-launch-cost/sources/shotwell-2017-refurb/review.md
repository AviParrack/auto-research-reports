---
source: shotwell-2017-refurb
reviewed_pass: 4
reviewed_by: claude+codex
date: 2026-05-25
---

# Source review: Shotwell 2017 refurb statement

## Summary

| Verdict | Count |
|---|---|
| Consistent | 1 |
| Different conclusion | 0 |
| Novel supporting | 0 |
| Merits investigation | 1 |
| Not relevant | 0 |

## Claims reviewed

### Claim 1 — Refurb cost "substantially less than half" of new-build
**Quote:** "refurbishing a recycled Falcon 9 booster cost 'substantially less than half the build' of a new rocket"
**Verdict:** Consistent (with caveat)

This is the load-bearing public anchor for q1 calc's refurb-rate assumptions. "Less than half" is consistent with my early-era 30% assumption. It does not, however, tighten the bound — "<50%" doesn't tell us whether the true 2017 figure was 40%, 30%, 20%, or 10%.

**Caveat:** the statement is from April 2017, one week after the first booster reuse. It reflects the *first-of-kind* refurb cost when SpaceX was still developing the process. By 2026, after 34 reuses on a single booster (B1076), the rate has clearly compressed. SpaceX has not publicly updated this number.

### Claim 2 — Implicit: refurb cost compresses over time
**Verdict:** Merits investigation

The Falcon 9 lifecycle from 2017 (single reuse, "<50%") to 2026 (34 reuses) implies the per-cycle refurb rate compressed substantially. My calc extrapolates to 15% mid-era and 8% late-era. Without an updated SpaceX statement, these are conjectures consistent with the lifecycle pattern but not directly evidenced.

A subsequent search-for or interview with current SpaceX leadership (Shotwell still President as of 2026) could update this anchor materially. Until then, the late-era 8% figure should be treated as a working estimate, not a hard number.

## Cross-reference

- Anchors the refurb-rate variable in [pass-02-calc.py] across all three operational scenarios
- The "first booster reuse just happened" context is important — Shotwell was making this claim 9 years before the 34-reuse milestone
- For source-review breadth, additional refurb data points would help: a 2020/2022/2024 SpaceX statement on refurb cost, or third-party analysis from launch-industry trade press

## What we'd want next

- An updated public statement from SpaceX (Shotwell or Musk) on current refurb cost % — Codex's source list mentioned a 2020 Musk "rapid reusability" tweet but didn't quantify refurb.
- Bennett-type external TEA on Falcon 9 economics with current data
