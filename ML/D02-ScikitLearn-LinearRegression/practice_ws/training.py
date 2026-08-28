import pandas as pd
import numpy as np
import math
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def mean_squared_percentage_error(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    return math.sqrt(np.mean(((y_true - y_pred) / y_true) ** 2))


def main():
    df = pd.read_csv("Walmart_Sales.csv")

    df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
    df["Year"] = df["Date"].dt.year
    df["Year_SQR"] = df["Year"] * df["Year"]
    df["Year_CUB"] = df["Year_SQR"] * df["Year"]
    df["Month"] = df["Date"].dt.month
    df["Month_SQR"] = df["Month"] * df["Month"]
    df["Month_CUB"] = df["Month_SQR"] * df["Month"]
    df["Month_QUA"] = df["Month_CUB"] * df["Month"]
    df["Month_FIF"] = df["Month_QUA"] * df["Month"]
    df["Month_Year"] = df["Month"] * df["Year"]
    

    categorical_features = ["Store"]
    numeric_features = [
        "Holiday_Flag",
        "Temperature",
        "Fuel_Price",
        "CPI",
        "Unemployment",
        "Year",
        "Year_SQR",
        "Year_CUB",
        "Month",
        "Month_SQR",
        "Month_CUB",
        "Month_QUA",
        "Month_FIF",
        "Month_Year",
    ]
    features = categorical_features + numeric_features
    X = df[features]
    y = df["Weekly_Sales"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=22, stratify=df["Store"]
    )

    preprocessor = ColumnTransformer(
        [
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
            ("num", StandardScaler(), numeric_features),
        ]
    )

    regressor = TransformedTargetRegressor(
        regressor=LinearRegression(), func=np.log, inverse_func=np.exp
    )

    model = Pipeline(
        [
            ("preprocess", preprocessor),
            ("regressor", regressor),
        ]
    )
    model.fit(X_train, y_train)

    y_pred_train = model.predict(X_train)
    print("Training Metric:")
    print(f"R^2: {r2_score(y_train, y_pred_train):.4f}")
    print(f"MAE: {mean_absolute_error(y_train, y_pred_train):.2f}")
    print(f"MAPE: {mean_absolute_percentage_error(y_train, y_pred_train):.2%}")
    print(f"MSPE: {mean_squared_percentage_error(y_train, y_pred_train):.2%}")

    y_pred = model.predict(X_test)

    print("\n\nTesting Metric:")
    print(f"R^2: {r2_score(y_test, y_pred):.4f}")
    print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
    print(f"MAPE: {mean_absolute_percentage_error(y_test, y_pred):.2%}")
    print(f"MSPE: {mean_squared_percentage_error(y_test, y_pred):.2%}")


# Results recorded in https://docs.google.com/spreadsheets/d/1I_qK9cHIvwvts7d9nXeyzzCB1nM1ivz-z9D5V2HY3nI/edit?gid=0#gid=0    
if __name__ == "__main__":
    main()
