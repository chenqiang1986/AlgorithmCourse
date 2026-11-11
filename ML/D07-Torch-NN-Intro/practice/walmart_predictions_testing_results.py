import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

def get_data(train_val_split):
    df = pd.read_csv("Walmart_Sales.csv")

    df["Weekly_Sales"]=np.log(df["Weekly_Sales"])

    df["dates"] = pd.to_datetime(df["Date"], format='%d-%m-%Y')
    df = df.sort_values("dates")

    df["month"] = df["dates"].dt.month
    df["year"] = df["dates"].dt.year
    df["doy"] = df["dates"].dt.day_of_year

    numeric_features = [
        "Temperature",
        "Fuel_Price",
        "CPI",
        "month",
        "doy",
        "year",
        "Holiday_Flag",

    ]

    categorical_features = [
        "Store",
    ]

    X = df[numeric_features + categorical_features+["dates"]]
    y = df["Weekly_Sales"]

    X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size = train_val_split, shuffle=False)

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),
        ]
    )

    preprocessor.set_output(transform="pandas")

    preprocessor.fit(X_train)
    X_train = preprocessor.transform(X_train)
    X_validation = preprocessor.transform(X_validation)
    return X_train, y_train, X_validation, y_validation

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

def evaluate(model, loader, loss_fn, device):
    model.eval()
    total_loss = 0.0
    total_examples = 0

    with torch.inference_mode():
        for X_batch, y_batch in loader:
            X_batch = X_batch.to(device)
            y_batch = y_batch.to(device)

            output = model(X_batch)
            loss =(torch.abs(torch.exp(output)-torch.exp(y_batch))/torch.exp(output)).sum()

            batch_size = X_batch.shape[0]
            total_loss += loss
            total_examples += batch_size

    return total_loss / total_examples

def train(model, train_loader, val_loader, loss_fn, optimizer, device, train_val_split, hidden_features):
    n_epochs = 500

    lowest_val_loss=1.0

    checkpoint = {}

    for epoch in range(1, n_epochs + 1):
        train_loss = train_one_epoch(
            model, train_loader, loss_fn, optimizer, device
        )
        val_loss = evaluate(model, val_loader, loss_fn, device)
        if val_loss < lowest_val_loss:
            lowest_val_loss=val_loss
            checkpoint = {
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'loss': train_loss,
            }

        if epoch == 1 or epoch % 10 == 0:
            print(
                f"epoch={epoch:3d} "
                f"train_loss={train_loss:.4f} "
                f"val_loss={val_loss:.4f}"
            )
    torch.save(checkpoint, f"data/NN-test-{hidden_features}-{train_val_split}.cpt")
    print(lowest_val_loss)
    return lowest_val_loss.item()

def best_val_for_fold(train_val_split, hidden_features):
    X_train, y_train, X_validation, y_validation = get_data(train_val_split)

    X_train = torch.from_numpy(X_train.to_numpy(dtype="float32"))
    y_train = torch.from_numpy(y_train.to_numpy(dtype="float32")[:,None])
    X_validation = torch.from_numpy(X_validation.to_numpy(dtype="float32"))
    y_validation = torch.from_numpy(y_validation.to_numpy(dtype="float32")[:,None])

    device=torch.device("mps")

    model=nn.Sequential(
        nn.Linear(in_features=X_train.shape[1], out_features=hidden_features),
        nn.ReLU(),
        nn.Linear(in_features=hidden_features, out_features=1),
    ).to(device)

    loss_fn=nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.02)

    train_dataset = TensorDataset(X_train, y_train)
    val_dataset = TensorDataset(X_validation, y_validation)

    train_loader = DataLoader(
        train_dataset,
        batch_size=64,
        shuffle=True,
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=128,
        shuffle=False,
    )

    return train(model, train_loader, val_loader, loss_fn, optimizer, device, train_val_split, hidden_features)

hidden_features=3
folds=[0.15]

losses=np.array([])
for fold in folds:
    losses=np.append(losses, best_val_for_fold(fold, hidden_features))
loss_mean=losses.mean()
loss_std=losses.std()
torch.save([], f"data/NN-test-{hidden_features}-{loss_mean:.4f}-{loss_std:.4f}")