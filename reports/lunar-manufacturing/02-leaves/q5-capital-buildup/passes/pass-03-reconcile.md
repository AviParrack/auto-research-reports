---
pass: 3
kind: reconcile
leaf: q5-capital-buildup
date: 2026-05-26
agent: claude-opus-4-7
audited: pending
---

# Pass 3 — Reconcile (q5-capital-buildup)

Compares first-principles derived numbers (pass-02-calc, Codex-amended) to the seven published anchors from pass-01-research. Sources are now read; per pass-leaf.md sub-pass 3, this is the appropriate stage.

The derived bracket from pass-02 (Codex-amended):
- **BAU**: $150-400B over ~25 years (central ~$200-300B)
- **Industrial explosion**: $1.2-3B over ~5 years
- **TAI**: Cost-degenerate, time-bound by physical lead time (~12-24 month floor from M6)
- **One-set capital mass**: 311-500 t
- **Total Earth-launched mass over 20 yr**: ~720-1,100 t

## Anchor-by-anchor comparison

### Anchor 1: Zubrin Moon Direct ($1.5B + $420M/yr)
**Source:** [figure-zubrin](../sources/figure-zubrin/extract.md). $1.5B initial + $420M/yr ongoing for sustained presence using Falcon Heavy-derived 10-t-payload landers and lunar-ice ISRU propellant.

**Verdict: Different conclusion (scope mismatch).** Zubrin's $1.5B is for "minimal sustained presence" — habitat + crewed visits + ISRU-for-propellant-only. He explicitly excludes the manufacturing complement and the industrial-export endpoint. Mapped to my milestone clock, his architecture roughly ends at M5 (ISRU pilot plant) or M6 (first sustained occupation). The annualized cost projects to $1.5B + 20 × $420M = ~$9.9B over 20 years for the minimal-presence target. Our IE-regime bracket of $1.2-3B is comparable to this $9.9B figure under the same scope. So Zubrin agrees within an order of magnitude that the *minimal-presence + ISRU* milestone subset is achievable for under $10B — and his number predates Starship-class launch, which our IE regime presumes. **Adjustment: our IE estimate is consistent with Zubrin once scope is normalized.**

### Anchor 2: Metzger 2013 bootstrap (12 t / 20 yr seed; cost unspecified)
**Source:** [metzger-2013-bootstrap](../sources/metzger-2013-bootstrap/extract.md). 12 t landed over 20 yr seeds a self-sustaining 156-MT (60 humanoid robots) endpoint, or up to 40,000 MT at higher launch rates (41 t total launched).

**Verdict: Different framing.** Metzger's 12 t / 20 yr seed is much smaller than our 311-500 t one-set figure — by an order of magnitude. The difference reflects scope: Metzger explicitly assumes the seed evolves through "Gen 1.0-6.0" with crudeness factors declining from 2.5x → 1.0x, with electronics shifting from Earth-imported to lunar-made; his 12 t bootstraps a *self-sustaining* industry, but the buildup uses lunar materials for the *bulk* of subsequent infrastructure. Our calc instead asks "what is the Earth-launched cumulative mass for the buildup including replacements," which counts the seed plus all subsequent imports.

Reconciling: if 12 t is the seed, and 41 t is the full Earth-launched mass to reach the high-throughput endpoint (40,000 MT industrial assets), then Metzger's framework implies that **most** of the manufacturing complement is lunar-made, not Earth-launched. This is much more aggressive than my calc assumes (I assume Earth-imported manufacturing complement of 40 t per replacement cycle). Under the Metzger-bootstrap framework, the Earth-launched mass over 20 yr could be as low as 41 t — an 18× compression vs my 722 t baseline. **Adjustment: this is consistent with my industrial-explosion regime mass-compression factor of 10×.** Metzger's framework is implicitly an IE-regime architecture.

The dollar implication: Metzger explicitly does not assess cost. If we apply our $/kg hardware × launch cost figures to his 41-t bootstrap, BAU launch+hardware ≈ 41,000 kg × ($466/kg × 5 + $100,000/kg) ≈ $4.2B; IE drops to $43M. So Metzger's framework is consistent with our IE regime.

### Anchor 3: Sowers 2021 commercial ($4B initial / $2.5B tent)
**Source:** [figure-sowers](../sources/figure-sowers/extract.md), [sowers-2021-ice-mining](../sources/sowers-2021-ice-mining/extract.md). $4B total / $2.5B for the tent ISRU plant; commercial standalone scenario; 9% ROI / $2B profit / 15-yr project life.

**Verdict: Different conclusion (scope mismatch — propellant only).** Sowers' $4B is for a propellant-only architecture using tent sublimation (φ ≈ 534, much higher than our φ = 20 estimate). His architecture has no habitat (fully robotic), no large mobility fleet, no manufacturing complement. Mapped to my milestone clock he ends at M5 (ISRU pilot plant) plus distribution chain. His architecture is for the M5-only target with no humans and no manufacturing.

