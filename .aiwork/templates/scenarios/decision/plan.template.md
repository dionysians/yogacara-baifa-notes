# Technical Plan: {workflow-name}

> Generated: {timestamp}

**Workflow ID**: {workflow-id}
**Type**: Decision Making

---

## Plan Overview

{Brief summary of decision-making approach}

---

## Session Alignment

{If SESSION.md exists:}
This workflow aligns with session: {session-name}
- Session type: {type}
- Session objectives: {relevant objectives}

---

## Decision Context

### The Decision

{Clearly restate the decision to be made}

### Options Under Consideration

{List all options being evaluated}

1. **Option A**: {description}
2. **Option B**: {description}
3. **Option C**: {description}
4. **{Additional options}**

### Decision Criteria

{List evaluation criteria with weights}

| Criterion | Weight | Description |
|-----------|--------|-------------|
| {Criterion 1} | Critical | {Why it matters} |
| {Criterion 2} | Important | {Why it matters} |
| {Criterion 3} | Nice-to-have | {Why it matters} |

---

## Decision-Making Approach

### Framework

{Describe decision-making methodology}

**Example:**
We'll use a structured decision matrix approach:
1. Define criteria and weights
2. Research each option thoroughly
3. Score options against criteria (1-10 scale)
4. Calculate weighted scores
5. Validate with stakeholder input
6. Make recommendation with confidence level

### Research Strategy

{Describe how information will be gathered}

**Primary Research:**
- Benchmarking and performance testing
- Cost analysis and TCO calculations
- Reference checks with existing users

**Secondary Research:**
- Documentation and technical reviews
- Industry analyst reports
- Community feedback and case studies

**Validation:**
- Proof of concept for top options
- Stakeholder interviews
- Risk assessment workshops

---

## Implementation Steps

This decision workflow is divided into {N} steps:

1. **Define & Structure** - Clarify decision, options, and criteria
2. **Research & Gather Data** - Collect information for each option
3. **Analysis** - Evaluate options against criteria
4. **Stakeholder Review** - Present findings and gather input
5. **Final Decision** - Make recommendation and document rationale

Each step:
- Produces concrete deliverables
- Can be reviewed by stakeholders
- Builds toward informed decision

---

## Research Plan

### For Each Option

{What needs to be researched for each alternative}

**Technical Evaluation:**
- Architecture fit and integration requirements
- Performance characteristics and limitations
- Scalability and reliability track record

**Operational Evaluation:**
- Deployment and maintenance complexity
- Monitoring and troubleshooting capabilities
- Backup and disaster recovery

**Business Evaluation:**
- Total cost of ownership (3-year projection)
- Vendor stability and ecosystem
- Team training and ramp-up time

**Risk Evaluation:**
- Known issues and limitations
- Migration difficulty if we need to change later
- Dependency and lock-in concerns

### Data Collection Methods

{How information will be gathered}

1. **Benchmarking**: Load test with realistic workload (if applicable)
2. **Interviews**: Talk to {N} teams using each technology
3. **Cost Analysis**: Calculate detailed TCO models
4. **Documentation Review**: Study architecture and operational docs
5. **POC Development**: Build small prototypes for top options

---

## Analysis Framework

### Decision Matrix

{Show how options will be scored}

| Criterion | Weight | Option A | Option B | Option C |
|-----------|--------|----------|----------|----------|
| {Criterion 1} | 30% | TBD | TBD | TBD |
| {Criterion 2} | 25% | TBD | TBD | TBD |
| {Criterion 3} | 20% | TBD | TBD | TBD |
| {Criterion 4} | 15% | TBD | TBD | TBD |
| {Criterion 5} | 10% | TBD | TBD | TBD |
| **Weighted Score** | | TBD | TBD | TBD |

Scoring: 1-10 scale, where 10 is best performance on that criterion

### Risk Assessment

{For each option, identify key risks}

**Option A Risks:**
- {Risk 1}: {Severity} - {Mitigation}
- {Risk 2}: {Severity} - {Mitigation}

**Option B Risks:**
- {Risk 1}: {Severity} - {Mitigation}
- {Risk 2}: {Severity} - {Mitigation}

---

## Stakeholder Engagement

### Communication Plan

{How stakeholders will be involved}

**Week 1**: Kick-off meeting with key stakeholders
- Present decision context and criteria
- Gather initial input and concerns

**Week 3**: Mid-point review
- Share preliminary findings
- Validate assumptions and criteria

**Week 5**: Final presentation
- Present recommendation with full analysis
- Address questions and concerns
- Seek approval or feedback for revision

### Stakeholder Input

{How to gather and incorporate stakeholder feedback}

- Interviews with engineering team about preferences and concerns
- Survey DevOps team about operational preferences
- Review session with Finance on cost implications
- Technical review with architects on integration concerns

---

## Output Artifacts

| Artifact | Type | Location | Purpose |
|----------|------|----------|---------|
| Decision matrix | Spreadsheet | outputs/analysis/ | Structured scoring |
| Research summary | Markdown | outputs/research/ | Findings for each option |
| Cost analysis | Spreadsheet | outputs/analysis/ | TCO calculations |
| Risk assessment | Markdown | outputs/analysis/ | Risk matrix and mitigations |
| Final recommendation | Document | outputs/recommendation/ | Decision rationale |
| Presentation | Slides | outputs/presentation/ | Stakeholder presentation |

---

## Decision Documentation

### Final Recommendation Format

{Structure for decision document}

**Executive Summary**: One-page recommendation with key points

**Detailed Analysis**:
1. Decision context and background
2. Options considered
3. Research methodology
4. Evaluation results (decision matrix)
5. Risk assessment
6. Recommendation with rationale
7. Implementation considerations
8. Dissenting opinions (if any)

**Appendices**:
- Detailed research notes
- Cost calculations
- Reference checks
- Stakeholder feedback

---

## Timeline & Milestones

{Based on constraints from spec}

| Week | Milestone | Deliverables |
|------|-----------|--------------|
| 1-2 | Research Phase | Research summaries for each option |
| 3 | Analysis Phase | Decision matrix, risk assessment |
| 4 | Validation Phase | Stakeholder feedback, revised analysis |
| 5 | Decision Phase | Final recommendation document |
| 6 | Communication | Present decision, implementation plan |

**Hard Deadline**: {deadline from spec}

---

## Success Criteria

{From spec}

This decision-making process is successful when:
- [ ] All options thoroughly researched
- [ ] Decision criteria applied objectively
- [ ] Key stakeholders consulted and input incorporated
- [ ] Risks identified and mitigations proposed
- [ ] Decision well-documented with clear rationale
- [ ] Team aligned and ready to implement
- [ ] Confidence level in decision: {High/Medium/Low}

---

## Confidence & Reversibility

### Decision Confidence

{How confident can we be in this decision?}

**Factors increasing confidence:**
- Objective data available
- Clear criteria and weights
- Stakeholder alignment
- Low uncertainty in requirements

**Factors decreasing confidence:**
- Limited real-world data
- Rapidly changing technology landscape
- Uncertain future requirements

### Reversibility Assessment

{How hard is it to change the decision later?}

**High Reversibility** (easy to change): Proceed with confidence
**Medium Reversibility**: Build in flexibility, regular reviews
**Low Reversibility**: Extra validation, pilot programs, contingency plans

---

## Next Steps

After plan approval:
1. Review steps.yaml (task breakdown)
2. Execute steps sequentially
3. Each step generates context package for AI collaboration
4. Final step produces recommendation document for stakeholders
