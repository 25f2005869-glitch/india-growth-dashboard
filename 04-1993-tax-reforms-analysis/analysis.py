"""
Author: Saloni Tiwari
Topic: 1993 Tax Reforms Analysis
Description: Statistical analysis of India's 1993 tax reforms data
"""

import pandas as pd

# Load dataset
df = pd.read_csv("data/tax_reforms_data.csv")

print("\n========== 1993 TAX REFORMS ANALYSIS ==========\n")

# Display dataset
print("Dataset Preview:\n")
print(df)

# GDP Growth Analysis
print("\n========== GDP GROWTH ==========\n")
print("Maximum GDP Growth:", df["GDP_Growth"].max())
print("Average GDP Growth:", df["GDP_Growth"].mean())

# Tax Revenue Analysis
print("\n========== TAX REVENUE ==========\n")
print("Maximum Tax Revenue:", df["Tax_Revenue"].max())
print("Average Tax Revenue:", df["Tax_Revenue"].mean())

# Fiscal Deficit Analysis
print("\n========== FISCAL DEFICIT ==========\n")
print("Minimum Fiscal Deficit:", df["Fiscal_Deficit"].min())

# Inflation Analysis
print("\n========== INFLATION ==========\n")
print("Maximum Inflation:", df["Inflation"].max())

# Customs Duty Analysis
print("\n========== CUSTOMS DUTY ==========\n")
print("Minimum Customs Duty:", df["Customs_Duty"].min())

# Corporate Tax Analysis
print("\n========== CORPORATE TAX ==========\n")
print("Minimum Corporate Tax:", df["Corporate_Tax"].min())

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())