# Lesson 1: Tensor Operations
*ML / M01-Tensor*

Machine-learning data and model parameters are usually stored as arrays of numbers. A **tensor** is the mathematical language for such an array, together with rules for how its indices are combined.

In this lesson, tensors are treated as multidimensional numerical arrays. This viewpoint is enough to read most machine-learning derivations and to connect the math directly to NumPy.

## 1. Tensors, dimensions, and indices

A tensor has one or more **axes**. Its **shape** gives the length of every axis.

| Object | Mathematical notation | Shape | NumPy example |
| --- | --- | --- | --- |
| Scalar | $a$ | `()` | `np.array(3.5)` |
| Vector | $x_i$ | `(d,)` | `np.array([2, 5, 7])` |
| Matrix | $A_{ij}$ | `(m, n)` | `np.array([[1, 2], [3, 4]])` |
| Order-3 tensor | $T_{ijk}$ | `(b, h, w)` | a batch of `b` images with height `h` and width `w` |

The number of axes is the **order** (also commonly called rank in machine learning). Thus, a vector has order 1 and a matrix has order 2. Do not confuse tensor order with the rank of a matrix in linear algebra.

For a tensor `T` with shape `(d1, d2, ..., dk)`, an entry is written `T[i1, i2, ..., ik]`, where each index is within the corresponding axis length.

For example, if `images.shape == (32, 28, 28)`, then `images[4, 10, 7]` is the pixel in image 4, row 10, column 7. In index notation, we might call it `I[4, 10, 7]`. Python starts indices at 0; some mathematics texts start them at 1.

```python
import numpy as np

images = np.zeros((32, 28, 28))
pixel = images[4, 10, 7]
first_image = images[0]        # shape: (28, 28)
```

An index says which entry or slice we select. An axis says what position that index occupies in the shape. Keeping axis meaning explicit—batch, feature, output unit, and so on—is essential in ML.

## 2. Elementwise operations

Let `A` and `B` have the same shape. An **elementwise** operation keeps that shape and applies the operation independently at every index:

```text
(A + B)[i1, ..., ik] = A[i1, ..., ik] + B[i1, ..., ik]
(A - B)[i1, ..., ik] = A[i1, ..., ik] - B[i1, ..., ik]
(A * B)[i1, ..., ik] = A[i1, ..., ik] * B[i1, ..., ik]
(A / B)[i1, ..., ik] = A[i1, ..., ik] / B[i1, ..., ik]
```

For example,

```text
[[1, 2],     [[10, 20],     [[10,  40],
 [3, 4]]  *   [30, 40]]  =   [90, 160]]
```

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[10, 20], [30, 40]])

A + B     # [[11, 22], [33, 44]]
A - B
A * B     # elementwise multiplication, not matrix multiplication
A / B
```

NumPy also supports **broadcasting**, which can apply an elementwise operation to compatible but unequal shapes. We will use the same index rules below, but this lesson starts with the simpler same-shape case.

## 3. Tensor product (outer product)

The **tensor product** (also called an outer product) of tensors `A` and `B` pairs every entry of `A` with every entry of `B`:

$$
C = A \otimes B
$$
It means
```text
C[i1, ..., ip, j1, ..., jq] = A[i1, ..., ip] * B[j1, ..., jq]
```

No index is summed away. The result has all axes of `A`, followed by all axes of `B`. If `A.shape == (2, 3)` and `B.shape == (4,)`, then `tensor_product.shape == (2, 3, 4)`.

For two vectors, the tensor product is the familiar outer product:

```text
C[i, j] = x[i] * y[j]
```

```python
x = np.array([1, 2])
y = np.array([10, 20, 30])

# Any of the following
C=np.outer(x, y)                 # shape (2, 3)
C=np.tensordot(x, y, axes=0)     # same result; works for any tensor orders
C=x[:, None] * y[None, :]        # See explanation below
C=np.einsum("i,j->ij", x, y)     # We will explain below, but you can guess

