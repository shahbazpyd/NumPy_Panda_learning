import pandas as pd
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
# Set 'OrderID' as the index, which makes it the row label
df.set_index('OrderID', inplace=True) 

print("DataFrame Index:")
print(df.index.tolist())
# Index: [1001, 1002, 1003, 1004, 1005, 1006, 1007]


# Select the 'Sales' value for the order with ID 1004
sales_value = df.loc[1004, 'Sales']
print(f"\nSales for Order 1004: {sales_value}")
# Output: 350.75


# Select rows from OrderID 1003 up to and INCLUDING 1006, 
# and only the 'Product' and 'Region' columns.
subset_label = df.loc[1003:1006, ['Product', 'Region']]
print("\nSubset (1003 to 1006, Product/Region):\n", subset_label)



# Select the element in the 3rd row (index 2) and 2nd column (index 1, 'Region')
region_value = df.iloc[2, 1]
print(f"\nRegion for the 3rd row: {region_value}") 
# Output: East



# Select rows starting from the 3rd-to-last (-3) to the end (:)
# Select columns from the start (:) up to the 5th column (4, exclusive)
subset_position = df.iloc[-3:, :4] 
print("\nSubset (Last 3 Rows, First 4 Cols):\n", subset_position)



# 1. Label-based selection (.loc[])
result_loc = df.loc[1002, ['Sales', 'Units']]
print(f"Sales and Units for 1002:\n{result_loc}")
# Output: 
# Sales    25.99
# Units    10.00

# 2. Position-based selection (.iloc[])
result_iloc = df.iloc[-1, :] # -1 for last row, : for all columns
print(f"\nData for the last row:\n{result_iloc}")
# Output: (Row 1007)
# Product      Mouse
# Region       South
# Sales       15.00
# Units        8.00
# ...