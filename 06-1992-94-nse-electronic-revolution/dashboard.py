# ============================================
# Author: Saloni Tiwari
# Project: 06-1992-94-NSE-Electronic-Revolution
# File: dashboard.py
# Description:
# NSE Electronic Trading Revolution
# Dashboard using Matplotlib
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/nse_revolution_data.csv")

# --------------------------------
# Trading Volume Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Trading_Volume_Cr"],
         marker='o',
         linewidth=3)

plt.title("NSE Trading Volume Growth")
plt.xlabel("Year")
plt.ylabel("Trading Volume (Crore)")
plt.grid(True)

plt.savefig("charts/trading_volume_growth.png")
plt.show()

# --------------------------------
# Settlement Reduction
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Settlement_Days"],
         marker='o',
         linewidth=3)

plt.title("Settlement Days Reduction")
plt.xlabel("Year")
plt.ylabel("Settlement Days")
plt.grid(True)

plt.savefig("charts/settlement_reduction.png")
plt.show()

# --------------------------------
# Liquidity Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.bar(df["Year"],
        df["Liquidity_Index"])

plt.title("Liquidity Growth After NSE")
plt.xlabel("Year")
plt.ylabel("Liquidity Index")
plt.grid(True)

plt.savefig("charts/liquidity_growth.png")
plt.show()

# --------------------------------
# Market Transparency
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Settlement_Days"],
         marker='o',
         label="Settlement Days")

plt.plot(df["Year"],
         df["Liquidity_Index"],
         marker='s',
         label="Liquidity")

plt.title("Market Transparency & Efficiency")
plt.xlabel("Year")
plt.legend()
plt.grid(True)

plt.savefig("charts/market_transparency.png")
plt.show()

# --------------------------------
# Electronic Trading Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["FII_Investment_Cr"],
         marker='o',
         linewidth=3)

plt.title("FII Investment Growth")
plt.xlabel("Year")
plt.ylabel("FII Investment (Crore)")
plt.grid(True)

plt.savefig("charts/electronic_trading_growth.png")
plt.show()

print("\n========== DASHBOARD COMPLETED ==========")
print("All charts saved successfully in charts folder.")