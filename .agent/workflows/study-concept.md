---
description: Create a structured note for a new concept (Dharma)
---

1. **Get Concept Name**:
   - Ask the user for the name of the concept (e.g., "触", "眼识").

2. **Determine Category**:
   - Ask the user which of the 5 Categories (五位) this concept belongs to:
     1. Mind (心法)
     2. Mental Factors (心所法) - Specify sub-group (e.g., 遍行, 别境)
     3. Form (色法)
     4. Non-associated (心不相应行法)
     5. Unconditioned (无为法)

3. **Gather Details**:
   - Ask for:
     - **Definition**: (White vernacular explanation)
     - **Original Text**: (Quote from the treatise if available)
     - **Core Features**: (Key characteristics)
     - **Examples**: (Daily life examples)

4. **Determine Path**:
   - Based on the category, determine the correct directory:
     - Mind -> `notes/02-心法/`
     - Mental Factors -> `notes/03-心所法/{SubGroup}/`
     - Form -> `notes/04-色法/`
     - Non-associated -> `notes/05-心不相应行法/`
     - Unconditioned -> `notes/06-无为法/`

5. **Create Note**:
   - Read the template at `.aiwork/templates/concept_note.md`.
   - Replace placeholders (`{概念名称}`, `{类别}`, etc.) with user input.
   - Write the file to the determined path: `{Path}/{ConceptName}.md`.

6. **Update Index**:
   - Read `notes/concept_index.md`.
   - Add the new concept to the corresponding table.
   - Write the file back.

7. **Update Review Tracker**:
   - // turbo
   - Run the `study-review` workflow (or logic) to add this new concept to the review schedule immediately.

8. **Confirmation**:
   - Inform the user the note has been created at `{Path}/{ConceptName}.md`.
/