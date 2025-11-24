import numpy as np

A = np.array([[1, 2, 3], 
              [4, 5, 6]])  # Shape (2, 3)

B = np.array([10, 20, 30])  # Shape (3,)

# The 1D array B is broadcast across both rows of A.
result = A + B 

print("Matrix A:\n", A)
print("\nVector B:\n", B)
print("\nBroadcast Result (A + B):\n", result)
# Output:
# [[1+10, 2+20, 3+30],
#  [4+10, 5+20, 6+30]]
# [[11 22 33]
#  [14 25 36]]