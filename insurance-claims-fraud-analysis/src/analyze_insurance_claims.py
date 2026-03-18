from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "insurance_claims.csv"
CLEAN = ROOT / "data" / "cleaned"
IMG = ROOT / "images"

CLEAN.mkdir(parents=True, exist_ok=True)
IMG.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(DATA, parse_dates=["claim_date"])

    df["tenure_bucket"] = pd.cut(df["policy_tenure_years"], bins=[0,2,5,10,20], labels=["0-2","3-5","6-10","11+"])
    df["claim_month"] = df["claim_date"].dt.to_period("M").astype(str)

    by_incident = df.groupby("incident_type", as_index=False).agg(
        claims=("claim_id","count"),
        fraud_rate=("fraud_reported","mean"),
        avg_claim_amount=("claim_amount","mean")
    ).sort_values("fraud_rate", ascending=False)
    by_incident["fraud_rate"] = (by_incident["fraud_rate"] * 100).round(2)

    by_region = df.groupby("region", as_index=False).agg(
        claims=("claim_id","count"),
        fraud_rate=("fraud_reported","mean"),
        avg_settlement_days=("settlement_days","mean")
    )
    by_region["fraud_rate"] = (by_region["fraud_rate"] * 100).round(2)

    by_tenure = df.groupby("tenure_bucket", as_index=False).agg(fraud_rate=("fraud_reported","mean"))
    by_tenure["fraud_rate"] = (by_tenure["fraud_rate"] * 100).round(2)

    by_incident.to_csv(CLEAN / "summary_by_incident_type.csv", index=False)
    by_region.to_csv(CLEAN / "summary_by_region.csv", index=False)
    by_tenure.to_csv(CLEAN / "summary_by_tenure_bucket.csv", index=False)
    df.to_csv(CLEAN / "insurance_claims_enriched.csv", index=False)

    plt.figure(figsize=(8,4))
    plt.bar(by_incident["incident_type"], by_incident["fraud_rate"])
    plt.title("Fraud Rate by Incident Type")
    plt.xlabel("Incident Type")
    plt.ylabel("Fraud Rate (%)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(IMG / "fraud_rate_by_incident_type.png")
    plt.close()

    plt.figure(figsize=(8,4))
    plt.hist(df["claim_amount"], bins=25)
    plt.title("Claim Amount Distribution")
    plt.xlabel("Claim Amount")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(IMG / "claim_amount_distribution.png")
    plt.close()

    plt.figure(figsize=(8,4))
    plt.scatter(df["claim_amount"], df["settlement_days"], alpha=0.35)
    plt.title("Claim Amount vs Settlement Days")
    plt.xlabel("Claim Amount")
    plt.ylabel("Settlement Days")
    plt.tight_layout()
    plt.savefig(IMG / "claim_amount_vs_settlement_days.png")
    plt.close()

    print("Outputs written to data/cleaned and images/")

if __name__ == "__main__":
    main()
