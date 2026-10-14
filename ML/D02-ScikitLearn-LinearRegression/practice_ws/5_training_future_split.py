import pandas as pd
import numpy as np
import math
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, PolynomialFeatures

from fourier_features import FourierFeatures
from group_features import GroupInteraction


def mean_squared_percentage_error(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    return math.sqrt(np.mean(((y_true - y_pred) / y_true) ** 2))


def main():
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
        #"Year",        
        "Holiday_Flag",
    ]
    numeric_features = [
        "Month",
        "Month^2",
        "Month^3",
        "Temperature",
        "Fuel_Price",
        "CPI",
        #"Unemployment",
    ]
    fourier_features = [
        "DaysSince"
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

    
    preprocessor = ColumnTransformer(
        [
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
            ("group", GroupInteraction("Store"), ["Store"] + numeric_features),         
            ("fourier", FourierFeatures(degree=24), fourier_features),
        ],

    )

    regressor = TransformedTargetRegressor(
        regressor=Ridge(alpha=1e-6), func=np.log1p, inverse_func=np.expm1
    )

    model = Pipeline(
        [
            ("preprocess", preprocessor),
            ("regressor", regressor),
        ]
    )
    model.fit(X_train, y_train)

    #print(model[:-1].get_feature_names_out())

    y_pred_train = model.predict(X_train)
    print("Training Metric:")
    print(f"R^2: {r2_score(y_train, y_pred_train):.4f}")
    print(f"MAE: {mean_absolute_error(y_train, y_pred_train):.2f}")
    print(f"MAPE: {mean_absolute_percentage_error(y_train, y_pred_train):.2%}")
    print(f"MSPE: {mean_squared_percentage_error(y_train, y_pred_train):.2%}")


    y_pred_val = model.predict(X_val)
    print("\n\nValidation Metric:")
    print(f"R^2: {r2_score(y_val, y_pred_val):.4f}")
    print(f"MAE: {mean_absolute_error(y_val, y_pred_val):.2f}")
    print(f"MAPE: {mean_absolute_percentage_error(y_val, y_pred_val):.2%}")
    print(f"MSPE: {mean_squared_percentage_error(y_val, y_pred_val):.2%}")


    y_pred = model.predict(X_test)

    print("\n\nTesting Metric:")
    print(f"R^2: {r2_score(y_test, y_pred):.4f}")
    print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
    print(f"MAPE: {mean_absolute_percentage_error(y_test, y_pred):.2%}")
    print(f"MSPE: {mean_squared_percentage_error(y_test, y_pred):.2%}")


# Results recorded in https://docs.google.com/spreadsheets/d/1I_qK9cHIvwvts7d9nXeyzzCB1nM1ivz-z9D5V2HY3nI/edit?gid=0#gid=0    
if __name__ == "__main__":
    main()
