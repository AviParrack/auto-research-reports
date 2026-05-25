---
source: metzger-2023
reviewed_pass: 4
reviewed_by: claude+codex
date: 2026-05-25
---

# Source Review: Metzger 2023 — *Economics of In-Space Industry and Competitiveness of Lunar-Derived Rocket Propellant*

Point-by-point review of claims relevant to the q4-gear-ratio leaf, with verdict taxonomy:
- **Consistent** — agrees with our analysis
- **Different conclusion** — we considered, disagree (with reason)
- **Novel supporting** — new info we hadn't used, integrated
- **Merits investigation** — flag for follow-up
- **Not relevant** — out of scope

## Summary

| Verdict | Count |
|---|---|
| Consistent | 6 |
| Different conclusion | 1 |
| Novel supporting | 3 |
| Merits investigation | 2 |
| Not relevant | 1 |

## Claims reviewed

### Claim 1 — competitiveness framework

**Quote:** *"The 'gear ratio on cost' for capital transport, G, and the production mass ratio of the capital, φ, are identified as the most important factors determining competitiveness."*

**Verdict:** Consistent

Our first-principles calc independently derives the same competitiveness inequality (Eq. 8 in Metzger). G and φ emerge naturally as the load-bearing variables once costs are launch-normalized. Confirmed by Codex audit of pass-02-calc.

### Claim 2 — tent sublimation φ values

**Quote:** *"Tent sublimation technology has a value of φ that is an order of magnitude better than the threshold for competitiveness even in low Earth orbit (LEO)."*

**Verdict:** Consistent (with caveat)

Tent sublimation φ values (Kornuta 442, Sowers 534) are roughly 10× a "~50" threshold. The order-of-magnitude framing is supported. Caveat: the "threshold" itself is destination-dependent and not a single number. Our q4.c7 reflects this.

### Claim 3 — physics advantage of 24×

**Quote:** *"the best payload mass fraction for conventional rocket technology launching off the Earth to GTO is about 2%. For launching off the Moon … the payload mass fraction can be about 48%, or 24 times higher."*

**Verdict:** Consistent

Direct from Tsiolkovsky with realistic IMF. Our derivation gives similar order-of-magnitude (G_LEO-LS ≈ 15 for round-trip reusable). The 24× figure is the upper-bound physics advantage assuming idealised propellant delivery; real architectures eat into it via Γ_X penalties.

### Claim 4 — competitive vs absolute advantage

**Quote:** *"lunar-derived propellant needs only a comparative advantage, not an absolute advantage"*

**Verdict:** Novel supporting

This reframing is not in our calc — we treated absolute advantage (ψ_X < 1) as the success condition. Metzger's point: lunar propellant competes against the *opportunity cost* of using Earth launch capacity for other payloads. With Starship-scale launch glut, lunar wins comparatively even if not absolutely. Adds nuance our analysis didn't capture.

### Claim 5 — Pelech φ = 3.7 for strip mining

**Quote:** *"For the strip mining technology P roughly estimated φ ~ 3.7. CD, J, and B predicted φ an order of magnitude larger for similar technology."*

**Verdict:** Merits investigation

Pelech's number is 5-10× below other strip-mining estimates. Metzger attributes this to overestimating M_K based on terrestrial excavator analogies. We don't have the Pelech primary source extracted; the disagreement matters because it determines whether strip mining is viable at all. Flagged for separate Source Review of Pelech.

### Claim 6 — Metzger MVP φ = 36.5

**Quote:** *"M estimated the resulting M_K to be an order of magnitude lower than other studies … yet φ = 36.5 is still high enough to gain absolute advantage at least to GTO."*

**Verdict:** Consistent

Our q4.c6 reflects this exactly. The "≥35 threshold" is the MVP value, not a universal cutoff.

### Claim 7 — insensitivity to launch cost at high G/x

**Quote:** *"Lunar propellant can be insulated from decreasing launch costs by achieving x < G as a capital design goal."*

**Verdict:** Novel supporting

Counter-intuitive and important. Our calc shows the sensitivity matrix (Table 3 in Metzger) but didn't extract the design implication clearly. Adds: lunar mining firms should *engineer* their capital so launch cost reduction doesn't undercut them. This refutes the "Starship makes lunar mining unviable" framing.

### Claim 8 — discount rate dominates timing

