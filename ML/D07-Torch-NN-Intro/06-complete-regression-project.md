# Lesson 6: Complete Regression Project
*ML / D07-Torch-NN-Intro*

This lesson trains a neural network on a nonlinear regression problem from
start to finish. The important result is not merely a low loss; it is a workflow
whose data split, shapes, training updates, and held-out evaluation can all be
explained.

## 1. The Learning Problem

Generate one feature $x$ and a noisy nonlinear target:

$$
y=0.6x^2+\sin(3x)+\varepsilon,
\qquad
\varepsilon\sim\mathcal{N}(0,0.15^2).
$$

A single linear layer cannot follow both the curve and the oscillation. A small
multilayer network can approximate them.

## 2. Generate and Split the Data

```python
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

torch.manual_seed(42)
g = torch.Generator().manual_seed(42)

n_samples = 1_200
X = -3.0 + 6.0 * torch.rand((n_samples, 1), generator=g)
noise = 0.15 * torch.randn((n_samples, 1), generator=g)
y = 0.6 * X**2 + torch.sin(3.0 * X) + noise

indices = torch.randperm(n_samples, generator=g)
n_train = int(0.70 * n_samples)
n_val = int(0.15 * n_samples)

train_idx = indices[:n_train]
val_idx = indices[n_train:n_train + n_val]
test_idx = indices[n_train + n_val:]

X_train, y_train = X[train_idx], y[train_idx]
X_val, y_val = X[val_idx], y[val_idx]
X_test, y_test = X[test_idx], y[test_idx]

assert X_train.ndim == y_train.ndim == 2
assert X_train.shape[1] == y_train.shape[1] == 1
```

The validation set guides modeling decisions. The test set is reserved for the
final estimate.

## 3. Standardize from Training Statistics

Feature scaling usually makes optimization easier. Compute statistics from the
training set only.

```python
X_mean = X_train.mean(dim=0, keepdim=True)
X_std = X_train.std(dim=0, keepdim=True).clamp_min(1e-8)

X_train_scaled = (X_train - X_mean) / X_std
X_val_scaled = (X_val - X_mean) / X_std
X_test_scaled = (X_test - X_mean) / X_std
```

Using validation or test statistics would leak information from held-out data
into the training pipeline.

## 4. Build the Data Loaders

```python
train_loader = DataLoader(
    TensorDataset(X_train_scaled, y_train),
    batch_size=64,
    shuffle=True,
)
val_loader = DataLoader(
    TensorDataset(X_val_scaled, y_val),
    batch_size=128,
    shuffle=False,
)
test_loader = DataLoader(
    TensorDataset(X_test_scaled, y_test),
    batch_size=128,
    shuffle=False,
)
```

Only the training loader shuffles because only training uses batch order to
produce updates.

## 5. Construct the Network

```python
model = nn.Sequential(
    nn.Linear(1, 32),
    nn.ReLU(),
    nn.Linear(32, 32),
    nn.ReLU(),
    nn.Linear(32, 1),
)

sample_output = model(X_train_scaled[:5])
assert sample_output.shape == (5, 1)
```

The final layer has one output and no activation because this is regression.

The parameter count is

$$
(1\cdot32+32)+(32\cdot32+32)+(32\cdot1+1)=1{,}153.
$$

## 6. Define the Training Tools

```python
def choose_device():
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def mean_loss(model, loader, loss_fn, device):
    model.eval()
    loss_sum = 0.0
    n_examples = 0

    with torch.inference_mode():
        for X_batch, y_batch in loader:
            X_batch = X_batch.to(device)
            y_batch = y_batch.to(device)
            loss = loss_fn(model(X_batch), y_batch)

            batch_size = X_batch.shape[0]
            loss_sum += loss.item() * batch_size
            n_examples += batch_size

    return loss_sum / n_examples


device = choose_device()
model = model.to(device)
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
```

Adam is still a gradient-based optimizer. It adapts the step size for each
parameter using moving summaries of past gradients.

## 7. Train and Monitor Validation Loss

