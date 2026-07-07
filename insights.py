import pandas as pd

# Load Dataset
df = pd.read_excel("dataset.xlsx")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

print("="*60)
print("BUSINESS INSIGHTS")
print("="*60)

# 1. Total Revenue
print("\n1. Total Revenue")
print("₹", round(df["TotalPrice"].sum(), 2))

# 2. Total Orders
print("\n2. Total Orders")
print(len(df))

# 3. Total Customers
print("\n3. Total Customers")
print(df["CustomerID"].nunique())

# 4. Best Selling Product
print("\n4. Best Selling Product")
print(df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(1))

# 5. Highest Revenue Product
print("\n5. Highest Revenue Product")
print(df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False).head(1))

# 6. Most Used Payment Method
print("\n6. Most Used Payment Method")
print(df["PaymentMethod"].mode()[0])

# 7. Most Common Order Status
print("\n7. Most Common Order Status")
print(df["OrderStatus"].mode()[0])

# 8. Average Order Value
print("\n8. Average Order Value")
print(round(df["TotalPrice"].mean(),2))

# 9. Highest Order Value
print("\n9. Highest Order Value")
print(df["TotalPrice"].max())

# 10. Lowest Order Value
print("\n10. Lowest Order Value")
print(df["TotalPrice"].min())