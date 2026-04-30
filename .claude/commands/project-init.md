# Initialize Project PRD (Product Requirements Document)

You are the PRD creation assistant for software development sessions. When the user runs this command, guide them through creating a comprehensive Product Requirements Document.

## Command Usage

```
/project-init
```

**No parameters required.** This command is interactive.

**Prerequisites:**
- Must have an active session of type "software"
- Should be run before creating workflows/features

---

## Your Tasks

### 1. Check Session Type

First, verify this is a software development session:

Read `.aiwork/session.yaml`:
- If `type: "software"` → Continue
- If other type → Show error

**Error if not software session:**
```
❌ This command is for software development sessions only

Your session type: {type}

For software development:
1. Initialize software session: /session-init software my-project
2. Then run: /project-init

For other session types, PRD is not needed. Use SESSION.md instead.
```

### 2. Check if PRD Already Exists

Check if `.aiwork/PRD.md` exists:

**If exists:**
```
⚠️ PRD already exists

Found existing PRD at .aiwork/PRD.md

Options:
1. View existing PRD (cancel this command)
2. Update existing PRD (use /project-update instead)
3. Recreate PRD from scratch (⚠️  will overwrite)

Choose option: (1/2/3)
```

Only proceed with recreation if user explicitly chooses option 3.

### 3. Interactive PRD Creation

Guide the user through 10-12 questions to build a comprehensive PRD.

**Tone:** Conversational and helpful. Provide examples for each question.

---

#### Question 1: Project Name and Vision

```
Let's create your Product Requirements Document (PRD)!

This will define the overall project requirements, tech stack, and constraints.
All features you create will reference this PRD.

---

Q1: What is your project name?

Example: "TaskFlow - Team Task Management App"

→ {user input}
```

---

#### Question 2: Project Vision

```
Q2: What is the project vision? (1-2 sentences)

This is the big-picture goal - what you're ultimately trying to achieve.

Example: "Create an intuitive task management platform that helps small teams
collaborate efficiently without the complexity of enterprise tools."

→ {user input}
```

---

#### Question 3: Problem and Target Users

```
Q3: What problem does this solve, and who are the target users?

Be specific about the problem and user segments.

Example: "Small teams (3-10 people) struggle with existing tools that are either
too simple (to-do lists) or too complex (enterprise PM tools). Target users are
startup teams, small agencies, and remote teams."

→ {user input}
```

---

#### Question 4: Core Value Proposition

```
Q4: What makes this project unique? What's the core value proposition?

Example: "Strikes the perfect balance between simplicity and power. Real-time
collaboration without the learning curve. Self-hosted option for privacy-conscious teams."

→ {user input}
```

---

#### Question 5: Key Success Metrics

```
Q5: What are 3-5 key success metrics (KPIs)?

These are measurable goals that define success.

Example:
- User activation rate: >60% create first task within 5 minutes
- Team retention: >70% of teams active after 30 days
- Performance: Page load time <1 second
- Reliability: 99.9% uptime

→ {user input}
```

---

#### Question 6: Tech Stack

```
Q6: What is your tech stack?

List the main technologies you'll use.

Example:
Backend: Node.js + Express + PostgreSQL
Frontend: React + TypeScript + Tailwind CSS
Infrastructure: Docker + AWS
Authentication: JWT
Real-time: WebSocket

→ {user input}
```

---

#### Question 7: System Architecture

```
Q7: Describe your system architecture (high-level)

Example: "Three-tier architecture:
- Frontend SPA (React) communicating via REST API
- Backend API server (Node.js) with business logic
- PostgreSQL database for persistence
- Redis for caching and session storage
- WebSocket server for real-time updates"

→ {user input}
```

---

#### Question 8: Core Modules/Features

```
Q8: What are the core modules or feature areas?

List 5-10 major functional areas. We'll prioritize these next.

Example:
1. User Authentication & Authorization
2. Task Management (CRUD)
3. Team/Workspace Management
4. Real-time Collaboration
5. Notifications
6. Search & Filtering
7. File Attachments
8. Activity Timeline
9. Reporting & Analytics

→ {user input}
```

---

#### Question 9: Feature Prioritization

```
Q9: Let's prioritize these features.

For each feature you listed, assign priority:
- MVP: Must have for initial release
- v1.0: Important, shortly after MVP
- v2.0: Nice to have, future release

{Show user's feature list and ask for priority for each}

Example:
1. User Authentication → MVP
2. Task Management → MVP
3. Team Management → MVP
4. Real-time Collaboration → v1.0
5. Notifications → v1.0
...

→ {user input}
```

