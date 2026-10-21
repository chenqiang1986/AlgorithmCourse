from copy import deepcopy

from sklearn.model_selection import train_test_split
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

torch.manual_seed(42)
g = torch.Generator().manual_seed(42)


def synthetic_data(n_samples):    
    X = -2.0 + 4.0 * torch.rand((n_samples, 2), generator=g)
    y = (X[:, 0] * X[:, 1] > 0).to(torch.float32).reshape(-1, 1)

    flip_mask = torch.rand((n_samples, 1), generator=g) < 0.05
    y = torch.where(flip_mask, 1.0 - y, y)

    return X, y

def train_val_test_split(X, y):
    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.176, random_state=42)

    train_loader = DataLoader(
        TensorDataset(X_train, y_train),
        batch_size=64,
        shuffle=True,
    )
    val_loader = DataLoader(
        TensorDataset(X_val, y_val),
        batch_size=128,
        shuffle=False,
    )
    test_loader = DataLoader(
        TensorDataset(X_test, y_test),
        batch_size=128,
        shuffle=False,
    )

    return train_loader, val_loader, test_loader

def model_opt():
    model = nn.Sequential(
        nn.Linear(2, 16),
        #nn.ReLU(),
        #nn.Linear(16, 16),
        nn.ReLU(),
        nn.Linear(16, 1),
    )

    loss_fn = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    return model, loss_fn, optimizer

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

def choose_device():
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def eval_on_test(test_loader, checkpoint_path, device):
    model, loss_fn, _ = model_opt()

    model.load_state_dict(torch.load(checkpoint_path))
    model = model.to(device)

    test_loss, test_accuracy = evaluate_binary(model, test_loader, loss_fn, device)
    print(f"test_loss={test_loss}, test_accuracy={test_accuracy}")
    
def main():
    X, y = synthetic_data(2000)

    _, _, test_loader = train_val_test_split(X, y)

    checkpoint_path = "xor_classifier_state_john.pt"

    # Suppose that we have another process to read
    eval_on_test(test_loader, checkpoint_path, choose_device())


if __name__ == "__main__":
    main()