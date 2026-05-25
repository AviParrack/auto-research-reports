[codex cli ok]
overall:
  verdict: weak
  summary: "Core ranges mostly trace to claims.yaml and the q1 calibration is accurate, but the draft fails the inline numerical-attribution standard in several sections. It also contains one high-severity internal contradiction about late Earth-imports vs aggressive-ISRU cost."

findings:
  - target: "structure"
    target_kind: section
    verdict: pass
    quote: "## Why this question matters ... ## Where it fits ... ## Headline"
    reason: "Required order is present, and the headline appears within 200 words after the motivation section."
    severity: low

  - target: "headline"
    target_kind: section
    verdict: partial
    quote: "spanning **$50–$33,000/kg** — a factor of 660"
    reason: "The range is consistent with q2.c3/q2.c5 after rounding, but the numerical headline and scenario bullets lack inline claim IDs."
    severity: medium

  - target: "c3"
    target_kind: claim
    verdict: contradicted
    quote: "Late-era Earth-imports-only ($1,303/kg with aerobraking) is *cheaper* than late-era aggressive-ISRU ($994/kg)"
    reason: "$1,303/kg is higher than $994/kg. This contradicts the table and q2.c3; it should say Earth-imports-only is more expensive by about $309/kg."
    severity: high

  - target: "c8"
    target_kind: claim
    verdict: supports
    quote: "Late-era aggressive-ISRU ($994/kg) is approximately **9× q1's partial-late ($107/kg)** and **17× q1's optimistic-late ($59/kg)**."
    reason: "Arithmetic is accurate: 994/107 = 9.3x and 994/59 = 16.8x."
    severity: low

  - target: "cost decomposition"
    target_kind: section
    verdict: unsupported
    quote: "c_prop ≈ $6,000/kg, contributing ~$6,000/kg of $13,000 total ... ~15% ... ~5-10%"
    reason: "These component-level numerical claims have no inline claim/source reference and are not explicitly stated in claims.yaml."
    severity: medium

  - target: "delta-v budget"
    target_kind: section
    verdict: partial
    quote: "For methalox (Isp 360 s), 0.556 and 0.794."
    reason: "Hydrolox fractions trace to q2.c2, but the methalox Isp/fractions are not separately claimed or cited inline."
    severity: medium

  - target: "mass-driver results"
    target_kind: claim
    verdict: partial
    quote: "$5-10/kg via mass driver, plus SEP-transfer-to-LEO at $40-50/kg additional in the mature era [q2.c11]"
    reason: "q2.c11 supports Handmer's lunar-orbit output state and $10/kg figure, but the $40-50/kg SEP increment should cite q2.c5 or a source/derivation directly."
    severity: low

  - target: "voice"
    target_kind: topic
    verdict: partial
    quote: "aerobraking is the load-bearing architectural lever"
    reason: "No exact banned transition words appear, but this is close to the flagged 'dominant lever' voice pattern."
    severity: low

notes:
  - issue: "Many table cells are not inline-cited. If the renderer can attach table-level citations, add q2.c3 to the chemical table and q2.c5 to the mass-driver table."
    severity: medium

  - issue: "Headline $50–$33,000/kg includes no-aerobraking cases, while carry-to-synthesis $50–$13,000/kg is aerobraking-only. This is consistent but should be labeled explicitly."
    severity: low

  - issue: "Limitations section has additional uncited numbers: $500/$150/$50 SEP cost and ~$36/kg Metzger cross-check should cite q2.c5/q2.c8 or a source slug inline."
    severity: medium