# Technical Plan: {workflow-name}

> Generated: {timestamp}

**Workflow ID**: {workflow-id}
**Type**: Software Development

---

## Plan Overview

{Brief summary of technical approach}

---

## Project Alignment

{If PRD exists:}
### PRD Alignment

This workflow implements module: **{module-name}** from PRD

**From PRD:**
- Priority: {priority}
- Target version: {version}
- Tech stack: {tech-stack}
- Architecture: {architecture-notes}

All technical decisions must align with PRD guidelines.

---

## Technical Approach

### Architecture

{Describe system design and component structure}

**Example:**
```
Client Request → Authentication Middleware → JWT Validation → Route Handler
                      ↓
                Token Generation Service
                      ↓
                User Database
```

### Technology Stack

{List technologies - reference PRD if available}

**Backend**: {framework}
**Database**: {database}
**Authentication**: {auth-method}
**Testing**: {test-frameworks}

**Example:**
- Node.js with Express.js
- PostgreSQL for user storage
- jsonwebtoken library for JWT operations
- Jest for unit tests, Supertest for integration tests

### Key Components

{List main components to build}

1. **Authentication Service**
   - Purpose: Handle login, token generation, token refresh
   - Files: `src/services/auth.service.js`, `src/models/user.model.js`

2. **JWT Middleware**
   - Purpose: Validate tokens on protected routes
   - Files: `src/middleware/jwt.middleware.js`

3. **Auth Routes**
   - Purpose: Expose authentication endpoints
   - Files: `src/routes/auth.routes.js`

---

## Implementation Steps

This workflow is divided into {N} steps:

1. **Setup & Dependencies** - Install libraries, configure environment
2. **Database Schema** - Create user tables and migrations
3. **Auth Service** - Implement login and token generation logic
4. **JWT Middleware** - Build token validation middleware
5. **API Routes** - Create authentication endpoints
6. **Testing** - Write unit and integration tests
7. **Documentation** - Update API docs and create migration guide

Each step:
- Has clear deliverables (code + tests)
- Can be verified independently
- Can be assigned to different AI tools

---

## File Structure

{Show where new/modified files will be}

```
project/
├── src/
│   ├── services/
│   │   └── auth.service.js           (new)
│   ├── middleware/
│   │   └── jwt.middleware.js         (new)
│   ├── routes/
│   │   └── auth.routes.js            (new)
│   ├── models/
│   │   └── user.model.js             (modified)
│   └── config/
│       └── jwt.config.js             (new)
├── tests/
│   ├── unit/
│   │   ├── auth.service.test.js      (new)
│   │   └── jwt.middleware.test.js    (new)
│   └── integration/
│       └── auth.routes.test.js       (new)
├── migrations/
│   └── 001_create_users_table.sql    (new)
└── docs/
    ├── api/auth.md                   (new)
    └── migration-guide.md            (new)
```

---

## Testing Strategy

{Describe how to verify implementation}

**Unit Tests:**
- Auth service: Login validation, token generation, token refresh
- JWT middleware: Token validation, error handling, expired tokens
- Coverage target: >80%

**Integration Tests:**
- Complete auth flows (login → use token → refresh → logout)
- Error scenarios (invalid credentials, expired tokens)
- Rate limiting verification

**Manual Testing:**
- Test with Postman/curl
- Verify token expiration behavior
- Check backward compatibility with API keys

---

## Security Considerations

{Important security aspects to address}

- Password hashing: Use bcrypt with appropriate salt rounds
- Token secrets: Store in environment variables, never commit
- Token expiration: Short-lived access tokens (24h), longer refresh tokens (7d)
- HTTPS only: Enforce secure connections in production
- Input validation: Sanitize all user inputs
- Rate limiting: Prevent brute force attacks on login endpoint

---

## Dependencies

{List external dependencies or prerequisites}

**Required:**
- `jsonwebtoken` - JWT creation and validation
- `bcrypt` - Password hashing
- `express-rate-limit` - Rate limiting middleware

**Existing Systems:**
- User database (PostgreSQL)
- Existing API routes (to be protected)

---

## Backward Compatibility

{If applicable: how to maintain compatibility during migration}

**Migration Strategy:**
- Phase 1: Deploy JWT auth alongside existing API key system
- Phase 2: Update documentation and notify API consumers
- Phase 3: Deprecate API keys after 90-day transition period

**Compatibility Layer:**
- Support both JWT and API key authentication during transition
- Log usage of deprecated API key system
- Provide migration utilities for existing users

---

## Success Criteria

{From spec}

This plan is successful when:
- [ ] All acceptance criteria met
- [ ] Test coverage >80%
- [ ] API documentation complete
- [ ] Security review passed
- [ ] Migration guide available
- [ ] No breaking changes for existing API key users (during transition)

---

## Next Steps

After plan approval:
1. Review steps.yaml (task breakdown)
2. Execute steps sequentially
3. Each step generates context package for AI collaboration
