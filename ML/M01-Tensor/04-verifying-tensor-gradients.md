# Lesson 4: Verifying Tensor Gradients with Code
*ML / M01-Tensor*

A gradient formula is often simple to write and easy to get subtly wrong. A **directional derivative** gives a compact numerical check: instead of perturbing every entry of a tensor one at a time, perturb all entries together in one chosen direction and compare the observed change with the change predicted by the analytical gradient.

This lesson verifies the gradient of the scalar tensor function

$$
f(X)=\sum_{i,j} X_{ij}^2.
$$

The method is the same for a vector, matrix, or higher-order tensor, provided that `X` and the direction `delta` have the same shape.

## 1. Basic idea

Let $X$ be the input tensor and let $\Delta$ be another tensor of the same shape. For a small positive number $t$, move a short distance from $X$ in direction $\Delta$:

$$
X \longmapsto X+t\Delta.
$$

The directional derivative measures the rate at which the scalar function changes along that line:

$$
D_{\Delta}f(X)=\lim_{t\to0}
\frac{f(X+t\Delta)-f(X)}{t}.
$$

### Numerical approximation

Code cannot take $t$ all the way to zero, so it uses a small value:

$$
\boxed{
\frac{f(X+t\Delta)-f(X)}{t}
}
$$

This is the **forward finite-difference** estimate. Its error is typically proportional to $t$: making `t` smaller initially improves the estimate, although an extremely small `t` can reveal floating-point roundoff error.

### Analytical prediction

If the analytical gradient $\nabla_X f(X)$ is correct, its contraction with the direction predicts exactly the same instantaneous rate:

$$
\boxed{
D_{\Delta}f(X)=\nabla_X f(X):\Delta
=\sum_{i,j}\frac{\partial f}{\partial X_{ij}}\Delta_{ij}
}
$$

The colon means elementwise multiplication followed by summation over every axis of the input tensor. For vectors, it is a dot product; for matrices, it is the Frobenius inner product.

For the running example,

$$
\frac{\partial f}{\partial X_{ij}}=2X_{ij},
\qquad \nabla_Xf(X)=2X,
$$

so the analytical directional derivative is

$$
D_{\Delta}f(X)=(2X):\Delta.
$$

## 2. When the output is also a tensor

The same check works when $F(X)$ is a tensor rather than a scalar. In that case, the directional derivative is a tensor with the same shape as the output:

$$
D_{\Delta}F(X)=\lim_{t\to0}
\frac{F(X+t\Delta)-F(X)}{t}.
$$

Following the module's convention from Lesson 2, the full gradient has its output axes first and its input axes last:

```text
F(X).shape      == output_shape
X.shape         == input_shape
grad_F(X).shape == output_shape + input_shape
```

Therefore the analytical check must contract **only the final `delta.ndim` axes** of the gradient. The leading output axes remain in the result:

$$
\left(D_{\Delta}F(X)\right)_{j_1\ldots j_q}
=
\sum_{i_1,\ldots,i_p}
\frac{\partial F_{j_1\ldots j_q}}
     {\partial X_{i_1\ldots i_p}}
\Delta_{i_1\ldots i_p}.
$$

For example, if $Y_{ij}=X_{ij}^2$, then

$$
\frac{\partial Y_{ij}}{\partial X_{kl}}
=2X_{ij}\delta_{ik}\delta_{jl},
$$

and contracting the last two axes with $\Delta_{kl}$ gives the matrix

$$
\left(D_{\Delta}Y(X)\right)_{ij}=2X_{ij}\Delta_{ij}.
$$

Do not use `np.sum(gradient(X) * delta)` for this general case: broadcasting can align the arrays, but that sum would incorrectly remove the output axes too. `np.tensordot` states exactly which axes to contract.

## 3. Code organization

Keep the four ideas separate. This makes a gradient-checking script easy to reuse when the function changes.

| Part | Role |
| --- | --- |
| `objective` | Original scalar function $f(X)$ |
| `gradient_objective` | Hand-derived analytical gradient $\nabla_X f(X)$ |
| `numerical_directional_derivative` | Forward finite difference from the original function |
| `analytical_directional_derivative` | Gradient contraction $\nabla_Xf(X):\Delta$ |

