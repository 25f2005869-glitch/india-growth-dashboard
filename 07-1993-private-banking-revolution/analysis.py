# ============================================
# Author: Saloni Tiwari
# Project: 07-1993-Private-Banking-Revolution
# File: analysis.py
# Description:
# Statistical Analysis of India's
# Private Banking Revolution
# ============================================

import pandas as pd

# Load Dataset
df = pd.read_csv("data/private_banking_data.csv")

print("\n========== DATASET ==========\n")
print(df)

# Data Info
print("\n========== DATA INFO ==========\n")
print(df.info())

# Summary Statistics
print("\n========== SUMMARY STATISTICS ==========\n")
print(df.describe())

# ATM Expansion
print("\n========== ATM EXPANSION ==========\n")
print("Maximum ATM Count:",
      df["ATM_Count"].max())

# Credit Growth
print("\n========== PRIVATE CREDIT ==========\n")
print("Maximum Credit Flow:",
      df["Private_Credit_Cr"].max())

# GDP Growth
print("\n========== GDP GROWTH ==========\n")
print("Maximum GDP Growth:",
      df["GDP_Growth"].max())

# NPA Analysis
print("\n========== NPA ANALYSIS ==========\n")
print("Lowest NPA Ratio:",
      df["NPA_Ratio"].min())

# Customer Service
print("\n========== CUSTOMER SERVICE ==========\n")
print("Highest Service Index:",
      df["Customer_Service_Index"].max())

# Correlation
print("\n========== CORRELATION ==========\n")
print(df.corr(numeric_only=True))