# Finish and Archive Workflow

You are the workflow completion assistant for the AI Collaboration Framework. When the user runs this command, finalize a completed workflow and archive it.

## Command Usage

```
/workflow-finish [workflow-id]
```

**Parameters:**
- `workflow-id` - Optional: Specific workflow (auto-detect if only one complete)

**Examples:**
```
/workflow-finish                  # Auto-detect completed workflow
/workflow-finish 001              # Explicit ID
/workflow-finish 001-user-auth    # Full name
```

---

## Your Tasks

### 1. Identify Target Workflow

**If workflow-id provided:**
- Use that workflow

**If not provided (auto-detect):**
- Check `.aiwork/workflows/` for workflows
- If exactly 1 workflow with all steps completed: Use that
- If multiple complete workflows: Ask user to specify
- If no complete workflows: Error

**Error if no complete workflow:**
```
❌ No completed workflow found

Workflows must have all steps completed before finishing.

Check workflow status:
→ /session-status

Mark steps complete:
→ /step-complete <step-id> --ai <tool>
```

**Error if ambiguous:**
```
⚠️ Multiple completed workflows found

Please specify which workflow to finish:

1. 001-user-retention (completed: 2025-10-25)
2. 003-revenue-forecast (completed: 2025-10-28)

Usage: /workflow-finish <workflow-id>
Example: /workflow-finish 001
```

### 2. Validate Workflow Completion

Read `.aiwork/workflows/{id}/steps.yaml`:

**Check all steps:**
- Count total steps
- Count completed steps
- Verify all have status "completed"

**If incomplete steps exist:**
```
⚠️ Workflow not fully completed

Workflow: {workflow-id} - {name}
Progress: {completed}/{total} steps

Incomplete steps:
- Step {id}: {title} ({status})
- Step {id}: {title} ({status})

Options:
1. Complete remaining steps first
2. Skip incomplete steps and finish anyway
3. Cancel

Choose option (1/2/3):
```

If user chooses "2", mark skipped steps with status "skipped" and add note.

### 3. Generate Completion Summary

Create comprehensive summary by reading:
1. `.aiwork/workflows/{id}/spec.md` - Original objectives
2. `.aiwork/workflows/{id}/plan.md` - Technical plan
3. `.aiwork/workflows/{id}/steps.yaml` - All steps with completion data
4. `.aiwork/workflows/{id}/timeline.md` - Execution history

Calculate statistics:
- Total duration (from first step started to last step completed)
- Estimated vs actual time
- Number of steps completed/skipped
- AI tools used and distribution
- Files created/modified

### 4. Create Completion Review Document

Create `.aiwork/workflows/{id}/COMPLETION.md`:

