# D06 — Random Data with NumPy and PyTorch
*ML / D06-Numpy-Torch-Random-Gen*

Random data is useful for testing code, understanding probability distributions,
and building small datasets where we know the true pattern. This module develops
the same workflow twice: first with NumPy arrays and then with PyTorch tensors.

## Course Goals

By the end of this module, students should be able to:

1. generate a random array or tensor with a requested shape;
2. make experiments repeatable with a seed;
3. choose a distribution that matches the kind of quantity being modeled;
4. sample categories, shuffle observations, and make train/test splits;
5. generate features $X$ and targets $y=f(X)+\varepsilon$ for regression;
6. generate classification labels from probabilities; and
7. deliberately add noise, imbalance, outliers, missing values, and distribution
   shift to test a training pipeline.

## Lessons

1. [Shapes, seeds, and uniform random values](./01-shapes-seeds-and-uniform-random-values.md)
2. [Choosing a probability distribution](./02-choosing-a-probability-distribution.md)
3. [Categories, permutations, and random splits](./03-categories-permutations-and-random-splits.md)
4. [Synthetic regression data: $y=f(X)+\varepsilon$](./04-synthetic-regression-data.md)
5. [Synthetic classification and realistic data problems](./05-synthetic-classification-and-data-problems.md)
6. [Practice set](./06-random-generation-practice-set.md)

## NumPy and PyTorch at a Glance

| Goal | NumPy (`rng`) | PyTorch (`generator=g`) |
|---|---|---|
| Uniform on $[0,1)$ | `rng.random((r, c))` | `torch.rand((r, c), generator=g)` |
| Standard normal | `rng.standard_normal((r, c))` | `torch.randn((r, c), generator=g)` |
| Integers in $[a,b)$ | `rng.integers(a, b, size=(r, c))` | `torch.randint(a, b, (r, c), generator=g)` |
| Random order | `rng.permutation(n)` | `torch.randperm(n, generator=g)` |
| Reproducible generator | `np.random.default_rng(seed)` | `torch.Generator().manual_seed(seed)` |

The two libraries use similar ideas but not identical argument names. NumPy
usually calls the output-shape argument `size`; PyTorch creation functions
usually accept the shape as a positional tuple.

## Suggested Pace

- Lessons 1–2: learn the APIs and distribution choices.
- Lesson 3: manipulate rows without breaking the connection between $X$ and $y$.
- Lessons 4–5: build complete fake training datasets and investigate them.
- Lesson 6: complete the tasks without copying earlier code.

## Official References

- [NumPy random sampling](https://numpy.org/doc/stable/reference/random/)
- [NumPy `Generator`](https://numpy.org/doc/stable/reference/random/generator.html)
- [PyTorch random sampling functions](https://docs.pytorch.org/docs/stable/torch.html#random-sampling)
- [PyTorch randomness notes](https://docs.pytorch.org/docs/stable/notes/randomness.html)

