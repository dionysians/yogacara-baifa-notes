---
description: Initialize a new learning stage
---

1. **Get Stage Number**:
   - Ask the user which stage to start (1-7).
   - Refer to `STUDY_PLAN.md` for stage names if needed.

2. **Check Prerequisites**:
   - Read `.aiwork/session.yaml` to see the current phase.
   - Warn if the previous stage is not marked as complete (unless user insists).

3. **Create Directories**:
   - Based on the stage number, create the directory: `notes/{StageNumber}-{StageName}/`.
   - Example: `notes/02-心法/`.

4. **Create Stage Files**:
   - **README.md**: Create a `README.md` in the stage directory with:
     - Stage Name
     - Start Date (Today)
     - Goals (Extract from `STUDY_PLAN.md` if possible, or leave placeholders)
   - **Summary Template**: Create `stage_summary.md` with a template for future use.

5. **Update Session**:
   - Update `.aiwork/session.yaml`:
     - Set `current_phase` to the new stage.
     - Add entry to `stage_history`.

6. **Update Plan**:
   - Update `.aiwork/STUDY_PLAN.md`:
     - Mark the new stage as "In Progress" in the progress table.
     - Set the start date.

7. **Confirmation**:
   - Notify the user that Stage {N} has started and directories are ready.
