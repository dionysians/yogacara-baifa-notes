# Software Development Workflow Questions

> Interactive questions for creating a software development workflow specification

---

## Q1: What is this feature/workflow about?

**Prompt**: Describe the feature or work you're implementing (2-3 sentences)

**Example**:
"Implementing JWT-based authentication for our REST API to secure endpoints and enable per-user rate limiting. This will replace the current API key system with a more secure, user-specific authentication mechanism."

**Guidance**: Be specific about what you're building and why it's needed.

---

## Q2: Why is this needed?

**Prompt**: Explain the business value or problem this solves

**Example**:
- Current API key system doesn't identify individual users
- Need user-level rate limiting to prevent abuse
- Security team requires token expiration and refresh capability
- Enables future user-specific features like usage dashboards

**Guidance**: Connect the technical work to business outcomes and user needs.

---

## Q3: Who are the users?

**Prompt**: Describe target users or use cases

**Example**:
- Primary: External API consumers (mobile apps, third-party integrations)
- Secondary: Internal services that need authenticated API access
- Admin users: Need to manage API access and view usage statistics

**Guidance**: Understanding users helps define acceptance criteria and testing scenarios.

---

## Q4: What are the acceptance criteria?

**Prompt**: List testable success criteria (3-7 items)

**Example**:
- Users can authenticate with username/password to receive JWT token
- Tokens expire after 24 hours and can be refreshed
- All API endpoints validate JWT tokens (except /auth/login)
- Invalid/expired tokens return appropriate HTTP error codes
- Token includes user ID and role claims
- Rate limiting is enforced per user ID from token

**Guidance**: Make criteria specific, measurable, and testable.

---

## Q5: Any technical constraints?

**Prompt**: List technical requirements, dependencies, or limitations

**Example**:
- Must use existing PostgreSQL database (no new databases)
- Tokens must be stateless (no session storage)
- Should integrate with current Express.js middleware stack
- Must maintain backward compatibility with existing API key system (during migration)
- Performance: Token validation should add <10ms overhead per request

**Guidance**: If PRD exists, reference the tech stack and architecture constraints from there.

---

## Q6: What are the expected deliverables?

**Prompt**: List all outputs this workflow should produce

**Example**:
- Authentication endpoints (/auth/login, /auth/refresh, /auth/logout)
- JWT middleware for token validation
- Database migration for user credentials
- Unit tests (>80% coverage)
- Integration tests for auth flows
- API documentation updates
- Migration guide for existing API key users

**Guidance**: Include code, tests, documentation, and any other artifacts.

---

## Q7: Any dependencies or deadlines?

**Prompt**: Mention prerequisites, blocking work, or time constraints

**Example**:
- Depends on: User management system (already deployed)
- Blocked by: None
- Deadline: MVP needed by end of Q1 for partner integration
- Must coordinate: Frontend team needs auth flow documentation 2 weeks before launch

**Guidance**: Understanding dependencies helps with planning and scheduling.

---

**Note**: These questions will be used to generate your workflow specification. Answer thoughtfully - you can always refine the spec later using the generated `spec.md` file.
