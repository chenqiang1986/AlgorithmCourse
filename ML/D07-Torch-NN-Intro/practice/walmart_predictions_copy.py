from jinja2 import BaseLoader
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

from fourier_features import FourierFeatures
from group_features import GroupInteraction

def get_data():
    df = pd.read_csv("Walmart_Sales.csv")

    df["Weekly_Sales"]=np.log1p(df["Weekly_Sales"])

    df["dates"] = pd.to_datetime(df["Date"], format='%d-%m-%Y')
    df = df.sort_values("dates")

    df["month"] = df["dates"].dt.month
    df["year"] = df["dates"].dt.year
    df["doy"] = df["dates"].dt.day_of_year

    df["month2"] = df["month"] * df["month"]
    df["month3"] = df["month"] * df["month2"]

    df["doy2"] = df["doy"] * df["doy"]
    df["doy3"] = df["doy"] * df["doy2"]

    numeric_features = [
        #"doy",
        #"doy2",
        #"doy3"
    ]

    group_features = [
        "Temperature",
        "Fuel_Price",
        "CPI",
        "month",
        "month2",
        "month3"
    ]

    categorical_features = ["Store", "Holiday_Flag", "year"]

    fourier_features = [
        "doy"
    ]

    # Step 3: choose features and target
    X = df[numeric_features + categorical_features + fourier_features + group_features + ["dates"]]
    y = df["Weekly_Sales"]

    # Step 4: split first
    X_train_validation, X_test, y_train_validation, y_test = train_test_split(X, y, test_size = 0.1, shuffle=False)
    X_train, X_validation, y_train, y_validation = train_test_split(X_train_validation, y_train_validation, test_size = 0.2, shuffle=False)
    print(X_train["dates"].min())
    print(X_train["dates"].max())
    print(X_validation["dates"].min())
    print(X_validation["dates"].max())
    print(X_test["dates"].min())
    print(X_test["dates"].max())

    # Step 5: tell sklearn which columns need which preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),
            ("grp", GroupInteraction("Store"), ["Store"] + group_features),
            ("fourier", FourierFeatures(degree=24), fourier_features),
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
            loss =(torch.abs(torch.expm1(output)-torch.expm1(y_batch))/torch.expm1(output)).sum()

            #print(torch.exp(output))
            #print(torch.exp(y_batch))

            batch_size = X_batch.shape[0]
            total_loss += loss
            total_examples += batch_size

    return total_loss / total_examples

def train(model, train_loader, val_loader, loss_fn, optimizer, device):
    n_epochs = 10000

    for epoch in range(1, n_epochs + 1):
        train_loss = train_one_epoch(
            model, train_loader, loss_fn, optimizer, device
        )
        #train_loss = evaluate(model, train_loader, loss_fn, device)
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

device=torch.device("cpu")

model=nn.Sequential(
    nn.Linear(in_features=X_train.shape[1], out_features=1),
    #nn.ReLU(),
    #nn.Linear(in_features=7, out_features=4),
    #nn.ReLU(),
    #nn.Linear(in_features=4, out_features=1),
).to(device)

loss_fn=nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

train_dataset = TensorDataset(X_train, y_train)
val_dataset = TensorDataset(X_validation, y_validation)

train_loader = DataLoader(
    train_dataset,
    batch_size=X_train.shape[0],
    shuffle=True,
)

val_loader = DataLoader(
    val_dataset,
    batch_size=X_validation.shape[0],
    shuffle=False,
)

train(model, train_loader, val_loader, loss_fn, optimizer, device)
