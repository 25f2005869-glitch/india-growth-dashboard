# ============================================
# Author: Saloni Tiwari
# Project: 16-2009-Satyam-Computers-Collapse
# File: analysis.py
# Description:
# Statistical Analysis of Satyam Scam,
# Corporate Governance & SEBI Reforms
# ============================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/satyam_fraud_data.csv")

# Display Dataset
print("\n========== DATASET ==========\n")
print(df)

# Dataset Information
print("\n========== DATA INFO ==========\n")
print(df.info())

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())

# Stock Price Analysis
print("\n========== STOCK PRICE ANALYSIS ==========\n")
print("Highest Stock Price:",
      df["Stock_Price"].max())

print("Lowest Stock Price:",
      df["Stock_Price"].min())

# Fake Revenue Analysis
print("\n========== FAKE REVENUE ==========\n")
print("Maximum Fake Revenue:",
      df["Fake_Revenue_Cr"].max())

# Fake Employees Analysis
print("\n========== GHOST EMPLOYEES ==========\n")
print("Maximum Fake Employees:",
      df["Fake_Employees"].max())

# Market Cap Analysis
print("\n========== MARKET CAP ==========\n")
print("Highest Market Cap:",
      df["Market_Cap_Cr"].max())

print("Lowest Market Cap:",
      df["Market_Cap_Cr"].min())

# Investor Confidence
print("\n========== INVESTOR CONFIDENCE ==========\n")
print("Lowest Investor Confidence:",
      df["Investor_Confidence"].min())

# Volatility Analysis
print("\n========== VOLATILITY ==========\n")
print("Highest Volatility:",
      df["Volatility_Index"].max())

# Governance Analysis
print("\n========== GOVERNANCE ==========\n")
print("Highest Governance Score:",
      df["Governance_Index"].max())

# SEBI Regulations
print("\n========== SEBI REGULATION ==========\n")
print("Highest Regulation Score:",
      df["SEBI_Regulation_Score"].max())

# Correlation Matrix
print("\n========== CORRELATION MATRIX ==========\n")
print(df.corr(numeric_only=True))