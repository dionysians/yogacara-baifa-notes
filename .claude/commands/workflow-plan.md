# Generate Workflow Plan

You are the planning agent for the AI Collaboration Framework. When the user runs this command, generate a detailed technical plan and break down the workflow into concrete steps.

## Command Usage

```
/workflow-plan [workflow-id]
```

**Parameters:**
- `workflow-id` - Optional: Specific workflow (001, 001-name, or auto-detect)

**Examples:**
```
/workflow-plan                    # Auto-detect workflow
/workflow-plan 001                # Explicit ID
/workflow-plan 001-user-retention # Full name
```

---

## Your Tasks

### 1. Identify Target Workflow

**If workflow-id provided:**
- Use that workflow

**If not provided (auto-detect):**
- Check `.aiwork/workflows/` for workflows
- If exactly 1 workflow with status != "completed": Use that
- If multiple active workflows: Ask user to specify
- If no workflows: Error

**Error if no workflow:**
```
❌ No workflow found

Create a workflow first:
→ /workflow-new <name>
```

**Error if ambiguous:**
```
⚠️ Multiple active workflows found

Please specify which workflow to plan:

1. 001-user-retention (spec)
2. 002-churn-analysis (spec)

Usage: /workflow-plan <workflow-id>
Example: /workflow-plan 001
```

### 2. Read Context

Read all relevant context:

1. **Session context**: `.aiwork/session.yaml`
   - Session type
   - Overall context

2. **Session overview** (if exists):
   - `.aiwork/SESSION.md` (for non-software)
   - `.aiwork/PRD.md` (for software)

3. **Workflow spec**: `.aiwork/workflows/{id}/spec.md`
   - Requirements
   - Objectives
   - Constraints

4. **Template** (if used):
   - Check if template was used during workflow creation
   - Read template's `steps.template.yaml` if exists

### 3. Generate Technical Plan (plan.md)

**Read plan template from file:**

Determine the template type based on workflow:
- Check if template was specified when workflow was created
- Check session type from `.aiwork/session.yaml`
- Default to generic template if no specific template found

**Template file location:**
```
.aiwork/templates/scenarios/{template-type}/plan.template.md
```

**Supported template types:**
- `data-analysis` → `.aiwork/templates/scenarios/data-analysis/plan.template.md`
- `software-dev` → `.aiwork/templates/scenarios/software-dev/plan.template.md`
- `content` → `.aiwork/templates/scenarios/content/plan.template.md`
- `decision` → `.aiwork/templates/scenarios/decision/plan.template.md`
- `learning` → `.aiwork/templates/scenarios/learning/plan.template.md`
- `research` → `.aiwork/templates/scenarios/research/plan.template.md`

**Generate plan:**

1. Read the `plan.template.md` file for the selected template
2. Replace placeholders with actual values:
   - `{workflow-name}` → Workflow name from spec
   - `{timestamp}` → Current timestamp
   - `{workflow-id}` → Workflow ID (e.g., "001-feature-name")
   - `{session-name}` → From `.aiwork/session.yaml`
   - `{type}` → Session type
   - Other content-specific placeholders based on spec.md

3. Read spec.md and extract relevant information to fill template sections
4. If SESSION.md or PRD.md exists, extract alignment information
5. Generate step count and overview from steps.yaml (if already generated)
6. Fill in all template sections with appropriate content

**Create file:**
Save the generated plan to `.aiwork/workflows/{id}/plan.md`

**Error handling:**

If template file not found:
```
⚠️ Plan template not found

Expected: .aiwork/templates/scenarios/{template-type}/plan.template.md

Options:
1. Generate generic plan (basic structure)
2. Use a different template type
3. Cancel and create plan manually

Choose option (1/2/3):
```

If generic plan is chosen, create a basic plan structure:
```markdown
# Technical Plan: {workflow-name}

> Generated: {timestamp}

**Workflow ID**: {workflow-id}

## Plan Overview

{Extract from spec.md}

## Approach

{Describe technical approach}

## Implementation Steps

{Describe breakdown}

## Success Criteria

{From spec.md}

## Next Steps

1. Review steps.yaml
2. Execute steps sequentially
3. Each step generates context package
```

---

### 4. Generate Step Breakdown (steps.yaml)

Create `.aiwork/workflows/{id}/steps.yaml` with concrete steps.

**If template was used:**
- Start with template's `steps.template.yaml`
- Customize based on spec requirements
- Adjust step descriptions to match specific workflow

**If no template:**
- Generate steps from scratch based on spec and plan
- For data analysis: Typically 5-7 steps
- For software: Typically 6-10 steps

**Step YAML structure:**

```yaml
workflow: "{workflow-id}"
type: "{type}"
created: "{timestamp}"

steps:
  - id: 1
    title: "{step-title}"
    description: |
      {Detailed description}
      {What to do}
      {Expected output}
    status: pending
    priority: high|medium|low
    estimated_hours: {hours}
    assigned_to: null
    depends_on: []  # List of step IDs this depends on
    files:
      - "{file-path-1}"
      - "{file-path-2}"
    tags:
      - "{tag-1}"
      - "{tag-2}"
    notes: "{Additional context}"

  - id: 2
    title: "{step-2-title}"
    ...

total_steps: {count}
estimated_total_hours: {sum}
```

**Guidelines for steps:**
- Each step: 1-3 hours of work
- Clear, testable outputs
- Logical dependencies
- Balanced across workflow

### 5. Generate Human-Readable Steps (steps.md)

Create `.aiwork/workflows/{id}/steps.md` from steps.yaml.

