import numpy as np

# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Array with a range of elements
range_arr = np.arange(0, 10, 2) # Start, stop, step
print("\nRange Array:", range_arr)

# Reshaping an array
reshape_arr = arr1.reshape((5, 1))
print("\nReshaped Array:", reshape_arr)