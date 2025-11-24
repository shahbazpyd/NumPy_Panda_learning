import numpy as np
# Create two small 1D datasets (e.g., two days of sensor data)
data_day_1 = np.array([10, 20, 30])
data_day_2 = np.array([40, 50, 60])

# Stack them vertically to treat them as two rows
vertical_stack = np.vstack([data_day_1, data_day_2])

print("\nVertical Stack (V-Stack):")
print(vertical_stack)
# Output:
# [[10 20 30]
#  [40 50 60]]
print(f"Shape: {vertical_stack.shape}") # (2, 3)


# Use the same data from above
horizontal_stack = np.hstack([data_day_1, data_day_2])

print("\nHorizontal Stack (H-Stack):")
print(horizontal_stack)
# Output:
# [10 20 30 40 50 60]
print(f"Shape: {horizontal_stack.shape}") # (6,)