# Lesson 4: Custom Modules and Autograd Lab
*ML / M06 — Supervised Learning*

## The question

How little PyTorch code is needed to define a new mathematical rule and have
PyTorch differentiate it? In this lab we build small modules, inspect their
outputs, and compare derivatives from `backward()` with derivatives found by
hand.

For all examples:

```python
import torch
from torch import nn

torch.set_printoptions(precision=4, sci_mode=False)
```

## 1. A parameter-free module with a scalar output

A module's constructor, `__init__`, is where persistent state normally goes.
This first rule has no state, so its constructor is deliberately empty except
for `super().__init__()`. Its `forward` method defines

$$
f(\mathbf{x})=\sum_i(x_i^3+2x_i).
$$

The output is a scalar, so `backward()` knows that its upstream derivative is
one and can be called directly. We set `requires_grad=True` on `X` because we
want the derivative with respect to the input.

```python
class CubicSum(nn.Module):
    def __init__(self):
        super().__init__()  # no parameters to create

    def forward(self, X):
        return (X ** 3 + 2 * X).sum()  # a scalar tensor


model = CubicSum()
X = torch.tensor([1.0, 2.0], requires_grad=True)
output = model(X)

print(output)  # tensor(15., grad_fn=<SumBackward0>)
output.backward()
print(X.grad)  # tensor([ 5., 14.])
```

By hand,

$$
\frac{\partial f}{\partial x_i}=3x_i^2+2.
$$

At `X = [1, 2]`, this gives `[5, 14]`, matching `X.grad`.

`X.grad` is filled only for a **leaf tensor** that requires gradients.
`X` above is a leaf because we created it directly. The scalar `output` is not
a leaf: PyTorch keeps the operations that produced it and uses them during the
backward pass.

## 2. Chain vector-output modules with `nn.Sequential`

`forward` may return a vector or a matrix just as easily. Here each module has
no parameter; it simply defines one vectorized mathematical operation:

$$
\mathbf{u}=2\mathbf{x},\qquad
\mathbf{v}=\mathbf{u}+\mathbf{1},\qquad
\mathbf{y}=\mathbf{v}^2.
$$

`nn.Sequential` feeds the output of one module into the next.

```python
class Double(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, X):
        return 2 * X


class AddOne(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, X):
        return X + 1


class Square(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, X):
        return X ** 2


model = nn.Sequential(Double(), AddOne(), Square())
X = torch.tensor([1.0, 2.0], requires_grad=True)
Y = model(X)

print(Y)  # tensor([ 9., 25.], grad_fn=<PowBackward0>)
Y.sum().backward()
print(X.grad)  # tensor([12., 20.])
```

`Y` has two entries, so calling `Y.backward()` without an argument is
ambiguous: derivative of which scalar combination of its entries? We choose
the scalar $\sum_i y_i$ with `Y.sum()`. Equivalently, we could write
`Y.backward(torch.ones_like(Y))`.

For this chain, $y_i=(2x_i+1)^2$, so

$$
\frac{\partial}{\partial x_i}\sum_j y_j=4(2x_i+1).
$$

At `[1, 2]`, the derivative is `[12, 20]`.

## 3. Put a trainable parameter inside a module

Use `nn.Parameter` for a tensor that is persistent and whose derivative we
want PyTorch to calculate. This module implements

$$
y_i=ax_i^2,
$$

where $a$ is a learned scalar parameter.

```python
class ScaledSquare(nn.Module):
    def __init__(self, initial_scale):
        super().__init__()
        self.scale = nn.Parameter(torch.tensor(initial_scale))

    def forward(self, X):
        return self.scale * X ** 2


model = ScaledSquare(initial_scale=3.0)
X = torch.tensor([1.0, 2.0], requires_grad=True)
Y = model(X)

print(Y)  # tensor([ 3., 12.], grad_fn=<MulBackward0>)
Y.sum().backward()

print("d(sum Y)/dX =", X.grad)       # tensor([ 6., 12.])
print("d(sum Y)/dscale =", model.scale.grad)  # tensor(5.)
```

