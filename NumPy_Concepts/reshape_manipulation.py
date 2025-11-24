import numpy as np

# 1D array representing 100 pixels
flat_pixels = np.arange(100) 
print("flat_pixels:", flat_pixels)
print(f"Original 1D Shape: {flat_pixels.shape}")

# Reshape the 1D array into a 10x10 2D matrix (image)
image_matrix = flat_pixels.reshape(10, 10)
print("image_matrix:", image_matrix)

print("\nReshaped 10x10 Image Matrix (Top-Left Corner):")
print(image_matrix[:2, :4]) 
# Output (shows the first two rows and four columns):
# [[ 0  1  2  3]
#  [10 11 12 13]]
print(f"New 2D Shape: {image_matrix.shape}")

# The magical -1: NumPy can automatically calculate one dimension if you provide -1.
# Example: Reshape the 10x10 matrix into a 50x2 matrix
fifty_by_two = image_matrix.reshape(50, -1) 
print("fifty_by_two:", fifty_by_two)
print(f"\n50x2 Reshaped Shape: {fifty_by_two.shape}")