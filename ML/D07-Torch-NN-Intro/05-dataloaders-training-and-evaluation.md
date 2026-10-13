# Lesson 5: Load CSV Data, Train with Mini-Batches, and Evaluate
*ML / D07-Torch-NN-Intro*

Real training data often begins in a CSV file rather than a tensor. This lesson
loads a CSV into a pandas DataFrame, prepares its columns, converts the values
to PyTorch tensors, and then uses `Dataset`, `DataLoader`, and separate training
and evaluation functions to create a reliable workflow.

## 1. Epochs and Mini-Batches

An **epoch** is one pass through the training set. A **mini-batch** is the group
of examples used for one parameter update.

With $N=1{,}000$ training examples and a batch size of $64$, most epochs contain
$16$ batches: $15$ full batches and one smaller final batch.

Mini-batches offer a useful compromise:

- they require less memory than the full dataset;
- they produce more updates per epoch;
- each update uses more evidence than a single example.

## 2. Load a CSV into a pandas DataFrame

The sample file
[`practice_ws/student_scores.csv`](./practice_ws/student_scores.csv) contains
four possible input columns and one regression target:

```text
hours_studied,attendance_rate,prior_score,study_method,exam_score
2.0,0.72,61,solo,64
5.5,0.91,78,group,84
```

Load the complete file with `pd.read_csv`:

```python
from pathlib import Path

import pandas as pd

csv_path = Path(
    "ML/D07-Torch-NN-Intro/practice_ws/student_scores.csv"
)
df = pd.read_csv(csv_path)

print(df.head())
print(df.shape)
print(df.dtypes)
```

Each DataFrame row represents one observation. Columns may play different
roles:

- feature columns are inputs to the model;
- the target column is the value the model should learn to predict;
- identifier columns describe rows but are usually not useful inputs.

Never convert a newly loaded table immediately. Inspect its column names,
dtypes, missing values, and a few rows first.

## 3. Select and Prepare the Columns

Separate features from the target by name:

```python
numeric_features = [
    "hours_studied",
    "attendance_rate",
    "prior_score",
]
categorical_features = ["study_method"]
target_column = "exam_score"

required_columns = numeric_features + categorical_features + [target_column]

missing_columns = set(required_columns) - set(df.columns)
if missing_columns:
    raise ValueError(f"Missing columns: {sorted(missing_columns)}")

if df[required_columns].isna().any().any():
    raise ValueError("Clean or impute missing values before conversion.")
```

A tensor must contain one numerical dtype. Text categories such as `"solo"`
and `"group"` therefore need numerical encoding. For this small example,
one-hot encoding creates one indicator column per category:

```python
feature_frame = pd.get_dummies(
    df[numeric_features + categorical_features],
    columns=categorical_features,
    dtype="float32",
)

target_frame = df[[target_column]]

print(feature_frame.head())
print(feature_frame.columns.tolist())
```

The double brackets in `df[[target_column]]` preserve a two-dimensional target
table. That will produce a tensor with shape `(n, 1)`, matching a regression
model with one output.

In a real project, learn data-dependent cleaning rules from the training set
only. For example, split before computing a median used to fill missing values.

## 4. Convert the DataFrame to PyTorch Tensors

Convert pandas data to a NumPy array with the intended dtype, then share that
array with a PyTorch tensor:

```python
import torch
from torch import nn

X_array = feature_frame.to_numpy(dtype="float32")
y_array = target_frame.to_numpy(dtype="float32")

X = torch.from_numpy(X_array)
y = torch.from_numpy(y_array)

print(X.shape, X.dtype)  # torch.Size([16, 5]) torch.float32
print(y.shape, y.dtype)  # torch.Size([16, 1]) torch.float32

assert X.ndim == 2
assert y.ndim == 2
assert X.shape[0] == y.shape[0]
assert torch.isfinite(X).all()
assert torch.isfinite(y).all()
```

`torch.from_numpy` avoids an unnecessary copy when possible. The tensor and
NumPy array may share memory, so changing one can change the other. Use
`torch.tensor(X_array)` when an independent copy is required.

