---
source: b1076-34-reuses-2026
reviewed_pass: 4
reviewed_by: claude+codex
date: 2026-05-25
---

# Source review: B1076 34-reuse milestone (March 2026)

## Summary

| Verdict | Count |
|---|---|
| Consistent | 1 |
| Novel supporting | 1 |
| Merits investigation | 1 |
| Different conclusion | 0 |
| Not relevant | 0 |

## Claims reviewed

### Claim 1 — Falcon 9 first-stage reused 34 times
**Verdict:** Novel supporting

Direct operational evidence that the partial-scenario (30 reuses) reuse count is *achievable* for Falcon 9 first-stage hardware in mature operation. Before this milestone, the 30-reuse target was aspirational. As of March 2026, it's demonstrated.

This is the *single most important* operational anchor for the q1 calc — it converts the partial scenario from "plausible" to "demonstrated for at least one booster."

### Claim 2 — B1076 has launched 22 Starlink batches + 12 dedicated missions
**Verdict:** Consistent

Supports the model that high-reuse hardware is preferentially assigned to lower-risk missions (Starlink, where SpaceX is its own customer) once it gets old. Implies that SpaceX's effective reuse counts may bifurcate: a few "workhorses" approach the demonstrated 34-flight ceiling, while many other boosters fly 5-15 times before retirement.

The fleet-average reuse count is probably closer to 15-20 than 34. **Important constraint for the pessimistic scenario** — it suggests the 10-reuse pessimistic is too pessimistic for the typical Starship booster (assuming Starship achieves Falcon 9-comparable hardware longevity).

### Claim 3 — Implicit: Falcon 9 reuse evidence transfers to Starship
**Verdict:** Merits investigation

As Codex noted in the pass-03 audit, Falcon 9 first-stage reuse is not the same as Starship full-system reuse. Starship has:
- A different upper stage (Ship) that itself must be reusable, vs. Falcon 9's expendable upper
- Larger vehicle, more complex thermal protection (heat shield tiles)
- Different propellant (methalox vs RP-1/LOX)
- Different recovery method (catch tower vs droneship)

The operational analogue isn't perfect. Falcon 9's 34-reuse milestone *bounds the optimism* (Starship probably won't exceed Falcon 9's record in early years) and *bounds the pessimism* (Starship is designed for reuse from day one whereas Falcon 9 was retrofit). It's a useful guide, not a direct prediction.

## Cross-reference

- Validates [pass-02-calc] partial-scenario (30 reuses) as the calibrated central case
- Constrains pessimistic-scenario boundary (10 reuses may be too low even for Falcon 9 fleet mean)
- Falcon-9-to-Starship extrapolation caveat (per Codex audit) carried forward to write pass

## What we'd want next

- SpaceX-reported fleet-average reuse count (not in this source)
- Booster failure rate data — how many SpaceX boosters have been *lost* before reaching 34 reuses? That bounds the reuse expectation actuarially.
