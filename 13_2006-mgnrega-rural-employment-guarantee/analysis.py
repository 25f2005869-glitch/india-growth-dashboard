# ============================================
# Author: Saloni Tiwari
# Project: 13-2006-MGNREGA
# File: analysis.py
# Description:
# Statistical Analysis of MGNREGA,
# Welfare Leakages & Financial Inclusion
# ============================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/mgnrega_data.csv")

print("\n========== DATASET ==========\n")
print(df)

# Dataset Info
print("\n========== DATA INFO ==========\n")
print(df.info())

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())

# Employment Analysis
print("\n========== EMPLOYMENT ==========\n")
print("Maximum Employment:",
      df["Employment_Crore"].max())

# Women Participation
print("\n========== WOMEN PARTICIPATION ==========\n")
print("Highest Women Participation:",
      df["Women_Participation"].max())

# Leakage Analysis
print("\n========== LEAKAGE INDEX ==========\n")
print("Lowest Leakage Index:",
      df["Leakage_Index"].min())

# Banking Linkage
print("\n========== BANK LINKAGE ==========\n")
print("Highest Banking Linkage:",
      df["Bank_Linkage"].max())

# DBT Analysis
print("\n========== DBT COVERAGE ==========\n")
print("Highest DBT Coverage:",
      df["DBT_Coverage"].max())

# Migration Analysis
print("\n========== MIGRATION ==========\n")
print("Lowest Migration Index:",
      df["Rural_Migration_Index"].min())

# Correlation
print("\n========== CORRELATION ==========\n")
print(df.corr(numeric_only=True))