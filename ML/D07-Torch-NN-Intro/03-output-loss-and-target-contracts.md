# Lesson 3: Choose Outputs and Loss Functions
*ML / D07-Torch-NN-Intro*

A loss function converts model errors into one scalar that training can
minimize. In PyTorch, each loss has a precise contract: expected output shape,
target shape, target dtype, and whether the model should return raw logits or
transformed probabilities.

## 1. The Loss Must Be Scalar

If a batch contains $n$ examples, each example may have its own loss. Training
normally minimizes their mean:

$$
L=\frac{1}{n}\sum_{i=1}^{n}\ell_i.
$$

PyTorch's common loss modules use `reduction="mean"` by default, so
`loss.backward()` begins from one scalar.

## 2. Regression: `nn.MSELoss`

For one continuous target, let both prediction and target have shape `(n, 1)`.

$$
\operatorname{MSE}=\frac{1}{n}\sum_{i=1}^{n}(\hat y_i-y_i)^2.
$$

```python
import torch
from torch import nn

model = nn.Linear(3, 1)
loss_fn = nn.MSELoss()

X = torch.randn(8, 3)
y = torch.randn(8, 1)

predictions = model(X)
loss = loss_fn(predictions, y)

print(predictions.shape)  # torch.Size([8, 1])
print(y.shape)            # torch.Size([8, 1])
print(loss.shape)         # torch.Size([]), a scalar tensor
```

Although PyTorch may broadcast mismatched shapes, a prediction of `(n, 1)` and
a target of `(n,)` is not the intended pairing. Use the same shape for both.

```python
y = y.reshape(-1, 1)
```

## 3. Binary Classification: `nn.BCEWithLogitsLoss`

For binary classification, return one raw logit $z_i$ per example. The sigmoid
probability is

$$
p_i=\sigma(z_i)=\frac{1}{1+e^{-z_i}}.
$$

`nn.BCEWithLogitsLoss` combines sigmoid and binary cross-entropy in a more
numerically stable calculation.

```python
model = nn.Linear(3, 1)          # one raw logit per row
loss_fn = nn.BCEWithLogitsLoss()

X = torch.randn(8, 3)
y = torch.tensor([[0.0], [1.0], [1.0], [0.0],
                  [1.0], [0.0], [0.0], [1.0]])

logits = model(X)
loss = loss_fn(logits, y)
```

Do not add `nn.Sigmoid()` to the model before this loss. Apply sigmoid only when
you want probabilities for interpretation:

```python
with torch.inference_mode():
    probabilities = torch.sigmoid(logits)
    predicted_classes = (probabilities >= 0.5).to(torch.int64)
```

Binary targets are floating-point values with the same shape as the logits.

## 4. Multiclass Classification: `nn.CrossEntropyLoss`

For $K$ mutually exclusive classes, return $K$ raw logits per example. The
target contains one integer class index per example.

```python
n_features = 5
n_classes = 3

model = nn.Linear(n_features, n_classes)
loss_fn = nn.CrossEntropyLoss()

X = torch.randn(8, n_features)
y = torch.tensor([0, 2, 1, 0, 1, 2, 2, 1], dtype=torch.long)

logits = model(X)       # shape (8, 3)
loss = loss_fn(logits, y)  # y has shape (8,)
```

`nn.CrossEntropyLoss` combines log-softmax and negative log-likelihood. Do not
put `Softmax` in the model before this loss.

Convert logits to predictions after training:

```python
probabilities = torch.softmax(logits, dim=1)
predicted_classes = logits.argmax(dim=1)
```

`argmax` gives the same class before or after softmax because softmax preserves
the ordering of logits.

## 5. The Three Main Contracts

| Task | Final output | Target | Target dtype | Loss |
|---|---|---|---|---|
| One-value regression | `(n, 1)` | `(n, 1)` | floating point | `nn.MSELoss()` |
| Binary classification | `(n, 1)` logits | `(n, 1)` zeros/ones | floating point | `nn.BCEWithLogitsLoss()` |
| $K$-class classification | `(n, K)` logits | `(n,)` class IDs | `torch.long` | `nn.CrossEntropyLoss()` |

Write this table from memory before building a new model. It resolves many
apparently mysterious loss errors.

## 6. Why Logits Are Useful

A logit is an unconstrained score. It can be any real number. Combined loss
functions work directly with logits because they can avoid unstable intermediate
computations such as taking the logarithm of a probability rounded to zero.

Keep a clean boundary:

- training: model returns logits, loss consumes logits;
- reporting: convert detached logits to probabilities or class predictions.

## 7. A Shape Guard

For regression and binary classification, assert equal shapes before computing
the loss:

```python
output = model(X)
assert output.shape == y.shape, (output.shape, y.shape)
loss = loss_fn(output, y)
```

For multiclass classification:

```python
logits = model(X)
assert logits.ndim == 2
assert y.ndim == 1
assert logits.shape[0] == y.shape[0]
assert y.dtype == torch.long
loss = loss_fn(logits, y)
```

These checks make the intended contract executable.

## 8. Class Practice 1: Select a Contract

For each task, choose the final layer and loss.

1. Predict tomorrow's temperature.
2. Predict whether a customer will churn.
3. Predict which one of ten digits appears in an image.

<details>
<summary>Solution</summary>

1. Use one output, such as `nn.Linear(hidden, 1)`, with `nn.MSELoss()`.
2. Use one raw logit, `nn.Linear(hidden, 1)`, with
   `nn.BCEWithLogitsLoss()`.
3. Use ten raw logits, `nn.Linear(hidden, 10)`, with
   `nn.CrossEntropyLoss()`.

$\square$

</details>

## 9. Class Practice 2: Find Three Bugs

The task has four mutually exclusive classes. Find three problems.

```python
model = nn.Sequential(
    nn.Linear(6, 12),
    nn.ReLU(),
    nn.Linear(12, 4),
    nn.Softmax(dim=1),
)

y = torch.tensor([[0.0], [2.0], [1.0]])
loss_fn = nn.CrossEntropyLoss()
loss = loss_fn(model(torch.randn(3, 6)), y)
```

<details>
<summary>Solution</summary>

Remove `nn.Softmax` because `CrossEntropyLoss` expects raw logits. The target
must be one-dimensional, with shape `(3,)`, and it must have dtype
`torch.long`:

```python
y = torch.tensor([0, 2, 1], dtype=torch.long)
```

$\square$

</details>

## 10. Key Takeaways

- A loss function defines a contract between outputs and targets.
- Match prediction and target shapes exactly for regression and binary
  classification.
- Use floating-point targets for `BCEWithLogitsLoss` and integer class IDs for
  `CrossEntropyLoss`.
- Return raw logits during classification training.
- Use sigmoid or softmax when interpreting predictions, not before a combined
  logit-based loss.

Next, we will use automatic differentiation and an optimizer to change the
model's parameters.

