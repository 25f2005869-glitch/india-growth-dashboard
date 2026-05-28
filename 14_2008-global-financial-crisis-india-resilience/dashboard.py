# ============================================
# Author: Saloni Tiwari
# Project: 14-2008-Global-Financial-Crisis
# File: dashboard.py
# Description:
# Dashboard Visualization of
# Global Financial Crisis 2008
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/global_financial_crisis_2008.csv")

# --------------------------------
# Sensex Crash & Recovery
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Sensex_Index"],
         marker='o',
         linewidth=3)

plt.title("Sensex Crash & Recovery")
plt.xlabel("Year")
plt.ylabel("Sensex Index")
plt.grid(True)

plt.savefig("charts/sensex_crash_recovery.png")
plt.show()

# --------------------------------
# FII Outflow Analysis
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["FII_Outflows_Bn"],
         marker='o',
         linewidth=3)

plt.title("FII Capital Outflows")
plt.xlabel("Year")
plt.ylabel("FII Outflows (Billion USD)")
plt.grid(True)

plt.savefig("charts/fii_outflow_analysis.png")
plt.show()

# --------------------------------
# Repo Rate Reduction
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Repo_Rate"],
         marker='o',
         linewidth=3)

plt.title("RBI Repo Rate Changes")
plt.xlabel("Year")
plt.ylabel("Repo Rate (%)")
plt.grid(True)

plt.savefig("charts/repo_rate_reduction.png")
plt.show()

# --------------------------------
# GDP Recovery
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["GDP_Growth"],
         marker='o',
         linewidth=3)

plt.title("India GDP Recovery")
plt.xlabel("Year")
plt.ylabel("GDP Growth (%)")
plt.grid(True)

plt.savefig("charts/gdp_recovery.png")
plt.show()

# --------------------------------
# Banking Stability
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Banking_Stability"],
         marker='o',
         linewidth=3)

plt.title("Indian Banking Stability")
plt.xlabel("Year")
plt.ylabel("Banking Stability Index")
plt.grid(True)

plt.savefig("charts/banking_stability.png")
plt.show()

# --------------------------------
# Liquidity Infusion
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Liquidity_Index"],
         marker='o',
         linewidth=3)

plt.title("Liquidity Infusion")
plt.xlabel("Year")
plt.ylabel("Liquidity Index")
plt.grid(True)

plt.savefig("charts/liquidity_infusion.png")
plt.show()

# --------------------------------
# Volatility Variance
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Volatility_Index"],
         marker='o',
         linewidth=3)

plt.title("Market Volatility Variance")
plt.xlabel("Year")
plt.ylabel("Volatility Index")
plt.grid(True)

plt.savefig("charts/volatility_variance.png")
plt.show()

# --------------------------------
# Domestic Consumption
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Domestic_Consumption"],
         marker='o',
         linewidth=3)

plt.title("Domestic Consumption Strength")
plt.xlabel("Year")
plt.ylabel("Consumption Index")
plt.grid(True)

plt.savefig("charts/domestic_consumption_strength.png")
plt.show()

print("\n========== DASHBOARD COMPLETED ==========")
print("All charts saved successfully in charts folder.")