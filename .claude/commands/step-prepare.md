# Prepare Step Context Package

You are the context package generator for the AI Collaboration Framework. When the user runs this command, generate a comprehensive, self-contained context package for the specified step.

## Command Usage

```
/step-prepare <step-id> [workflow-id]
```

**Parameters:**
- `step-id` - Step number (1, 2, 3, etc.)
- `workflow-id` - Optional: Specific workflow if multiple active

**Examples:**
```
/step-prepare 1                    # Auto-detect workflow, step 1
/step-prepare 3                    # Auto-detect workflow, step 3
/step-prepare 2 001                # Explicit workflow 001, step 2
/step-prepare 1 001-user-retention # Full workflow name, step 1
```

---

## Your Tasks

### 1. Identify Target Workflow and Step

**Workflow resolution:**
- If workflow-id provided: Use that
- If not: Auto-detect (same as /workflow-plan)
- Error if ambiguous or not found

**Step validation:**
- Check step exists in steps.yaml
- Error if step-id not found

### 2. Check Step Status

Read `.aiwork/workflows/{id}/steps.yaml`:

**If step status is "completed":**
```
⚠️ Step already completed

Step {step-id} was completed on {date} by {ai-tool}.

Options:
1. View existing work (check timeline.md)
2. Prepare context anyway (for revision)
3. Cancel

Choose option: (1/2/3)
```

**If step status is "blocked":**
```
⚠️ Step is blocked

Step {step-id} is marked as blocked.
Reason: {notes from steps.yaml}

Resolve blocker first or proceed anyway? (resolve/proceed/cancel)
```

### 3. Check Dependencies

Read `depends_on` field in steps.yaml for this step.

**If step has dependencies:**

```
📋 Step Dependencies

Step {step-id} depends on:
{for each dep:}
- Step {dep-id}: {title} - {status}

{if any dep not completed:}
⚠️ Warning: Some dependencies not completed

Incomplete dependencies:
- Step {dep-id}: {title} ({status})

Recommendations:
1. Complete dependencies first
2. Proceed anyway if dependencies are not critical

Continue? (yes/no)
```

If user says no, stop here.

### 4. Gather Complete Context

Collect all information needed for the context package:

1. **Session context**:
   - Read `.aiwork/session.yaml`
   - Read `.aiwork/SESSION.md` or `.aiwork/PRD.md` (if exists)

2. **Workflow context**:
   - Read spec.md
   - Read plan.md
   - Read steps.yaml (all steps)

3. **Previous steps context**:
   - For each completed step (id < current step-id):
     - Read from timeline.md what was accomplished
     - Note key outputs and findings
   - Summarize relevant context

4. **Current step details**:
   - From steps.yaml: title, description, files, tags, notes
   - Estimated time
   - Dependencies

5. **Code/data context** (if applicable):
   - For software: Read relevant existing code files
   - For data analysis: Include data schemas, sample data

### 5. Generate Context Package

Create `.aiwork/workflows/{id}/context/step-{step-id}.md` with comprehensive content:

---

