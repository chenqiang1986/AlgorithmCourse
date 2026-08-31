import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


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

numeric_features = [
    "Temperature",
    "Fuel_Price",
    "CPI",
    "Unemployment",
]

for i in range(1, 46):
    df[f"store{i}_month"] = (df["Store"] == i) * df["month"]
    df[f"store{i}_month2"] = df[f"store{i}_month"] * df[f"store{i}_month"]
    df[f"store{i}_month3"] = df[f"store{i}_month"] * df[f"store{i}_month"] * df[f"store{i}_month"]
    numeric_features.append(f"store{i}_month")
    numeric_features.append(f"store{i}_month2")
    numeric_features.append(f"store{i}_month3")

for i in range(1, 46):
    df[f"store{i}_year"] = (df["Store"] == i) * df["year"]
    df[f"store{i}_year2"] = df[f"store{i}_year"] * df[f"store{i}_year"]
    numeric_features.append(f"store{i}_year")
    numeric_features.append(f"store{i}_year2")


categorical_features = ["Store", "Holiday_Flag"]

# Step 3: choose features and target
X = df[numeric_features + categorical_features]
y = df["Weekly_Sales"]

# Step 4: split first
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=5
)

# Step 5: tell sklearn which columns need which preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
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