# Workflow Detailed Information

You are the workflow information provider for the AI Collaboration Framework. When the user runs this command, provide comprehensive details about a specific workflow.

## Command Usage

```
/workflow-info <workflow-id>
```

**Parameters:**
- `workflow-id` - Workflow identifier (001, 001-name, or full name)

**Examples:**
```
/workflow-info 001
/workflow-info 001-user-retention
/workflow-info user-retention
```

---

## Your Tasks

### 1. Resolve Workflow ID

**If workflow-id provided:**
- Find matching workflow in `.aiwork/workflows/`
- Support partial matches (001, 001-name, or name)

**If workflow-id not provided:**
```
❌ Missing workflow ID

Usage: /workflow-info <workflow-id>

Available workflows:
{List all workflows with IDs}

Example: /workflow-info 001
```

**If workflow not found:**
```
❌ Workflow not found: {workflow-id}

Available workflows:
{List all workflows from .aiwork/workflows/}
- 001-user-retention
- 002-churn-analysis

Usage: /workflow-info <workflow-id>
```

**If ambiguous (multiple matches):**
```
⚠️ Multiple workflows match "{workflow-id}"

Please be more specific:
1. 001-user-retention
2. 002-user-segmentation

Usage: /workflow-info <full-id>
```

### 2. Read Complete Workflow Context

Read all workflow files:
1. `.aiwork/workflows/{id}/spec.md` - Specification
2. `.aiwork/workflows/{id}/plan.md` - Technical plan (if exists)
3. `.aiwork/workflows/{id}/steps.yaml` - Steps with metadata
4. `.aiwork/workflows/{id}/steps.md` - Human-readable steps (if exists)
5. `.aiwork/workflows/{id}/timeline.md` - Execution history (if exists)
6. `.aiwork/workflows/{id}/context/` - Context packages (if exist)
7. `.aiwork/session.yaml` - Session metadata for this workflow

### 3. Display Comprehensive Information

```
# Workflow Information: {workflow-name}

**Workflow ID**: {workflow-id}
**Session**: {session-id} ({session-type})
**Status**: {status-emoji} {status}
**Created**: {created-date}
**Last Activity**: {last-activity}

---

## Overview

**Objective**: {brief objective from spec}

{If template used:}
**Template**: {template-name}

**Priority**: {priority}
**Type**: {workflow-type}

---

## Progress Summary

**Overall Progress**: {completed}/{total} steps ({percentage}%)

```
Progress: ████████░░░░ {percentage}%
```

**Status Breakdown**:
- ✅ Completed: {count} steps
- 🔄 In Progress: {count} steps
- ⚪ Pending: {count} steps
- 🚫 Blocked: {count} steps
- ⏭️ Skipped: {count} steps

**Time Tracking**:
- Estimated Total: {estimated-hours}h
- Actual Spent: {actual-hours}h
- Remaining: {remaining-hours}h
- Efficiency: {actual/estimated ratio}

---

## Steps Overview

| ID | Title | Status | Priority | Assigned To | Duration | Progress |
|----|-------|--------|----------|-------------|----------|----------|
| 1 | {title} | ✅ | High | claude | 1h 23m / 1.5h | 100% |
| 2 | {title} | 🔄 | High | chatgpt | 0h 45m / 2h | In progress |
| 3 | {title} | ⚪ | Medium | - | - / 2h | Not started |
| 4 | {title} | ⚪ | Medium | - | - / 1.5h | Waiting on: Step 2 |

---

## Detailed Step Information

{For each step:}

### Step {id}: {title}

**Status**: {status-emoji} {status}
**Priority**: {priority-emoji} {priority}
**Estimated Time**: {hours}h
{If started:}
**Assigned To**: {ai-tool}
**Started**: {started-timestamp}
{If completed:}
**Completed**: {completed-timestamp}
**Completed By**: {ai-tool}
**Duration**: {actual-duration} (estimated: {estimated}h)

**Dependencies**: {list of step IDs or "None"}

#### Description
{description from steps.yaml}

#### Files to Create/Modify
{from steps.yaml:}
- `{file-1}`
- `{file-2}`

{If completed:}
#### Completion Summary
{completion_notes from steps.yaml}

**Deliverables Created**:
- `{file-1}` ✓
- `{file-2}` ✓

{If in_progress:}
#### Current Status
- Started: {time-ago}
- Duration so far: {duration}
- Context package: `.aiwork/workflows/{id}/context/step-{step-id}.md`

{If pending and has dependencies:}
#### Blocked By
Waiting on:
- Step {dep-id}: {dep-title} ({dep-status})

{If pending and no dependencies:}
#### Ready to Start
✅ No dependencies - Ready to begin
→ /step-prepare {step-id} {workflow-id}

#### Tags
{tags from steps.yaml}

---

{End of step list}

---

## Execution Timeline

{If timeline.md exists, show recent entries:}

### Recent Activity

{Show last 5-10 timeline entries:}

**{timestamp} - {event}**
{details}

{If many entries:}
---
*Showing recent entries. See complete timeline:*
→ `.aiwork/workflows/{workflow-id}/timeline.md`

{If no timeline:}
*No execution history yet*

---

## Technical Plan

{If plan.md exists:}

### Plan Summary

{Brief summary from plan.md - first paragraph or overview section}

**Key Technical Decisions**:
{Extract key points from plan:}
- {Decision 1}
- {Decision 2}
- {Decision 3}

**View Complete Plan**:
→ `.aiwork/workflows/{workflow-id}/plan.md`

{If no plan:}
*Technical plan not generated yet*
→ Run `/workflow-plan {workflow-id}` to generate

---

## Specification

{Brief summary from spec.md:}

### Requirements
{List key requirements from spec}

### Success Criteria
{List success criteria from spec}

**View Complete Spec**:
→ `.aiwork/workflows/{workflow-id}/spec.md`

---

## Dependencies & Relationships

{If this workflow relates to session context:}

### Session Alignment

{For software with PRD:}
**PRD Module**: {module-name}
**Priority in PRD**: {priority}
**Target Version**: {version}

{For other sessions with SESSION.md:}
**Session Objectives Addressed**:
- {objective-1}
- {objective-2}

### Step Dependencies

**Dependency Chain**:
```
{Generate simple dependency visualization:}
Step 1
  └─> Step 2
       ├─> Step 3
       └─> Step 4
            └─> Step 5
