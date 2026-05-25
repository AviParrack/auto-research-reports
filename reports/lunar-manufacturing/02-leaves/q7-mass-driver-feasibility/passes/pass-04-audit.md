[codex cli ok]
```yaml
overall:
  verdict: weak
  summary: "Broad coverage and mostly source-faithful quoting, but one load-bearing Tier-S quote is contradicted by its extract. The pass is usable only after correcting the Wright efficiency decomposition and tightening coverage/taxonomy caveats."

findings:
  - target: "wright-kuznetsov-kloesel-2011"
    target_kind: claim
    verdict: contradicted
    quote: "33% total efficiency, decomposed as ~50% motor + ~7% power conversion losses"
    reason: "This quote does not appear in the extract. The extract says '~50% motor + ~66% power conversion + remaining losses'; because this is a Tier-S efficiency claim, the anti-hallucination check fails at high severity."
    severity: high

  - target: "nasa-mass-drivers-iii-1979"
    target_kind: claim
    verdict: partial
    quote: "Total: 3,130,000 kg"
    reason: "The quote supports 3.13 million kg, or 3,130 tonnes, but the review reasoning calls this '3.13 Mt.' That unit label is off by 1000x, even though the $3.1B multiplication appears to use kg correctly."
    severity: medium

  - target: "oneill-kolm-acta-1980"
    target_kind: section
    verdict: partial
    quote: "Bibliographic anchor only; full PDF not fetched in this session."
    reason: "The caveat is disclosed, but this is not a full Tier-S claim review despite the stated Tier-S review depth. Coverage is incomplete until the actual paper is extracted."
    severity: medium

  - target: "aiaa-2025-4123-mass-driver-tech"
    target_kind: section
    verdict: partial
    quote: "paywalled - full review awaits PDF fetch"
    reason: "The merits-investigation verdict is calibrated, but the source is Tier A peer-reviewed and only abstract/search-summary content was reviewed. This should remain an explicit coverage caveat."
    severity: low

  - target: "musk-mass-driver-tweet-2026"
    target_kind: claim
    verdict: weak
    quote: "500 to 1000 TW/year of AI satellites into deep space"
    reason: "Calling this 'contradicts our analysis' depends on an assumed kg/kW conversion and throughput model, not the quote alone. Better Newman framing would be Different conclusion or Merits investigation, with the mass-intensity assumption stated."
    severity: medium

  - target: "dsiac-hypervelocity-2015"
    target_kind: claim
    verdict: partial
    quote: "Adapting EMRG technology to a land-based system the size of a tank may prove unachievable."
    reason: "The quote supports a scale-limit caution, but the review's '~1000x larger scale' gloss is not in the extract and sits awkwardly beside its own 10x per-shot energy comparison. Treat as broad analogue, not scalar validation."
    severity: low

  - target: "tier-B"
    target_kind: section
    verdict: partial
    quote: "Supports / Mixed / Contradicts our analysis"
    reason: "Tier B switches away from the stated Newman taxonomy. The judgments are mostly understandable, but the labels should be mapped back to Consistent, Different conclusion, Novel supporting, Merits investigation, or Not relevant."
    severity: low

  - target: "handmer-mass-driver-2026"
    target_kind: claim
    verdict: partial
    quote: "Sintered magnet blocks 9 m long under 1000g shear and oscillating tension fatigue is not obviously feasible."
    reason: "The scalar verdict is reasonably calibrated by its caveats, but 'Consistent' may be too clean for a Tier-C advocate source with an aspirational $10/kg headline. 'Novel supporting with caveat' or 'conditional/mixed' would better preserve the hierarchy under Wright 2011."
    severity: low

notes:
  - issue: "Most other quoted snippets checked against the extracts are present or are acceptable ellipses/paraphrases."
    severity: low
  - issue: "The SP-428 96.4% efficiency claim is correctly marked Merits investigation; do not promote the subsystem interpretation without re-extraction."
    severity: medium
  - issue: "Metzger's tweet extract says the quote was reconstructed after an X.com fetch failure; surface that provenance caveat if using it as verbatim evidence."
    severity: low
```
