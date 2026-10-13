# Lesson 4: Synthetic Regression Data — $y=f(X)+\varepsilon$
*ML / D06-Numpy-Torch-Random-Gen*

Synthetic data is especially useful when we want to know the true pattern. We
choose a function $f$, generate random features $X$, and add an independent
random noise term $\varepsilon$:

$$
\boxed{y=f(X)+\varepsilon.}
$$

The function is the signal. The extra random term is irreducible noise: even a
perfect model of $f$ cannot predict its exact realized value.

## 1. Linear Data in NumPy

For $d$ features, a linear data-generating process is

$$
y=Xw+b+\varepsilon,
\qquad
\varepsilon\sim\mathcal{N}(0,\sigma^2 I).
$$

```python
import numpy as np

rng = np.random.default_rng(42)

n_samples = 1_000
n_features = 3
noise_std = 0.5

X = rng.normal(loc=0.0, scale=1.0, size=(n_samples, n_features))
true_w = np.array([2.0, -1.5, 0.75])
true_b = np.array([3.0])

signal = X @ true_w + true_b
noise = rng.normal(loc=0.0, scale=noise_std, size=n_samples)
y = signal + noise

assert X.shape == (1_000, 3)
assert true_w.shape == (3,)
assert true_b.shape == (1,)
assert y.shape == (1_000,)
```

`noise_std` is $\sigma$. The variance of the noise is `noise_std ** 2`.
Calling it `noise_variance` and passing it as `scale` would be a parameter bug.

## 2. The Same Data-Generating Process in PyTorch

```python
import torch

g = torch.Generator().manual_seed(42)

n_samples = 1_000
n_features = 3
noise_std = 0.5

X = torch.randn((n_samples, n_features), generator=g)
true_w = torch.tensor([2.0, -1.5, 0.75])
true_b = torch.tensor([3.0])

signal = X @ true_w + true_b
noise = noise_std * torch.randn((n_samples,), generator=g)
y = signal + noise

assert X.shape == (1_000, 3)
assert true_w.shape == (3,)
assert true_b.shape == (1,)
assert y.shape == (1_000,)
```

The NumPy and PyTorch versions use the same convention: `true_w`, `signal`,
`noise`, and `y` are one-dimensional. The one-element `true_b` is also
one-dimensional and adds the same intercept to every observation.

## 3. Noise Controls Difficulty

Use the same $X$ and signal while changing only the noise level:

```python
rng = np.random.default_rng(42)
X_comparison = rng.standard_normal((n_samples, n_features))
signal_np = X_comparison @ np.array([2.0, -1.5, 0.75]) + 3.0
noise_unit = rng.normal(size=n_samples)

y_clean = signal_np + 0.0 * noise_unit
y_easy = signal_np + 0.2 * noise_unit
y_hard = signal_np + 3.0 * noise_unit
```

Reusing `noise_unit` makes the comparison controlled: the direction of every
noise value stays fixed while only its size changes. With larger $\sigma$, the
points spread farther from $f(X)$ and prediction metrics worsen.

The conditional mean is still

$$
E[y\mid X]=f(X)
$$

when the noise has mean zero and is independent of $X$.

## 4. Nonlinear Targets

The target function does not have to be linear.

```python
# NumPy: two input features and one nonlinear target
rng = np.random.default_rng(7)
X = rng.uniform(-3.0, 3.0, size=(2_000, 2))

signal = (
    2.0 * np.sin(X[:, 0])
    + 0.5 * X[:, 1] ** 2
    - X[:, 0] * X[:, 1]
)
noise = rng.normal(0.0, 0.3, size=len(X))
y = signal + noise
```

```python
# PyTorch equivalent
g = torch.Generator().manual_seed(7)
X = -3.0 + 6.0 * torch.rand((2_000, 2), generator=g)

signal = (
    2.0 * torch.sin(X[:, 0])
    + 0.5 * X[:, 1] ** 2
    - X[:, 0] * X[:, 1]
)
noise = 0.3 * torch.randn((len(X),), generator=g)
y = signal + noise
```

This is useful for testing whether a model can learn curvature and feature
interactions.

## 5. Heteroscedastic Noise

Constant-variance noise is called **homoscedastic**. Some real problems become
noisier as a feature grows. We can simulate that too:

```python
rng = np.random.default_rng(10)
X = rng.uniform(0.0, 10.0, size=(1_500, 1))

signal = 4.0 + 2.0 * X[:, 0]
local_noise_std = 0.1 + 0.25 * X[:, 0]
noise = local_noise_std * rng.standard_normal(len(X))
y = signal + noise
```

Now

$$
\operatorname{Var}(y\mid X=x)
=\left(0.1+0.25x\right)^2,
$$

so residual spread grows with $x$.

## 6. Separate Data Noise from Parameter Randomness

These are different experiments:

- random $X$, fixed $w$: test whether training recovers a known rule;
- random $X$, random $w$: create many related tasks;
- fixed $X$, new $\varepsilon$: study repeated measurements;
- new $X$, new $\varepsilon$: create a new dataset from the same population.

For a basic learning experiment, keep the true parameters visible and fixed.
Otherwise it becomes difficult to tell whether a change came from the data, the
noise, or the underlying task.

## 7. A Reusable NumPy Function

```python
def make_linear_regression_data(
    n_samples=1_000,
    weights=(2.0, -1.5, 0.75),
    bias=3.0,
    noise_std=0.5,
    seed=42,
):
    rng = np.random.default_rng(seed)
    weights = np.asarray(weights, dtype=float)
    bias = np.asarray(bias, dtype=float).reshape(1)

    X = rng.standard_normal((n_samples, len(weights)))
    signal = X @ weights + bias
    noise = rng.normal(0.0, noise_std, size=n_samples)
    y = signal + noise

    return X, y
```

Keep `seed` as an argument so callers can reproduce one dataset or request a
new realization deliberately.

## 8. Class Practice

1. Generate $X$ with shape `(500, 4)` and a target using known coefficients.
2. Generate three targets from the same signal with noise standard deviations
   `0.0`, `0.5`, and `2.0`.
3. Assert that `true_w`, `true_b`, `signal`, `noise`, and `y` follow the
   one-dimensional convention used in this lesson.
4. Create a nonlinear target containing a squared term and an interaction term.
5. Create noise whose standard deviation is larger for rows where `X[:, 0] > 0`.

## 9. Key Takeaways

- Synthetic regression starts with $X$, computes a signal $f(X)$, then adds a
  separate random error term.
- Normal samplers take a standard deviation; variance is its square.
- Keep signal and noise in separate variables so the experiment is inspectable.
- Use the same one-dimensional parameter and target convention in NumPy and
  PyTorch code.
- Changing the noise distribution or scale changes the learning problem even
  when the true function remains fixed.

