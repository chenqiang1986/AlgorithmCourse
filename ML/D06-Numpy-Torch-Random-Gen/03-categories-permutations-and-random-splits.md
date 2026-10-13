# Lesson 3: Categories, Permutations, and Random Splits
*ML / D06-Numpy-Torch-Random-Gen*

Random generation is not limited to numeric feature values. We also use it to
choose labels, change row order, sample mini-batches, and divide observations
into training and test sets.

## 1. Sample Categories with Chosen Probabilities

Suppose a simulated customer is on a basic, plus, or premium plan with
probabilities $0.60$, $0.30$, and $0.10$.

```python
import numpy as np

rng = np.random.default_rng(42)

plans = np.array(["basic", "plus", "premium"])
probabilities = np.array([0.60, 0.30, 0.10])

sampled_plans = rng.choice(
    plans,
    size=1_000,
    replace=True,
    p=probabilities,
)
```

The probabilities must be nonnegative and sum to $1$.

PyTorch commonly samples category indices rather than strings:

```python
import torch

g = torch.Generator().manual_seed(42)
probabilities = torch.tensor([0.60, 0.30, 0.10])

plan_ids = torch.multinomial(
    probabilities,
    num_samples=1_000,
    replacement=True,
    generator=g,
)

# 0 means basic, 1 means plus, and 2 means premium
```

Integer IDs work naturally with models. Keep a separate mapping when human-
readable labels are needed.

## 2. With Replacement Versus Without Replacement

- **With replacement:** an item can be selected again. This models independent
  draws from a population and is necessary above because 1,000 labels are drawn
  from only three categories.
- **Without replacement:** an item can appear at most once. This is appropriate
  for selecting unique rows or creating a random ordering.

```python
unique_np = rng.choice(100, size=10, replace=False)
unique_torch = torch.randperm(100, generator=g)[:10]
```

## 3. Shuffle $X$ and $y$ Together

If row $i$ of $X$ describes the target in row $i$ of $y$, they must use the
same permutation. In the snippets below, assume the paired arrays `X_np`,
`y_np` and paired tensors `X_torch`, `y_torch` have already been generated.

```python
# NumPy
n = X_np.shape[0]
order = rng.permutation(n)
X_np = X_np[order]
y_np = y_np[order]
```

```python
# PyTorch
n = X_torch.shape[0]
order = torch.randperm(n, generator=g)
X_torch = X_torch[order]
y_torch = y_torch[order]
```

Creating one permutation for `X` and another for `y` destroys the relationship
the model is supposed to learn.

## 4. Make a Train/Test Split

The following split reserves the last 20% of a random ordering for testing.

```python
# NumPy
n = X_np.shape[0]
n_train = int(0.8 * n)
order = rng.permutation(n)

train_idx = order[:n_train]
test_idx = order[n_train:]

X_train_np, y_train_np = X_np[train_idx], y_np[train_idx]
X_test_np, y_test_np = X_np[test_idx], y_np[test_idx]
```

```python
# PyTorch
n = X_torch.shape[0]
n_train = int(0.8 * n)
order = torch.randperm(n, generator=g)

train_idx = order[:n_train]
test_idx = order[n_train:]

X_train_torch, y_train_torch = X_torch[train_idx], y_torch[train_idx]
X_test_torch, y_test_torch = X_torch[test_idx], y_torch[test_idx]
```

For real projects, `sklearn.model_selection.train_test_split` and PyTorch data
utilities provide more features. Writing the split once by hand makes the
indexing rule visible.

## 5. Sample a Mini-Batch

A training step often uses a small random subset of rows.

```python
batch_size = 32

# NumPy, without replacement inside this batch
batch_idx_np = rng.choice(len(X_train_np), size=batch_size, replace=False)
X_batch_np = X_train_np[batch_idx_np]
y_batch_np = y_train_np[batch_idx_np]
```

```python
# PyTorch, without replacement inside this batch
batch_idx_torch = torch.randperm(
    len(X_train_torch), generator=g
)[:batch_size]
X_batch_torch = X_train_torch[batch_idx_torch]
y_batch_torch = y_train_torch[batch_idx_torch]
```

This does not guarantee that every row is seen exactly once per epoch. To get
that behavior, generate one permutation for the epoch and divide it into
consecutive batches.

## 6. Keep Test Data Untouched

Operations learned from data belong to the training set only. For example,
compute normalization statistics from `X_train`, then reuse them on `X_test`:

```python
mean = X_train_np.mean(axis=0, keepdims=True)
std = X_train_np.std(axis=0, keepdims=True)
std = np.where(std == 0, 1.0, std)

X_train_scaled = (X_train_np - mean) / std
X_test_scaled = (X_test_np - mean) / std
```

Computing separate test-set statistics leaks information about the test set and
makes the evaluation less honest.

## 7. A Useful Pairing Test

When creating a teaching dataset, temporarily make the row relationship obvious:

```python
X = np.arange(10).reshape(5, 2)
y = X.sum(axis=1)

order = rng.permutation(len(X))
X = X[order]
y = y[order]

assert np.array_equal(y, X.sum(axis=1))
```

This small assertion catches a surprisingly common shuffling bug.

## 8. Class Practice

1. Generate 500 class IDs with probabilities `[0.7, 0.2, 0.1]`. Count each ID.
2. Create an array containing integers `0` through `19`, then shuffle it without
   losing or duplicating any values.
3. Create paired `X` and `y`, shuffle them together, and assert that their rule
   still holds.
4. Split 1,003 rows into approximately 75% training and 25% test data. Report
   the exact sizes.
5. Divide one random permutation into batches of size 64. What happens to the
   final batch?

## 9. Key Takeaways

- Weighted category sampling requires valid probabilities that sum to $1$.
- Use replacement for repeated population draws and no replacement for unique
  row selection.
- Apply exactly the same row indices to $X$ and $y$.
- Split before learning preprocessing statistics.
- One permutation per epoch gives each training row one visit in a shuffled order.

