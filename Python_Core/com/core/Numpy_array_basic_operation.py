import numpy as np

# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Creating a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)

# Basic operations
arr3 = np.array([10, 20, 30, 40, 50])
print("\nAddition:", arr1 + arr3)
print("\nSubtraction:", arr3 - arr1)
print("\nMultiplication:", arr1 * arr3)
print("\nDivision:", arr3 / arr1)