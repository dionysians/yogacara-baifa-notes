# Content Creation Workflow Questions

> Interactive questions for creating a content creation workflow specification

---

## Q1: What content are you creating?

**Prompt**: Describe the content piece (2-3 sentences)

**Example**:
"Creating a comprehensive guide on microservices architecture for mid-level backend developers. This will be a 5-chapter technical ebook covering patterns, best practices, and real-world implementation examples with code samples."

**Guidance**: Be specific about the type, scope, and format of content.

---

## Q2: What is the purpose and audience?

**Prompt**: Explain the goal and target readers

**Example**:
- **Purpose**: Educate backend developers on microservices architecture to improve system design decisions
- **Primary Audience**: Mid-level backend engineers (2-5 years experience)
- **Secondary Audience**: Tech leads evaluating microservices adoption
- **Technical Level**: Intermediate - assumes knowledge of web APIs, databases, basic distributed systems
- **Outcome**: Readers can design and implement a basic microservices architecture

**Guidance**: Understanding audience shapes tone, depth, and presentation style.

---

## Q3: What is the planned structure?

**Prompt**: Outline sections, chapters, or main topics

**Example**:
1. **Introduction** - What are microservices and when to use them
2. **Architecture Patterns** - Common patterns (API Gateway, Service Discovery, etc.)
3. **Communication** - Sync vs Async, REST vs gRPC, Message Queues
4. **Data Management** - Database per service, distributed transactions
5. **Observability** - Logging, monitoring, tracing in distributed systems

Each chapter: ~3000 words, code examples, diagrams

**Guidance**: Break down content into logical sections with estimated scope.

---

## Q4: What research or references do you need?

**Prompt**: List sources, references, and research required

**Example**:
- **Technical Resources**: AWS/GCP microservices documentation, Martin Fowler's microservices guide
- **Books**: "Building Microservices" (Sam Newman), "Microservices Patterns" (Chris Richardson)
- **Code Examples**: Will create original examples in Node.js and Python
- **Case Studies**: Netflix, Uber, Amazon microservices architectures
- **Tools to Cover**: Docker, Kubernetes, RabbitMQ, gRPC

**Guidance**: Identify what research needs to happen before writing.

---

## Q5: What is the desired output format?

**Prompt**: Specify format, length, and deliverables

**Example**:
- **Primary Format**: Markdown (for flexibility)
- **Final Formats**: PDF (for ebook), HTML (for web), EPUB (for e-readers)
- **Length**: ~15,000 words total (5 chapters x ~3000 words)
- **Supplementary Materials**:
  - Code examples repository (GitHub)
  - Architecture diagrams (Mermaid or PNG)
  - Quick reference cheat sheet (1-page PDF)
- **Style Guide**: Technical but approachable, use code examples liberally

**Guidance**: Define all deliverables and formats upfront.

---

## Q6: What are the key success criteria?

**Prompt**: Define what makes this content successful

**Example**:
- Content is technically accurate (reviewed by senior engineers)
- Code examples are tested and runnable
- All major microservices patterns covered
- Appropriate for target audience (not too basic, not too advanced)
- Includes practical implementation guidance, not just theory
- Professional diagrams and formatting
- Complete within estimated timeline

**Guidance**: Include quality standards, technical accuracy, and business goals.

---

## Q7: Any constraints or deadlines?

**Prompt**: Mention time limits, resource constraints, or other limitations

**Example**:
- **Deadline**: Complete draft in 6 weeks, final version in 8 weeks
- **Review Process**: Technical review by 2 senior engineers (week 7)
- **Tools Available**: Standard dev environment, diagramming tools
- **Constraints**: No access to proprietary company architectures for examples
- **Publishing**: Will be published under company blog and as downloadable ebook

**Guidance**: Understanding constraints helps scope the work appropriately.

---

**Note**: These questions will be used to generate your workflow specification. Answer thoughtfully - you can always refine the spec later using the generated `spec.md` file.
