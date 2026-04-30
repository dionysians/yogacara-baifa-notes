---
description: Record daily study session, update progress, and log insights
---

1. **Check Session State**:
   - Read `.aiwork/session.yaml` to confirm it exists.
   - If not found, ask the user to initialize the session first.

2. **Gather Information**:
   - Ask the user for the following information (you can ask all at once or step-by-step):
     - **Date**: (Default to today)
     - **Stage**: (Which stage 1-7 are they studying?)
     - **Content**: (What did they study? e.g., "Read verses 1-5")
     - **Duration**: (In minutes)
     - **Insights**: (Optional: Any key takeaways?)
     - **Questions**: (Optional: Any doubts?)
     - **Keywords**: (Optional: Key concepts learned)

3. **Create Log File**:
   - Generate a filename: `notes/logs/{YYYY-MM-DD}_study_log.md`.
   - Create the file using the following structure:
     ```markdown
     # 学习日志 - {YYYY年MM月DD日}
     
     > **学习项目**: 大乘百法明门论
     > **学习阶段**: {Stage Name}
     > **学习时长**: {Duration}分钟
     > **日期**: {YYYY-MM-DD}
     
     ---
     
     ## 📖 学习内容
     {Content}
     
     ---
     
     ## 💭 学习心得
     {Insights or "_今日无特别心得记录_"}
     
     ---
     
     ## 🤔 疑难问题
     {Questions or "_今日无疑问记录_"}
     
     ---
     
     ## 🔑 关键概念
     {Keywords or "_今日无关键概念记录_"}
     ```

4. **Update Session Data**:
   - Read `.aiwork/session.yaml`.
   - Update `study_log.total_sessions` (increment by 1).
   - Update `study_log.total_hours` (add duration).
   - Update `study_log.last_session_date` (to today).
   - Write the updated content back to `.aiwork/session.yaml`.

5. **Update Study Plan**:
   - Read `.aiwork/STUDY_PLAN.md`.
   - Locate the "5.2 学习记录" table.
   - Append a new row: `| {Date} | {Content Summary} | {Duration}m | [查看日志](../notes/logs/{Date}_study_log.md) | {Insight Summary} |`.
   - Write the updated content back to `.aiwork/STUDY_PLAN.md`.

6. **Update Review Tracker**:
   - Read `.aiwork/review_tracker.yaml` (create if missing).
   - Add a new entry to `reviews` list with the learned content and schedule reviews for +1, +2, +4, +7, +15 days.
   - Write the updated content back.

7. **Summary**:
   - Notify the user that the log has been saved.
   - Show a brief summary of the session stats.
