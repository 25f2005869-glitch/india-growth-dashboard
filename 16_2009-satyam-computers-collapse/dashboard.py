# ============================================
# Author: Saloni Tiwari
# Project: 16-2009-Satyam-Computers-Collapse
# File: dashboard.py
# Description:
# Dashboard Visualization of
# Satyam Corporate Fraud
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/satyam_fraud_data.csv")

# --------------------------------
# Stock Price Crash
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Stock_Price"],
         marker='o',
         linewidth=3)

plt.title("Stock Price Crash")
plt.xlabel("Year")
plt.ylabel("Stock Price")
plt.grid(True)

plt.savefig("charts/stock_price_crash.png")
plt.show()

# --------------------------------
# Fake Revenue Analysis
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Fake_Revenue_Cr"],
         marker='o',
         linewidth=3)

plt.title("Fake Revenue Analysis")
plt.xlabel("Year")
plt.ylabel("Fake Revenue (Crore)")
plt.grid(True)

plt.savefig("charts/fake_revenue_analysis.png")
plt.show()

# --------------------------------
# Market Cap Collapse
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Market_Cap_Cr"],
         marker='o',
         linewidth=3)

plt.title("Market Cap Collapse")
plt.xlabel("Year")
plt.ylabel("Market Cap (Crore)")
plt.grid(True)

plt.savefig("charts/market_cap_collapse.png")
plt.show()

# --------------------------------
# Volatility Variance
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Volatility_Index"],
         marker='o',
         linewidth=3)

plt.title("Volatility Variance")
plt.xlabel("Year")
plt.ylabel("Volatility Index")
plt.grid(True)

plt.savefig("charts/volatility_variance.png")
plt.show()

# --------------------------------
# Investor Confidence Recovery
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Investor_Confidence"],
         marker='o',
         linewidth=3)

plt.title("Investor Confidence Recovery")
plt.xlabel("Year")
plt.ylabel("Confidence Index")
plt.grid(True)

plt.savefig("charts/investor_confidence_recovery.png")
plt.show()

# --------------------------------
# Audit Failure Analysis
# --------------------------------
plt.figure(figsize=(8,5))

audit_failure = (
    df["Fake_Revenue_Cr"] / 100
)

plt.plot(df["Year"],
         audit_failure,
         marker='o',
         linewidth=3)

plt.title("Audit Failure Analysis")
plt.xlabel("Year")
plt.ylabel("Audit Failure Index")
plt.grid(True)

plt.savefig("charts/audit_failure_analysis.png")
plt.show()

# --------------------------------
# Governance Reforms
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Governance_Index"],
         marker='o',
         linewidth=3)

plt.title("Governance Reforms")
plt.xlabel("Year")
plt.ylabel("Governance Score")
plt.grid(True)

plt.savefig("charts/governance_reforms.png")
plt.show()

# --------------------------------
# SEBI Regulation Impact
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["SEBI_Regulation_Score"],
         marker='o',
         linewidth=3)

plt.title("SEBI Regulation Impact")
plt.xlabel("Year")
plt.ylabel("SEBI Regulation Score")
plt.grid(True)

plt.savefig("charts/sebi_regulation_impact.png")
plt.show()

# --------------------------------
# Corporate Recovery
# --------------------------------
plt.figure(figsize=(8,5))

recovery = (
    df["Investor_Confidence"]
    + df["Governance_Index"]
)

plt.plot(df["Year"],
         recovery,
         marker='o',
         linewidth=3)

plt.title("Corporate Recovery")
plt.xlabel("Year")
plt.ylabel("Recovery Index")
plt.grid(True)

plt.savefig("charts/corporate_recovery.png")
plt.show()

# --------------------------------
# Statistical Mean Reversion
# --------------------------------
plt.figure(figsize=(8,5))

mean_reversion = (
    df["Volatility_Index"]
    - df["Investor_Confidence"]
)

plt.plot(df["Year"],
         mean_reversion,
         marker='o',
         linewidth=3)

plt.title("Statistical Mean Reversion")
plt.xlabel("Year")
plt.ylabel("Variance Difference")
plt.grid(True)

plt.savefig("charts/statistical_mean_reversion.png")
plt.show()

print("\n========== DASHBOARD COMPLETED ==========")
print("All charts saved successfully in charts folder.")