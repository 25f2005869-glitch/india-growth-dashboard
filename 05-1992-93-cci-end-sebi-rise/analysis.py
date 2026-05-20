# ============================================
# Author: Saloni Tiwari
# Project: 05-1992-93-CCI-End-SEBI-Rise
# File: analysis.py
# Description:
# Statistical Analysis of CCI Removal and
# Rise of SEBI in Indian Stock Market
# ============================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/sebi_reforms_data.csv")

print("\n========== DATASET ==========\n")
print(df)

# Basic Information
print("\n========== DATA INFO ==========\n")
print(df.info())

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())

# Capital Raised Analysis
print("\n========== CAPITAL RAISED ==========\n")
print("Maximum Capital Raised:", df["Capital_Raised_Cr"].max())
print("Minimum Capital Raised:", df["Capital_Raised_Cr"].min())

# Volatility Analysis
print("\n========== MARKET VOLATILITY ==========\n")
print("Highest Volatility:", df["Volatility_Index"].max())
print("Lowest Volatility:", df["Volatility_Index"].min())

# Investor Protection Analysis
print("\n========== INVESTOR PROTECTION ==========\n")
print("Highest Complaints Resolved:",
      df["Investor_Complaints_Resolved"].max())

# SEBI Era Data
print("\n========== SEBI ERA DATA ==========\n")
print(df[df["Era"] == "SEBI"])

# Correlation
print("\n========== CORRELATION ==========\n")
print(df.corr(numeric_only=True))