---
description: Check for due reviews based on Ebbinghaus curve
---

1. **Read Review Tracker**:
   - Read `.aiwork/review_tracker.yaml`.
   - If it doesn't exist, inform the user there are no reviews yet.

2. **Check Due Reviews**:
   - Parse the `reviews` list.
   - For each item, check the `review_schedule`.
   - Find items where `due_date` <= Today AND `completed` is false.

3. **Display Due Items**:
   - Group by urgency:
     - **Overdue**: Due date < Today
     - **Due Today**: Due date == Today
   - List the items: "{Concept Name} (Round {N})".

4. **Action Options**:
   - **Complete**: Ask user if they want to mark any item as completed.
     - If yes, ask for the Item ID or Name.
     - Ask for self-rated mastery (1-5 stars).
     - Update `review_tracker.yaml`: mark current round as complete, set `completed_date`.
     - If mastery is low (<3), consider resetting the schedule or adding an extra review.
   - **Schedule**: Show upcoming reviews for the next 7 days.

5. **Update Files**:
   - Save any changes to `.aiwork/review_tracker.yaml`.
