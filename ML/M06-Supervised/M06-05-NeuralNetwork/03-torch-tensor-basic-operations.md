# Lesson 3: PyTorch Tensor Basics and Broadcasting
*ML / M06 — Supervised Learning*

## The question

Neural-network equations use vectors, matrices, and batches of examples. How
do we express those calculations efficiently in PyTorch?

A PyTorch `torch.Tensor` is very similar to a NumPy `ndarray`: both store a
rectangular, multidimensional collection of values; both have shapes, dtypes,
slicing, and vectorized arithmetic. PyTorch tensors additionally run on GPUs
and can record operations for automatic differentiation. This lesson introduces
the tensor operations used to write a neural-network forward pass.

```python
import torch
```

## 1. Tensors are like NumPy arrays

| Idea | NumPy | PyTorch |
| --- | --- | --- |
| Array object | `np.ndarray` | `torch.Tensor` |
| Shape | `x.shape` | `x.shape` |
| Create zeros | `np.zeros((2, 3))` | `torch.zeros(2, 3)` |
| Elementwise addition | `x + y` | `x + y` |
| Matrix multiplication | `x @ y` | `x @ y` |
| Sum along an axis | `x.sum(axis=0)` | `x.sum(dim=0)` |

PyTorch normally calls an axis a **dimension** and names it `dim`. Shapes and
indexing use the same conventions as NumPy: dimension `0` is first, `-1` is
last, and `:` selects a whole dimension.

```python
x = torch.tensor([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0]])

print(x.shape)    # torch.Size([2, 3])
print(x.ndim)     # 2
print(x.dtype)    # torch.float32
print(x[0, 1])    # tensor(2.)
print(x[:, 1])    # tensor([2., 5.])
```

Use floating-point tensors for features, parameters, and most neural-network
calculations. Integer tensors are appropriate for indices and class labels, but
they cannot require gradients.

## 2. Create, reshape, and index tensors

```python
scalar = torch.tensor(3.0)                  # shape: ()
vector = torch.tensor([1.0, 2.0, 3.0])      # shape: (3,)
matrix = torch.tensor([[1.0, 2.0],
                       [3.0, 4.0]])         # shape: (2, 2)

zeros = torch.zeros(2, 3)
ones = torch.ones(2, 3)
random = torch.randn(2, 3)                  # independent N(0, 1) values
sequence = torch.arange(12).reshape(3, 4)   # shape: (3, 4)
```

`reshape` changes how values are grouped into dimensions without changing
their order. Use `-1` for one inferred dimension:

```python
x = torch.arange(24)
print(x.reshape(2, 3, 4).shape)  # torch.Size([2, 3, 4])
print(x.reshape(2, -1).shape)    # torch.Size([2, 12])
```

`unsqueeze` inserts a length-one dimension and `squeeze` removes one:

```python
v = torch.tensor([10.0, 20.0, 30.0])
row = v.unsqueeze(0)       # (1, 3)
column = v.unsqueeze(1)    # (3, 1)
back_to_vector = column.squeeze(1)  # (3,)
```

These length-one dimensions are central to broadcasting.

## 3. Elementwise arithmetic

For matching shapes, arithmetic works independently at every position:

```python
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([[10.0, 20.0], [30.0, 40.0]])

print(a + b)     # [[11., 22.], [33., 44.]]
print(a * b)     # [[10., 40.], [90., 160.]]
print(a ** 2)    # [[1., 4.], [9., 16.]]
```

Here `*` means **elementwise multiplication**, not matrix multiplication. As
in NumPy, `**` means exponentiation; `^` is bitwise XOR, not power. Common
elementwise functions include `torch.exp`, `torch.log`, `torch.sqrt`,
`torch.relu`, and `torch.sigmoid`.

## 4. Matrix multiplication and reductions

For a batch of `B` examples with `D` features and a layer with `H` hidden
units,

$$
X\in\mathbb R^{B\times D},\qquad W\in\mathbb R^{D\times H},\qquad
Z=XW\in\mathbb R^{B\times H}.
$$

Use `@` (or `torch.matmul`) for the matrix product:

