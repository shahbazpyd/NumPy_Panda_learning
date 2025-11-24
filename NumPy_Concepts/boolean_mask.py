import numpy as np

# Simulate 12 sales figures
sales = np.array([550, 810, 320, 950, 480, 750, 610, 1020, 500, 770, 900, 200])

# Define the threshold
threshold = 750


# Create the mask: Are sales greater than the threshold?
high_performance_mask = sales > threshold

print(f"Original Sales: {sales}")
print(f"Boolean Mask:   {high_performance_mask}")
# Output:
# [False  True False  True False False False  True False  True  True False]


# Apply the mask to filter the original 'sales' array
high_sales_figures = sales[high_performance_mask]

print(f"\nSales Figures Above {threshold}: {high_sales_figures}")
# Output: [ 810  950 1020  770  900]




# Create a new combined mask
combined_mask = (sales > 750) & (sales < 1000)
print("combined_mask", combined_mask)
# Apply the combined mask
mid_to_high_sales = sales[combined_mask]

print(f"\nSales between 750 and 1000: {mid_to_high_sales}")
# Output: [810 950 770 900]



temperatures = np.array([22, 25, 31, 18, 29, 35, 20, 28])

# We need two conditions combined with OR:
# Condition 1: Temp < 20 (too cold)
# Condition 2: Temp > 30 (too hot)

outlier_mask = (temperatures < 20) | (temperatures > 30)

outliers = temperatures[outlier_mask]

print(f"Original Temperatures: {temperatures}")
print(f"Outliers (Below 20 OR Above 30): {outliers}")
# Output: [31 18 35]