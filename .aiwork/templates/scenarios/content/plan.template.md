# Technical Plan: {workflow-name}

> Generated: {timestamp}

**Workflow ID**: {workflow-id}
**Type**: Content Creation

---

## Plan Overview

{Brief summary of content creation approach}

---

## Session Alignment

{If SESSION.md exists:}
This workflow aligns with session: {session-name}
- Session type: {type}
- Session objectives: {relevant objectives}

---

## Content Approach

### Content Structure

{Describe the overall organization and flow}

**Example:**
```
Introduction (10%)
  └─ Problem definition, scope, target audience

Core Content (70%)
  ├─ Chapter 1: Fundamentals
  ├─ Chapter 2: Patterns
  ├─ Chapter 3: Implementation
  └─ Chapter 4: Best Practices

Conclusion (10%)
  └─ Summary, next steps, resources

Appendices (10%)
  └─ References, glossary, cheat sheets
```

### Tone & Style

**Writing Style**: {Describe tone and voice}

**Example:**
- Technical but approachable
- Use second person ("you") to engage readers
- Include practical examples and code snippets
- Balance theory with real-world application
- Progressive complexity (start simple, build up)

### Target Metrics

{Define content goals}

**Length**: ~{N} words total
**Reading Level**: {level} (intermediate technical)
**Code Examples**: {count} working examples
**Diagrams**: {count} architecture/flow diagrams
**Estimated Reading Time**: {time} minutes

---

## Content Pipeline

### Research Phase

{Describe research activities}

**Activities:**
1. Review reference materials and documentation
2. Study existing architectures and case studies
3. Identify key patterns and best practices
4. Gather code examples and adapt for context

**Outputs:**
- Research notes
- Source list
- Code example repository

### Drafting Phase

{Describe writing process}

**Process:**
1. Create detailed outline for each section
2. Write first draft (focus on content, not polish)
3. Add code examples and diagrams
4. Internal review for technical accuracy

**Outputs:**
- Draft content in Markdown
- Code examples (tested and runnable)
- Draft diagrams

### Editing Phase

{Describe revision process}

**Activities:**
1. Technical review (accuracy, completeness)
2. Style and clarity editing
3. Code testing and verification
4. Diagram refinement
5. Final proofreading

**Outputs:**
- Polished content
- Verified code examples
- Professional diagrams

### Publishing Phase

{Describe publication process}

**Activities:**
1. Convert to final formats (PDF, HTML, EPUB)
2. Create supplementary materials
3. Set up code repository
4. Prepare publishing assets

**Outputs:**
- Final content in all formats
- Published code repository
- Distribution-ready assets

---

## Implementation Steps

This content project is divided into {N} steps:

1. **Research & Planning** - Gather sources, create detailed outline
2. **Chapter 1 Draft** - Write first chapter with examples
3. **Chapter 2 Draft** - Write second chapter with examples
4. **Chapter 3 Draft** - Write third chapter with examples
5. **Review & Edit** - Technical review and editing
6. **Finalize & Publish** - Format, test, and prepare for publication

Each step:
- Produces concrete deliverables
- Can be reviewed independently
- Maintains consistent voice and quality

---

## Tools & Resources

### Writing Tools

**Primary**: Markdown editor (VS Code, Typora, etc.)
**Diagramming**: Mermaid, Draw.io, or similar
**Code Testing**: Local development environment
**Version Control**: Git for tracking changes

### Reference Materials

{List key references}

**Example:**
- Books: "Building Microservices" by Sam Newman
- Documentation: AWS, GCP microservices guides
- Articles: Martin Fowler's blog on microservices
- Code: Open source microservices examples

### Technical Requirements

{List any technical setup needed}

**Example:**
- Markdown environment for writing
- Code editor for examples (Node.js/Python setup)
- Diagramming tools for architecture visuals
- PDF/EPUB conversion tools

---

## Quality Assurance

### Content Quality Checks

**Technical Accuracy:**
- All code examples tested and runnable
- Technical concepts reviewed by experts
- Current best practices (not outdated patterns)

**Clarity & Readability:**
- Appropriate for target audience level
- Clear explanations and examples
- Logical flow and structure
- Consistent terminology

**Completeness:**
- All planned topics covered
- Code examples for key concepts
- Diagrams for complex architectures
- References and further reading

### Review Process

{Describe review workflow}

**Draft Review** (Week 5):
- Technical accuracy check
- Structure and flow review
- Identify gaps or weak sections

**Final Review** (Week 7):
- Complete technical review
- Copy editing
- Code verification
- Format checking

---

## Output Artifacts

| Artifact | Type | Location | Purpose |
|----------|------|----------|---------|
| Main content | Markdown | outputs/content/ | Source content |
| PDF ebook | PDF | outputs/published/ | Downloadable ebook |
| Web version | HTML | outputs/published/ | Online reading |
| Code examples | Repository | outputs/code/ | Runnable examples |
| Diagrams | PNG/SVG | outputs/diagrams/ | Visual aids |
| Cheat sheet | PDF | outputs/supplementary/ | Quick reference |

---

## Timeline & Milestones

{Based on constraints from spec}

**Week 1-2**: Research and detailed outline
**Week 3-4**: Draft chapters 1-3
**Week 5**: Draft chapters 4-5, first review
**Week 6**: Revisions and editing
**Week 7**: Final review and technical verification
**Week 8**: Format, publish, and distribute

---

## Success Criteria

{From spec}

This plan is successful when:
- [ ] All chapters complete and reviewed
- [ ] Code examples tested and documented
- [ ] Technical review passed
- [ ] Content meets quality standards
- [ ] All formats (PDF, HTML, EPUB) generated
- [ ] Supplementary materials complete
- [ ] Published and distributed

---

## Next Steps

After plan approval:
1. Review steps.yaml (task breakdown)
2. Execute steps sequentially
3. Each step generates context package for AI collaboration
