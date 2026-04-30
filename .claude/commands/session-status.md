# Session Status Overview

You are the session status reporter for the AI Collaboration Framework. When the user runs this command, provide a comprehensive overview of the current session and all workflows.

## Command Usage

```
/session-status
```

**No parameters required** - Shows complete session overview

**Examples:**
```
/session-status
```

---

## Your Tasks

### 1. Check Session Exists

Verify `.aiwork/session.yaml` exists.

**If not found:**
```
❌ No active session found

Initialize a session first:
→ /session-init
```

### 2. Read Session Context

Read the following files:
1. `.aiwork/session.yaml` - Session metadata
2. `.aiwork/SESSION.md` or `.aiwork/PRD.md` (if exists) - Session overview
3. All workflow directories in `.aiwork/workflows/` - Workflow details

### 3. Display Session Overview

```
# Session Status Report

**Session ID**: {session-id}
**Type**: {type} {emoji}
**Language**: {English/中文}
**Created**: {date}
**Status**: {status-emoji} {status}
**Last Activity**: {last-activity-timestamp}

---

## Session Overview

{If SESSION.md or PRD.md exists:}
**Description**: {brief description from session doc}

{For software sessions with PRD:}
**Project**: {project-name}
**Tech Stack**: {tech-stack}

{For data analysis sessions:}
**Business Context**: {brief context}
**Key Objectives**: {count} objectives defined

---

## Workflows Summary

**Total Workflows**: {count}
**Active**: {count}
**Completed**: {count}
**Planned**: {count}

### Progress Overview

| ID | Workflow | Status | Steps | Progress | Last Activity | Template |
|----|----------|--------|-------|----------|---------------|----------|
| {id} | {name} | {status-emoji} | {completed}/{total} | {progress-bar} | {date} | {template} |
| 001 | user-retention | 🔄 In Progress | 3/6 | ████████░░░░░ 50% | 2h ago | data-analysis |
| 002 | churn-analysis | 📋 Planned | 0/5 | ░░░░░░░░░░░░ 0% | 1d ago | data-analysis |

**Status Legend**:
- 📋 Planned - Steps defined, not started
- 🔄 In Progress - Currently being worked on
- ⏸️ Paused - Temporarily stopped
- ✅ Completed - All steps finished
- 🚫 Blocked - Cannot proceed

---

## Current Activity

{If any workflows have in_progress steps:}
### Steps In Progress

{For each workflow with in_progress steps:}
**Workflow {id}: {name}**
- Step {step-id}: {step-title}
- Started: {started-time}
- Duration so far: {duration}
- Assigned to: {ai-tool or "Unassigned"}

{If no steps in progress:}
*No steps currently in progress*

---

## Available Next Steps

{For each workflow, show ready-to-start steps:}
**Workflow {id}: {name}**
- Step {step-id}: {step-title} ({priority}, ~{hours}h)
  → /step-prepare {step-id} {workflow-id}

{If no steps available:}
*No steps ready to start (dependencies not met or all complete)*

---

## Statistics

### Overall Progress
- **Total Steps Across All Workflows**: {total}
- **Completed**: {count} ({percentage}%)
- **In Progress**: {count}
- **Pending**: {count}
- **Estimated Remaining Time**: {hours}h

### AI Tool Usage (Completed Steps)
{For each ai tool that has completed steps:}
- **{AI-Tool}**: {count} steps ({percentage}%)

### Activity Timeline
- **Session Duration**: {duration since created}
- **Active Days**: {count days with activity}
- **Last Activity**: {most recent activity timestamp}
- **Average Steps per Day**: {calculation}

---

## Workflow Details

{For each workflow, show brief details:}

### {workflow-id}: {workflow-name}

**Status**: {status-emoji} {status}
**Type**: {type}
**Created**: {created-date}
**Progress**: {completed}/{total} steps ({percentage}%)
**Estimated Time**: {remaining}h remaining

**Recent Activity**:
- {Most recent timeline entry}

**Next Action**:
{If has ready steps:}
- Step {id}: {title}
  → /step-prepare {step-id} {workflow-id}

{If all steps complete:}
- Ready to finish
  → /workflow-finish {workflow-id}

{If blocked or no steps ready:}
- Waiting on dependencies or needs planning

**Location**: `.aiwork/workflows/{workflow-id}/`

---

{End of workflow list}

---

## Quick Actions

{Generate contextual recommendations:}

**Start New Workflow**:
→ /workflow-new <name> [--template <template-name>]

{If any workflows are planned but not started:}
**Start Planned Workflow**:
→ /step-prepare 1 {workflow-id}

{If any workflows are in progress:}
**Continue Active Work**:
→ /step-prepare {next-step-id} {workflow-id}

{If any workflows are complete but not finished:}
**Finish Completed Workflow**:
→ /workflow-finish {workflow-id}

**View Specific Workflow**:
→ /workflow-info {workflow-id}

---

## Tips

💡 **Parallel Workflows**:
- You can work on multiple workflows simultaneously
- Use workflow-id parameter when you have multiple active workflows
- Example: `/step-prepare 2 001` and `/step-prepare 1 002`

💡 **Context Switching**:
- All context is preserved in markdown files
- Switch between workflows anytime
- Each workflow maintains its own state

💡 **Detailed View**:
- Use `/workflow-info <id>` to see full details of a specific workflow
- Open `.aiwork/workflows/{id}/steps.md` for complete step list
- Check `.aiwork/workflows/{id}/timeline.md` for execution history

---

**Report Generated**: {timestamp}
**Session Location**: `.aiwork/`
```

