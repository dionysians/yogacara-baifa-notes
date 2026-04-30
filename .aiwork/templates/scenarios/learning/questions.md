# Learning Workflow Questions

> Interactive questions for creating a learning workflow specification

---

## Q1: What are you learning?

**Prompt**: Describe the topic or skill you want to learn (2-3 sentences)

**Example**:
"Learning Rust programming language to build high-performance backend services. Focus on ownership/borrowing system, concurrency, and practical application in web development. Goal is to be productive enough to contribute to our new Rust microservices."

**Guidance**: Be specific about the topic, scope, and depth of learning desired.

---

## Q2: What is your current level and learning goal?

**Prompt**: Describe your starting point and target proficiency

**Example**:
- **Current Level**: Experienced with C++ and Go, understand systems programming concepts, no Rust experience
- **Target Level**: Intermediate Rust developer - can build REST APIs, understand ownership model, write idiomatic code
- **Specific Goals**:
  - Understand ownership, borrowing, and lifetimes
  - Build a REST API with async/await
  - Write unit and integration tests
  - Understand common patterns and idioms
- **Success Indicator**: Can review and contribute to team's Rust codebase confidently

**Guidance**: Set realistic, measurable learning objectives based on your background.

---

## Q3: Why are you learning this?

**Prompt**: Explain the motivation and use case

**Example**:
- **Primary Driver**: Team is adopting Rust for performance-critical services
- **Timeline Pressure**: Need to contribute to Rust codebase in 6 weeks
- **Career Goal**: Expand systems programming expertise
- **Project Need**: Will be implementing authentication service in Rust
- **Long-term**: Want to be proficient in modern systems languages

**Guidance**: Understanding motivation helps prioritize what to learn and how deep to go.

---

## Q4: What learning resources will you use?

**Prompt**: List books, courses, documentation, projects, etc.

**Example**:
- **Primary Resources**:
  - "The Rust Programming Language" book (official)
  - Rust By Example (hands-on exercises)
  - Official Rust documentation
- **Video Courses**:
  - "Ultimate Rust Crash Course" (Udemy)
- **Practice**:
  - Rustlings exercises (interactive learning)
  - LeetCode problems in Rust
  - Build small CLI tools
- **Reference**:
  - Rust standard library docs
  - Tokio documentation (async runtime)
  - Community Discord for questions

**Guidance**: Mix different learning modalities - reading, watching, practicing.

---

## Q5: What is your learning approach?

**Prompt**: Describe how you'll structure your learning

**Example**:
- **Week 1-2**: Fundamentals (syntax, ownership, basic types)
  - Read chapters 1-10 of Rust book
  - Complete Rustlings exercises
  - Daily: 2 hours reading + 1 hour exercises
- **Week 3-4**: Advanced concepts (traits, lifetimes, async)
  - Read chapters 11-20
  - Build small projects (CLI tools)
  - Daily: 1 hour reading + 2 hours coding
- **Week 5-6**: Web development focus
  - Learn Actix-web or Axum framework
  - Build REST API project
  - Study team's codebase
  - Daily: 3 hours project work
- **Study Schedule**: Weekday evenings (3h), weekends (6h/day)

**Guidance**: Balance theory and practice. Set realistic time commitments.

---

## Q6: What projects or exercises will you complete?

**Prompt**: List hands-on projects to reinforce learning

**Example**:
1. **CLI Todo App** (Week 2)
   - File I/O, error handling, basic structs
   - Deliverable: Working CLI tool

2. **Concurrent Web Scraper** (Week 3)
   - Async/await, tokio, HTTP requests
   - Deliverable: Multi-threaded scraper

3. **REST API** (Week 5-6)
   - Web framework (Axum), database (SQLx), JWT auth
   - Deliverable: Complete API with tests

4. **Code Review** (Week 6)
   - Review team's Rust codebase
   - Understand patterns and practices
   - Make small contribution

**Guidance**: Projects should progressively increase in complexity and align with your goal.

---

## Q7: How will you measure progress and success?

**Prompt**: Define how you'll track learning and know when you've succeeded

**Example**:
- **Weekly Checkpoints**:
  - Week 1: Complete chapters 1-5, finish 50% of Rustlings
  - Week 2: Complete chapters 6-10, finish all Rustlings
  - Week 3: Build CLI todo app, start web scraper
  - Week 4: Complete web scraper, start REST API
  - Week 5: 50% of REST API complete
  - Week 6: REST API complete, make first code contribution

- **Success Criteria**:
  - Can explain ownership/borrowing clearly
  - Code passes Clippy linter without issues
  - Can read and understand team's Rust code
  - Successfully merge first Rust PR to team repo
  - Comfortable with async/await patterns

- **Assessment Methods**:
  - Code review from senior Rust developer
  - Self-assessment against learning objectives
  - Ability to debug Rust compiler errors efficiently

**Guidance**: Set measurable milestones. Plan for both self-assessment and external validation.

---

**Note**: These questions will be used to generate your workflow specification. Answer thoughtfully - you can always refine the spec later using the generated `spec.md` file.
