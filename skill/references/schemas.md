# Data Schemas

Every report folder under `reports/{slug}/` must conform. Site rendering depends on it.

## `meta.yaml`

```yaml
slug: lunar-manufacturing                   # matches folder name
root_question: "..."                        # the single question we're answering
status: in_progress | done
current_pass: 7                             # incremented each pass
created: 2026-05-25                         # ISO date
last_updated: 2026-05-26T03:14:00Z          # ISO datetime
models:
  primary: claude-opus-4-7
  critic: gpt-5-pro
deploy:
  mode: cloudflare | local                  # required — set at intake
  cloudflare_project: lunar-manufacturing   # only when mode=cloudflare
  url: https://...                          # optional, set after first deploy
  last_deploy: 2026-05-26T03:14:00Z         # optional
termination:
  root_answered: false
  all_figures_reviewed: false
```

## `01-tree/tree.yaml`

```yaml
root:
  id: root
  question: "..."                           # must match meta.root_question
  answer: null                              # filled by synthesis pass
  status: open | answered

nodes:
  - id: q1-bulk-mass-cost                   # slug, used as URL component
    parent: root                            # parent id ('root' for top level)
    depth: 1                                # 1 = direct child of root
    type: leaf | synthesis | constraint
    question: "..."
    status: open | researching | answered | deprecated
    answer: "..."                           # one-line current best answer; null until set
    confidence: high | medium | low | speculative
    leaf_path: 02-leaves/q1-bulk-mass-cost/ # relative to report root
    created_by: agent | user
    created_pass: 3
    last_touched_pass: 7
    children: [q1.1, q1.2]                  # ids, may be empty
    flags: []                               # e.g. [needs_human_gate, drifted, contested]
```

