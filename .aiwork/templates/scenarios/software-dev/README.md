# Software Development Scenario Template

> Pre-configured workflow for software feature development

## Overview

This template provides a structured workflow for software development tasks, from design through implementation, testing, and documentation.

**This template is equivalent to the v2.0 workflow pattern**, adapted for the v3.0 universal framework.

## Typical Workflow Steps

1. **Technical Design**
   - Architecture and component design
   - API/interface design
   - Data model design
   - Output: Design document

2. **Core Implementation**
   - Implement main functionality
   - Business logic
   - Data access layer
   - Output: Core code

3. **API/Interface Layer**
   - REST API endpoints or UI components
   - Request/response handling
   - Validation
   - Output: API/UI code

4. **Integration**
   - Connect components
   - External service integration
   - Configuration
   - Output: Integrated system

5. **Testing**
   - Unit tests
   - Integration tests
   - Manual testing scenarios
   - Output: Test suite

6. **Documentation**
   - API documentation
   - Code comments
   - Usage examples
   - Output: Documentation

7. **Code Review & Refinement** (optional)
   - Review code quality
   - Refactor if needed
   - Performance optimization
   - Output: Refined code

8. **Deployment Preparation** (optional)
   - Migration scripts
   - Environment configuration
   - Deployment documentation
   - Output: Deployment package

## When to Use This Template

✅ **Good for:**
- Feature implementation
- New module/component development
- API development
- Refactoring projects
- Bug fixes (for complex bugs)

