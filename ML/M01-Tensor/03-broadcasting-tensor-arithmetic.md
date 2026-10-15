# Lesson 3: Broadcasting for Tensor Arithmetic
*ML / M01-Tensor*

Broadcasting lets an elementwise operation act on tensors whose shapes differ, as long as their axes can be aligned. It is the practical way to translate index equations such as

$$
A_{ijkl}=B_{ijl}C_{ikl}
$$

into NumPy without writing Python loops or physically repeating data.

This lesson compares three useful expressions of the same idea:

1. `einsum`, which makes the index labels explicit for a product;
2. inserting singleton axes with `None` (or `np.newaxis`); and
3. `reshape`, which inserts those same singleton axes explicitly by shape.

## 1. The broadcasting rule

Broadcasting is especially useful when the two tensors have different numbers of axes. Before comparing axes, NumPy **conceptually** gives the lower-order tensor enough leading length-`1` axes to match the higher-order tensor's order. It then compares shapes from the **rightmost** axis moving left.

For example, a tensor `X` with shape `(B, T, D)` and a vector `bias` with shape `(D,)` have orders 3 and 1:

```text
X:       (B, T, D)
bias:    (      D)

# conceptual alignment of the lower-order tensor
X:       (B, T, D)
bias:    (1, 1, D)
```

Therefore `X + bias` has shape `(B, T, D)`, with

$$
(X+\operatorname{bias})_{btd}=X_{btd}+\operatorname{bias}_d.
$$

NumPy does not normally create a new repeated array for those leading `1`s; this is the right mental model for how its shapes align. On each aligned axis, the sizes must either be equal or one size must be `1`. A size-`1` axis is then virtually repeated to match the other size.

For example, shapes `(I, J, 1, L)` and `(I, 1, K, L)` broadcast to `(I, J, K, L)`:

```text
                 I  J  1  L
                 I  1  K  L
result:          I  J  K  L
```

The word *virtual* matters: broadcasting normally does not allocate repeated copies of either input. It determines which input value to use at each output location.

## 2. Running example: pair `j` with `k`

Suppose

```text
B[i, j, l] has shape (I, J, L)
C[i, k, l] has shape (I, K, L)
```

and we want an output with shape `(I, J, K, L)`. At every output entry, the two operands must be

```text
B[i, j, l] and C[i, k, l].
```

Thus `B` needs an axis for `k`, and `C` needs an axis for `j`:

```text
B aligned: (I, J, 1, L)   -> B[i, j, 0, l]
C aligned: (I, 1, K, L)   -> C[i, 0, k, l]
```

Broadcasting supplies the missing indices, so both aligned tensors behave as if they had shape `(I, J, K, L)`.

### 2.1 Multiplication: `einsum` gives the index equation directly

For the product

$$
A_{ijkl}=B_{ijl}C_{ikl},
$$

use:

```python
A = np.einsum("ijl,ikl->ijkl", B, C)
```

Every index appears in the output, so no index is summed. `einsum` pairs the two values that share `i` and `l`, and takes every combination of `j` and `k`.

#### Advantages

- Lines up directly with the mathematical expression.
- Supports index reordering by choosing the output labels after `->`.

#### Limitations

- Only works for tensor multiplication (and optional summation), not other elementwise operations such as `+` or `**`.

### 2.2 Insert axes with `None`

`None` inserts a length-one axis exactly where it appears in the index expression:

```python
B_aligned = B[:, :, None, :]  # (I, J, 1, L): insert the k axis
C_aligned = C[:, None, :, :]  # (I, 1, K, L): insert the j axis

A_product = B_aligned * C_aligned
A_sum = B_aligned + C_aligned
```

Their entries are

$$
\begin{aligned}
(A_{\text{product}})_{ijkl} &= B_{ijl}C_{ikl},\\
(A_{\text{sum}})_{ijkl} &= B_{ijl}+C_{ikl}.
\end{aligned}
$$

For real-valued tensors, the elementwise power is written with `**` in NumPy:

```python
A_power = B_aligned ** C_aligned
```

so

$$
(A_{\text{power}})_{ijkl}=B_{ijl}^{C_{ikl}}.
$$

Do not write `B_aligned ^ C_aligned` for powers: in NumPy, `^` is bitwise XOR, not exponentiation. It is only appropriate for integer or Boolean bit operations.

The assignments are optional; the concise form is often easiest to read:

```python
A_product = B[:, :, None, :] * C[:, None, :, :]
A_sum = B[:, :, None, :] + C[:, None, :, :]
A_power = B[:, :, None, :] ** C[:, None, :, :]
```

#### Advantages

- Works with other elementwise operators such as `*`, `+`, `-`, `/`, and `**`.

