import pandas as pd
import numpy as np
import io

csv_data = """
OrderID,Product,Region,Sales,Units,Date,Discount
1001,Laptop,East,1200.50,2,2025-10-01,0.10
1002,Mouse,West,25.99,10,2025-10-01,0.05
1003,Keyboard,East,75.00,5,2025-10-02,0.00
1004,Monitor,North,350.75,3,2025-10-02,0.15
1005,Webcam,East,45.00,4,2025-10-03,0.00
1006,Laptop,West,1200.50,1,2025-10-03,0.10
1007,Mouse,South,15.00,8,2025-10-04,0.05
"""
df = pd.read_csv(io.StringIO(csv_data))

print("Original DataFrame (df):\n", df.head(3))

# Access the 'Sales' column using dot notation
sales_series = df.Sales 

print("\n--- A. Single Column (Series) ---")
print(sales_series.head(3))
print(f"Type: {type(sales_series)}")
# Output: <class 'pandas.core.series.Series'>



# Access the 'Product' column using bracket notation
product_series = df['Product']
print(product_series.tail(2))
print(f"\nType: {type(product_series)}")



# Calculate the total sales value (sum of all elements in the 'Sales' Series)
total_sales = df['Sales'].sum()

print(f"Total Sales from Series: ${total_sales:.2f}")



# Access 'Product', 'Units', and 'Sales' using a list of columns
sales_metrics_df = df[['Product', 'Units', 'Sales']]

print("\n--- B. Multiple Columns (DataFrame Subset) ---")
print(sales_metrics_df.head(3))
print(f"Type: {type(sales_metrics_df)}")
# Output: <class 'pandas.core.frame.DataFrame'>


# Calculate the maximum value for *each* numerical column in the subset
max_values = sales_metrics_df[['Units', 'Sales']].max()

print("\nMax Units and Max Sales:")
print(max_values)


# 1. Access Discount (Series) and calculate mean
mean_discount = df.Discount.mean()
print(f"Mean Discount: {mean_discount:.4f}")

# 2. Access OrderID and Date (DataFrame) and check shape
id_date_df = df[['OrderID', 'Date']]
print(f"OrderID and Date Shape: {id_date_df.shape}") 
# Output: (7, 2)