---

#### Question 10: Non-Functional Requirements

```
Q10: What are your non-functional requirements?

Think about: performance, security, scalability, reliability, usability

Example:
- Performance: API response time <200ms for 95% of requests
- Security: Data encrypted at rest and in transit, GDPR compliant
- Scalability: Support 10K concurrent users
- Reliability: 99.9% uptime, automated backups
- Usability: Mobile-responsive, accessibility (WCAG 2.1 AA)

→ {user input}
```

---

#### Question 11: Technical Constraints

```
Q11: Any technical constraints or limitations?

Example:
- Must support offline mode
- Must work on mobile browsers
- Must integrate with Slack and GitHub
- Maximum bundle size: 500KB (gzipped)
- Support browsers: Chrome, Firefox, Safari (last 2 versions)

→ {user input}
```

---

#### Question 12: Timeline and Milestones

```
Q12: What's your target timeline?

Example:
- MVP: 3 months (Q1 2025)
- v1.0: 6 months (Q2 2025)
- v2.0: 12 months (Q4 2025)

→ {user input}
```

---

### 4. Generate PRD Document

Create `.aiwork/PRD.md` using all the answers:

```markdown
# Product Requirements Document (PRD)

> {project-name}

**Version**: 1.0
**Created**: {date}
**Last Updated**: {date}
**Status**: Active

---

## 1. Project Overview

### 1.1 Project Name

{project-name}

### 1.2 Vision Statement

{vision from Q2}

### 1.3 Problem Statement

{problem from Q3}

**Target Users:**
{target users from Q3}

### 1.4 Value Proposition

{value proposition from Q4}

---

## 2. Product Goals & Success Metrics

### 2.1 Key Success Metrics (KPIs)

{metrics from Q5}

### 2.2 Business Goals

{Infer from answers or ask if needed}

---

## 3. System Architecture

### 3.1 Tech Stack

**Backend:**
{backend tech from Q6}

**Frontend:**
{frontend tech from Q6}

**Infrastructure:**
{infrastructure from Q6}

**Other:**
{other tech from Q6}

### 3.2 Architecture Overview

{architecture description from Q7}

```
{Optional: Add mermaid diagram if architecture is clear}
```

### 3.3 Data Model (High-Level)

{Infer key entities from features, or note "TBD in feature specs"}

---

## 4. Core Feature Modules

### 4.1 Feature Overview

{List features from Q8 with priorities from Q9}

| Module | Description | Priority | Target Version |
|--------|-------------|----------|----------------|
| {feature-1} | {brief description} | {priority} | {version} |
| {feature-2} | {brief description} | {priority} | {version} |
...

### 4.2 MVP Scope

**Must-Have Features for MVP:**
{List all MVP-priority features}

**MVP Success Criteria:**
- All MVP features implemented and tested
- Core user flows working end-to-end
- {Other criteria based on context}

### 4.3 Post-MVP Roadmap

**v1.0 Features:**
{List v1.0 features}

**v2.0 Features:**
{List v2.0 features}

---

## 5. Non-Functional Requirements

### 5.1 Performance

{performance requirements from Q10}

### 5.2 Security

{security requirements from Q10}

### 5.3 Scalability

{scalability requirements from Q10}

### 5.4 Reliability

{reliability requirements from Q10}

### 5.5 Usability

{usability requirements from Q10}

---

## 6. Technical Constraints & Standards

### 6.1 Constraints

{constraints from Q11}

### 6.2 Coding Standards

{Provide sensible defaults based on tech stack}

**Example for Node.js + TypeScript:**
- TypeScript strict mode enabled
- ESLint + Prettier for code formatting
- Jest for unit testing (>80% coverage target)
- Conventional Commits for git messages

### 6.3 API Standards

{Provide sensible defaults}

**Example for REST API:**
- RESTful design principles
- JSON request/response format
- JWT for authentication
- Versioned endpoints (/api/v1/...)
- Standard HTTP status codes

---

## 7. Development Guidelines

### 7.1 Workflow Process

When creating new features, use:
```
/workflow-new <feature-name>
```

Each feature should:
- Reference this PRD for tech stack and constraints
- Align with architecture defined here
- Follow coding standards
- Include tests meeting coverage target

### 7.2 Definition of Done

A feature is complete when:
- [ ] All acceptance criteria met
- [ ] Code reviewed and approved
- [ ] Tests written and passing (unit + integration)
- [ ] Documentation updated
- [ ] Deployed to staging and verified
- [ ] Security review completed (if applicable)

---

## 8. Project Timeline

### 8.1 Milestones

{timeline from Q12}

### 8.2 Dependencies

{List any external dependencies or blockers}

---

## 9. Risks & Mitigation

{Identify 3-5 key risks based on project scope}

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| {risk-1} | {High/Medium/Low} | {High/Medium/Low} | {mitigation strategy} |

**Example risks:**
- Technical complexity underestimated → Regular architecture reviews
- Third-party API reliability → Build fallback mechanisms
- Team scaling challenges → Document everything, onboarding process

---

## 10. Open Questions

{List any questions that came up during PRD creation}

- [ ] {Question 1}
- [ ] {Question 2}

---

## 11. Implementation Tracking

### 11.1 Workflows

*This section tracks all workflows (features) implemented for this project*

| ID | Feature/Workflow | Status | Version | Steps | Completed | Duration |
|----|------------------|--------|---------|-------|-----------|----------|
| - | - | - | - | - | - | - |

**Status Legend**:
- 📋 Planned - Spec created, not started
- 🔄 In Progress - Development underway
- ✅ Completed - All steps done, feature delivered
- 🚫 Blocked - Cannot proceed
- ⏸️ Paused - Temporarily on hold

**Note**: Workflows will be automatically added here when you create them with `/workflow-new`.

---

### 11.2 Overall Progress

**Current Version**: v1.0 (In Development)

**v1.0 Progress**:
- Workflows created: 0
- Workflows completed: 0
- Total steps: 0
- Completed steps: 0
- Overall completion: 0%

**Time Tracking**:
- Estimated total: TBD
- Actual time spent: 0h
- Remaining: TBD

---

## Appendix A: Glossary

{Define key terms specific to this project}

---

## Appendix B: References

{Links to relevant resources, competitor analysis, user research, etc.}

---

**Document Status**: ✅ Active

**Next Steps:**
1. Review this PRD with team/stakeholders
2. Refine any sections as needed using `/project-update`
3. Begin feature development: `/workflow-new <first-feature-name>`

---

*This PRD is a living document. Update it as the project evolves using `/project-update`.*
```

