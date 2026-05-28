# ============================================
# Author: Saloni Tiwari
# Project: 08-1994-Service-Tax-Introduction
# File: dashboard.py
# Description:
# Service Tax Dashboard using
# Python & Matplotlib
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/service_tax_data.csv")

# --------------------------------
# Service Tax Revenue Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Service_Tax_Revenue_Cr"],
         marker='o',
         linewidth=3)

plt.title("Service Tax Revenue Growth")
plt.xlabel("Year")
plt.ylabel("Revenue (Crore)")
plt.grid(True)

plt.savefig("charts/service_tax_growth.png")
plt.show()

# --------------------------------
# Fiscal Deficit Reduction
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Fiscal_Deficit"],
         marker='o',
         linewidth=3)

plt.title("Fiscal Deficit Reduction")
plt.xlabel("Year")
plt.ylabel("Fiscal Deficit (%)")
plt.grid(True)

plt.savefig("charts/fiscal_deficit_reduction.png")
plt.show()

# --------------------------------
# Service Sector GDP Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.bar(df["Year"],
        df["Service_Sector_GDP"])

plt.title("Service Sector GDP Growth")
plt.xlabel("Year")
plt.ylabel("GDP Contribution (%)")
plt.grid(True)

plt.savefig("charts/service_sector_gdp.png")
plt.show()

# --------------------------------
# Revenue Expansion
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Taxable_Services"],
         marker='o',
         linewidth=3)

plt.title("Expansion of Taxable Services")
plt.xlabel("Year")
plt.ylabel("Number of Taxable Services")
plt.grid(True)

plt.savefig("charts/revenue_expansion.png")
plt.show()

# --------------------------------
# GST Foundation
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Service_Tax_Revenue_Cr"],
         marker='o',
         label="Service Tax Revenue")

plt.plot(df["Year"],
         df["Taxable_Services"],
         marker='s',
         label="Taxable Services")

plt.title("Foundation of GST")
plt.xlabel("Year")
plt.legend()
plt.grid(True)

plt.savefig("charts/gst_foundation.png")
plt.show()

# --------------------------------
# Tax Stability
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Service_Sector_GDP"],
         marker='o',
         label="Service GDP")

plt.plot(df["Year"],
         df["Service_Tax_Revenue_Cr"],
         marker='s',
         label="Tax Revenue")

plt.title("Service GDP vs Tax Revenue")
plt.xlabel("Year")
plt.legend()
plt.grid(True)

plt.savefig("charts/tax_stability.png")
plt.show()

print("\n========== DASHBOARD COMPLETED ==========")
print("All charts saved successfully in charts folder.")