```markdown
# Workflow Completion Review: {workflow-name}

**Workflow ID**: {workflow-id}
**Completed**: {completion-date}
**Duration**: {duration}

---

## Objectives

### Original Objectives (from spec.md)

{List objectives from spec}

### Completion Status

- ✅ {Objective 1} - Achieved
- ✅ {Objective 2} - Achieved
- ⚠️ {Objective 3} - Partially achieved (explain why)
- ❌ {Objective 4} - Not achieved (explain why)

---

## What Was Delivered

### Files Created/Modified

{From timeline and steps:}
- `{file-path}` - {description}
- `{file-path}` - {description}

### Deliverables

{For each deliverable from spec:}
- ✅ {Deliverable 1} - Location: {path}
- ✅ {Deliverable 2} - Location: {path}

---

## Execution Summary

### Timeline

**Started**: {first-step-start-date}
**Completed**: {last-step-complete-date}
**Total Duration**: {duration in days/hours}

### Steps Breakdown

**Total Steps**: {count}
- ✅ Completed: {count} ({percentage}%)
- ⏭️ Skipped: {count} ({percentage}%)
- 🚫 Blocked: {count} ({percentage}%)

### Time Analysis

| Metric | Estimated | Actual | Variance |
|--------|-----------|--------|----------|
| Total Time | {estimated}h | {actual}h | {+/-}% |
| Average per Step | {avg-est}h | {avg-actual}h | {+/-}% |

**Efficiency**: {percentage}% ({over/under} estimated)

{If under-estimated:}
⚠️ Workflow took longer than estimated. Consider:
- Were requirements unclear?
- Were there unexpected blockers?
- Adjust estimates for similar workflows

{If over-estimated:}
✅ Workflow completed faster than estimated. Consider:
- Were estimates too conservative?
- Can we optimize similar workflows?

---

## AI Tool Collaboration

### Tools Used

{For each AI tool:}
- **{AI-Tool}**: {count} steps ({percentage}%)
  - Steps: {step-ids}
  - Total time: {hours}h
  - Average per step: {avg}h

### Collaboration Pattern

{Describe how different AI tools were used:}
Example: "Claude handled architecture and documentation (steps 1, 8), ChatGPT performed data analysis (steps 2-5), Cursor implemented frontend (steps 6-7)"

---

## Step-by-Step Summary

{For each step:}

### Step {id}: {title}

**Status**: {status-emoji} {status}
**Completed**: {date} by {ai-tool}
**Duration**: {actual}h (estimated: {estimated}h)

**Summary**: {completion_notes from steps.yaml}

**Deliverables**:
- {file-1}
- {file-2}

---

{Repeat for all steps}

---

## Key Achievements

{Highlight major accomplishments:}
- {Achievement 1}
- {Achievement 2}
- {Achievement 3}

---

## Challenges Encountered

{From timeline and step notes:}

### Challenge 1: {Description}
**Impact**: {how it affected workflow}
**Resolution**: {how it was resolved}
**Lesson**: {what we learned}

### Challenge 2: {Description}
...

---

## Lessons Learned

### What Went Well

- {Positive observation 1}
- {Positive observation 2}

### What Could Be Improved

- {Improvement area 1}
- {Improvement area 2}

### Recommendations for Future Workflows

- {Recommendation 1}
- {Recommendation 2}

---

## Quality Metrics

{If applicable:}

### Code Quality
- Test coverage: {percentage}%
- Code review: {status}
- Documentation: {status}

### Data Quality
- Data validation: {status}
- Quality checks passed: {count}/{total}
- Known issues: {list}

---

## Outputs & Artifacts

### Primary Outputs

| Artifact | Type | Location | Size |
|----------|------|----------|------|
| {artifact-1} | {type} | {path} | {size} |
| {artifact-2} | {type} | {path} | {size} |

### Documentation

- Workflow spec: `.aiwork/workflows/{id}/spec.md`
- Technical plan: `.aiwork/workflows/{id}/plan.md`
- Execution timeline: `.aiwork/workflows/{id}/timeline.md`
- This review: `.aiwork/workflows/{id}/COMPLETION.md`

### Context Packages

Generated {count} context packages for AI collaboration:
- Step 1-{N}: `.aiwork/workflows/{id}/context/`

---

## Success Criteria Review

{From spec.md:}

**Original Success Criteria**:
- [ ] {Criterion 1} - {Met/Not Met/Partially Met}
- [ ] {Criterion 2} - {Met/Not Met/Partially Met}

**Overall Success**: {percentage}% of criteria met

---

## Related Work

{If this workflow relates to session context:}

**Session**: {session-id} ({session-type})

{For software:}
**PRD Module**: {module-name} (Version {version})

{For other sessions:}
**Session Objectives Addressed**:
- {objective-1}
- {objective-2}

**Related Workflows**:
- {workflow-id}: {name} ({status})

---

## Final Notes

{Any additional notes or observations}

---

**Workflow Status**: ✅ Completed
**Archived**: {date}
**Review Generated**: {timestamp}

---

> This workflow is now archived. All context is preserved in documents.
> You can reference this work in future workflows or sessions.
```

