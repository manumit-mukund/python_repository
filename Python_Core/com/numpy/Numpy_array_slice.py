import numpy as np

# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Creating a 2D array
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("\n2D Array:\n", arr2)

# Slicing arrays
print("\nSlice of arr1:", arr1[1:4])
print("\nSlice of arr2:\n", arr2[:, 1:])