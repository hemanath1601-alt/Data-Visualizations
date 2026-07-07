import streamlit as st
import pandas as pd
import plotly.express as px
import os

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
file = "dataset.xlsx"

if not os.path.exists(file):
    st.error("dataset.xlsx not found in project folder.")
    st.stop()

df = pd.read_excel(file)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Filters")

products = st.sidebar.multiselect(
    "Select Product",
    options=sorted(df["Product"].unique()),
    default=sorted(df["Product"].unique())
)

payments = st.sidebar.multiselect(
    "Payment Method",
    options=sorted(df["PaymentMethod"].unique()),
    default=sorted(df["PaymentMethod"].unique())
)

status = st.sidebar.multiselect(
    "Order Status",
    options=sorted(df["OrderStatus"].unique()),
    default=sorted(df["OrderStatus"].unique())
)

filtered_df = df[
    (df["Product"].isin(products)) &
    (df["PaymentMethod"].isin(payments)) &
    (df["OrderStatus"].isin(status))
]

# -----------------------------
# Dashboard Title
# -----------------------------
st.title("📊 E-Commerce Sales Dashboard")

st.markdown("---")

# -----------------------------
# KPI Cards
# -----------------------------
total_revenue = filtered_df["TotalPrice"].sum()
total_orders = len(filtered_df)
customers = filtered_df["CustomerID"].nunique()
avg_order = filtered_df["TotalPrice"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Revenue", f"₹{total_revenue:,.2f}")
col2.metric("📦 Orders", total_orders)
col3.metric("👥 Customers", customers)
col4.metric("🛒 Avg Order", f"₹{avg_order:,.2f}")

st.markdown("---")

# -----------------------------
# Top Products
# -----------------------------
st.subheader("Top Selling Products")

product_sales = (
    filtered_df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    product_sales,
    x="Product",
    y="Quantity",
    color="Quantity",
    text="Quantity"
)

st.plotly_chart(fig, width="stretch")

# -----------------------------
# Payment Methods
# -----------------------------
st.subheader("Payment Method Distribution")

fig = px.pie(
    filtered_df,
    names="PaymentMethod",
    hole=0.4
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Order Status
# -----------------------------
st.subheader("Order Status")

status_df = (
    filtered_df["OrderStatus"]
    .value_counts()
    .reset_index()
)

status_df.columns = ["OrderStatus", "Count"]

fig = px.bar(
    status_df,
    x="OrderStatus",
    y="Count",
    color="OrderStatus",
    text="Count"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Monthly Revenue
# -----------------------------
st.subheader("Monthly Revenue")

monthly = (
    filtered_df
    .groupby(filtered_df["Date"].dt.strftime("%B"))["TotalPrice"]
    .sum()
    .reset_index()
)

monthly.columns = ["Month", "Revenue"]

fig = px.line(
    monthly,
    x="Month",
    y="Revenue",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Revenue by Product
# -----------------------------
st.subheader("Revenue by Product")

revenue_product = (
    filtered_df.groupby("Product")["TotalPrice"]
    .sum()
    .reset_index()
)

fig = px.bar(
    revenue_product,
    x="Product",
    y="TotalPrice",
    color="TotalPrice",
    text_auto=True
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Scatter Plot
# -----------------------------
st.subheader("Quantity vs Total Price")

fig = px.scatter(
    filtered_df,
    x="Quantity",
    y="TotalPrice",
    color="Product",
    hover_data=["CustomerID"]
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Raw Data
# -----------------------------
st.subheader("Dataset")

st.dataframe(filtered_df)

# -----------------------------
# Download Cleaned Dataset
# -----------------------------
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download CSV",
    csv,
    "Filtered_Data.csv",
    "text/csv"
)

st.success("Dashboard Loaded Successfully!")