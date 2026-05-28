# ============================================
# Author: Saloni Tiwari
# Project: 10-1998-Pokhran-Sanctions-Resurgent-Bonds
# File: dashboard.py
# Description:
# Pokhran-II Economic Sanctions Dashboard
# using Python & Matplotlib
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/pokhran_sanctions_data.csv")

# --------------------------------
# Forex Reserve Recovery
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Forex_Reserves_Bn"],
         marker='o',
         linewidth=3)

plt.title("Forex Reserve Recovery")
plt.xlabel("Year")
plt.ylabel("Forex Reserves (Billion USD)")
plt.grid(True)

plt.savefig("charts/forex_reserve_recovery.png")
plt.show()

# --------------------------------
# FII Shock
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["FII_Inflow_Bn"],
         marker='o',
         linewidth=3)

plt.title("FII Inflow Shock After Sanctions")
plt.xlabel("Year")
plt.ylabel("FII Inflow (Billion USD)")
plt.grid(True)

plt.savefig("charts/fii_outflow_shock.png")
plt.show()

# --------------------------------
# RIB Investment Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.bar(df["Year"],
        df["RIB_Investment_Bn"])

plt.title("Resurgent India Bonds (RIB)")
plt.xlabel("Year")
plt.ylabel("Investment (Billion USD)")
plt.grid(True)

plt.savefig("charts/rib_investment_growth.png")
plt.show()

# --------------------------------
# Sanctions vs Recovery
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Sanctions_Severity_Index"],
         marker='o',
         label="Sanctions Severity")

plt.plot(df["Year"],
         df["Forex_Reserves_Bn"],
         marker='s',
         label="Forex Reserves")

plt.title("Sanctions vs Economic Recovery")
plt.xlabel("Year")
plt.legend()
plt.grid(True)

plt.savefig("charts/sanctions_vs_recovery.png")
plt.show()

# --------------------------------
# Rupee Volatility
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Rupee_Per_Dollar"],
         marker='o',
         linewidth=3)

plt.title("Rupee Volatility During Sanctions")
plt.xlabel("Year")
plt.ylabel("Rupee per Dollar")
plt.grid(True)

plt.savefig("charts/rupee_volatility.png")
plt.show()

# --------------------------------
# Economic Resilience
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["GDP_Growth"],
         marker='o',
         label="GDP Growth")

plt.plot(df["Year"],
         df["Forex_Reserves_Bn"],
         marker='s',
         label="Forex Reserves")

plt.title("Economic Resilience After Pokhran")
plt.xlabel("Year")
plt.legend()
plt.grid(True)

plt.savefig("charts/economic_resilience.png")
plt.show()

# --------------------------------
# Sovereign Confidence
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["RIB_Investment_Bn"],
         marker='o',
         linewidth=3)

plt.title("NRI Confidence Through RIB")
plt.xlabel("Year")
plt.ylabel("RIB Investment (Billion USD)")
plt.grid(True)

plt.savefig("charts/sovereign_confidence.png")
plt.show()

print("\n========== DASHBOARD COMPLETED ==========")
print("All charts saved successfully in charts folder.")