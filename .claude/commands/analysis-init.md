# Initialize Analysis Session Overview

You are the session overview creator for data analysis sessions. When the user runs this command, guide them through creating a comprehensive SESSION.md document.

## Command Usage

```
/analysis-init
```

**No parameters required.** This command is interactive.

**Prerequisites:**
- Must have an active session of type "data-analysis"
- Should be run after `/session-init data-analysis <name>`

---

## Your Tasks

### 1. Check Session Type and Read Language Setting

First, verify this is a data-analysis session and read language preference:

Read `.aiwork/session.yaml`:
- Check `type: "data-analysis"` → If not, show error
- Read `language` field → Use this for all generated content

**Language setting:**
- If `language: "en"` → Generate all content in English
- If `language: "zh"` → Generate all content in Chinese (中文)
- If `language` not set → Default to English

**Error if not data-analysis session:**
```
❌ This command is for data analysis sessions only

Your session type: {type}

For data analysis sessions:
1. Initialize session: /session-init data-analysis <name>
2. Then run: /analysis-init

For other session types:
- software → /project-init
- content → /content-init
- decision → /decision-init
- learning → /learning-init
- research → /research-init
```

### 2. Check if SESSION.md Already Exists

Check if `.aiwork/SESSION.md` exists:

**If exists:**
```
⚠️ SESSION.md already exists

Found existing session overview at .aiwork/SESSION.md

Options:
1. View existing SESSION.md (cancel this command)
2. Update existing SESSION.md (create /analysis-update command for this)
3. Recreate from scratch (⚠️  will overwrite)

Choose option: (1/2/3)
```

Only proceed with recreation if user explicitly chooses option 3.

### 3. Interactive Session Overview Creation

Guide the user through 7 questions to build a comprehensive analysis session overview.

**Tone:** Conversational and helpful. Provide examples for each question.

**IMPORTANT:** Use the language specified in session.yaml for ALL questions, examples, and generated content.

---

#### Question 1: Analysis Topic

**If language is English (en):**

```
Let's create your Analysis Session Overview!

This will define the context, objectives, and scope for your data analysis work.
All workflows you create will reference this overview.

---

Q1: What is this analysis session about? (1-2 sentences)

Describe the main focus and purpose of your analysis.

Example: "Analyzing user retention patterns across different acquisition channels
to identify which channels produce the most engaged users and optimize Q4 marketing
budget allocation."

→ {user input}
```

**If language is Chinese (zh):**

```
让我们创建你的分析会话概览！

这将定义你的数据分析工作的背景、目标和范围。
你创建的所有工作流都将参考这个概览。

---

问题1: 这次分析会话是关于什么的？（1-2句话）

描述你分析的主要焦点和目的。

示例: "分析不同获客渠道的用户留存模式，识别哪些渠道产生最活跃的用户，
并优化第四季度的营销预算分配。"

→ {用户输入}
```

---

#### Question 2: Business Context

```
Q2: What is the business context or problem you're trying to solve?

Explain why this analysis is needed and what business decision it will inform.

Example: "The company has seen declining retention rates in recent cohorts (Q3 2024
dropped 15% compared to Q1). The marketing team has $500K Q4 budget to allocate
across paid search, paid social, organic, and referral channels, but doesn't know
which channels produce the most valuable long-term users. This analysis will directly
inform the budget allocation decision."

→ {user input}
```

---

#### Question 3: Stakeholders

```
Q3: Who are the key stakeholders? Who will use these insights?

List the people/teams who need this analysis and what they need from it.

Example:
- Sarah Chen (Product Manager) - Needs retention insights to inform product roadmap
  and prioritize features that drive engagement
- Marcus Lee (Marketing Lead) - Needs channel comparison to make Q4 budget allocation
  decision ($500K at stake)
- Executive team (CEO, CFO) - Needs high-level strategic recommendations with
  expected ROI impact

→ {user input}
```

---

#### Question 4: Objectives

```
Q4: What are the main objectives of this analysis? (List 3-5 key goals)

These should be specific, measurable goals that define success for this analysis.

Example:
1. Calculate 7-day, 30-day, and 90-day retention rates by weekly cohort
2. Compare retention across acquisition channels (organic, paid social, paid search, referral)
3. Identify user behaviors and characteristics that correlate with higher retention
4. Quantify the value difference between channels (LTV, engagement metrics)
5. Provide data-driven recommendations for Q4 budget allocation with expected impact

→ {user input}
```

