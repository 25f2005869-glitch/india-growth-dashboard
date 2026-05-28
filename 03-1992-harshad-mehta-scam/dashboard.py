# ============================================
# Author: Saloni Tiwari
# Topic: 1992 Harshad Mehta Scam Dashboard
# Description:
# Data visualization project showing the
# impact of the Harshad Mehta Scam on
# India's stock market and economy.
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/scam_data.csv")

# ============================================
# Sensex Crash Visualization
# ============================================

plt.figure(figsize=(10,5))

plt.plot(
    df["Year"],
    df["Sensex"],
    marker='o',
    linewidth=3
)

plt.title("Sensex Boom and Crash (1990-1995)")
plt.xlabel("Year")
plt.ylabel("Sensex")

plt.grid(True)

plt.savefig("charts/sensex_crash.png")

plt.show()

# ============================================
# ACC Stock Growth Visualization
# ============================================

plt.figure(figsize=(10,5))

plt.bar(
    df["Year"],
    df["ACC_Stock"]
)

plt.title("ACC Stock Price Growth")
plt.xlabel("Year")
plt.ylabel("ACC Stock Price")

plt.savefig("charts/acc_stock_growth.png")

plt.show()

# ============================================
# Inflation Trend Visualization
# ============================================

plt.figure(figsize=(10,5))

plt.plot(
    df["Year"],
    df["Inflation"],
    marker='o',
    linewidth=3
)

plt.title("Inflation Trend During Scam Period")
plt.xlabel("Year")
plt.ylabel("Inflation")

plt.grid(True)

plt.savefig("charts/inflation_trend.png")

plt.show()