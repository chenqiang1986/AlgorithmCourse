# Lesson 7: Complete Classification Project and Debugging Guide
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

## 12. Final Mental Model

```text
choose task
    -> define output/loss/target contract
    -> split data
    -> build Dataset and DataLoader objects
    -> construct nn.Module
    -> move model and each batch to one device
    -> repeat forward/loss/backward/step on training batches
    -> evaluate without updates on validation data
    -> select the model
    -> test once
    -> save state_dict
```

## 13. Key Takeaways

- Binary models should return one raw logit per example during training.
- Convert logits to probabilities and decisions only when interpreting output.
- Validation data selects a model; test data estimates the selected model.
- Save and restore `state_dict` values with a matching architecture.
- Debug in a fixed order: shapes, dtypes, devices, finite values, gradients,
  updates, and only then architecture or hyperparameters.
- A model is trustworthy only when the complete data and evaluation workflow is
  trustworthy.

