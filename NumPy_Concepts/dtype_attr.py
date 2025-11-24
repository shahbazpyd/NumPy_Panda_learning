import numpy as np

# 1D Array (from np.linspace)
time_vector = np.linspace(0, 10, 50) 

# 2D Array (from np.zeros)
blank_image_matrix = np.zeros((64, 64), dtype=np.uint8)

# Check the shape of the 1D array
print(f"Time Vector Shape: {time_vector.shape}") 
# Output: (50,) -> The comma indicates it's a 1-dimensional array of 50 elements.

# Check the shape of the 2D matrix
print(f"Image Matrix Shape: {blank_image_matrix.shape}")
# Output: (64, 64) -> This confirms it has 64 rows and 64 columns.

# Example Diagnosis: If you were expecting a 100x100 image and got (64, 64), 
# the shape immediately tells you something went wrong during loading.


# Check the number of dimensions
print(f"Time Vector Dimensions (.ndim): {time_vector.ndim}") 
# Output: 1 (A simple line of data)

print(f"Image Matrix Dimensions (.ndim): {blank_image_matrix.ndim}")
# Output: 2 (A grid/table of data)



# Check the data type
print(f"Time Vector Data Type (.dtype): {time_vector.dtype}") 
# Output: float64 (Default for linspace/calculations)

print(f"Image Matrix Data Type (.dtype): {blank_image_matrix.dtype}")
# Output: uint8 (Unsigned 8-bit integer, standard for grayscale pixels)

# Important Note: If you were calculating averages, you would want a 'float' type 
# to avoid losing precision due to integer truncation.