```

**Parallelizable Steps**:
{List steps that can be done in parallel:}
- Steps {step-ids} have no dependencies on each other

---

## Context Packages

{If context/ directory exists:}

**Generated Context Packages**:
{List all context packages:}
- `step-{id}.md` - {step-title} (Step {id})

**Latest Context Package**:
→ `.aiwork/workflows/{workflow-id}/context/step-{latest}.md`

{If no context packages:}
*No context packages generated yet*
→ Run `/step-prepare <step-id> {workflow-id}` to generate

---

## AI Tool Collaboration

{If any steps completed:}

**AI Tool Usage**:
{For each AI tool that worked on this workflow:}
- **{AI-Tool}**: {count} steps
  - Completed: Step {step-ids}
  - Average duration: {avg-time}

**Collaboration Pattern**:
{Describe the pattern:}
Example: "Claude for design and documentation, ChatGPT for data analysis"

{If no steps completed:}
*No steps completed yet*

---

## Statistics

**Workflow Metrics**:
- Total steps: {total}
- Completed: {count} ({percentage}%)
- Average step duration: {avg-duration}
- Estimated completion: {estimated-completion-date based on pace}

**Efficiency**:
- Estimated time: {estimated}h
- Actual time: {actual}h
- Variance: {difference} ({percentage})
{If under-estimated:}
⚠️ Taking longer than estimated
{If over-estimated:}
✅ Progressing faster than estimated

---

## Files & Outputs

**Workflow Directory**: `.aiwork/workflows/{workflow-id}/`

**Structure**:
```
{workflow-id}/
├── spec.md                    {exists: ✓ or ✗}
├── plan.md                    {exists: ✓ or ✗}
├── steps.yaml                 {exists: ✓ or ✗}
├── steps.md                   {exists: ✓ or ✗}
├── timeline.md                {exists: ✓ or ✗}
└── context/
    ├── step-1.md              {exists: ✓ or ✗}
    ├── step-2.md              {exists: ✓ or ✗}
    └── ...
```

{If outputs directory exists:}
**Outputs Directory**: `outputs/{workflow-id}/`
{List output files if available}

---

## Next Actions

{Generate contextual recommendations:}

{If no steps started:}
**Start First Step**:
→ /step-prepare 1 {workflow-id}

{If steps in progress:}
**Continue Current Step**:
- Step {step-id}: {title} (in progress)
- Started: {time-ago}
- Context: `.aiwork/workflows/{workflow-id}/context/step-{step-id}.md`

When complete:
→ /step-complete {step-id} --ai <tool> {workflow-id}

{If steps ready to start:}
**Start Next Available Step**:
{For each ready step:}
- Step {step-id}: {title} ({priority}, ~{hours}h)
  → /step-prepare {step-id} {workflow-id}

{If all complete:}
**Finish Workflow**:
All steps completed! 🎉
→ /workflow-finish {workflow-id}

{If blocked:}
**Resolve Blockers**:
{List blocking issues}

---

## Related Commands

**View Session Status**:
→ /session-status

**Plan Workflow** (if not planned):
→ /workflow-plan {workflow-id}

**Prepare Step**:
→ /step-prepare <step-id> {workflow-id}

**Complete Step**:
→ /step-complete <step-id> --ai <tool> {workflow-id}

**Edit Specification**:
→ Edit `.aiwork/workflows/{workflow-id}/spec.md`

**Edit Steps**:
→ Edit `.aiwork/workflows/{workflow-id}/steps.yaml`

---

## Tips

💡 **Detailed Documentation**: All workflow state is in markdown/YAML files - completely transparent and editable

💡 **Context Switching**: You can pause this workflow anytime and work on another. All context is preserved.

💡 **AI Tool Flexibility**: Each step can be executed by a different AI tool using context packages.

💡 **Progress Tracking**: Timeline tracks every action for complete audit trail.

---

**Report Generated**: {timestamp}
**Workflow Location**: `.aiwork/workflows/{workflow-id}/`
```

