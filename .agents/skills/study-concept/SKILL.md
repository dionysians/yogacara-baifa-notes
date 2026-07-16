---
name: study-concept
description: Use only when the user explicitly invokes `study-concept`, `$study-concept`, or asks to run the `study-concept` workflow for this 《大乘百法明门论》 project. Do not trigger from general semantic similarity. Executes the complete Claude `/study-concept` command contract without simplifying it.
---

# Study Concept

This repository keeps the detailed workflow in one canonical place so the Claude command and Codex skill cannot drift.

## Required execution contract

1. Read [`AGENTS.md`](../../../AGENTS.md) completely before taking action.
2. Read [the canonical Claude command](../../../.claude/commands/study-concept.md) completely, from the first line through the end, every time this skill runs.
3. Execute that command as the binding workflow specification. Preserve all of its modes, parameter validation, questions and their order, calculations, templates, file reads and writes, synchronization rules, confirmations, error handling, examples, and final output requirements.
4. Do not replace the command with a summary, skip an interaction because this adapter is shorter, or invent behavior that is absent from the command.
5. Treat `$study-concept <arguments>`, `study-concept <arguments>`, and the command's `/study-concept <arguments>` syntax as the same invocation. Translate only the invocation syntax; keep the workflow's observable behavior and repository changes unchanged.
6. When the command requires user input that was not supplied, ask for it at the exact point prescribed by the command. When the input is already present in the conversation or repository, reuse it instead of asking again.

The linked Claude command is the source of truth. If this adapter and the command ever appear to disagree, follow the command.
