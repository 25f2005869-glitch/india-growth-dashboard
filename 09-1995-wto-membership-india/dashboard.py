# ============================================
# Author: Saloni Tiwari
# Project: 09-1995-WTO-Membership-India
# File: dashboard.py
# Description:
# WTO & Trade Liberalization Dashboard
# using Python and Matplotlib
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/wto_india_data.csv")

# --------------------------------
# Trade Openness Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Trade_Openness_Index"],
         marker='o',
         linewidth=3)

plt.title("Trade Openness Growth")
plt.xlabel("Year")
plt.ylabel("Trade Openness Index")
plt.grid(True)

plt.savefig("charts/trade_openness_growth.png")
plt.show()

# --------------------------------
# Forex Reserve Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Forex_Reserves_Bn"],
         marker='o',
         linewidth=3)

plt.title("Forex Reserve Growth")
plt.xlabel("Year")
plt.ylabel("Forex Reserves (Billion USD)")
plt.grid(True)

plt.savefig("charts/forex_reserve_growth.png")
plt.show()

# --------------------------------
# Tariff Reduction
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Average_Tariff_Rate"],
         marker='o',
         linewidth=3)

plt.title("Average Tariff Reduction")
plt.xlabel("Year")
plt.ylabel("Tariff Rate (%)")
plt.grid(True)

plt.savefig("charts/tariff_reduction.png")
plt.show()

# --------------------------------
# Export Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.bar(df["Year"],
        df["Export_Growth"])

plt.title("Export Growth After WTO")
plt.xlabel("Year")
plt.ylabel("Export Growth (%)")
plt.grid(True)

plt.savefig("charts/export_growth.png")
plt.show()

# --------------------------------
# Pharma Export Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Pharma_Exports_Bn"],
         marker='o',
         linewidth=3)

plt.title("Indian Pharma Export Growth")
plt.xlabel("Year")
plt.ylabel("Pharma Exports (Billion USD)")
plt.grid(True)

plt.savefig("charts/pharma_export_growth.png")
plt.show()

# --------------------------------
# GDP & Trade Correlation
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Trade_Openness_Index"],
         marker='o',
         label="Trade Openness")

plt.plot(df["Year"],
         df["GDP_Growth"],
         marker='s',
         label="GDP Growth")

plt.title("Trade Openness vs GDP Growth")
plt.xlabel("Year")
plt.legend()
plt.grid(True)

plt.savefig("charts/gdp_trade_correlation.png")
plt.show()

print("\n========== DASHBOARD COMPLETED ==========")
print("All charts saved successfully in charts folder.")