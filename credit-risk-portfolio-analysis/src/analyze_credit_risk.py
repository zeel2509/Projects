from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "loan_data.csv"
CLEAN = ROOT / "data" / "cleaned"
IMG = ROOT / "images"

CLEAN.mkdir(parents=True, exist_ok=True)
IMG.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(DATA)

    # Basic validation
    print("Rows, columns:", df.shape)
    print(df.isna().sum())

    # Feature engineering
    df["dti_bucket"] = pd.cut(df["dti_ratio"], bins=[0,10,20,30,50], labels=["0-10","10-20","20-30","30+"])
    df["util_bucket"] = pd.cut(df["utilization_rate"], bins=[0,30,50,70,100], labels=["0-30","30-50","50-70","70+"])
    df["score_band"] = pd.cut(df["credit_score"], bins=[300,580,670,740,800,850], labels=["Poor","Fair","Good","Very Good","Excellent"], include_lowest=True)

    # Summaries
    by_grade = df.groupby("grade", as_index=False).agg(
        total_loans=("customer_id","count"),
        default_rate=("default_flag","mean"),
        avg_loan_amount=("loan_amount","mean"),
        avg_credit_score=("credit_score","mean"),
    )
    by_grade["default_rate"] = (by_grade["default_rate"] * 100).round(2)

    by_dti = df.groupby("dti_bucket", as_index=False).agg(default_rate=("default_flag","mean"))
    by_dti["default_rate"] = (by_dti["default_rate"] * 100).round(2)

    by_purpose = df.groupby("purpose", as_index=False).agg(default_rate=("default_flag","mean")).sort_values("default_rate", ascending=False)
    by_purpose["default_rate"] = (by_purpose["default_rate"] * 100).round(2)

    by_grade.to_csv(CLEAN / "summary_by_grade.csv", index=False)
    by_dti.to_csv(CLEAN / "summary_by_dti_bucket.csv", index=False)
    by_purpose.to_csv(CLEAN / "summary_by_purpose.csv", index=False)
    df.to_csv(CLEAN / "loan_data_enriched.csv", index=False)

    # Charts
    plt.figure(figsize=(8,4))
    plt.bar(by_grade["grade"], by_grade["default_rate"])
    plt.title("Default Rate by Grade")
    plt.xlabel("Grade")
    plt.ylabel("Default Rate (%)")
    plt.tight_layout()
    plt.savefig(IMG / "default_rate_by_grade.png")
    plt.close()

    plt.figure(figsize=(8,4))
    plt.hist(df["credit_score"], bins=25)
    plt.title("Credit Score Distribution")
    plt.xlabel("Credit Score")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(IMG / "credit_score_distribution.png")
    plt.close()

    plt.figure(figsize=(8,4))
    plt.scatter(df["dti_ratio"], df["utilization_rate"], alpha=0.35)
    plt.title("DTI Ratio vs Utilization Rate")
    plt.xlabel("DTI Ratio")
    plt.ylabel("Utilization Rate")
    plt.tight_layout()
    plt.savefig(IMG / "dti_vs_utilization.png")
    plt.close()

    print("Outputs written to data/cleaned and images/")

if __name__ == "__main__":
    main()
