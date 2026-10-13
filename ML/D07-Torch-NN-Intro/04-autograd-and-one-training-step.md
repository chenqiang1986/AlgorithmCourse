# Lesson 4: Perform One Training Step
*ML / D07-Torch-NN-Intro*

Training repeats a short feedback cycle: make predictions, measure error,
compute how every parameter affected that error, and update the parameters.
PyTorch's autograd engine and optimizers implement the last two parts.

## 1. The Five Operations

One training step contains five essential operations:

```python
optimizer.zero_grad()       # 1. clear gradients from the previous step
output = model(X_batch)     # 2. forward pass
loss = loss_fn(output, y_batch)  # 3. measure error
loss.backward()             # 4. compute parameter gradients
optimizer.step()            # 5. update parameters
```

Their order is part of the algorithm. Calling `step()` before `backward()`
would update from missing or stale gradients.

## 2. What Autograd Records

Registered model parameters normally have `requires_grad=True`. When those
parameters participate in tensor operations, PyTorch records a computation
graph connecting the final loss to the parameters.

```python
import torch
from torch import nn

torch.manual_seed(7)

model = nn.Linear(2, 1)
X = torch.tensor([[1.0, 2.0], [2.0, -1.0]])
y = torch.tensor([[4.0], [1.0]])

predictions = model(X)
loss = nn.MSELoss()(predictions, y)

print(loss)          # a scalar tensor
print(loss.grad_fn)  # records how the loss was produced
```

Calling `loss.backward()` applies the chain rule backward through this graph.
The resulting gradient for each parameter is stored in its `.grad` attribute.

```python
loss.backward()

print(model.weight.grad.shape)  # same shape as model.weight
print(model.bias.grad.shape)    # same shape as model.bias
```

This connects to the scalar-loss gradients from
[Tensor Gradients](../M01-Tensor/02-tensor-gradient.md): if $L$ is scalar, then
$\nabla_WL$ has the same shape as $W$.

## 3. The Optimizer Owns the Update Rule

An optimizer receives the parameters it may update and its hyperparameters.

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.05)
```

For plain stochastic gradient descent, the conceptual update is

$$
\theta\leftarrow\theta-\eta\nabla_\theta L,
$$

where $\eta$ is the learning rate. `optimizer.step()` performs the update
without becoming part of the autograd graph.

## 4. Inspect One Complete Step

```python
torch.manual_seed(7)

model = nn.Linear(2, 1)
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.05)

X = torch.tensor([[1.0, 2.0], [2.0, -1.0]])
y = torch.tensor([[4.0], [1.0]])

weight_before = model.weight.detach().clone()

optimizer.zero_grad()
predictions = model(X)
loss = loss_fn(predictions, y)
loss.backward()

print("loss:", loss.item())
print("weight gradient:", model.weight.grad)

optimizer.step()

weight_after = model.weight.detach().clone()
print("weight changed:", not torch.equal(weight_before, weight_after))
```

`detach()` returns a tensor disconnected from the graph. `clone()` takes a
snapshot of the values. Without `clone()`, the saved tensor could still share
storage with a parameter that changes in place.

## 5. Why Gradients Must Be Cleared

PyTorch adds new gradients to existing `.grad` values. This accumulation is
useful for advanced workflows, but an ordinary mini-batch step should begin by
clearing old gradients.

```python
optimizer.zero_grad()
loss = loss_fn(model(X), y)
loss.backward()
first_gradient = model.weight.grad.detach().clone()

# No zero_grad here: a second backward adds to the first gradient.
loss = loss_fn(model(X), y)
loss.backward()
accumulated_gradient = model.weight.grad.detach().clone()

print(torch.allclose(accumulated_gradient, 2 * first_gradient))  # True
```

Use `optimizer.zero_grad()` once per ordinary batch. Gradient accumulation
should be an explicit choice, not an accident.

## 6. Repeat Steps to Learn

One update rarely solves a problem. Training repeats the step over many
iterations.

```python
torch.manual_seed(7)

X = torch.linspace(-2.0, 2.0, 100).reshape(-1, 1)
y = 3.0 * X - 0.5

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.05)

for step in range(201):
    optimizer.zero_grad()
    predictions = model(X)
    loss = loss_fn(predictions, y)
    loss.backward()
    optimizer.step()

    if step % 50 == 0:
        print(step, loss.item())

print(model.weight.item(), model.bias.item())
```

The learned weight should approach $3$ and the learned bias should approach
$-0.5$.

`loss.item()` converts a one-element tensor to a Python number for logging. Do
not call `.item()` before `backward()`; a Python number has no computation graph.

## 7. Learning Rate Behavior

The learning rate controls update size:

- too small: loss may decrease extremely slowly;
- reasonable: loss decreases steadily;
- too large: loss may oscillate, explode, or become non-finite.

If a loss becomes `nan` or `inf`, first inspect input values and shapes, then
try a smaller learning rate. Do not assume every training failure is caused by
the model architecture.

## 8. Class Practice 1: Put the Step in Order

Put these operations in a valid order: `optimizer.step()`, `loss.backward()`,
`model(X)`, `optimizer.zero_grad()`, and `loss_fn(output, y)`.

<details>
<summary>Solution</summary>

```python
optimizer.zero_grad()
output = model(X)
loss = loss_fn(output, y)
loss.backward()
optimizer.step()
```

$\square$

</details>

## 9. Class Practice 2: Explain a Frozen Model

The loss prints the same value at every step. What essential operation is
missing?

```python
for step in range(100):
    optimizer.zero_grad()
    loss = loss_fn(model(X), y)
    loss.backward()
    print(loss.item())
```

<details>
<summary>Solution</summary>

`optimizer.step()` is missing, so gradients are computed but never used to
change the parameters.

$\square$

</details>

## 10. Key Takeaways

- Autograd records how a scalar loss depends on parameters.
- `loss.backward()` fills each parameter's `.grad` tensor.
- `optimizer.step()` updates parameters using those gradients.
- Gradients accumulate unless they are cleared.
- Use `.item()` for logging only after preserving the tensor needed by
  `backward()`.
- Learning rate is a major cause of training that is too slow or unstable.

Next, we will apply this step to mini-batches and separate training from
evaluation.

