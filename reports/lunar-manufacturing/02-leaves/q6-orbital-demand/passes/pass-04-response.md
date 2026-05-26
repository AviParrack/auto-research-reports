---
pass: 4
kind: response
leaf: q6-orbital-demand
date: 2026-05-26
status: done
audit_responded: passes/pass-04-audit.md
---

# Pass 4 — Response to Codex audit

Codex returned `verdict: flagged` with six findings (two medium, two
low for counts/summaries, plus two clarifications). Most are accepted
and fixed in-place.

## Accepted (review files updated in-place)

- **Scientific American review cross-attribution (medium)**: Codex correctly noted the 100 GW US AI demand by 2030 framing is Marcy's, not Scientific American's. The extract for scientificamerican-2026-sdc states "nearly half of U.S. electricity demand growth through 2030" + Starcloud's 5 GW 2035 + Suncatcher's $200/kg — these are the correct attributions. Review file updated to remove the cross-attribution.

- **Marcy review unit error (medium)**: Codex correctly caught the 1000× unit error: 5 GW × 40 t/MW = 200,000 t in 16 km² = 12.5 kg/m², not 12.5 t/m². The 20-30 t/m² figure I invented was not from the extract and was an order-of-magnitude error. Fixed.

- **Tier S "full claim-by-claim review" overclaim (medium)**: Codex correctly noted that five of seven tier S sources had primary PDFs that were not parseable via WebFetch. The reviews are claim-by-claim against the LOCAL extract.md content (which is itself derived from secondary aggregators, abstracts, agency-site descriptions). Updated the pass-04 aggregator to clarify this framing. Future iteration should hand-extract primary PDFs.

- **Tier C count inconsistency (low)**: Tier C has 11 sources, not 9 (I miscounted Handmer × 2). Corrected.

- **Tier B aggregate inconsistency (low)**: Bezos is "Mixed" per his own review file; the aggregate summary incorrectly counted him with the optimists. Corrected to "three figures + Bezos mixed."

- **Tier S Crawford not-relevant verdict omitted (low)**: One of Crawford's claim verdicts is "Not relevant" (Earth-Moon system coupling); the aggregate summary omitted this. Added.

- **Anti-hallucination claim scope (medium note)**: Codex correctly noted that "quotes appear in extract.md" is a check against my hallucinating, not a check against the original primary documents being faithfully extracted. Clarified the framing in the aggregate.

## Disputed / clarified

- **Musk weakest provenance (low note)**: Codex notes Musk's quotes come partly via Wikipedia rather than direct transcript. Acknowledging — the 1M-ton and 1000-ship-per-window figures are widely re-quoted and consistent across multiple sources; the May 2025 presentation cadence ramp is from primary Musk audio/video. Future iteration could anchor each Musk quote to a specific dated transcript. Holding for now because the figures are not in dispute as Musk's stated positions.

## Notes engaged

- **Per-figure scoping (low note)**: Codex confirmed the tier B per-figure reviews are appropriately scoped vs broader article reviews. No change required.

- **Verdict calibration (low note)**: Codex confirmed C/D verdicts don't contradict S without flag. No change required.

## Updated stance

Codex's audit was correct on the two medium-severity findings (cross-
attribution, unit error) and on the count + summary inconsistencies.
All fixed in-place in the individual review files and the aggregate.

The aggregate-level conclusions are unchanged: 22 consistent + 2 novel
+ 5 merits + 1 different + 1 not-relevant at tier S; tier B brackets
the optimist-skeptic range via Handmer 2× vs McCalip 3.2×; tier C/D
broadly support tier S findings.

No findings rejected.

## Next pass

Pass 5 (consistency): cross-leaf claim comparison against q1, q3, q4
(all reviewed). Particular attention to q1 cost-demand coupling and
q3 ISRU feasibility supplying the lunar-sourced bulk-mass half of
q6.c6's argument.
