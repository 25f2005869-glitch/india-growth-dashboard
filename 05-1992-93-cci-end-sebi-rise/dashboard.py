# ============================================
# Author: Saloni Tiwari
# Project: 05-1992-93-CCI-End-SEBI-Rise
# File: dashboard.py
# Description:
# Data Visualization Dashboard using
# Matplotlib for SEBI Reforms Analysis
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/sebi_reforms_data.csv")

# -------------------------------
# 1. Capital Raised Growth
# -------------------------------
plt.figure(figsize=(8,5))
plt.plot(df["Year"], df["Capital_Raised_Cr"],
         marker='o', linewidth=3)

plt.title("Capital Raised Growth After SEBI")
plt.xlabel("Year")
plt.ylabel("Capital Raised (Crore)")
plt.grid(True)

plt.savefig("charts/capital_raised_growth.png")
plt.show()

# -------------------------------
# 2. Market Volatility
# -------------------------------
plt.figure(figsize=(8,5))
plt.plot(df["Year"], df["Volatility_Index"],
         marker='o', linewidth=3)

plt.title("Market Volatility Reduction")
plt.xlabel("Year")
plt.ylabel("Volatility Index")
plt.grid(True)

plt.savefig("charts/market_volatility.png")
plt.show()

# -------------------------------
# 3. Investor Protection
# -------------------------------
plt.figure(figsize=(8,5))
plt.bar(df["Year"],
        df["Investor_Complaints_Resolved"])

plt.title("Investor Complaints Resolved")
plt.xlabel("Year")
plt.ylabel("Resolved Complaints")
plt.grid(True)

plt.savefig("charts/investor_protection.png")
plt.show()

# -------------------------------
# 4. SEBI Growth Era
# -------------------------------
sebi_df = df[df["Era"] == "SEBI"]

plt.figure(figsize=(8,5))
plt.plot(sebi_df["Year"],
         sebi_df["Capital_Raised_Cr"],
         marker='o', linewidth=3)

plt.title("SEBI Era Capital Market Growth")
plt.xlabel("Year")
plt.ylabel("Capital Raised")
plt.grid(True)

plt.savefig("charts/sebi_growth.png")
plt.show()

# -------------------------------
# 5. Market Modernization
# -------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Capital_Raised_Cr"],
         marker='o',
         label="Capital Raised")

plt.plot(df["Year"],
         df["Volatility_Index"],
         marker='s',
         label="Volatility")

plt.title("Market Modernization After SEBI")
plt.xlabel("Year")
plt.legend()
plt.grid(True)

plt.savefig("charts/market_modernization.png")
plt.show()

print("\n========== DASHBOARD COMPLETED ==========")
print("All charts saved successfully in charts folder.")