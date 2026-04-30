# Decision Making Workflow Questions

> Interactive questions for creating a decision-making workflow specification

---

## Q1: What decision are you making?

**Prompt**: Clearly state the decision you need to make (2-3 sentences)

**Example**:
"Choosing a database technology for our new microservices platform. Need to decide between PostgreSQL, MongoDB, and Cassandra based on our scalability requirements, team expertise, and operational complexity."

**Guidance**: Frame the decision clearly. What exactly needs to be decided?

---

## Q2: What are the options being considered?

**Prompt**: List all alternatives under consideration

**Example**:
1. **PostgreSQL**
   - Traditional relational database
   - Strong ACID guarantees
   - Familiar to team

2. **MongoDB**
   - Document database
   - Flexible schema
   - Good developer experience

3. **Cassandra**
   - Distributed wide-column store
   - High availability
   - Linear scalability

4. **Hybrid Approach**
   - PostgreSQL for transactional data
   - MongoDB for analytics/logs

**Guidance**: Include all viable options, even if some seem less likely. Include "do nothing" if it's an option.

---

## Q3: What are the decision criteria?

**Prompt**: List factors that will influence the decision

**Example**:
- **Scalability**: Can it handle 10M+ records and 10K+ concurrent users?
- **Performance**: Query latency under 100ms for 95th percentile
- **Team Expertise**: How much training/ramp-up time needed?
- **Operational Complexity**: Ease of deployment, monitoring, backup
- **Cost**: Total cost of ownership (licensing, hosting, maintenance)
- **Data Model Fit**: How well does it match our domain model?
- **Ecosystem**: Library support, community, tooling
- **Risk**: Maturity, vendor lock-in, migration difficulty

**Weight priorities:**
- Critical: Scalability, Performance, Cost
- Important: Team Expertise, Data Model Fit
- Nice-to-have: Ecosystem richness

**Guidance**: List both technical and non-technical factors. Consider weighting criteria by importance.

---

## Q4: What information do you need to gather?

**Prompt**: Describe research, data, or analysis needed to make the decision

**Example**:
- **Benchmarking**: Load test each database with realistic workload
- **Cost Analysis**: Calculate 3-year TCO for each option
- **Team Assessment**: Survey team about experience and preferences
- **Architecture Review**: Evaluate fit with existing systems
- **Reference Checks**: Talk to companies using each technology at scale
- **Proof of Concept**: Build small prototype with top 2 options
- **Documentation Review**: Study operational requirements and limitations

**Guidance**: Be specific about what research will help inform the decision.

---

## Q5: Who are the stakeholders?

**Prompt**: List who will be affected by or involved in the decision

**Example**:
- **Decision Maker**: CTO (final approval)
- **Key Stakeholders**:
  - Engineering Lead (implementation responsibility)
  - DevOps Team (operational impact)
  - Product Manager (feature timeline impact)
- **Consulted**:
  - Backend Engineers (daily usage)
  - Finance (budget approval)
- **Informed**:
  - Executive team (strategic alignment)
  - QA team (testing impact)

**Guidance**: Identify who decides, who must buy in, who should be consulted, and who needs to be informed.

---

## Q6: What is the decision timeline?

**Prompt**: When does the decision need to be made, and what are the key milestones?

**Example**:
- **Week 1-2**: Research and data gathering
- **Week 3**: Initial analysis and option elimination
- **Week 4**: Deep dive on top 2-3 options
- **Week 5**: Stakeholder review and feedback
- **Week 6**: Final decision and documentation
- **Hard Deadline**: Decision by end of Q1 (impacts Q2 roadmap)

**Guidance**: Set realistic timelines with milestones. Identify hard deadlines and their drivers.

---

## Q7: What are the constraints and risks?

**Prompt**: List limitations, risks, or considerations that constrain the decision

**Example**:
- **Budget Constraint**: Total 3-year cost must be under $150K
- **Time Constraint**: Must choose and implement before Q2 launch
- **Technical Constraint**: Must integrate with existing Java services
- **Risk: Wrong Choice**: Difficult to migrate later if we choose incorrectly
- **Risk: Analysis Paralysis**: Too much research could delay decision
- **Risk: Team Resistance**: Team may resist unfamiliar technology
- **Constraint: Compliance**: Must meet GDPR/SOC2 requirements

**Guidance**: Identify what limits options and what could go wrong.

---

**Note**: These questions will be used to generate your workflow specification. Answer thoughtfully - you can always refine the spec later using the generated `spec.md` file.
