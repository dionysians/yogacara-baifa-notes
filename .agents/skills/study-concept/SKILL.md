---
name: study-concept
description: Use only when the user explicitly invokes `study-concept`, `$study-concept`, or asks to run the `study-concept` workflow for this 《大乘百法明门论》 project. Do not trigger from general semantic similarity. This workflow creates or updates a single concept-study note, concept index entries, and related backlinks for one 百法 concept.
---

# Study Concept

This is a workflow-style skill for this repository. Treat it as the Codex equivalent of the old `/study-concept` command.

## Inputs

- Required: concept name
- Optional: category, source quote, plain-language explanation, key traits, daily example, related concepts

If the concept name is missing, stop and ask for it directly.

## Workflow

1. Read [AGENTS.md](../../../AGENTS.md) before editing anything.
2. Read these files as needed:
   - `.aiwork/templates/concept_note.md`
   - `notes/concept_index.md`
   - `.aiwork/session.yaml`
   - today's log under `notes/logs/`
3. Determine the concept category and target path:
   - `notes/02-心法/`
   - `notes/03-心所法/遍行心所/`
   - `notes/03-心所法/别境心所/`
   - `notes/03-心所法/善心所/`
   - `notes/03-心所法/烦恼心所/`
   - `notes/03-心所法/随烦恼心所/`
   - `notes/03-心所法/不定心所/`
   - `notes/04-色法/`
   - `notes/05-心不相应行法/`
   - `notes/06-无为法/`
4. Create or update the concept note from `.aiwork/templates/concept_note.md`.
5. Fill known fields and leave honest placeholders for unknown material instead of inventing content.
6. If the note contains interpretation beyond direct quotation, follow the three-layer distinction required by `AGENTS.md`.
7. Update `notes/concept_index.md` in the matching section.
8. If related concept notes exist, add reciprocal links carefully without overwriting user content.
9. If today's study log exists and the new concept was studied today, add a short linked entry there.

## Output Expectations

- Report the created or updated note path
- Mention any fields left incomplete
- Mention any backlinks or index entries updated

## Guardrails

- Only use this skill when directly invoked by name
- Preserve existing note structure and user-written content
- Do not fabricate classical citations
- Use repository-relative conventions already present in existing notes
