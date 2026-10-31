# Homework: The Moore--Penrose Pseudoinverse
*ML / M02 — Linear Algebra, Class 7*

Use the [pseudoinverse lesson](./07-pseudoinverse.md) as a reference. Show
your algebra for the hand calculation and include both your code and its
output for the computational parts.

## 1. Three ways to compute a pseudoinverse

Let

$$
A=
\begin{pmatrix}
1&1\\
1&-1\\
1&1
\end{pmatrix}.
$$

This is a full-column-rank $3\times2$ matrix, so its pseudoinverse has shape
$2\times3$.

1. **By hand, using an SVD.** Compute $A^+$ without using software or the
   full-column-rank identity. Construct a compact SVD

   $$
   A=U_r\Sigma_rV_r^T,
   $$

   then use

   $$
   A^+=V_r\Sigma_r^{-1}U_r^T.
   $$

   Show $A^TA$, its eigenvalues and orthonormal eigenvectors, $V_r$,
   $\Sigma_r$, and $U_r$. Then show your final $2\times3$ matrix.

   *Hint:* The columns of $V_r$ are the orthonormal eigenvectors of $A^TA$.
   The singular values on the diagonal of $\Sigma_r$ are the square roots of
   the corresponding eigenvalues of $A^TA$. After finding $V_r$ and
   $\Sigma_r$, compute $U_r=AV_r\Sigma_r^{-1}$.

2. **With NumPy's built-in pseudoinverse.** Use `np.linalg.pinv(A)` to
   compute $A^+$. Print the result.

3. **From an SVD.** Use `np.linalg.svd(A, full_matrices=False)` to obtain
   `U`, `s`, and `Vt`. Build $\Sigma^{-1}$ by replacing each nonzero singular
   value in `s` with its reciprocal, then compute

   $$
   A^+=V\Sigma^{-1}U^T
   $$

   in code. (In NumPy, $V$ is `Vt.T`.) Print this result.

4. **Verify.** Use `np.allclose` to verify that the three results agree.
   Also report the largest absolute entrywise difference between the hand
   result and each NumPy result. Briefly explain why tiny nonzero differences,
   if any, are expected.

You may start from this template:

```python
import numpy as np

A = np.array([[1., 1.],
              [1., -1.],
              [1., 1.]])

# Part 1: replace with your hand result
A_plus_hand = np.array([[..., ..., ...],
                        [..., ..., ...]])

# Part 2
A_plus_pinv = np.linalg.pinv(A)

# Part 3
U, s, Vt = np.linalg.svd(A, full_matrices=False)
Sigma_inv = np.diag(1 / s)
A_plus_svd = Vt.T @ Sigma_inv @ U.T

print("hand:\\n", A_plus_hand)
print("pinv:\\n", A_plus_pinv)
print("SVD:\\n", A_plus_svd)
print("hand agrees with pinv:", np.allclose(A_plus_hand, A_plus_pinv))
print("hand agrees with SVD:", np.allclose(A_plus_hand, A_plus_svd))
print("max |hand - pinv|:", np.max(np.abs(A_plus_hand - A_plus_pinv)))
print("max |hand - SVD|:", np.max(np.abs(A_plus_hand - A_plus_svd)))
```
