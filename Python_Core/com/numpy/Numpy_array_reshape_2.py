import numpy as np

arr = np.arange(12)  # Creates a 1D array from 0 to 11
print(f"Original array: {arr}")
print(f"Original shape: {arr.shape}")

# Let NumPy infer the number of rows
reshaped_inferred_rows = arr.reshape(-1, 4)
print(f"\nReshaped with inferred rows:\n{reshaped_inferred_rows}")
print(f"New shape: {reshaped_inferred_rows.shape}")

# Let NumPy infer the number of columns
reshaped_inferred_cols = arr.reshape(3, -1)
print(f"\nReshaped with inferred columns:\n{reshaped_inferred_cols}")
print(f"New shape: {reshaped_inferred_cols.shape}")