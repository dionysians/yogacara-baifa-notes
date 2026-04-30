---
name: study-review
description: Use only when the user explicitly invokes `study-review`, `$study-review`, or asks to run the `study-review` workflow for this 《大乘百法明门论》 project. Do not trigger from general semantic similarity. This workflow manages spaced-review queues, due items, and completion updates.
---

# Study Review

This is a workflow-style skill for this repository. Treat it as the Codex equivalent of the old `/study-review` command.

## Modes

- Default: show items due today
- `due`: show all due and overdue items
- `upcoming`: show upcoming reviews
- `all`: show the full review plan
- `complete <id>`: mark one review step complete
- `schedule`: show a review-calendar style view

## Workflow

1. Read [AGENTS.md](../../../AGENTS.md).
2. Read `.aiwork/review_tracker.yaml` and related note or log files referenced by each review item.
3. Interpret dates using the repository timezone and today's actual date.
4. For read modes, group and sort review items by urgency.
5. For `complete <id>`, update only the targeted review item and any directly linked counters.
6. If a linked concept note has a review table and the workflow requires syncing it, append a precise entry without rewriting the rest of the note.

## Output Expectations

- A clear due list with priority, source date, and linked note path when available
- For completion mode, the item updated and the next remaining review state
- For schedule mode, a compact date-grouped calendar summary

## Guardrails

- Only use this skill when directly invoked by name
- Never silently renumber unrelated review items
- Preserve historical completion records
- If tracker structure is inconsistent, explain the inconsistency before editing
