---
leaf: q1-earth-industrial-ceiling
pass: write-response
responding_to: pass-write-audit.md
auditor: codex / gpt-5.5
responder: claude-opus-4-7
---

# Response to Codex write-pass audit

## Accepted (will patch the write)

- **Headline OOM contradiction (high):** I wrote "three to four orders of magnitude below" Tt/yr in the headline, then "one to three OOM" later in the same paragraph and in q1.c9. Internal contradiction. **Fix:** change headline to "one to three orders of magnitude" — single, consistent OOM count throughout.

- **Bury-the-lead at ~256 words (medium):** the motivation + where-it-fits sections push the headline past 200 words. **Fix:** compress motivation to ~80 words and where-it-fits to ~60 words, putting headline at ~150 words.

- **"Manhattan Project / Interstate Highway / aircraft manufacturing" comparison (high unsupported):** these are rhetorical flourishes not encoded in any claim. **Fix:** remove the sentence; keep only the quantitative substance (ASU count, pad count, engine count, ASU power).

- **"Architecturally necessary" / "load-bearing handoff" (high unsupported synthesis):** these are synthesis moves belonging to q9, not q1. **Fix:** soften to "this is the upper bound on Earth alone; q9 will determine whether the Moon channel reaches above it."

- **Editorialising phrases (medium):** Codex flagged "by a wide margin," "civilizational-scale," "categorical-scale infeasibility," "architecturally necessary," "enormous," "cinematic-imagination," "not a luxury," "load-bearing piece of architecture." Per anti-pattern #13, replace with quantitative substance. **Fix:** remove most; the few that remain ("civilizational-scale") will be re-cast as quantitative ("requires ~$1.1T new capex").

## Disputed / clarified

- **"Why this matters / Where it fits" not in claims (medium):** the leaf-write schema (anti-pattern #12) *requires* a motivation + where-it-fits section before the headline. Codex flagged this as unsupported, but the spec explicitly allows context-framing here. **Clarification:** these sections are structural framing, not load-bearing claims; the per-claim audit applies to the body, not the framing.

- **Manhattan/Interstate as rhetorical flourishes (high):** ACCEPT. Removing.

- **Helium / cryogenic / avionics / hydrolox / EPA-retrieval in Limitations (medium):** Codex flagged these as not-in-claims. But the leaf-write schema (anti-pattern #12 step 6) *requires* a Limitations section. Per the source-tier schema, Limitations are known-omissions, not load-bearing claims that need to appear in `claims.yaml`. **Clarification:** these are surfaced from pass-02-calc.md "Caveats and known omissions" footer (Codex audit informed) — they belong in Limitations by design.

- **Launch loop / TRL / hydrolox / TAI in "What changes if the answer flips" (medium):** these are sensitivity-scenario sketches, not claims. ACCEPT in principle: should mark as `type: estimate` claims if cited as facts. **Fix:** soften to "out-of-scope for this leaf; flagged for future cross-leaf work" without specific numbers; or move the specific numbers to claims with `confidence: speculative`.

## What changes substantively

- Headline OOM number (fix from 3-4 to 1-3).
- Compress motivation + where-it-fits to ≤200 combined words.
- Remove Manhattan Project / Interstate Highway / aircraft-manufacturing rhetorical comparisons.
- Soften "architecturally necessary" / synthesis-move framing.
- Trim editorialising verbs (anti-pattern #13).
- Add a Note: "What changes if the answer flips" section's specific numbers (Lofstrom 4 GW / 750 kt/yr / $3/kg) cite the workspace anchor extract; mark as speculative/sensitivity-only.

## What does not change

- The binding-input ordering (LOX → engines → pads → ASU power → methane → steel).
- The 1-100 Mt/yr ceiling band.
- The Tt/yr-impossibility conclusion.
- The confidence labels per claim.
- The structure of the leaf-write (motivation → where-it-fits → headline → body → confidence → limitations).
