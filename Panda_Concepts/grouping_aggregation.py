import pandas as pd
import io

csv_data = """
Month,Product_Category,Price,Units_Sold,Cost,Region
Jan,Electronics,1200,2,800,North
Jan,Apparel,50,15,20,South
Feb,Electronics,150,5,100,North
Feb,Apparel,60,10,25,South
Mar,Electronics,1000,1,650,West
Mar,Apparel,45,20,15,West
"""
df = pd.read_csv(io.StringIO(csv_data))

# Calculate a 'Profit' column first
df['Profit'] = (df['Price'] - df['Cost']) * df['Units_Sold']

print("DataFrame Head:")
print(df.head())




avg_price_by_category = df.groupby('Product_Category')['Price'].mean()

print("\n--- A. Average Price by Category ---")
print(avg_price_by_category)
# Output:
# Product_Category
# Apparel       51.666667
# Electronics  783.333333




monthly_summary = df.groupby('Month').agg(
    Total_Profit=('Profit', 'sum'),
    Total_Units=('Units_Sold', 'sum'),
    Min_Price=('Price', 'min') # Add a third aggregation just for fun
)

print("\n--- B. Monthly Summary using .agg() ---")
print(monthly_summary)
# Output (shows sums for Profit and Units, and min for Price, grouped by Month):
#       Total_Profit  Total_Units  Min_Price
# Month
# Feb          250.0           15         60
# Jan         840.00           17         50
# Mar         370.00           21         45




# Group by Region FIRST, then by Product_Category SECOND
regional_product_profit = df.groupby(['Region', 'Product_Category'])['Profit'].sum()

print("\n--- C. Profit by Region and Category (Multi-Index Result) ---")
print(regional_product_profit)
# Output is a Series with a Multi-Index:
# Region  Product_Category
# North   Electronics          800.0
#         Apparel              450.0
# South   Electronics          250.0
#         Apparel              350.0
# ...