```python
B, D, H = 4, 3, 2
X = torch.randn(B, D)
W = torch.randn(D, H)
Z = X @ W
assert Z.shape == (B, H)
```

`sum` and `mean` reduce one or more dimensions. With no `dim`, they produce a
scalar. `keepdim=True` retains a length-one dimension for later broadcasting.

```python
x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print(x.sum())                         # tensor(21.)
print(x.sum(dim=0))                    # tensor([5., 7., 9.])
print(x.mean(dim=1))                   # tensor([2., 5.])
print(x.sum(dim=1, keepdim=True).shape)  # torch.Size([2, 1])
```

## 5. Broadcasting: align dimensions from the right

Broadcasting lets PyTorch apply an elementwise operation to tensors with
different shapes. Compare dimensions from the right. Aligned dimensions are
compatible when they are equal or when one is `1`. PyTorch behaves as if it
repeats values across a length-one dimension, without normally allocating
repeated input data.

For example, add one bias value per feature to every batch item:

```python
X = torch.randn(32, 10)  # (batch, features)
bias = torch.randn(10)   # (features,)
Y = X + bias             # (32, 10)
```

```text
X:       (32, 10)
bias:    ( 1, 10)  # conceptual leading dimension
result:  (32, 10)
```

Thus $Y_{bf}=X_{bf}+\text{bias}_f$. No `unsqueeze` is needed because
the final dimensions already align. A neural-network layer uses this directly:

```python
B, D, H = 32, 10, 5
X = torch.randn(B, D)
W = torch.randn(D, H)
b = torch.randn(H)       # one bias per hidden unit
Z = X @ W + b            # (B, H) + (H,) -> (B, H)
A = torch.relu(Z)
```

## 6. Insert dimensions deliberately

Sometimes a needed broadcast dimension is not already in the right position.
Insert a singleton dimension with `None` (also called `newaxis`) or
`unsqueeze`.

Suppose:

```text
B[i, j, l] has shape (I, J, L)
C[i, k, l] has shape (I, K, L)
```

To form every pair of `j` and `k` values for matching `i` and `l`, we want

$$
A_{ijkl}=B_{ijl}C_{ikl}.
$$

```python
B_aligned = B[:, :, None, :]  # (I, J, 1, L): insert k axis
C_aligned = C[:, None, :, :]  # (I, 1, K, L): insert j axis

A_product = B_aligned * C_aligned  # (I, J, K, L)
A_sum = B_aligned + C_aligned
A_power = B_aligned ** C_aligned
```

The same alignment using `unsqueeze` is:

```python
B_aligned = B.unsqueeze(2)  # (I, J, 1, L)
C_aligned = C.unsqueeze(1)  # (I, 1, K, L)
```

The inserted dimensions make this work for all elementwise operators: `+`,
`-`, `*`, `/`, and `**`.

`reshape` can create the same alignment when the dimensions are known:

```python
I, J, L = B.shape
_, K, _ = C.shape
B_aligned = B.reshape(I, J, 1, L)
C_aligned = C.reshape(I, 1, K, L)
```

For an unknown number of leading dimensions, build the shapes from the input
shapes rather than hard-coding them:

```python
# B: (*leading, J, L), C: (*leading, K, L)
B_aligned = B.reshape(B.shape[:-1] + (1,) + B.shape[-1:])
C_aligned = C.reshape(C.shape[:-2] + (1,) + C.shape[-2:])
```

These are respectively `(*leading, J, 1, L)` and
`(*leading, 1, K, L)`, the same shapes produced by the ellipsis form below.

### A concrete check

```python
B = torch.arange(2 * 3 * 5, dtype=torch.float32).reshape(2, 3, 5)
C = torch.arange(2 * 4 * 5, dtype=torch.float32).reshape(2, 4, 5) + 1

A = B[:, :, None, :] * C[:, None, :, :]
assert A.shape == (2, 3, 4, 5)
assert A[1, 2, 3, 4] == B[1, 2, 4] * C[1, 3, 4]
```

## 7. Leading dimensions and ellipsis

Machine-learning tensors often have several leading dimensions, such as batch
and attention-head dimensions. `...` preserves all leading dimensions, even
when their count is not known in advance.

