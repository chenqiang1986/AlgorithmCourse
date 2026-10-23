# Lesson 3: Linear Regression from Scratch with NumPy
*ML / M06 — Supervised Learning*

## The goal

Implement the data creation, forward pass, mean-squared loss, analytical
gradients, and gradient-descent update yourself. NumPy performs array
arithmetic only; it does not differentiate or train for us.

## 1. The vectorized gradients

For $X\in\mathbb R^{n\times d}$, $w\in\mathbb R^d$, scalar bias $b$, and

$$
L(w,b)=\frac1n\lVert Xw+b\mathbf1-y\rVert_2^2,
$$

let $r=Xw+b\mathbf1-y$. Then

$$
\nabla_wL=\frac{2}{n}X^Tr,
\qquad
\frac{\partial L}{\partial b}=\frac{2}{n}\sum_{i=1}^n r_i.
$$

\`X.T @ residual\` computes all feature gradients at once—no Python loop over
examples is needed.

## 2. Complete hand implementation

~~~python
import numpy as np

rng = np.random.default_rng(7)
n, d = 200, 3
X = rng.normal(size=(n, d))
true_w = np.array([2.0, -3.0, 0.5])
true_b = 1.25
y = X @ true_w + true_b + rng.normal(scale=0.25, size=n)

def linear_forward(X, w, b):
    """Return one prediction per row of X."""
    return X @ w + b


def mse_loss(prediction, target):
    """Mean squared error for a batch of predictions."""
    return np.mean((prediction - target) ** 2)


def linear_mse_gradient(X, prediction, target):
    """Return the gradients with respect to w and b."""
    residual = prediction - target
    n = len(target)
    grad_w = (2 / n) * (X.T @ residual)
    grad_b = 2 * residual.mean()
    return grad_w, grad_b


def gradient_descent(X, y, w, b, forward_fn, loss_fn, gradient_fn,
                     learning_rate, steps, log_every=None):
    """Train a model with weights w and bias b using full-batch gradient descent."""
    w = w.copy()

    for step in range(steps):
        prediction = forward_fn(X, w, b)
        loss = loss_fn(prediction, y)
        grad_w, grad_b = gradient_fn(X, prediction, y)

        w -= learning_rate * grad_w
        b -= learning_rate * grad_b

        if log_every is not None and step % log_every == 0:
            print(f"step={step:4d}  mse={loss:.6f}")

    return w, b


w, b = gradient_descent(
    X, y,
    w=np.zeros(d),
    b=0.0,
    forward_fn=linear_forward,
    loss_fn=mse_loss,
    gradient_fn=linear_mse_gradient,
    learning_rate=0.05,
    steps=2_000,
    log_every=400,
)

print("learned w:", w)
print("learned b:", b)
~~~

The estimates should be near \`true_w\` and \`true_b\`, but not identical because
the targets contain random noise. The optimizer is reusable for models with a
weight vector and scalar bias, while the linear-regression math stays in the
three small functions above.

## 3. Check the gradient numerically

An implementation can look plausible while having a missing factor or wrong
sign. A finite-difference check compares the analytical derivative with a
small perturbation.

~~~python
epsilon = 1e-6
j = 0
w_plus, w_minus = w.copy(), w.copy()
w_plus[j] += epsilon
w_minus[j] -= epsilon
numeric = (
    mse_loss(linear_forward(X, w_plus, b), y)
    - mse_loss(linear_forward(X, w_minus, b), y)
) / (2 * epsilon)

prediction = linear_forward(X, w, b)
analytic_grad_w, _ = linear_mse_gradient(X, prediction, y)
analytic = analytic_grad_w[j]
print(numeric, analytic, np.isclose(numeric, analytic, rtol=1e-4))
~~~

Run this check before training or after a small number of steps. Very tiny
\`epsilon\` is not always better: floating-point cancellation eventually harms
the numerical approximation.

## 4. Compare with least squares

For this small dense problem, compute the OLS optimum without explicitly
forming $(X^TX)^{-1}$:

~~~python
X_augmented = np.column_stack([np.ones(n), X])
beta_lstsq, residual_sum, rank, singular_values = np.linalg.lstsq(
    X_augmented, y, rcond=None
)
print("least-squares bias:", beta_lstsq[0])
print("least-squares weights:", beta_lstsq[1:])
print("design rank:", rank)
~~~

Gradient descent should approach this solution with a suitable learning rate.
If it diverges, first standardize feature columns and lower the learning rate.

## Homework: solve linear regression with the normal equation

Implement a function that learns the bias and weights directly from the
normal equation—do not use gradient descent or `np.linalg.lstsq` for this
exercise. First add a column of ones to `X` so the bias is part of the
parameter vector, then compute

$$
\beta = (X_{\mathrm{aug}}^T X_{\mathrm{aug}})^{-1}X_{\mathrm{aug}}^T y.
$$

Return `beta[0]` as the bias and `beta[1:]` as the weights. Test your result
against the data generated above and compare its predictions with the
gradient-descent model.

Hint: `np.linalg.inv` can compute the inverse in the formula above.

Question: what happens if $X_{\mathrm{aug}}^T X_{\mathrm{aug}}$ is singular?
What properties of the data could make this happen, and what alternative
approach would you use?

## Common shape mistakes

- Keep targets as \`(n,)\` here; mixing \`(n,)\` and \`(n, 1)\` can silently
  broadcast to an \`(n, n)\` residual matrix.
- Initialize \`w\` with shape \`(d,)\`, not \`(d, 1)\`, unless every other quantity
  is intentionally column-shaped.
- Do not update \`w\` before computing \`grad_b\` from the same residual.

## Key takeaways

- A full-batch training step is forward pass, residual, loss, gradients, then
  simultaneous parameter updates.
- \`X.T @ residual\` is the vectorized weight gradient.
- Finite differences are a useful independent gradient check.
- \`np.linalg.lstsq\` is a stable reference solution for OLS.