```markdown
# Context Package: Step {step-id} - {step-title}

> Complete context for executing this step
> Generated: {timestamp}

**Workflow**: {workflow-id} - {workflow-name}
**Session**: {session-name}
**Step**: {step-id} of {total-steps}
**Estimated Time**: {hours} hours
**Priority**: {priority}

---

## 🎯 Current Step Goal

{Clear, concise statement of what this step accomplishes}

**Deliverables:**
{from steps.yaml files list:}
- `{file-1}` - {description}
- `{file-2}` - {description}

**Success Criteria:**
- {Criterion 1}
- {Criterion 2}
- {Criterion 3}

---

## 📋 Session Context

**Session Type**: {type}
**Session ID**: {session-id}

{If SESSION.md or PRD.md exists:}
### Project Overview

{Brief summary of session objectives}

{For software with PRD:}
**Related PRD Module**: {module-name}
**Tech Stack**: {stack}
**Key Constraints**:
- {constraint-1}
- {constraint-2}

{For data analysis:}
**Analysis Questions**:
- {question-1}
- {question-2}

---

## 🗂️ Workflow Context

**Workflow**: {workflow-name}
**Objective**: {from spec}

**This workflow aims to**: {brief description from spec}

---

## ✅ Previous Steps Summary

{For each completed step before this one:}

### Step {prev-id}: {prev-title} ✅

**Completed**: {date} by {ai-tool}
**Key Outputs**:
- {output-1}
- {output-2}

**Key Findings/Decisions**:
{from timeline.md:}
- {finding-1}
- {finding-2}

{If relevant files were created:}
**Created Files**:
- `{file-path}` - {description}

---

{Repeat for all previous completed steps}

{If no previous steps:}
*This is the first step in the workflow.*

---

## 📊 Available Resources

### Data/Code Available

{For data analysis:}
**Datasets**:
| Dataset | Location | Rows | Columns | Description |
|---------|----------|------|---------|-------------|
| {name} | {path} | {count} | {count} | {desc} |

**Data Schema**:
```
{column}: {type} - {description}
...
```

**Sample Data** (first 3 rows):
```
{sample data if available}
```

{For software:}
**Existing Code Context**:

File: `{relevant-file-1}`
```{language}
{relevant code snippet}
```

File: `{relevant-file-2}`
```{language}
{relevant code snippet}
```

### Dependencies/Libraries

{List relevant libraries, tools, or dependencies}

---

## 🛠️ Implementation Guide

### Approach

{From plan.md and steps.yaml description, provide detailed guidance}

**Step-by-step implementation:**

1. **{Sub-task 1}**
   - {Detailed instruction}
   - {What to check}
   - Expected output: {description}

2. **{Sub-task 2}**
   - {Instruction}
   - {What to check}
   - Expected output: {description}

3. **{Sub-task 3}**
   - {Instruction}
   - Expected output: {description}

{For data analysis:}
### Suggested Code Structure

```python
# 1. {Sub-task 1}
import pandas as pd
# {guidance}

# 2. {Sub-task 2}
# {guidance}

# 3. {Sub-task 3}
# {guidance}
```

{For software:}
### Code Structure

**Files to create/modify**:

1. `{file-path-1}`
   - Purpose: {purpose}
   - Key functions/classes: {list}

2. `{file-path-2}`
   - Purpose: {purpose}

### Example Code Skeleton

```{language}
{provide skeleton code to guide implementation}
```

---

## ✅ Testing & Verification

### How to Verify This Step

{Detailed testing instructions}

**Checks to perform:**
- [ ] {Check 1}
- [ ] {Check 2}
- [ ] {Check 3}

{For data analysis:}
**Data Quality Checks:**
- [ ] Output row count: {expected or range}
- [ ] No missing values in key columns: {columns}
- [ ] Data types correct: {types}
- [ ] {Domain-specific check}

{For software:}
**Tests to write:**
```{language}
# Test: {test-name}
def test_{function}():
    # {test-description}
    {test-skeleton}
```

**Manual testing:**
1. {Manual test step 1}
2. {Manual test step 2}

---

## 📦 Expected Outputs

### Files to Create/Modify

{From steps.yaml files list:}

| File | Type | Description | Location |
|------|------|-------------|----------|
| `{file-1}` | {type} | {description} | {full-path} |
| `{file-2}` | {type} | {description} | {full-path} |

{For data analysis:}
### Output Data Schema

If this step produces data, expected schema:
```
{column}: {type} - {description}
...
```

---

## ⚠️ Important Notes

{From steps.yaml notes field and plan.md}

**Key Considerations:**
- {Note 1}
- {Note 2}

**Common Pitfalls:**
- {Pitfall 1 and how to avoid}
- {Pitfall 2 and how to avoid}

**Constraints:**
{From PRD or spec:}
- {Constraint 1}
- {Constraint 2}

---

## 🔗 References

### Related Documentation

{If relevant:}
- Session overview: `.aiwork/SESSION.md`
- Workflow spec: `.aiwork/workflows/{id}/spec.md`
- Technical plan: `.aiwork/workflows/{id}/plan.md`
{For software with PRD:}
- Project PRD: `.aiwork/PRD.md`

### External Resources

{Any links from spec or plan}
- {Resource 1}
- {Resource 2}

---

## 📝 Completion Checklist

Before marking this step complete:

- [ ] All deliverable files created/modified
- [ ] All verification checks pass
- [ ] Output files saved in correct locations
- [ ] {For software:} Tests written and passing
- [ ] {For data:} Data quality validated
- [ ] Documentation updated (if applicable)
- [ ] Ready to run `/step-complete {step-id} --ai <tool> [workflow-id]`

---

## 🚀 Next Steps After Completion

After completing this step:

1. Run: `/step-complete {step-id} --ai <tool> [workflow-id]`
   (Replace `<tool>` with: claude, chatgpt, cursor, copilot, etc.)

   **If you have only one active workflow:**
   ```
   /step-complete {step-id} --ai claude
   ```

   **If you have multiple active workflows:**
   ```
   /step-complete {step-id} --ai claude {workflow-id}
   ```

2. The following steps will become available:
{List steps that depend on this one:}
   - Step {next-id}: {title}

---

**Context Package Generated**: {timestamp}

**How to Use This Package:**
1. Copy this entire document
2. Paste into your preferred AI tool (Claude, ChatGPT, Cursor, etc.)
3. The AI will have complete context to execute this step
4. After completion, return here and run `/step-complete {step-id} --ai <tool> [workflow-id]`

**All context is preserved in documents. You can resume anytime.**

```

