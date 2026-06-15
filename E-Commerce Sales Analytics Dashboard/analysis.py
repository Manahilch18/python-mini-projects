import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("ecommerce_data.csv")

# Display first 5 rows
print("Sales Data:")
print(df.head())

# Total Sales
total_sales = np.sum(df['Sales'])
print("\nTotal Sales:", total_sales)

# Total Orders
total_orders = len(df)
print("Total Orders:", total_orders)

# Average Order Value
avg_order = np.mean(df['Sales'])
print("Average Order Value:", round(avg_order, 2))

# Best Selling Product
best_product = df.groupby('Product')['Quantity'].sum().idxmax()
print("Best Selling Product:", best_product)

# Sales by Product
product_sales = df.groupby('Product')['Sales'].sum()
print("\nSales by Product:")
print(product_sales)

# Monthly Sales Analysis
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.month_name()

monthly_sales = df.groupby('Month')['Sales'].sum()
print("\nMonthly Sales:")
print(monthly_sales)

# Top Customer
top_customer = df.groupby('Customer')['Sales'].sum().idxmax()
print("\nTop Customer:", top_customer)

# Sales Statistics using NumPy
print("\nSales Statistics")
print("Maximum Sale:", np.max(df['Sales']))
print("Minimum Sale:", np.min(df['Sales']))
print("Median Sale:", np.median(df['Sales']))
print("Standard Deviation:", round(np.std(df['Sales']), 2))