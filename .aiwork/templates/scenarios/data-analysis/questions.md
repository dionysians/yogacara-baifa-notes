# Data Analysis Workflow Questions

> Interactive questions for creating a data analysis workflow specification

---

## Q1: What is this analysis about?

**Prompt**: Provide a brief description of what you're analyzing (2-3 sentences)

**Example**:
"Analyzing user retention patterns across different acquisition channels to identify which channels bring the highest-quality users and optimize marketing budget allocation."

**Guidance**: Be specific about the business question or problem you're trying to solve.

---

## Q2: What are the primary research questions?

**Prompt**: List 2-5 key questions this analysis should answer

**Example**:
- What is the 7-day, 30-day, and 90-day retention rate by acquisition channel?
- Which user cohorts (by signup week) have the highest retention?
- Are there significant differences in retention between user segments?
- What user behaviors correlate with higher retention?

**Guidance**: Make questions specific and measurable. These will guide your entire analysis.

---

## Q3: What data sources will you use?

**Prompt**: Describe your datasets including name, format, size, and location

**Example**:
- `users.csv` - User registration data (500K rows, 15 columns) - `/data/users.csv`
- `events.csv` - User activity events (2M rows, 8 columns) - `/data/events.csv`
- Schema: user_id, signup_date, channel, event_type, event_date

**Guidance**: Include enough detail so AI tools know what data is available and how to access it.

---

## Q4: Who is the target audience for this analysis?

**Prompt**: Describe stakeholders and their technical level

**Example**:
- Primary: Product Manager (non-technical, needs executive summary)
- Secondary: Marketing Lead (semi-technical, wants detailed channel insights)
- Technical Level: Mix of technical and non-technical

**Guidance**: This affects how results should be presented and what level of detail to include.

---

## Q5: What are the key success criteria?

**Prompt**: Define what makes this analysis successful

**Example**:
- All research questions answered with statistical confidence
- Clear recommendations for marketing budget reallocation
- Visualizations suitable for executive presentation
- Analysis reproducible by other team members

**Guidance**: Be specific about deliverables, quality standards, and business impact.

---

## Q6: What are the expected deliverables?

**Prompt**: List all outputs this analysis should produce

**Example**:
- Executive summary (1 page PDF)
- Detailed analysis report (Markdown)
- Jupyter notebooks (reproducible analysis)
- Visualizations (PNG charts for presentation)
- Retention metrics CSV (for dashboard integration)

**Guidance**: Think about different audiences and their needs.

---

## Q7: Any constraints or deadlines?

**Prompt**: Mention time limits, data constraints, technical constraints, or other limitations

**Example**:
- Deadline: Analysis needed by end of Q1 for budget planning
- Data limitation: Only have data from last 12 months
- Technical: Must run on laptop (no cloud GPU required)
- Privacy: Cannot share raw user data externally

**Guidance**: Understanding constraints helps plan the analysis scope and approach.

---

**Note**: These questions will be used to generate your workflow specification. Answer thoughtfully - you can always refine the spec later using the generated `spec.md` file.
