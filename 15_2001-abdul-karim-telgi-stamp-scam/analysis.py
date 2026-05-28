# ============================================
# Author: Saloni Tiwari
# Project: 15-2001-Abdul-Karim-Telgi-Stamp-Scam
# File: analysis.py
# Description:
# Statistical Analysis of Telgi Stamp Scam,
# Revenue Leakage & E-Stamping Revolution
# ============================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/telgi_stamp_scam_data.csv")

# Display Dataset
print("\n========== DATASET ==========\n")
print(df)

# Dataset Information
print("\n========== DATA INFO ==========\n")
print(df.info())

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())

# Property Registrations
print("\n========== PROPERTY REGISTRATIONS ==========\n")
print("Highest Registrations:",
      df["Property_Registrations_Lakh"].max())

# Stamp Revenue Analysis
print("\n========== STAMP REVENUE ==========\n")
print("Lowest Revenue:",
      df["Stamp_Revenue_Cr"].min())

# Counterfeit Analysis
print("\n========== COUNTERFEIT INDEX ==========\n")
print("Highest Counterfeit Activity:",
      df["Counterfeit_Index"].max())

# Fiscal Deficit Analysis
print("\n========== FISCAL DEFICIT IMPACT ==========\n")
print("Maximum Fiscal Impact:",
      df["Fiscal_Deficit_Impact"].max())

# Banking Exposure
print("\n========== BANKING EXPOSURE ==========\n")
print("Highest Banking Exposure:",
      df["Banking_Exposure"].max())

# E-Stamping Adoption
print("\n========== E-STAMPING ==========\n")
print("Highest E-Stamping Adoption:",
      df["E_Stamping_Adoption"].max())

# Fraud Variance
print("\n========== FRAUD VARIANCE ==========\n")
print("Highest Fraud Variance:",
      df["Fraud_Variance"].max())

# Correlation Matrix
print("\n========== CORRELATION MATRIX ==========\n")
print(df.corr(numeric_only=True))