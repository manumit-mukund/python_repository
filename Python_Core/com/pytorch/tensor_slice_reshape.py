import torch

tensor = torch.tensor([[1, 2], [3, 4], [5, 6]])

element = tensor[1, 0]
print(f"Indexed Element (Row 1, Column 0): {element}")

slice_tensor = tensor[:2, :]
print(f"Sliced Tensor (First two rows): \n{slice_tensor}")

reshaped_tensor = tensor.view(2, 3)
print(f"Reshaped Tensor (2x3): \n{reshaped_tensor}")