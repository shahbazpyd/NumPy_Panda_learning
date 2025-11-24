import numpy as np
# 1. Create simulated data (30 days x 24 hours)
# Using random data for realism
sensor_data = np.random.randint(20, 35, size=(30, 24)) 
print(f"Full Data Shape: {sensor_data.shape}")

# 2. Extract the Subset:
# Days 7 through 13 (inclusive) map to indices 6 through 14 (exclusive: 6:14)
# Hours 12 (noon) and 13 (1 PM) map to indices 12 and 13 (exclusive: 12:14)

subset = sensor_data[6:14, 12:14]

print(f"\nSubset Shape (Days x Hours): {subset.shape}") 
# Output: (8, 2)  (8 days, 2 hours)
print("\nExtracted Subset (First 5 Rows):")
print(subset[:5])