For $\mathcal L=\sum_i ax_i^2$, hand calculation gives

$$
\frac{\partial\mathcal L}{\partial x_i}=2ax_i,
\qquad
\frac{\partial\mathcal L}{\partial a}=\sum_i x_i^2.
$$

Thus the printed gradients are `[6, 12]` and `5`. `nn.Parameter` defaults to
`requires_grad=True` and is automatically returned by `model.parameters()`.

## 4. Leave gradients off for the input

Inputs do not need gradients during ordinary model use. If `X` does not have
`requires_grad=True`, autograd can still differentiate the result with respect
to trainable parameters, but it does not retain an input gradient.

```python
model = ScaledSquare(initial_scale=3.0)
X = torch.tensor([1.0, 2.0])  # requires_grad=False by default
Y = model(X)
Y.sum().backward()

print(X.grad)            # None
print(model.scale.grad)  # tensor(5.)
```

This is usually what we want while fitting a model: update its parameters, not
the data. Set `X.requires_grad=True` only when an experiment needs an input
derivative, such as this lab, sensitivity analysis, or an adversarial-example
calculation.

## 5. A bad parameter: PyTorch cannot differentiate it

An ordinary tensor attribute is not a registered trainable parameter. In this
bad example, neither the input nor `scale` requires gradients. Therefore the
output does not require gradients either, and backward propagation cannot
begin.

```python
class BadScaledSquare(nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.tensor(3.0)  # wrong: not nn.Parameter

    def forward(self, X):
        return self.scale * X ** 2


model = BadScaledSquare()
X = torch.tensor([1.0, 2.0])
Y = model(X)

print(Y.requires_grad)  # False
Y.sum().backward()
# RuntimeError: element 0 of tensors does not require grad and does not have a grad_fn
```

The fix is not merely to make `scale` require gradients. A tensor used for a
learned module value should be an `nn.Parameter` so it is both differentiable
and registered: it appears in `model.parameters()`, moves with the module to a
device, and is included in the module state.

If `X.requires_grad=True` in this bad example, PyTorch can calculate `X.grad`
because the output depends on `X`; however, `model.scale.grad` remains `None`.
That still makes the module unsuitable for a trainable scale.

## 6. Implement a bias-free linear layer by hand

`nn.Linear` normally stores a weight matrix and a bias. To see what a layer
owns, implement the simpler bias-free rule yourself:

$$
Y=XW.
$$

The matrix `weight` is the parameter. For a batch `X` of shape
`(batch, in_features)`, choose `weight` with shape
`(in_features, out_features)`.

```python
class ManualLinear(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.weight = nn.Parameter(
            torch.tensor([[1.0], [2.0]])  # shape (2, 1)
        )

    def forward(self, X):
        return X @ self.weight  # no bias


model = ManualLinear(in_features=2, out_features=1)
X = torch.tensor([[1.0, 3.0],
                  [2.0, 4.0]], requires_grad=True)
Y = model(X)

print(Y)
# tensor([[ 7.],
#         [10.]], grad_fn=<MmBackward0>)

Y.sum().backward()
print("d(sum Y)/dX =\n", X.grad)
# tensor([[1., 2.],
#         [1., 2.]])
print("d(sum Y)/dweight =\n", model.weight.grad)
# tensor([[3.],
#         [7.]])
```

For $\mathcal L=\sum_{bi}Y_{bi}$ when there is one output feature,
$\mathcal L=\sum_b\sum_dX_{bd}W_{d0}$. Therefore

$$
\frac{\partial\mathcal L}{\partial X_{bd}}=W_{d0},
\qquad
\frac{\partial\mathcal L}{\partial W_{d0}}=\sum_bX_{bd}.
$$

