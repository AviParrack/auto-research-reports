[codex cli ok]
```yaml
overall:
  verdict: pass_with_caveat
  summary: "All claim-level Quote blocks are traceable to the provided extracts as verbatim text or close paraphrase. Caveat: one Aerospace America metadata/date note contains a quoted statement not present in its extract and contradicts the extract metadata."

findings:
  - target: "sierra-space-carbothermal-2024"
    target_kind: source
    verdict: pass
    reason: "all quotes traceable"
    severity: low
  - target: "lyon-industries-isru-2026"
    target_kind: source
    verdict: pass
    reason: "all quotes traceable"
    severity: low
  - target: "lunarpedia-ffc-cambridge"
    target_kind: source
    verdict: pass
    reason: "all quotes traceable; Metalysis wording is paraphrased but supported by the extract's Generations 1-4 statement"
    severity: low
  - target: "schreiner-mre-model"
    target_kind: source
    verdict: pass
    reason: "all quotes traceable"
    severity: low
  - target: "arxiv-simulant-2601"
    target_kind: source
    verdict: partial
    reason: "all Quote blocks are traceable, but the non-quoted Claim 6 rationale about TPR experimental limitations is not supported by extract text"
    severity: low
  - target: "sanders-prime1-viper"
    target_kind: source
    verdict: pass
    reason: "all quotes traceable"
    severity: low
  - target: "nasa-sanders-2025"
    target_kind: source
    verdict: pass
    reason: "all quotes traceable"
    severity: low
  - target: "wustl-lunar-soil"
    target_kind: source
    verdict: pass
    reason: "all quotes traceable"
    severity: low
  - target: "lunarpedia-ilmenite"
    target_kind: source
    verdict: pass
    reason: "all quotes traceable; verdict wording in Claim 3 is messy but resolves to Consistent and matches the extract"
    severity: low
  - target: "helios-project"
    target_kind: source
    verdict: pass
    reason: "all quotes traceable"
    severity: low
  - target: "aerospace-america-propellant"
    target_kind: source
    verdict: hallucination_detected
    reason: "claim quotes are traceable, but the review note quotes 'The checked article is dated April 1, 2021, not 2024,' which is not in extract.md; the note also says extract.md was updated to year:2021, while the provided extract still says year: 2024 and 'article was 2024'"
    severity: medium
  - target: "changee5-volatiles"
    target_kind: source
    verdict: pass
    reason: "all quotes traceable as close paraphrases"
    severity: low

notes:
  - issue: "Some review explanations go beyond the extract text, but the quoted Claim blocks themselves generally remain traceable."
    severity: low
  - issue: "Lyon and NASA Sanders quote thermal-input efficiency; any use as wall-plug efficiency is an interpretation rather than directly quoted source language."
    severity: low```