### 5. Update Session Tracking

Update `.aiwork/session.yaml`:

```yaml
session_id: "{session-id}"
type: "software"
# ... existing fields ...
prd_created: "{timestamp}"
prd_version: "1.0"
```

### 6. Output Summary

```
✅ PRD Created Successfully!

Location: .aiwork/PRD.md
Version: 1.0

📋 PRD Contents:
- Project overview and vision
- Tech stack: {brief tech stack}
- {N} core feature modules
- {X} MVP features, {Y} v1.0 features, {Z} v2.0 features
- Non-functional requirements
- Technical constraints
- Project timeline

🎯 MVP Scope:
{List MVP features}

📅 Target Timeline:
- MVP: {timeline}
- v1.0: {timeline}
- v2.0: {timeline}

📋 Next Steps:

1. **Review the PRD**:
   → Open .aiwork/PRD.md and review
   → Refine if needed: /project-update

2. **Start building features**:
   → /workflow-new <feature-name>
   → Features will automatically reference this PRD

3. **Prioritize MVP features first**:
   Recommended order:
   - {first MVP feature}
   - {second MVP feature}
   - {third MVP feature}

💡 Tips:
- All features you create will reference this PRD
- PRD ensures consistency across features
- Update PRD as project evolves: /project-update
- PRD is version-controlled like all other docs
```

---

## Important Notes

- **PRD is optional but recommended** for software projects
- PRD ensures all features align with overall project vision
- Tech stack and constraints from PRD are enforced in feature specs
- PRD is a living document - update via `/project-update`
- For small projects, can skip PRD and use SESSION.md instead

---

## Error Handling

### If not a software session:
```
❌ PRD is for software development only

Your session type: {type}

For software sessions: /session-init software <name>
For other types: Use SESSION.md for project overview
```

### If session not initialized:
```
❌ No session found

Initialize a software session first:
→ /session-init software <project-name>

Then run: /project-init
```

---

## Example PRD Creation Flow

```
User: /project-init