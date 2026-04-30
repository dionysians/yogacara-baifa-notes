---
name: study-log
description: Use only when the user explicitly invokes `study-log`, `$study-log`, or asks to run the `study-log` workflow for this 《大乘百法明门论》 project. Do not trigger from general semantic similarity. This workflow records one study session and updates the linked tracking files.
---

# Study Log

This is a workflow-style skill for this repository. Treat it as the Codex equivalent of the old `/study-log` command.

## Inputs

- Date, defaulting to today if the user does not override it
- Study stage
- Study content
- Duration
- Optional reflections, questions, and key concepts

## Workflow

1. Read [AGENTS.md](../../../AGENTS.md).
2. Read `.aiwork/session.yaml`, `.aiwork/STUDY_PLAN.md`, and `.aiwork/review_tracker.yaml`.
3. Confirm the session is a learning session from `.aiwork/session.yaml`.
4. Gather the session details listed above.
5. Create or update `notes/logs/YYYY-MM-DD_study_log.md`.
6. Update `.aiwork/session.yaml` progress and study-log statistics consistently.
7. Append a matching entry to the study record section in `.aiwork/STUDY_PLAN.md` if that section exists.
8. Add or extend spaced-review entries in `.aiwork/review_tracker.yaml` for the studied content and key concepts.

## Output Expectations

- Report the log file path
- Summarize which tracking files were updated
- Call out any missing fields or structural mismatches found in `.aiwork/*`

## Guardrails

- Only use this skill when directly invoked by name
- Keep date formats consistent with the repository
- Update statistics incrementally rather than rebuilding whole files
- Preserve manual notes already present in study logs and plans
