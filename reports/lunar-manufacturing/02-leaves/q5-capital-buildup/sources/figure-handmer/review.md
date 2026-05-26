---
public_figure: "Casey Handmer"
tier: B
reviewed_pass: 4
reviewed_by: claude+codex
roles: ["CEO Terraform Industries", "Former JPL software architect", "Prominent space-economics commentator"]
relevance: "Closest contemporary analog to Sowers architectural framing; trillion-dollar mature-industry pole"
---

# Public figure: Casey Handmer

## Quotes reviewed

### Quote 1
**Statement:** "Trillions of dollars necessary to build and sustain space factories"
**Source:** Casey Handmer blog Feb-May 2026 → sources/figure-handmer/extract.md (trillions-of-dollars)
**Verdict:** Different scope — mature-industry endpoint, not initial buildup
**Why:** Handmer's "trillions" is end-state mature-industry total, not initial net-positive-export-base capex. Our q5 calc converges $150-400B for the initial BAU buildup of a single net-positive-export base. "Trillions" for mature multi-driver industry is a different scope (analogous to multi-decade fab industry total spend, not first-fab buildup). Useful as the maximally-optimistic-commercial-end-state anchor; not directly comparable to our M8 endpoint.
**Severity:** medium (frequently cited as "lunar capex" without scope-disclaimer)

### Quote 2
**Statement:** "Space-based inference might cost twice as much but still leaves 98% margin for profit due to AI inference pricing being 100x the cost for ground-based datacenters"
**Source:** Handmer blog → sources/figure-handmer/extract.md (ai-margin-100x)
**Verdict:** Out of scope for q5 (demand-side, q6 question)
**Why:** Margin economics is the demand-side justification for q5-scale buildup. Cross-references q6 (lunar-demand). For q5 we take it as exogenous that there exists demand justifying the buildup; Handmer's margin claim is the load-bearing assumption that justifies trillion-dollar investment.
**Severity:** low

### Quote 3
**Statement:** "Raw basalt rocks at $10/kg in lunar orbit; $100B/yr revenue per driver"
**Source:** Handmer blog (How to build a lunar mass driver, 8 May 2026) → sources/figure-handmer/extract.md (basalt-10-per-kg-100b-yr)
**Verdict:** Cross-references q7 (mass-driver economics) — not load-bearing for q5
**Why:** This is q7's territory. For q5: provides a per-driver revenue anchor that combined with q7's $1.24T BAU capex figure gives a payback period (~12 yr) consistent with capital-intensive industrial buildout. Q5 cross-leaf flag: q7's $1.24T BAU mass-driver capex is roughly 3-8× our q5 base capex range, which means the mass-driver is the dominant capital line item, not the base itself. Q5's base capex is necessary-but-not-sufficient for the Handmer architecture.
**Severity:** medium (q7 cross-leaf alignment)

### Quote 4
**Statement:** "Any serious infrastructure will require serious power, either from extremely large nuclear reactors" (~450 MW class, $2-4B Earth-cost, possibly 10x on Moon)
**Source:** Handmer blog → sources/figure-handmer/extract.md (450mw-nuclear-floor)
**Verdict:** Different conclusion — Handmer's power floor is ~1000× our calc baseline
**Why:** Our calc-baseline power is 500 kWe (q5.c8). Handmer's 450 MW class is ~900× larger. Difference is scope: 500 kWe is the calc-baseline net-positive-export base; 450 MW is the mature-industry / multi-driver buildout. The 10× lunar-vs-Earth cost markup Handmer cites is consistent with our $100k/kg aerospace-flight-hardware multiplier when applied to Earth's $2-4B reactor cost: $2-4B × 10 = $20-40B for one 450 MW unit, vs our 500 kWe class at $12.5B (125 t × $100k/kg, q5.c1+q5.c3). Per-MW the calc-baseline is more expensive than Handmer's projection (consistent with lower-MW class being inherently less mass-efficient).
**Severity:** medium

### Quote 5
**Statement:** "GPUs imported from Earth for many years to come"
**Source:** Handmer blog → sources/figure-handmer/extract.md (gpus-from-earth)
**Verdict:** Consistent with Metzger Gen 1-2 framing
**Why:** Handmer's "GPUs from Earth for many years" aligns with Metzger 2013's Gen 1-2 (electronics not lunar-made until Gen 3+). Useful corroboration of the bootstrap framework's electronics-substitution lag.
**Severity:** low

### Quote 6
**Statement:** "The hard problem is not a mass driver cannon, but rather an industrial transport loop"
**Source:** Handmer blog → sources/figure-handmer/extract.md (mass-driver-not-cannon)
**Verdict:** Consistent with our q5/q7 architectural framing
**Why:** Handmer's reframing — the bottleneck is the steady-state industrial supply chain, not the launch mechanism — directly supports q5's framing that mass-driver-only capex (q7) is incomplete without base-manufacturing capex (q5). Architectural alignment is high.
**Severity:** low

### Quote 7
**Statement:** "[Mass driver] feasibility depends on Earth launch becoming supply-limited in some way"
**Source:** Handmer blog → sources/figure-handmer/extract.md (driver-feasibility-conditional)
**Verdict:** Consistent with q7 feasibility-conditional framing
**Why:** Acknowledges that mass-driver-architecture-viability is conditional. Important honest framing of which regime supports which architecture: Sowers-class architecture works in BAU; Handmer-class mass-driver-industry requires Earth-launch supply constraint as a precondition.
**Severity:** low

## Cross-reference

- Handmer is the most-aligned contemporary public figure to our IE/mass-driver framing. His "trillions of dollars" upper anchor is the mature-industry endpoint; our q5 initial-buildup capex is the early portion of his timeline.
- Strong q7 cross-leaf (mass-driver economics): Handmer is the canonical contemporary mass-driver voice.
- Strong q6 cross-leaf (demand): his AI-margin-100× claim is the demand-side justification.
- His 450 MW power-floor figure is ~900× our base-case 500 kWe — both are consistent at their respective scopes.
- Codex anti-hallucination check: all quotes trace verbatim to figure-handmer/extract.md anchors. The two Handmer blog posts (Feb 2026, May 2026) are independent primary sources.