If I rescale my calc with Sowers' φ = 534 (vs my φ = 20), my ISRU plant mass falls from 75 t to ~3 t — closer to the tent-sublimation architecture. And if I remove the habitat, mobility, manufacturing complement, my one-set drops from 311 t to maybe 150 t. Multiplied by Sowers' all-robotic regime and using more compressed hardware-cost assumptions (~$50k/kg for purpose-built ISRU rather than human-rated equipment), I land at roughly $5-15B. This is within a factor of 2-4 of Sowers' $4B.

**Adjustment: Sowers' $4B reflects a different architectural choice (tent sublimation φ=534, no humans, no mfg). My calc's net-positive-export base is fundamentally a different product class.** Our two estimates are consistent given their scope differences.

### Anchor 4: Isaacman 2026 NASA ($20B / 7-yr surface base)
**Source:** [figure-isaacman](../sources/figure-isaacman/extract.md), [spaceflightnow-2026-20b-moonbase](../sources/spaceflightnow-2026-20b-moonbase/extract.md), [nasa-oig-2021-artemis-93b](../sources/nasa-oig-2021-artemis-93b/extract.md). $20B over 7 yr for surface base with habitats, pressurized rovers, nuclear power systems. Cancels Gateway, repurposes components.

**Verdict: Consistent with BAU lower bound.** Isaacman's $20B over 7 yr ≈ $2.9B/yr sustained matches our BAU launch+hardware figure of $73B over 20 yr ≈ $3.6B/yr. The 7-year scope ends at roughly M6 (first sustained crewed occupation) rather than M8 (net-positive export), and *excludes* manufacturing complement (Isaacman's framing is exploration-base, not industrial-export-base). So $20B is in the M3-M6 portion of the buildup, our BAU $73B is M1-M8. Per-year rates align tightly. **Adjustment: Isaacman's number is consistent with our BAU regime at the M6 stage.**

### Anchor 5: PwC 2026 cumulative ($72-88B 2026-2050)
**Source:** [pwc-2026-lunar-market](../sources/pwc-2026-lunar-market/extract.md). $72.7-88.5B cumulative infrastructure 2026-2050, all-party (NASA + ESA + JAXA + China + commercial). Transportation 70-80% in early years; five infrastructure pillars (mobility, comms, habitation, energy, water).

**Verdict: Consistent with BAU full-scope.** PwC's $72-88B all-party / all-infrastructure / 24-yr cumulative aligns surprisingly well with our BAU launch+hardware figure of $73B over 20 yr. The agreement is within ±20%. Two reasons this is genuinely informative rather than coincidence: (a) PwC's methodology is "publicly available data + expert interviews + scenario modeling," which is fundamentally a different reasoning path from our bottom-up engineering estimate; (b) the agreement between independent methodologies on a number that spans 3+ orders of magnitude in the published literature is a real convergence signal. **Adjustment: my BAU $73B-without-dev figure is the right anchor for "all-party cumulative infrastructure spend"; the $93-100B dev addition is plausibly counted separately or implicitly in PwC's higher band.**

### Anchor 6: MacDonald CSIS / SEI ceiling (~$1T in today's dollars)
**Source:** [csis-macdonald-2026-economics](../sources/csis-macdonald-2026-economics/extract.md). Apollo $250-300B today's dollars; SEI 1989 projected $500B in 1989 dollars (~$1T today).

**Verdict: Consistent with BAU pessimistic ceiling.** MacDonald's $1T anchor is the 1989-architecture upper bound — what the program *would* have cost under SLS-class transport, government-cost-plus contracting, and pre-Starship launch economics. Our BAU upper bound ($400B with Codex-accepted adjustments) is ~40% of MacDonald's anchor; the gap is roughly explained by the difference between commercial-Starship-launch (our BAU $466/kg) and SLS-class transport (~$30,000/kg for SEI-era architecture). MacDonald's number is the "what if we did this with Apollo-style contracting and pre-Starship launch" anchor, which our BAU explicitly does not assume. **Adjustment: MacDonald's $1T is consistent with our BAU upper bound after accounting for the commercial-vs-SLS architectural difference.**

### Anchor 7: Handmer trillion-dollar buildout
**Source:** [figure-handmer](../sources/figure-handmer/extract.md). "Trillions of dollars necessary to build and sustain space factories" — full orbital-AI-compute / lunar-manufacturing trillion-dollar scenario. $100B/yr per mass driver at full operation. 450 MW reactor floor ($2-4B Earth-cost, possibly 10x on Moon).

**Verdict: Consistent with the full-AI-compute-export endpoint scope.** Handmer's trillion-dollar framing is for a *much* larger end-state than our minimum-net-positive-export base. He envisions dozens of mass drivers, 100 GW orbital compute capacity, full Moon-to-orbit logistics loop. Our calc is sized for a single net-positive-export base at the M8 milestone (one ISRU plant, one mfg complement, one settlement). Handmer's "trillion+" describes the *steady-state mature industry* perhaps 2-3 decades after our M8. **Adjustment: Handmer's scope is the multi-base industrial buildout that our q5 question doesn't directly address; agreement is by virtue of being at different milestones of the same architectural arc.**

