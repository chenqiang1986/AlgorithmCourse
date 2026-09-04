import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from fourier_features import FourierFeatures
from group_features import GroupInteraction

def mean_abs_p_error(actual, pred):
    diff = actual - pred
    diff = diff.abs()
    diff = diff / actual
    return diff.mean()


df = pd.read_csv("Walmart_Sales.csv")

# Step 1: convert raw dates
df["dates"] = pd.to_datetime(df["Date"], format='%d-%m-%Y')

# Step 2: create date features
df["month"] = df["dates"].dt.month
df["year"] = df["dates"].dt.year
df["doy"] = df["dates"].dt.day_of_year

numeric_features = [
    "month"
]

group_features = [
    "Temperature",
    "Fuel_Price",
    "CPI",
    "Unemployment",
]

categorical_features = ["Store", "Holiday_Flag", "year"]

fourier_features = ["doy"]

# Step 3: choose features and target
X = df[numeric_features + categorical_features + fourier_features + group_features]
y = df["Weekly_Sales"]

# Step 4: split first
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=5
)

# Step 5: tell sklearn which columns need which preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("grp", GroupInteraction("Store"), ["Store"] + group_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("fourier", FourierFeatures(degree=100), fourier_features),
    ]
)

# Step 6: combine preprocessing and model into one pipeline
feature_pipeline = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        ("regressor", LinearRegression())
    ]
)

model = TransformedTargetRegressor(
    regressor=feature_pipeline, func=np.log1p, inverse_func=np.expm1
)

# Step 7: fit on training data only
model.fit(X_train, y_train)

# Step 8: predict on test data
y_pred = model.predict(X_test)
y_train_pred = model.predict(X_train)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("MAEP:", mean_abs_p_error(y_test, y_pred))
print("MAEP_train:", mean_abs_p_error(y_train, y_train_pred))
print("R^2:", r2_score(y_test, y_pred))