# ============================================
# Author: Saloni Tiwari
# Project: 13-2006-MGNREGA
# File: dashboard.py
# Description:
# MGNREGA Rural Employment Dashboard
# using Python & Matplotlib
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/mgnrega_data.csv")

# --------------------------------
# Leakage Variance
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Leakage_Index"],
         marker='o',
         linewidth=3)

plt.title("Leakage Variance Reduction")
plt.xlabel("Year")
plt.ylabel("Leakage Index")
plt.grid(True)

plt.savefig("charts/leakage_variance.png")
plt.show()

# --------------------------------
# DBT Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["DBT_Coverage"],
         marker='o',
         linewidth=3)

plt.title("DBT Coverage Growth")
plt.xlabel("Year")
plt.ylabel("DBT Coverage (%)")
plt.grid(True)

plt.savefig("charts/dbt_growth.png")
plt.show()

# --------------------------------
# Rural Employment Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Employment_Crore"],
         marker='o',
         linewidth=3)

plt.title("Rural Employment Growth")
plt.xlabel("Year")
plt.ylabel("Employment (Crore)")
plt.grid(True)

plt.savefig("charts/rural_employment_growth.png")
plt.show()

# --------------------------------
# Migration Reduction
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Rural_Migration_Index"],
         marker='o',
         linewidth=3)

plt.title("Rural Migration Reduction")
plt.xlabel("Year")
plt.ylabel("Migration Index")
plt.grid(True)

plt.savefig("charts/migration_reduction.png")
plt.show()

# --------------------------------
# Banking Linkage
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Bank_Linkage"],
         marker='o',
         linewidth=3)

plt.title("Banking Linkage Growth")
plt.xlabel("Year")
plt.ylabel("Bank Linkage (%)")
plt.grid(True)

plt.savefig("charts/banking_linkage.png")
plt.show()

# --------------------------------
# Women Participation
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Women_Participation"],
         marker='o',
         linewidth=3)

plt.title("Women Participation Growth")
plt.xlabel("Year")
plt.ylabel("Women Participation (%)")
plt.grid(True)

plt.savefig("charts/women_participation.png")
plt.show()

print("\n========== DASHBOARD COMPLETED ==========")
print("All charts saved successfully in charts folder.")