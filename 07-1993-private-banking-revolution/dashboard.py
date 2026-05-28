# ============================================
# Author: Saloni Tiwari
# Project: 07-1993-Private-Banking-Revolution
# File: dashboard.py
# Description:
# Banking Revolution Dashboard using
# Python & Matplotlib
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/private_banking_data.csv")

# --------------------------------
# Private Credit Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Private_Credit_Cr"],
         marker='o',
         linewidth=3)

plt.title("Private Sector Credit Growth")
plt.xlabel("Year")
plt.ylabel("Credit Flow (Crore)")
plt.grid(True)

plt.savefig("charts/private_credit_growth.png")
plt.show()

# --------------------------------
# ATM Expansion
# --------------------------------
plt.figure(figsize=(8,5))

plt.bar(df["Year"],
        df["ATM_Count"])

plt.title("ATM Expansion in India")
plt.xlabel("Year")
plt.ylabel("ATM Count")
plt.grid(True)

plt.savefig("charts/atm_expansion.png")
plt.show()

# --------------------------------
# Banking Efficiency
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Customer_Service_Index"],
         marker='o',
         linewidth=3)

plt.title("Banking Service Efficiency")
plt.xlabel("Year")
plt.ylabel("Service Index")
plt.grid(True)

plt.savefig("charts/banking_efficiency.png")
plt.show()

# --------------------------------
# NPA Management
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["NPA_Ratio"],
         marker='o',
         linewidth=3)

plt.title("NPA Ratio Reduction")
plt.xlabel("Year")
plt.ylabel("NPA Ratio")
plt.grid(True)

plt.savefig("charts/npa_management.png")
plt.show()

# --------------------------------
# Financial Inclusion
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Private_Banks"],
         marker='o',
         linewidth=3)

plt.title("Growth of Private Banks")
plt.xlabel("Year")
plt.ylabel("Number of Private Banks")
plt.grid(True)

plt.savefig("charts/financial_inclusion.png")
plt.show()

# --------------------------------
# GDP & Credit Correlation
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Private_Credit_Cr"],
         marker='o',
         label="Credit Flow")

plt.plot(df["Year"],
         df["GDP_Growth"],
         marker='s',
         label="GDP Growth")

plt.title("GDP Growth vs Credit Expansion")
plt.xlabel("Year")
plt.legend()
plt.grid(True)

plt.savefig("charts/gdp_credit_correlation.png")
plt.show()

print("\n========== DASHBOARD COMPLETED ==========")
print("All charts saved successfully in charts folder.")