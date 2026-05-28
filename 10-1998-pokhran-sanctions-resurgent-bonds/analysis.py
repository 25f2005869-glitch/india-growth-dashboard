# ============================================
# Author: Saloni Tiwari
# Project: 10-1998-Pokhran-Sanctions-Resurgent-Bonds
# File: analysis.py
# Description:
# Statistical Analysis of Pokhran-II,
# Economic Sanctions & Resurgent India Bonds
# ============================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/pokhran_sanctions_data.csv")

print("\n========== DATASET ==========\n")
print(df)

# Data Information
print("\n========== DATA INFO ==========\n")
print(df.info())

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())

# Forex Analysis
print("\n========== FOREX RESERVES ==========\n")
print("Maximum Forex Reserves:",
      df["Forex_Reserves_Bn"].max())

# FII Analysis
print("\n========== FII INFLOW ==========\n")
print("Lowest FII Inflow:",
      df["FII_Inflow_Bn"].min())

# Rupee Volatility
print("\n========== RUPEE VOLATILITY ==========\n")
print("Highest Rupee per Dollar:",
      df["Rupee_Per_Dollar"].max())

# RIB Analysis
print("\n========== RESURGENT INDIA BONDS ==========\n")
print("Maximum RIB Investment:",
      df["RIB_Investment_Bn"].max())

# Correlation
print("\n========== CORRELATION ==========\n")
print(df.corr(numeric_only=True))