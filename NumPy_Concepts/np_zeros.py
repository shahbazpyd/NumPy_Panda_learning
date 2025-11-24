import numpy as np
# Create a 64x64 matrix filled with zeros (representing a blank black image)
# We specify 'dtype=np.uint8' as this is the standard data type for image pixel values.
blank_image_matrix = np.zeros((64, 64), dtype=np.uint8)

print("Blank Image Matrix (64x64):")
print(blank_image_matrix)
print(f"Shape: {blank_image_matrix.shape}")
# Output:
# [[0 0 ... 0 0]
#  [0 0 ... 0 0]
#  ...
#  [0 0 ... 0 0]]
# Shape: (64, 64)