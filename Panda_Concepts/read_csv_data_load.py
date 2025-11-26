import pandas as pd
import numpy as np
import io # Used to simulate a file for this example

# Simulated CSV content (usually you'd read a physical file)
csv_data = """
OrderID,Product,Region,Sales,Units,Date,Discount
1001,Laptop,East,1200.50,2,2025-10-01,0.10
1002,Mouse,West,25.99,10,2025-10-01,0.05
1003,Keyboard,East,75.00,5,2025-10-02,0.00
1004,Monitor,North,350.75,3,2025-10-02,0.15
1005,Webcam,East,45.00,NaN,2025-10-03,0.00
1006,Laptop,West,1200.50,1,2025-10-03,0.10
1007,Mouse,South,NaN,8,2025-10-04,0.05
"""

# Load the data into a DataFrame
file= io.StringIO(csv_data)
print("file", file)
df = pd.read_csv(file)

print("Data Loaded Successfully.", df)


print("\n--- A. Quick Peek (.head()) ---")
print(df.head(3))

print("\n--- A. Quick Peek (.tail()) ---")
print(df.tail(3))


print("\n--- B. Structural Info (.info()) ---")
df.info()
# Diagnosis: Note the 'Units' and 'Sales' columns have less than 7 non-null values, 
# indicating missing data (NaN) that needs cleaning.
# Also, 'Date' is likely an 'object' (string) and needs to be converted later.



print("\n--- C. Statistical Summary (.describe()) ---")
print(df.describe())
# Diagnosis: Look at 'Sales'. The 'max' is 1200.50, and 'min' is 25.99. 
# Are these ranges reasonable? The '50%' quartile (median) is 350.75.


print("\n--- D. Column Names ---")
print(df.columns.tolist())