The derivatives printed above follow directly: each row of `X.grad` is
`[1, 2]`, while the two entries of `weight.grad` are the column sums `3` and
`7`.

## Class practice

### 1. Hand derivative and `backward()`

Create a parameter-free module whose forward rule is

$$
f(\mathbf{x})=\sum_i(3x_i-1)^2.
$$

Use `X = torch.tensor([1.0, 2.0], requires_grad=True)`.

1. Calculate $f(\mathbf{x})$ by hand.
2. Calculate $\partial f/\partial x_i$ by hand.
3. Implement the module and call `output.backward()`.
4. Compare your hand result with `X.grad`.

<details>
<summary>Suggested answer</summary>

$f([1,2])=2^2+5^2=29$. Since

$$
\frac{\partial f}{\partial x_i}=6(3x_i-1),
$$

the derivative is `[12, 30]`.

```python
class TripleMinusOneSquaredSum(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, X):
        return ((3 * X - 1) ** 2).sum()


X = torch.tensor([1.0, 2.0], requires_grad=True)
TripleMinusOneSquaredSum()(X).backward()
print(X.grad)  # tensor([12., 30.])
```

</details>

### 2. Write a module for a matrix parameter and matrix input

Write an `nn.Module` class named `QuadraticForm`. Its constructor must store
the matrix $A$ as an `nn.Parameter`, and its `forward(X)` method must compute

$$
O=A^T X A,
$$

Let the parameter and input both be $2\times2$ matrices, and use

$$
\mathcal L=\text{MSE}(O,Y),
$$

where `nn.MSELoss()` uses the mean of all four squared entries.

```python
X = torch.tensor([[2.0, 1.0],
                  [1.0, 3.0]])
Y = torch.tensor([[1.0, 0.0],
                  [0.0, 1.0]])
```

1. Implement `QuadraticForm` with initial value `[[1.0, 2.0], [0.0, 1.0]]`
   for $A$.
2. Create the model, compute `O = model(X)`, and use `nn.MSELoss()` and
   `loss.backward()` to find `model.A.grad`.
3. Calculate $O$, the loss, and the gradient with respect to $A$ by hand.
   Compare all three with PyTorch.

<details>
<summary>PyTorch check</summary>

```python
class QuadraticForm(nn.Module):
    def __init__(self):
        super().__init__()
        self.A = nn.Parameter(torch.tensor([[1.0, 2.0],
                                            [0.0, 1.0]]))

    def forward(self, X):
        return self.A.T @ X @ self.A


model = QuadraticForm()
loss_fn = nn.MSELoss()
O = model(X)
loss = loss_fn(O, Y)
loss.backward()

print(O)
print(loss)
print(model.A.grad)
# tensor([[ 2.,  5.],
#         [ 5., 15.]], grad_fn=<MmBackward0>)
# tensor(61.7500, grad_fn=<MseLossBackward0>)
# tensor([[27., 80.],
#         [26., 75.]])
```

For a careful hand check, first differentiate the MSE:

$$
\frac{\partial\mathcal L}{\partial O}
=\frac{2}{4}(O-Y).
$$

Then apply the chain rule through both appearances of $A$ in $A^T X A$.
The two paths both contribute to `model.A.grad`.

</details>

## Key takeaways

- A custom `nn.Module` describes its mathematical rule in `forward`; a module
  with no state still needs only the minimal constructor.
- A scalar output can use `.backward()` directly. For a vector output, first
  choose a scalar combination such as `.sum()`, or supply an upstream gradient.
- `requires_grad=True` on a leaf input makes its derivative available in
  `X.grad`; omitting it leaves `X.grad` as `None`.
- Put learned module tensors in `nn.Parameter`, not ordinary tensor
  attributes, so autograd and the module can track them.
- Once `forward` uses differentiable tensor operations, PyTorch applies the
  chain rule to calculate derivatives for every tracked input and parameter.
