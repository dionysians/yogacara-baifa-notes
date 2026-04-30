# Technical Plan: {workflow-name}

> Generated: {timestamp}

**Workflow ID**: {workflow-id}
**Type**: Data Analysis

---

## Plan Overview

{Brief summary of the technical approach}

---

## Session Alignment

{If SESSION.md exists:}
This workflow aligns with session: {session-name}
- Session type: {type}
- Session objectives: {relevant objectives}

---

## Analysis Approach

### Data Pipeline

{Describe the data flow: sources → processing → outputs}

**Example:**
1. **Input**: users.csv (500K rows), events.csv (2M rows)
2. **Processing**: Clean → Join → Aggregate → Calculate metrics
3. **Output**: Retention metrics CSV, visualizations, report

### Tools & Technologies

**Programming Language**: Python
**Key Libraries**:
- pandas (data manipulation)
- matplotlib/seaborn (visualization)
- scipy/statsmodels (statistics)

**Environment**: Jupyter notebooks (for reproducibility)

### Statistical Methods

{Describe analytical methods to be used}

**Example:**
- Cohort analysis (group by signup week)
- Retention calculation (D7, D30, D90 return rates)
- Segmentation analysis (by channel, behavior)
- Statistical significance testing (chi-square for segment differences)

---

## Implementation Steps

{Describe how work will be broken down}

This analysis is divided into {N} steps:

1. **Data Loading & Exploration** - Understand data structure and quality
2. **Data Cleaning** - Prepare clean dataset
3. **EDA** - Exploratory analysis and visualization
4. **Core Analysis** - Calculate key metrics and answer research questions
5. **Reporting** - Compile findings and recommendations

Each step:
- Produces a Jupyter notebook (01_loading.ipynb, 02_cleaning.ipynb, etc.)
- Saves intermediate outputs
- Can be executed by any AI tool with Python/Jupyter support

---

## Data Quality Considerations

{Note any data quality concerns from spec}

**Example:**
- ~5% of events have missing user_id (will be filtered)
- Small sample size for niche channels (will combine into "Other")
- Data only available from 2024-01-01 (will note in limitations)

---

## Output Artifacts

| Artifact | Type | Location | Purpose |
|----------|------|----------|---------|
| Clean dataset | CSV | outputs/data/clean_data.csv | Validated data ready for analysis |
| Notebooks | Jupyter | outputs/notebooks/*.ipynb | Reproducible analysis steps |
| Visualizations | PNG | outputs/visualizations/*.png | Charts for report |
| Final report | Markdown | outputs/reports/final_report.md | Insights and recommendations |

---

## Validation & Testing

How to verify each step:
- Data loading: Check row counts, data types
- Cleaning: Validate no critical missing values, check distributions
- Analysis: Verify metric calculations, check statistical assumptions
- Visualizations: Ensure clarity and accuracy

---

## Risks & Mitigations

{From spec or discovered during planning}

| Risk | Impact | Mitigation |
|------|--------|------------|
| Missing data | May reduce sample size | Document impact, use appropriate methods |
| Small segments | Low statistical power | Combine small groups, note confidence |
| Data freshness | May not reflect recent changes | Note analysis date range in report |

---

## Success Criteria

{From spec}

This plan is successful when:
- [ ] All research questions answered
- [ ] Key metrics calculated with confidence intervals
- [ ] Visualizations created
- [ ] Final report delivered to stakeholders
- [ ] Analysis is reproducible

---

## Next Steps

After plan approval:
1. Review steps.yaml (task breakdown)
2. Execute steps sequentially
3. Each step generates context package for AI collaboration
