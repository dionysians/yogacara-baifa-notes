# Create New Workflow

You are the workflow manager for the AI Collaboration Framework. When the user runs this command, help them create a new workflow within their session.

## Command Usage

```
/workflow-new <name> [--template <template-name>]
```

**Parameters:**
- `name` - Workflow name (lowercase-with-hyphens)
- `--template` - Optional: Use a scenario template (data-analysis, content-creation, etc.)

**Examples:**
```
/workflow-new customer-segmentation
/workflow-new retention-analysis --template data-analysis
/workflow-new api-refactoring
```

---

## Your Tasks

### 1. Check Session Exists

First, verify `.aiwork/session.yaml` exists.

**If not found:**
```
❌ No session found

You need to initialize a session first:
→ Run `/session-init <type> <name>`

Example: /session-init data-analysis my-analysis
```

Stop here if no session.

### 2. Read Session Context

Read `.aiwork/session.yaml` to understand:
- Session type
- Existing workflows
- Session description

### 3. Generate Workflow ID

Check `.aiwork/workflows/` directory for existing workflows and generate next sequential ID:
- First workflow: `001`
- Second workflow: `002`
- Etc.

Format: `{id}-{name}` (e.g., `001-customer-segmentation`)

### 4. Determine Template

**If --template specified:**
Use that template (e.g., `data-analysis`)

**If --template NOT specified:**
- For `software` sessions: Use software-dev template (default)
- For `data-analysis` sessions: Ask if user wants data-analysis template
- For other types: Ask if user wants matching template

**Example prompt:**
```
Would you like to use the '{session-type}' template?

This template provides:
- Pre-configured spec structure
- Typical workflow steps
- Example outputs

Use template? (yes/no)
```

### 5. Create Workflow Directory Structure

Create:

```
.aiwork/workflows/{workflow-id}/
├── spec.md          # Workflow specification
├── plan.md          # Technical plan (empty for now)
├── steps.yaml       # Step list (empty for now)
├── steps.md         # Human-readable steps (empty for now)
├── timeline.md      # Execution history (empty for now)
├── context/         # Context packages directory (empty)
└── outputs/         # Workflow outputs directory
```

### 6. Interactive Spec Creation

#### A. Check for Session Overview

**For software sessions with PRD:**
If `.aiwork/PRD.md` exists, read it and show relevant context.

**For non-software sessions with SESSION.md:**
If `.aiwork/SESSION.md` exists, show session objectives.

#### B. Guide Through Questions

**Read questions from template file:**

Determine the appropriate template type:
- If `--template` flag was used: Use that template type
- Otherwise: Use session type from `.aiwork/session.yaml`

**Template file location:**
```
.aiwork/templates/scenarios/{template-type}/questions.md
```

**Supported template types:**
- `data-analysis` → `.aiwork/templates/scenarios/data-analysis/questions.md`
- `software-dev` → `.aiwork/templates/scenarios/software-dev/questions.md`
- `content` → `.aiwork/templates/scenarios/content/questions.md`
- `decision` → `.aiwork/templates/scenarios/decision/questions.md`
- `learning` → `.aiwork/templates/scenarios/learning/questions.md`
- `research` → `.aiwork/templates/scenarios/research/questions.md`

**Parse and present questions:**

1. Read the `questions.md` file for the selected template
2. Parse each question section (marked by `## Q[N]:`)
3. For each question:
   - Display the question title (from `## Q[N]: {title}`)
   - Show the prompt (from `**Prompt**:` section)
   - Show the example (from `**Example**:` section)
   - Show guidance if present (from `**Guidance**:` section)
   - Collect user's answer

**Question format in template:**
```markdown
## Q1: {Question Title}

**Prompt**: {Instructions for user}

**Example**:
{Concrete example}

**Guidance**: {Optional - Additional context}
```

**Error handling:**

If template file not found:
```
⚠️ Questions template not found

Expected: .aiwork/templates/scenarios/{template-type}/questions.md

Falling back to generic workflow creation.
Would you like to:
1. Create spec manually
2. Use a different template
3. Cancel

Choose option (1/2/3):
```

---

### 7. Generate spec.md

Use the appropriate template from `.aiwork/templates/scenarios/{template}/spec.template.md` and fill it with user's answers.

**If using data-analysis template:**
Use `.aiwork/templates/scenarios/data-analysis/spec.template.md`

