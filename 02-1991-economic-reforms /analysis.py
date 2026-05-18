# ============================================
# Author: Saloni Tiwari
# Project: India Growth Dashboard (1991-2025)
# File: analysis.py
# Description:
# Basic statistical analysis of India's
# growth indicators.
# ============================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/india_growth_data.csv")

print("\n========== DATASET ==========\n")
print(df)

print("\n========== SUMMARY ==========\n")
print(df.describe())

print("\n========== MAX GDP GROWTH ==========\n")
print(df["GDP_Growth"].max())

print("\n========== AVERAGE GDP GROWTH ==========\n")
print(df["GDP_Growth"].mean())

print("\n========== MAX FOREX RESERVES ==========\n")
print(df["Forex_Reserves"].max())
