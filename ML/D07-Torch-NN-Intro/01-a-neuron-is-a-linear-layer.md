# Lesson 1: A Neuron Is a Linear Layer
*ML / D07-Torch-NN-Intro*

A neural network begins with a familiar operation: multiply inputs by weights,
add a bias, and produce an output. PyTorch packages those trainable numbers and
the computation that uses them inside `torch.nn` modules.

## 1. From One Neuron to a Batch

One neuron with $d$ input features computes

$$
z=w_1x_1+cdots+w_dx_d+b=w^Tx+b.
$$

For a batch of $n$ examples and $m$ output neurons, PyTorch computes

$$
Z=XW^T+b,
$$

where

$$
X\in\mathbb{R}^{n\times d},\qquad
W\in\mathbb{R}^{m\times d},\qquad
b\in\mathbb{R}^{m},\qquad
Z\in\mathbb{R}^{n\times m}.
$$

The same $W$ and $b$ are applied to every row. The model does not get a new set
of weights for each observation.

## 2. `nn.Linear` Stores the Parameters

```python
import torch
from torch import nn

layer = nn.Linear(in_features=3, out_features=2)

X = torch.tensor([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0],
    [0.0, 1.0, 0.0],
])

Z = layer(X)

print(X.shape)             # torch.Size([4, 3])
print(layer.weight.shape)  # torch.Size([2, 3])
print(layer.bias.shape)    # torch.Size([2])
print(Z.shape)             # torch.Size([4, 2])
```

`in_features=3` must match the final dimension of `X`. `out_features=2`
chooses the final dimension of the output.

PyTorch initializes the weights and biases automatically. Their values are
random starting points, not learned answers.

## 3. Call the Module, Not `forward` Directly

Use

```python
Z = layer(X)
```

rather than

```python
Z = layer.forward(X)  # avoid this
```

Calling the module runs `forward` while preserving PyTorch's surrounding module
behavior, including hooks. The public interface is `layer(X)`.

## 4. Verify the Formula by Hand

For inspection, we can replace the initial parameters with chosen values.

```python
layer = nn.Linear(3, 2)

with torch.no_grad():
    layer.weight.copy_(torch.tensor([
        [1.0, 0.0, -1.0],
        [0.5, 0.5, 0.5],
    ]))
    layer.bias.copy_(torch.tensor([2.0, -1.0]))

X = torch.tensor([
    [3.0, 4.0, 5.0],
    [1.0, 0.0, -1.0],
])

Z_module = layer(X)
Z_manual = X @ layer.weight.T + layer.bias

print(Z_module)
print(torch.allclose(Z_module, Z_manual))  # True
```

`torch.no_grad()` is used because this block deliberately changes parameter
values; the copies should not become part of a gradient computation.

## 5. Parameters Are Registered Tensors

`nn.Linear` registers its `weight` and `bias` as `nn.Parameter` objects. A
parameter is a tensor that PyTorch knows should usually be trained.

```python
for name, parameter in layer.named_parameters():
    print(name, parameter.shape, parameter.requires_grad)
```

Expected structure:

```text
weight torch.Size([2, 3]) True
bias   torch.Size([2])    True
```

An optimizer will later receive `model.parameters()` and update all registered
parameters. A plain tensor stored in an unrelated Python list is not
automatically registered.

## 6. Count the Parameters

A layer with $d$ input features and $m$ output features contains

$$
md+m=m(d+1)
$$

trainable scalar values: $md$ weights and $m$ biases.

**Example (Parameter count).** How many parameters does `nn.Linear(5, 8)` have?

**Solution:**

The weight has shape `(8, 5)`, so it contains $8\cdot5=40$ values. The bias
has shape `(8,)`, so it contains $8$ values. The total is

$$
40+8=48.
$$

$\square$

## 7. A Reliable Shape Rule

`nn.Linear(d, m)` preserves every leading dimension and transforms only the
last one:

```python
layer = nn.Linear(3, 2)

print(layer(torch.randn(3)).shape)        # torch.Size([2])
print(layer(torch.randn(5, 3)).shape)     # torch.Size([5, 2])
print(layer(torch.randn(4, 5, 3)).shape)  # torch.Size([4, 5, 2])
```

For this module, we will normally use two-dimensional feature batches with
shape `(batch_size, n_features)`.

## 8. Class Practice 1: Read a Layer

Suppose `X.shape == (32, 6)` and the model begins with `nn.Linear(6, 10)`.

1. What is the output shape?
2. What are the weight and bias shapes?
3. How many trainable scalar parameters are in the layer?

<details>
<summary>Solution</summary>

1. The output shape is `(32, 10)`.
2. The weight shape is `(10, 6)` and the bias shape is `(10,)`.
3. There are $10\cdot6+10=70$ trainable scalar parameters.

$\square$

</details>

## 9. Class Practice 2: Diagnose a Shape Error

Why does this fail, and what are two valid ways to fix it?

```python
layer = nn.Linear(4, 2)
X = torch.randn(20, 3)
output = layer(X)
```

<details>
<summary>Solution</summary>

The layer expects the final input dimension to equal `4`, but `X` has only
three features. Either create data with shape `(20, 4)` or change the layer to
`nn.Linear(3, 2)`, depending on which feature count the problem actually uses.

$\square$

</details>

## 10. Key Takeaways

- `nn.Linear(d, m)` computes $XW^T+b$.
- The final input dimension must equal `in_features`.
- The output's final dimension equals `out_features`.
- A layer owns registered trainable parameters; its input data is not a
  parameter.
- Call a module with `module(X)`.

Next, we will connect multiple layers and add nonlinear activation functions.

