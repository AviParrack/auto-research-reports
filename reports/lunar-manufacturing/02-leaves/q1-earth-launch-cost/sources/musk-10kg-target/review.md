---
source: musk-10kg-target
reviewed_pass: 4
reviewed_by: claude+codex
date: 2026-05-25
---

# Source review: Musk $10/kg Starship target

## Summary

| Verdict | Count |
|---|---|
| Consistent | 1 |
| Different conclusion | 1 |
| Novel supporting | 0 |
| Merits investigation | 1 |
| Not relevant | 0 |

## Claims reviewed

### Claim 1 — $10/kg target (Musk)
**Quote (paraphrased from multiple Musk statements):** Starship will reduce launch costs to ~$10/kg.
**Verdict:** Different conclusion

The q1 calc cannot reproduce $10/kg from first-principles assumptions. Even the most aggressive scenario (100 reuses, 150t payload, 8% refurb, $0.5M ops) gives ~$59/kg internal cost. To get to $10/kg requires either:
- Sub-2% refurb (vs Shotwell 2017's "<50%" anchor)
- Plus near-zero ops cost
- Plus zero margin on customer-facing pricing

Or — as Codex flagged in pass-03 audit — Musk may be describing internal *cost* not list *price*. Under TAI-grade automation (compressing refurb labor 10×, cadence 10×) the internal-cost figure could approach $10-20/kg. Customer price still requires zero margin to match.

**Our position:** the figure is aspirational and outside the calc envelope without these extra mechanisms. Cite Musk explicitly; do not adopt $10/kg as an unattributed central estimate.

### Claim 2 — "Propellant accounts for roughly one-third" of $10/kg
**Verdict:** Merits investigation

If $10/kg is the total and propellant is 1/3 ≈ $3.33/kg, then for 150t payload: propellant = $500k/launch. My calc uses $1M propellant per launch (Musk's own previously-stated number). The ratio implies Musk has revised either the propellant figure down or the total target up since the earlier statements.

Either way, the propellant arithmetic constrains the rest. If propellant is genuinely $500k/launch and represents 1/3 of cost, total $1.5M/launch, divided by 150t = $10/kg. This matches the target but assumes:
- Hardware fully amortised (effectively $0/launch — requires very high reuse + low refurb)
- Ops cost <$100k/launch (vs my late-era assumption of $500k)

These are aggressive but not impossible under industrial-explosion conditions.

### Claim 3 — Implicit: $10/kg achievable as Starship matures
**Verdict:** Consistent (conditional)

Consistent with the q1 framework *given*: (a) sustained automation pressure on refurb + ops, (b) zero margin during market-capture, (c) reuse counts beyond 100 cycles. The published $1,600/kg early → $100-150/kg long-term projection (cited in the same source) is the more conservative reading without those assumptions.

## Cross-reference

- The reconciled mapping in [pass-03-reconcile.md] places Musk's $10/kg outside the standard envelope and inside a narrow corner requiring TAI-grade compression. This source review confirms that mapping with arithmetic.
- The propellant-arithmetic claim (Musk's 1/3 ratio) is non-obvious and worth promoting to a numerical claim in claims.yaml during the write pass.
- Musk should be cited but not silently treated as ground truth (per Avi's guidance + anti-pattern #13 voice rules).
