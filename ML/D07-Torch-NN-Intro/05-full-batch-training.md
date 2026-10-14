# Lesson 5: Load CSV Data and Train with One Full Batch
*ML / D07-Torch-NN-Intro*

Real training data often begins in a CSV file rather than a tensor. This lesson
loads a CSV into pandas, prepares its columns, converts the values to PyTorch
tensors, and trains by passing the entire training set to the model at once.

There is no `Dataset`, `DataLoader`, or loop over smaller batches yet. The only
loop repeats one full-training-set update across epochs.

## 1. Load a CSV into a pandas DataFrame

The sample file
[`practice_ws/student_scores.csv`](./practice_ws/student_scores.csv) contains
four possible input columns and one regression target:

```text
hours_studied,attendance_rate,prior_score,study_method,exam_score
2.0,0.72,61,solo,64
5.5,0.91,78,group,84
```

Load the file and inspect it before converting anything:

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

Each row is one observation. Columns have different roles:

- feature columns are inputs to the model;
- the target column is the value the model should learn to predict;
- identifier columns describe rows but are usually not useful inputs.

Always inspect column names, dtypes, missing values, and a few rows before
building tensors.

## 2. Select and Prepare the Columns

Select features and the target by name:

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

A tensor must have one numerical dtype. The text values in `study_method`
therefore need numerical encoding. One-hot encoding creates one indicator
column per category:

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
table. It will become a tensor with shape `(n, 1)`, matching a regression model
with one output.

In a larger project, split the data before learning any data-dependent
preprocessing rule. For example, a fill value or scaling statistic must be
learned from the training rows only.

## 3. Convert the DataFrame to PyTorch Tensors

Choose the dtype explicitly during conversion:

```python
import torch
from torch import nn

X_array = feature_frame.to_numpy(dtype="float32")
y_array = target_frame.to_numpy(dtype="float32")

X_train = torch.from_numpy(X_array)
y_train = torch.from_numpy(y_array)

print(X_train.shape, X_train.dtype)  # torch.Size([16, 5]) torch.float32
print(y_train.shape, y_train.dtype)  # torch.Size([16, 1]) torch.float32

assert X_train.ndim == 2
assert y_train.ndim == 2
assert X_train.shape[0] == y_train.shape[0]
assert torch.isfinite(X_train).all()
assert torch.isfinite(y_train).all()
```

`torch.from_numpy` avoids an unnecessary copy when possible. The tensor and
NumPy array may share memory. Use `torch.tensor(X_array)` when an independent
copy is required.

pandas numerical columns are often `float64`, while PyTorch layers use
`float32` parameters by default. Explicit conversion prevents a dtype mismatch
during the forward pass.

### Classification targets use a different conversion

The target dtype and shape must follow the loss contract from
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

The student-score data is a regression dataset, so its target uses `float32`
and shape `(n, 1)`.

## 4. Treat the Entire Training Set as One Batch

A **batch** is the group of examples used to calculate one loss and one set of
gradients. Here, `X_train` and `y_train` contain every training example:

```python
n_examples, n_features = X_train.shape

print(n_examples)  # 16
print(n_features)  # 5
```

Passing `X_train` to the model produces all 16 predictions in one operation.
There is no need to loop over individual rows.

## 5. Build the Model and Training Tools

Use the simplest regression model from Lesson 1: one linear layer with one
output.

```python
torch.manual_seed(42)

model = nn.Linear(n_features, 1)

loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

assert model(X_train).shape == y_train.shape
```

`nn.MSELoss()` combines the errors from all 16 rows into one scalar mean loss.
The optimizer uses the gradients of that scalar to update every trainable
parameter.

## 6. Make One Full-Batch Update per Epoch

An **epoch** is one complete pass through the training set. Because the whole
training set is passed to the model together, one epoch contains exactly one
optimizer update:

```python
n_epochs = 500

for epoch in range(1, n_epochs + 1):
    model.train()

    optimizer.zero_grad()
    predictions = model(X_train)
    loss = loss_fn(predictions, y_train)
    loss.backward()
    optimizer.step()

    if epoch == 1 or epoch % 100 == 0:
        print(f"epoch={epoch:3d} training_mse={loss.item():.4f}")
```

The five operations from Lesson 4 are unchanged. The epoch loop simply repeats
them. With 500 epochs and one full batch, `optimizer.step()` runs 500 times.

The reported value is training loss. It measures fit to the same examples that
produced the parameter updates, so it does not estimate performance on unseen
data. Lesson 6 will split held-out data and evaluate it separately.

## 7. Why Full-Batch Training Is a Useful Starting Point

Full-batch training makes the data flow explicit:

```text
all X_train rows -> model -> all predictions -> one mean loss
                                                |
                                                v
                              backward -> optimizer step
```

It also has a practical limit. Every training row must fit in memory, and the
optimizer makes only one update after processing the whole training set.
Mini-batch training divides the tensors into smaller groups while keeping the
same five optimizer operations.

## 8. Class Practice 1: Convert a CSV Target

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

## 9. Class Practice 2: Count the Updates

A model uses the entire training set as one batch and trains for 250 epochs.
How many times is `optimizer.step()` called?

<details>
<summary>Solution</summary>

It is called 250 times: once per epoch.

$\square$

</details>

## 10. Key Takeaways

- Inspect a CSV before converting its columns.
- Select features and the target explicitly, and encode text categories.
- Convert features to `float32`; choose target dtype and shape according to the
  loss function.
- A batch is the set of examples used for one loss and one parameter update.
- Full-batch training sends every training row through the model at once.
- With one full batch, one epoch produces exactly one optimizer update.
- Training loss alone does not measure performance on unseen data.

Next, we will divide the tensors into mini-batches with `TensorDataset` and
`DataLoader`, then evaluate on held-out data.
