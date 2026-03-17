# Credit Risk Portfolio Analysis

An end-to-end portfolio project that analyzes borrower risk, default behavior, and loan segmentation using **Python, SQL, and Power BI-ready outputs**.

## Business problem
Lenders need to understand which borrower segments are more likely to default so they can reduce portfolio losses and improve approval quality.

## Dataset
This repository includes a **synthetic lending dataset** (`data/raw/loan_data.csv`) that is safe to publish on GitHub.

## Tools used
- Python
- SQL
- Power BI
- Pandas / NumPy / Matplotlib

## Project workflow
1. Load and validate the loan dataset
2. Clean and enrich variables such as `default_flag`
3. Analyze default behavior by grade, DTI, utilization, and purpose
4. Export summary tables for dashboarding
5. Present insights and business recommendations

## Key questions answered
- Which loan grades have the highest default rate?
- How does debt-to-income ratio affect default?
- Which borrower segments should be monitored more closely?
- Which loan purposes are associated with higher risk?

## Repository structure
- `data/raw/` raw CSV data
- `data/cleaned/` cleaned or aggregated outputs
- `notebooks/` exploratory and presentation-ready notebook
- `sql/` schema and analysis queries
- `src/` reusable Python analysis script
- `dashboard/` dashboard layout notes
- `images/` chart screenshots
- `reports/` final summary files

## Suggested dashboard pages
1. Portfolio overview
2. Risk segmentation
3. Borrower behavior
4. Recommendations

## Sample business recommendations
- Tighten approval rules for low-grade, high-DTI borrowers
- Flag borrowers with high utilization for extra review
- Review pricing and underwriting for higher-risk loan purposes
