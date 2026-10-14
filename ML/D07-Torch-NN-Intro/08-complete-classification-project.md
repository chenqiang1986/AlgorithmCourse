# Lesson 8: Complete Classification Project and Debugging Guide
*ML / D07-Torch-NN-Intro*

This lesson trains a network to learn a nonlinear binary pattern. It completes
the workflow by evaluating logits as class decisions, saving and restoring a
checkpoint, and diagnosing common training failures.

The complete runnable version is
[`practice_ws/train_xor_classifier.py`](./practice_ws/train_xor_classifier.py).

## 1. A Noisy XOR Problem

Generate two features. A point belongs to class $1$ when its coordinates have
the same sign and class $0$ otherwise:

$$
y=\begin{cases}
1,&x_1x_2>0,\\
0,&x_1x_2\le0.
\end{cases}
$$

Then flip a small random fraction of labels. The four quadrants create a
nonlinear classification boundary that one linear classifier cannot solve.

```python
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

torch.manual_seed(42)
g = torch.Generator().manual_seed(42)

n_samples = 2_000
X = -2.0 + 4.0 * torch.rand((n_samples, 2), generator=g)
y = (X[:, 0] * X[:, 1] > 0).to(torch.float32).reshape(-1, 1)

flip_mask = torch.rand((n_samples, 1), generator=g) < 0.05
y = torch.where(flip_mask, 1.0 - y, y)
```

The target has floating-point dtype and shape `(n, 1)`, matching the contract
for `BCEWithLogitsLoss`.

## 2. Split and Load the Data

```python
indices = torch.randperm(n_samples, generator=g)
n_train = int(0.70 * n_samples)
n_val = int(0.15 * n_samples)

train_idx = indices[:n_train]
val_idx = indices[n_train:n_train + n_val]
test_idx = indices[n_train + n_val:]

train_loader = DataLoader(
    TensorDataset(X[train_idx], y[train_idx]),
    batch_size=64,
    shuffle=True,
)
val_loader = DataLoader(
    TensorDataset(X[val_idx], y[val_idx]),
    batch_size=128,
    shuffle=False,
)
test_loader = DataLoader(
    TensorDataset(X[test_idx], y[test_idx]),
    batch_size=128,
    shuffle=False,
)
```

The random split mixes all four quadrants into each subset.

## 3. Build a Binary Classifier

```python
model = nn.Sequential(
    nn.Linear(2, 16),
    nn.ReLU(),
    nn.Linear(16, 16),
    nn.ReLU(),
    nn.Linear(16, 1),
)

loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
```

The model returns one raw logit. There is no sigmoid layer because the loss
already combines sigmoid and binary cross-entropy.

## 4. Evaluate Loss and Accuracy

```python
def evaluate_binary(model, loader, loss_fn, device):
    model.eval()
    loss_sum = 0.0
    correct = 0
    n_examples = 0

    with torch.inference_mode():
        for X_batch, y_batch in loader:
            X_batch = X_batch.to(device)
            y_batch = y_batch.to(device)

            logits = model(X_batch)
            loss = loss_fn(logits, y_batch)
            predictions = (logits >= 0.0).to(y_batch.dtype)

            batch_size = X_batch.shape[0]
            loss_sum += loss.item() * batch_size
            correct += (predictions == y_batch).sum().item()
            n_examples += batch_size

    return loss_sum / n_examples, correct / n_examples
```

A logit threshold of $0$ corresponds exactly to a sigmoid probability threshold
of $0.5$.

## 5. Train and Keep the Best Validation State

```python
def choose_device():
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


device = choose_device()
model = model.to(device)

best_val_loss = float("inf")
best_state = None

for epoch in range(1, 101):
    model.train()

    for X_batch, y_batch in train_loader:
        X_batch = X_batch.to(device)
        y_batch = y_batch.to(device)

        optimizer.zero_grad()
        logits = model(X_batch)
        loss = loss_fn(logits, y_batch)
        loss.backward()
        optimizer.step()

    val_loss, val_accuracy = evaluate_binary(
        model, val_loader, loss_fn, device
    )

    if val_loss < best_val_loss:
        best_val_loss = val_loss
        best_state = {
            name: tensor.detach().cpu().clone()
            for name, tensor in model.state_dict().items()
        }

    if epoch == 1 or epoch % 20 == 0:
        print(
            f"epoch={epoch:3d} "
            f"val_loss={val_loss:.4f} "
            f"val_accuracy={val_accuracy:.3f}"
        )
```

With $5\%$ label flips, perfect accuracy is neither expected nor desirable as a
training target. The model should learn the quadrant pattern rather than
memorize every corrupted label.

## 6. Test the Selected Model