**Quote:** *"S [Sowers] estimates an Internal Rate of Return (IRR) of 8.84% in a fully commercial venture, which is much less than the 21.7% that CD thought necessary to attract investors."*

**Verdict:** Consistent

Discount rate is the bigger lever than tech for breakeven timing. Our q4.c5 captures this. Metzger's Table 1 shows 5-23 year ranges, with the variance driven mostly by financing not technology.

### Claim 9 — market size weak effect

**Quote:** *"each order of magnitude reduction in the market delays absolute advantage in LEO by about 2 years."*

**Verdict:** Novel supporting

I didn't reason about market size in calc. Metzger's finding that 100× smaller market only delays LEO by 4 years is notable — it means policy support / customer aggregation isn't the bottleneck. The tech + finance variables dominate. Worth flagging in synthesis.

### Claim 10 — LEO viability requires SEP architecture

**Quote:** Implied across Fig 6 + Section 4.10: lunar absolute advantage at LEO uses SEP from LLO toward Earth (I_sp = 2000 s) rather than pure chemical.

**Verdict:** Consistent

Our q4.c9 captures this. Pure chemical reusable RT has Γ_LEO ≈ 14 making LEO structurally hard.

### Claim 11 — reliability optimisation

**Quote:** *"the main finding is that it is unnecessary to make costly improvements to the hardware to gain higher reliabilities typical of NASA exploration missions"*

**Verdict:** Not relevant (to gear ratio leaf)

This belongs to a different leaf (perhaps q3-isru-feasibility or q5-capital-buildup). Reliability cost optimisation is an interesting modelling choice but not load-bearing on the gear-ratio question per se.

### Claim 12 — pessimistic TEAs (CD, J) used SLS for capital transport

**Quote:** *"CD assumed high G = 64.9 (per current pricing) due to the use of government-built (non-commercial) rockets for capital transport. Even with EOS/SOE and learning curve, since G is high the reduction in x has diminishing returns"*

**Verdict:** Consistent

Architectural choice (SLS vs commercial) drives a 10× swing in G. The published pessimistic conclusions of CD and Jones were a function of conservative transport assumptions that don't reflect 2026 commercial reality. Our framework predicts the same: G dominates when high.

### Claim 13 — economies of scale + Wright's Law assumptions

**Quote:** *"a = 0.66 used as empirical scaling exponent ... b = 0.75 (more conservative learning than typical b=0.80 for new industry)"*

**Verdict:** Merits investigation

Metzger's choices are defensible (Haldi-Whitcombe industry data; Wright's Law literature) but inherently assume *business-as-usual industrial scaling*. They don't account for industrial-explosion-grade automation. Under TAI-grade conditions, both a and b could collapse dramatically (effectively a near 0, b approaching 0.5). This is a research-frontier consideration that Metzger does not address.

## Cross-references to internal pages

- q4.c1, q4.c2 confirmed by Metzger's Γ analysis
- q4.c3 derivation matches Metzger's Eq. 8 necessary condition
- q4.c6, q4.c7, q4.c8 directly from Table 2 + Section 6
- q4.c9 from Fig 6 + Section 4.10
- q4.c10 (TAI sensitivity) is *not* covered by Metzger — original to our analysis

## What Metzger 2023 does *not* address (gaps for synthesis)

1. **Industrial-explosion / TAI-grade automation sensitivity.** Wright's Law and EOS assumed at conservative industry norms. No treatment of what happens under sustained automated capital design improvement.
2. **Sub-2023 cost-curve realism.** Starship trajectory used per Musk's 2022 statements; doesn't update for actual 2024-2026 launch cadence.
3. **Strategic/national-security demand.** Treated as a footnote (Listner 2023); not modelled.
4. **Aerobraking as alternative to SEP for LEO.** Only briefly mentioned; full architecture analysis would be valuable.

## Overall verdict

Metzger 2023 is the load-bearing source for the gear-ratio leaf. Our first-principles framework converges on the same competitiveness structure independently. The main differences are scope (he models lifecycle dynamics; our calc is snapshot) and modelling sophistication (his finance treatment is more nuanced). Where his published results are firm (Tables 1 + 2, Fig. 5-9), our framework gives consistent answers when parameterized appropriately.

The leaf write pass can confidently use Metzger's TEA reassessment as the substantive answer to "what φ is needed and is it attainable" — with the TAI caveat from q4.c10 layered on.
