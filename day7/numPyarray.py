import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:")
print(arr)

# Slicing
print("\nSliced Array:")
print(arr[1:5])

# Reshaping
reshaped = arr.reshape(2, 3)
print("\nReshaped Array:")
print(reshaped)

# Statistics
print("\nMean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Maximum:", np.max(arr))
