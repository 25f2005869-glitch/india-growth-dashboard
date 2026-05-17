# ============================================
# Author : Saloni Tiwari
# Project : 1991 Economic Crisis Analysis
# Topic : Economic Data Analysis
# ============================================

import pandas as pd

# Load CSV Data
df = pd.read_csv("data/crisis_data.csv")

# Display Dataset
print("\n========== INDIA 1991 ECONOMIC CRISIS DATA ==========\n")
print(df)

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())

# Maximum Inflation
print("\n========== MAXIMUM INFLATION ==========\n")
print(df["Inflation"].max())

# Average GDP Growth
print("\n========== AVERAGE GDP GROWTH ==========\n")
print(df["GDP_Growth"].mean())

# Minimum Forex Reserves
print("\n========== MINIMUM FOREX RESERVES ==========\n")
print(df["Forex_Reserves"].min())
