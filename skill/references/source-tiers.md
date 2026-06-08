# Source Tiers

The canonical source hierarchy for the research sub-pass. Every source gathered gets tier-assigned at gather time. Review depth and rendering downstream both key off the tier.

## The hierarchy

| Tier | What | Review depth | Volume target |
|---|---|---|---|
| **S** | Peer-reviewed primary papers on the exact question; foundational papers everyone cites in this field; government technical reports where the agency IS the primary source (NASA SP-87, DoD CMPR, NIST); books from field-central scholars | **Full claim-by-claim review** — verbatim quotes, per-claim verdict, may spawn tree nodes | Read all relevant — 10-50+ as topic demands |
| **A** | Peer-reviewed review articles + meta-analyses; major-conference proceedings (AIAA SciTech, ICRA, NeurIPS); credentialed-group preprints (arxiv from established labs); textbook chapters; survey papers | **Medium review** — key claims extracted, scalar verdict + 2-3 sentence justification per source | 10-30 |
| **B** | **Public figures** — politicians, tech executives, company founders, prominent commentators. The "what do important people say" tier. | **Quote/claim review** — pull individual statements they've made, verdict per statement (supports / contradicts / mixed / not relevant to our analysis), with link to original. Politics-brief-style fact-checking. | 5-20 figures × 1-5 quotes each |
| **C** | Industry trade press (Spaceflight Now, Ars Technica, SemiAnalysis); credentialed-expert blogs/Substacks; expert podcasts; corporate technical white papers (SpaceX press kits, Blue Origin papers) | **Scalar verdict** — agrees / disagrees / mixed / not_relevant / inconclusive + one-paragraph justification | 3-15 |
| **D** | Mainstream press (NYT, Reuters, BBC); social media from non-public-figures; aggregator sites; general commentary | **Scalar verdict** + one paragraph; flag prominently if conflicts with higher tier | 3-15 |
| **E** | Wikipedia; derivative blog summaries; general-audience books used for orientation; lecture notes | **Not reviewed** — orientation only; never cited as evidence in claims | As needed |

## Tier-assignment rules

When gathering a source in the research sub-pass:

1. **Peer-reviewed?** Yes → S or A. Check the venue: original empirical/theoretical paper on this exact question = S; review article or tangential paper = A.
2. **Quoting a person, not a publication?** That person's quote goes to tier B if they are a public figure (politician, tech executive, founder, well-known commentator). The container — a NYT interview, a podcast — is tier D, but the quote itself gets tier B treatment.
3. **Trade press or expert blog?** Tier C.
4. **Mainstream press or social media (non-public-figure)?** Tier D.
5. **Wikipedia or derivative?** Tier E.

Edge cases:
- **Agency blog post by a scientist:** if author is well-known and the post discusses primary research, treat as A. If general-audience PR, treat as D.
- **Substack by someone who's both a public figure AND credentialed expert:** the post body is tier C; specific quotes from it that represent that figure's stated positions can ALSO be promoted to tier B for quote review. A source can appear in two tiers.
- **Preprint from an unknown author:** treat as C, not A. Credentialing matters.
- **Government report not by the primary agency:** if NIST cites a DoD CMPR figure, the NIST report is tier A/B (depending on whether NIST is doing primary work or summarising). The DoD CMPR is the tier S source.

## What this changes about the workflow

**Research sub-pass becomes the heaviest sub-pass.** Target: read all relevant peer-reviewed work in the topic area before declaring the gather complete. For AI-explosive topics, this could be 50-100+ peer-reviewed sources alone.

**Source-review sub-pass splits by tier.** Tier S/A go through the full Newman-style claim-by-claim treatment. Tier B becomes a per-figure quote review. Tier C/D collapse into a fast scalar pass — one paragraph per source, no claim extraction. Tier E gets no review file at all.

**Context overload is the binding constraint.** Even 100 tier-S sources × full extracts will exceed context. The mitigation: `sources/{slug}/extract.md` is structured notes (abstract + 3-7 key claims + reviewer notes), not raw text. See `schemas.md`.

## What this changes about the site

Sources list page:
- Tier badges (S/A/B/C/D/E) shown prominently
- Filter by tier, by topic, by leaf, by type, by date, by verdict
- Sort by tier × date × verdict
- Tier B renders as person cards with per-quote verdict, not source rows
- Tier E hidden from default view (orientation only)

The sorted, filtered, tier-aware source list IS one of the main outputs of the workflow. Done right, it gives the user a structured reading list to dig deeper from — not just "here are some sources we used."
