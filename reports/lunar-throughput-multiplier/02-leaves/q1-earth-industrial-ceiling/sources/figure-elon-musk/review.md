---
public_figure: "Elon Musk"
tier: B
reviewed_pass: 6
reviewed_by: claude+gpt
roles: ["SpaceX CEO", "Tesla CEO", "X owner"]
relevance: "Primary stakeholder in Starship cadence projections; statements are inputs to industry expectations"
---

# Public figure: Elon Musk

## Quote 1

**Statement:** "Maybe as high as 10,000 ships per year" — Starship production target, replying to an X post about scaling Starship production "similar to how aircraft manufacturers do."
**Source:** Reported by Benzinga, January 4, 2026 → [musk-10k-ships-2026-01/extract.md](../musk-10k-ships-2026-01/extract.md)
**Verdict:** **Contradicts** (in the sense that the constraint is wrong, not the number)
**Why:** Musk's stated target frames the binding constraint as ship production. The q1 calc shows LOX binds well before ship production at any aspirational reuse cadence. At 100-flight reuse, 10,000 ships/yr supports ~10⁶ launches/yr in steady-state — but reaching that launch rate requires ~1,350 Baytown-class ASUs ($1.1T capex) and ~2,740 launch pads. **Ship production is not the binding constraint; LOX is.** This is a real disagreement: Musk's framing assumes the production line is the bottleneck, while the supply-chain analysis shows it isn't.
**Severity:** medium — the stated target is widely cited, and the implied "if we produce N ships we can do N flights" reasoning is structurally wrong.
**Cited in:** [q1.c10](../../claims.yaml).

## Quotes not reviewed

Several other Musk statements (e.g., "$10/kg to LEO", "Starship launches every hour within 3 years", "Mars by 2030") are not directly cited in q1; their review belongs to sibling leaves (lunar-manufacturing q1-earth-launch-cost covers the $10/kg target). If they surface in source-review or audit passes for q1, append here.
