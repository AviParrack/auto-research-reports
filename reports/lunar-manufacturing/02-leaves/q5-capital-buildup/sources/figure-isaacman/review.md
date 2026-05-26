---
public_figure: "Jared Isaacman"
tier: B
reviewed_pass: 4
reviewed_by: claude+codex
roles: ["NASA Administrator (2026-)", "Founder Shift4 Payments", "Polaris Dawn commander"]
relevance: "Sitting NASA Administrator; $20B / 7-year moon base announcement is the de-facto current US program-of-record"
---

# Public figure: Jared Isaacman

## Quotes reviewed

### Quote 1
**Statement:** "$20 billion over the next seven years to build a moon base near the lunar south pole"
**Source:** NASA HQ announcement Mar 24-25 2026 → sources/figure-isaacman/extract.md (20b-7-years)
**Verdict:** Consistent with our BAU bracket at scope-corrected interpretation
**Why:** $20B/7yr ≈ $2.9B/yr surface-base capex. This is the surface-base layer specifically — it sits on top of the existing $93B Artemis transport program-of-record (nasa-oig-2021-artemis-93b). Combined US public-program capex through ~2033: $93B + $20B + operations ≈ $115-140B (claim q5.c12). This is below our BAU $150-400B bracket because Isaacman's announcement explicitly excludes the manufacturing complement and net-positive-export endpoint — i.e., his scope is at the M6/M7 boundary, not M8. The two figures are scope-consistent.
**Severity:** medium (highest-policy-weight number on the topic; load-bearing for the BAU-anchor case)

### Quote 2
**Statement:** "I envision launching two moon landing missions per year to establish semi-permanent astronaut occupation"
**Source:** NASA HQ Mar 2026 → sources/figure-isaacman/extract.md (two-landings-per-year)
**Verdict:** Consistent with BAU cadence; below IE cadence
**Why:** Two crewed landings/year matches our BAU cadence assumption. IE regime would imply higher cadence. The "semi-permanent" framing aligns with our M6 (first crewed sustained occupation) milestone definition; the 12-month irreducible occupation floor applies.
**Severity:** low

### Quote 3
**Statement:** "This time, the goal is not flags and footprints. This time, the goal is to stay"
**Source:** NASA HQ Mar 2026 → sources/figure-isaacman/extract.md (not-flags-and-footprints)
**Verdict:** Aligned with q5 premise (net-positive-export-base scope is "to stay")
**Why:** Direct policy endorsement of sustained-presence framing. Aligns with Bezos's "this time to stay" 2019 language. No quantitative content.
**Severity:** low

### Quote 4
**Statement:** "We intend to work with no fewer than two launch providers with the aim of crewed landings every six months"
**Source:** NASA HQ Mar 2026 → sources/figure-isaacman/extract.md (crewed-landings-every-6-months)
**Verdict:** Consistent with multi-provider Starship + Blue Moon cadence
**Why:** Two-provider redundancy with 6-month cadence implies SpaceX HLS + Blue Moon as the two providers — both are at TRL where this cadence is plausible by approximately 2028-2030. Consistent with q1 transport-architecture assumptions.
**Severity:** low

### Quote 5
**Statement:** "NASA would be able to afford the new Artemis architecture, space nuclear power development, ongoing science missions and new exploration ventures, as well as working to facilitate the commercialization of low-Earth orbit, with its existing budget, repurposing hardware to focus on the moon and by trimming bureaucratic waste and inefficiency"
**Source:** NASA HQ Mar 2026 → sources/figure-isaacman/extract.md (existing-budget-claim)
**Verdict:** Aspirational; not validated by independent budget analysis
**Why:** The claim that $20B/7yr fits "within existing budget" via efficiency gains is the politically-load-bearing claim and is the most likely to be falsified over time. Our q5 numbers do not depend on this — we take the $20B figure as published and aggregate it against Artemis-transport ($93B OIG). Whether the program "fits" within NASA's top-line is a budget-politics question, not an engineering-capex one.
**Severity:** medium (frequently cited in advocacy without acknowledgement that "fits within budget" is the contested part)

### Quote 6
**Statement:** "Phase 1, Phase 2, Phase 3. If the next administration wants to dial back a little bit of Moon-based spending, no problem"
**Source:** NASA HQ Mar 2026 → sources/figure-isaacman/extract.md (phase-1-2-3)
**Verdict:** Consistent with our staged-milestone framework
**Why:** Phased decomposition is consistent with our M1-M8 milestone structure (q5.c7). Useful as policy-level confirmation that the staged-buildup view is the operating assumption inside NASA leadership.
**Severity:** low

### Quote 7
**Statement:** "NASA is canceling plans to deploy a space station in lunar orbit and will instead use its components to construct a $20 billion base on the moon's surface over the next seven years"
**Source:** NASA HQ Mar 2026 → sources/figure-isaacman/extract.md (gateway-cancelled)
**Verdict:** Consistent with Zubrin 2019 critique; confirms surface-focus
**Why:** Gateway cancellation aligns with Zubrin's long-standing critique and removes one of the recurring cost drivers in legacy lunar-buildup architectures. Improves the credibility of the $20B figure as a surface-only number (no Gateway-orbit overhead).
**Severity:** low

## Cross-reference

- Isaacman's $20B/7yr is the highest-policy-weight anchor on the topic. Per claim q5.c12: combined US public-program through ~2033 is $115-140B order of magnitude (Artemis $93B + Isaacman $20B + operations).
- Scope-corrected, this is below our BAU $150-400B bracket because it excludes manufacturing complement and M8 endpoint.
- Cross-references nasa-oig-2021-artemis-93b (Tier A; $93B Artemis program-of-record audit), spaceflightnow-2026-20b-moonbase (Tier C; primary press coverage), cbs-2026-moonbase (Tier D; mainstream press).
- Codex anti-hallucination check: all quotes trace verbatim to figure-isaacman/extract.md anchors. Verbatim "not flags and footprints" and "every six months" lines are confirmed against both Spaceflight Now and CBS coverage.
