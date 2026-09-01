# Lesson 1: How Transformers Work — fit, transform, fit_transform
*ML / D05-ScikitLearn-FeatureEngineering*

In [D02 Lesson 3](../D02-ScikitLearn-LinearRegression/03-linear-regression-data-preprocess.md) we used `OneHotEncoder`, `StandardScaler`, and `ColumnTransformer` together without asking what those tools actually have in common. This lesson opens that box by calling them one at a time, by hand, so `ColumnTransformer` stops looking like magic.

## 1. The Shared Interface

Every scikit-learn preprocessing tool — `StandardScaler`, `PolynomialFeatures`, `OneHotEncoder`, and (starting in Lesson 2) our own custom transformers — supports exactly three methods:

- `fit(X)` — look at `X` and learn something from it (a mean, a standard deviation, how many output columns to produce, ...). Nothing is transformed yet. Returns the object itself.
- `transform(X)` — apply whatever was learned in `fit` to `X`, and return the transformed array. `X` here does not have to be the same data that was passed to `fit`.
- `fit_transform(X)` — a shortcut that calls `fit(X)` then `transform(X)` on the same `X`.

Because every one of these tools follows this exact pattern, code that calls `.fit(...)` and `.transform(...)` does not need to know or care which specific transformer it is holding. That is the whole trick behind `ColumnTransformer` and `Pipeline` — see Section 4.

## 2. Calling StandardScaler by Hand

```python
import numpy as np
from sklearn.preprocessing import StandardScaler

X = np.array([[2.0], [4.0], [3.0], [6.0], [8.0], [5.0]])

scaler = StandardScaler()
scaler.fit(X)

print("learned mean:", scaler.mean_)
print("learned std:", scaler.scale_)

X_scaled = scaler.transform(X)
print(X_scaled)
```

`fit` computed a mean and a standard deviation from `X` and stored them as `scaler.mean_` and `scaler.scale_`. `transform` then applied:

$$
\text{new\_value} = \frac{\text{value} - \text{mean}}{\text{std}}
$$

Nothing was scaled until `transform` was called. `fit` only learned the numbers.

### The shortcut

```python
X_scaled = scaler.fit_transform(X)
```

This does the same two steps in one call, as long as you want to fit and transform the same array.

### Why the shortcut is dangerous on test data

`fit` should only ever see training data. If you call `fit_transform` on the test set too, the scaler learns a *different* mean/std from the test data instead of reusing what it learned from training — that is data leakage, the same mistake flagged in [D02 Lesson 3](../D02-ScikitLearn-LinearRegression/03-linear-regression-data-preprocess.md#13-common-mistakes).

```python
X_train = np.array([[2.0], [4.0], [3.0], [6.0]])
X_test = np.array([[8.0], [5.0]])

scaler = StandardScaler()
scaler.fit(X_train)                    # learn from training data only

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)   # reuse the training mean/std — NOT fit_transform
```

## 3. Calling PolynomialFeatures by Hand

```python
from sklearn.preprocessing import PolynomialFeatures

X = np.array([[2.0], [3.0], [4.0]])

poly = PolynomialFeatures(degree=3, include_bias=False)
poly.fit(X)
print(poly.get_feature_names_out())   # ['x0' 'x0^2' 'x0^3']

X_poly = poly.transform(X)
print(X_poly)
```

`PolynomialFeatures.fit` does not learn statistics the way `StandardScaler` does — it works out how many input columns there are and what the output columns should be named. That still counts as "fit," and the rule is the same: call `fit` (or `fit_transform`) once on training data, then reuse it with `transform` on anything else, including test data or new columns with the same shape.

```python
X_poly = poly.fit_transform(X)   # same shortcut as before
```

## 4. What ColumnTransformer Actually Does Underneath

`ColumnTransformer` takes a list of `(name, transformer, columns)` tuples and, for every one of them, calls `fit_transform` on the training slice and `transform` on any other data — then stacks the results side by side. Nothing more.

Here is that loop written out by hand, next to the `ColumnTransformer` call it replaces:

```python
import numpy as np

# --- what ColumnTransformer does internally, spelled out ---
def manual_column_transform(transformers, X_train, X_test):
    fitted = []
    train_parts, test_parts = [], []
    for name, transformer, columns in transformers:
        transformer.fit(X_train[columns])
        train_parts.append(transformer.transform(X_train[columns]))
        test_parts.append(transformer.transform(X_test[columns]))
        fitted.append((name, transformer))
    return np.hstack(train_parts), np.hstack(test_parts), fitted
```

```python
# --- the ColumnTransformer equivalent ---
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("poly", PolynomialFeatures(3, include_bias=False), poly_features),
])
X_train_out = preprocessor.fit_transform(X_train)
X_test_out = preprocessor.transform(X_test)
```

Both versions do the same thing: fit each transformer on the training columns it was assigned, transform train and test with that fitted state, and stack the results into one wide array. `ColumnTransformer` is just a tidier, well-tested way to write the loop above.

## 5. Class Practice

### Practice 1

Using your own toy numeric column (a `numpy` array with one column), call `PolynomialFeatures(degree=2, include_bias=False)` and `StandardScaler()` separately: `fit_transform` the column with `PolynomialFeatures` first, then `fit_transform` the *result* with `StandardScaler`. Print the shape after each step.

### Practice 2

Fill in `manual_column_transform` from Section 4 so it works on a small `pandas` `DataFrame` with two column groups (one numeric, one categorical with `OneHotEncoder`). Compare the output array to what `ColumnTransformer.fit_transform` / `.transform` produces on the same data — they should match.

## 6. Key Takeaways

- Every scikit-learn transformer shares the same `fit` / `transform` / `fit_transform` contract.
- `fit` learns parameters from data and stores them; `transform` applies what was learned.
- Always `fit` on training data only; reuse that fitted state with `transform` on test data — never `fit_transform` the test set.
- `fit_transform` is a convenience shortcut, not a different operation.
- `ColumnTransformer` and `Pipeline` call these same three methods for you, looped over column groups — there is no hidden magic underneath.

Lesson 2 builds a transformer of our own that follows this exact contract, so it can drop into a `ColumnTransformer` or `Pipeline` just like `PolynomialFeatures` or `StandardScaler`.