---

### 6. Update Step Status

Update `.aiwork/workflows/{id}/steps.yaml`:

```yaml
steps:
  - id: {step-id}
    ...
    status: in_progress  # Changed from pending
    started_at: "{timestamp}"
    ...
```

### 7. Update Timeline

Append to `.aiwork/workflows/{id}/timeline.md`:

```markdown
### {date} - Step {step-id} Started

- Step: {step-title}
- Context package generated
- Status: In Progress
```

### 8. Output Summary

```yaml
✅ Context Package Ready

Step: {step-id} - {step-title}
Workflow: {workflow-id} - {workflow-name}
Priority: {priority}
Estimated Time: {hours} hours

📄 Context Package Location:
.aiwork/workflows/{workflow-id}/context/step-{step-id}.md

📋 Package Contents:
- Current step goal and deliverables
- Complete session and workflow context
- Summary of previous {N} completed steps
- Available data/code resources
- Detailed implementation guide
- Testing and verification steps
- Expected outputs specification

{If dependencies:}
📌 Dependencies:
{for each dep:}
- Step {dep-id}: {title} ({status})
{if any incomplete:}
⚠️  Note: Some dependencies incomplete (proceed with caution)

🎯 Next Actions:

1. **Open the context package**:
   → cat .aiwork/workflows/{workflow-id}/context/step-{step-id}.md
   → Or open in your editor

2. **Copy to your preferred AI tool**:
   → Claude Code (you're here!)
   → ChatGPT (great for Python/data work)
   → Cursor (great for multi-file editing)
   → Or any other AI assistant

3. **Execute the step**:
   → Follow the implementation guide
   → Create/modify the specified files
   → Run tests and verify outputs

4. **Mark complete when done**:
   → /step-complete {step-id} --ai <tool-name>
   → This updates tracking and generates next step

💡 Tips:
- The context package is self-contained
- All necessary information is included
- You can switch AI tools mid-workflow
- Previous work is summarized, not lost
- Resume anytime by reading the context package

{If this is step 1:}
🎉 This is the first step! Set the foundation well.

{If final step:}
🏁 This is the final step! Complete the workflow.
```

---

## Important Notes

- **Context packages must be self-contained** - Include everything needed
- **Be comprehensive** - AI tool should not need to ask for more context
- **Include examples** - Code skeletons, sample data, expected outputs
- **Reference previous work** - Summarize completed steps concisely
- **Provide guidance** - Implementation guide should be actionable
- **Check dependencies** - Warn if dependencies incomplete

---

## Error Handling

### If workflow not found:
```
❌ No workflow found
→ Run `/workflow-new` first
```

### If step not found:
```
❌ Step {step-id} not found in workflow {workflow-id}

Available steps: 1 to {total-steps}
Check: .aiwork/workflows/{workflow-id}/steps.md
```

### If steps.yaml not generated:
```
❌ No step plan found

The workflow hasn't been planned yet.
→ Run `/workflow-plan` first to generate steps
```

---

## Examples

See complete context packages in:
- `examples/data-analysis-complete/workflows/001-retention/context/step-1.md`
- `examples/software-feature-complete/workflows/001-auth/context/step-3.md`

---

**Remember**: The context package is the key to multi-AI collaboration. Make it comprehensive and self-contained!