❌ **Not ideal for:**
- Quick bug fixes (< 2 hours, don't need workflow)
- Documentation-only tasks
- Configuration changes
- Non-development work (use other templates)

## How to Use

### 1. Initialize Software Session

```bash
/session-init software my-project
```

### 2. Create PRD (Recommended)

```bash
/project-init
```

This creates a global Product Requirements Document with:
- Project vision and goals
- Tech stack and architecture
- Feature roadmap
- Non-functional requirements
- Technical constraints

**All features will reference this PRD for consistency.**

### 3. Create Feature Workflow with Template

```bash
/workflow-new user-authentication --template software-dev
```

This will:
- Create workflow directory
- Pre-fill spec.md with software development template
- Guide you through feature requirements

### 4. Customize Spec

Answer questions about your specific feature:
- What is this feature?
- Why is it needed?
- Who are the users?
- What are the acceptance criteria?
- Tech stack (from PRD or specify)

### 5. Generate Plan

```bash
/workflow-plan
```

The template includes suggested steps (design → implement → test → document) that you can:
- Use as-is
- Modify for your needs
- Add/remove steps

### 6. Execute Steps

```bash
/step-prepare 1
# Implement design...
/step-complete 1 --ai claude

/step-prepare 2
# Implement core...
/step-complete 2 --ai cursor

# ... continue through steps
```

## Example: User Authentication Feature

See `example-workflow/` for a complete JWT authentication feature with:
- PRD alignment
- 8-step workflow
- Multi-AI collaboration
- Complete outputs (models, services, API, tests, docs)

## Template Customization

### Modify Steps

Edit `steps.template.yaml` to change default steps.

For example, if you always need:
- Database migrations
- Docker configuration
- CI/CD setup

Add these as default steps.

### Modify Spec Template

Edit `spec.template.md` to change questions and structure for your organization's needs.

### Add Project-Specific Templates

Create sub-templates for common patterns in your project:
- `microservice/` - Pre-configured for microservice development
- `react-component/` - React component development workflow
- `api-endpoint/` - REST API endpoint workflow

## PRD Integration

### How PRD Works with Features

When you create a feature with PRD:

1. **Spec references PRD:**
   ```markdown
   # Feature Specification: User Authentication

   > **Related PRD Module**: User Management
   > **PRD Priority**: MVP
   ```

2. **Plan aligns with PRD:**
   - Uses tech stack from PRD (Node.js, PostgreSQL, JWT)
   - Follows architecture from PRD (3-tier architecture)
   - Respects constraints from PRD (performance, security)

3. **Consistency enforced:**
   - All features use same tech stack
   - All features follow same patterns
   - All features meet same quality bar

### When to Update PRD

Update PRD when:
- Adding new feature areas to roadmap
- Changing tech stack
- Updating architecture
- Modifying non-functional requirements

Use: `/project-update`

## AI Tool Recommendations

### Best Tools for Each Step

| Step | Recommended AI | Why |
|------|----------------|-----|
| Technical Design | Claude | Excellent architectural reasoning |
| Core Implementation | Cursor | Best for multi-file code editing |
| API Layer | ChatGPT / Cursor | Good at API patterns |
| Integration | Cursor | Can see and edit multiple files |
| Testing | GitHub Copilot | Great test generation |
| Documentation | Claude | Excellent writing |
| Code Review | Claude | Strong analytical skills |

### Multi-AI Strategy

**Strategy 1: Claude for planning, Cursor for coding**
- Use Claude for steps 1 (design) and 7 (review)
- Use Cursor for steps 2-4 (implementation)
- Use Claude for step 6 (documentation)

**Strategy 2: Specialized per language**
- Python: ChatGPT Code Interpreter (can execute)
- TypeScript: Cursor (excellent TS support)
- Go: Claude (good with Go idioms)

## Output Artifacts

Expected outputs from this workflow:

```
project/
├── src/
│   ├── {new-module}/
│   │   ├── model.ts
│   │   ├── service.ts
│   │   ├── controller.ts
│   │   └── index.ts
│   └── {modified-files}
│
├── tests/
│   └── {module}.test.ts
│
├── docs/
│   ├── api/
│   │   └── {module}-api.md
│   └── {module}-guide.md
│
└── migrations/
    └── {timestamp}_{module}.sql

.aiwork/workflows/{workflow-id}/
├── spec.md
├── plan.md
├── steps.yaml
├── steps.md
└── timeline.md
```

## Common Patterns

### Pattern 1: Full-Stack Feature

```yaml
# Full feature from database to UI
steps:
  - id: 1
    title: "Database schema and migrations"
  - id: 2
    title: "Data access layer (models)"
  - id: 3
    title: "Business logic (services)"
  - id: 4
    title: "API endpoints (controllers)"
  - id: 5
    title: "Frontend components"
  - id: 6
    title: "Integration tests"
  - id: 7
    title: "Documentation"
```

### Pattern 2: Backend-Only API

```yaml
# API development
steps:
  - id: 1
    title: "API design (OpenAPI spec)"
  - id: 2
    title: "Data models"
  - id: 3
    title: "Service layer"
  - id: 4
    title: "API controllers"
  - id: 5
    title: "Input validation"
  - id: 6
    title: "Unit tests"
  - id: 7
    title: "Integration tests"
  - id: 8
    title: "API documentation"
```

### Pattern 3: Refactoring

```yaml
# Code refactoring
steps:
  - id: 1
    title: "Analyze current code and identify issues"
  - id: 2
    title: "Design refactored structure"
  - id: 3
    title: "Write comprehensive tests for existing behavior"
  - id: 4
    title: "Refactor implementation"
  - id: 5
    title: "Verify all tests still pass"
  - id: 6
    title: "Update documentation"
```

## Tips & Best Practices

### Design First

Always start with technical design (step 1):
- Think through architecture before coding
- Design APIs/interfaces
- Plan data model
- Consider edge cases

**Good design saves time in implementation.**

### TDD When Appropriate

For complex logic, consider test-driven development:
- Write tests first (step 5 before step 2)
- Implement to pass tests
- Refactor with confidence

### Keep Steps Focused

Each step should:
- Have single responsibility
- Produce testable output
- Take 1-3 hours
- Not depend on many other steps

### PRD Alignment

Before starting implementation:
- Read PRD tech stack
- Check PRD constraints
- Follow PRD patterns
- Meet PRD quality bar

### Code Review Step

For important features, add code review step:
- Have different AI review the code
- Check for bugs, security issues
- Verify best practices
- Suggest improvements

## Troubleshooting

### Issue: Feature scope too large

**Problem:** Workflow has 15+ steps, feels overwhelming

**Solution:**
- Break into multiple workflows
- Each workflow = 1 module or component
- Create dependencies between workflows

**Example:**
Instead of "User Management" (20 steps):
- Workflow 1: "User Authentication" (8 steps)
- Workflow 2: "User Profiles" (6 steps)
- Workflow 3: "User Permissions" (7 steps)

### Issue: PRD and feature conflict

**Problem:** Feature needs different tech stack than PRD

**Solution:**
1. **Preferred:** Update PRD if change makes sense project-wide
2. **Alternative:** Document exception in feature spec
3. **Red flag:** If many features need exceptions, PRD is wrong

### Issue: Tests failing after implementation

**Problem:** Implemented feature but tests don't pass

**Solution:**
- This is normal! Tests catch issues
- Debug and fix implementation
- Don't mark step complete until tests pass
- Update estimate for testing step (may take longer)

## Resources

- **PRD Template:** See `.aiwork/templates/prd.template.md`
- **Example Feature:** See `example-workflow/`
- **Step Templates:** See `steps.template.yaml`

## Comparison with v2.0

| Aspect | v2.0 | v3.0 software-dev |
|--------|------|-------------------|
| Commands | `/feature-*`, `/task-*` | `/workflow-*`, `/step-*` |
| Directory | `.workflow/features/` | `.aiwork/workflows/` |
| PRD | `.workflow/PRD.md` | `.aiwork/PRD.md` |
| Spec | `spec.md` | `spec.md` (same) |
| Plan | `plan.md` | `plan.md` (same) |
| Tasks | `tasks.yaml` + `tasks.md` | `steps.yaml` + `steps.md` |

**Migration:** Rename commands and directories. Content structure is identical.

## Version History

- **v3.0** (2025-10-30): Adapted for universal framework
  - Renamed to software-dev template
  - Updated for new command names
  - Enhanced PRD integration

- **v2.1** (2025-10-29): Original version
  - PRD support
  - Dual-format tasks
  - Multi-AI collaboration

- **v2.0** (2025-10-28): Initial version
  - Document-driven workflow
  - Context packages
  - Feature development pattern
