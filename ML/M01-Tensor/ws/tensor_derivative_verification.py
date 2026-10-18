"""Verify a hand-derived tensor gradient with a directional derivative."""

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
    """Matrix-input version: contract the final two gradient axes with delta.

    If the output has axes represented by ``...``, the gradient has shape
    ``... + (rows, columns)``.  The result retains ``...``.
    """
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
