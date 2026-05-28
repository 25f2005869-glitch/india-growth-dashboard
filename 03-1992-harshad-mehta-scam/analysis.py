# ============================================
# Author: Saloni Tiwari
# Topic: 1992 Harshad Mehta Scam Analysis
# Description:
# Statistical analysis of India's stock market
# during the Harshad Mehta Scam period.
# ============================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/scam_data.csv")

print("\n========== DATASET ==========\n")
print(df)

# Maximum Sensex
print("\n========== MAXIMUM SENSEX ==========\n")
print(df["Sensex"].max())

# Average Sensex
print("\n========== AVERAGE SENSEX ==========\n")
print(df["Sensex"].mean())

# Maximum ACC Stock Price
print("\n========== MAXIMUM ACC STOCK PRICE ==========\n")
print(df["ACC_Stock"].max())

# Average Inflation
print("\n========== AVERAGE INFLATION ==========\n")
print(df["Inflation"].mean())

# Minimum Forex Reserves
print("\n========== MINIMUM FOREX RESERVES ==========\n")
print(df["Forex_Reserves"].min())

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())