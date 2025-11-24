import numpy as np
# Create 50 data points evenly spaced between 0 and 10 (inclusive)
time_vector = np.linspace(0, 10, 50)

print("Time Vector (first 5 points):")
print(time_vector[:5])
print(f"Number of elements: {len(time_vector)}")
# Output:
# [ 0.          0.20408163  0.40816327  0.6122449   0.81632653]
# Number of elements: 50