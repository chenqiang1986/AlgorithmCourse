import pandas as pd
import numpy as np
import math
import torch
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, PolynomialFeatures
from torch import nn

from fourier_features import FourierFeatures
from group_features import GroupInteraction
from torch_util import convert_to_torch


def mean_squared_percentage_error(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    return math.sqrt(np.mean(((y_true - y_pred) / y_true) ** 2))

def read_data_and_feature_eng():
    df = pd.read_csv("Walmart_Sales.csv")
    
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
    df = df.sort_values("Date")

    df["DaysSince"] = df["Date"].dt.day_of_year
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Month^2"] = df["Date"].dt.month * df["Month"]
    df["Month^3"] = df["Month"] * df["Month^2"]


    categorical_features = [
        "Store",   
        "Holiday_Flag",
    ]
    numeric_features = [
        "Year",     
        "Month",
        "Month^2",
        "Month^3",
        "Temperature",
        "Fuel_Price",
        "CPI",
        "Unemployment",
        #DaysSince"
    ]
    fourier_features = [
        #"DaysSince"
    ]

    features = categorical_features + numeric_features + fourier_features + ["Date"]
    X = df[features]
    y = df["Weekly_Sales"]

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=0.2, shuffle=False
    )

    assert(X_train["Date"].max() <= X_val["Date"].min())
    assert(X_val["Date"].max() <= X_test["Date"].min())

    
    preprocessor = ColumnTransformer(
        [
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
            #("group", GroupInteraction("Store"), ["Store"] + numeric_features),         
            ("Scale", StandardScaler(), numeric_features),
            #("fourier", FourierFeatures(degree=24), fourier_features),
        ],

    )
    
    print("Before feature eng: X train shape: ", X_train.shape)
    X_train = preprocessor.fit_transform(X_train).toarray()
    print("After feature eng: X train shape: ", X_train.shape)

    print("Before feature eng: X val shape: ", X_val.shape)
    # No more fitting here
    X_val = preprocessor.transform(X_val).toarray()
    print("After feature eng: X val shape: ", X_val.shape)

    print("Before feature eng: X shape: ", X_test.shape)
    # No more fitting here
    X_test = preprocessor.transform(X_test).toarray()
    print("After feature eng: X shape: ", X_test.shape)

    return X_train, y_train, X_val, y_val, X_test, y_test

def nn_eval(title, model, loss_fn, X, y):
    model.eval()
    ln_y_pred = model(X)
    y_pred = torch.exp(ln_y_pred)

    print(title, "Evaluation:")
    print(" - MAE:", torch.abs(y_pred - y).mean())
    print(" - MAPE:", (torch.abs(y_pred - y)/y).mean())

def nn_train(X_train, y_train, X_val, y_val, max_iter=100000, lr=0.03):
    ln_y_train = torch.log(y_train)

    model = nn.Sequential(
        nn.Linear(X_train.shape[1], 16),
        nn.ReLU(),
        nn.Linear(16, 4),      
        nn.ReLU(),
        nn.Linear(4, 1),     
    )
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=lr)
       
    for i in range(max_iter):
        # Tell the model it is now in training mode
        model.train()
        optimizer.zero_grad()

        predictions = model(X_train)
        loss = loss_fn(predictions, ln_y_train)

        loss.backward()
        optimizer.step()

        if i % 500 == 0:
            nn_eval("Validation", model, loss_fn, X_val, y_val)




def main():    
    X_train, y_train, X_val, y_val, X_test, y_test = read_data_and_feature_eng()

    X_nn_train, y_nn_train, X_nn_val, y_nn_val, X_nn_test, y_nn_test = convert_to_torch(
        X_train, y_train, X_val, y_val, X_test, y_test
    )

    print(X_nn_train.dtype)
    print(X_nn_train.shape)

    print(y_nn_train.dtype)
    print(y_nn_train.shape)

    print(X_nn_val.shape)
    print(y_nn_val.shape)
    print(X_nn_test.shape)
    print(y_nn_test.shape)

    nn_train(X_nn_train, y_nn_train, X_nn_val, y_nn_val)



        

# Results recorded in https://docs.google.com/spreadsheets/d/1I_qK9cHIvwvts7d9nXeyzzCB1nM1ivz-z9D5V2HY3nI/edit?gid=0#gid=0    
if __name__ == "__main__":
    main()
