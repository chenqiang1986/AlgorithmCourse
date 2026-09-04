from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.compose import ColumnTransformer
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_array, check_is_fitted
from fourier_features import FourierFeatures
from group_features import GroupInteraction

df = pd.DataFrame({
    "store": ["A", "A", "B", "B"],
    "temp": [40, 60, 40, 60],
    "fuel": [2, 8, 8, 2]
})

processor = ColumnTransformer([
    ("grp", GroupInteraction("store"), ["store", "temp"]),
], remainder="passthrough", verbose_feature_names_out=False).set_output(transform="pandas")

print(processor.fit_transform(df))