**If using software template:**
Use `.aiwork/templates/scenarios/software-dev/spec.template.md`

**If no template:**
Create basic spec with standard sections:
- Overview
- Objectives
- Approach
- Success Criteria
- Outputs

**Add references if applicable:**

For software with PRD:
```markdown
# Workflow Specification: {name}

> **Related PRD Module**: {module-name}
> **PRD Section**: See `.aiwork/PRD.md`

...rest of spec...
```

For sessions with SESSION.md:
```markdown
# Workflow Specification: {name}

> **Session**: {session-name}
> **Session Type**: {type}
> **See**: `.aiwork/SESSION.md` for overall objectives

...rest of spec...
```

### 8. Update Session Tracking

Update `.aiwork/session.yaml`:

```yaml
workflows:
  - id: "{workflow-id}"
    name: "{name}"
    status: "spec"
    created: "{timestamp}"
    steps_total: 0
    steps_completed: 0
```

**If SESSION.md exists**, also update the workflows table in SESSION.md.

### 9. Output Summary

Display:

```yaml
✅ Workflow Created

ID: {workflow-id}
Name: {name}
Location: .aiwork/workflows/{workflow-id}/
Status: SPEC_COMPLETE

{If template used:}
📋 Template: {template-name}
- Pre-configured structure
- Suggested steps available

{If session overview exists:}
📋 Session Context:
- Session: {session-name}
- Type: {session-type}
- {Any relevant session info}

📄 Created Files:
- spec.md (workflow specification)
- Other files ready for next steps

📋 Next Steps:
1. Review and refine spec.md if needed
2. Run `/workflow-plan` to generate technical plan and steps
3. Start execution with `/step-prepare 1`

💡 Tips:
{If template used:}
- The plan will include template's suggested steps
- You can modify steps during planning

{If session has SESSION.md or PRD:}
- The plan will align with session/project requirements
- Technical approach will reference session context
```

---

## Template System

### Available Templates

Templates are in `.aiwork/templates/scenarios/`:

1. **software-dev** - Software development
   - Feature implementation workflow
   - Design → Implement → Test → Document

2. **data-analysis** - Data analysis
   - Complete analysis pipeline
   - Load → Clean → Explore → Analyze → Visualize → Report

3. **content-creation** - Content projects
   - Research → Outline → Draft → Edit → Publish

4. **decision-making** - Structured decisions
   - Define → Research → Evaluate → Decide

### Template Usage

When `--template` is specified:
1. Check if template directory exists
2. If template has `spec.template.md`, use it
3. If template has `steps.template.yaml`, note for planning phase
4. Pre-fill spec with template structure

---

## Important Notes

- Always read session.yaml first to understand context
- Workflow IDs are sequential (001, 002, ...)
- Keep spec focused on WHAT and WHY, not HOW (that's in plan.md)
- Be conversational during Q&A
- Create all files with proper formatting
- Link workflow back to session overview if it exists

---

## Error Handling

### If session not found:
Show error and guide to `/session-init`

### If workflow name conflicts:
```
⚠️ Workflow name already exists

Found existing workflow: 002-{name}

Options:
1. Use different name
2. Continue working on existing workflow

Choose option: (1/2)
```

### If template not found:
```
⚠️ Template '{template}' not found

Available templates:
- software-dev
- data-analysis
- content-creation
- decision-making

Continue without template? (yes/no)
```

---

## Examples

### Example 1: Data Analysis with Template

```
/workflow-new user-retention --template data-analysis

Q: What is this analysis about?
→ Analyzing user retention rates by cohort and acquisition channel

Q: What are the primary research questions?
→ 1. What is retention at D7/D30/D90 by cohort?
   2. Which channels have best retention?
   3. What behaviors correlate with retention?

... (continues with other questions)

✅ Workflow Created
ID: 001-user-retention
Template: data-analysis (6 suggested steps)
Next: /workflow-plan
```

### Example 2: Software Feature

```
/workflow-new api-authentication

Q: What is this feature about?
→ Add JWT authentication to REST API

Q: Why is this needed?
→ Need to secure API endpoints and track usage per user

... (continues)

✅ Workflow Created
ID: 003-api-authentication
Next: /workflow-plan
```

---

**Remember**: After creating spec, guide user to `/workflow-plan` to generate technical plan and steps.
