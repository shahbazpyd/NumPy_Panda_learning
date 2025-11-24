import numpy as np

# 1. Simulate the data
morning_purchases = np.random.randint(1, 100, size=(10, 2))
afternoon_purchases = np.random.randint(1, 100, size=(5, 2))
print(morning_purchases,"&", afternoon_purchases)


# 2. Combine them row-wise (vertically)
all_purchases = np.vstack([morning_purchases, afternoon_purchases])
print("all_purchases",all_purchases)
print(f"Morning Purchases Shape: {morning_purchases.shape}")
print(f"Afternoon Purchases Shape: {afternoon_purchases.shape}")
print(f"Combined Purchases Shape: {all_purchases.shape}")
# Output: (15, 2)