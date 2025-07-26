import torch

x = torch.tensor(2.0, requires_grad=True)
y = x ** 2
y.backward()
print(x.grad)  #(dy/dx = 2x = 4 when x=2)