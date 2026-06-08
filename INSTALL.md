# Install

The `auto-research` engine is a Claude Code skill plus a small set of scripts. Two ways to use it:

1. **As a globally-available skill** — symlink `skill/` into your Claude Code skills directory so you can invoke `/auto-research` from anywhere on your machine.
2. **As a repo-local workflow** — clone the repo, open it in Claude Code, and ask Claude to "run a pass." Claude reads [`skill/SKILL.md`](skill/SKILL.md) directly. No global install required.

Both modes are first-class. Pick whichever fits your workflow.

---

## Prerequisites

- **Node 22+** — for the Astro site
- **Python 3** — for the helper scripts
- **One of these GPT paths** for the Claude+GPT tag team:
  - **Codex CLI** (recommended; bills against your ChatGPT subscription):
    ```bash
    npm install -g @openai/codex
    codex login
    ```
  - **OR** an OpenAI API key:
    ```bash
    export OPENAI_API_KEY="sk-..."
    ```
  - If neither is configured, the engine still runs but marks GPT audits as `unaudited`. You can add the key later and re-run `--pass audit`.

For **cloudflare deploy mode** only (optional — local mode skips all of this):
- Push access to a GitHub remote
- A Cloudflare Pages project pointed at the repo with:
  - Build command: `cd site && npm install && npm run build`
  - Output directory: `site/dist`
  - Environment: `NODE_VERSION=22`

For **local deploy mode** only:
- Nothing additional. After clone + `npm install` the site builds and serves from your machine.

---

## Option 1 — Globally-available skill (recommended)

Symlink the bundled `skill/` directory into your Claude Code skills folder. From the repo root:

```bash
ln -s "$(pwd)/skill" ~/.claude/skills/auto-research
```

Verify:

```bash
ls -la ~/.claude/skills/auto-research/SKILL.md
```

Claude Code picks the skill up on its next session. You can now invoke it from any directory:

```
/auto-research --pass intake
```

The skill's repo-relative paths assume your working directory is an `auto-research-reports` repo. If you keep multiple research projects, clone the repo per-project (or per-organisation) and run the skill from inside each clone.

If you prefer to copy rather than symlink (so changes to the repo don't affect your installed skill):

```bash
cp -R skill ~/.claude/skills/auto-research
```

Re-copy when the repo updates.

---

## Option 2 — Repo-local workflow

Skip the symlink. Just open this repo in Claude Code (or any Claude-driven IDE) and ask Claude to start a new report. The [`CLAUDE.md`](CLAUDE.md) at the repo root tells Claude where the skill lives and how to drive it.

```
You: "Start an auto-research report on whether ocean-thermal-energy beats nuclear for baseload by 2050. Use local deploy mode."
Claude: [reads skill/references/pass-intake.md, runs intake pass, scaffolds reports/ocean-thermal-baseload/, builds site, opens http://localhost:4321/ocean-thermal-baseload/]
```

This is the simplest path for one-off use. No global state, no PATH munging — just clone, install dependencies (`cd site && npm install`), and start the conversation.

---

## First-run setup

After install (either option), do this once:

```bash
cd site
npm install
cd ..
```

This populates `site/node_modules/` so the first build doesn't fight a fresh dependency tree.

Optional: run the build once manually to confirm it works:

```bash
cd site
npm run build
```

You should see output in `site/dist/`. No errors? You're ready.

---

## Deploy mode at intake

When you start your first report, the engine asks which deploy mode you want:

- **`cloudflare`** — every pass commits + pushes to GitHub. Cloudflare Pages auto-rebuilds. Your reports are live at your custom domain (or `*.pages.dev`).
- **`local`** — every pass commits but does not push. `scripts/serve-local.sh` builds the site and serves it at `http://localhost:4321/`. Browser opens automatically on first start.

The choice persists in `reports/{slug}/meta.yaml.deploy.mode`. You can mix modes per-report in a single repo.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `gpt unreachable` in pass logs | No Codex CLI and no `OPENAI_API_KEY` | Install Codex CLI or export an API key; re-run `--pass audit` to back-fill |
| `npm: command not found` | No Node | Install Node 22+ from nodejs.org |
| Local server fails to start | Port 4321 in use | `export AUTO_RESEARCH_PORT=5173` and re-run |
| Local server starts but page is blank | Build failed silently | `cd site && npm run build` — read the error |
| Cloudflare build fails | `NODE_VERSION` not set | Set env var on the Cloudflare project (Settings → Environment variables) |
| Push rejected (cloudflare mode) | Concurrent edits to the same branch | `git pull --rebase` then re-push |
| Skill not appearing in `/` autocomplete | Symlink target doesn't exist | Check `ls -la ~/.claude/skills/auto-research/SKILL.md` |

For deeper issues, read [`SPEC.md`](SPEC.md) and [`skill/SKILL.md`](skill/SKILL.md) — they document the engine's invariants.
