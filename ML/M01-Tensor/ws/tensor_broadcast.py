import numpy as np
import torch

X = torch.tensor([[1,2], [4,5], [6,7]])

print(torch.einsum("...j->...", X))