import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_excel("Sample - Superstore.xls")
# If CSV:
# df = pd.read_csv("Superstore.csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print(f"Total Sales : ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")

# Sales by Category
sales_category = df.groupby("Category", as_index=False)["Sales"].sum()

# Profit by Category
profit_category = df.groupby("Category", as_index=False)["Profit"].sum()

# Monthly Sales Trend
monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M").astype(str), as_index=False)["Sales"].sum()
)

# Charts
fig1 = px.bar(
    sales_category,
    x="Category",
    y="Sales",
    title="Sales by Category",
    color="Category"
)

fig2 = px.bar(
    profit_category,
    x="Category",
    y="Profit",
    title="Profit by Category",
    color="Category"
)

fig3 = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    title="Monthly Sales Trend",
    markers=True
)

# Save charts
fig1.write_html("sales_by_category.html")
fig2.write_html("profit_by_category.html")
fig3.write_html("monthly_sales_trend.html")

fig1.show()
fig2.show()
fig3.show()