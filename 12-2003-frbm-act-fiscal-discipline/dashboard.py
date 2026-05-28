# ============================================
# Author: Saloni Tiwari
# Project: 12-2003-FRBM-Act-Fiscal-Discipline
# File: dashboard.py
# Description:
# FRBM Fiscal Discipline Dashboard
# using Python & Matplotlib
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/frbm_fiscal_data.csv")

# --------------------------------
# Fiscal Deficit Reduction
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Fiscal_Deficit_GDP"],
         marker='o',
         linewidth=3)

plt.title("Fiscal Deficit Reduction")
plt.xlabel("Year")
plt.ylabel("Fiscal Deficit (% GDP)")
plt.grid(True)

plt.savefig("charts/fiscal_deficit_reduction.png")
plt.show()

# --------------------------------
# Revenue Deficit Control
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Revenue_Deficit_GDP"],
         marker='o',
         linewidth=3)

plt.title("Revenue Deficit Reduction")
plt.xlabel("Year")
plt.ylabel("Revenue Deficit (% GDP)")
plt.grid(True)

plt.savefig("charts/revenue_deficit_control.png")
plt.show()

# --------------------------------
# Debt Stability
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Public_Debt_GDP"],
         marker='o',
         linewidth=3)

plt.title("Public Debt Stability")
plt.xlabel("Year")
plt.ylabel("Debt-to-GDP Ratio")
plt.grid(True)

plt.savefig("charts/debt_stability.png")
plt.show()

# --------------------------------
# Inflation Control
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Inflation_Rate"],
         marker='o',
         linewidth=3)

plt.title("Inflation Stability")
plt.xlabel("Year")
plt.ylabel("Inflation Rate (%)")
plt.grid(True)

plt.savefig("charts/inflation_control.png")
plt.show()

# --------------------------------
# Credit Rating Improvement
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Credit_Rating_Index"],
         marker='o',
         linewidth=3)

plt.title("Sovereign Credit Rating Improvement")
plt.xlabel("Year")
plt.ylabel("Credit Rating Index")
plt.grid(True)

plt.savefig("charts/credit_rating_improvement.png")
plt.show()

# --------------------------------
# Fiscal Variance Stability
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Fiscal_Deficit_GDP"],
         marker='o',
         label="Fiscal Deficit")

plt.plot(df["Year"],
         df["Inflation_Rate"],
         marker='s',
         label="Inflation")

plt.title("Fiscal Stability & Variance Reduction")
plt.xlabel("Year")
plt.legend()
plt.grid(True)

plt.savefig("charts/fiscal_variance_stability.png")
plt.show()

# --------------------------------
# FRBM Reform Impact
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["FDI_Inflows_Bn"],
         marker='o',
         label="FDI Inflows")

plt.plot(df["Year"],
         df["Credit_Rating_Index"],
         marker='s',
         label="Credit Rating")

plt.title("FRBM Reform Impact")
plt.xlabel("Year")
plt.legend()
plt.grid(True)

plt.savefig("charts/frbm_reforms_impact.png")
plt.show()

print("\n========== DASHBOARD COMPLETED ==========")
print("All charts saved successfully in charts folder.")