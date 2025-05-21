import numpy as np

# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Creating a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)

# Matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
print("\nMatrix Multiplication:\n", np.dot(matrix1, matrix2))

# Statistical functions
print("\nMean of arr1:", np.mean(arr1))
print("\nStandard deviation of arr1:", np.std(arr1))
print("\nMaximum value in arr1:", np.max(arr1))
print("\nMinimum value in arr1:", np.min(arr1))