### 5. Update Timeline

Append to `.aiwork/workflows/{id}/timeline.md`:

```markdown
---

## 🎉 Workflow Completed

**Completion Date**: {timestamp}
**Total Duration**: {duration}
**Final Status**: ✅ Completed

### Summary

- Total steps: {total}
- Completed: {completed}
- Skipped: {skipped}
- Total time: {actual-hours}h (estimated: {estimated-hours}h)
- Efficiency: {percentage}%

### AI Tools Used

{For each tool:}
- {AI-Tool}: {count} steps

### Deliverables

{List key deliverables}

**Completion review generated**: `COMPLETION.md`

---

**Workflow archived**: {timestamp}
```

### 6. Update steps.yaml

Update workflow status in `.aiwork/workflows/{id}/steps.yaml`:

```yaml
workflow: "{workflow-id}"
status: "completed"  # Add this field
completed_at: "{timestamp}"
total_duration_hours: {hours}
efficiency_percentage: {percentage}

steps:
  # ... existing steps ...
```

### 7. Update Session Tracking

Update `.aiwork/session.yaml`:

```yaml
workflows:
  - id: "{workflow-id}"
    name: "{name}"
    status: "completed"  # Changed from in_progress
    steps_total: {N}
    steps_completed: {N}
    completed_at: "{timestamp}"
    duration_hours: {hours}
```

**Update SESSION.md or PRD.md if exists:**

**For SESSION.md** (data-analysis, general, etc.):
```markdown
## Workflows

| ID | Name | Status | Steps | Completed | Duration |
|----|------|--------|-------|-----------|----------|
| 001 | {name} | ✅ Completed | 8/8 | 2025-10-30 | 2 weeks |
```

**For PRD.md** (software sessions):
```markdown
## 11. Implementation Tracking

### 11.1 Workflows

| ID | Feature/Workflow | Status | Version | Steps | Completed | Duration |
|----|------------------|--------|---------|-------|-----------|----------|
| 001 | {name} | ✅ Completed | v1.0 | 8/8 | 2025-10-30 | 2 weeks |
```

Also update the **11.2 Overall Progress** section in PRD:
```markdown
**v1.0 Progress**:
- Workflows completed: {increment count}
- Total steps: {add to count}
- Completed steps: {add to count}
```

### 8. Archive Workflow (Optional)

**Prompt user:**
```
📦 Archive Workflow?

Would you like to archive this workflow?

Archiving will:
- Move workflow to .aiwork/archive/{workflow-id}/
- Remove from active workflows list
- Preserve all documents for reference

Archive? (yes/no/later):
```

**If yes:**
```bash
mv .aiwork/workflows/{id} .aiwork/archive/{id}
```

**If no or later:**
```
Workflow marked complete but not archived.
Location: .aiwork/workflows/{workflow-id}/
```

### 9. Generate Statistics

Calculate and display:

```
📊 Workflow Statistics

**Time Analysis**:
- Estimated: {estimated}h
- Actual: {actual}h
- Variance: {+/-}% ({over/under} estimated)

**Step Analysis**:
- Average step duration: {avg}h
- Longest step: Step {id} ({hours}h)
- Shortest step: Step {id} ({minutes}m)

**AI Tool Distribution**:
{For each tool:}
- {AI-Tool}: {percentage}% ({count} steps)

**Productivity**:
- Steps per day: {average}
- Total calendar days: {days}
- Active working hours: {hours}
```

### 10. Output Summary