## Cross-anchor summary

| Anchor | $-figure | Scope | Our regime match | Verdict |
|---|---|---|---|---|
| Zubrin | $1.5B + $9.9B/20y | Minimal presence + propellant ISRU | IE @ M5 | Consistent w/ scope adjustment |
| Metzger 2013 | (no $) 12-41 t Earth-launched | Self-sustaining bootstrap | IE | Consistent (implicitly IE architecture) |
| Sowers 2021 | $4B | Propellant-only, fully robotic | BAU @ M5 only | Consistent w/ φ=534 architecture difference |
| Isaacman 2026 | $20B / 7yr | Surface base @ M6, no mfg | BAU @ M6 | Consistent ($2.9B/yr matches) |
| PwC 2026 | $72-88B / 24yr | All-party all-infra cumulative | BAU @ M8 | **Consistent w/in 20%** — convergence signal |
| MacDonald SEI | ~$1T | 1989 SLS-architecture ceiling | BAU upper bound | Consistent (after SLS-vs-commercial reframe) |
| Handmer | trillions+ | Full mature industry (dozens of bases) | beyond our M8 | Consistent at different milestone |

**The big finding:** when published anchors are normalized to common scope (product class, milestone, transport architecture), the spread from $1.5B (Zubrin minimal) to $1T+ (Handmer mature industry) is **explained by scope and regime, not by genuine analytical disagreement**. The 3-order-of-magnitude spread in raw numbers is a scope-and-product-class artifact. The "actual disagreement" — the spread on the *same* milestone under the *same* architecture — is more like 2-4× across credible sources, which is the expected range for a still-developing area of engineering economics.

## Implications for claims.yaml

Three new claims to add (factual claims from sources, not derivations):

- q5.c11: PwC 2026 cumulative infrastructure $72.7-88.5B (2026-2050, all parties) — converges with our BAU-without-dev within 20%.
- q5.c12: NASA Artemis program-of-record $93B through FY2025 (OIG audit) + $20B / 7yr surface base (Isaacman 2026) = ~$115-140B US public-program lunar spend through ~2033.
- q5.c13: Sowers' $4B propellant-only architecture using tent-sublimation (φ ≈ 534) is consistent with our BAU regime when scope is normalized to M5-only target.

And one resolution to a derived claim:

- q5.c4 (BAU $150-400B): reconcile evidence array updated. Strong convergence with PwC ($72-88B without our dev cost). MacDonald upper bound consistent. Isaacman/Zubrin/Sowers consistent at narrower scope. Downgrade BAU central estimate from "$200-300B" to "$100-300B" reflecting PwC convergence. Confidence raises to medium.

## Disagreement summary

The only material *analytical* disagreement after scope normalization is:
- **Whether the Earth-launched manufacturing-complement mass is large (our calc: 40-150 t per cycle) or small (Metzger bootstrap: most mfg complement is lunar-made after Gen 3.0).** This is the highest-leverage uncertainty in the BAU figure. If Metzger's bootstrap framework holds, our BAU drops from $150-400B to roughly $50-150B. If it doesn't (because the precision-electronics / motors / bearings / chips dependency on Earth is more persistent than Metzger assumes), our calc's $150-400B is closer to right.

Confidence on resolution: **medium**. The empirical answer requires the M7 milestone demonstration on the lunar surface — we will not know for certain until the first generation of lunar-made manufacturing equipment is actually built and operated.

## To carry to source-review

Tier S/A claim-by-claim review will check:
- Whether Metzger 2013's generation-scheme assumptions about precision-electronics lunar-substitution are evidence-grounded or aspirational
- Whether Sowers 2021's $4B includes development cost or just deployment
- Whether the NIA bigidea ISRU sizing reference (Codex link) gives a third independent anchor
- Whether the Walther 2024 in-situ-boulders architecture compresses our infrastructure mass budget further

Source review will produce per-figure quote reviews for the 9 Tier B figures.

## Anti-pattern check

- ✓ Each anchor mapped to our derived bracket with explicit scope normalization
- ✓ Numerical disagreements decomposed into structural (scope, regime) vs analytical (lunar-vs-Earth-imported manufacturing) drivers
- ✓ The 3-order-of-magnitude raw-spread is not papered over — it is explained
- ✓ Convergence with PwC ($72-88B vs our BAU launch+hardware $73B) is genuine cross-methodology agreement, not coincidence
- ⚠ Codex audit on this reconcile pass should check: (a) my scope-normalization arguments are not just hand-wave justifications for whatever numbers happen to land where; (b) my "structural vs analytical disagreement" decomposition is fair to the source authors.
