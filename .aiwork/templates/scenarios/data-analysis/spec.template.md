# Workflow Specification: {workflow-name}

> Data Analysis Workflow

**Workflow ID**: {workflow-id}
**Created**: {date}
**Type**: Data Analysis
**Status**: SPEC

---

## Analysis Overview

### What is this analysis about?

{Brief description of the analysis purpose and scope}

**Example:**
> This analysis examines user retention patterns over the past year to identify which user segments have the highest retention and what behaviors correlate with long-term engagement.

### Why do we need this analysis?

{The business question or problem this analysis addresses}

**Example:**
> The product team needs to understand why user retention dropped 15% in Q3 and which user acquisition channels produce the most engaged users, to inform Q4 marketing budget allocation.

---

## Data Sources

### Primary Data

| Data Source | Description | Format | Size | Location |
|-------------|-------------|--------|------|----------|
| {source-1} | {description} | {CSV/SQL/JSON/etc} | {rows/GB} | {path/URL} |
| {source-2} | {description} | {format} | {size} | {location} |

**Example:**
| Data Source | Description | Format | Size | Location |
|-------------|-------------|--------|------|----------|
| users.csv | User registration data | CSV | 500K rows | data/users.csv |
| events.csv | User activity events | CSV | 2M rows | data/events.csv |
| subscriptions.csv | Subscription history | CSV | 300K rows | data/subscriptions.csv |

### Data Schema

#### Dataset 1: {name}

```
{column-name}: {type} - {description}
{column-name}: {type} - {description}
...
```

**Example:**
```
user_id: integer - Unique user identifier
signup_date: date - Date user registered
cohort: string - Weekly cohort label (YYYY-WW)
channel: string - Acquisition channel (organic, paid, referral)
```

#### Dataset 2: {name}

```
{schema}
```

---

## Analysis Questions

### Primary Questions

1. **{Main question 1}**
   - {Sub-question or clarification}
   - Expected output: {description}

2. **{Main question 2}**
   - {Sub-question}
   - Expected output: {description}

**Example:**
1. **What is the retention rate by cohort over time?**
   - Calculate 7-day, 30-day, and 90-day retention for each weekly cohort
   - Expected output: Retention curve chart, cohort retention table

2. **Which user segments have the highest retention?**
   - Segment by: channel, subscription tier, signup period
   - Expected output: Retention by segment table, comparison chart

### Secondary Questions

- {Additional question 1}
- {Additional question 2}

**Example:**
- Are there seasonal patterns in retention?
- What events correlate with higher retention?

---

## Success Metrics

### Analysis Success Criteria

What makes this analysis successful?

- [ ] {Criterion 1}
- [ ] {Criterion 2}
- [ ] {Criterion 3}

**Example:**
- [ ] Identify top 3 user segments by retention rate
- [ ] Quantify retention difference between channels
- [ ] Provide actionable recommendations with confidence intervals
- [ ] Deliver insights that directly inform budget allocation decision

### Key Metrics to Calculate

| Metric | Definition | Target/Benchmark |
|--------|------------|------------------|
| {metric-1} | {definition} | {target} |
| {metric-2} | {definition} | {target} |

**Example:**
| Metric | Definition | Target/Benchmark |
|--------|------------|------------------|
| 7-day retention | % of cohort active on day 7 | >40% (industry avg) |
| 30-day retention | % of cohort active on day 30 | >20% |
| LTV by channel | Lifetime value by acquisition source | Maximize |

---

## Target Audience

### Who will use this analysis?

- **Primary**: {role/team}
  - Needs: {what they need from the analysis}
  - Technical level: {low/medium/high}

- **Secondary**: {role/team}
  - Needs: {what they need}

**Example:**
- **Primary**: Product Manager & Marketing Lead
  - Needs: Clear retention numbers by channel, actionable recommendations
  - Technical level: Medium (comfortable with basic stats)

- **Secondary**: Executive team
  - Needs: High-level insights and budget recommendations
  - Technical level: Low (need simple visualizations)

### Output Format Preferences

- [ ] Written report (Markdown/PDF)
- [ ] Jupyter notebook (reproducible analysis)
- [ ] Dashboard (interactive)
- [ ] Presentation slides
- [ ] Data export (CSV/Excel)

**Example:**
- [x] Written report with embedded visualizations
- [x] Jupyter notebooks for reproducibility
- [ ] Dashboard (future phase)
- [x] Key data tables as CSV for stakeholders

---

## Constraints & Requirements

### Data Constraints

- {Constraint 1}
- {Constraint 2}

**Example:**
- Data only available from 2024-01-01 onwards
- User privacy: No PII in outputs, aggregate only
- Incomplete data for November (exclude from cohort analysis)

