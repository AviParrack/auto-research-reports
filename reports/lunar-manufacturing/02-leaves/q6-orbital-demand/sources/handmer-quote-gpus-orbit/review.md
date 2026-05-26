---
public_figure: "Casey Handmer"
tier: B
reviewed_pass: 4
reviewed_by: claude+gpt
roles: ["Terraform CEO", "former JPL engineer"]
relevance: "Influential mid-optimist on orbital compute economics; 2x cost-premium baseline position"
---

# Public figure: Casey Handmer (q6 quote review)

## Quotes reviewed

### Quote 1: 2× per-token cost premium

**Statement:** "SpaceX, with their incumbent advantages in launch and
Starlink hardware expertise, may be able to ship gigawatts of inference
compute into Earth orbit for something like 2× the per-token cost of
ground-based AI, but that this would still be quite profitable."

**Source:** Direct Current Data Centers (Terraform blog, 2026-01-30).

**Verdict:** Supports under TAI-C; contradicts McCalip's 3.2× analysis

**Why:** Handmer's 2× cost-premium estimate operates on per-token
inference economics under SpaceX-integrated architecture (Starship +
Starlink + GPUs). McCalip's 3.2× operates on whole-project capex+opex
for a 1 GW deployment under generic launch + commodity hardware. The
distinction matters: under SpaceX integration, the launch + comms cost
is amortized across existing constellation infrastructure, while
McCalip's calculator treats orbital DC as a green-field deployment.
Both can be correct under their own framings. q6.c2 regime range
bracketed by both.

**Severity:** high (key bracket position vs McCalip)

### Quote 2: "Glorified Starlink satellites with GPUs"

**Statement:** Orbital data centers are "essentially glorified Starlink
satellites with a bunch of GPUs attached."

**Source:** Direct Current Data Centers, 2026-01-30.

**Verdict:** Supports framing (architectural shortcut)

**Why:** Handmer's framing emphasizes that orbital DC is not a
clean-sheet engineering problem but an extension of existing
satellite-constellation operations. This is the architectural
justification for the q6.c5 "Starlink-derived" cost amortization
that makes Handmer's 2× figure defensible. Cross-references
introl-2026's documentation of Starcloud + Kepler + Axiom + Aetherflux
all using Starlink-class platforms.

**Severity:** medium

### Quote 3: SSO band 10^17 W available

**Statement:** Unshaded sun-synchronous orbital band 800-2500 km
altitude provides "10^17 W available."

**Source:** Direct Current Data Centers.

**Verdict:** Supports framing (100 PW solar flux)

**Why:** 10^17 W is the integrated incident solar power across the
unshaded SSO band — a theoretical upper bound for SSO-deployed solar
collection. Even capturing 1 part in 10^6 of this would supply 100 TW,
far exceeding any plausible orbital DC demand. This bounds the
energy-supply side of the orbital DC equation: solar is not the
binding constraint. Q6.c6's argument that mass-supply (not energy
supply) is the binding constraint is consistent.

**Severity:** medium

### Quote 4: O'Neill justification

**Statement:** Orbital compute is "finally, an application of space-
based solar power that can justify something like the vision of Gerry
O'Neill."

**Source:** Direct Current Data Centers.

**Verdict:** Supports framing (qualitative)

**Why:** Handmer's invocation of O'Neill links orbital compute to the
historical SBSP / space-settlement infrastructure case. This is
rhetorically significant for q8 synthesis (the lunar-manufacturing
thesis aligns with O'Neill's broader vision) but not directly
quantitative for q6.

**Severity:** low

## Aggregate verdict

Handmer's positions span (a) operational architecture (Starlink-derived
orbital DC), (b) cost-economics (2× premium acceptable), (c) energy-
supply unconstrained, and (d) rhetorical alignment with the O'Neill
infrastructure vision. The 2× premium is the canonical mid-optimist
position that brackets McCalip's 3.2× at the lower end. q6.c2 regime
range captures both positions as defensible under different demand
assumptions.

Cross-reference: handmer-2025-propellant-stability provides Handmer's
quantitative depot/propellant analysis; these quote reviews cover the
orbital-DC viability framing only.
