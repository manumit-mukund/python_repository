import torch

a = torch.tensor([1.0, 2.0])
b = torch.tensor([3.0, 4.0])

# Element-wise addition
print('Element Wise Addition of a & b: \n', a + b)

# Matrix multiplication
print('Matrix Multiplication of a & b: \n',
      torch.matmul(a.view(2, 1), b.view(1, 2)))

tensor_a = torch.tensor([[1, 2, 3], [4, 5, 6]])

tensor_b = torch.tensor([[10, 20, 30]])

broadcasted_result = tensor_a + tensor_b
print(f"Broadcasted Addition Result: \n{broadcasted_result}")

matrix_multiplication_result = torch.matmul(tensor_a, tensor_a.T)
print(f"Matrix Multiplication Result (tensor_a * tensor_a^T): \n{matrix_multiplication_result}")