---

#### Question 5: Data Sources

```
Q5: What data sources will you be using?

List all datasets with: name, description, format, approximate size, location (if known)

Example:
- users.csv - User registration data with signup date, channel, location (500K rows, data/users.csv)
- events.csv - User activity events with event_type and timestamp (2M rows, data/events.csv)
- subscriptions.csv - Subscription history and payments (300K rows, data/subscriptions.csv)
- Optional: marketing_spend.csv - Channel spend data (if available)

→ {user input}
```

---

#### Question 6: Expected Deliverables

```
Q6: What are the expected deliverables from this analysis?

List all outputs you plan to produce (datasets, notebooks, visualizations, reports, etc.)

Example:
- Clean datasets (users_clean.csv, events_clean.csv) for future analysis
- Jupyter notebooks documenting full analysis pipeline (reproducible)
- Retention metrics CSV with cohort × channel breakdown
- Visualizations:
  * Retention curves by cohort over time
  * Retention comparison by channel
  * User behavior correlation heatmap
  * LTV by channel chart
- Final report (Markdown) with:
  * Executive summary
  * Key findings with statistical significance
  * Actionable recommendations with expected impact
  * Methodology documentation

→ {user input}
```

---

#### Question 7: Timeline

```
Q7: Any timeline constraints or deadlines?

Mention any hard deadlines, target dates, or time estimates.

Example: "Need to complete by November 5, 2025 for Q4 planning meeting on November 8.
Estimated 10-15 hours of analysis work over 2 weeks."

Or: "No hard deadline, but aiming to complete within 2 weeks. Estimated 12 hours total."

Or: "Flexible timeline, will work on this iteratively."

→ {user input}
```

---

### 4. Generate SESSION.md

Create `.aiwork/SESSION.md` using all the answers:

```markdown
# Session: {session-name converted to title case}

**Session ID**: {session-id from session.yaml}
**Type**: Data Analysis
**Created**: {timestamp}
**Status**: Active

---

## Session Overview

{Answer from Q1}

**Business Context:**
{Answer from Q2}

**Key Stakeholders:**
{Parse Q3 answer - convert to formatted list}
- {Stakeholder 1} - {their needs}
- {Stakeholder 2} - {their needs}

---

## Objectives

{Parse Q4 answer - convert to checklist with emoji status indicators}
1. ⚪ {Objective 1}
2. ⚪ {Objective 2}
3. ⚪ {Objective 3}
4. ⚪ {Objective 4}
5. ⚪ {Objective 5}

**Note**: ⚪ = Pending, 🔄 = In Progress, ✅ = Completed

---

## Data Sources

### Primary Datasets

{Parse Q5 answer - convert to table format}

| Data Source | Description | Format | Size | Location |
|-------------|-------------|--------|------|----------|
| {source-1} | {description} | {CSV/SQL/JSON} | {size} | {path or "TBD"} |
| {source-2} | {description} | {format} | {size} | {path or "TBD"} |

### Data Quality Notes

{Leave section for notes to be added later}

*Add notes about data quality, missing values, or known issues as you discover them.*

---

## Expected Deliverables

{Parse Q6 answer - convert to checklist}

### Analysis Outputs
- [ ] {Deliverable 1}
- [ ] {Deliverable 2}
- [ ] {Deliverable 3}

### Visualizations
- [ ] {Visualization 1}
- [ ] {Visualization 2}

### Documentation
- [ ] {Documentation 1}
- [ ] {Documentation 2}

---

## Timeline

{Parse Q7 answer}

**Deadline**: {deadline or "Flexible"}
**Estimated Duration**: {estimate or "TBD"}
**Target Completion**: {target date or "TBD"}

---

## Workflows

*Workflows will be added as you create them with `/workflow-new`*

| ID | Name | Status | Steps | Completed | Duration |
|----|------|--------|-------|-----------|----------|
| - | - | - | - | - | - |

---

## Progress Summary

**Session Status**: 🟢 Active

**Progress:**
- Workflows created: 0
- Workflows completed: 0
- Total steps: 0
- Completed steps: 0
- Completion: 0%

**Time Tracking:**
- Estimated total: {from Q7 or "TBD"}
- Actual time spent: 0h
- Remaining: {estimate or "TBD"}

---

## Key Findings

*This section will be populated as you complete workflows and generate insights*

### Preliminary Findings

{Empty - to be filled during analysis}

### Final Insights

{Empty - to be filled at completion}

---

## Recommendations

*This section will be populated with actionable recommendations based on analysis findings*

{Empty - to be filled during/after analysis}

---

## Notes

*Session-level notes, observations, and context*

{Empty initially - add notes as you work}

---

## Appendix

### Methodology

*Document analysis methods, statistical tests, assumptions*

### References

*Links to related documents, papers, previous analyses*

### Change Log

| Date | Change | Updated By |
|------|--------|------------|
| {timestamp} | Session overview created | {ai-tool} |

---

**Session Created**: {timestamp}
**Last Updated**: {timestamp}
```

