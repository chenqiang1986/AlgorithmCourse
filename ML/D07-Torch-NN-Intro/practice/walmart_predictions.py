from jinja2 import BaseLoader
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

def get_data():
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

    X_train_validation, X_test, y_train_validation, y_test = train_test_split(X, y, test_size = 0.2, shuffle=False)
    X_train, X_validation, y_train, y_validation = train_test_split(X_train_validation, y_train_validation, test_size = 0.2, shuffle=False)

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),
        ]
    )

    preprocessor.set_output(transform="pandas")

    preprocessor.fit(X_train)
    X_train = preprocessor.transform(X_train)
    X_test = preprocessor.transform(X_test)
    X_validation = preprocessor.transform(X_validation)
    return X_train, X_test, y_train, y_test, X_validation, y_validation

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

def train(model, train_loader, val_loader, loss_fn, optimizer, device):
    n_epochs = 500

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

X_train, X_test, y_train, y_test, X_validation, y_validation = get_data()

X_train = torch.from_numpy(X_train.to_numpy(dtype="float32"))
X_test = torch.from_numpy(X_test.to_numpy(dtype="float32"))
y_train = torch.from_numpy(y_train.to_numpy(dtype="float32")[:,None])
y_test = torch.from_numpy(y_test.to_numpy(dtype="float32")[:,None])
X_validation = torch.from_numpy(X_validation.to_numpy(dtype="float32"))
y_validation = torch.from_numpy(y_validation.to_numpy(dtype="float32")[:,None])

device=torch.device("mps")

model=nn.Sequential(
    nn.Linear(in_features=X_train.shape[1], out_features=7),
    nn.ReLU(),
    nn.Linear(in_features=7, out_features=4),
    nn.ReLU(),
    nn.Linear(in_features=4, out_features=1),
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

train(model, train_loader, val_loader, loss_fn, optimizer, device)
