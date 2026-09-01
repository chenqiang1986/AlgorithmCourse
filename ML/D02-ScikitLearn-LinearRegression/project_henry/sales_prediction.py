import math

import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures, StandardScaler


def mean_abs_p_error(actual, pred):
    diff = actual - pred
    diff = diff.abs()
    diff = diff / actual
    return diff.mean()

def mean_abs_p2_error(actual, pred):
    diff = actual - pred
    diff = diff.abs()
    diff = diff / actual
    diff = diff * diff
    return math.sqrt(diff.mean())


class GroupInteraction(BaseEstimator, TransformerMixin):
    def __init__(self, group_col):
        self.group_col = group_col

    def fit(self, X, y=None):
        self.numeric_cols_ = [c for c in X.columns if c != self.group_col]
        self.ohe_ = OneHotEncoder(handle_unknown="ignore")
        self.ohe_.fit(X[[self.group_col]])
        self.scaler_ = StandardScaler()
        self.scaler_.fit(X[self.numeric_cols_])
        return self

    def transform(self, X):
        groups = self.ohe_.transform(X[[self.group_col]]).toarray()  # (n, n_groups)
        nums = self.scaler_.transform(X[self.numeric_cols_])         # (n, n_features)
        # outer product per row -> (n, n_groups * n_features)
        return (groups[:, :, None] * nums[:, None, :]).reshape(len(X), -1)

    def get_feature_names_out(self, input_features=None):
        groups = self.ohe_.categories_[0]
        return [f"{g}_{f}" for g in groups for f in self.numeric_cols_]


df = pd.read_csv("Walmart_Sales.csv")

# Step 1: convert raw dates
df["dates"] = pd.to_datetime(df["Date"], format='%d-%m-%Y')

# Step 2: create date features
df["month"] = df["dates"].dt.month
df["year"] = df["dates"].dt.year


base_features = [
    "month",
    "year",
    "Unemployment",
    "CPI",
    "Fuel_Price",
    "Temperature",
]


poly_cols = ["month", 
             "year",
             "Unemployment", "CPI", "Fuel_Price"
            ]
categorical_features = ["Store", "Holiday_Flag"]

# Step 3: choose features and target
X = df[base_features + categorical_features]
y = df["Weekly_Sales"]

# Step 4: split first
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=5
)

# Step 5: tell sklearn which columns need which preprocessing

# Center month/year at 0 before raising to powers: raw x and x^2 are
# quasi-colinear when x sits far from 0 (e.g. year ~ 2010-2012), since
# x^2 = (mean + delta)^2 is then dominated by the linear term 2*mean*delta.
# Centering removes that dominant linear component first.
centered_poly = Pipeline(
    steps=[
        ("center", StandardScaler(with_std=False)),
        ("poly", PolynomialFeatures(degree=3, include_bias=False)),
    ]
)

poly_expander = ColumnTransformer(
    transformers=[
        ("poly", centered_poly, poly_cols),
    ],
    remainder="passthrough",
    verbose_feature_names_out=False,
).set_output(transform="pandas")

# Fitting only reveals the generated column names (shape-dependent, not
# value-dependent), so this doesn't leak anything from X_train.
poly_expander.fit(X_train)
numeric_features = [
    c for c in poly_expander.get_feature_names_out() if c not in categorical_features
]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", StandardScaler(), numeric_features),
        ("group", GroupInteraction("Store"), ["Store"] + numeric_features)
    ]
)

# Step 6: combine preprocessing and model into one pipeline
feature_pipeline = Pipeline(
    steps=[
        ("polyexpand", poly_expander),
        ("preprocess", preprocessor),
        ("regressor", Ridge(alpha=1.5))
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
print("MAEP2:", mean_abs_p2_error(y_test, y_pred))
print("MAEP2_train:", mean_abs_p2_error(y_train, y_train_pred))
print("R^2:", r2_score(y_test, y_pred))