# Lesson 2: Writing a Custom Feature Transformer
*ML / D05-ScikitLearn-FeatureEngineering*

Lesson 1 showed that every transformer shares the same `fit` / `transform` / `fit_transform` contract. This lesson builds a transformer of our own that follows the exact same contract, so it can be dropped into a `ColumnTransformer` or `Pipeline` exactly like `PolynomialFeatures` or `StandardScaler`.

## 1. The Minimum Contract

To make a class usable as a scikit-learn transformer:

1. Inherit from `BaseEstimator` and `TransformerMixin`.
2. `__init__(self, ...)` — store hyperparameters as-is. Do not compute anything here.
3. `fit(self, X, y=None)` — learn whatever `transform` will need, store it on `self` using a name that ends in an underscore (a scikit-learn convention for "learned during fit"), then `return self`.
4. `transform(self, X)` — use the values learned in `fit` to build and return the new feature array.

Inheriting from `BaseEstimator, TransformerMixin` gives you `fit_transform` for free (built automatically from your `fit` and `transform`) and makes the object compatible with `Pipeline` and `ColumnTransformer`. You don't need to know how that inheritance works internally — just that adding those two base classes is what makes a custom class "a real transformer" instead of a plain Python class.

## 2. A First Custom Transformer: LogFeature

```python
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_array, check_is_fitted


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
```

Two helper functions do the input validation:

- `check_array(X)` converts `X` into a well-formed 2D `numpy` array and raises a clear error if it isn't shaped like one. It's the same helper `StandardScaler` and `PolynomialFeatures` use internally.
- `check_is_fitted(self, "min_")` raises a readable error if `transform` is called before `fit` — without it, calling `transform` first would just crash with a confusing `AttributeError`.

```python
X = np.array([[2.0], [4.0], [3.0], [10.0]])

log_feature = LogFeature()
X_log = log_feature.fit_transform(X)     # fit_transform works automatically
print(X_log)

X_new = np.array([[5.0]])
print(log_feature.transform(X_new))      # reuses self.min_ learned above
```

## 3. Reading Example: FourierFeatures

Here is a real custom transformer used later in this module, from `ML/lib/fourier_features.py`:

```python
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_array, check_is_fitted


class FourierFeatures(BaseEstimator, TransformerMixin):
    """Expand each raw feature x into Fourier terms.

    For every input column and every harmonic n = 1..degree, generates
        sin(2*pi*n*x / L) and cos(2*pi*n*x / L)
    where L is the range (max - min) of that column, learned at fit time.
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
```

Things worth noticing:

- `degree` is stored as-is in `__init__` and only used later in `fit`/`transform` — this is required so `get_params`/`set_params` (used by `Pipeline`) can inspect and clone the object correctly.
- `fit` learns `period_` — the span of each training column — and stores `n_features_in_` so `transform` can double-check it is being handed data shaped the way it expects.
- `transform` never touches `self.period_` differently than what `fit` computed; it only *uses* it. If you called `.fit` on training data and then `.transform` on test data, the test data reuses the training period exactly like `StandardScaler` reuses the training mean in Lesson 1.
- `get_feature_names_out` is not required by the base contract, but both `PolynomialFeatures` and `OneHotEncoder` implement it, and providing it keeps calls like `model[:-1].get_feature_names_out()` working when this transformer sits inside a `ColumnTransformer`/`Pipeline`.

We'll put `FourierFeatures` to work in Lesson 4.

## 4. Chaining Transformers: ColumnTransformer Runs in Parallel, Pipeline Runs in Sequence

Recall from [Lesson 1, Section 4](./01-transformer-fit-transform.md#4-what-columntransformer-actually-does-underneath): `ColumnTransformer` loops over its `(name, transformer, columns)` tuples independently. Every transformer in that list only ever sees the *original* columns it was assigned — never another entry's output. All entries are evaluated side by side ("simultaneously") and their results are stacked, not fed into each other.

That's fine when each column group needs exactly one transformation. But sometimes the *same* column group needs two transformations applied in sequence — for example, first clip outliers with `ClipFeature` (Practice 1 above), then scale the clipped result with `StandardScaler`. Listing both against the same columns in a `ColumnTransformer` does **not** chain them:

```python
# WRONG: both transformers look at the same original X, not at each other's output
preprocessor = ColumnTransformer([
    ("clip", ClipFeature(low=0, high=100), numeric_features),
    ("scale", StandardScaler(), numeric_features),
])
```

This computes `ClipFeature().fit_transform(X[numeric_features])` and, separately, `StandardScaler().fit_transform(X[numeric_features])` on the *same* input, then stacks both results side by side — doubling the columns instead of clipping and then scaling.

To make the output of one step feed into the next, wrap the steps in a `Pipeline` and hand that `Pipeline` to `ColumnTransformer` as if it were a single transformer:

```python
from sklearn.pipeline import Pipeline

clip_then_scale = Pipeline([
    ("clip", ClipFeature(low=0, high=100)),
    ("scale", StandardScaler()),
])

preprocessor = ColumnTransformer([
    ("num", clip_then_scale, numeric_features),
    ("poly", PolynomialFeatures(3, include_bias=False), poly_features),
])
```

`Pipeline` follows the exact same `fit` / `transform` / `fit_transform` contract as any other transformer (Lesson 1, Section 1) — that's why it can drop straight into a `ColumnTransformer` tuple in place of a single estimator. Internally, `Pipeline.fit_transform(X)` calls `clip.fit_transform(X)` and then feeds *that result* into `scale.fit_transform(...)`, instead of calling both steps on the original `X`.

Rule of thumb:

- Different column groups, one transformer each → list them directly in `ColumnTransformer`.
- Same column group, multiple transformers applied in sequence → wrap them in a `Pipeline` first, then give that `Pipeline` a single entry in `ColumnTransformer`.

## 5. Class Practice

### Practice 1

Implement a `ClipFeature(low, high)` transformer: `fit` should record the given `low`/`high` bounds (or compute them as quantiles of the training data, your choice), and `transform` should clip every value into `[low, high]` using `np.clip`. Inherit from `BaseEstimator, TransformerMixin` and use `check_array`/`check_is_fitted` like the examples above.

### Practice 2

Instantiate `FourierFeatures(degree=2)` directly (not inside a `ColumnTransformer`) on a toy column `np.arange(30).reshape(-1, 1)` representing 30 days. Call `fit_transform`, print the resulting shape, and call `get_feature_names_out()`. Confirm the output has `2 * degree` columns per input column, and that the names match what you'd expect from the harmonics `n = 1, 2`.

## 6. Key Takeaways

- Inherit from `BaseEstimator, TransformerMixin`; implement `__init__`, `fit`, `transform`.
- `fit` learns and stores fitted state as attributes ending in `_`; `transform` only uses that state, never re-learns it.
- `check_array` / `check_is_fitted` give the same input validation and error messages as built-in transformers.
- `get_feature_names_out` is optional but keeps introspection tools like `model[:-1].get_feature_names_out()` working when your transformer sits inside a pipeline.
- `ColumnTransformer` evaluates its entries in parallel, each against the original input columns — it never feeds one entry's output into another. To apply several transformers to the same columns in sequence, wrap them in a `Pipeline` and give that `Pipeline` a single entry in the `ColumnTransformer`.

Lesson 3 puts `PolynomialFeatures` back in the spotlight — and the one thing you must not forget when raising its degree.
