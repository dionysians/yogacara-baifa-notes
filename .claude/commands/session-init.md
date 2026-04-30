# Initialize New Session

You are the session manager for the AI Collaboration Framework. When the user runs this command, help them initialize a new work session.

## Command Usage

```
/session-init [name]
```

**Parameters:**
- `name` - Optional: Session name (lowercase-with-hyphens). If not provided, will prompt for it.

**Examples:**
```
/session-init
/session-init customer-retention-study
/session-init my-project
```

---

## Your Tasks

### 1. Check if .aiwork/ Already Exists

First, check if `.aiwork/` directory already exists:

**If exists:**
```
⚠️ Session already exists

Found existing .aiwork/ directory.

Current session:
- ID: {session-id from session.yaml}
- Type: {type}
- Created: {date}

Options:
1. Use existing session (cancel this command)
2. Create new workflow in existing session: /workflow-new <name>
3. Overwrite existing session (⚠️  will delete all data)

Choose option: (1/2/3)
```

Only proceed with overwrite if user explicitly types "3".

### 2. Interactive Session Type Selection

**If name was not provided in command:**
```
Welcome to AI Collaboration Framework!

Let's create a new session.

What would you like to name your session?

Use lowercase with hyphens (e.g., my-project, customer-analysis)

→ {user input for name}
```

**Then show session type menu:**

```
Great! Now, what type of work will you be doing?

Choose a session type:

1. 📊 data-analysis    - Data exploration and analysis projects
2. 💻 software         - Software development projects
3. ✍️  content         - Content creation (articles, courses, documentation)
4. 🤔 decision         - Decision-making processes
5. 📚 learning         - Learning and skill development
6. 🔬 research         - Research projects
7. ⚙️  general         - General purpose (for any other work type)

Enter number (1-7) or type name:
→ {user input}
```

**Accept either:**
- Number: `1`, `2`, `3`, etc.
- Type name: `data-analysis`, `software`, `content`, etc.

**Validate input:**
- If invalid, show error and ask again
- If valid, proceed

### 3. Select Documentation Language

**Ask for language preference:**

```
What language would you like to use for documentation?

Choose documentation language:

1. 🇺🇸 English    - All documentation in English
2. 🇨🇳 中文        - 所有文档使用中文

Enter number (1-2) or language name (english/chinese/中文):
→ {user input}
```

**Accept:**
- Number: `1` or `2`
- Language name: `english`, `chinese`, `中文`, `英文`

**Map to language code:**
- English → `en`
- Chinese → `zh`

### 4. Confirm and Show Details

```
✅ Session Configuration

Name: {session-name}
Type: {type-name}
Language: {English/中文}

{Show description for selected type:}

{if software:}
📝 Software Development
- Purpose: Build software projects with structured workflows
- Typical work: Features, bug fixes, refactoring, testing
- Key command: /project-init (creates PRD)

{if data-analysis:}
📊 Data Analysis
- Purpose: Explore, analyze, and derive insights from data
- Typical work: Data pipelines, statistical analysis, reporting
- Key command: /analysis-init (creates SESSION.md)

{if content:}
✍️ Content Creation
- Purpose: Create written content and media
- Typical work: Articles, courses, documentation, books
- Key command: /content-init (creates SESSION.md)

{if decision:}
🤔 Decision Making
- Purpose: Structured decision-making processes
- Typical work: Option evaluation, criteria definition, research
- Key command: /decision-init (creates SESSION.md)

{if learning:}
📚 Learning & Development
- Purpose: Track learning journeys and skill development
- Typical work: Courses, practice projects, exercises
- Key command: /learning-init (creates SESSION.md)

{if research:}
🔬 Research
- Purpose: Academic or professional research projects
- Typical work: Literature review, experiments, analysis, papers
- Key command: /research-init (creates SESSION.md)

{if general:}
⚙️ General Purpose
- Purpose: Any type of structured work not covered above
- Typical work: Planning, brainstorming, project management, etc.
- Key command: /general-init (creates SESSION.md)
- Flexible: Adapt to any workflow you need

Proceed with this configuration? (yes/no)
→ {user input}
```

If user says no, go back to type selection.

### 2. Create Directory Structure

Create the following structure:

```
.aiwork/
├── session.yaml           # Session metadata
├── SESSION.md            # Optional session overview (create if type != software)
├── workflows/            # Workflow directories
├── templates/            # Copy scenario templates
│   └── scenarios/
│       ├── software-dev/
│       ├── data-analysis/
│       ├── content-creation/
│       └── decision-making/
└── config/
    └── session-config.yaml
```

### 3. Generate session.yaml

Create `.aiwork/session.yaml` with:

```yaml
session_id: "{name}"
type: "{type}"
title: "{human-readable title}"
created: "{ISO 8601 timestamp}"
status: "active"
language: "{en or zh}"
description: ""
workflows: []
```

**Example (English):**
```yaml
session_id: "customer-retention-study"
type: "data-analysis"
title: "Customer Retention Analysis"
created: "2025-10-30T10:00:00Z"
status: "active"
language: "en"
description: ""
workflows: []
```

**Example (Chinese):**
```yaml
session_id: "customer-retention-study"
type: "data-analysis"
title: "客户留存分析"
created: "2025-10-30T10:00:00Z"
status: "active"
language: "zh"
description: ""
workflows: []
```

### 4. Create session-config.yaml

Create `.aiwork/config/session-config.yaml` with default settings:

```yaml
session:
  auto_archive: true
  require_review: true

workflows:
  default_status: "pending"
  auto_numbering: true

steps:
  default_status: "pending"
  allowed_ai_tools:
    - claude
    - chatgpt
    - cursor
    - copilot
    - gemini
    - other

tracking:
  track_time: true
  track_ai_tool: true
  track_iterations: true

outputs:
  default_directory: "outputs"
  archive_directory: "archive"
```

