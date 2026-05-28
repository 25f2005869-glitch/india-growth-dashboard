"""
Author: Saloni Tiwari
Topic: 1993 Tax Reforms Dashboard
Description: Visualization dashboard for India's 1993 tax reforms
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv("data/tax_reforms_data.csv")

# -----------------------------------
# GDP Growth Chart
# -----------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["GDP_Growth"],
    marker="o"
)

plt.title("India GDP Growth After 1993 Tax Reforms")
plt.xlabel("Year")
plt.ylabel("GDP Growth")

plt.grid(True)

plt.savefig("charts/gdp_growth.png")

plt.show()

# -----------------------------------
# Tax Revenue Growth Chart
# -----------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    df["Year"],
    df["Tax_Revenue"]
)

plt.title("Tax Revenue Growth")
plt.xlabel("Year")
plt.ylabel("Tax Revenue")

plt.grid(True)

plt.savefig("charts/tax_revenue_growth.png")

plt.show()

# -----------------------------------
# Fiscal Deficit Chart
# -----------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["Fiscal_Deficit"],
    marker="o"
)

plt.title("Fiscal Deficit Trend")
plt.xlabel("Year")
plt.ylabel("Fiscal Deficit")

plt.grid(True)

plt.savefig("charts/fiscal_deficit.png")

plt.show()

# -----------------------------------
# Inflation Trend
# -----------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["Inflation"],
    marker="o"
)

plt.title("Inflation Trend After Reforms")
plt.xlabel("Year")
plt.ylabel("Inflation")

plt.grid(True)

plt.savefig("charts/inflation_trend.png")

plt.show()

# -----------------------------------
# Customs Duty Reduction
# -----------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["Customs_Duty"],
    marker="o"
)

plt.title("Customs Duty Reduction")
plt.xlabel("Year")
plt.ylabel("Customs Duty")

plt.grid(True)

plt.savefig("charts/customs_duty_reduction.png")

plt.show()

# -----------------------------------
# Laffer Curve
# -----------------------------------

tax_rate = np.array([10,20,30,40,50,60,70,80,90])
tax_revenue = np.array([20,40,60,75,90,70,50,30,10])

plt.figure(figsize=(8,5))

plt.plot(
    tax_rate,
    tax_revenue,
    marker="o"
)

plt.title("Laffer Curve")
plt.xlabel("Tax Rate (%)")
plt.ylabel("Tax Revenue")

plt.grid(True)

plt.savefig("charts/laffer_curve.png")

plt.show()