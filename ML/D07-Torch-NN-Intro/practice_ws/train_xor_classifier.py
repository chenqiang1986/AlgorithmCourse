"""Train a small PyTorch network on a noisy XOR classification problem."""

from copy import deepcopy

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


def choose_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def make_loaders(seed: int = 42) -> tuple[DataLoader, DataLoader, DataLoader]:
    generator = torch.Generator().manual_seed(seed)
    n_samples = 2_000

    features = -2.0 + 4.0 * torch.rand(
        (n_samples, 2), generator=generator
    )
    targets = (features[:, 0] * features[:, 1] > 0).to(torch.float32)
    targets = targets.reshape(-1, 1)

    flip_mask = torch.rand((n_samples, 1), generator=generator) < 0.05
    targets = torch.where(flip_mask, 1.0 - targets, targets)

    indices = torch.randperm(n_samples, generator=generator)
    n_train = int(0.70 * n_samples)
    n_val = int(0.15 * n_samples)

    train_indices = indices[:n_train]
    val_indices = indices[n_train : n_train + n_val]
    test_indices = indices[n_train + n_val :]

    train_dataset = TensorDataset(
        features[train_indices], targets[train_indices]
    )
    val_dataset = TensorDataset(features[val_indices], targets[val_indices])
    test_dataset = TensorDataset(features[test_indices], targets[test_indices])

    shuffle_generator = torch.Generator().manual_seed(seed + 1)
    train_loader = DataLoader(
        train_dataset,
        batch_size=64,
        shuffle=True,
        generator=shuffle_generator,
    )
    val_loader = DataLoader(val_dataset, batch_size=128, shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=128, shuffle=False)
    return train_loader, val_loader, test_loader


def build_model() -> nn.Module:
    return nn.Sequential(
        nn.Linear(2, 16),
        nn.ReLU(),
        nn.Linear(16, 16),
        nn.ReLU(),
        nn.Linear(16, 1),
    )


def evaluate_binary(
    model: nn.Module,
    loader: DataLoader,
    loss_fn: nn.Module,
    device: torch.device,
) -> tuple[float, float]:
    model.eval()
    loss_sum = 0.0
    correct = 0
    n_examples = 0

    with torch.inference_mode():
        for features, targets in loader:
            features = features.to(device)
            targets = targets.to(device)

            logits = model(features)
            loss = loss_fn(logits, targets)
            predictions = (logits >= 0.0).to(targets.dtype)

            batch_size = features.shape[0]
            loss_sum += loss.item() * batch_size
            correct += (predictions == targets).sum().item()
            n_examples += batch_size

    return loss_sum / n_examples, correct / n_examples


def main() -> None:
    torch.manual_seed(42)
    device = choose_device()
    train_loader, val_loader, test_loader = make_loaders()

    model = build_model().to(device)
    loss_fn = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    best_val_loss = float("inf")
    best_state = None

    for epoch in range(1, 101):
        model.train()
        for features, targets in train_loader:
            features = features.to(device)
            targets = targets.to(device)

            optimizer.zero_grad()
            logits = model(features)
            loss = loss_fn(logits, targets)
            loss.backward()
            optimizer.step()

        val_loss, val_accuracy = evaluate_binary(
            model, val_loader, loss_fn, device
        )
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_state = deepcopy(model.state_dict())

        if epoch == 1 or epoch % 20 == 0:
            print(
                f"epoch={epoch:3d} "
                f"val_loss={val_loss:.4f} "
                f"val_accuracy={val_accuracy:.3f}"
            )

    if best_state is None:
        raise RuntimeError("Training did not produce a checkpoint.")

    model.load_state_dict(best_state)
    test_loss, test_accuracy = evaluate_binary(
        model, test_loader, loss_fn, device
    )
    print(f"device={device}")
    print(f"test_loss={test_loss:.4f}")
    print(f"test_accuracy={test_accuracy:.3f}")


if __name__ == "__main__":
    main()

