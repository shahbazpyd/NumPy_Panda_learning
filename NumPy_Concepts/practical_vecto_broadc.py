import numpy as np

# Create 10,000 random data points (simulating sensor readings or test scores)
data_points = np.random.randn(10000) * 10 + 50 # Mean ~50, Std Dev ~10
print("data_points",data_points)
# Step 1: Calculate Mean (mu) and Standard Deviation (sigma) using NumPy's aggregate functions.
# These operations are already vectorized!
mu = np.mean(data_points)
sigma = np.std(data_points)

print(f"Data Mean (mu): {mu:.4f}")
print(f"Data Std Dev (sigma): {sigma:.4f}")

# Step 2: Apply the normalization formula using Vectorization and Broadcasting.
# NumPy automatically subtracts the scalar 'mu' from every element 
# and divides every element by the scalar 'sigma'.
normalized_data = (data_points - mu) / sigma
print("normalized_data", normalized_data)
# Check the results: Normalized data should have a mean close to 0 and std dev close to 1
print(f"\nNormalized Data Mean: {np.mean(normalized_data):.4f}")
print(f"Normalized Data Std Dev: {np.std(normalized_data):.4f}")

# Compare speed (conceptually): This operation on 10,000 points takes microseconds, 
# while a Python for loop would be significantly slower.