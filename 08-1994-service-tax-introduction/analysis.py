# ============================================
# Author: Saloni Tiwari
# Project: 08-1994-Service-Tax-Introduction
# File: analysis.py
# Description:
# Statistical Analysis of India's
# Service Tax Introduction (1994)
# ============================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/service_tax_data.csv")

print("\n========== DATASET ==========\n")
print(df)

# Data Information
print("\n========== DATA INFO ==========\n")
print(df.info())

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())

# Revenue Analysis
print("\n========== SERVICE TAX REVENUE ==========\n")
print("Maximum Revenue:",
      df["Service_Tax_Revenue_Cr"].max())

# Fiscal Deficit Analysis
print("\n========== FISCAL DEFICIT ==========\n")
print("Lowest Fiscal Deficit:",
      df["Fiscal_Deficit"].min())

# Service Sector GDP
print("\n========== SERVICE GDP ==========\n")
print("Maximum Service Sector GDP:",
      df["Service_Sector_GDP"].max())

# Taxable Services Growth
print("\n========== TAXABLE SERVICES ==========\n")
print("Maximum Taxable Services:",
      df["Taxable_Services"].max())

# Correlation
print("\n========== CORRELATION ==========\n")
print(df.corr(numeric_only=True))