import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def main():
    df = pd.read_csv("Walmart_Sales.csv")

    df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month

    categorical_features = ["Store"]
    numeric_features = [
        "Holiday_Flag",
        "Temperature",
        "Fuel_Price",
        "CPI",
        "Unemployment",
        "Year",
        "Month",
    ]
    features = categorical_features + numeric_features
    X = df[features]
    y = df["Weekly_Sales"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    preprocessor = ColumnTransformer(
        [
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
            ("num", StandardScaler(), numeric_features),
        ]
    )

    model = Pipeline(
        [
            ("preprocess", preprocessor),
            ("regressor", LinearRegression()),
        ]
    )
    model.fit(X_train, y_train)

    y_pred_train = model.predict(X_train)
    print("Training Metric:")
    print(f"R^2: {r2_score(y_train, y_pred_train):.4f}")
    print(f"MAE: {mean_absolute_error(y_train, y_pred_train):.2f}")
    print(f"MAPE: {mean_absolute_percentage_error(y_train, y_pred_train):.2%}")

    y_pred = model.predict(X_test)

    print("\n\nTesting Metric:")
    print(f"R^2: {r2_score(y_test, y_pred):.4f}")
    print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
    print(f"MAPE: {mean_absolute_percentage_error(y_test, y_pred):.2%}")


    print("\n\nCoffifient:")
    feature_names = model.named_steps["preprocess"].get_feature_names_out()
    regressor = model.named_steps["regressor"]
    for feature, coef in zip(feature_names, regressor.coef_):
        print(f"{feature}: {coef:.2f}")
    print(f"Intercept: {regressor.intercept_:.2f}")


if __name__ == "__main__":
    main()
