# Lesson 6: Train with Mini-Batches and Evaluate
*ML / D07-Torch-NN-Intro*

[Lesson 5](./05-full-batch-training.md) converted a CSV to tensors and used the
entire training set for each parameter update. This lesson divides those
tensors into mini-batches with `TensorDataset` and `DataLoader`. It also keeps
validation data separate and introduces reusable training and evaluation
functions.

## 1. Epochs and Mini-Batches

An **epoch** is one pass through the training set. A **mini-batch** is a smaller
group of training examples used for one parameter update.

With $N=1{,}000$ training examples and a batch size of $64$, one epoch contains
$16$ batches: $15$ full batches and one smaller final batch. Therefore, one
epoch now produces 16 optimizer updates rather than one.

Mini-batches offer a useful compromise:

- they require less memory than the full dataset;
- they produce more updates per epoch;
- each update uses more evidence than a single example.

The five optimizer operations do not change. They run once for each
mini-batch.

## 2. Split Before Building Data Loaders

Start with the `X_train` and `y_train` tensors created from the CSV in Lesson 5.
Keep aliases to the complete tensors, then make a reproducible
training-validation split:

```python
X_all = X_train
y_all = y_train

g = torch.Generator().manual_seed(42)
permutation = torch.randperm(len(X_all), generator=g)

n_train = int(0.8 * len(X_all))
train_indices = permutation[:n_train]
val_indices = permutation[n_train:]

X_train = X_all[train_indices]
y_train = y_all[train_indices]
X_val = X_all[val_indices]
y_val = y_all[val_indices]

assert len(X_train) + len(X_val) == len(X_all)
```

Validation rows must not influence parameter updates. In a real project,
reserve a final test set as well. Use validation results for modeling choices
and inspect the test set only after those choices are finished.

## 3. Pair Features and Targets with `TensorDataset`

```python
from torch.utils.data import DataLoader, TensorDataset

train_dataset = TensorDataset(X_train, y_train)
val_dataset = TensorDataset(X_val, y_val)

X_first, y_first = train_dataset[0]
print(X_first.shape)  # torch.Size([5])
print(y_first.shape)  # torch.Size([1])
```

Every tensor passed to `TensorDataset` must have the same first dimension. Row
$i$ from every tensor is treated as one sample, which preserves the pairing
between features and targets.

## 4. Let `DataLoader` Create Mini-Batches

```python
train_loader = DataLoader(
    train_dataset,
    batch_size=4,
    shuffle=True,
)

val_loader = DataLoader(
    val_dataset,
    batch_size=8,
    shuffle=False,
)
```

Iterating over a loader yields one paired mini-batch at a time:

```python
for X_batch, y_batch in train_loader:
    print(X_batch.shape, y_batch.shape)
    break
```

Use `shuffle=True` for ordinary training so consecutive epochs use different
batch groupings. Validation does not learn from batch order, so it uses
`shuffle=False`.

`DataLoader` includes a smaller final batch when the dataset size is not
divisible by `batch_size`, unless `drop_last=True` is requested.

## 5. Define the Model and Choose a Device

```python
def choose_device():
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


device = choose_device()

torch.manual_seed(42)
model = nn.Linear(X_all.shape[1], 1).to(device)

loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
```

This is a new model for a new training experiment. Keeping the same linear
architecture as Lesson 5 isolates the change from full-batch to mini-batch
training. Keep the source datasets on the CPU for this introductory workflow.
Each batch will move to the model's device inside the training or evaluation
function.

## 6. Train for One Epoch

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

The loop body is the same training step used for one full batch in Lesson 5.
The new outer `for` loop repeats that step for every mini-batch.

`model.train()` enables training behavior. This matters for modules such as
dropout and batch normalization, even if a simple linear/ReLU network behaves
identically in both modes.

The function weights each batch's mean loss by its batch size. Averaging batch
means directly would give a smaller final batch the same influence as a full
batch.

## 7. Evaluate Without Updating Parameters

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

`torch.inference_mode()` does not call `model.eval()` for you. The two lines
have different responsibilities.

## 8. Run the Epoch Loop

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
estimates performance on held-out data. Falling training loss accompanied by
rising validation loss is evidence of overfitting.

## 9. Classification Accuracy During Evaluation

For multiclass logits, an evaluation function can also count correct class
predictions:

```python
predicted_classes = output.argmax(dim=1)
correct += (predicted_classes == y_batch).sum().item()
```

For binary logits with shape `(n, 1)`, a probability threshold of $0.5$ is
equivalent to a logit threshold of $0$:

```python
predicted_classes = (output >= 0.0).to(y_batch.dtype)
correct += (predicted_classes == y_batch).sum().item()
```

Accuracy is useful only when it matches the problem. For imbalanced classes,
also inspect precision, recall, $F_1$, and a confusion matrix.

## 10. Class Practice 1: Count Mini-Batch Updates

A training dataset contains 1,000 examples and uses `batch_size=64` with
`drop_last=False`. How many times is `optimizer.step()` called in one epoch?

<details>
<summary>Solution</summary>

It is called 16 times: 15 full batches contain 960 examples, and the final
batch contains the remaining 40 examples.

$\square$

</details>

## 11. Class Practice 2: Fix Evaluation

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

## 12. Class Practice 3: Aggregate Unequal Batches

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

## 13. Key Takeaways

- Split held-out data before building loaders or training the model.
- `TensorDataset` preserves the pairing between feature and target rows.
- `DataLoader` creates mini-batches and can shuffle training data.
- One ordinary mini-batch produces one optimizer update.
- Training and evaluation need separate code paths.
- Use both `model.eval()` and `torch.inference_mode()` during evaluation.
- Weight batch mean losses by batch size before averaging across an epoch.
- The model, inputs, and targets in one computation must share a device.

Next, we will combine the pieces in a complete nonlinear regression project.
