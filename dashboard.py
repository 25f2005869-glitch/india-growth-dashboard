# ============================================
# Author: Saloni Tiwari
# Project: India Growth Dashboard (1991-2025)
# File: dashboard.py
# Description:
# Data visualization dashboard for India's
# economic and development growth.
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load CSV Data
df = pd.read_csv("data/india_growth_data.csv")

# -------------------------------
# GDP Growth Line Chart
# -------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    df["Year"],
    df["GDP_Growth"],
    marker="o",
    linewidth=2
)

plt.title("India GDP Growth (1991-2025)")
plt.xlabel("Year")
plt.ylabel("GDP Growth (%)")
plt.grid(True)

plt.savefig("charts/gdp_growth.png")

plt.show()


# -------------------------------
# Forex Reserves Bar Chart
# -------------------------------

plt.figure(figsize=(10, 5))

plt.bar(
    df["Year"],
    df["Forex_Reserves"]
)

plt.title("India Forex Reserves")
plt.xlabel("Year")
plt.ylabel("Forex Reserves (Billion USD)")

plt.savefig("charts/forex_reserves.png")

plt.show()