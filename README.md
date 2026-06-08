# Auto-Research Reports

A multi-pass agentic research engine. You give Claude a research question; it builds a structured report — claim graph, source reviews, point-by-point critique, dual-model synthesis — one re-runnable pass at a time, with the result rendered as a live webpage.

The engine reverse-engineers and corrects the failure modes of Steve Newman's [Centaur Era](https://secondthoughts.ai/p/the-centaur-era) auto-research approach. The full design lives in [`SPEC.md`](SPEC.md); the orchestrator skill lives in [`skill/`](skill/).

## What's in the box

- **The skill** ([`skill/SKILL.md`](skill/SKILL.md) + [`skill/references/`](skill/references/)) — a Claude Code skill that drives the engine. Symlink it into your skills directory, or let Claude read it directly from the repo.
- **The site** ([`site/`](site/)) — an Astro app that reads any number of reports from `reports/` and renders them at `/{slug}/`. Multi-tenant by default.
- **The scripts** ([`scripts/`](scripts/)) — small Python and shell helpers: scaffold a new report, ask GPT for a critique, deploy a pass.
- **The spec** ([`SPEC.md`](SPEC.md)) — data primitives, pass types, anti-patterns. Read first if you're going to extend the engine.

## Two deploy modes

Pick at intake; persists in `meta.yaml`; can be mixed per-report in a single repo.

| Mode | What happens after each pass | When |
|---|---|---|
| **`cloudflare`** | Commit + push. Cloudflare Pages auto-rebuilds. Reports live at your custom domain. | Public sharing, multi-device access. |
| **`local`** | Commit (no push). Builds the site and serves it on `http://localhost:4321/`. | Private research, offline work, no Cloudflare/GitHub required. |

Both modes render every report on the same site at `/{slug}/` — only the host differs.

## How it works (60 seconds)

1. **Intake.** You give a root question. The engine scaffolds a report folder, generates a 5-10 leaf question tree, and deploys the first version of the site (live in <15 minutes).
2. **Per-leaf passes.** Each leaf goes through six sub-passes — research, first-principles calc, reconcile, source review, consistency check, write — with a Claude+GPT tag team at every writing step.
3. **Cross-leaf consistency.** Contradictions between leaves are surfaced as required-resolution items, not buried.
4. **Synthesis.** Claude and GPT independently write synthesis reports. A diff agent triages style vs. substance. Substantive disagreements trigger a debate phase, then consensus extraction, then v2 writes.
5. **Audit.** Walks every claim, every source, every calc. Verifies links. Re-derives derivatives. Mandatory before declaring done.

You stay in the loop. Between passes you delete drifted questions, seed new ones, resolve flagged contradictions — the engine runs each pass, you punctuate with judgement.

## Quick start

```bash
git clone https://github.com/AviParrack/auto-research-reports.git
cd auto-research-reports
cd site && npm install && cd ..

# Install the skill (or skip — see INSTALL.md option 2)
ln -s "$(pwd)/skill" ~/.claude/skills/auto-research
```

In Claude Code (or any Claude-driven environment), in this repo's directory:

```
/auto-research --pass intake
```

The skill prompts for your root question, time horizon, seed sources, and deploy mode. After ~10-15 minutes you'll have a tree v1 and a live site.

For full setup including dependencies and Cloudflare Pages configuration, see [`INSTALL.md`](INSTALL.md). For the engine's design rationale, see [`SPEC.md`](SPEC.md).

## What makes this different

Most LLM research tools fail in the same way: paragraph-by-paragraph narrative that's plausible-sounding but doesn't survive cross-section logic. The structural fix is the engine's core thesis:

1. **Claim graph as substrate.** Every factual statement in prose traces to a claim ID in `claims.yaml`. Prose is rendered from the graph, never the other way around.
2. **First-principles calc with sources sealed.** The math pass doesn't peek at existing sources. Reconciliation happens later — when calc and sources disagree, that's data, not a bug to paper over.
3. **Claude+GPT tag team at every step.** Single-model echo chambers are countered structurally. GPT critiques claim-by-claim; Claude responds; unresolved goes to the user.
4. **Point-by-point source review against every major figure.** "Did the analysis check what each public figure on the topic actually says?" — Newman's termination criterion #2, encoded.
5. **Git-committed pass log.** Every pass is a commit. Every artifact is reproducible. Every decision is auditable.

Full anti-pattern list and the Newman-citation rationale: [`SPEC.md` → Anti-Patterns](SPEC.md#anti-patterns-the-things-you-are-explicitly-designing-against).

## Status

The engine is operational. Real reports built with it: see `reports/`. Site shell, multi-tenant rendering, pass log visualisation, audit overlay, and search are all wired. The pieces still settling: per-tier source rendering polish, debate-skill integration, plot synthesis cohesion across leaves.

## License

MIT. Use it, fork it, build something better. If you do, file an issue — the engine improves fastest with adversarial users.

## Credit

Inspired by Steve Newman's [The Centaur Era](https://secondthoughts.ai/p/the-centaur-era). The structural fixes here are responses to the failure modes Newman flagged in his own footnote 11.
