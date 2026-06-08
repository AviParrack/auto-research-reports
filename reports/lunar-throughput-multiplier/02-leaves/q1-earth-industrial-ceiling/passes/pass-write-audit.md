overall:
  verdict: weak
  summary: "Core LOX-first and 1-100 Mt/yr conclusions mostly trace to q1.c1-q1.c9, but the write-up adds many unsupported factual details and contains a high-severity order-of-magnitude contradiction in the headline. The lead is buried behind about 256 words of setup."

findings:
  - target: "Headline answer"
    target_kind: section
    verdict: contradicted
    reason: "The sentence saying the 1-100 Mt/yr ceiling is 'three to four orders of magnitude below' Tt/yr contradicts q1.c9, which states the gap is 1-3 orders of magnitude. The same paragraph later gives the correct 1-3 OOM range."
    severity: high

  - target: "Why this question matters / Where this fits"
    target_kind: section
    verdict: unsupported
    reason: "The Moon-as-curiosity/load-bearing framing, q2/q3/q9 role descriptions, and 'q1 result is half of the upper bound' are not traceable to any q1 claim in claims.yaml."
    severity: medium

  - target: "q1.c1"
    target_kind: claim
    verdict: partial
    reason: "The 5% soft ceiling and 100% hard ceiling trace to q1.c1, but 'the level above which the rocket sector visibly disrupts other industrial users' is not stated in the claim."
    severity: low

  - target: "Binding-input ordering"
    target_kind: section
    verdict: partial
    reason: "The ordering traces to q1.c7, but explanatory facts including Raptor's 3.6:1 mixture ratio, 4.0:1 stoichiometric ratio, and cryogenic oxygen being pegged to ASU capacity are not stated as claims."
    severity: medium

  - target: "q1.c2 / q1.c10"
    target_kind: claim
    verdict: partial
    reason: "The engine ceiling and 10,000-ships/year target trace to claims, but McGregor, the planned second Texas facility, and the stated motivation of faster engine replacement in a high-attrition regime do not."
    severity: medium

  - target: "q1.c3"
    target_kind: claim
    verdict: partial
    reason: "The pad ceiling traces to q1.c3, but 'current ~30 active sites globally,' 'historical maximum of ~30-50 simultaneously-active sites,' and the 100x comparison are not in claims.yaml."
    severity: medium

  - target: "Where the ceiling sits at maturity"
    target_kind: section
    verdict: unsupported
    reason: "The comparison to the Manhattan Project, Interstate Highway System, and global aircraft manufacturing is not traceable to any claim. 'Largest industrial mobilisation in human history' is also unsupported."
    severity: high

  - target: "q1.c9"
    target_kind: claim
    verdict: partial
    reason: "The Tt/yr impossibility conclusion traces to q1.c9, but the detailed requirement list, including ~10^4 pads, ~10^7 engines/year, and commercial-aviation engine-production comparison, is not stated in claims.yaml."
    severity: medium

  - target: "What this means for the cosmic-scale question"
    target_kind: section
    verdict: unsupported
    reason: "The claim that the Moon is 'architecturally necessary' and that any Mt/yr lunar leaf carries the parent answer above the Earth-chemical ceiling is a synthesis move, not a q1 claim."
    severity: high

  - target: "Confidence per finding"
    target_kind: section
    verdict: partial
    reason: "The confidence labels trace to claims, but details such as robustness to +/-20%, 'industry-consensus' O2, and 'primary trade-data' are not consistently present as claims."
    severity: low

  - target: "Limitations"
    target_kind: section
    verdict: unsupported
    reason: "Helium supply, cryogenic plumbing, avionics, copper/high-temperature alloys, ground-system overhead of 1.2-1.5x, hydrolox ratios, and EPA retrieval failure are not encoded as claims."
    severity: medium

  - target: "What changes if the answer flips"
    target_kind: section
    verdict: unsupported
    reason: "Launch-loop performance, $3/kg, 4 GW, TRL status, hydrolox/electrolysis effects, and TAI timeline compression are not traceable to claims.yaml."
    severity: medium

notes:
  - issue: "burial-of-lead: the first direct answer appears in 'Headline answer' after about 256 body words, exceeding the 200-word threshold."
    severity: medium
  - issue: "No explicit 'However', 'Furthermore', 'Moreover', or 'It is important to consider' phrasing found."
    severity: low
  - issue: "Mechanical narrative moves: 'Why this question matters' and 'Where this fits' delay the answer; 'What this means for the cosmic-scale question' and 'This is the load-bearing handoff' read as synthesis boilerplate."
    severity: medium
  - issue: "Editorialising phrases: 'cinematic-imagination input,' 'curiosity,' 'load-bearing piece of architecture,' 'not a luxury,' 'by a wide margin,' 'civilizational-scale,' 'categorical-scale infeasibility,' 'architecturally necessary,' and 'enormous.'"
    severity: medium