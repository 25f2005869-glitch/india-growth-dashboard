# ============================================
# Author : Saloni Tiwari
# Project : 1991 Economic Crisis Dashboard
# Topic : Economic Data Visualization
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load CSV Data
df = pd.read_csv("data/crisis_data.csv")

# --------------------------------------------
# Forex Reserve Graph
# --------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["Forex_Reserves"],
    marker='o'
)

plt.title("India Forex Reserves (1985-1995)")
plt.xlabel("Year")
plt.ylabel("Forex Reserves")

plt.grid(True)

plt.savefig("charts/forex_reserves.png")

plt.show()

# --------------------------------------------
# Inflation Graph
# --------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["Inflation"],
    marker='o'
)

plt.title("India Inflation Trend (1985-1995)")
plt.xlabel("Year")
plt.ylabel("Inflation")

plt.grid(True)

plt.savefig("charts/inflation_trend.png")

plt.show()

# --------------------------------------------
# GDP Growth Graph
# --------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    df["Year"],
    df["GDP_Growth"]
)

plt.title("India GDP Growth (1985-1995)")
plt.xlabel("Year")
plt.ylabel("GDP Growth")

plt.savefig("charts/gdp_growth.png")

plt.show()