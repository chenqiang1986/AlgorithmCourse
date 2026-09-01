import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_array, check_is_fitted
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures, StandardScaler

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