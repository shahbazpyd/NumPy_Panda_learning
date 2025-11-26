import pandas as pd
import numpy as np
import io

csv_data = """
ID,Age,Salary,Join_Date,Active_Status
1,25,50000,2022-01-01,Y
2,30,NaN,2022-03-15,Y
3,NaN,75000,2022-05-20,N
4,45,90000,2022-08-10,Y
5,22,60000,NaN,Y
6,40,NaN,2023-01-01,N
"""
df = pd.read_csv(io.StringIO(csv_data))

print("Original Data Info:")
df.info()

missing_values = df.isnull().sum()
print("\n--- A. Count of Missing Values ---")
print(missing_values)
# Output confirms 1 NaN in Age, 2 NaNs in Salary, 1 NaN in Join_Date.



# Calculate the mean of the non-missing Salary values
salary_mean = df['Salary'].mean() 

# Fill the NaNs in the 'Salary' column with the calculated mean
df['Salary'].fillna(salary_mean, inplace=True) 

print(f"\nSalary Mean used for fill: {salary_mean:.2f}")
print("Salary Column after filling with mean:")
print(df['Salary'])



age_median = df['Age'].median()

# Fill the NaNs in the 'Age' column with the calculated median
df['Age'].fillna(age_median, inplace=True)

print(f"\nAge Median used for fill: {age_median:.0f}")
print("Age Column after filling with median:")
print(df['Age'])



# Drop rows where *any* value is missing (only 1 row has NaN remaining in Join_Date)
df_clean = df.dropna()

print("\n--- C. Data after dropping rows with NaNs in any column ---")
print(df_clean)
print(f"Original Rows: {len(df)}. Rows after dropna: {len(df_clean)}")




# Drop rows where *any* value is missing (only 1 row has NaN remaining in Join_Date)
df_clean = df.dropna()

print("\n--- C. Data after dropping rows with NaNs in any column ---")
print(df_clean)
print(f"Original Rows: {len(df)}. Rows after dropna: {len(df_clean)}")



# Convert Age to integer type
df_clean['Age'] = df_clean['Age'].astype(int)

# Convert Join_Date object (string) to datetime type
df_clean['Join_Date'] = pd.to_datetime(df_clean['Join_Date'])

print("\n--- D. Final Data Types Check (.info()) ---")
df_clean.info()
# Output now shows Age as int64 and Join_Date as datetime64[ns]



# Convert 'Y'/'N' to True/False:
# The expression df_clean['Active_Status'] == 'Y' creates the required Boolean mask.
df_clean['Is_Active'] = (df_clean['Active_Status'] == 'Y').astype(bool)

print("\nActive Status and new Is_Active Column:")
print(df_clean[['Active_Status', 'Is_Active']])