```python
model.load_state_dict(best_state)
model = model.to(device)

test_loss, test_accuracy = evaluate_binary(
    model, test_loader, loss_fn, device
)

print(f"test loss:     {test_loss:.4f}")
print(f"test accuracy: {test_accuracy:.3f}")
```

The test result estimates how the selected training procedure behaves on new
points from the same data-generating process.

## 7. Turn One Logit into a Reportable Prediction

```python
new_point = torch.tensor([[1.2, -0.7]], device=device)

model.eval()
with torch.inference_mode():
    logit = model(new_point)
    probability = torch.sigmoid(logit)
    predicted_class = (probability >= 0.5).to(torch.int64)

print(logit.item())
print(probability.item())
print(predicted_class.item())
```

The raw logit is best for the loss. The probability is easier to communicate.
The class is a decision made by applying a threshold.

## 8. Save and Restore the Learned State

Save parameter values rather than the entire Python model object:

```python
checkpoint_path = "xor_classifier_state.pt"
torch.save(model.state_dict(), checkpoint_path)
```

To restore it, recreate the same architecture and load the state dictionary:

```python
restored_model = nn.Sequential(
    nn.Linear(2, 16),
    nn.ReLU(),
    nn.Linear(16, 16),
    nn.ReLU(),
    nn.Linear(16, 1),
)

state = torch.load(
    checkpoint_path,
    map_location="cpu",
    weights_only=True,
)
restored_model.load_state_dict(state)
restored_model.eval()
```

`state_dict` does not store the class definition or architecture. The code that
constructs the model must remain available and must match the saved state.

## 9. Debugging Checklist

### 9.1 Shape or matrix-multiplication error

Print:

```python
print(X_batch.shape, y_batch.shape)
print(model)
```

Check the final feature dimension against the first layer's `in_features`, then
trace every layer's output width.

### 9.2 Loss complains about dtype

Check the task contract:

- binary targets: floating point, same shape as logits;
- multiclass targets: `torch.long`, shape `(n,)`;
- regression targets: floating point, same shape as predictions.

### 9.3 Device mismatch

```python
print(next(model.parameters()).device)
print(X_batch.device, y_batch.device)
```

All tensors participating in one operation must be on the same device.

### 9.4 Loss never changes

Confirm that the loop calls both `loss.backward()` and `optimizer.step()`, and
that the optimizer was created from `model.parameters()`.

### 9.5 Loss becomes `nan`

Check that inputs and targets are finite, then reduce the learning rate:

```python
assert torch.isfinite(X_batch).all()
assert torch.isfinite(y_batch).all()
```

### 9.6 Training is good but validation is poor

This is evidence of overfitting or a train/validation distribution mismatch.
Try a smaller model, more data, stronger regularization, or a closer inspection
of how the split was produced.

### 9.7 Every prediction is the same class

Inspect class balance, several logits, and the target encoding. Accuracy may
look deceptively good on an imbalanced dataset even when the model learned only
the majority class.

## 10. Class Practice 1: Remove the Hidden Layers

Replace the network with `nn.Linear(2, 1)`. Train and compare its validation
accuracy to the multilayer model. Explain the result geometrically.

<details>
<summary>Solution</summary>

One linear logit produces one straight decision boundary. XOR assigns opposite
quadrants to the same class, so no single line separates the classes. Hidden
layers and nonlinear activations can build a piecewise nonlinear boundary and
should perform substantially better.

$\square$

</details>

## 11. Class Practice 2: Change the Decision Threshold

Change the probability threshold from $0.5$ to $0.8$. What should happen to the
number of predicted positives? Which metric would usually rise, and which would
usually fall?

<details>
<summary>Solution</summary>

Fewer examples will be predicted positive. Precision will usually rise because
the remaining positive decisions require stronger evidence, while recall will
usually fall because more true positives are rejected. The exact result must be
measured on held-out data.

$\square$

</details>

## 12. Real Practice Project: Telecom Customer Churn

Return to the churn problem from
[D03-ScikitLearn-LinearCategoryIdentification](../D03-ScikitLearn-LinearCategoryIdentification/README.md).
Use the existing
[`WA_Fn-UseC_-Telco-Customer-Churn.csv`](../D03-ScikitLearn-LinearCategoryIdentification/project_henry/WA_Fn-UseC_-Telco-Customer-Churn.csv)
data to compare a PyTorch neural network with the earlier logistic-regression
baseline.

### 12.1 Clean and split the raw table

```python
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv(
    "ML/D03-ScikitLearn-LinearCategoryIdentification/"
    "project_henry/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.drop(columns="customerID")

train_val_df, test_df = train_test_split(
    df,
    test_size=0.20,
    random_state=5,
    stratify=df["Churn"],
)

train_df, val_df = train_test_split(
    train_val_df,
    test_size=0.25,
    random_state=16,
    stratify=train_val_df["Churn"],
)
```