#### Limitations

- Does not show explicit index letters.
- Cannot reorder axes.
- Cannot remove a size-`1` axis; use `np.squeeze` for that operation.

### 2.3 Insert the same axes with `reshape`

`reshape` expresses the same alignment through target shapes:

```python
I, J, L = B.shape
_, K, _ = C.shape

B_aligned = B.reshape(I, J, 1, L)
C_aligned = C.reshape(I, 1, K, L)

A_product = B_aligned * C_aligned
A_sum = B_aligned + C_aligned
A_power = B_aligned ** C_aligned
```

The operands passed to the arithmetic operator have exactly the same shapes as in the `None` method, so the results are identical.

#### Advantages

- Provides the greatest flexibility when working with dynamic dimensions, including removing a size-`1` dimension.

#### Limitations

- Verbose.
- Cannot reorder axes.

### Comparison

| Method | Product $B_{ijl}C_{ikl}$ | Addition / power | Best use |
| --- | --- | --- | --- |
| `einsum` | `np.einsum('ijl,ikl->ijkl', B, C)` | Not directly available | Mirror an index-based product or contraction |
| `None` | `B[:, :, None, :] * C[:, None, :, :]` | Replace `*` with `+` or `**` | Show exactly where each missing axis goes |
| `reshape` | `B.reshape(I,J,1,L) * C.reshape(I,1,K,L)` | Replace `*` with `+` or `**` | Work from explicitly computed shapes |

All three multiplication expressions produce an array of shape `(I, J, K, L)`.

## 3. Unknown number of leading dimensions: `...`

Machine-learning code often preserves an unknown number of leading axes. For example, a tensor might have batch axes, heads, or several grouping axes before its final two meaningful axes.

Suppose

```text
B[..., j, l] has shape (*leading, J, L)
C[..., k, l] has shape (*leading, K, L)
```

where the leading shapes are the same (or broadcast-compatible), but their number of axes is not known in advance. We want

$$
A_{\ldots jkl}=B_{\ldots jl}+C_{\ldots kl}.
$$

Use an ellipsis followed by an inserted singleton axis:

```python
A = B[..., :, None, :] + C[..., None, :, :]
```

Read the two operands as follows:

```text
B[..., :, None, :]  -> (*leading, J, 1, L)
C[..., None, :, :]  -> (*leading, 1, K, L)
result                -> (*leading, J, K, L)
```

The ellipsis preserves every leading axis; `:` names `j` or `k`; `None` inserts the other axis; and the final `:` preserves `l`. The same alignment works for any elementwise operator:

```python
A_product = B[..., :, None, :] * C[..., None, :, :]
A_sum = B[..., :, None, :] + C[..., None, :, :]
A_power = B[..., :, None, :] ** C[..., None, :, :]
```

For multiplication only, `einsum` also accepts an ellipsis:

```python
A_product = np.einsum("...jl,...kl->...jkl", B, C)
```

This form says that the leading indices match by position and remain in the output. It is especially useful for checking the index pattern, while the `None` form is the general solution for arbitrary elementwise arithmetic.

## 4. Dynamic `reshape`

The preceding `None` expression is usually the most robust choice when the number of leading dimensions is unknown. If a `reshape` is required, build the target shape from `shape` rather than hard-coding its order:

```python
# B.shape is (*leading, J, L)
B_new_shape = B.shape[:-1] + (1,) + B.shape[-1:]
B_aligned = B.reshape(B_new_shape)

# C.shape is (*leading, K, L)
C_new_shape = C.shape[:-2] + (1,) + C.shape[-2:]
C_aligned = C.reshape(C_new_shape)

A = B_aligned + C_aligned
```

Technically, code can build a `new_shape` that inserts a `1` at any position—for example, one singleton axis after every original axis—although that pattern is rarely useful. This is what gives dynamic `reshape` the highest degree of freedom.

The two shapes are respectively `(*leading, J, 1, L)` and `(*leading, 1, K, L)`. Notice that the singleton is inserted **before** the final two axes of `C`, but only before the final axis of `B`. That difference is exactly what gives the output separate `j` and `k` axes.

For example, if `leading == (batch, heads)`, then:

```text
B: (batch, heads, J, L) -> (batch, heads, J, 1, L)
C: (batch, heads, K, L) -> (batch, heads, 1, K, L)
A:                         (batch, heads, J, K, L)
```

## 5. A small check

