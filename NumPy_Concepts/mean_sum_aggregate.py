import numpy as np

# Simulate scores (4 students, 3 subjects)
scores = np.array([
    [85, 90, 78],  # Student 1
    [70, 88, 92],  # Student 2
    [95, 75, 80],  # Student 3
    [60, 65, 70]   # Student 4
])

print("Student Scores Matrix:")
print(scores)
print(f"Shape: {scores.shape}") # (4, 3)


# Calculate the overall average score for ALL students and ALL tests
overall_mean = np.mean(scores)
print(f"\nOverall Mean Score (All data points): {overall_mean:.2f}") 
# Output: Mean of all 12 scores.


# Calculate the average score for each test (column-wise mean)
mean_by_test = np.mean(scores, axis=0)

print("\nMean Score for Each Test (axis=0):")
print(mean_by_test)
# Output: [77.5 79.5 80.0]
# Result is a 1D array of shape (3,).



# Calculate the total score for each student (row-wise sum)
total_by_student = np.sum(scores, axis=1)

print("\nTotal Score for Each Student (axis=1):")
print(total_by_student)
# Output: [253 250 250 195]
# Result is a 1D array of shape (4,).



# Simulated data (Rows=Months, Cols=Products)
sales_data = np.array([
    [100, 250, 400, 150],  # Month 1
    [110, 240, 390, 145],  # Month 2
    [90, 260, 410, 160],   # Month 3
])

# To find the minimum sales for *each product* (columns), we must collapse the rows.
# Collapse Rows = axis=0
min_sales_by_product = np.min(sales_data, axis=0)

print(f"Sales Data Shape: {sales_data.shape}") # (3, 4)
print(f"Min Sales for Each Product: {min_sales_by_product}") 
# Output: [ 90 240 390 145]