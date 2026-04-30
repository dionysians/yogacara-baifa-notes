---
name: study-stage
description: Use only when the user explicitly invokes `study-stage`, `$study-stage`, or asks to run the `study-stage` workflow for this 《大乘百法明门论》 project. Do not trigger from general semantic similarity. This workflow starts or re-enters a learning stage, prepares stage files, and aligns stage tracking data.
---

# Study Stage

This is a workflow-style skill for this repository. Treat it as the Codex equivalent of the old `/study-stage` command.

## Inputs

- Required: stage number `1-7`
- Optional: whether to continue, restart, or only inspect an already-started stage

## Workflow

1. Read [AGENTS.md](../../../AGENTS.md).
2. Read `.aiwork/session.yaml` and `.aiwork/STUDY_PLAN.md`.
3. Validate the requested stage number and map it to the stage structure already used in the repository:
   - 1: 准备与概览
   - 2: 心法
   - 3: 心所法
   - 4: 色法
   - 5: 心不相应行法
   - 6: 无为法
   - 7: 整合与深化
4. Check the previous stage state and the requested stage's existing status.
5. If starting or restarting, prepare the stage directory, `README.md`, and `stage_summary.md` scaffold as appropriate for that stage.
6. Update `.aiwork/session.yaml` and `.aiwork/STUDY_PLAN.md` so current stage, dates, and progress remain consistent.
7. Reuse the repository's existing stage folder naming and subfolder layout instead of inventing a new structure.

## Output Expectations

- Report the stage entered
- Report any files created or updated
- Mention prerequisites or incomplete prior stages if relevant

## Guardrails

- Only use this skill when directly invoked by name
- Avoid resetting an active stage unless the user explicitly asks for restart behavior
- Keep stage names and numbering consistent with the existing repository