```python
import numpy as np

B = np.arange(2 * 3 * 5).reshape(2, 3, 5)        # (I, J, L)
C = np.arange(2 * 4 * 5).reshape(2, 4, 5) + 1    # (I, K, L)

by_einsum = np.einsum("ijl,ikl->ijkl", B, C)
by_none = B[:, :, None, :] * C[:, None, :, :]
by_reshape = B.reshape(2, 3, 1, 5) * C.reshape(2, 1, 4, 5)

assert by_einsum.shape == (2, 3, 4, 5)
assert np.array_equal(by_einsum, by_none)
assert np.array_equal(by_einsum, by_reshape)

# Addition uses the same alignment, not einsum.
sum_result = B[:, :, None, :] + C[:, None, :, :]
assert sum_result.shape == (2, 3, 4, 5)
```

## 6. Practice: translate between index notation and NumPy

For each problem, state the shape of every input and result. When broadcasting is used, identify the singleton axes that make the operation possible.

### A. From math to code

Unless a question explicitly asks for `einsum`, write ordinary NumPy broadcasting code. Assume `import numpy as np` has already run.

1. `B.shape == (I, J, L)` and `C.shape == (I, K, L)`. Write two implementations of

   $$
   A_{ijkl}=B_{ijl}C_{ikl}.
   $$

   Use `np.einsum` for one implementation and `None` indexing for the other.

2. With the same input shapes, write NumPy code for

   $$
   A_{ijkl}=B_{ijl}+C_{ikl}.
   $$

   Why is ordinary broadcasting more appropriate than `einsum` here?

3. With the same input shapes, write code for

   $$
   A_{ijkl}=B_{ijl}^{C_{ikl}}.
   $$

   Which NumPy operator means exponentiation? What operation would `B ^ C` perform instead?

4. `B.shape == (batch, heads, J, L)` and `C.shape == (batch, heads, K, L)`. Write code for

   $$
   A_{bhjkl}=B_{bhjl}-C_{bhkl}.
   $$

   First use `None`; then use `reshape` without hard-coding the values of the dimensions.

5. More generally, `B.shape == (*leading, J, L)` and `C.shape == (*leading, K, L)`. The length of `leading` is unknown. Write code for

   $$
   A_{\ldots jkl}=B_{\ldots jl}+C_{\ldots kl}.
   $$

6. Let `X.shape == (B, T, D)` and `bias.shape == (D,)`. Write a broadcasting expression for

   $$
   Y_{btd}=X_{btd}+\operatorname{bias}_d.
   $$

   Does this case require `None`? Explain briefly.

7. Let `B.shape == (J, I, L)` and `C.shape == (L, J, K, I)`. Write ordinary NumPy code for

   $$
   A_{ijk}=\sum_l B_{jil}^{C_{ljki}}.
   $$

   Your solution should use multiple steps to reorder axes, align the operands, and reduce over `l`.

8. Let `B.shape == (I, L)` and `C.shape == (L, J, K)`. Write ordinary NumPy code for

   $$
   A_{ijk}=\sum_l \left(B_{il}+C_{ljk}\right)^2.
   $$

   Use multiple steps to align the operands and reduce over `l`.

### B. From code to math

For each sample, write an index equation for the result, including every output index. State whether an axis is inserted, broadcast, or contracted.

1. ```python
   A = np.einsum("ijl,ikl->ijkl", B, C)
   ```

   Assume `B.shape == (I, J, L)` and `C.shape == (I, K, L)`.

2. ```python
   A = B[:, :, None, :] + C[:, None, :, :]
   ```

   Assume `B.shape == (I, J, L)` and `C.shape == (I, K, L)`.

3. ```python
   A = B[..., :, None, :] * C[..., None, :, :]
   ```

   Assume `B.shape == (*leading, J, L)` and `C.shape == (*leading, K, L)`.

4. ```python
   B_new_shape = B.shape[:-1] + (1,) + B.shape[-1:]
   C_new_shape = C.shape[:-2] + (1,) + C.shape[-2:]
   B_aligned = B.reshape(B_new_shape)
   C_aligned = C.reshape(C_new_shape)
   A = B_aligned ** C_aligned
   ```

   Use the same general shapes as the preceding problem.

5. ```python
   scores = query[..., :, None, :] * key[..., None, :, :]
   ```

   Assume `query.shape == (batch, heads, queries, features)` and `key.shape == (batch, heads, keys, features)`. Use `q`, `k`, and `f` as the final three index labels in your formula.

6. ```python
   Y = X + bias
   ```

   Assume `X.shape == (batch, tokens, features)` and `bias.shape == (features,)`.

7. ```python
   Y = X + bias
   ```

   Assume `X.shape == (batch, tokens, features, 1)` and `bias.shape == (features,)`. Identify:

   1. What is wrong with this expression for adding one bias value to each feature?
   2. Why can the code still execute, and what is the shape of its output?
   3. How would you fix the code so that the result has the intended shape?

