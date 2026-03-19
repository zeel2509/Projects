from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "retail_sales.csv"
CLEAN = ROOT / "data" / "cleaned"
IMG = ROOT / "images"

CLEAN.mkdir(parents=True, exist_ok=True)
IMG.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(DATA, parse_dates=["order_date"])
    df["month"] = df["order_date"].dt.to_period("M").astype(str)

    category_summary = df.groupby("product_category", as_index=False).agg(
        total_sales=("sales","sum"),
        total_profit=("profit","sum")
    ).sort_values("total_sales", ascending=False)

    region_summary = df.groupby("region", as_index=False).agg(
        total_sales=("sales","sum"),
        total_profit=("profit","sum")
    ).sort_values("total_sales", ascending=False)

    top_products = df.groupby("product_name", as_index=False).agg(
        total_sales=("sales","sum")
    ).sort_values("total_sales", ascending=False).head(10)

    monthly = df.groupby("month", as_index=False).agg(monthly_sales=("sales","sum"))
    monthly["month_start"] = pd.to_datetime(monthly["month"] + "-01")
    monthly["t"] = np.arange(len(monthly))

    train = monthly.iloc[:-6].copy()
    test = monthly.iloc[-6:].copy()

    baseline_pred = np.repeat(train["monthly_sales"].iloc[-1], len(test))
    baseline_mae = mean_absolute_error(test["monthly_sales"], baseline_pred)

    model = LinearRegression()
    model.fit(train[["t"]], train["monthly_sales"])
    model_pred = model.predict(test[["t"]])
    model_mae = mean_absolute_error(test["monthly_sales"], model_pred)

    forecast_compare = test[["month","monthly_sales"]].copy()
    forecast_compare["baseline_pred"] = baseline_pred
    forecast_compare["linear_regression_pred"] = model_pred.round(2)

    category_summary.to_csv(CLEAN / "summary_by_category.csv", index=False)
    region_summary.to_csv(CLEAN / "summary_by_region.csv", index=False)
    top_products.to_csv(CLEAN / "top_products.csv", index=False)
    monthly.to_csv(CLEAN / "monthly_sales.csv", index=False)
    forecast_compare.to_csv(CLEAN / "forecast_vs_actual.csv", index=False)

    with open(CLEAN / "forecast_metrics.txt", "w", encoding="utf-8") as f:
        f.write(f"Baseline MAE: {baseline_mae:.2f}\n")
        f.write(f"Linear Regression MAE: {model_mae:.2f}\n")

    plt.figure(figsize=(8,4))
    plt.plot(monthly["month_start"], monthly["monthly_sales"])
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig(IMG / "monthly_sales_trend.png")
    plt.close()

    plt.figure(figsize=(8,4))
    plt.bar(category_summary["product_category"], category_summary["total_sales"])
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.savefig(IMG / "sales_by_category.png")
    plt.close()

    plt.figure(figsize=(8,4))
    plt.scatter(df["discount"], df["profit"], alpha=0.35)
    plt.title("Discount vs Profit")
    plt.xlabel("Discount")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.savefig(IMG / "discount_vs_profit.png")
    plt.close()

    print("Outputs written to data/cleaned and images/")
    print(f"Baseline MAE: {baseline_mae:.2f}")
    print(f"Linear Regression MAE: {model_mae:.2f}")

if __name__ == "__main__":
    main()
