# ============================================
# Author: Saloni Tiwari
# Project: 11-2000-FEMA
# File: dashboard.py
# Description:
# FEMA Dashboard using Python
# & Matplotlib
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/fema_data.csv")

# --------------------------------
# Forex Reserve Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Forex_Reserves_Bn"],
         marker='o',
         linewidth=3)

plt.title("Forex Reserve Growth After FEMA")
plt.xlabel("Year")
plt.ylabel("Forex Reserves (Billion USD)")
plt.grid(True)

plt.savefig("charts/forex_reserve_growth.png")
plt.show()

# --------------------------------
# Trade Openness Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Trade_Openness_Index"],
         marker='o',
         linewidth=3)

plt.title("Trade Openness Index Growth")
plt.xlabel("Year")
plt.ylabel("Trade Openness Index")
plt.grid(True)

plt.savefig("charts/trade_openness_growth.png")
plt.show()

# --------------------------------
# FDI Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.bar(df["Year"],
        df["FDI_Inflows_Bn"])

plt.title("FDI Inflows Growth")
plt.xlabel("Year")
plt.ylabel("FDI Inflows (Billion USD)")
plt.grid(True)

plt.savefig("charts/fdi_inflow_growth.png")
plt.show()

# --------------------------------
# IT Export Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["IT_Exports_Bn"],
         marker='o',
         linewidth=3)

plt.title("Indian IT Export Growth")
plt.xlabel("Year")
plt.ylabel("IT Exports (Billion USD)")
plt.grid(True)

plt.savefig("charts/it_export_growth.png")
plt.show()

# --------------------------------
# Current Account Liberalization
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Trade_Openness_Index"],
         marker='o',
         label="Trade Openness")

plt.plot(df["Year"],
         df["FDI_Inflows_Bn"],
         marker='s',
         label="FDI Inflows")

plt.title("Current Account Liberalization")
plt.xlabel("Year")
plt.legend()
plt.grid(True)

plt.savefig("charts/current_account_liberalization.png")
plt.show()

# --------------------------------
# Forex Stability
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Forex_Reserves_Bn"],
         marker='o',
         label="Forex Reserves")

plt.plot(df["Year"],
         df["FEMA_Impact_Index"],
         marker='s',
         label="FEMA Impact")

plt.title("Forex Stability After FEMA")
plt.xlabel("Year")
plt.legend()
plt.grid(True)

plt.savefig("charts/forex_stability.png")
plt.show()

# --------------------------------
# FEMA vs FERA
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["FEMA_Impact_Index"],
         marker='o',
         linewidth=3)

plt.title("Transition from FERA to FEMA")
plt.xlabel("Year")
plt.ylabel("FEMA Impact Index")
plt.grid(True)

plt.savefig("charts/fema_vs_fera.png")
plt.show()

print("\n========== DASHBOARD COMPLETED ==========")
print("All charts saved successfully in charts folder.")