### Answer check

Try the exercises before opening this section.

<details>
<summary>Suggested answers</summary>

**A1.**

```python
A_einsum = np.einsum("ijl,ikl->ijkl", B, C)
A_none = B[:, :, None, :] * C[:, None, :, :]
```

Both have shape `(I, J, K, L)`.

**A2.** `A = B[:, :, None, :] + C[:, None, :, :]`. `einsum` specifies multiplication and summation patterns, not elementwise addition. The result has shape `(I, J, K, L)`.

**A3.** `A = B[:, :, None, :] ** C[:, None, :, :]`. `**` is exponentiation; `^` is bitwise XOR. The result has shape `(I, J, K, L)`.

**A4.**

```python
A_none = B[..., :, None, :] - C[..., None, :, :]

B_new_shape = B.shape[:-1] + (1,) + B.shape[-1:]
C_new_shape = C.shape[:-2] + (1,) + C.shape[-2:]
B_aligned = B.reshape(B_new_shape)
C_aligned = C.reshape(C_new_shape)
A_reshape = B_aligned - C_aligned
```

Both results have shape `(batch, heads, J, K, L)`.

**A5.** `A = B[..., :, None, :] + C[..., None, :, :]`, with shape `(*leading, J, K, L)`.

**A6.** `Y = X + bias`; its shape is `(B, T, D)`. Right-aligned broadcasting matches `bias`'s only axis with the final `D` axis of `X`, so no axis needs to be inserted.

**A7.**

```python
B_reordered = B.transpose(1, 0, 2)       # (I, J, L)
C_reordered = C.transpose(3, 1, 2, 0)    # (I, J, K, L)
B_aligned = B_reordered[:, :, None, :]   # (I, J, 1, L)

A = (B_aligned ** C_reordered).sum(axis=-1)  # (I, J, K)
```

**A8.**

```python
B_aligned = B[:, None, None, :]          # (I, 1, 1, L)
C_reordered = C.transpose(1, 2, 0)[None, :, :, :]  # (1, J, K, L)

A = ((B_aligned + C_reordered) ** 2).sum(axis=-1)  # (I, J, K)
```

**B1.** $A_{ijkl}=B_{ijl}C_{ikl}$. No index is contracted because all four labels appear after `->`; `einsum` pairs all `j` and `k` values for matching `i,l`.

**B2.** $A_{ijkl}=B_{ijl}+C_{ikl}$. `B` gains a length-one third axis and `C` gains a length-one second axis; each is broadcast along that axis.

**B3.** $A_{\ldots jkl}=B_{\ldots jl}C_{\ldots kl}$. The ellipsis preserves and aligns all leading indices; the inserted singleton axes broadcast across `k` and `j`, respectively.

**B4.** $A_{\ldots jkl}=B_{\ldots jl}^{C_{\ldots kl}}$. The `B_new_shape` and `C_new_shape` calculations create the same singleton axes as in B3, and `**` is applied elementwise after broadcasting.

**B5.** $\text{scores}_{bhqkf}=\text{query}_{bhqf}\,\text{key}_{bhkf}$. The result has shape `(batch, heads, queries, keys, features)`; the inserted axes broadcast the query and key positions. This is not yet the usual attention score, which would also sum over `f`.

**B6.** $Y_{btf}=X_{btf}+\operatorname{bias}_f$. `bias` is broadcast across the batch and token axes; no axes are contracted.

**B7.** The trailing size-`1` axis causes `bias` to align with that final axis rather than with `X`'s `features` axis. NumPy treats the shapes as `(batch, tokens, features, 1)` and `(1, 1, 1, features)`, so the code runs but produces shape `(batch, tokens, features, features)`. Use `Y = X + bias[None, None, :, None]`; then `Y.shape == (batch, tokens, features, 1)` and $Y_{btf0}=X_{btf0}+\operatorname{bias}_f$.

</details>

## 7. Summary

- Broadcasting aligns axes from the right; equal sizes or a size of `1` are compatible.
- To form $A_{ijkl}$ from $B_{ijl}$ and $C_{ikl}$, align the inputs as `(I, J, 1, L)` and `(I, 1, K, L)`.
- `np.einsum('ijl,ikl->ijkl', B, C)` is precise for the multiplicative index equation.
- `B[:, :, None, :]` and `C[:, None, :, :]` expose the necessary singleton axes and work with `*`, `+`, `**`, and other elementwise operators.
- With unknown leading dimensions, use `B[..., :, None, :]` and `C[..., None, :, :]` to preserve them.
- In NumPy, `**` means exponentiation; `^` means bitwise XOR.
