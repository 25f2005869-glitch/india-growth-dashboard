# ============================================
# Author: Saloni Tiwari
# Project: 06-1992-94-NSE-Electronic-Revolution
# File: analysis.py
# Description:
# Statistical Analysis of NSE Electronic
# Trading Revolution in India
# ============================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/nse_revolution_data.csv")

print("\n========== DATASET ==========\n")
print(df)

# Data Information
print("\n========== DATA INFO ==========\n")
print(df.info())

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())

# Trading Volume Analysis
print("\n========== TRADING VOLUME ==========\n")
print("Maximum Trading Volume:",
      df["Trading_Volume_Cr"].max())

# Settlement Analysis
print("\n========== SETTLEMENT PERIOD ==========\n")
print("Minimum Settlement Days:",
      df["Settlement_Days"].min())

# Liquidity Analysis
print("\n========== LIQUIDITY ANALYSIS ==========\n")
print("Highest Liquidity Index:",
      df["Liquidity_Index"].max())

# FII Investment Analysis
print("\n========== FII INVESTMENT ==========\n")
print("Maximum FII Investment:",
      df["FII_Investment_Cr"].max())

# Correlation
print("\n========== CORRELATION ==========\n")
print(df.corr(numeric_only=True))