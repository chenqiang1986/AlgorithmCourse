# Lesson 1: Shapes, Seeds, and Uniform Random Values
*ML / D06-Numpy-Torch-Random-Gen*

Machine-learning code frequently needs an array with a known shape before it
needs realistic data. Random generation lets us create that array immediately.
The important questions are:

- What should the shape be?
- What values are allowed?
- Should another run reproduce the same values?

## 1. Shape Means the Same Thing in Both Libraries

For a training feature matrix,

$$
X\in\mathbb{R}^{n\times d},
$$

$n$ is the number of observations and $d$ is the number of features. Therefore,
`X.shape` should be `(n, d)`.

```python
n = 100       # observations (rows)
d = 4         # features (columns)
shape = (n, d)
```

A single target per row can have either shape `(n,)` or `(n, 1)`. Both can be
valid, but they do not broadcast in the same way. Always inspect the shape your
model expects.

## 2. NumPy: Create a Generator, Then Draw Samples

The modern NumPy style is to create a local `Generator` with `default_rng`.

```python
import numpy as np

rng = np.random.default_rng(42)

X = rng.random(size=(100, 4))
print(X.shape)       # (100, 4)
print(X.dtype)       # usually float64
print(X.min(), X.max())
```

Every value is sampled uniformly from the half-open interval $[0,1)$. Uniform
means equal-length subintervals have equal probability.

To sample uniformly from $[a,b)$, use `uniform`:

```python
temperatures = rng.uniform(low=15.0, high=30.0, size=(7, 24))
```

This produces seven days by 24 hourly readings. The shape describes the layout;
`low` and `high` describe the distribution.

## 3. PyTorch: Create a Tensor Directly

```python
import torch

g = torch.Generator().manual_seed(42)

X = torch.rand((100, 4), generator=g)
print(X.shape)       # torch.Size([100, 4])
print(X.dtype)       # usually torch.float32
print(X.min(), X.max())
```

`torch.rand` also samples uniformly from $[0,1)$. Scale and shift it to get
$[a,b)$:

```python
low, high = 15.0, 30.0
temperatures = low + (high - low) * torch.rand((7, 24), generator=g)
```

The transformation works because if $U\sim\operatorname{Uniform}(0,1)$, then

$$
a+(b-a)U\sim\operatorname{Uniform}(a,b).
$$

## 4. Random Integers

The upper endpoint is excluded in both APIs.

```python
# NumPy: values can be 0, 1, 2, 3, 4, or 5
dice_np = rng.integers(low=1, high=7, size=(20,))

# PyTorch: values can be 0, 1, 2, 3, 4, or 5
dice_torch = torch.randint(low=1, high=7, size=(20,), generator=g)
```

The shape `(20,)` means a one-dimensional collection of 20 rolls. The comma is
what makes `(20,)` a one-element tuple in Python.

## 5. Seeds and Reproducibility

Random generators are actually **pseudorandom**: a deterministic algorithm
produces a sequence that looks random. A seed chooses the starting state.

```python
rng_a = np.random.default_rng(7)
rng_b = np.random.default_rng(7)

print(rng_a.random(3))
print(rng_b.random(3))   # same three values
```

The same idea works with local PyTorch generators:

```python
g_a = torch.Generator().manual_seed(7)
g_b = torch.Generator().manual_seed(7)

print(torch.rand(3, generator=g_a))
print(torch.rand(3, generator=g_b))   # same three values
```

One generator advances after every draw. Reusing it does **not** repeat values:

```python
rng = np.random.default_rng(7)
first = rng.random(3)
second = rng.random(3)    # the next three values, not a repeat
```

During debugging, store the seed in one visible place. For a genuinely new
experiment, change the seed intentionally rather than scattering seed calls
throughout the program.

## 6. Dtype and Device in PyTorch

PyTorch tensors may participate in gradient-based training, so dtype and device
often matter.

```python
X64 = torch.rand((8, 3), dtype=torch.float64, generator=g)
X32 = torch.rand((8, 3), dtype=torch.float32, generator=g)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
X_device = torch.rand((8, 3), device=device)
```

A generator is associated with a device. For accelerator-specific reproducible
generation, create an appropriate generator for that device. Exact results are
not guaranteed to be identical across every PyTorch release, platform, and
device, even with the same seed.

## 7. A Shape Checklist

Before using generated data, inspect it:

```python
assert X.shape == (100, 4)
assert torch.isfinite(X).all()
print(X.dtype, X.device)
print(X.mean(dim=0))
```

For NumPy, the corresponding checks are:

```python
assert X.shape == (100, 4)
assert np.isfinite(X).all()
print(X.dtype)
print(X.mean(axis=0))
```

## 8. Class Practice

1. Generate a NumPy array of shape `(5, 3)` from $[0,1)$.
2. Generate a PyTorch tensor of shape `(2, 4, 6)` from $[-2,2)$.
3. Generate 100 integer class IDs from `{0, 1, 2}` in both libraries.
4. Prove by experiment that two generators with the same seed start with the
   same values, but two consecutive calls to one generator do not.

## 9. Key Takeaways

- Shape says how samples are organized; the distribution says how values are
  chosen.
- Prefer `np.random.default_rng(seed)` over NumPy's older global random API.
- A local `torch.Generator` avoids changing the global PyTorch random stream.
- Both integer APIs exclude the upper endpoint.
- A seed supports debugging and comparison; it does not make an experiment
  universally identical across all software and hardware.