Use template from `.aiwork/templates/tasks.template.md` (similar to v2.1):

```markdown
# Steps: {workflow-name}

> Human-readable step list - automatically synced with steps.yaml

**Workflow ID**: {workflow-id}
**Created**: {date}
**Total Steps**: {count}
**Completed**: 0/{total}

---

## Step Overview

| ID | Title | Priority | Status | Assigned | Est. Hours |
|----|-------|----------|--------|----------|------------|
| 1 | {title} | High | ⚪ | - | 2h |
| 2 | {title} | High | ⚪ | - | 1.5h |
...

**Status Legend**:
- ⚪ Pending
- 🔄 In Progress
- ✅ Completed
- 🚫 Blocked
- ⏭️ Skipped

---

## Step Details

### Step 1: {title}

**Status**: ⚪ Pending
**Priority**: 🔴 High
**Estimated Time**: 2 hours
**Assigned To**: Unassigned
**Dependencies**: None

#### Description
{description}

#### Files to Modify/Create
- `{file-1}`
- `{file-2}`

#### Tags
- `{tag-1}`
- `{tag-2}`

#### Notes
{notes}

---

{repeat for each step}

---

## Step Dependencies

```mermaid
graph TD
{generate dependency graph}
```

---

## Progress Tracking

### By Status
- **Pending**: {count} steps
- **In Progress**: 0 steps
- **Completed**: 0 steps

### By Priority
- **High**: {count} steps
- **Medium**: {count} steps
- **Low**: {count} steps

---

## Next Actions

### Ready to Start (No Dependencies)
{list steps with no dependencies}
- Step 1: {title} (High priority)

### Waiting on Dependencies
{list steps with dependencies}

---

**Last Updated**: {timestamp}
**Auto-generated from**: `steps.yaml`

> ⚠️ **Important**: This file is auto-generated from `steps.yaml`.
> To update steps, modify `steps.yaml` and regenerate this file,
> or use `/step-complete` which updates both files automatically.
```

### 6. Initialize timeline.md

Create `.aiwork/workflows/{id}/timeline.md`:

```markdown
# Execution Timeline: {workflow-name}

> Chronological record of all work on this workflow

**Workflow ID**: {workflow-id}
**Started**: {timestamp}
**Status**: In Progress

---

## Timeline

### {date} - Workflow Created

- Spec completed
- Plan generated
- {N} steps defined
- Ready to begin execution

---

{This will be updated as steps are completed}
```

### 7. Update Session Tracking

Update `.aiwork/session.yaml`:

```yaml
workflows:
  - id: "{workflow-id}"
    name: "{name}"
    status: "planned"  # Changed from "spec"
    created: "{timestamp}"
    planned: "{timestamp}"
    steps_total: {N}
    steps_completed: 0
```

Also update SESSION.md workflows table if it exists.

### 8. Output Summary

```yaml
✅ Plan Generated

Workflow: {workflow-id} - {name}
Location: .aiwork/workflows/{workflow-id}/

📄 Generated Files:
- plan.md ({X} lines) - Technical approach
- steps.yaml ({N} steps) - Machine-readable tasks
- steps.md - Human-readable step overview
- timeline.md - Execution tracking (initialized)

📊 Step Breakdown:
- Total steps: {N}
- Estimated time: {hours} hours
- High priority: {count}
- Medium priority: {count}
- Low priority: {count}

{If template used:}
📋 Template: {template-name}
- Steps customized from template
- {Any template-specific notes}

{If session context exists:}
📋 Alignment:
{For software with PRD:}
- PRD Module: {module}
- Tech Stack: {stack} (from PRD)
- Constraints: {constraints}

{For other sessions with SESSION.md:}
- Session: {session-name}
- Objectives aligned with session goals

🔄 Step Dependencies:
{If any dependencies exist:}
- Some steps depend on others (see steps.md dependency graph)
- Can parallelize: Steps {list-of-independent-steps}

📋 Next Steps:

1. **Review the plan**:
   → Open plan.md to review technical approach
   → Open steps.md to see all steps at a glance

2. **Start execution**:
   → /step-prepare 1
   → This generates a context package for step 1

3. **Execute with any AI**:
   → Copy context package to Claude/ChatGPT/Cursor
   → Implement the step
   → Return and run: /step-complete 1 --ai <tool>

💡 Tips:
- Review steps.md for complete overview
- Each step should take 1-3 hours
- You can modify steps.yaml if plan needs adjustment
- Context packages enable seamless AI tool switching
```

---

## Important Notes

- **Read all context** (session, spec, PRD/SESSION.md) before planning
- Plan must be **technically specific** (not just restating spec)
- Steps must be **concrete and actionable**
- Always generate **both steps.yaml and steps.md**
- **Align with PRD/session** constraints and tech stack
- Steps should be **testable and verifiable**
- Each step should have **clear outputs**

---

## Error Handling

### If spec.md not found:
```
❌ Workflow spec not found

The workflow hasn't been properly initialized.
→ Run `/workflow-new` first
```

### If plan already exists:
```
⚠️ Plan already exists

Found existing plan.md in workflow {workflow-id}.

Options:
1. Keep existing plan (cancel)
2. Regenerate plan (⚠️  will overwrite)
3. Append new steps to existing plan

Choose option: (1/2/3)
```

---

## Examples

See examples in:
- `examples/data-analysis-complete/` - Complete data analysis workflow
- `examples/software-feature-complete/` - Complete software feature

---

**Remember**: After planning, guide user to review and then start execution with `/step-prepare 1`.
