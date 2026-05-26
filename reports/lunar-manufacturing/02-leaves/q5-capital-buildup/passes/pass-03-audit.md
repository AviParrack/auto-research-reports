[codex cli ok]
```yaml
overall:
  verdict: weak
  summary: "The reconciliation has useful scope distinctions, but several 'Consistent' verdicts are too generous. PwC is the key failure: the 73B vs 72-88B match is mostly an artifact of selecting the author's no-dev hardware subtotal and comparing it to an all-party market forecast."

findings:
  - target: "Zubrin Moon Direct"
    target_kind: section
    verdict: partial
    quote: "Our IE-regime bracket of $1.2-3B is comparable to this $9.9B figure under the same scope."
    reason: "The scope-mismatch diagnosis is fair: Zubrin is minimal presence/propellant, not manufacturing/export. But the comparison mixes a full-M8 IE result with a minimal-presence architecture, so 'consistent' should be framed only as a lower-bound sanity check, not convergence."
    severity: medium

  - target: "Metzger 2013 bootstrap"
    target_kind: section
    verdict: partial
    quote: "if 12 t is the seed, and 41 t is the full Earth-launched mass to reach the high-throughput endpoint"
    reason: "Metzger really does model 41 MT total landed mass for the high-throughput case, and the Gen 3+ electronics/local-production assumption supports the idea that most later capital is lunar-made. The overreach is treating that as validated cost compression: Metzger excludes development cost, failure/replacement realism, and detailed terrestrial supply-chain closure."
    severity: medium

  - target: "Sowers 2021 commercial"
    target_kind: section
    verdict: weak
    quote: "If I rescale my calc with Sowers' φ = 534 ... my ISRU plant mass falls from 75 t to ~3 t"
    reason: "The qualitative φ-architecture argument is defensible: tent sublimation and robotic propellant-only operations are a different architecture. The numeric bridge is weak because φ is lifetime product per capital mass, so 75 t -> 3 t is not valid without matching lifetime, output, and product definition; the $5-15B bridge is mostly assumed."
    severity: high

  - target: "Isaacman 2026 NASA"
    target_kind: section
    verdict: partial
    quote: "$20B over 7 yr ≈ $2.9B/yr sustained matches our BAU launch+hardware figure of $73B over 20 yr ≈ $3.6B/yr"
    reason: "The anchor is useful for M6 surface-base scale, but annual-rate matching is not strong normalization. Isaacman's figure is incremental surface-base spend on top of Artemis transport/program costs, while the author's $73B is a no-dev launch+hardware subtotal for a one-program manufacturing/export base."
    severity: medium

  - target: "PwC 2026 cumulative"
    target_kind: section
    verdict: fail
    quote: "PwC's $72-88B all-party / all-infrastructure / 24-yr cumulative aligns surprisingly well with our BAU launch+hardware figure of $73B over 20 yr."
    reason: "This is not apples-to-apples. PwC is all-party cumulative infrastructure across 2026-2050; the author's $73B is one engineered base over 20 years with development stripped out. The agreement is created by choosing the author's hardware-without-dev subtotal instead of the stated BAU $150-400B program capex."
    severity: high

  - target: "PwC within 20% claim"
    target_kind: claim
    verdict: unsupported
    quote: "The agreement is within ±20% ... a real convergence signal."
    reason: "This is artifact, not strong cross-methodology convergence. PwC includes multiple actors and transportation-heavy market infrastructure; the author's comparable total would be the full BAU range, not the selected $73B subtotal."
    severity: high

  - target: "MacDonald CSIS / SEI ceiling"
    target_kind: section
    verdict: weak
    quote: "the gap is roughly explained by the difference between commercial-Starship-launch ... and SLS-class transport"
    reason: "Using SEI/Apollo as a pessimistic historical ceiling is reasonable. But launch-cost delta cannot explain the gap inside the author's own model, where launch is only about $1.7B and hardware/dev dominate; 'consistent' should be downgraded to contextual upper-bound."
    severity: medium

  - target: "Handmer trillion-dollar buildout"
    target_kind: section
    verdict: partial
    quote: "Handmer's trillion-dollar framing is for a much larger end-state than our minimum-net-positive-export base."
    reason: "The scope-normalization is mostly defensible: Handmer is discussing mature AI-compute/space-factory scale, not the author's minimum base. But the anchor does not validate the BAU/IE bracket; it is merely non-contradictory at a later milestone."
    severity: low

notes:
  - issue: "Too-generous 'Consistent' verdicts: PwC should be fail/unsupported, Sowers weak, MacDonald weak, Zubrin partial, Isaacman partial, Handmer partial. Metzger is the strongest technical compression counterpoint but still not a cost validation."
    severity: high
  - issue: "The BAU-without-dev = $73B comparison to PwC $72-88B is scope-mismatched: one-program manufacturing base vs all-party lunar market infrastructure, and no-dev subtotal vs cumulative investment forecast."
    severity: high
  - issue: "External checks used: PwC page https://www.pwc.fr/en/publications/2026/01/lunar-market-assessment.html ; SpaceQ PwC summary https://spaceq.ca/pwc-report-lunar-economy-projected-to-generate-up-to-us127-billion-by-2050/ ; Metzger arXiv https://arxiv.org/abs/1612.03238"
    severity: low
```