Do not rely on pandas to choose a training dtype implicitly. pandas numerical
columns are often `float64`, while PyTorch layers use `float32` parameters by
default. Explicit `float32` conversion prevents a dtype mismatch during the
forward pass.

### Classification targets use a different conversion

The correct target conversion depends on the loss contract from
[Lesson 3](./03-output-loss-and-target-contracts.md):

```python
# Binary classification with BCEWithLogitsLoss:
y_binary = torch.from_numpy(
    df[["binary_target"]].to_numpy(dtype="float32")
)  # shape (n, 1), floating point

# Multiclass classification with CrossEntropyLoss:
y_multiclass = torch.from_numpy(
    df["class_id"].to_numpy(dtype="int64")
)  # shape (n,), torch.int64 / torch.long
```

The sample CSV is a regression dataset, so the main example uses `y`, not the
illustrative classification columns above.

## 5. Pair Tensors with `TensorDataset`

```python
from torch.utils.data import DataLoader, TensorDataset

dataset = TensorDataset(X, y)

X_first, y_first = dataset[0]
print(X_first.shape)  # torch.Size([5])
print(y_first.shape)  # torch.Size([1])
print(len(dataset))        # 16
```

Every tensor passed to `TensorDataset` must have the same first dimension. Row
$i$ from every tensor is treated as one sample.

## 6. Wrap the Dataset with `DataLoader`

```python
train_loader = DataLoader(
    dataset,
    batch_size=4,
    shuffle=True,
)

for X_batch, y_batch in train_loader:
    print(X_batch.shape, y_batch.shape)
    break
```

Use `shuffle=True` for training so consecutive epochs use different batch
groupings. Use `shuffle=False` for validation and testing because order is not
needed for learning.

## 7. Split Before Building Loaders

The validation set must not influence parameter updates.

```python
g = torch.Generator().manual_seed(42)

permutation = torch.randperm(len(X), generator=g)
n_train = int(0.8 * len(X))
train_indices = permutation[:n_train]
val_indices = permutation[n_train:]

train_dataset = TensorDataset(X[train_indices], y[train_indices])
val_dataset = TensorDataset(X[val_indices], y[val_indices])

train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=8, shuffle=False)
```

In a real project, reserve a final test set as well. Use validation results to
make modeling choices and inspect the test set only after those choices are
finished.

## 8. A Reusable Training Function

```python
def train_one_epoch(model, loader, loss_fn, optimizer, device):
    model.train()
    total_loss = 0.0
    total_examples = 0

    for X_batch, y_batch in loader:
        X_batch = X_batch.to(device)
        y_batch = y_batch.to(device)

        optimizer.zero_grad()
        output = model(X_batch)
        loss = loss_fn(output, y_batch)
        loss.backward()
        optimizer.step()

        batch_size = X_batch.shape[0]
        total_loss += loss.item() * batch_size
        total_examples += batch_size

    return total_loss / total_examples
```

`model.train()` enables training behavior. This matters for modules such as
dropout and batch normalization, even though a simple linear/ReLU network may
behave identically in both modes.

The function weights each batch's mean loss by its batch size. Averaging batch
means directly would give the smaller final batch the same influence as a full
batch.

## 9. A Reusable Evaluation Function

```python
def evaluate(model, loader, loss_fn, device):
    model.eval()
    total_loss = 0.0
    total_examples = 0

    with torch.inference_mode():
        for X_batch, y_batch in loader:
            X_batch = X_batch.to(device)
            y_batch = y_batch.to(device)

            output = model(X_batch)
            loss = loss_fn(output, y_batch)

            batch_size = X_batch.shape[0]
            total_loss += loss.item() * batch_size
            total_examples += batch_size

    return total_loss / total_examples
```

Evaluation makes three deliberate changes:

1. `model.eval()` enables evaluation behavior.
2. `torch.inference_mode()` disables autograd recording and related overhead.
3. There is no `backward()` or `optimizer.step()`.

`torch.inference_mode()` does not call `model.eval()` for you. Both lines have
different responsibilities.