```python
best_val_loss = float("inf")
best_state = None

for epoch in range(1, 301):
    model.train()
    train_loss_sum = 0.0
    n_train_examples = 0

    for X_batch, y_batch in train_loader:
        X_batch = X_batch.to(device)
        y_batch = y_batch.to(device)

        optimizer.zero_grad()
        predictions = model(X_batch)
        loss = loss_fn(predictions, y_batch)
        loss.backward()
        optimizer.step()

        batch_size = X_batch.shape[0]
        train_loss_sum += loss.item() * batch_size
        n_train_examples += batch_size

    train_loss = train_loss_sum / n_train_examples
    val_loss = mean_loss(model, val_loader, loss_fn, device)

    if val_loss < best_val_loss:
        best_val_loss = val_loss
        best_state = {
            name: tensor.detach().cpu().clone()
            for name, tensor in model.state_dict().items()
        }

    if epoch == 1 or epoch % 50 == 0:
        print(
            f"epoch={epoch:3d} "
            f"train_mse={train_loss:.4f} "
            f"val_mse={val_loss:.4f}"
        )
```

The copied `best_state` preserves the parameters with the lowest validation
loss. Without cloning, later in-place updates could change what appears to be a
saved best state.

## 8. Restore the Best Model and Test Once

```python
model.load_state_dict(best_state)

test_mse = mean_loss(model, test_loader, loss_fn, device)
test_rmse = test_mse**0.5

model.eval()
with torch.inference_mode():
    predictions = model(X_test_scaled.to(device)).cpu()

test_mae = (predictions - y_test).abs().mean().item()

print(f"test MSE:  {test_mse:.4f}")
print(f"test RMSE: {test_rmse:.4f}")
print(f"test MAE:  {test_mae:.4f}")
```

RMSE has the same unit as $y$. MAE reports the average absolute miss and is less
sensitive to a few large errors than MSE or RMSE.

## 9. Compare Against a Simple Baseline

A model should beat a reasonable simple guess. For MSE, predict the training
target mean for every test example:

```python
baseline_prediction = y_train.mean()
baseline_mse = ((y_test - baseline_prediction) ** 2).mean().item()

print(f"baseline test MSE: {baseline_mse:.4f}")
print(f"network test MSE:  {test_mse:.4f}")
```

A decreasing training loss is not enough. If the network cannot beat this
baseline on held-out data, the complete pipeline needs investigation.

## 10. Inspect Individual Predictions

```python
for x_value, target, prediction in zip(
    X_test[:10], y_test[:10], predictions[:10]
):
    print(
        f"x={x_value.item(): .3f} "
        f"target={target.item(): .3f} "
        f"prediction={prediction.item(): .3f}"
    )
```

Aggregate metrics can hide systematic errors. A plot of prediction and target
against $x$ is even more informative because the true pattern is one-dimensional.

## 11. Class Practice 1: Linear Baseline

Replace the network with `nn.Linear(1, 1)` and retrain it. Predict what should
happen to training and test MSE, then verify experimentally.

<details>
<summary>Solution</summary>

Both errors should be worse because one affine function cannot represent the
quadratic and sinusoidal pattern. The experiment demonstrates that hidden
layers plus nonlinear activations add useful representational capacity.

$\square$

</details>

## 12. Class Practice 2: Leakage Check

Why is the following scaling rule invalid?

```python
X_test_scaled = (X_test - X_test.mean()) / X_test.std()
```

<details>
<summary>Solution</summary>

It uses information from the test set to define preprocessing. The test set is
supposed to simulate unseen data. Scale validation and test features using
`X_mean` and `X_std` computed from training data only.

$\square$

</details>

## 13. Key Takeaways

- Split data before making data-dependent preprocessing choices.
- Fit preprocessing statistics on training data only.
- A regression model usually returns unrestricted numerical outputs.
- Track validation performance and restore the best validation state.
- Evaluate on the test set after model choices are complete.
- Compare against a simple baseline and inspect individual predictions.

Next, we will train a binary classifier, convert logits into decisions, save its
learned state, and use a debugging checklist.