### Technical Constraints

- {Constraint 1}
- {Constraint 2}

**Example:**
- Analysis must run on local machine (no cloud computing)
- Use Python (pandas, matplotlib, seaborn)
- Maximum processing time: 10 minutes per notebook

### Time Constraints

- **Deadline**: {date}
- **Time budget**: {hours} hours total

**Example:**
- **Deadline**: 2025-11-05
- **Time budget**: 12 hours total (2 hours per step)

---

## Expected Outputs

### Deliverables

1. **{Output 1}**
   - Format: {format}
   - Location: {path}
   - Description: {description}

2. **{Output 2}**
   - Format: {format}
   - Location: {path}
   - Description: {description}

**Example:**
1. **Clean Dataset**
   - Format: CSV
   - Location: outputs/data/clean_data.csv
   - Description: Cleaned and validated user+event data

2. **Retention Analysis Report**
   - Format: Markdown with embedded PNG charts
   - Location: outputs/reports/retention_report.md
   - Description: Complete analysis with findings and recommendations

3. **Jupyter Notebooks**
   - Format: .ipynb files
   - Location: outputs/notebooks/
   - Description: Reproducible analysis steps (01_load.ipynb through 06_report.ipynb)

### Visualization Requirements

Specific charts/visualizations needed:

- [ ] {Chart 1 - type and purpose}
- [ ] {Chart 2}
- [ ] {Chart 3}

**Example:**
- [x] Retention curves by cohort (line chart)
- [x] Retention by channel (bar chart with error bars)
- [x] Correlation heatmap (retention vs. user behaviors)
- [x] Cohort retention table (heatmap visualization)

---

## Analysis Approach (High-Level)

### Suggested Methodology

{Brief outline of the analysis approach}

**Example:**
1. **Data Preparation**: Load, validate, clean (handle missing, duplicates)
2. **Cohort Definition**: Group users by weekly signup cohort
3. **Event Aggregation**: Calculate user activity metrics per cohort
4. **Retention Calculation**: Compute D7, D30, D90 return rates
5. **Segmentation Analysis**: Break down by channel, tier, behavior
6. **Insights & Recommendations**: Synthesize findings, provide actionable next steps

### Statistical Methods

{Any specific statistical techniques required}

**Example:**
- Descriptive statistics (mean, median, percentiles)
- Confidence intervals for retention rates
- Chi-square test for segment differences
- Correlation analysis between retention and engagement metrics

---

## Assumptions

{List key assumptions made in this analysis}

**Example:**
- A "retained" user is defined as having at least 1 event in the period
- Cohorts are defined by week (Monday start)
- Users who churned and returned are counted as retained in later periods
- Free trial users are excluded from retention calculations

---

## Risks & Challenges

### Known Challenges

1. **{Challenge 1}**
   - Impact: {impact}
   - Mitigation: {mitigation strategy}

**Example:**
1. **Data Quality Issues**
   - Impact: ~5% of events have missing user_id
   - Mitigation: Filter out invalid events, document impact on sample size

2. **Small Sample Sizes for Some Segments**
   - Impact: Low statistical confidence for niche channels
   - Mitigation: Combine small channels into "Other", note confidence levels

### Open Questions

- {Question 1}
- {Question 2}

**Example:**
- Should we exclude bot traffic? (May need separate analysis to identify)
- How to handle users who signed up but never activated?

---

## Acceptance Criteria

This analysis is considered complete when:

- [ ] {Criterion 1}
- [ ] {Criterion 2}
- [ ] {Criterion 3}
- [ ] {Criterion 4}

**Example:**
- [ ] All 6 steps executed and documented
- [ ] Clean dataset validated (no missing critical fields)
- [ ] Key metrics calculated for all cohorts
- [ ] Visualizations created and saved
- [ ] Final report written with clear recommendations
- [ ] Stakeholders have reviewed and approved findings

---

## References

### Background Reading

- {Link or document 1}
- {Link or document 2}

**Example:**
- [Company Retention Metrics Wiki](internal-link)
- [Previous Q2 Retention Analysis](link)

### Related Work

- {Related analysis or project}

**Example:**
- Q2 2024 user engagement analysis (see .aiwork/archive/002-engagement/)

---

## Notes

{Any additional notes, context, or considerations}

**Example:**
- This analysis follows up on Q2 engagement analysis but focuses specifically on retention
- Marketing team will use findings for Q4 budget planning meeting on 2025-11-08
- If retention patterns are unclear, may need follow-up qualitative research (user interviews)

---

**Spec Status**: DRAFT

**Next Steps**:
1. Review and refine this spec
2. Run `/workflow-plan` to generate technical plan and steps
3. Begin execution with `/step-prepare 1`