**Node types:**
- `leaf` — atomic factual question; gets full leaf-pass treatment
- `synthesis` — combines multiple leaves into a derived answer
- `constraint` — structural blocker (Newman's "Side Chapter") — usually qualitative

## `02-leaves/{leaf-id}/leaf.yaml`

```yaml
id: q1-bulk-mass-cost
question: "..."                             # same as tree.nodes[].question
status: open | researching | drafting | reviewed | done
passes_status:
  research: pending | in_progress | done | needs_rerun
  calc: pending | in_progress | done | needs_rerun
  reconcile: pending | in_progress | done | needs_rerun
  source-review: pending | in_progress | done | needs_rerun
  consistency: pending | in_progress | done | needs_rerun
  write: pending | in_progress | done | needs_rerun
last_pass: 5
contradictions_with: []                     # leaf ids surfaced by consistency pass
```

## `02-leaves/{leaf-id}/claims.yaml`

A list of claims — the prose substrate. **Every factual statement in the leaf's prose must trace to a claim here.**

```yaml
- id: q1.c1                                 # leaf-prefixed
  text: "Starship LEO delivery cost falls to $100/kg by 2030 (optimistic case)."
  type: factual | derived | estimate
  evidence:
    - source: spacex-iac-2024                # slug under sources/
      ref: slide-12                         # specific anchor inside extract.md
      verdict: supports | contradicts | partial
  confidence: high | medium | low | speculative
  derivation_path: passes/pass-02-calc.md   # only for type: derived
  audit:
    gpt:
      status: passed | flagged | unaudited
      audit_file: passes/pass-02-audit.md
      notes: "..."                          # short summary of any flag
    human:
      status: noted | unnoted
      comment_file: notes/user-2026-05-26.md
```

## `02-leaves/{leaf-id}/sources/{source-slug}/extract.md`

**Structured notes**, not raw text dump. With 50+ sources per leaf the full-text approach overflows context — extracts must be tractable. See [`source-tiers.md`](source-tiers.md) for tier definitions; review depth varies by tier.

Frontmatter:
```yaml
---
slug: spacex-iac-2024
title: "Elon Musk IAC 2024 Keynote"
url: "https://..."
fetched: 2026-05-26
fetcher: claude | user
tier: S | A | B | C | D | E         # canonical tier (see source-tiers.md)
type: paper | preprint | book | report | press | blog | podcast | tweet | thread | speech | interview
peer_reviewed: true | false
venue: "Nature" | "AIAA SciTech 2024" | "ArXiv" | "Spaceflight Now"   # required for S/A
authors: ["Elon Musk"]
year: 2024
date: 2024-09-15                     # full ISO date if available
topics: [topic-slug, ...]            # cross-leaf topic tags; see topics.yaml
public_figure: "Elon Musk"           # set for tier B sources only
---
```

Body structure — `## Abstract`, `## Key claims`, `## Reviewer notes`:

```markdown
## Abstract
(150-300 words. Author's abstract verbatim if it exists; otherwise our tight distillation.)

## Key claims
- claim-anchor-1: [verbatim quote or tight paraphrase] (page/section ref if known)
- claim-anchor-2: ...
(3-7 claims for tier S/A. Fewer for lower tiers.)

## Reviewer notes
(50-150 words: what's load-bearing for our question, what's tangential, what's notably absent, who the author cites.)
```

Anchors like `## key-claims` / `### claim-anchor-1` let `claims.yaml` evidence entries point at specific pieces via `ref:`.

**Optional `raw.md`** alongside `extract.md` preserves full extracted text for tier S/A when we anticipate deep re-review. Tier C/D never store raw. Tier E gets no extract at all — it's orientation only and doesn't appear in `sources/`.

## `02-leaves/{leaf-id}/sources/{source-slug}/review.md`

Review depth depends on tier (see [`source-tiers.md`](source-tiers.md)).

### Tier S — full claim-by-claim review

```markdown
---
source: metzger-2023-lunar-economy
tier: S
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: Metzger 2023 — Lunar economy framework

## Summary

| Verdict | Count |
|---|---|
| Consistent | 3 |
| Different conclusion | 1 |
| Novel supporting | 2 |
| Merits investigation | 1 |
| Not relevant | 4 |

## Claim 1: "Lunar manufacturing crosses over at L_p > 35 × Γ_LEO"
**Quote:** "..." (verbatim from extract.md)
**Verdict:** Consistent
**Why:** Our q4 derivation reproduces this within tolerance.

## Claim 2: ...
```

### Tier A — medium review (key claims only)

```markdown
---
source: aiaa-2024-mass-driver-survey
tier: A
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: AIAA 2024 mass-driver survey

**Overall verdict:** consistent | different_conclusion | mixed | novel | not_relevant
**Two-sentence summary:** ...

## Key claims
- "..." → Consistent / Different / Novel / Merits / Not-relevant — one-sentence justification
- "..." → ...
(3-5 key claims, not every claim in the paper.)
```

### Tier B — quote/claim review (per public figure)

This is the "what do important people say" tier. Renders on the site as a person card. One review.md per public figure, even if their quotes come from multiple containers.

```markdown
---
public_figure: "Elon Musk"
tier: B
reviewed_pass: 4
reviewed_by: claude+gpt
roles: ["SpaceX CEO", "Tesla CEO"]
relevance: "Primary stakeholder in Starship cost projections"
---

# Public figure: Elon Musk

## Quotes reviewed

### Quote 1
**Statement:** "Starship will achieve $10/kg to LEO by 2027"
**Source:** IAC 2024 keynote, Sept 15 2024 → sources/spacex-iac-2024/extract.md
**Verdict:** Contradicts our analysis
**Why:** Our q1 framework projects $59-878/kg under any operationally-evidenced reuse rate. The $10/kg figure requires sub-2% refurb AND zero-margin pricing AND TAI-grade automation — three load-bearing assumptions Musk does not defend.
**Severity:** medium (aspirational target, frequently cited)

### Quote 2
**Statement:** "..."
...
```

### Tier C — scalar verdict + one paragraph

```markdown
---
source: spaceflight-now-2026-03-30
tier: C
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: Spaceflight Now — B1076 34-reuse milestone

**Verdict:** Consistent
**Confidence:** high

The article reports a 34-reuse milestone on Falcon 9 first-stage B1076, March 2026. This is direct empirical support for our q1 partial-reuse scenario (30 reuses). No conflicting claims. Treats the milestone factually with stage-flow images and recovery telemetry — no editorial extrapolation. Useful as load-bearing evidence for q1.c6.
```

### Tier D — same shape as C, with conflict-flag check

```markdown
---
source: nyt-2026-05-12-lunar
tier: D
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: NYT — "Why we'll never go back to the Moon"

**Verdict:** Mixed
**Confidence:** medium
**Conflicts with higher tier?** Yes — see flag.

General-press piece. Some claims align with q3 ISRU TRL findings (carbothermal at TRL 6, plausible). Other claims contradict Metzger (tier S): article implies ISRU is "decades away" without engaging with the actual TRL roadmap. Flag for synthesis: where general press lags peer-reviewed by 5+ years, our synthesis should foreground the tier-S view.
```

## `pass-log.jsonl`

One JSON object per line, appended each pass.

**Required fields:** `pass_id`, `focus`, `kinds`, `started`, `ended`, `models`, `outcome`, `commit`, `artifacts`, `human_input`.

The `human_input` field captures user messages verbatim — every prompt, critique, or guidance from the user that shaped this pass. Multiple messages concatenated with `\n---\n`. Empty string (`""`) for purely autonomous passes. The pass log is a record of the collaboration, not just of Claude's actions; without the user's tokens the log is half the story.

```jsonl
{"pass_id":"p001","focus":"intake","kinds":["intake"],"started":"2026-05-25T20:00:00Z","ended":"2026-05-25T20:18:00Z","models":["claude"],"outcome":"tree v1 created with 7 leaves","commit":"a3f8c2","artifacts":["meta.yaml","01-tree/tree.yaml"],"human_input":"start a new auto-research on whether the Moon is necessary for cosmic-scale mass throughput"}
{"pass_id":"p002","focus":"leaf:q1-bulk-mass-cost","kinds":["research","calc"],"started":"...","ended":"...","models":["claude","gpt"],"outcome":"5 claims added, 1 flagged","commit":"b7d4e1","artifacts":["...","..."],"human_input":"begin with q1"}
```

## Privacy

In `local` deploy mode there is no public surface — nothing leaves the machine. In `cloudflare` deploy mode, content marked `private: true` in frontmatter is stripped before commit. Sensitive notes belong in `notes/private/` (gitignored by default). Default to public — the whole point is shareable reports.
