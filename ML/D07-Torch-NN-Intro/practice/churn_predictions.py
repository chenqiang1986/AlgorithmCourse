import math
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

def find_cost(y_pred_logit, y, id, df):
    best_threshold = 100
    best_threshold_cost = 1000000.0
    id=id.detach().cpu().numpy()
    combined = df.copy()
    combined.loc[id, 'Churn'] = y.detach().cpu().numpy()
    combined.loc[id, 'pred_prob'] = 1 / (1 + np.exp(-y_pred_logit.detach().cpu().numpy()))
    for threshold in range(30, 31):
        combined.loc[id, 'pred_churn'] = np.where(combined.loc[id, 'pred_prob'] >= threshold/100, 1, 0)
        combined.loc[id, 'cost'] = np.select([
            (combined.loc[id, 'Churn'] == 1) & (combined.loc[id, 'pred_churn'] == 0),
            (combined.loc[id, 'Churn'] == 0) & (combined.loc[id, 'pred_churn'] == 1)
        ], [
            combined.loc[id, "MonthlyCharges"],
            20 
        ],
        default=0)
        cost = combined.loc[id, "cost"].sum()
        if  cost < best_threshold_cost:
            best_threshold = threshold
            best_threshold_cost = cost
    return best_threshold_cost, best_threshold

def find_cost_torch(output, y_batch, mc_batch):
    #pred_churn = torch.where(output >= math.log(3/7), 1, 0)
    #costs = torch.where(y_batch == 1, torch.where(pred_churn == 1, 0, mc_batch), torch.where(pred_churn == 1, 20, 0))
    #return costs.sum()
    return -torch.where(y_batch==1,
                        torch.where(output > -10, torch.log(torch.sigmoid(output)), output), 
                        torch.where(output < 10, torch.log(1 - torch.sigmoid(output)), -output)
    ).sum()

class CostLoss(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, predictions, targets, mc):
        cost = find_cost_torch(predictions, targets, mc)
        return cost


def get_data(seed):
    df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
    df["TotalCharges"] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    numeric_features = [
        "tenure",
        'TotalCharges',
        "MonthlyCharges",
    ]

    categorical_features = [
        'gender', 'SeniorCitizen', 'Partner', 'Dependents',
        'PhoneService', 'MultipleLines', 'InternetService',
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
        'PaymentMethod', 
    ]

    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    X = df[numeric_features + categorical_features]
    y = df["Churn"]

    X_train_vali, X_test, y_train_vali, y_test = train_test_split(X, y, test_size = 0.2, shuffle=True, random_state = 5)

    X_train, X_vali, y_train, y_vali = train_test_split(X_train_vali, y_train_vali, test_size = 0.25, shuffle=True, random_state = seed)

    mc_train = X_train["MonthlyCharges"]
    mc_vali = X_vali["MonthlyCharges"]

    preprocessor = ColumnTransformer(
        transformers = [
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),
        ]
    )

    preprocessor.set_output(transform="pandas")

    preprocessor.fit(X_train)
    X_train = preprocessor.transform(X_train)
    X_vali = preprocessor.transform(X_vali)
    X_test = preprocessor.transform(X_test)

    return X_train, X_vali, X_test, y_train, y_vali, y_test, mc_train, mc_vali

def train_one_epoch(model, loader, loss_fn, optimizer, device):
    model.train()
    total_loss = 0.0
    total_examples = 0

    for X_batch, y_batch, mc_batch in loader:
        X_batch = X_batch.to(device)
        y_batch = y_batch.to(device)
        mc_batch = mc_batch.to(device)

        optimizer.zero_grad()
        output = model(X_batch)
        loss = loss_fn(output, y_batch, mc_batch)
        loss.backward()
        optimizer.step()
        
        batch_size = X_batch.shape[0]
        total_loss += loss.item() * batch_size
        total_examples += batch_size

    return total_loss / total_examples

def evaluate(model, loader, loss_fn, device):
    model.eval()
    total_cost = 0.0
    total_examples = 0

    with torch.inference_mode():
        for X_batch, y_batch, mc_batch in loader:
            X_batch = X_batch.to(device)
            y_batch = y_batch.to(device)

            output = model(X_batch)
            cost = loss_fn(output, y_batch, mc_batch)

            batch_size = X_batch.shape[0]
            total_cost += cost.item()
            total_examples += batch_size

    return total_cost / total_examples

def train(model, train_loader, val_loader, loss_fn, optimizer, device):
    n_epochs = 3000

    best_cost = 1000
    best_epoch = 0

    for epoch in range(1, n_epochs + 1):
        train_loss = train_one_epoch(
            model, train_loader, loss_fn, optimizer, device
        )

        if epoch == 1 or epoch % 100 == 0:
            cost = evaluate(model, val_loader, loss_fn, device)

            if cost < best_cost:
                best_cost = cost
                best_epoch = epoch
            print(
                f"epoch={epoch:3d} "
                f"train_loss={train_loss:.4f} "
                f"val_cost={cost:.4f} "
            ) 
    return best_cost, best_epoch

seeds = [15, 10, 20, 25, 5, 30, 35]

for hidden_size in [5, 10, 15]:
    costs = []
    thresholds = []
    epochs = []
    for seed in seeds:
        print("Hidden Size, Seed", hidden_size, seed)
        X_train, X_validation, X_test, y_train, y_validation, y_test, mc_train, mc_vali = get_data(seed)

        X_train = torch.from_numpy(X_train.to_numpy(dtype="float32"))
        X_test = torch.from_numpy(X_test.to_numpy(dtype="float32"))
        y_train = torch.from_numpy(y_train.to_numpy(dtype="float32")[:,None])
        y_test = torch.from_numpy(y_test.to_numpy(dtype="float32")[:,None])
        X_validation = torch.from_numpy(X_validation.to_numpy(dtype="float32"))
        y_validation = torch.from_numpy(y_validation.to_numpy(dtype="float32")[:,None])
        mc_train = torch.from_numpy(mc_train.to_numpy(dtype="float32"))
        mc_vali = torch.from_numpy(mc_vali.to_numpy(dtype="float32"))

        device = torch.device("mps")

        model = nn.Sequential(
            nn.Linear(in_features = X_train.shape[1], out_features = hidden_size),
            nn.ReLU(),
            nn.Linear(in_features = hidden_size, out_features=1)
        ).to(device)

        loss_fn = CostLoss()
        optimizer = torch.optim.SGD(model.parameters(), 0.0005)

        train_dataset = TensorDataset(X_train, y_train, mc_train)
        val_dataset = TensorDataset(X_validation, y_validation, mc_vali)

        train_loader = DataLoader(
            train_dataset,
            batch_size = 64,
            shuffle = True,
        )

        val_loader = DataLoader(
            val_dataset,
            batch_size = X_validation.shape[0],
            shuffle = False,
        )

        cost, epoch = train(model, train_loader, val_loader, loss_fn, optimizer, device)
        costs.append(cost)
        epochs.append(epoch)
    costs = np.array(costs)
    epochs = np.array(epochs)
    cost_mean = costs.mean()
    cost_std = costs.std()
    epochs_mean = epochs.mean()
    epochs_std = epochs.std()
    with open("result.txt", "a") as file:
        file.write(f"Hidden Size: {hidden_size}\n")
        file.write(f"Cost Mean: {cost_mean}\n")
        file.write(f"Cost Std: {cost_std}\n")
        file.write(f"Epochs Mean: {epochs_mean}\n")
        file.write(f"Epochs Std: {epochs_std}\n")