### 5. Do NOT Create SESSION.md

**Do not create SESSION.md in this command.**

Instead, guide users to use the appropriate initialization command for their session type.


### 6. Show Next Steps

Display a summary and guide next steps:

```
✅ Session Initialized

Session ID: {session-id}
Type: {type}
Language: {English/中文}
Location: .aiwork/

📁 Structure created:
- session.yaml (metadata, language: {en/zh})
- config/session-config.yaml (settings)
- workflows/ (empty, ready for workflows)

📝 Documentation Language: {English/中文}
All generated documents will be in {English/Chinese}.

📋 Next Steps:

{Display appropriate next steps based on session type:}

{if type == "software":}
1. **Create Project Requirements Document (PRD)**:
   → Run: /project-init
   → This creates a comprehensive PRD defining your project's tech stack,
     architecture, features, and constraints
   → Optional but highly recommended for consistency

2. **Or skip to creating features**:
   → Run: /workflow-new <feature-name> --template software-dev

{if type == "data-analysis":}
1. **Create Analysis Session Overview**:
   → Run: /analysis-init
   → This will guide you through 7 questions to define your analysis context,
     objectives, data sources, and expected deliverables
   → Creates comprehensive SESSION.md (similar to PRD for data analysis)
   → Recommended before creating workflows

2. **Then create your first analysis workflow**:
   → Run: /workflow-new <analysis-name> --template data-analysis

{if type == "content":}
1. **Create Content Session Overview**:
   → Run: /content-init
   → This will help you define your content goals, audience, and plan
   → Creates SESSION.md for your content project

2. **Then create your first content workflow**:
   → Run: /workflow-new <content-piece>

{if type == "decision":}
1. **Create Decision Session Overview**:
   → Run: /decision-init
   → This will help you define the decision, options, and criteria
   → Creates SESSION.md for your decision process

2. **Then create your first decision workflow**:
   → Run: /workflow-new <decision-aspect>

{if type == "learning":}
1. **Create Learning Session Overview**:
   → Run: /learning-init
   → This will help you define your learning goals and plan
   → Creates SESSION.md for your learning journey

2. **Then create your first learning workflow**:
   → Run: /workflow-new <topic-or-module>

{if type == "research":}
1. **Create Research Session Overview**:
   → Run: /research-init
   → This will help you define your research question and methodology
   → Creates SESSION.md for your research project

2. **Then create your first research workflow**:
   → Run: /workflow-new <research-phase>

{if type == "general":}
1. **Create General Session Overview**:
   → Run: /general-init
   → This will help you define your work objectives and approach
   → Creates SESSION.md for your general purpose work
   → Flexible format that adapts to any type of work

2. **Then create your first workflow**:
   → Run: /workflow-new <workflow-name>
   → Tip: You can use any existing template or create custom workflow

💡 Tips:
- Each workflow represents a major phase or component
- You can create multiple workflows within this session
- All context is preserved in markdown files
- Switch between AI tools freely using context packages
```

---

## Session Type Details

### software
- Purpose: Software development projects
- Typical workflows: Features, refactorings, bug fixes
- Typical steps: Design, implement, test, document
- Output: Code, tests, documentation

### data-analysis
- Purpose: Data exploration and analysis
- Typical workflows: Analysis pipelines, reports
- Typical steps: Load, clean, explore, analyze, visualize, report
- Output: Notebooks, reports, datasets, visualizations

### content
- Purpose: Content creation projects
- Typical workflows: Articles, courses, documentation
- Typical steps: Research, outline, draft, edit, publish
- Output: Written content, media assets

### decision
- Purpose: Structured decision-making
- Typical workflows: Option evaluation, research
- Typical steps: Define criteria, research options, evaluate, decide
- Output: Decision document, comparison matrices

### learning
- Purpose: Learning and skill development
- Typical workflows: Courses, projects, exercises
- Typical steps: Learn concept, practice, build project, review
- Output: Notes, projects, reflections

### research
- Purpose: Research projects
- Typical workflows: Literature review, experiments, analysis
- Typical steps: Research, synthesize, experiment, document
- Output: Research notes, papers, findings

### general
- Purpose: Any type of structured work not covered by other types
- Typical workflows: Custom workflows for any purpose
- Typical steps: Flexible - define your own
- Output: Any type of output
- Use cases: Project planning, brainstorming, event planning, personal organization, etc.

---

## Important Notes

- **Only run this once per project/session**
- Creates `.aiwork/` directory in current working directory
- If `.aiwork/` exists, warn and ask user to confirm overwrite
- Session names should be descriptive but concise
- Session type determines available templates and default workflows

## Error Handling

### If `.aiwork/` already exists:

```
⚠️ Session already exists

Found existing .aiwork/ directory.

Options:
1. Use existing session (cancel this command)
2. Create new workflow in existing session: `/workflow-new <name>`
3. Overwrite existing session (⚠️  will delete all data)

Continue with overwrite? (yes/no)
```

Only proceed with overwrite if user explicitly types "yes".

---

## Example Sessions

### Example 1: Data Analysis Session

```bash
/session-init data-analysis q4-marketing-analysis
```

Creates structure ready for marketing data analysis workflows.

### Example 2: Software Project

```bash
/session-init software task-manager-app
```

Creates structure for software feature development.

### Example 3: Learning Project

```bash
/session-init learning rust-programming
```

Creates structure for tracking learning progress and projects.

---

**Remember**: After initialization, guide user to create their first workflow with `/workflow-new`.
