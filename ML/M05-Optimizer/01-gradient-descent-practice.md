# Practice Set 1: Implement Gradient Descent by Hand
*ML / M05 — Optimizer*

Use NumPy unless a problem explicitly asks for PyTorch. Do not use
`torch.optim`, scikit-learn estimators, automatic differentiation, or a
numerical-gradient helper. Write each derivative and each update yourself.

## Problem 1: Scalar quadratic

Implement 20 steps of gradient descent for $f(x)=5x^2-20x+7$, beginning at
$x_0=-3$. Run it with learning rates $0.01$, $0.10$, and $0.25$. For each run,
record $x_0$, $x_1$, $x_2$, final $x$, and final loss. Which runs converge?

## Problem 2: Predict the stability boundary

For $f(x)=12x^2$, derive the update factor multiplying $x_t$. Find the
convergence boundary (the supremum of learning rates for which iterates
converge). Test rates just below and just
above that boundary from $x_0=1$ and print the first ten iterates.

## Problem 3: Two-dimensional bowl

Implement gradient descent for

$$
f(x,y)=x^2+20y^2.
$$

Start at $(8,8)$. Run 100 steps with $\eta=0.02$ and $\eta=0.08$. Store every
point. Explain the different behavior using Hessian eigenvalues. Then try a
stable rate that makes the $y$ direction converge without oscillation.

## Problem 4: Hand-coded linear regression

Generate 200 data points with seed `17`:

~~~python
X = rng.normal(size=(200, 2))
y = 2.5 * X[:, 0] - 1.2 * X[:, 1] + 0.7 + rng.normal(scale=0.15, size=200)
~~~

Write `mse_and_grads(X, y, w, b)`. Train from zero parameters for 500
full-batch steps. Print loss every 100 steps, report final $w$ and $b$, and
assert that the final loss is smaller than the initial loss.

## Problem 5: The scaling trap

Repeat Problem 4 after multiplying only `X[:, 1]` by `1_000`. First use the
same learning rate and describe the result. Then standardize both feature
columns using training-set mean and standard deviation, retrain, and compare.
Explain why feature scaling changes a safe practical rate.

## Problem 6: Batch-size twist

Modify Problem 4 to use one shuffled mini-batch of 20 rows per update. Compute
gradients using the mini-batch size in the denominator. Compare 500 mini-batch
updates with 500 full-batch updates using the same nominal rate. Which trace is
noisier, and why?

## Problem 7: Gradient checker

For the loss from Problem 4, choose random $w$ and $b$. Approximate one
coordinate of $\nabla_wL$ and the bias derivative with centered differences:

$$
\frac{L(\theta+\varepsilon)-L(\theta-\varepsilon)}{2\varepsilon},
\qquad\varepsilon=10^{-5}.
$$

Compare with your analytic gradient and report absolute error.

## Problem 8: Learning-rate protocol

With standardized data from Problem 5, run 200 updates using rates
`[1e-4, 1e-3, 1e-2, 1e-1, 1.0]`. Keep initialization, data, and update count
fixed. Make a table with final loss and a label: `slow`, `useful`,
`oscillating`, or `diverged`. Choose one rate for the next lesson and justify
it from evidence.
