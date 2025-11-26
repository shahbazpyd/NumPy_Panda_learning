import pandas as pd
import io

csv_data = """
OrderID,Product,Region,Sales,Units,Date,Discount
1001,Laptop,East,1200.50,2,2025-10-01,0.10
1002,Mouse,West,25.99,10,2025-10-01,0.05
1003,Keyboard,East,75.00,5,2025-10-02,0.00
1004,Monitor,North,350.75,3,2025-10-02,0.15
1005,Webcam,West,45.00,4,2025-10-03,0.00
1006,Laptop,West,1200.50,1,2025-10-03,0.10
1007,Mouse,South,15.00,8,2025-10-04,0.05
"""
df = pd.read_csv(io.StringIO(csv_data))

print("Original Data (df):")
print(df)


condition_1 = df['Sales'] > 1000

print("\n--- Condition 1 Mask (Sales > 1000) ---")
print(condition_1)
# Output (Series of True/False): 0: True, 5: True, others False



condition_2 = df['Region'] == 'West'

print("\n--- Condition 2 Mask (Region == 'West') ---")
print(condition_2)
# Output (Series of True/False): 1: True, 4: True, 5: True, others False



combined_mask = (df['Sales'] > 1000) & (df['Region'] == 'West')

print("\n--- Combined Mask (Sales > 1000 AND Region == 'West') ---")
print(combined_mask)
# Output: 5: True (Order 1006 satisfies both)



high_sales_west = df[combined_mask]

print("\n--- Filtered Results: High Sales in West Region ---")
print(high_sales_west)
# Output: Only row 5 (Order 1006)




# Create the OR condition
or_mask = (df['Product'] == 'Mouse') | (df['Units'] < 3)

# Apply the filter
result_or = df[or_mask]

print("\nFiltered by 'Mouse' OR 'Units' < 3:")
print(result_or)
# Output should include: 
# 1001 (Laptop, Units=2) 
# 1002 (Mouse)
# 1006 (Laptop, Units=1) 
# 1007 (Mouse)