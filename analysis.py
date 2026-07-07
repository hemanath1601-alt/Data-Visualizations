import pandas as pd

df = pd.read_excel("dataset.xlsx")

print(df.head())
print(df.info())
print(df.columns)
print(df.isnull().sum())
print(df.describe())
print(df["TotalPrice"].sum())
print(df["Product"].value_counts())
print(df["PaymentMethod"].value_counts())
print(df["OrderStatus"].value_counts())
print(df["ReferralSource"].value_counts())
import matplotlib.pyplot as plt

df["Product"].value_counts().plot(kind="bar")

plt.title("Product Sales")

plt.xlabel("Product")

plt.ylabel("Orders")

plt.show()
df["PaymentMethod"].value_counts().plot(kind="pie", autopct="%1.1f%%")

plt.title("Payment Methods")

plt.show()
df.to_excel("Cleaned_Dataset.xlsx", index=False)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ========================================
# LOAD DATASET
# ========================================

df = pd.read_excel("dataset.xlsx")

print("="*60)
print("DATA ANALYTICS PROJECT")
print("="*60)

# ========================================
# FIRST & LAST RECORDS
# ========================================

print("\nFirst 5 Records")
print(df.head())

print("\nLast 5 Records")
print(df.tail())

# ========================================
# DATASET SHAPE
# ========================================

print("\nDataset Shape")
print(df.shape)

# ========================================
# DATASET INFORMATION
# ========================================

print("\nDataset Information")
print(df.info())

# ========================================
# COLUMN NAMES
# ========================================

print("\nColumn Names")
print(df.columns)

# ========================================
# DATA TYPES
# ========================================

print("\nData Types")
print(df.dtypes)

# ========================================
# MISSING VALUES
# ========================================

print("\nMissing Values")
print(df.isnull().sum())

# ========================================
# DUPLICATE VALUES
# ========================================

duplicates = df.duplicated().sum()
print("\nDuplicate Rows :", duplicates)

df = df.drop_duplicates()

# ========================================
# CONVERT DATE COLUMN
# ========================================

df["Date"] = pd.to_datetime(df["Date"])

# ========================================
# STATISTICAL SUMMARY
# ========================================

print("\nStatistical Summary")
print(df.describe())

# ========================================
# UNIQUE PRODUCTS
# ========================================

print("\nUnique Products")
print(df["Product"].unique())

print("\nNumber of Products")
print(df["Product"].nunique())

# ========================================
# PRODUCT ANALYSIS
# ========================================

print("\nProduct Count")
print(df["Product"].value_counts())

# ========================================
# PAYMENT METHOD ANALYSIS
# ========================================

print("\nPayment Methods")
print(df["PaymentMethod"].value_counts())

# ========================================
# ORDER STATUS
# ========================================

print("\nOrder Status")
print(df["OrderStatus"].value_counts())

# ========================================
# TOTAL REVENUE
# ========================================

print("\nTotal Revenue")
print(df["TotalPrice"].sum())

# ========================================
# AVERAGE ORDER VALUE
# ========================================

print("\nAverage Order Value")
print(df["TotalPrice"].mean())

# ========================================
# MAXIMUM ORDER VALUE
# ========================================

print("\nMaximum Order")
print(df["TotalPrice"].max())

# ========================================
# MINIMUM ORDER VALUE
# ========================================

print("\nMinimum Order")
print(df["TotalPrice"].min())

# ========================================
# TOP CUSTOMERS
# ========================================

print("\nTop 10 Customers")
print(df["CustomerID"].value_counts().head(10))

# ========================================
# MONTHLY SALES
# ========================================

monthly_sales = df.groupby(df["Date"].dt.month)["TotalPrice"].sum()

print("\nMonthly Sales")
print(monthly_sales)

# ========================================
# BAR CHART
# ========================================

plt.figure(figsize=(10,5))

df["Product"].value_counts().plot(kind="bar")

plt.title("Product Sales")

plt.xlabel("Product")

plt.ylabel("Orders")

plt.tight_layout()

plt.show()

# ========================================
# PIE CHART
# ========================================

plt.figure(figsize=(7,7))

df["PaymentMethod"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Payment Methods")

plt.ylabel("")

plt.show()

# ========================================
# LINE CHART
# ========================================

plt.figure(figsize=(10,5))

monthly_sales.plot(marker="o")

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Revenue")

plt.grid()

plt.show()

# ========================================
# HISTOGRAM
# ========================================

plt.figure(figsize=(8,5))

plt.hist(df["TotalPrice"], bins=20)

plt.title("Total Price Distribution")

plt.xlabel("Total Price")

plt.ylabel("Frequency")

plt.show()

# ========================================
# BOX PLOT
# ========================================

plt.figure(figsize=(6,5))

plt.boxplot(df["TotalPrice"])

plt.title("Total Price Boxplot")

plt.show()

# ========================================
# SCATTER PLOT
# ========================================

plt.figure(figsize=(8,5))

plt.scatter(df["Quantity"], df["TotalPrice"])

plt.title("Quantity vs Total Price")

plt.xlabel("Quantity")

plt.ylabel("Total Price")

plt.show()

# ========================================
# SAVE CLEANED DATASET
# ========================================

df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("\nCleaned dataset saved successfully.")

print("\nProject Completed Successfully.")