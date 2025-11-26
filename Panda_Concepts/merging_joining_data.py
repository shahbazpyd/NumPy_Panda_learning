import pandas as pd
import numpy as np

# DataFrame 1: Customer Info (Static data)
customers_data = {
    'Customer_ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'City': ['NYC', 'LA', 'NYC', 'Miami']
}
df_customers = pd.DataFrame(customers_data)

# DataFrame 2: Order History (Transaction data)
orders_data = {
    'Order_ID': [5001, 5002, 5003, 5004, 5005],
    'Customer_ID': [101, 103, 105, 101, 102], # Note: 105 is NEW, 104 is MISSING
    'Item': ['Laptop', 'Keyboard', 'Webcam', 'Monitor', 'Mouse']
}
df_orders = pd.DataFrame(orders_data)

print("--- DataFrame 1: Customers ---")
print(df_customers)
print("\n--- DataFrame 2: Orders ---")
print(df_orders)





inner_join = pd.merge(
    left=df_customers, 
    right=df_orders, 
    on='Customer_ID', 
    how='inner'
)
print("\n--- A. Inner Join (Matches in Both) ---")
print(inner_join)
# Only customers 101, 102, 103 are included.





left_join = pd.merge(
    left=df_customers, 
    right=df_orders, 
    on='Customer_ID', 
    how='left'
)
print("\n--- B. Left Join (All Customers Kept) ---")
print(left_join)
# Customer 104 is present with NaN values for Order_ID and Item.



right_join = pd.merge(
    left=df_customers, 
    right=df_orders, 
    on='Customer_ID', 
    how='right'
)
print("\n--- C. Right Join (All Orders Kept) ---")
print(right_join)
# Order 5003 (Customer 105) is present with NaN values for Name and City.



outer_join = pd.merge(
    left=df_customers, 
    right=df_orders, 
    on='Customer_ID', 
    how='outer'
)
print("\n--- D. Outer Join (All Records Kept) ---")
print(outer_join)
# Both Customer 104 (no order) and Customer 105 (no info) are present.