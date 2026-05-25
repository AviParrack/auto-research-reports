[codex cli ok]
overall:
  verdict: weak
  summary: "Sampled reviews often match the extract at the level of facts, but several review entries label paraphrases or secondary-summary text as quotes. Exact quote provenance is therefore weak."

findings:
  - target: "coutts-sowers-2025 claim 1"
    target_kind: claim
    verdict: fail
    quote: "Starship's projected cost is approximately $67-100/kg..."
    reason: "This quoted sentence does not appear in the extract. The extract supports the $30/$100/$300 per kg figures, but not this exact quoted wording."
    severity: high

  - target: "handmer-mass-driver-2026 claim 2"
    target_kind: claim
    verdict: partial
    quote: "If rocks can survive 1000 gs of acceleration (they can) then the launch track need only be 128 m long."
    reason: "The extract contains the 128 m track and ~1000 g values, but this sentence does not appear verbatim. The Consistent verdict is reasonable; the quote label is not."
    severity: medium

  - target: "metzger-2023 claim 1"
    target_kind: claim
    verdict: supports
    quote: "The propellant use ratio Γ for moving lunar product from lunar surface to LEO is approximately 14 under pure chemical reusable round-trip architecture."
    reason: "The quoted text appears in the extract and supports the Consistent verdict."
    severity: low

  - target: "sciencearray-mass-drivers claim 2"
    target_kind: claim
    verdict: weak
    quote: "A lunar mass driver several kilometers long... should be able to deliver 600,000 tons a year to L-5 at a cost of about $1 per pound."
    reason: "This exact quote does not appear in the extract, which only summarizes 600,000 tons/year to L5 at about $1/lb. The Different conclusion verdict is plausible, but the review also overstates the throughput gap: 10^9 kg/yr is not 10x 6x10^8 kg/yr."
    severity: medium

  - target: "wiki-delta-v claim 4"
    target_kind: claim
    verdict: partial
    quote: "The high-thrust tables 'assume that the Oberth effect is being used—this is possible with high thrust chemical propulsion but not with current (as of 2018) electrical propulsion.'"
    reason: "The extract mentions high-thrust Oberth assumptions, but this quoted sentence does not appear. The verdict matches the extract’s meaning, but the quote is not extract-grounded."
    severity: medium

  - target: "wiki-mass-driver claim 4"
    target_kind: claim
    verdict: supports
    quote: "under $1 of electrical energy cost per kilogram shipped to LEO"
    reason: "The quote appears in the extract, and the Consistent verdict matches the extract’s caveat that total cost exceeds electricity alone."
    severity: low

notes:
  - issue: "Several reviews say 'All quotes appear in extract.md' even when sampled quotes are paraphrases or text from secondary summaries not present in the extract."
    severity: high
  - issue: "For this corpus, verdict labels are generally directionally reasonable, but quote hygiene is unreliable unless paraphrases are explicitly marked."
    severity: medium