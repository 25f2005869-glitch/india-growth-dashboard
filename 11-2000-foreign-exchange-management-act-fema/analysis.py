# ============================================
# Author: Saloni Tiwari
# Project: 11-2000-FEMA
# File: analysis.py
# Description:
# Statistical Analysis of FEMA &
# India's Foreign Exchange Liberalization
# ============================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/fema_data.csv")

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

# Trade Openness
print("\n========== TRADE OPENNESS ==========\n")
print("Highest Trade Openness:",
      df["Trade_Openness_Index"].max())

# FDI Analysis
print("\n========== FDI INFLOWS ==========\n")
print("Maximum FDI Inflow:",
      df["FDI_Inflows_Bn"].max())

# IT Export Analysis
print("\n========== IT EXPORTS ==========\n")
print("Maximum IT Exports:",
      df["IT_Exports_Bn"].max())

# Correlation
print("\n========== CORRELATION ==========\n")
print(df.corr(numeric_only=True))