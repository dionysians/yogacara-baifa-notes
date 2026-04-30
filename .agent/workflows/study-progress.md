---
description: View or update the overall learning progress
---

1. **Read Session Data**:
   - Read `.aiwork/session.yaml`.
   - Extract `progress` data (start date, current phase, completion percentage).

2. **Read Study Plan**:
   - Read `.aiwork/STUDY_PLAN.md`.
   - Parse the "5.1 阶段进度" table to get the status of each stage.

3. **Display Progress**:
   - Show a summary to the user:
     - **Overall Progress**: {completion_percentage}%
     - **Current Phase**: {current_phase}
     - **Days Active**: (Calculate from start date)
     - **Stage Status**: List each stage and its status (Completed/In Progress/Not Started).

4. **Update Option**:
   - Ask the user if they want to update the progress.
   - If yes:
     - Ask which stage to update.
     - Ask for the new status or completion percentage.
     - Update `.aiwork/session.yaml` and `.aiwork/STUDY_PLAN.md` accordingly.
     - If a stage is marked "Completed", prompt to create a stage summary (refer to `study-stage` workflow logic).

5. **Stats Option**:
   - If the user asks for stats, read `.aiwork/session.yaml` `study_log` section.
   - Display total sessions, total hours, and average duration.
