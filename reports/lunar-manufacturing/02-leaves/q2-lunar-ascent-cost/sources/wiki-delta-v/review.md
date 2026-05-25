---
source: wiki-delta-v
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: Wikipedia "Delta-v budget"

## Summary

| Verdict | Count |
|---|---|
| Consistent | 3 |
| Different conclusion | 0 |
| Novel supporting | 0 |
| Merits investigation | 0 |
| Not relevant | 1 |

## Claim 1: Lunar surface to LLO 1.87 km/s
**Quote:** "From the high-thrust Earth-Moon table: 1.87 km/s"
**Verdict:** Consistent
**Why:** Direct input to my calc. q2.c1 carries this exactly.

## Claim 2: Moon surface to LEO total 5.93 km/s
**Quote:** "Moon surface to LEO-Ken: 5.93 km/s"
**Verdict:** Consistent
**Why:** My no-aerobraking total of 5.57 km/s is within 6% of this. Slight difference is due to my conservative 3.0 km/s LEO insertion vs the table's assumed transfer. Both numbers are textbook conventions; the calc carries the load.

## Claim 3: Earth surface to LEO 9.3-9.8 km/s
**Quote:** "Launch to LEO—this not only requires an increase of velocity from 0 to 7.8 km/s, but also typically 1.5–2 km/s for atmospheric drag and gravity drag"
**Verdict:** Not relevant
**Why:** q1's domain. Used for comparison but not as a calc input.

## Claim 4: Oberth-assistance assumption
**Source content (paraphrased from extract's "Key Assumption" block):** The high-thrust tables assume the Oberth effect is being used — possible with high-thrust chemical propulsion but not with current electrical propulsion (as of 2018).
**Verdict:** Consistent
**Why:** Validates my use of Oberth-style LEO insertion ΔV in the chemical case. Captured implicitly in the 3.0 km/s value for propulsive LEO insertion.

## Anti-hallucination check

All quotes verbatim from extract.md. No hallucinated content.