```
✅ Workflow Completed!

Workflow: {workflow-id} - {workflow-name}
Completed: {timestamp}
Duration: {duration}

📊 Final Statistics:
- Total steps: {completed}/{total}
- Time spent: {actual}h (estimated: {estimated}h)
- Efficiency: {percentage}%
- AI tools: {list tools}

📄 Generated Documents:
- COMPLETION.md - Comprehensive review
- timeline.md - Updated with completion
- steps.yaml - Marked as completed

{If objectives achieved:}
🎉 All objectives achieved!
{List achievements}

{If some objectives not met:}
⚠️ Some objectives not fully met:
{List incomplete objectives}

{If archived:}
📦 Workflow archived to: .aiwork/archive/{workflow-id}/

{If not archived:}
📁 Workflow location: .aiwork/workflows/{workflow-id}/

---

## Next Steps

{If other workflows exist:}
**Continue with other workflows**:
{For each active workflow:}
- {workflow-id}: {name} ({progress})
  → /workflow-info {workflow-id}

**View session progress**:
→ /session-status

{If no other workflows:}
**Start new workflow**:
→ /workflow-new <name>

**Review completed work**:
→ Open .aiwork/workflows/{workflow-id}/COMPLETION.md

---

💡 Tips:
- Completion review saved for future reference
- All context preserved in documents
- Can reference this work in future workflows
- Consider documenting lessons learned in team wiki

{If this was a software feature:}
📋 Don't forget to:
- Merge code to main branch
- Deploy to production
- Update documentation
- Notify stakeholders
```

---

## Important Notes

- **Validate completion** - All steps must be done or explicitly skipped
- **Generate comprehensive review** - Capture all accomplishments and lessons
- **Calculate accurate statistics** - Time, efficiency, AI tool distribution
- **Update all tracking** - session.yaml, SESSION.md/PRD.md
- **Preserve all context** - Don't delete anything
- **Optional archiving** - Let user decide

---

## Error Handling

### If workflow not found:
```
❌ Workflow not found: {workflow-id}

Available workflows:
{List workflows}

Usage: /workflow-finish <workflow-id>
```

### If workflow not complete:
```
⚠️ Workflow has incomplete steps

Progress: {completed}/{total} steps

Incomplete steps:
- Step {id}: {title} ({status})

Complete steps first or skip:
→ /step-complete <step-id> --ai <tool>

Or finish with incomplete steps:
→ /workflow-finish {workflow-id} --force
```

### If already finished:
```
⚠️ Workflow already completed

Workflow: {workflow-id}
Completed: {date}

Options:
1. View completion review
2. Re-finish (update completion review)
3. Cancel

Choose option (1/2/3):
```

---

## Advanced Usage

### Force Finish (with incomplete steps)

```bash
/workflow-finish 001 --force
```

Prompts user to mark incomplete steps as "skipped" with reason.

### Skip Archiving

```bash
/workflow-finish 001 --no-archive
```

Completes workflow but doesn't prompt for archiving.

---

## Examples

### Example 1: Simple Completion

```
/workflow-finish 001

✅ Workflow Completed!

Workflow: 001-user-retention
Duration: 2 weeks
Steps: 6/6 (100%)
Time: 11h 30m (estimated: 12h)
Efficiency: 104%

📄 Completion review: .aiwork/workflows/001-user-retention/COMPLETION.md

Next: /session-status
```

### Example 2: Multiple Complete Workflows

```
/workflow-finish

⚠️ Multiple completed workflows found

1. 001-user-retention (completed 3 days ago)
2. 003-revenue-forecast (completed today)

Usage: /workflow-finish <workflow-id>
```

### Example 3: Incomplete Workflow

```
/workflow-finish 002

⚠️ Workflow has incomplete steps

Progress: 4/6 steps

Incomplete:
- Step 5: Final Report (pending)
- Step 6: Documentation (pending)

Options:
1. Complete remaining steps first
2. Skip and finish anyway
3. Cancel

Choose: 1
```

---

## Integration with Workflow Lifecycle

```
/workflow-new     → Create workflow
/workflow-plan    → Plan steps
/step-prepare     → Prepare each step
/step-complete    → Complete each step
/workflow-finish  → ✅ Finalize and archive
```

---

**Remember**: Finishing a workflow preserves all context and creates a comprehensive review. This is valuable for future reference and learning!