---

## Display Rules

### Status Formatting

**Status Emojis**:
- 📋 Planned - Not started
- 🔄 In Progress - Has in_progress steps
- ⏸️ Paused - Explicitly paused
- ✅ Completed - All steps done
- 🚫 Blocked - Cannot proceed

**Priority Emojis**:
- 🔴 High priority
- 🟡 Medium priority
- 🟢 Low priority

**Step Status**:
- ✅ Completed
- 🔄 In Progress
- ⚪ Pending
- 🚫 Blocked
- ⏭️ Skipped

### Time Formatting

**Relative Times**:
- "2 minutes ago"
- "1 hour ago"
- "3 days ago"
- "Just now"

**Duration Formatting**:
- "1h 23m"
- "45m"
- "2h 15m"

### Progress Bars

Use 12-character bars:
```
0-10%:   ░░░░░░░░░░░░
25%:     ███░░░░░░░░░
50%:     ████████░░░░
75%:     ███████████░
100%:    ████████████
```

---

## Important Notes

- **Read all files** - Gather complete information
- **Calculate accurate statistics** - Don't estimate
- **Show relative timestamps** - More user-friendly
- **Provide actionable next steps** - What can user do now
- **Handle missing files gracefully** - Some files may not exist yet
- **Show file exists indicators** - ✓ or ✗ for file structure
- **Format duration nicely** - Human-readable format

---

## Error Handling

### If spec.md missing:

```
⚠️ Workflow specification not found

This workflow appears incomplete.

Expected: `.aiwork/workflows/{workflow-id}/spec.md`

The workflow may not have been properly initialized.
```

### If steps.yaml missing:

```
⚠️ No step plan found

The workflow hasn't been planned yet.

Generate plan:
→ /workflow-plan {workflow-id}
```

### If workflow directory empty:

```
❌ Workflow directory is empty

Location: `.aiwork/workflows/{workflow-id}/`

This workflow may be corrupted. Consider:
1. Regenerating with /workflow-new
2. Or manually checking the directory
```

---

## Examples

### Example Output - Active Workflow

```
# Workflow Information: User Retention Analysis

**Workflow ID**: 001-user-retention
**Session**: my-analysis (data-analysis)
**Status**: 🔄 In Progress
**Created**: 2025-10-28
**Last Activity**: 2 hours ago

---

## Overview

**Objective**: Analyze user retention patterns across acquisition channels to optimize marketing budget allocation

**Template**: data-analysis
**Priority**: High

---

## Progress Summary

**Overall Progress**: 3/6 steps (50%)

```
Progress: ████████░░░░ 50%
```

**Status Breakdown**:
- ✅ Completed: 3 steps
- 🔄 In Progress: 0 steps
- ⚪ Pending: 3 steps

**Time Tracking**:
- Estimated Total: 12h
- Actual Spent: 5h 15m
- Remaining: ~6h 45m
- Efficiency: 113% (slightly under time)

---

## Steps Overview

| ID | Title | Status | Priority | Assigned To | Duration |
|----|-------|--------|----------|-------------|----------|
| 1 | Data Loading | ✅ | High | claude | 1h 15m / 1.5h |
| 2 | Data Cleaning | ✅ | High | chatgpt | 1h 45m / 2h |
| 3 | EDA | ✅ | High | chatgpt | 2h 15m / 2.5h |
| 4 | Core Analysis | ⚪ | High | - | - / 3h |
| 5 | Visualization | ⚪ | Medium | - | - / 2h |
| 6 | Final Report | ⚪ | Medium | - | - / 1.5h |

---

## Next Actions

**Start Next Step**:
- Step 4: Core Analysis (high, ~3h)
  → /step-prepare 4 001

---

**Report Generated**: 2025-10-30 14:30:00
```

---

**Remember**: This command provides deep dive into a single workflow. Make it comprehensive and useful!