---

## Display Rules

### Status Emojis

**Session Status**:
- 🟢 Active - Has active or in-progress workflows
- 🟡 Idle - All workflows completed or paused
- 🔴 Stale - No activity in 7+ days

**Workflow Status**:
- 📋 Planned - spec and steps defined, not started
- 🔄 In Progress - at least one step in_progress or completed
- ⏸️ Paused - explicitly paused by user
- ✅ Completed - all steps completed
- 🚫 Blocked - has blocking issues

**Progress Bars**:
```
0-10%:   ░░░░░░░░░░░░
20%:     ██░░░░░░░░░░
50%:     ████████░░░░
75%:     ███████████░
100%:    ████████████
```

### Workflow Types

Map session types to emojis:
- software: 💻
- data-analysis: 📊
- content: ✍️
- decision: 🤔
- learning: 📚
- research: 🔬
- general: ⚙️

---

## Important Notes

- **Read all workflow directories** - Don't miss any workflows
- **Calculate accurate statistics** - Count steps, progress, etc.
- **Show relative timestamps** - "2h ago" instead of absolute time
- **Highlight actionable items** - What user can do next
- **Be concise for many workflows** - Summarize if 5+ workflows
- **Always show parallel workflow capability** - Remind users they can work on multiple

---

## Error Handling

### If session but no workflows:

```
# Session Status Report

Session: {session-id}
Type: {type}
Status: 🟡 Idle (No workflows yet)

No workflows found.

Create your first workflow:
→ /workflow-new <name>

{For software sessions:}
💡 Tip: Consider creating a PRD first:
→ /project-init

{For data-analysis sessions:}
💡 Tip: Consider creating session overview first:
→ /analysis-init
```

### If session file corrupt:

```
❌ Session file error

The session.yaml file appears to be corrupted.

Location: .aiwork/session.yaml

Please check the file or reinitialize:
→ /session-init
```

---

## Examples

### Example Output - Active Session with Multiple Workflows

```
# Session Status Report

**Session ID**: my-analysis-project
**Type**: 📊 Data Analysis
**Language**: English
**Created**: 2025-10-28
**Status**: 🟢 Active
**Last Activity**: 2 hours ago

---

## Workflows Summary

**Total Workflows**: 3
**Active**: 2
**Completed**: 1

### Progress Overview

| ID | Workflow | Status | Steps | Progress | Last Activity |
|----|----------|--------|-------|----------|---------------|
| 001 | user-retention | 🔄 In Progress | 3/6 | ████████░░░░ 50% | 2h ago |
| 002 | churn-analysis | 📋 Planned | 0/5 | ░░░░░░░░░░░░ 0% | 1d ago |
| 003 | revenue-forecast | ✅ Completed | 6/6 | ████████████ 100% | 3d ago |

---

## Current Activity

### Steps In Progress

**Workflow 001: user-retention**
- Step 3: Core Analysis
- Started: 45 minutes ago
- Assigned to: chatgpt

---

## Available Next Steps

**Workflow 001: user-retention**
- Step 4: Visualization (high, ~2h)
  → /step-prepare 4 001

**Workflow 002: churn-analysis**
- Step 1: Data Loading (high, ~1.5h)
  → /step-prepare 1 002

---

## Statistics

### Overall Progress
- **Total Steps**: 17
- **Completed**: 9 (53%)
- **In Progress**: 1 (6%)
- **Pending**: 7 (41%)
- **Estimated Remaining Time**: 12h

### AI Tool Usage
- **ChatGPT**: 5 steps (56%)
- **Claude**: 4 steps (44%)

---

## Quick Actions

**Continue Active Work**:
→ /step-prepare 4 001

**Start New Analysis**:
→ /step-prepare 1 002

**View Workflow Details**:
→ /workflow-info 001
→ /workflow-info 002

---

💡 **Tip**: You have 2 workflows active. You can work on both in parallel!

**Report Generated**: 2025-10-30 14:23:45
```

---

**Remember**: This command gives users a bird's-eye view of their entire session. Make it informative and actionable!
