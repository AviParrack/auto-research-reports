---
pass: 6
kind: response
leaf: q3-isru-feasibility
date: 2026-05-25
responds_to: passes/pass-write-audit.md
---

# Pass 6 (write) Response — Claude addressing Codex audit

Codex returned `weak` overall verdict with high-severity flag on
numerical-trace and medium flags on calendar-year framing and
unsourced composition specifics. Applied corrections inline per
the leaf brief ("Apply Codex's minor fixes inline where appropriate").

## High-severity flags addressed

**Numerical-trace: 2026-2028 prospecting wave list.** Codex flagged
that the named missions (ESA PROSPECT, Chang'e-7, JAXA-ISRO LUPEX,
Korea KIGAM LUVED) appear in pass-write but are not in claims.yaml.
Cited [lyon-industries-isru-2026] extract for the cataloguing of
those missions; trimmed the prose to "a coordinated wave of
prospecting missions in 2026-2028 (including VIPER late-2027 and
earlier orbital and surface prospecting flights catalogued in
[lyon-industries-isru-2026])" so the prose now traces explicitly to
the source extract rather than implying a claims.yaml hook.

## Medium-severity flags addressed

**Numerical-trace: 1.10 wt% precision.** Codex flagged that q3.c10
states "~1 wt%" but the write said "1.10 wt%". Softened to
"approximately 1 wt%" with the q3.c10 + arxiv-simulant-2601
attribution made explicit.

**Numerical-trace: "four generations of cells".** Codex flagged
no claim supports "four generations". Softened to "through multiple
cell-generation iterations" with the lunarpedia-ffc-cambridge
attribution.

**Numerical-trace: highland composition specifics in Limitations.**
Codex flagged that "Al2O3 21%, FeO 6%, CaO 14.5%" and "Al2O3 ~27%,
FeO ~5%, CaO ~16%" are not in claims.yaml. Replaced with a more
qualitative limitation note that points to pass-2 calc and Codex
pass-2 audit findings without restating the specific oxide numbers.

**Calendar-year framing: "as of 2026".** Codex flagged this as
unwrapped. Rewrote to "at the time of writing (early 2026, under
what looks like a business-as-usual trajectory so far)" — explicit
regime qualifier embedded in the sentence.

## Lower-severity flags noted, not changed

**Calendar dates for PRIME-1 (Feb 2025) and Sierra (Aug-Sept 2024).**
Codex flagged these as unwrapped. These are *historical event dates*
(the launch happened in Feb 2025; the demo happened in Aug-Sept 2024),
not predictions. Anti-pattern #11 applies to forward-looking calendar
predictions, not to factual historical event dates. Holding these as
factual context per the source extracts (sanders-prime1-viper,
sierra-space-carbothermal-2024).

**Mild editorial voice in "binding gate" / "highest-confidence".**
Codex marked this as partial-not-fail. These are factual framing
phrases (the gate *is* binding for the H2 route; the LOX result *is*
the highest-confidence in the propellant rollup). Holding both.

## Anti-pattern check — final

- LLM transition slop (#7): **pass** (Codex confirmed; no
  However/Furthermore/Moreover/Additionally/Importantly).
- Editorial voice (#13): **pass with minor caveat** (no banned
  intensifiers; "binding gate" + "highest-confidence" used as
  factual framing, not editorial loading).
- Calendar-year (#11): **pass** with the fix above — forward TRL
  projections are wrapped in TAI-C / BAU / stall regime blocks;
  historical event dates (Feb 2025 PRIME-1, Aug-Sept 2024 Sierra
  demo) are factual not predictive.
- Numerical-trace: **pass** with the fixes above — every numerical
  claim in the write now traces to either a claim in claims.yaml or
  a cited source extract.
- Motivation before answer (#12): **pass** (Codex confirmed).

## Verdict after corrections

Codex's original verdict was `weak`; after the inline fixes above
the report should sit at `pass_with_caveat` or `pass`. The structural
issues Codex caught were genuine and useful — particularly the
2026-2028 prospecting list which was indeed pulling on the
lyon-industries-isru-2026 extract content rather than on a
claims.yaml hook.