The `main` function only chooses `X`, `delta`, and a step size, calls the two checks, and prints their results.

When the input is always a matrix, the two input axes can be written directly with `einsum` instead of being computed dynamically:

```python
def analytical_directional_derivative_matrix_input(gradient, X, delta):
    # Gradient axes: output axes ..., then matrix-input axes i, j.
    # Contract i and j; retain every output axis represented by ....
    return np.einsum("...ij,ij->...", gradient(X), delta)
```

Here `i` and `j` are the two axes of `delta` and the final two axes of the gradient. The ellipsis (`...`) represents zero or more output axes, so this helper works for both scalar and tensor outputs. It assumes that `X` and `delta` are matrices; use the general `tensordot` helper when the input rank may vary.

```python
import numpy as np


def objective(X):
    """Original function: f(X) = sum_ij X_ij^2."""
    return np.sum(X**2)


def gradient_objective(X):
    """Analytical gradient: grad f(X) = 2X."""
    return 2 * X


def numerical_directional_derivative(function, X, delta, step):
    """Estimate D_delta f(X) using a forward finite difference."""
    return (function(X + step * delta) - function(X)) / step


def analytical_directional_derivative(gradient, X, delta):
    """Compute D_delta f(X) = grad f(X) : delta.

    The gradient axes are ordered as output axes followed by input axes.
    Contract only the trailing input axes, leaving any output axes intact.
    """
    gradient_value = gradient(X)
    input_axes_of_gradient = tuple(
        range(gradient_value.ndim - delta.ndim, gradient_value.ndim)
    )
    input_axes_of_delta = tuple(range(delta.ndim))
    return np.tensordot(
        gradient_value, delta, axes=(input_axes_of_gradient, input_axes_of_delta)
    )


def analytical_directional_derivative_matrix_input(gradient, X, delta):
    """Matrix-input version: contract the final two gradient axes with delta."""
    return np.einsum("...ij,ij->...", gradient(X), delta)


def main():
    rng = np.random.default_rng(seed=43)
    X = rng.normal(size=(2, 3))
    delta = np.array([[1.0, 1.0, 0.0], [-1.0, 0.0, 1.0]])
    step = 1e-6

    numerical = numerical_directional_derivative(objective, X, delta, step)
    analytical = analytical_directional_derivative(gradient_objective, X, delta)
    analytical_matrix_input = analytical_directional_derivative_matrix_input(
        gradient_objective, X, delta
    )

    print(f"Numerical directional derivative:  {numerical:.10f}")
    print(f"Analytical directional derivative: {analytical:.10f}")
    print(f"Matrix-input einsum result:        {analytical_matrix_input:.10f}")
    print(f"Absolute difference:               {abs(numerical - analytical):.3e}")


if __name__ == "__main__":
    main()
```

The same runnable code is available in [`ws/tensor_derivative_verification.py`](ws/tensor_derivative_verification.py).

## 4. Reading the result

Run the program from the repository root:

```bash
python ML/M01-Tensor/ws/tensor_derivative_verification.py
```

The numerical and analytical values should agree closely, with a small difference caused by the finite step. They will not generally be bit-for-bit identical because the numerical value approximates a limit.

To check another scalar tensor function:

1. Replace `objective` with the original function.
2. Replace `gradient_objective` with its hand-derived gradient.
3. Keep `delta` the same shape as `X`.
4. Compare the two printed values for several reasonable step sizes, such as `1e-4`, `1e-5`, and `1e-6`.

If the discrepancy stays large across sensible step sizes, first check the analytical gradient's signs, coefficients, and axes. A directional check does not prove a gradient is correct in every direction, so test multiple nonzero directions before trusting a new implementation.

## 5. Practice

Let

$$
g(X)=\sum_{i,j}\sin(X_{ij}).
$$

1. Derive $\nabla_X g(X)$.
2. Replace `objective` and `gradient_objective` in the program.
3. Verify the gradient with at least three different directions `delta`.
4. Compare what happens as `step` decreases from `1e-3` to `1e-8`.