### 5. Update Session Tracking

Update `.aiwork/session.yaml`:

```yaml
session_id: "{session-id}"
type: "data-analysis"
# ... existing fields ...
session_overview_created: "{timestamp}"
session_overview_version: "1.0"
```

### 6. Output Summary

```
✅ Analysis Session Overview Created!

Location: .aiwork/SESSION.md
Type: Data Analysis
Created: {timestamp}

📋 Session Overview Contents:
- Analysis topic: {brief summary from Q1}
- Business context and stakeholders documented
- {N} objectives defined
- {N} data sources identified
- {N} expected deliverables listed
- Timeline: {deadline or "Flexible"}

📊 Your Objectives:
{List objectives from Q4}

⏰ Timeline:
{Timeline from Q7}

📋 Next Steps:

1. **Review your session overview**:
   → Open .aiwork/SESSION.md
   → Make any edits if needed

2. **Create your first analysis workflow**:
   → /workflow-new <analysis-name> --template data-analysis
   → Recommended: Use template for pre-configured 6-step analysis pipeline

3. **Start executing**:
   → /workflow-plan (generates detailed steps)
   → /step-prepare 1 (prepares first step with context)

💡 Tips:
- All workflows you create will reference this SESSION.md
- Update objectives status (⚪ → 🔄 → ✅) as you progress
- Add findings and notes to SESSION.md as you discover insights
- SESSION.md is a living document - keep it updated!

Example workflow creation:
→ /workflow-new retention-analysis --template data-analysis
```

---

## Important Notes

- **Run once per session** - Creates the session overview
- **SESSION.md is like PRD for data analysis** - Provides overall context
- **All workflows reference SESSION.md** - Maintains consistency
- **Update SESSION.md as you work** - Living document with findings
- **SESSION.md != workflow spec** - SESSION is session-level, spec is workflow-level

---

## Error Handling

### If no session found:
```
❌ No session found

Initialize a data analysis session first:
→ /session-init data-analysis <name>

Then run: /analysis-init
```

### If wrong session type:
```
❌ Wrong session type

Your session type: {type}

This command is for data-analysis sessions only.

For {type} sessions, use:
- software → /project-init
- content → /content-init
- decision → /decision-init
- learning → /learning-init
- research → /research-init
```

### If SESSION.md already exists:
```
⚠️ SESSION.md already exists

Options:
1. View existing (cancel)
2. Update (use /analysis-update when available)
3. Recreate (will overwrite)

Choose: (1/2/3)
```

---

## Example Session Creation Flow

```
User: /session-init data-analysis customer-retention

✅ Session Initialized
Session ID: customer-retention
Type: data-analysis

📋 Next Steps:
→ Run /analysis-init to create your session overview

---

User: /analysis-init

Let's create your Analysis Session Overview!

Q1: What is this analysis session about?
→ User: Analyzing user retention to optimize marketing spend

Q2: What is the business context?
→ User: Q3 retention dropped 15%, need to allocate $500K Q4 budget

Q3: Who are the key stakeholders?
→ User: Product Manager, Marketing Lead, Executives

Q4: What are the main objectives?
→ User:
1. Calculate retention by cohort
2. Compare channels
3. Identify retention drivers
4. Provide budget recommendations

Q5: What data sources?
→ User: users.csv (500K), events.csv (2M)

Q6: Expected deliverables?
→ User: Notebooks, visualizations, final report

Q7: Timeline?
→ User: Complete by Nov 5

✅ Analysis Session Overview Created!

Next: /workflow-new retention-study --template data-analysis
```

---

**Remember**: This command creates the SESSION-LEVEL overview. Each workflow will have its own spec.md with workflow-specific details.
