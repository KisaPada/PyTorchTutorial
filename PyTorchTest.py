import torch

print(f"{torch.cuda.is_available()=}")
tensor = torch.rand((5, 3))
print(tensor)
print(f"tensor is stored on: {tensor.device}")
