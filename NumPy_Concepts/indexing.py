import numpy as np

# Create a 5x5 grid (0 to 24, then reshape)
grid = np.arange(25).reshape(5, 5)

print("Original Grid:")
print(grid)
# Output:
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]

# Access the element in the 3rd row (index 2) and 4th column (index 3)
element = grid[2, 3] 
print(f"\nElement at [2, 3]: {element}") 
# Output: 13