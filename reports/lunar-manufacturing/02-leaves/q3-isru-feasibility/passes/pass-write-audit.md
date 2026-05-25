[codex cli ok]
```yaml
overall:
  verdict: weak
  summary: "The write mostly follows the claimed technical structure, citations, and motivation-before-answer pattern, but it fails the strict numerical-trace rule in several places and has multiple calendar-year statements outside explicit regime framing."

findings:
  - target: "Every numerical statement traces to claims.yaml"
    target_kind: topic
    verdict: partial
    quote: "The 2026-2028 prospecting wave — ESA PROSPECT, Chang'e-7, JAXA-ISRO LUPEX, Korea KIGAM LUVED, and finally VIPER late-2027"
    reason: "Claims q3.c4 and q3.c14 support PRIME-1, VIPER, and water-electrolysis maturity, but claims.yaml does not support the listed 2026-2028 prospecting campaign or the named non-VIPER missions."
    severity: high

  - target: "Every numerical statement traces to claims.yaml"
    target_kind: topic
    verdict: partial
    quote: "TPR measurements on simulant give 1.10 wt% apparent oxygen yield on pure ilmenite and 0.02 wt% on highland regolith"
    reason: "Claim q3.c10 supports ~1 wt% and ~0.02 wt%, but the exact 1.10 wt% value is more specific than the claim text."
    severity: medium

  - target: "Every numerical statement traces to claims.yaml"
    target_kind: topic
    verdict: partial
    quote: "On Earth, Metalysis has scaled the process through four generations of cells"
    reason: "q3.c3 says Earth Metalysis is TRL 7+ and q3.c6 covers FFC dependence, but no claim supports 'four generations of cells'."
    severity: medium

  - target: "Every numerical statement traces to claims.yaml"
    target_kind: topic
    verdict: unsupported
    quote: "highland regolith composition assumption (Al\\(_2\\)O\\(_3\\) 21%, FeO 6%, CaO 14.5%)"
    reason: "q3.c1 supports regional oxygen fractions and canonical oxide compositions generally, but these specific oxide percentages are not present in claims.yaml."
    severity: medium

  - target: "Every numerical statement traces to claims.yaml"
    target_kind: topic
    verdict: unsupported
    quote: "pure Apollo 16 anorthositic soil (Al\\(_2\\)O\\(_3\\) ~27%, FeO ~5%, CaO ~16%)"
    reason: "No claim in claims.yaml supports the Apollo 16 composition values."
    severity: medium

  - target: "Calendar-year statements"
    target_kind: topic
    verdict: fail
    quote: "as of 2026"
    reason: "This is a calendar-year status statement outside explicit TAI-C / BAU / stall framing. The report later has a regime section, but anti-pattern #11 requires calendar-year statements to be wrapped locally."
    severity: medium

  - target: "Calendar-year statements"
    target_kind: topic
    verdict: fail
    quote: "PRIME-1 launched on IM-2 in February 2025"
    reason: "The statement is factual and claim-supported by q3.c4, but it is not wrapped in acceleration-regime framing."
    severity: low

  - target: "Calendar-year statements"
    target_kind: topic
    verdict: fail
    quote: "Sierra Space demonstrated a single reactor producing the equivalent of 140 kg O\\(_2\\) per year at vacuum-chamber conditions in August-September 2024"
    reason: "The numerical claim traces to q3.c12, but the calendar-year event is not locally framed by acceleration regime."
    severity: low

  - target: "Bury-the-lead"
    target_kind: section
    verdict: pass
    reason: "The write opens with motivation and context before the headline answer, and the headline appears early, within the expected first ~400 words."
    severity: low

  - target: "LLM transition slop"
    target_kind: topic
    verdict: pass
    reason: "The banned transition phrases are not present."
    severity: low

  - target: "Editorial voice"
    target_kind: topic
    verdict: partial
    quote: "the bottleneck"
    reason: "The exact banned phrase does not appear, but related phrasing such as 'binding gate' and 'highest-confidence' gives the report a mild editorial ranking voice. This is not a hard fail under the listed string checks."
    severity: low

  - target: "Citations"
    target_kind: topic
    verdict: pass
    reason: "Citations generally follow the report style as [source-slug]."
    severity: low

notes:
  - issue: "Several claims are source-style or training-knowledge anchored inside the write, but claims.yaml is the required trace layer; unsupported detail should either be added to claims.yaml or removed."
    severity: medium
  - issue: "The acceleration-regime decomposition section handles future projections well, but earlier standalone years still need local conditional framing or should be presented as historical evidence rather than planning dates."
    severity: medium```
