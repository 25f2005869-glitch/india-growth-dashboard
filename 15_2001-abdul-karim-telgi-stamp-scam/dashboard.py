# ============================================
# Author: Saloni Tiwari
# Project: 15-2001-Abdul-Karim-Telgi-Stamp-Scam
# File: dashboard.py
# Description:
# Dashboard Visualization of
# Telgi Stamp Scam & E-Stamping
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/telgi_stamp_scam_data.csv")

# --------------------------------
# Revenue Loss Analysis
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Stamp_Revenue_Cr"],
         marker='o',
         linewidth=3)

plt.title("Revenue Loss Analysis")
plt.xlabel("Year")
plt.ylabel("Stamp Revenue (Crore)")
plt.grid(True)

plt.savefig("charts/revenue_loss_analysis.png")
plt.show()

# --------------------------------
# Counterfeit Network Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Counterfeit_Index"],
         marker='o',
         linewidth=3)

plt.title("Counterfeit Network Growth")
plt.xlabel("Year")
plt.ylabel("Counterfeit Index")
plt.grid(True)

plt.savefig("charts/counterfeit_network_growth.png")
plt.show()

# --------------------------------
# Property Registration vs Revenue
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Property_Registrations_Lakh"],
         marker='o',
         linewidth=3,
         label="Registrations")

plt.plot(df["Year"],
         df["Stamp_Revenue_Cr"],
         marker='o',
         linewidth=3,
         label="Revenue")

plt.title("Property Registration vs Revenue")
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend()
plt.grid(True)

plt.savefig("charts/property_registration_vs_revenue.png")
plt.show()

# --------------------------------
# Fiscal Deficit Impact
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Fiscal_Deficit_Impact"],
         marker='o',
         linewidth=3)

plt.title("Fiscal Deficit Impact")
plt.xlabel("Year")
plt.ylabel("Fiscal Impact Index")
plt.grid(True)

plt.savefig("charts/fiscal_deficit_impact.png")
plt.show()

# --------------------------------
# Anomaly Detection
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Fraud_Variance"],
         marker='o',
         linewidth=3)

plt.title("Anomaly Detection")
plt.xlabel("Year")
plt.ylabel("Fraud Variance")
plt.grid(True)

plt.savefig("charts/anomaly_detection.png")
plt.show()

# --------------------------------
# Banking Sector Exposure
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Banking_Exposure"],
         marker='o',
         linewidth=3)

plt.title("Banking Sector Exposure")
plt.xlabel("Year")
plt.ylabel("Exposure Index")
plt.grid(True)

plt.savefig("charts/banking_sector_exposure.png")
plt.show()

# --------------------------------
# E-Stamping Growth
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["E_Stamping_Adoption"],
         marker='o',
         linewidth=3)

plt.title("E-Stamping Growth")
plt.xlabel("Year")
plt.ylabel("Adoption (%)")
plt.grid(True)

plt.savefig("charts/e_stamping_growth.png")
plt.show()

# --------------------------------
# Revenue Divergence
# --------------------------------
plt.figure(figsize=(8,5))

difference = (
    df["Property_Registrations_Lakh"]
    - (df["Stamp_Revenue_Cr"] / 100)
)

plt.plot(df["Year"],
         difference,
         marker='o',
         linewidth=3)

plt.title("Revenue Divergence")
plt.xlabel("Year")
plt.ylabel("Divergence Index")
plt.grid(True)

plt.savefig("charts/revenue_divergence.png")
plt.show()

# --------------------------------
# Paper vs Digital Security
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Counterfeit_Index"],
         marker='o',
         linewidth=3,
         label="Paper System Risk")

plt.plot(df["Year"],
         df["E_Stamping_Adoption"],
         marker='o',
         linewidth=3,
         label="Digital Adoption")

plt.title("Paper vs Digital Security")
plt.xlabel("Year")
plt.ylabel("Index")
plt.legend()
plt.grid(True)

plt.savefig("charts/paper_vs_digital_security.png")
plt.show()

# --------------------------------
# Fraud Variance Analysis
# --------------------------------
plt.figure(figsize=(8,5))

plt.plot(df["Year"],
         df["Fraud_Variance"],
         marker='o',
         linewidth=3)

plt.title("Fraud Variance Analysis")
plt.xlabel("Year")
plt.ylabel("Fraud Variance")
plt.grid(True)

plt.savefig("charts/fraud_variance_analysis.png")
plt.show()

print("\n========== DASHBOARD COMPLETED ==========")
print("All charts saved successfully in charts folder.")