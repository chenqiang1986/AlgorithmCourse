from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.compose import ColumnTransformer
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_array, check_is_fitted
from fourier_features import FourierFeatures

class LogFeature(BaseEstimator, TransformerMixin):
    """Replace each column with log1p(x - min(x)) learned at fit time."""

    def fit(self, X, y=None):
        X = check_array(X)
        self.min_ = X.min(axis=0)
        return self

    def transform(self, X):
        check_is_fitted(self, "min_")
        X = check_array(X)
        return np.log1p(X - self.min_)

X = np.array([[2.0], [4.0], [3.0], [10.0]])

log_feature = LogFeature()
X_log = log_feature.fit_transform(X)     # fit_transform works automatically
print(X_log)

X_new = np.array([[5.0]])
print(log_feature.transform(X_new))      # reuses self.min_ learned above

fourier_feature = FourierFeatures()
X_fourier = fourier_feature.fit_transform(X)
print(fourier_feature.get_feature_names_out())
print(X_fourier)
print(fourier_feature.transform(X_new))