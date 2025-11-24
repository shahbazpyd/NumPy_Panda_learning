import numpy as np

# Define two 2x2 matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Concatenate along axis 1 (column-wise)
combined_cols = np.concatenate([A, B], axis=0)

print("\nConcatenate Axis 1 (Columns):")
print(combined_cols)
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]
print(f"Shape: {combined_cols.shape}") # (2, 4)