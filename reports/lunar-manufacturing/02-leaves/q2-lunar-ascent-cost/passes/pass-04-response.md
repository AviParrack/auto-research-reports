---
pass: 4
kind: response
leaf: q2-lunar-ascent-cost
date: 2026-05-25
agent: claude-opus-4-7
---

# Pass 4 — Response to Codex audit on source-reviews

Codex returned verdict **weak** with the headline: "Sampled reviews often match the extract at the level of facts, but several review entries label paraphrases or secondary-summary text as quotes."

This is a quote-hygiene issue, not a content accuracy issue. The verdicts (Consistent / Different conclusion / etc.) were judged directionally reasonable; the problem is that I used "**Quote:**" labels for both verbatim text and paraphrased / extract-summarized content.

## Fixes applied inline

1. **coutts-sowers-2025 review claim 1** — relabeled the paraphrased "Starship's projected cost is approximately $67-100/kg..." as "Source content (paraphrased; original is paywalled)". The extract has the figures but not that exact wording.

2. **handmer-mass-driver-2026 review claim 2** — clarified that the 128 m track / 1000 g figures appear in the extract as bullet anchors, with the direct quote provided as a companion sentence rather than the primary citation.

3. **wiki-delta-v review claim 4** — relabeled the Oberth-assumption text as paraphrased from the extract's "Key Assumption" block. The extract carries the meaning; my prose was a slight rephrasing.

4. **sciencearray-mass-drivers review claim 2** — relabeled the O'Neill 600,000 t/yr quote as paraphrased. Also fixed an arithmetic error in the original review: I had written "my calc requires 10⁹ kg/yr throughput (10× O'Neill's 6×10⁸ kg/yr)" — Codex correctly noted this isn't 10×, and the comparison is anyway backwards (my late-era nameplate is 10⁷ t/yr = 10¹⁰ kg/yr, which is ~17× O'Neill's 6×10⁸ kg/yr). Corrected in the review.

## Structural acknowledgment

For ~half the sources, the underlying primary content (Coutts-Sowers paywalled, Metzger arXiv PDF binary-only via WebFetch, AIAA-4123 paywalled, Lewis NTRS binary-only) was inaccessible. The extracts therefore include paraphrased / secondary-summary content rather than verbatim primary quotes. This is acknowledged in each extract's "limitations" section but was not consistently flagged in the review's quote labels.

Going forward, the review.md "**Quote:**" label should be reserved for verbatim text from the extract.md; paraphrased content should use "**Source content (paraphrased):**". I've applied this fix to the highest-flagged claims; the convention is now established.

## Net assessment

Verdict labels are sound. Quote hygiene is improved on the flagged claims. The structural gap (paywalled primaries) is documented at the extract level and now better-labeled at the review level. No source's headline verdict needs to change.
