# Lesson 5: Synthetic Classification and Realistic Data Problems
*ML / D06-Numpy-Torch-Random-Gen*

For regression, a continuous target can be generated as $f(X)+\varepsilon$.
For classification, we usually turn a score into a probability and then draw a
random label from that probability.

Synthetic data can also imitate the unpleasant parts of real datasets: class
imbalance, missing values, outliers, mislabeled rows, and distribution shift.

## 1. Binary Labels from a Logistic Model

Begin with a linear score:

$$
z=Xw+b.
$$

Turn the score into a probability with the sigmoid function:

$$
p(y=1\mid X)=\sigma(z)=\frac{1}{1+e^{-z}}.
$$

Finally sample

$$
y\mid X\sim\operatorname{Bernoulli}(p).
$$

That last step is the classification version of adding random variation. Rows
with the same features can receive different labels, but rows with larger
scores are more likely to receive class `1`.

## 2. NumPy Implementation

```python
import numpy as np

rng = np.random.default_rng(42)

n_samples = 2_000
X = rng.normal(size=(n_samples, 2))
true_w = np.array([1.8, -1.2])
true_b = -0.4

logits = X @ true_w + true_b
probabilities = 1.0 / (1.0 + np.exp(-logits))
y = rng.binomial(n=1, p=probabilities)

assert X.shape == (2_000, 2)
assert y.shape == (2_000,)
assert set(np.unique(y)).issubset({0, 1})
```

Avoid `y = (probabilities >= 0.5).astype(int)` when the goal is noisy labels.
That threshold makes the classes perfectly deterministic once $X$ is known.

## 3. PyTorch Implementation

```python
import torch

g = torch.Generator().manual_seed(42)

n_samples = 2_000
X = torch.randn((n_samples, 2), generator=g)
true_w = torch.tensor([1.8, -1.2])
true_b = -0.4

logits = X @ true_w + true_b
probabilities = torch.sigmoid(logits)
y = torch.bernoulli(probabilities, generator=g)

assert X.shape == (2_000, 2)
assert y.shape == (2_000,)
assert torch.all((y == 0) | (y == 1))
```

PyTorch stores these Bernoulli samples as floating-point values. Many PyTorch
loss functions intentionally expect float targets for binary classification.

## 4. Control Class Balance with the Intercept

The intercept shifts every logit. A more negative intercept generally creates
fewer positive labels; a more positive intercept creates more.

```python
rng = np.random.default_rng(42)
X_np = rng.normal(size=(2_000, 2))
true_w_np = np.array([1.8, -1.2])

for bias in [-3.0, 0.0, 3.0]:
    logits = X_np @ true_w_np + bias
    probabilities = 1.0 / (1.0 + np.exp(-logits))
    labels = rng.binomial(1, probabilities)
    print(bias, labels.mean())
```

Because the features also affect the probabilities, an intercept does not
directly equal the desired positive rate. Measure the generated rate and tune
the intercept if a particular level of imbalance is required.

## 5. Multiclass Labels

For $K$ classes, compute $K$ logits per row, turn them into probabilities with
softmax, and draw one class ID per row.

```python
# PyTorch
g = torch.Generator().manual_seed(8)
n_samples, n_features, n_classes = 1_000, 4, 3

X = torch.randn((n_samples, n_features), generator=g)
W = torch.randn((n_features, n_classes), generator=g)
b = torch.tensor([0.5, 0.0, -0.5])

logits = X @ W + b
probabilities = torch.softmax(logits, dim=1)
y = torch.multinomial(
    probabilities,
    num_samples=1,
    replacement=True,
    generator=g,
).squeeze(1)

assert probabilities.shape == (1_000, 3)
assert torch.allclose(probabilities.sum(dim=1), torch.ones(1_000))
assert y.shape == (1_000,)
```

For NumPy, sample each row using its own probability vector:

```python
rng = np.random.default_rng(8)
n_samples, n_features, n_classes = 1_000, 4, 3

X_np = rng.standard_normal((n_samples, n_features))
W_np = rng.standard_normal((n_features, n_classes))
b_np = np.array([0.5, 0.0, -0.5])

logits = X_np @ W_np + b_np
shifted = logits - logits.max(axis=1, keepdims=True)
exp_logits = np.exp(shifted)
probabilities = exp_logits / exp_logits.sum(axis=1, keepdims=True)

y = np.array([
    rng.choice(n_classes, p=row_probabilities)
    for row_probabilities in probabilities
])
```

Subtracting the row maximum before exponentiating makes softmax numerically
stable without changing its result.

## 6. Add Label Noise

Real labels can be wrong. Flip a chosen fraction of binary training labels:

```python
# Assume y_train is a NumPy array created by a clean train/test split.
flip_rate = 0.10
flip_mask = rng.random(len(y_train)) < flip_rate
y_train_noisy = y_train.copy()
y_train_noisy[flip_mask] = 1 - y_train_noisy[flip_mask]
```

Keep the original label array so the corruption can be measured. Unless the
experiment specifically studies noisy evaluation, corrupt the training labels
and leave validation/test labels clean.

## 7. Add Missing Values and Outliers

```python
# Assume X_train is a NumPy array created by a clean train/test split.
X_train_messy = X_train.copy()

# About 5% of individual cells become missing.
missing_mask = rng.random(X_train_messy.shape) < 0.05
X_train_messy[missing_mask] = np.nan

# About 2% of rows get a large disturbance in the first feature.
outlier_rows = rng.random(len(X_train_messy)) < 0.02
X_train_messy[outlier_rows, 0] += rng.normal(
    loc=0.0,
    scale=15.0,
    size=outlier_rows.sum(),
)
```

These are two different mechanisms:

- missingness removes information;
- outliers retain a value but make it unusually extreme.

Generate masks explicitly so you can count which rows were affected.

## 8. Create Correlated Features

Independent standard-normal columns are convenient but often unrealistic.
One simple way to create correlated features is to share a latent variable:

```python
n = 2_000
shared = rng.standard_normal(n)

x1 = shared + 0.3 * rng.standard_normal(n)
x2 = 0.8 * shared + 0.4 * rng.standard_normal(n)
x3 = rng.standard_normal(n)

X = np.column_stack([x1, x2, x3])
print(np.corrcoef(X, rowvar=False))
```

Here `x1` and `x2` tend to move together, while `x3` is independent of their
shared source.

## 9. Simulate Distribution Shift

Training and test data are sometimes drawn from different populations.

```python
rng_train = np.random.default_rng(100)
rng_test = np.random.default_rng(200)

X_train = rng_train.normal(loc=0.0, scale=1.0, size=(2_000, 3))
X_test = rng_test.normal(loc=1.0, scale=1.4, size=(500, 3))
```

This is a feature-distribution shift: test values have a different mean and
spread. To isolate the effect, use the same target rule for both sets.

Do not accidentally create shift by using unrelated target parameters for
training and test data. That is a different and usually harder experiment.

## 10. Keep an Experiment Honest

When manipulating fake data:

1. Generate a clean dataset and save the true rule.
2. Split into train, validation, and test sets.
3. Apply intended corruption to the training set only unless the research
   question says otherwise.
4. Preserve clean copies and the random seed.
5. Record the actual corruption rates and class proportions.
6. Evaluate on data that the model and preprocessing steps did not inspect.

Synthetic data is evidence that code can recover a known pattern. It is not, by
itself, evidence that the same model will work on a real population.

## 11. Class Practice

1. Generate binary labels from two features using a sigmoid and Bernoulli draw.
2. Change only the intercept and compare positive-class proportions.
3. Add 15% label noise to training data while keeping test labels clean.
4. Make two correlated features and verify their sample correlation.
5. Create a shifted test set and compare feature means between train and test.
6. Train a familiar classifier on clean and corrupted versions of the same
   synthetic dataset. Which corruption hurts it most?

## 12. Key Takeaways

- Classification randomness enters through a Bernoulli or categorical draw.
- A probability is not itself a label.
- Intercepts help control class balance, but the realized balance must be checked.
- Explicit masks make missing values, outliers, and label errors auditable.
- Change one property at a time when comparing experiments.
- Preserve an untouched evaluation set.

