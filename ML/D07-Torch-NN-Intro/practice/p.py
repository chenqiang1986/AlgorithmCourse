import torch
from torch import nn

class MyNode(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, X):
        return X[0]*X[0]+X[1]


f = MyNode()

X = torch.tensor([9.0,1.0], requires_grad=True)
Y = f(X)
Y.backward()

print(f)
print(X.grad)