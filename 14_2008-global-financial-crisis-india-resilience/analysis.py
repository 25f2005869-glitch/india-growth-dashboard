# ============================================
# Author: Saloni Tiwari
# Project: 14-2008-Global-Financial-Crisis
# File: analysis.py
# Description:
# Statistical Analysis of the
# 2008 Global Financial Crisis
# & India's Economic Resilience
# ============================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/global_financial_crisis_2008.csv")

# Display Dataset
print("\n========== DATASET ==========\n")
print(df)

# Dataset Info
print("\n========== DATA INFO ==========\n")
print(df.info())

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())

# Sensex Crash Analysis
print("\n========== SENSEX ANALYSIS ==========\n")
print("Highest Sensex:",
      df["Sensex_Index"].max())

print("Lowest Sensex:",
      df["Sensex_Index"].min())

# FII Outflow Analysis
print("\n========== FII OUTFLOWS ==========\n")
print("Maximum Capital Outflow:",
      df["FII_Outflows_Bn"].min())

# GDP Recovery Analysis
print("\n========== GDP RECOVERY ==========\n")
print("Highest GDP Growth:",
      df["GDP_Growth"].max())

# Repo Rate Analysis
print("\n========== RBI REPO RATE ==========\n")
print("Lowest Repo Rate:",
      df["Repo_Rate"].min())

# Banking Stability
print("\n========== BANKING STABILITY ==========\n")
print("Highest Banking Stability:",
      df["Banking_Stability"].max())

# Volatility Analysis
print("\n========== VOLATILITY ==========\n")
print("Highest Volatility:",
      df["Volatility_Index"].max())

# Correlation Matrix
print("\n========== CORRELATION MATRIX ==========\n")
print(df.corr(numeric_only=True))