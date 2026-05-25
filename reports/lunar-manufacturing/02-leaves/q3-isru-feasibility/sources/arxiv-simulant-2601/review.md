---
source: arxiv-simulant-2601
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: Physicochemical Properties of Lunar Regolith Simulant for ISRU O2 Production

## Summary

| Verdict | Count |
|---|---|
| Consistent | 2 |
| Different conclusion | 0 |
| Novel supporting | 2 |
| Merits investigation | 1 |
| Not relevant | 0 |

## Claim 1 — Ilmenite hydrogen reduction yield 1.10 wt%

**Quote:** "Ilmenite produces an apparent yield of 1.10 wt% oxygen
under hydrogen reduction conditions" at 900°C via FeTiO3 + H2 → Fe +
TiO2 + H2O.

**Verdict:** Consistent (q3.c10)

**Why:** Direct measurement support for ilmenite reduction yield. Note
"apparent" — the authors are signalling TPR (temperature-programmed
reduction) experimental method, which gives a yield bound dependent
on heating rate and residence time. Per Codex audit, q3.c10
confidence held at medium-high not high to acknowledge simulant
proxy + TPR limitation.

## Claim 2 — Highland yield 0.02 wt%

**Quote:** "Highland simulant (LHS-2) achieved only approximately 0.02
wt% oxygen extraction despite low ilmenite, attributed to distributed
Fe-bearing silicate and glassy phases."

**Verdict:** Consistent (q3.c10)

**Why:** Direct support for the mare-vs-highland yield gap (50× ratio
on simulant). The explanation — "distributed Fe-bearing silicate and
glassy phases" — strengthens the argument that highland H2 reduction
is fundamentally yield-limited, not just process-limited.

## Claim 3 — Polar yield 0.01 wt%

**Quote:** LSP-2 yielded "0.01 wt%" oxygen.

**Verdict:** Consistent (q3.c10)

**Why:** Polar regolith is even worse for ilmenite-route than
highland; reinforces that polar deployment needs whole-regolith
processes (MRE / carbothermal) and/or water electrolysis.

## Claim 4 — Process implication for highland deployment

**Quote:** "Oxygen extraction behavior in realistic lunar regolith is
governed by whole-regolith response rather than ilmenite content
alone, supporting processing strategies beyond ilmenite-selective
beneficiation for highland/polar regions."

**Verdict:** Novel supporting (q3.c1, q3.c10)

**Why:** A research-level statement endorsing the process-diversity
axis (carbothermal, MRE) over the historical ilmenite-focus. Direct
support for the framework framing in my calc.

## Claim 5 — Simulant mineralogy table

**Quote:** "LHS-1 & LHS-2: Anorthosite 74.4%, Glass-rich Basalt 24.7%,
Ilmenite 0.4%…"

**Verdict:** Novel supporting

**Why:** Specific simulant mineralogy useful for pass-2 composition
reconciliation. The LHS simulants are mid-mafic highland mixes (not
pure anorthosite), which means my pass-2 highland composition (FeO 6,
Al2O3 21) is actually closer to LHS simulant than to Apollo 16
anorthosite. Modest reconciliation gain.

## Claim 6 — TPR experimental limitations

**Verdict:** Merits investigation

**Why:** TPR (temperature-programmed reduction) yields are typically
lower bounds for steady-state operation in a real reactor with
extended residence time and optimized flow. Could spawn tree node:
"What's the gap between TPR-measured yield and steady-state-reactor
yield for ilmenite + hydrogen + lunar simulant?"
