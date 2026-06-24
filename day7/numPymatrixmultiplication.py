import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Matrix multiplication
C = np.matmul(A, B)

# Alternative:
# C = A @ B

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nA × B:")
print(C)
