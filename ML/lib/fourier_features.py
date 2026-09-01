import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_array, check_is_fitted


class FourierFeatures(BaseEstimator, TransformerMixin):
    """Expand each raw feature x into Fourier terms.

    For every input column and every harmonic n = 1..degree, generates
        sin(2*pi*n*x / L) and cos(2*pi*n*x / L)
    where L is the range (max - min) of that column, learned at fit time.

    Parameters
    ----------
    degree : int, default=1
        Highest harmonic n to generate.
    """

    def __init__(self, degree=1):
        self.degree = degree

    def fit(self, X, y=None):
        X = check_array(X)
        self.n_features_in_ = X.shape[1]
        self.period_ = X.max(axis=0) - X.min(axis=0) + 1
        return self

    def transform(self, X):
        check_is_fitted(self, "period_")
        X = check_array(X)
        n_samples, n_features = X.shape
        if n_features != self.n_features_in_:
            raise ValueError(
                f"X has {n_features} features, but FourierFeatures is "
                f"expecting {self.n_features_in_} features."
            )

        harmonics = np.arange(1, self.degree + 1)
        angles = 2 * np.pi * X[:, :, None] * harmonics[None, None, :] / self.period_[None, :, None]

        sin_features = np.sin(angles).reshape(n_samples, -1)
        cos_features = np.cos(angles).reshape(n_samples, -1)
        return np.hstack([sin_features, cos_features])

    def get_feature_names_out(self, input_features=None):
        check_is_fitted(self, "period_")
        if input_features is None:
            input_features = [f"x{i}" for i in range(self.n_features_in_)]

        sin_names = [
            f"sin({n}*{name})" for name in input_features for n in range(1, self.degree + 1)
        ]
        cos_names = [
            f"cos({n}*{name})" for name in input_features for n in range(1, self.degree + 1)
        ]
        return np.asarray(sin_names + cos_names, dtype=object)
