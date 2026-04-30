# Data Analysis Scenario Template

> Pre-configured workflow for data analysis projects

## Overview

This template provides a structured workflow for data analysis projects, from data loading through final report generation.

## Typical Workflow Steps

1. **Data Loading & Exploration**
   - Load datasets
   - Check data quality (shape, types, missing values)
   - Initial statistical summary
   - Output: Exploration report

2. **Data Cleaning**
   - Handle missing values
   - Remove duplicates
   - Fix data type issues
   - Output: Clean dataset

3. **Exploratory Data Analysis (EDA)**
   - Distribution analysis
   - Correlation analysis
   - Identify patterns and anomalies
   - Output: EDA visualizations and insights

4. **Feature Engineering** (if needed)
   - Create derived features
   - Transform variables
   - Encode categorical data
   - Output: Engineered dataset

5. **Core Analysis**
   - Statistical tests
   - Segmentation/cohort analysis
   - Trend analysis
   - Output: Analysis results

6. **Visualization & Reporting**
   - Create final charts
   - Compile insights
   - Generate report
   - Output: Final report with recommendations

## When to Use This Template

✅ **Good for:**
- Customer behavior analysis
- Business metrics analysis
- A/B test analysis
- Cohort/retention analysis
- Survey data analysis
- Sales/financial analysis

❌ **Not ideal for:**
- Machine learning model building (use ML template instead)
- Real-time data pipelines (use data-engineering template)
- Simple one-off queries

## How to Use

### 1. Initialize Session

```bash
/session-init data-analysis my-analysis-name
```

### 2. Create Workflow with Template

```bash
/workflow-new exploratory-analysis --template data-analysis
```

This will:
- Create workflow directory
- Pre-fill spec.md with template
- Guide you through customization

### 3. Customize Spec

Answer questions about your specific analysis:
- What data sources?
- What questions to answer?
- What metrics to calculate?
- Who is the audience?

### 4. Generate Plan

```bash
/workflow-plan
```

The template includes suggested steps that you can:
- Use as-is
- Modify for your needs
- Add/remove steps

### 5. Execute Steps

```bash
/step-prepare 1
# Load and explore data...
/step-complete 1 --ai claude

/step-prepare 2
# Clean data...
/step-complete 2 --ai chatgpt

# ... continue through steps
```

## Example: Customer Retention Analysis

See `example-workflow/` for a complete example analyzing customer retention with:
- 500K users
- 2M events
- 6-step workflow
- Multi-AI collaboration
- Complete outputs

## Template Customization

### Modify Steps

Edit `steps.template.yaml` to change default steps:

```yaml
steps:
  - id: 1
    title: "Your custom first step"
    description: "..."
    estimated_hours: 2
```

### Modify Spec Template

Edit `spec.template.md` to change questions and structure.

### Add Domain-Specific Templates

Create sub-templates for specific domains:
- `cohort-analysis/` - Pre-configured for cohort analysis
- `ab-testing/` - A/B test specific workflow
- `survey-analysis/` - Survey data workflow

## AI Tool Recommendations

### Best Tools for Each Step

| Step | Recommended AI | Why |
|------|----------------|-----|
| Data Loading | Claude | Good at structured data understanding |
| Data Cleaning | ChatGPT Code Interpreter | Executes Python directly |
| EDA | ChatGPT Code Interpreter | Creates visualizations inline |
| Analysis | Claude | Strong analytical reasoning |
| Visualization | ChatGPT/Claude | Both handle plotting well |
| Reporting | Claude | Excellent at writing and synthesis |

### Multi-AI Strategy

**Strategy 1: Use Python execution tools for steps 1-3**
- ChatGPT Code Interpreter or Claude with artifacts
- These can run code and show results immediately

**Strategy 2: Use Claude for analytical steps 4-6**
- Better at reasoning about results
- Excellent report writing

## Output Artifacts

Expected outputs from this workflow:

```
.aiwork/workflows/001-analysis/
├── outputs/
│   ├── data/
│   │   ├── raw_data.csv
│   │   ├── clean_data.csv
│   │   └── processed_data.csv
│   │
│   ├── notebooks/
│   │   ├── 01_exploration.ipynb
│   │   ├── 02_cleaning.ipynb
│   │   ├── 03_eda.ipynb
│   │   └── 04_analysis.ipynb
│   │
│   ├── visualizations/
│   │   ├── distribution_plots.png
│   │   ├── correlation_heatmap.png
│   │   ├── trend_analysis.png
│   │   └── key_insights.png
│   │
│   └── reports/
│       ├── exploration_report.md
│       ├── eda_insights.md
│       └── final_report.md
│
├── spec.md
├── plan.md
├── steps.yaml
├── steps.md
└── timeline.md
```

## Common Patterns

### Pattern 1: Iterative EDA

```yaml
# steps.yaml structure
steps:
  - id: 1
    title: "Initial exploration"
  - id: 2
    title: "Clean obvious issues"
  - id: 3
    title: "Deep dive EDA"  # May discover more issues
  - id: 4
    title: "Additional cleaning"  # Based on EDA findings
  - id: 5
    title: "Final analysis"
```

### Pattern 2: Parallel Analysis Tracks

```yaml
steps:
  - id: 1
    title: "Load and clean"
  - id: 2
    title: "Cohort analysis"
    depends_on: [1]
  - id: 3
    title: "Trend analysis"
    depends_on: [1]  # Parallel with step 2
  - id: 4
    title: "Segment analysis"
    depends_on: [1]  # Parallel with steps 2-3
  - id: 5
    title: "Synthesis report"
    depends_on: [2, 3, 4]
```

## Tips & Best Practices

### Data Management

- **Keep raw data immutable**: Never modify original files
- **Save intermediate outputs**: Each step saves processed data
- **Document transformations**: Note all cleaning/engineering steps

### Notebook Organization

- **One notebook per step**: Makes it easy to re-run individual steps
- **Clear cell structure**: Markdown explanations, then code
- **Save key outputs**: Export key dataframes and plots

### Context Packages

For data analysis, context packages should include:
- Data schema (columns, types, sample values)
- Previous findings summary
- Code snippets from previous steps
- Specific analysis questions for this step

### Collaboration

- **Assign coding steps to tools with execution**: ChatGPT Code Interpreter, Claude artifacts
- **Assign analytical steps to Claude**: Better reasoning and synthesis
- **Review in parallel**: Have different AIs review key findings

## Troubleshooting

### Issue: Data too large for AI context

**Solution:**
- Provide data summary instead of full data
- Sample representative subset
- Include schema + statistics + sample rows
- Store data in accessible location, provide path

### Issue: Analysis requires domain knowledge

**Solution:**
- Include domain context in spec.md
- Provide links to relevant resources
- Add domain definitions to context packages

### Issue: Multiple analysis iterations needed

**Solution:**
- This is normal! Add steps as needed
- Use `/workflow-plan --append` to add steps
- Document learnings in timeline

## Resources

- **Example datasets**: See `example-data/`
- **Notebook templates**: See `notebook-templates/`
- **Report templates**: See `report-templates/`

## Version History

- **v1.0** (2025-10-30): Initial data analysis template
  - 6-step standard workflow
  - Customer retention example
  - Multi-AI recommendations
