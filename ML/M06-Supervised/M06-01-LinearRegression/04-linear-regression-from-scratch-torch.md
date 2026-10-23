# Lesson 4: Linear Regression with PyTorch
*ML / M06 — Supervised Learning*

## The goal

We will implement the same linear-regression model in two styles:

1. **Scratch with tensors and autograd.** We own the parameters, loss, and
   update rule, but make each responsibility an explicit function.
2. **The PyTorch way.** We write a small `nn.Module` and let PyTorch's loss and
   optimizer APIs handle the rest.

In both cases, the model is $\hat y = Xw + b$.

## Version 1: trainable tensors with explicit functions

Setting `requires_grad=True` tells PyTorch to record the operations linking the
loss to `w` and `b`. These two tensors are the whole model—there is no
`nn.Linear` here.

~~~python
import torch

torch.manual_seed(7)
n, d = 200, 3
X = torch.randn(n, d)
true_w = torch.tensor([2.0, -3.0, 0.5])
true_b = 1.25
y = X @ true_w + true_b + 0.25 * torch.randn(n)


def forward(X, w, b):
    """Compute predicted targets: Xw + b."""
    return X @ w + b


def mean_squared_error(prediction, target):
    """Compute the mean squared error loss."""
    return ((prediction - target) ** 2).mean()


def gradient_descent_step(loss, parameters, learning_rate):
    """Use autograd gradients to update a collection of parameters."""
    loss.backward()

    # An update is not part of the forward model or its autograd graph.
    with torch.no_grad():
        for parameter in parameters:
            parameter -= learning_rate * parameter.grad

    # Gradients accumulate by default, so clear them for the next step.
    for parameter in parameters:
        parameter.grad.zero_()


w = torch.zeros(d, requires_grad=True)
b = torch.zeros((), requires_grad=True)  # scalar tensor
learning_rate = 0.05

for step in range(2_000):
    prediction = forward(X, w, b)
    loss = mean_squared_error(prediction, y)
    gradient_descent_step(loss, [w, b], learning_rate)

    if step % 400 == 0:
        print(f"step={step:4d}  mse={loss.item():.6f}")

print("learned w:", w.detach())
print("learned b:", b.detach().item())
~~~

### Why `torch.no_grad()` and clearing gradients matter

The update is an optimizer instruction, not part of the mathematical forward
model. Without `torch.no_grad()`, modifying a leaf tensor that requires
gradients raises an error, or an out-of-place update can create an
ever-growing graph.

After `loss.backward()`, `.grad` holds the computed gradient. PyTorch adds the
next backward result to it rather than replacing it. Therefore,
`gradient_descent_step` clears each gradient after the update. If a function
might receive a parameter that has not yet received a gradient, use the more
defensive form:

~~~python
if parameter.grad is not None:
    parameter.grad.zero_()
~~~

### Compare autograd with the hand derivative

Before calling `gradient_descent_step`, the autograd result should equal the
formula from the NumPy lesson:

~~~python
prediction = forward(X, w, b)
loss = mean_squared_error(prediction, y)
loss.backward()

residual = prediction - y
manual_grad_w = (2 / n) * X.T @ residual
manual_grad_b = 2 * residual.mean()

print(torch.allclose(w.grad, manual_grad_w))  # True
print(torch.allclose(b.grad, manual_grad_b))  # True

w.grad.zero_()
b.grad.zero_()
~~~

This is a strong debugging habit: autograd and a separately derived formula
should agree up to floating-point tolerance.

## Version 2: a module plus PyTorch's training APIs

Most models do not need us to write parameter storage, gradient updates, or
gradient clearing ourselves. A subclass of `nn.Module` defines the model's
parameters and its forward calculation. We can also place the loss calculation
on the model for this lesson. PyTorch supplies `MSELoss`, `SGD`, `Adam`, and
the autograd machinery.

~~~python
import torch
from torch import nn


class LinearRegression(nn.Module):
    def __init__(self, num_features):
        super().__init__()
        self.w = nn.Parameter(torch.zeros(num_features))
        self.b = nn.Parameter(torch.zeros(()))
        self.mse = nn.MSELoss()

    def forward(self, X):
        return X @ self.w + self.b

    def loss(self, X, target):
        prediction = self(X)  # Calls forward(X).
        return self.mse(prediction, target)


model = LinearRegression(d)
optimizer = torch.optim.SGD(model.parameters(), lr=0.05)
# Adam is equally easy to try:
# optimizer = torch.optim.Adam(model.parameters(), lr=0.05)

for step in range(2_000):
    optimizer.zero_grad()
    loss = model.loss(X, y)
    loss.backward()
    optimizer.step()

    if step % 400 == 0:
        print(f"step={step:4d}  mse={loss.item():.6f}")

print("learned w:", model.w.detach())
print("learned b:", model.b.detach().item())
~~~

The important boundary is small: for a new kind of layer, we implement its
parameters and `forward`. Once its operations are PyTorch tensor operations,
autograd can differentiate them. Optimizers can update every parameter exposed
by `model.parameters()`. The same APIs work when this simple layer becomes one
piece of a much larger network.

## Homework: tensor-only linear regression without `.backward()`

Implement linear regression using PyTorch tensors, but **do not call
`.backward()`** (and do not use `torch.autograd.grad`). This is the NumPy
algorithm from the previous lesson expressed with tensor operations.

1. Generate or reuse `X` and `y` above. Initialize `w = torch.zeros(d)` and
   `b = torch.zeros(())`. Do **not** set `requires_grad=True`.
2. Write `forward(X, w, b)` and `mean_squared_error(prediction, target)`.
3. Write `manual_gradient_descent_step(X, y, w, b, learning_rate)` that:
   - computes `prediction`, `residual`, and the MSE loss;
   - computes `grad_w = (2 / n) * X.T @ residual` and
     `grad_b = 2 * residual.mean()`;
   - updates and returns the new `w`, `b`, and loss.
4. Train for 2,000 steps and print the loss every 400 steps. Compare your final
   `w` and `b` with `true_w` and `true_b` using `torch.allclose` (choose a
   reasonable tolerance because the targets contain noise).
5. In a short comment, explain why this version does not need `requires_grad`,
   `torch.no_grad()`, or gradient clearing.

## Key takeaways

- Separating `forward`, loss, and an update step makes each part of a training
  loop testable and easier to reuse.
- Plain tensors plus autograd expose the mechanics behind PyTorch training.
- With `nn.Module`, you primarily define parameters and `forward`; autograd and
  optimizers such as SGD or Adam take care of differentiation and updates.
- Tensor algebra works equally well for hand-derived gradients when autograd is
  intentionally not used.
