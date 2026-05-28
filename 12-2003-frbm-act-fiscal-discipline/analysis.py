# ============================================
# Author: Saloni Tiwari
# Project: 12-2003-FRBM-Act-Fiscal-Discipline
# File: analysis.py
# Description:
# Statistical Analysis of India's
# FRBM Act & Fiscal Discipline Reforms
# ============================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/frbm_fiscal_data.csv")

print("\n========== DATASET ==========\n")
print(df)

# Dataset Info
print("\n========== DATA INFO ==========\n")
print(df.info())

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())

# Fiscal Deficit Analysis
print("\n========== FISCAL DEFICIT ==========\n")
print("Lowest Fiscal Deficit:",
      df["Fiscal_Deficit_GDP"].min())

# Revenue Deficit Analysis
print("\n========== REVENUE DEFICIT ==========\n")
print("Lowest Revenue Deficit:",
      df["Revenue_Deficit_GDP"].min())

# Debt Analysis
print("\n========== PUBLIC DEBT ==========\n")
print("Lowest Debt-to-GDP Ratio:",
      df["Public_Debt_GDP"].min())

# Credit Rating
print("\n========== CREDIT RATING ==========\n")
print("Highest Credit Rating Index:",
      df["Credit_Rating_Index"].max())

# FDI Analysis
print("\n========== FDI INFLOWS ==========\n")
print("Highest FDI Inflows:",
      df["FDI_Inflows_Bn"].max())

# Correlation
print("\n========== CORRELATION ==========\n")
print(df.corr(numeric_only=True))