import numpy as np
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.linear_model import LinearRegression
from sklearn.utils.validation import check_array, check_is_fitted


class RidgePerColumn(BaseEstimator, RegressorMixin):
    """Ridge regression with a separate penalty strength per input column.

    Parameters
    ----------
    alphas : array-like of shape (n_features,)
        Penalty for each column; 0 means no penalty on that column.
    fit_intercept : bool, default=True
        Whether to center X and y before fitting.
    """

    def __init__(self, alphas, fit_intercept=True):
        self.alphas = alphas
        self.fit_intercept = fit_intercept

    def fit(self, X, y):
        X = check_array(X, dtype=float)
        y = np.asarray(y, dtype=float)
        p = X.shape[1]
        alphas = np.asarray(self.alphas, dtype=float)  # length p

        if self.fit_intercept:
            X_mean, y_mean = X.mean(axis=0), y.mean()
            Xc, yc = X - X_mean, y - y_mean
        else:
            X_mean, y_mean = np.zeros(p), 0.0
            Xc, yc = X, y

        # append sqrt(alpha_j) on the diagonal as extra "pseudo-rows", zeros for y
        penalty_rows = np.diag(np.sqrt(alphas))
        X_aug = np.vstack([Xc, penalty_rows])
        y_aug = np.concatenate([yc, np.zeros(p)])

        reg = LinearRegression(fit_intercept=False).fit(X_aug, y_aug)
        self.coef_ = reg.coef_
        self.intercept_ = y_mean - X_mean @ self.coef_ if self.fit_intercept else 0.0
        self.n_features_in_ = p
        return self

    def predict(self, X):
        check_is_fitted(self, "coef_")
        X = check_array(X, dtype=float)
        return X @ self.coef_ + self.intercept_
