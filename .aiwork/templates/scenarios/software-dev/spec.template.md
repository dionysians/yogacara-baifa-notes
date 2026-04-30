# Workflow Specification: {workflow-name}

> Software Development Workflow

**Workflow ID**: {workflow-id}
**Created**: {date}
**Type**: Software Development
**Status**: SPEC

---

## PRD Alignment

{if-prd-exists}
**Related PRD Module**: {module-name}
**PRD Priority**: {priority} (MVP / v1.0 / v2.0)
**Target Version**: {version}

See `.aiwork/PRD.md` for:
- Project tech stack
- System architecture
- Technical constraints
- Non-functional requirements
{endif}

---

## What

> A clear, concise description of what this feature/workflow does.

{feature-description}

**Example:**
> This feature implements JWT-based authentication for the API, allowing users to securely sign up, log in, and access protected endpoints.

---

## Why

> The business value or problem this feature solves.

{feature-rationale}

**Example:**
> Currently, the API has no authentication, making it impossible to:
> - Track usage per user
> - Implement user-specific features
> - Secure sensitive endpoints
> - Meet security compliance requirements
>
> This feature enables user management and secures the API.

---

## Who

> Target users or stakeholders.

### User Personas

- **{persona-1}**: {description}
- **{persona-2}**: {description}

**Example:**
- **API Consumers**: External developers building applications using our API
- **Internal Services**: Other microservices that need to authenticate requests
- **Admin Users**: Team members who need access to admin endpoints

### User Stories

- As a {user-type}, I want to {action}, so that {benefit}
- As a {user-type}, I want to {action}, so that {benefit}

**Example:**
- As an API consumer, I want to register an account, so that I can access protected endpoints
- As an API consumer, I want to log in and receive a token, so that I can authenticate my requests
- As a developer, I want tokens to expire after 24 hours, so that the system remains secure
- As an internal service, I want to verify tokens, so that I can trust incoming requests

---

## Acceptance Criteria

> Testable conditions that must be met for this feature to be considered complete.

- [ ] {criterion-1}
- [ ] {criterion-2}
- [ ] {criterion-3}
- [ ] {criterion-4}
- [ ] {criterion-5}

**Example:**
- [ ] Users can register with email and password
- [ ] Users can log in and receive a valid JWT token
- [ ] Protected endpoints reject requests without valid token
- [ ] Protected endpoints accept requests with valid token
- [ ] Tokens expire after 24 hours
- [ ] Token refresh mechanism works
- [ ] Password hashing uses bcrypt (not plain text)
- [ ] All endpoints return appropriate HTTP status codes
- [ ] API documentation updated
- [ ] Unit tests cover 80%+ of code
- [ ] Integration tests cover all endpoints

---

## Scope

### In Scope