## 10. Choose a Device Once

```python
def choose_device():
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


device = choose_device()
model = model.to(device)
```

Move each input and target batch to the same device inside the loop. A model on
an accelerator cannot operate on a CPU input tensor.

Keep the source dataset on CPU for this introductory workflow; the loader sends
one batch at a time to the selected device.

## 11. The Epoch Loop

```python
n_epochs = 50

for epoch in range(1, n_epochs + 1):
    train_loss = train_one_epoch(
        model, train_loader, loss_fn, optimizer, device
    )
    val_loss = evaluate(model, val_loader, loss_fn, device)

    if epoch == 1 or epoch % 10 == 0:
        print(
            f"epoch={epoch:3d} "
            f"train_loss={train_loss:.4f} "
            f"val_loss={val_loss:.4f}"
        )
```

Training loss measures fit to data that produced updates. Validation loss
estimates performance on held-out data. A widening gap in which training loss
falls while validation loss rises is evidence of overfitting.

## 12. Classification Accuracy During Evaluation

For multiclass logits, add:

```python
predicted_classes = output.argmax(dim=1)
correct += (predicted_classes == y_batch).sum().item()
```

For binary logits with shape `(n, 1)`, a probability threshold of $0.5$ is
equivalent to a logit threshold of $0$:

```python
predicted_classes = (logits >= 0.0).to(y_batch.dtype)
correct += (predicted_classes == y_batch).sum().item()
```

Accuracy is useful only when it matches the problem. For imbalanced classes,
also inspect precision, recall, $F_1$, and a confusion matrix.

## 13. Class Practice 1: Convert a CSV Target

A CSV contains three floating-point feature columns and an integer column named
`species_id` with class IDs $0$, $1$, and $2$. Write the pandas-to-tensor
conversion required by `nn.CrossEntropyLoss`.

<details>
<summary>Solution</summary>

```python
feature_columns = ["length", "width", "mass"]

X = torch.from_numpy(
    df[feature_columns].to_numpy(dtype="float32")
)
y = torch.from_numpy(
    df["species_id"].to_numpy(dtype="int64")
)

assert X.ndim == 2
assert y.ndim == 1
assert y.dtype == torch.long
```

The features use `float32`. The target is a one-dimensional tensor of integer
class IDs, as required by `CrossEntropyLoss`.

$\square$

</details>

## 14. Class Practice 2: Fix Evaluation

What is wrong with this validation loop?

```python
for X_batch, y_batch in val_loader:
    optimizer.zero_grad()
    loss = loss_fn(model(X_batch), y_batch)
    loss.backward()
    optimizer.step()
```

<details>
<summary>Solution</summary>

It trains on validation data, so the validation result is no longer held out.
Use `model.eval()` and `torch.inference_mode()`, and remove `zero_grad`,
`backward`, and `step`.

$\square$

</details>

## 15. Class Practice 3: Aggregate Unequal Batches

Two batches contain $64$ and $16$ examples. Their mean losses are $0.4$ and
$1.0$. What is the example-weighted mean loss?

<details>
<summary>Solution</summary>

$$
\frac{64(0.4)+16(1.0)}{64+16}
=\frac{41.6}{80}
=0.52.
$$

The unweighted average, $0.7$, would incorrectly give both batches equal
importance.

$\square$

</details>

## 16. Key Takeaways

- Use `pd.read_csv` to load a CSV and inspect the DataFrame before conversion.
- Select features and the target explicitly; encode text categories numerically.
- Convert features to `float32` and choose the target dtype and shape according
  to the loss function.
- Verify row counts, tensor ranks, and finite values before training.
- `TensorDataset` preserves the pairing between feature and target rows.
- `DataLoader` creates mini-batches and can shuffle training data.
- One ordinary mini-batch produces one optimizer update.
- Training and evaluation need separate code paths.
- Use both `model.eval()` and `torch.inference_mode()` during evaluation.
- Aggregate mean batch losses according to the number of examples.
- The model, inputs, and targets involved in one computation must share a
  device.

Next, we will combine the pieces in a complete nonlinear regression project.

