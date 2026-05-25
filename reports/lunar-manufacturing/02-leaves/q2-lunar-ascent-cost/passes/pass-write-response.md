---
pass: 6
kind: response
leaf: q2-lunar-ascent-cost
date: 2026-05-25
agent: claude-opus-4-7
---

# Response to Codex audit on the write pass

Codex audited the leaf write ([pass-write-audit.md](pass-write-audit.md)) with verdict **weak** — same headline as on the calc pass. The structural finding (motivation → where-it-fits → headline → body) was judged "pass"; the calibration to q1 was judged "supports" with the arithmetic verified. The "weak" verdict came from one high-severity internal contradiction and several inline-attribution gaps.

## High-severity fix applied

**The "Earth-imports cheaper than aggressive-ISRU" claim was backwards.** I wrote that late-era Earth-imports-only ($1,303/kg) is "cheaper than" late-era aggressive-ISRU ($994/kg) "by a thin margin" — but $1,303 > $994, so Earth-imports is *more expensive*, not cheaper. The structural point I was trying to make (the gap narrows in the late era as terrestrial L_p falls) survives the correction, but the directional language was wrong. **Fixed inline.**

## Medium-severity fixes applied

1. **Headline range ambiguity:** the $50-$33,000/kg headline includes the no-aerobraking cases. The aerobraking-only envelope is $50-$13,029. Both labeled explicitly in the headline section.

2. **Inline attribution in headline scenario bullets:** added [q2.c3], [q2.c5], [q2.c10], [q2.c12] claim IDs in the headline scenarios and added source slug references.

3. **Cost decomposition section:** original prose had uncited component percentages. Replaced with explicit per-line numbers from [pass-02-calc.py](pass-02-calc.py) with [q2.c3] citation.

4. **Methalox Isp/fractions:** noted these are derived from the same Tsiolkovsky calculation, linked to [pass-02-calc.py](pass-02-calc.py).

5. **Limitations section's SEP cross-check:** added [q2.c5] and [metzger-2023] citations to the back-of-envelope $36/kg figure.

## Low-severity items not separately rewritten

- "Aerobraking is the load-bearing architectural lever" is close to the flagged "the dominant lever" voice pattern. I judge it acceptable because the claim is specifically about a load-bearing structural assumption, not editorialising about which factor "matters." "Load-bearing" is engineering jargon for "the thing the result depends on."
- Mass-driver-results section's $5-10/kg + $40-50/kg breakdown cites [q2.c11] but not [q2.c5] explicitly. Acceptable because the surrounding sentence's table at the top of the section is [q2.c5].
- Several table cells are not inline-cited. The site renderer attaches captions to tables, and the table itself was introduced with [q2.c3] inline; I judge this sufficient.

## Net assessment

The arithmetic error (Earth-imports cheaper than aggressive-ISRU) was the load-bearing fix; the remaining items were attribution-hygiene improvements. The headline range, the calibration to q1, and the structural finding (mass driver + SEP is the only architecture that closes within 2× of optimistic-late Starship) all survive.