A = np.ones((2, 3))
B = np.ones((4,))
C = np.outer(A, B)
C = np.tensordot(A, B, axes=0)   # shape (2, 3, 4)
C = A[:, :, None] * B[None, None, :]
C = np.einsum("ij,k->ijk", A, B)
```

The expression `x[:, None] * y[None, :]` produces the same outer product using broadcasting. Suppose `x.shape == (m,)` and `y.shape == (n,)`:

```python
x_column = x[:, None]  # shape: (m, 1)
y_row = y[None, :]     # shape: (1, n)
C = x_column * y_row   # shape: (m, n)
```

Using the broadcasting mental model, `x_column` is virtually repeated across columns and `y_row` is virtually repeated across rows:

```text
x_column_broadcast[i, j] = x[i]
y_row_broadcast[i, j] = y[j]
```

The `*` is an **elementwise product** of these two virtual matrices. Therefore, at every matrix index:

```text
C[i, j] = x_column_broadcast[i, j] * y_row_broadcast[i, j]
        = x[i] * y[j]
```

This is exactly the tensor product of the vectors: every entry of `x` is paired and multiplied with every entry of `y`. NumPy does not need to materialize the two repeated matrices; broadcasting supplies the matching values while computing the elementwise product.

### Broadcasting by inserting an axis

In NumPy, `None` (also written `np.newaxis`) inserts an axis of length 1. For example, if `b` has shape `(I, K, L)`, then:

```python
a = b[:, None, :, :]
```

gives `a` shape `(I, 1, K, L)`. This raises the tensor order from 3 to 4 and places a new second axis between the original first and second axes.

Only the index value `0` exists on this new axis, so the stored array satisfies:

```text
a[i, 0, k, l] = b[i, k, l]
```

Suppose we next combine `a` with a tensor whose shape is `(I, J, K, L)`. NumPy broadcasts the length-1 second axis without making a full copy. The useful mental model is the *virtual expanded tensor*:

```text
a_broadcast[i, j, k, l] = b[i, k, l]    for every valid j
```

The physical `a` stores only `a[i, 0, k, l]`; the values for other `j` are supplied conceptually during the operation. The main purpose of inserting `None` is to raise the order and align axes so an elementwise operation can pair the intended indices.


## 4. Reductions and contraction

A **reduction** removes one axis by summing independently over that index. For example, if `T` has shape `(d1, d2, d3)`, summing its second axis gives a tensor with shape `(d1, d3)`:

$R_{ik} = \sum_j T_{ijk}$

This operation uses `np.sum(axis=...)`; its summation index does not need to equal another index.

```python
T = np.ones((2, 3, 4))    # A tensor of shape(2,3,4) with all entries as value 1

T.sum(axis=1).shape       # (2, 4): sum the second axis
T.sum(axis=(0, 2)).shape  # (3,): sum the first and third axes independently
```

A **contraction** sums over two or more indices that are required to take the same value. For a matrix, contracting its row and column indices means keeping only the diagonal entries, then summing:

$$\operatorname{trace}(A) = \sum_i A_{ii}$$

`np.trace(A)` performs this two-axis contraction. For a higher-order tensor, `np.einsum` is usually the clearest way to state which indices must match:

```python
T = np.ones((2, 3, 3))
Q = np.ones((3, 3, 3))

np.einsum('ijj->i', T)  # result[i] = sum_j T[i, j, j]
np.einsum('iii->', Q)   # sum_i Q[i, i, i] for a cubic tensor
```

In tensor algebra, contraction often follows a tensor product. First form a larger tensor by pairing entries; then require one axis from each input to take the same value and sum over that shared index.

### Matrix-vector product

For a matrix `A` with shape `(m, n)` and vector `x` with shape `(n,)`, their tensor product has entries `P[i, j, k] = A[i, j] * x[k]`. Contract the second and third axes by matching `j` and `k` and summing:

$y_i = \sum_j A_{ij} x_j$

The result has shape `(m,)`. It is the core computation in a linear layer before adding bias and applying an activation.

```python
A = np.array([[1, 2, 3], [4, 5, 6]])  # shape (2, 3)
x = np.array([10, 20, 30])            # shape (3,)

y = A @ x                             # shape (2,)
# equivalent:
y = np.matmul(A, x)

# equivalent: the axes=([1], [0]) is saying to contract on A's 2nd axis and x's 1st axis
y = np.tensordot(A, x, axes=([1], [0]))

# equivalent: indicates y[i] = sum_j A[i,j]x[j]
y = np.einsum("ij,j->i" ,A ,x)