{List what's included in this workflow}

**Example:**
- User registration (POST /api/auth/register)
- User login (POST /api/auth/login)
- Token verification middleware
- Token refresh endpoint (POST /api/auth/refresh)
- Password hashing and validation
- JWT token generation and verification
- Basic user profile endpoint (GET /api/users/me)
- Unit and integration tests
- API documentation

### Out of Scope

{List what's NOT included - may be future work}

**Example:**
- OAuth/SSO integration (v2.0 feature)
- Password reset via email (separate workflow)
- Two-factor authentication (v2.0 feature)
- Role-based access control (separate workflow)
- User profile editing (separate workflow)
- Rate limiting (separate workflow)

---

## Technical Approach (High-Level)

{if-prd-exists}
### Tech Stack (from PRD)

**Backend**: {tech-stack from PRD}
**Database**: {database from PRD}
**Authentication**: {auth method from PRD}

{endif}

### Components to Build

1. **{Component 1}**
   - Purpose: {purpose}
   - Files: {file-list}

2. **{Component 2}**
   - Purpose: {purpose}
   - Files: {file-list}

**Example:**
1. **User Model**
   - Purpose: Database schema and ORM model for users
   - Files: `src/models/User.ts`

2. **Auth Service**
   - Purpose: Business logic for registration, login, token generation
   - Files: `src/services/AuthService.ts`

3. **Auth Controller**
   - Purpose: API endpoints for authentication
   - Files: `src/controllers/AuthController.ts`

4. **Auth Middleware**
   - Purpose: Verify JWT tokens for protected routes
   - Files: `src/middleware/auth.ts`

### API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| {method} | {path} | {description} | {yes/no} |

**Example:**
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | /api/auth/register | Register new user | No |
| POST | /api/auth/login | Login and get token | No |
| POST | /api/auth/refresh | Refresh expired token | Yes (refresh token) |
| GET | /api/users/me | Get current user profile | Yes |

---

## Success Metrics

> How will we measure if this feature is successful?

- {metric-1}: {target}
- {metric-2}: {target}

**Example:**
- Registration success rate: >95%
- Login response time: <200ms
- Token validation overhead: <10ms per request
- Test coverage: >80%
- Zero critical security vulnerabilities

---

## Dependencies

### Internal Dependencies

- {dependency-1}: {description}
- {dependency-2}: {description}

**Example:**
- Database setup: PostgreSQL with users table must exist
- Configuration: Environment variables for JWT secret

### External Dependencies

- {library-1}: {purpose}
- {library-2}: {purpose}

**Example:**
- jsonwebtoken: JWT token generation and verification
- bcrypt: Password hashing
- validator: Email validation

---

## Constraints & Assumptions

### Technical Constraints

{if-prd-exists}
**From PRD:**
- {constraint from PRD}
- {constraint from PRD}

{endif}

**Feature-Specific:**
- {constraint-1}
- {constraint-2}

**Example:**
**From PRD:**
- Must use PostgreSQL (existing project database)
- Must follow RESTful API conventions
- Must achieve <200ms API response time

**Feature-Specific:**
- Tokens must be stateless (JWT, not session-based)
- No external authentication service (build in-house)
- Must work with existing API structure

### Assumptions

- {assumption-1}
- {assumption-2}

**Example:**
- Users will provide valid email addresses
- Email uniqueness is sufficient for user identification
- 24-hour token expiry is acceptable for our use case
- HTTPS is handled at infrastructure level

---

## Security Considerations

{Important for software features}

- {security-concern-1}: {mitigation}
- {security-concern-2}: {mitigation}

**Example:**
- **Password storage**: Hash with bcrypt (cost factor 10), never store plain text
- **Token security**: Use strong secret key (256-bit), stored in environment variables
- **SQL injection**: Use ORM parameterized queries, validate all inputs
- **Rate limiting**: Implement in separate workflow (noted in out of scope)
- **HTTPS**: Required for production (infrastructure concern)

---

## Data Model

{If this feature involves database changes}

### New Tables

**{table-name}**
```sql
{schema}
```

**Example:**
**users**
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

### Migrations

- {migration-description}

**Example:**
- Migration: `001_create_users_table.sql`
- Rollback: `001_create_users_table.down.sql`

---

## Testing Strategy

### Unit Tests

{What to test at unit level}

**Example:**
- AuthService.register(): Creates user, hashes password, returns user object
- AuthService.login(): Validates credentials, generates token
- AuthService.verifyToken(): Validates JWT, returns decoded payload
- User model validations

### Integration Tests

{What to test end-to-end}

**Example:**
- POST /api/auth/register → Creates user in database
- POST /api/auth/login → Returns valid token
- GET /api/users/me with valid token → Returns user profile
- GET /api/users/me without token → Returns 401
- GET /api/users/me with expired token → Returns 401

### Manual Testing Scenarios

{What to test manually}

**Example:**
1. Register user via Postman
2. Login and receive token
3. Use token to access protected endpoint
4. Wait for token to expire, verify rejection
5. Test with invalid credentials

---

## Documentation Requirements

{What documentation is needed}

**Example:**
- API documentation (OpenAPI/Swagger spec)
- Authentication flow diagram
- Code comments for public methods
- README section on authentication
- Example requests and responses

---

## Risks & Challenges

{Potential issues and how to address them}

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| {risk-1} | {High/Med/Low} | {High/Med/Low} | {mitigation} |

**Example:**
| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Token secret leaked | High | Low | Use strong secret, rotate regularly, store in env vars |
| Password hashing too slow | Medium | Medium | Use appropriate bcrypt cost factor (10), async operations |
| Token size too large | Low | Low | Include only necessary claims in JWT payload |

---

## Open Questions

{Questions that need to be resolved}

- [ ] {question-1}
- [ ] {question-2}

**Example:**
- [ ] Should we implement refresh tokens, or rely on 24-hour expiry?
- [ ] Do we need email verification for new accounts? (Answer: Not in MVP)
- [ ] What should happen to expired tokens? (Answer: Return 401, client must re-authenticate)

---

## References

> Links to related documents, designs, or discussions.

{if-prd-exists}
- Project PRD: `.aiwork/PRD.md`
{endif}
- {external-reference-1}
- {external-reference-2}

**Example:**
- Project PRD: `.aiwork/PRD.md` (Tech stack, architecture)
- JWT Best Practices: https://auth0.com/docs/secure/tokens/json-web-tokens
- bcrypt documentation: https://github.com/kelektiv/node.bcrypt.js

---

## Related Workflows

{Other workflows that relate to this one}

**Example:**
- **Depends on**: Database setup workflow (if not already complete)
- **Blocks**: User profile management workflow (needs auth first)
- **Related**: Password reset workflow (future)

---

## Acceptance Checklist

This workflow is considered complete when:

- [ ] All acceptance criteria met
- [ ] All API endpoints implemented and working
- [ ] All tests written and passing
- [ ] Security review completed
- [ ] Documentation updated
- [ ] Code reviewed
- [ ] Deployed to staging and verified
- [ ] Ready for production deployment

---

**Spec Status**: DRAFT

**Next Steps**:
1. Review and refine this spec
2. Get stakeholder approval (if needed)
3. Run `/workflow-plan` to generate technical plan and steps
4. Begin execution with `/step-prepare 1`

---

**Created**: {date}
**Status**: Draft
**Owner**: {ai-tool or team-member}
