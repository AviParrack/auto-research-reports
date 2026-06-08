#!/usr/bin/env python3
"""
Scaffold a new report folder. Used by the intake pass.

Usage:
  new-report.py --slug lunar-manufacturing --question "When does..." [--seeds path/to/seeds.md]

Creates:
  reports/{slug}/meta.yaml
  reports/{slug}/00-intake/question.md
  reports/{slug}/01-tree/tree.yaml (empty nodes list)
  reports/{slug}/pass-log.jsonl (empty)
"""

import argparse
import datetime as dt
import os
import sys
import textwrap

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPORTS_DIR = os.path.join(REPO_ROOT, "reports")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--question", required=True)
    ap.add_argument("--seeds", help="Path to a markdown file with seed sources/notes")
    ap.add_argument("--primary-model", default="claude-opus-4-7")
    ap.add_argument("--critic-model", default="gpt-5-pro")
    ap.add_argument(
        "--deploy-mode",
        choices=["cloudflare", "local"],
        default="cloudflare",
        help="cloudflare: commit+push, Pages auto-rebuilds. local: commit+serve on localhost:4321.",
    )
    args = ap.parse_args()

    slug = args.slug.strip().lower()
    if not slug.replace("-", "").isalnum():
        sys.stderr.write("slug must be lowercase alphanumeric + hyphens\n")
        sys.exit(3)

    target = os.path.join(REPORTS_DIR, slug)
    if os.path.exists(target):
        sys.stderr.write(f"refusing to overwrite existing report: {target}\n")
        sys.exit(3)

    os.makedirs(os.path.join(target, "00-intake"), exist_ok=True)
    os.makedirs(os.path.join(target, "01-tree", "history"), exist_ok=True)
    os.makedirs(os.path.join(target, "02-leaves"), exist_ok=True)
    os.makedirs(os.path.join(target, "03-synthesis"), exist_ok=True)
    os.makedirs(os.path.join(target, "audits"), exist_ok=True)

    today = dt.date.today().isoformat()
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if args.deploy_mode == "cloudflare":
        deploy_block = f"""\
        deploy:
          mode: cloudflare
          cloudflare_project: {slug}"""
    else:
        deploy_block = """\
        deploy:
          mode: local"""

    meta = textwrap.dedent(f"""\
        slug: {slug}
        root_question: "{args.question}"
        status: in_progress
        current_pass: 0
        created: {today}
        last_updated: {now}
        models:
          primary: {args.primary_model}
          critic: {args.critic_model}
{deploy_block}
        termination:
          root_answered: false
          all_figures_reviewed: false
    """)

    question_md = textwrap.dedent(f"""\
        # Root Question

        **{args.question}**

        ## Why this question

        _Fill in during intake pass._

        ## Scope notes

        - Time horizon: _tbd_

        ## Seed sources

        _Fill in during intake pass._
    """)

    if args.seeds and os.path.isfile(args.seeds):
        with open(args.seeds) as f:
            seeds_content = f.read()
        question_md += "\n\n## Seed material\n\n" + seeds_content

    tree_yaml = textwrap.dedent(f"""\
        root:
          id: root
          question: "{args.question}"
          answer: null
          status: open

        nodes: []
    """)

    with open(os.path.join(target, "meta.yaml"), "w") as f:
        f.write(meta)
    with open(os.path.join(target, "00-intake", "question.md"), "w") as f:
        f.write(question_md)
    with open(os.path.join(target, "01-tree", "tree.yaml"), "w") as f:
        f.write(tree_yaml)
    open(os.path.join(target, "pass-log.jsonl"), "w").close()
    open(os.path.join(target, "feedback.md"), "w").close()

    print(f"created {target}")
    print(f"next: run intake pass to populate tree.yaml")


if __name__ == "__main__":
    main()
