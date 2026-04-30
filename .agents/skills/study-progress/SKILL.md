---
name: study-progress
description: Use only when the user explicitly invokes `study-progress`, `$study-progress`, or asks to run the `study-progress` workflow for this 《大乘百法明门论》 project. Do not trigger from general semantic similarity. This workflow views or updates overall learning progress, stage status, and study statistics.
---

# Study Progress

This is a workflow-style skill for this repository. Treat it as the Codex equivalent of the old `/study-progress` command.

## Modes

- Default: show current progress
- `update`: change stage progress or current stage
- `stats`: produce detailed statistics

## Workflow

1. Read [AGENTS.md](../../../AGENTS.md).
2. Read `.aiwork/session.yaml`, `.aiwork/STUDY_PLAN.md`, `.aiwork/review_tracker.yaml`, `notes/`, and `notes/logs/` as needed.
3. For default mode, report:
   - project start date
   - current stage
   - completion percentage
   - stage-by-stage status
   - study counts and time
   - note, log, and review counts
4. For `stats`, compute richer counts from the current repository state rather than relying only on stored summaries.
5. For `update`, modify the smallest necessary set of fields in `.aiwork/session.yaml` and `.aiwork/STUDY_PLAN.md`.
6. When marking a stage complete, keep dates, percentages, and stage-history fields synchronized.

## Output Expectations

- For read mode: a concise progress dashboard
- For update mode: exact fields changed and the new effective status
- For stats mode: a compact but concrete report with computed counts

## Guardrails

- Only use this skill when directly invoked by name
- Prefer repository truth over stale cached counters
- Do not overwrite narrative sections of the study plan unless the workflow specifically updates them
