# Research Workflow Questions

> Interactive questions for creating a research workflow specification

---

## Q1: What is your research question or topic?

**Prompt**: Clearly state what you're researching (2-3 sentences)

**Example**:
"Investigating the effectiveness of different machine learning approaches for early detection of fraudulent transactions in real-time payment systems. Comparing traditional rule-based systems, supervised learning (Random Forest, XGBoost), and deep learning (LSTM, Transformer) approaches across accuracy, latency, and false positive rates."

**Guidance**: Frame as a clear, answerable research question. Be specific about scope.

---

## Q2: What is the research objective and hypothesis?

**Prompt**: Describe what you're trying to discover or validate

**Example**:
- **Primary Objective**: Determine which ML approach provides best balance of accuracy and latency for fraud detection
- **Secondary Objectives**:
  - Identify key features most predictive of fraud
  - Understand trade-offs between model complexity and performance
  - Evaluate feasibility of real-time deployment

- **Hypothesis**: Deep learning models will achieve higher accuracy but may have prohibitive latency for real-time systems, while ensemble methods (XGBoost) will offer best accuracy/latency trade-off

**Guidance**: State what you expect to find and why. Good hypotheses are testable.

---

## Q3: Why is this research important?

**Prompt**: Explain the significance and potential impact

**Example**:
- **Business Impact**: Fraud costs company $5M annually; better detection could reduce by 40%
- **Current Gap**: Existing rule-based system has 65% accuracy and 30% false positive rate
- **Decision Support**: Results will inform $500K investment in fraud detection infrastructure
- **Knowledge Contribution**: Limited public research on transformers for fraud detection
- **Timeline**: Need to decide on approach by Q2 for Q3 implementation

**Guidance**: Connect research to real decisions or knowledge gaps.

---

## Q4: What data and resources will you use?

**Prompt**: Describe datasets, tools, and resources needed

**Example**:
- **Primary Dataset**: Historical transaction data (10M transactions, Jan-Dec 2024)
  - Features: amount, merchant, location, time, user history, device
  - Labels: 50K confirmed fraud cases (0.5% fraud rate)
  - Format: PostgreSQL database, exportable to CSV

- **Supplementary Data**:
  - Public fraud detection datasets (Kaggle) for benchmarking
  - Industry fraud pattern databases

- **Tools & Infrastructure**:
  - Python (scikit-learn, XGBoost, PyTorch)
  - GPU instances for deep learning training
  - MLflow for experiment tracking
  - Jupyter notebooks for analysis

- **Expertise**: Access to data science team for consultation

**Guidance**: Be specific about data availability, quality, and access.

---

## Q5: What is your research methodology?

**Prompt**: Describe how you'll conduct the research

**Example**:
**Phase 1: Data Preparation** (Week 1-2)
- Clean and preprocess transaction data
- Feature engineering (time-based, user behavior, transaction patterns)
- Train/validation/test split (60/20/20, time-based)
- Handle class imbalance (SMOTE, class weights)

**Phase 2: Baseline Models** (Week 3)
- Implement rule-based system (current approach)
- Train simple models (Logistic Regression, Decision Trees)
- Establish baseline metrics

**Phase 3: Advanced Models** (Week 4-6)
- Random Forest and XGBoost
- LSTM and Transformer models
- Hyperparameter tuning
- Cross-validation

**Phase 4: Evaluation** (Week 7)
- Compare models on accuracy, precision, recall, F1, AUC
- Measure inference latency (critical for real-time)
- Analyze false positives/negatives
- Feature importance analysis

**Phase 5: Report & Recommendations** (Week 8)
- Document findings
- Make implementation recommendations
- Identify risks and limitations

**Guidance**: Outline clear steps from data to conclusions.

---

## Q6: What are your evaluation criteria?

**Prompt**: How will you measure success and compare approaches?

**Example**:
- **Primary Metrics**:
  - Accuracy: >85% (current: 65%)
  - False Positive Rate: <10% (current: 30%)
  - Inference Latency: <50ms (for real-time deployment)

- **Secondary Metrics**:
  - Precision (reduce false alarms)
  - Recall (catch more fraud)
  - F1 Score (balanced metric)
  - AUC-ROC (overall discrimination)

- **Operational Metrics**:
  - Model training time
  - Model size (deployment constraints)
  - Explainability (for regulatory compliance)
  - Maintenance complexity

- **Trade-off Analysis**:
  - Accuracy vs Latency curve
  - Cost vs Benefit analysis
  - Risk assessment (false negatives more costly than false positives)

**Guidance**: Define success quantitatively. Consider multiple dimensions.

---

## Q7: What are the expected deliverables?

**Prompt**: List all research outputs

**Example**:
1. **Technical Report** (20-30 pages)
   - Methodology description
   - Results and analysis
   - Model comparisons
   - Recommendations

2. **Jupyter Notebooks**
   - Data preprocessing
   - Model training and evaluation
   - Reproducible analysis

3. **Trained Models**
   - Serialized models for top 3 approaches
   - Model performance summaries

4. **Presentation** (15-20 slides)
   - Executive summary for stakeholders
   - Key findings and recommendations

5. **Code Repository**
   - Clean, documented code
   - Requirements and setup instructions
   - Experiment tracking logs

6. **Dataset Documentation**
   - Data dictionary
   - Feature descriptions
   - Known limitations

**Guidance**: Think about different audiences - technical team, executives, future researchers.

---

## Q8: What are the constraints and risks?

**Prompt**: Identify limitations and potential issues

**Example**:
- **Time Constraint**: 8 weeks to complete research (hard deadline for budgeting)
- **Data Constraint**: Only 0.5% fraud rate (class imbalance challenge)
- **Privacy Constraint**: Cannot share raw transaction data externally
- **Compute Constraint**: Limited GPU budget ($500)
- **Risk: Data Quality**: Missing features, labeling errors
- **Risk: Overfitting**: Models may not generalize to future fraud patterns
- **Risk: Concept Drift**: Fraud patterns evolve over time
- **Risk: False Negatives**: Missing fraud is costly ($100-$10K per case)
- **Risk: Deployment Lag**: Research-to-production gap

**Guidance**: Identify what could prevent success or limit findings.

---

**Note**: These questions will be used to generate your workflow specification. Answer thoughtfully - you can always refine the spec later using the generated `spec.md` file.