```text
B[..., j, l] has shape (*leading, J, L)
C[..., k, l] has shape (*leading, K, L)
```

```python
A = B[..., :, None, :] + C[..., None, :, :]
# shape: (*leading, J, K, L)
```

The ellipsis keeps `leading`; the singleton dimensions broadcast over `k` and
`j`, respectively. This pattern compares every query position with every key
position in an attention model.

Be alert to right alignment. If `X.shape == (batch, tokens, features, 1)` and
`bias.shape == (features,)`, `X + bias` runs but has the wrong shape:
`(batch, tokens, features, features)`. The bias aligns with the final
length-one dimension. State the intended alignment instead:

```python
Y = X + bias[None, None, :, None]
```

Now `Y.shape == X.shape`.

## 8. `einsum`: write index equations directly

`torch.einsum` is readable for tensor products and contractions. The product
from Section 6 can be written directly from its index equation:

```python
A = torch.einsum("ijl,ikl->ijkl", B, C)
```

Every index is in the output, so no dimension is summed. It matches the
broadcasting multiplication. For a matrix product,

$$
Z_{bh}=\sum_d X_{bd}W_{dh},
$$

write:

```python
Z = torch.einsum("bd,dh->bh", X, W)
```

An index absent after `->` is summed. Use `einsum` when an index equation
makes multiplication and summation clear; use broadcasting for general
elementwise addition, subtraction, division, or powers.

## 9. Devices, dtypes, and NumPy conversion

Operands normally need compatible dtypes and must be on the same device:

```python
x = torch.randn(2, 3, dtype=torch.float32)
print(x.dtype)
print(x.device)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = x.to(device)
```

To move data between NumPy and PyTorch on the CPU:

```python
import numpy as np

array = np.array([1.0, 2.0, 3.0], dtype=np.float32)
x = torch.from_numpy(array)  # shares CPU memory when possible
array_copy = x.numpy()       # use x.detach().cpu().numpy() for gradient/GPU tensors
```

## Practice

1. Let `X.shape == (B, T, D)` and `bias.shape == (D,)`. Write the expression
   for $Y_{btd}=X_{btd}+\text{bias}_d$ and state its shape.
2. Let `B.shape == (I, J, L)` and `C.shape == (I, K, L)`. Write PyTorch code
   for $A_{ijkl}=B_{ijl}+C_{ikl}$ using `None` indexing. State the shape.
3. Rewrite problem 2 using `unsqueeze`.
4. Given `X.shape == (batch, features)` and `W.shape == (features, hidden)`,
   write a layer pre-activation with `bias.shape == (hidden,)`. State its shape.
5. Let `scores.shape == (batch, heads, queries, keys)`. Compute the mean over
   `keys` while retaining that dimension.
6. Why is `X * W` not appropriate for problem 4? Which operator is needed?

<details>
<summary>Suggested answers</summary>

1. `Y = X + bias`; shape `(B, T, D)`.
2. `A = B[:, :, None, :] + C[:, None, :, :]`; shape `(I, J, K, L)`.
3. `A = B.unsqueeze(2) + C.unsqueeze(1)`; shape `(I, J, K, L)`.
4. `Z = X @ W + bias`; shape `(batch, hidden)`.
5. `mean_scores = scores.mean(dim=-1, keepdim=True)`; shape
   `(batch, heads, queries, 1)`.
6. `*` multiplies matching positions elementwise and does not contract the
   features dimension. Use `X @ W` or `torch.matmul(X, W)`.

</details>

## Key takeaways

- A PyTorch tensor shares NumPy arrays' core shape, indexing, and arithmetic
  ideas, while adding GPU support and automatic differentiation.
- `*` is elementwise multiplication; `@` is matrix multiplication; reductions
  use `dim`.
- Broadcasting compares dimensions from the right; equal sizes and size `1`
  are compatible.
- Use `None` or `unsqueeze` to make an intended broadcast explicit.
- `torch.einsum` directly expresses tensor multiplication and contraction.

Next, PyTorch can record these tensor operations and automatically compute
their gradients with `autograd`.
