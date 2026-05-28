# ============================================
# Author: Saloni Tiwari
# Project: 09-1995-WTO-Membership-India
# File: analysis.py
# Description:
# Statistical Analysis of India's WTO
# Membership & Trade Liberalization
# ============================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/wto_india_data.csv")

print("\n========== DATASET ==========\n")
print(df)

# Data Information
print("\n========== DATA INFO ==========\n")
print(df.info())

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())

# Trade Openness
print("\n========== TRADE OPENNESS ==========\n")
print("Highest Trade Openness:",
      df["Trade_Openness_Index"].max())

# Forex Reserves
print("\n========== FOREX RESERVES ==========\n")
print("Maximum Forex Reserves:",
      df["Forex_Reserves_Bn"].max())

# Tariff Reduction
print("\n========== TARIFF REDUCTION ==========\n")
print("Lowest Tariff Rate:",
      df["Average_Tariff_Rate"].min())

# Export Growth
print("\n========== EXPORT GROWTH ==========\n")
print("Highest Export Growth:",
      df["Export_Growth"].max())

# Pharma Exports
print("\n========== PHARMA EXPORTS ==========\n")
print("Maximum Pharma Exports:",
      df["Pharma_Exports_Bn"].max())

# Correlation
print("\n========== CORRELATION ==========\n")
print(df.corr(numeric_only=True))