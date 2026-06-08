# Pass: Tree

Refine the question DAG. Add new nodes, deprecate drifted ones, restructure parent links. The most-frequent pass between heavy leaf passes.

## When to run
- After a leaf reveals new dependencies (consistency pass flagged a missing question)
- After the user seeds new direction via `--message`
- Before synthesis, to verify completeness
- After audit, to act on flagged drift

## Procedure

### 1. Read current state
- `tree.yaml` (current)
- `meta.yaml`
- `feedback.md` if exists
- Any `notes/` the user added
- `01-tree/history/` to see what's already been tried

### 2. Apply the user's `--message` first (highest priority)
If `--message "..."` was passed, that's the explicit guidance for this pass. Implement it literally. Don't second-guess. If the user says "add a branch on political economy," add that branch.

### 3. Run drift check on existing nodes
For each node, ask:
- Does answering this directly contribute to answering the root?
- Has subsequent research revealed this branch is tangential?
- Is this node a duplicate of another?

Mark drifted nodes with `flags: [drifted]`. Don't delete — flag for the user (they remove via subsequent message-pass or by editing tree.yaml manually).

### 4. Propose new nodes (autonomous expansion)
Allowed depth: +1 from existing tree depth. Beyond that, flag for the user.

For each proposed new node:
- Sharp question, not a topic
- Justify in `growth-log.md`: "Added because the calc pass for q1 surfaced an unaddressed assumption about X..."
- Set `created_by: agent`, `created_pass: {current}`

### 5. Write
- Snapshot current `tree.yaml` to `01-tree/history/v{N}.yaml` before any change
- Update `tree.yaml`
- Append to `01-tree/growth-log.md`: what changed, why, by whom (agent or user)
- For new leaves, create stub `02-leaves/{leaf-id}/leaf.yaml`

### 6. Tag team
Tree changes are structural, not claim-bearing — generally skip the Claude+GPT tag team. EXCEPTION: if the user's `--message` is contested (e.g., "I don't think this branch matters"), invoke GPT to give a second opinion before deprecating.

### 7. Report to the user
- Added: {N} new nodes with one-line each
- Flagged as drifted: {N} (waiting for the user's call)
- Deepened beyond depth+1: {N} (waiting for the user's gate)
- Suggested next: next leaf to run, or synthesis if tree feels complete
