import numpy as np
color_image = np.ones((10, 10, 3), dtype=np.int16)
print(f"color_image: {color_image}")
print(f"Shape: {color_image.shape}") 
# Output: (10, 10, 3)

print(f"Dimensions: {color_image.ndim}")
# Output: 3

print(f"Data Type: {color_image.dtype}")
# Output: int16