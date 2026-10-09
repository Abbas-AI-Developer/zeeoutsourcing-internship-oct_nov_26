import pandas as pd

df = pd.read_csv(r"D:\ZeeOutsourcing Internship\ML Assignment 1\train.txt")

# First 5 rows
print("HEAD:")
print(df.head())

# Rows and columns
print("\nSHAPE:")
print(df.shape)

# Column names and data types
print("\nINFO:")
df.info()

# Statistical summary
print("\nDESCRIBE:")
print(df.describe())

# Missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())