This produces a $60\%/20\%/20\%$ train/validation/test split while preserving
approximately the same churn rate in each subset.

### 12.2 Fit preprocessing on training data only

```python
numeric_columns = ["tenure", "MonthlyCharges", "TotalCharges"]
categorical_columns = [
    "gender", "SeniorCitizen", "Partner", "Dependents",
    "PhoneService", "MultipleLines", "InternetService",
    "OnlineSecurity", "OnlineBackup", "DeviceProtection",
    "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
    "PaperlessBilling", "PaymentMethod",
]
```

Build a `ColumnTransformer`: median-impute and standardize numeric columns;
most-frequent-impute and one-hot encode categorical columns using
`OneHotEncoder(handle_unknown="ignore", sparse_output=False)`.

Call `fit_transform` only on the training features. Call `transform` on
validation and test features. Convert the resulting arrays to `float32` tensors.

```python
y_train = torch.from_numpy(
    train_df["Churn"]
    .map({"No": 0.0, "Yes": 1.0})
    .to_numpy(dtype="float32")
).reshape(-1, 1)
```

Apply the same mapping to validation and test targets.

### 12.3 Required Comparison: Minimize Retention Cost

Accuracy treats every mistake equally, but these two churn mistakes have
different financial consequences. For this exercise, define the cost for
customer $i$ as

$$
C_i=
\begin{cases}
M_i,&y_i=1\text{ and }\widehat y_i=0,\\
20,&y_i=0\text{ and }\widehat y_i=1,\\
0,&\text{otherwise},
\end{cases}
$$

where $M_i$ is the customer's `MonthlyCharges`, $y_i=1$ means the customer
actually churned, and $\widehat y_i=1$ means the model predicted churn. Total
business loss is $C_{\mathrm{total}}=\sum_i C_i$.

Materialize that objective in code:

```python
import numpy as np


def retention_cost(frame, y_true, y_pred):
    actual = np.asarray(y_true).reshape(-1).astype(int)
    predicted = np.asarray(y_pred).reshape(-1).astype(int)
    monthly_charge = frame["MonthlyCharges"].to_numpy(dtype=float)

    false_negative = (actual == 1) & (predicted == 0)
    false_positive = (actual == 0) & (predicted == 1)

    missed_churn_loss = monthly_charge[false_negative].sum()
    unnecessary_incentive_loss = 20.0 * false_positive.sum()

    return {
        "missed_churn_loss": float(missed_churn_loss),
        "unnecessary_incentive_loss": float(unnecessary_incentive_loss),
        "total_cost": float(missed_churn_loss + unnecessary_incentive_loss),
    }
```

The rows in `frame`, `y_true`, and `y_pred` must remain in the same order.

Train a logistic-regression baseline and at least one PyTorch neural network on
exactly the same training rows and preprocessing. You decide how to minimize
validation cost. Possible experiments include model architecture, regularization,
sampling, sample or class weights, the training loss, and the rule that converts
probabilities into decisions. None of these choices is required in advance.

Use validation cost to select the complete strategy. Freeze every choice before
evaluating the test set; never tune against test cost. Report:

| Model | Chosen strategy | Validation total cost | Test missed-churn loss | Test unnecessary-incentive loss | Test total cost |
|---|---|---:|---:|---:|---:|
| Logistic-regression baseline | | | | | |
| Selected PyTorch network | | | | | |

Also report the confusion matrix, precision, recall, and $F_1$ as diagnostic
information, but rank the models by total business cost.

### 12.4 Investigation questions

1. Which modeling or decision choices reduced validation cost most?
2. Which contributes more to total cost: missed churn or unnecessary incentives?
3. Does the model treat high-charge churners differently from low-charge churners?
4. Does the model with the best $F_1$ also have the lowest business cost?
5. Is the cost improvement stable and large enough to justify the network?

## 13. Final Mental Model

```text
define task and cost -> split -> fit preprocessing on training data
    -> build loaders and nn.Module -> train on mini-batches
    -> select the complete strategy using validation cost
    -> test once -> save preprocessing and state_dict
```

## 14. Key Takeaways

- Binary models should return one raw logit per example during training.
- Convert logits to probabilities and decisions only when interpreting output.
- Validation data selects a model; test data estimates the selected model.
- Save and restore `state_dict` values with a matching architecture.
- Debug in a fixed order: shapes, dtypes, devices, finite values, gradients,
  updates, and only then architecture or hyperparameters.
- A model is trustworthy only when the complete data and evaluation workflow is
  trustworthy.
- A neural network should be compared with a simpler baseline on identical
  rows, preprocessing, business-cost rules, and held-out evaluation protocol.