```

### Matrix product: tensor product followed by contraction

Let `A` have shape `(m, n)` and `B` have shape `(n, p)`. Their tensor product has four indices:

```text
P[i, j, k, l] = A[i, j] * B[k, l]
```

The second axis of `P` (index `j`) and third axis (index `k`) both have length `n`. Contract those axes by setting `j = k` and summing over that shared index:

$C_{il} =\sum_j P_{ijjl}= \sum_j A_{ij} B_{jl}$

Thus matrix multiplication is a special case of tensor product followed by contraction on the second and third indices. The remaining first and fourth indices become the axes of `C`.

```python
A = np.ones((2, 3))
B = np.ones((3, 4))
C = A @ B                              # shape (2, 4)

# equivalent:
C = np.matmul(A, B)

# equivalent:
C = np.tensordot(A, B, axes=([1], [0]))

# equivalent: C[i,k] = sum_j A[i,j]B[j,k]
C = np.einsum("ij,jk->ik", A, B)
```

The trace is another familiar contraction: identify a matrix's row and column indices, then sum along that diagonal.

$\operatorname{trace}(A) = \sum_i A_{ii}$

```python
A = np.array([[2, 1], [7, 3]])
np.trace(A)                            # 5

# equivalent:
np.einsum("ii->", A)
```

## 5. Einstein summation notation (IMPORTANT!!!!)

**Einstein summation** (or *einsum*) makes tensor operations compact by using index labels:

- An index appearing once on the right is kept in the output.
- An index not appearing on the right is summed over (contracted).
- Indices appearing on the left name the output axes and their order.

Examples:

1. 
`B = np.einsum("ij->", A)`
It means
$$
B =\sum_{i}\sum_{j}A_{ij}
$$

The output index, namely the string to the right of "->" is empty, so the output will be a scalar, and thus it will take sum over both i, and j.

2.
`C = np.einsum("ij,ij->j", A, B)`
It means
$$
C_{j} = \sum_i A_{ij}B_{ij}
$$

The output index is $j$, which means the output will take this index. Index $i$ does not appear in the output, and thus we take sum over it. Note that this one gives us the diagnal elements of matrix $A^TB$ in a form of a vector.

3.
`C = np.einsum("iij,jkk->ik", A, B)`
It means
$$
C_{ik}=\sum_j A_{iij}B_{jkk}
$$

Common Use Cases:

| Index notation | Meaning | NumPy |
| --- | --- | --- |
| $C_{ij} = x_i y_j$ | outer product | `np.einsum('i,j->ij', x, y)` |
| $s = \sum_i x_i y_i$ | dot product | `np.einsum('i,i->', x, y)` |
| $y_i = \sum_j A_{ij} x_j$ | matrix-vector contraction | `np.einsum('ij,j->i', A, x)` |
| $C_{ik} = \sum_j A_{ij} B_{jk}$ | matrix multiplication | `np.einsum('ij,jk->ik', A, B)` |
| $t = \sum_i A_{ii}$ | trace | `np.einsum('ii->', A)` |
| $B = A^T$ | transpose | `B=np.einsum("ij->ji", A)` |

The first row is a useful warning: `einsum` describes multiplication and summation, not arbitrary arithmetic. Do elementwise addition or subtraction with ordinary NumPy operators.

### Reading an einsum expression

```python
scores = np.einsum('bhd,dk->bhk', X, W)
```

If `X.shape == (batch, tokens, features)` and `W.shape == (features, outputs)`, the repeated label `d` is summed over. The labels `b`, `h`, and `k` remain, so the result has shape `(batch, tokens, outputs)`:

$\text{scores}_{bhk} = \sum_d X_{bhd} W_{dk}$

This is a batched linear transformation. The equation shows exactly which axis is consumed and which axes survive—one reason Einstein notation is so useful for ML derivations.

## 6. Summary

- A tensor is a multidimensional array; its shape names the size of each axis.
- Elementwise operations preserve shape and operate index by index.
- A tensor product adds axes by pairing every entry of two tensors.
- A contraction identifies matching axes and sums only entries with equal index values; after a tensor product, matching axes can be contracted together.
- Einstein notation records these operations using index labels; `np.einsum` executes the same pattern.

## 7. Practice: translate between math and NumPy

For every problem, state:

- the order and shape of each input tensor;
- the order and shape of the result tensor; and
- which axes are kept, paired, or summed over.

Use `np.array` values small enough to check your answer by hand when useful.

### A. From index notation to NumPy

1. `A` and `B` both have shape `(2, 3, 4)`. Write NumPy code for each result:

   - $C_{ijk} = A_{ijk} + B_{ijk}$
   - $D_{ijk} = A_{ijk} - B_{ijk}$
   - $E_{ijk} = A_{ijk} B_{ijk}$
   - $F_{ijk} = A_{ijk} / B_{ijk}$

   What is the order and shape of every result?

2. `x.shape == (3,)` and `y.shape == (5,)`. Write NumPy code for the tensor product:

   $$C_{ij} = x_i y_j$$

   What is the order and shape of `C`?

3. `T.shape == (2, 3, 4)`. Write NumPy code for:

   $$R_{ik} = \sum_j T_{ijk}$$

   What are the order and shape of `T` and `R`?

4. `A.shape == (4, 3)` and `B.shape == (3, 5)`. Write NumPy code for:

   $$C_{ik} = \sum_j A_{ij}B_{jk}$$

   State the order and shape of `A`, `B`, and `C`. Which axes were contracted?

5. Let `A.shape == (batch, tokens, outputs)`, `B.shape == (batch, tokens, features)`, and `C.shape == (features, outputs)`. Write ordinary NumPy code, without `einsum`, for:

   $$D_{ijk} = A_{ijk} + \sum_l B_{ijl}C_{lk}$$

   State the order and shape of every input and of `D`. Identify the elementwise step and the contracted axes.

### B. From NumPy to index notation

For each code sample, write an index equation, using a summation sign whenever an axis is contracted. Then identify the order and shape of all inputs and the result.

1. ```python
   result = A * B
   ```

   Assume `A.shape == B.shape == (batch, features)`.

2. ```python
   result = np.tensordot(X, Y, axes=0)
   ```

   Assume `X.shape == (2, 3)` and `Y.shape == (4,)`.

3. ```python
   result = T.sum(axis=(1, 2))
   ```

   Assume `T.shape == (batch, height, width)`.

4. ```python
   result = A @ x
   ```

   Assume `A.shape == (outputs, features)` and `x.shape == (features,)`.

5. ```python
   D = A + np.matmul(B, C)
   ```

   Assume `A.shape == (batch, tokens, outputs)`, `B.shape == (batch, tokens, features)`, and `C.shape == (features, outputs)`. Write the full index equation for `D`. Which part is elementwise and which part is a contraction?

### C. Rewrite NumPy operations with `einsum`

For each sample, write an equivalent `np.einsum(...)` call. Then give the index equation and the order and shape of the result.

1. Tensor product / outer product:

   ```python
   outer = np.tensordot(x, y, axes=0)
   ```

   Assume `x.shape == (m,)` and `y.shape == (n,)`.

2. Matrix trace:

   ```python
   diagonal_sum = np.trace(A)
   ```

   Assume `A.shape == (n, n)`.

3. Matrix multiplication:

   ```python
   C = A @ B
   ```

   Assume `A.shape == (m, n)` and `B.shape == (n, p)`.

4. Batched matrix-vector product:

   ```python
   y = np.matmul(A, x[..., None]).squeeze(-1)
   ```

   Assume `A.shape == (batch, outputs, features)` and `x.shape == (batch, features)`.

5. Composite operation: batched matrix product plus an elementwise residual:

   ```python
   D = A + np.matmul(B, C)
   ```

   Assume `A.shape == (batch, tokens, outputs)`, `B.shape == (batch, tokens, features)`, and `C.shape == (features, outputs)`. Rewrite the contraction with `einsum`, keeping the elementwise addition explicit.

6. Cyclic property of the trace: let `A.shape == (m, n)` and `B.shape == (n, m)`. Prove that

   $$\operatorname{trace}(AB)=\operatorname{trace}(BA).$$

   Expand both traces in index notation. Why are both products defined even when `A` and `B` are not square?

### D. Readability reflection

Compare these equivalent implementations:

```python
D = A + np.matmul(B, C)
```

```python
D = A + np.einsum('ijl,lk->ijk', B, C)
```

1. Which version makes the contracted and remaining axes clearer?
2. Which version would you prefer when reading or checking a tensor derivation, and why?
3. When might the ordinary NumPy version still be a good choice?

### Answer check

Try the exercises before opening this section.

<details>
<summary>Suggested answers</summary>

**A1.** `C = A + B`, `D = A - B`, `E = A * B`, and `F = A / B`. Every input and output has order 3 and shape `(2, 3, 4)`; no axes are added or summed over.

**A2.** `C = np.tensordot(x, y, axes=0)` or `C = np.outer(x, y)`. `x` and `y` have order 1; `C` has order 2 and shape `(3, 5)`.

**A3.** `R = T.sum(axis=1)`. `T` has order 3 and shape `(2, 3, 4)`; `R` has order 2 and shape `(2, 4)`. The second axis is summed over.

**A4.** `C = A @ B` or `C = np.tensordot(A, B, axes=([1], [0]))`. `A`, `B`, and `C` have orders 2, 2, and 2, with shapes `(4, 3)`, `(3, 5)`, and `(4, 5)`. The second axis of `A` and first axis of `B` are contracted.

**A5.** `D = A + np.matmul(B, C)`. `A`, `B`, and `C` have orders 3, 3, and 2; `D` has order 3 and shape `(batch, tokens, outputs)`. `np.matmul(B, C)` contracts the third axis of `B` with the first axis of `C`; adding `A` is elementwise.

**B1.** $\text{result}_{bf} = A_{bf}B_{bf}$. All tensors have order 2 and shape `(batch, features)`.

**B2.** $\text{result}_{ijk} = X_{ij}Y_k$. The inputs have orders 2 and 1; the result has order 3 and shape `(2, 3, 4)`.

**B3.** $\text{result}_b = \sum_h \sum_w T_{bhw}$. `T` has order 3 and shape `(batch, height, width)`; the result has order 1 and shape `(batch,)`.

**B4.** $\text{result}_o = \sum_f A_{of}x_f$. The inputs have orders 2 and 1; the result has order 1 and shape `(outputs,)`.

**B5.** $D_{ijk} = A_{ijk} + \sum_l B_{ijl}C_{lk}$. The multiplication followed by $\sum_l$ is the contraction; adding $A_{ijk}$ is elementwise. The input orders are 3, 3, and 2, and `D` has order 3 and shape `(batch, tokens, outputs)`.

**C1.** `np.einsum('i,j->ij', x, y)`; $\text{outer}_{ij} = x_i y_j$; result order 2, shape `(m, n)`.

**C2.** `np.einsum('ii->', A)`; $\text{diagonal_sum} = \sum_i A_{ii}$; result order 0, shape `()`.

**C3.** `np.einsum('ij,jk->ik', A, B)`; $C_{ik} = \sum_j A_{ij}B_{jk}$; result order 2, shape `(m, p)`.

**C4.** `np.einsum('bof,bf->bo', A, x)`; $y_{bo} = \sum_f A_{bof}x_{bf}$; result order 2, shape `(batch, outputs)`.

**C5.** `D = A + np.einsum('ijl,lk->ijk', B, C)`; $D_{ijk} = A_{ijk} + \sum_l B_{ijl}C_{lk}$; result order 3, shape `(batch, tokens, outputs)`.

**C6.** Since $(AB)_{ii}=\sum_j A_{ij}B_{ji}$ and $(BA)_{jj}=\sum_i B_{ji}A_{ij}$,

$$
\operatorname{trace}(AB)
=\sum_i\sum_j A_{ij}B_{ji}
=\sum_j\sum_i B_{ji}A_{ij}
=\operatorname{trace}(BA).
$$

`AB` has shape `(m, m)` and `BA` has shape `(n, n)`, so each trace is defined. The matrices themselves need not be square; only their inner dimensions must match.

**D.** The `einsum` version makes the contracted axis `l` and retained axes `i`, `j`, and `k` explicit, so it is generally clearer when comparing code with a tensor derivation. `np.matmul` is still a strong choice when the operation is standard matrix multiplication and its axes are already obvious from the surrounding code.

</details>
