import torch

t = torch.tensor([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])

# Reshaping
print("Reshaping")
print(t.reshape(6, 2))

# Resizing (deprecated, use reshape)
print("\nResizing")
print(t.view(2, 6))

# Transposing
print("\nTransposing")
print(t.transpose(0, 1))