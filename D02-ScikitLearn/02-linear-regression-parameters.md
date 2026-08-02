# Lesson 2: Linear Regression Parameters

This lesson continues with the same `LinearRegression` model, but now we focus on the parameters we can control when training it.

Important idea:

- `LinearRegression` is a simple model
- it does not have many tuning knobs compared with models like `Ridge`, `Lasso`, or decision trees
- that makes it a good model for learning how scikit-learn APIs work

## 1. Two Kinds of Things We Can Control

When beginners say "model parameters," they often mean two different things.

### Model configuration

These are settings we choose before training, such as:

- `fit_intercept`
- `positive`
- `n_jobs`

We set these when creating the model.

### Learned parameters

These are values the model learns from the data, such as:

- `coef_`
- `intercept_`

We only get these after calling `fit`.

So in code:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept=True, positive=False)
```

Here we choose the configuration first. Later, training will produce learned values.

## 2. The Main Constructor Parameters

For a basic introduction, these are the most useful settings to know:

- `fit_intercept`
- `positive`
- `copy_X`
- `tol`
- `n_jobs`

We will also discuss `sample_weight`, which is passed to `fit(...)` instead of the constructor.

## 3. Example Setup

We will use a small dataset with two features.

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "sleep_hours": [8, 8, 7, 7, 6, 6, 5, 5],
    "exam_score": [50, 54, 60, 64, 71, 75, 81, 87]
})

X = df[["study_hours", "sleep_hours"]]
y = df["exam_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
```

## 4. `fit_intercept`

```python
model = LinearRegression(fit_intercept=True)
```

This controls whether the model learns a constant offset term.

If `fit_intercept=True`, the model is roughly:

```text
prediction = a1 * x1 + a2 * x2 + b
```

If `fit_intercept=False`, the model is roughly:

```text
prediction = a1 * x1 + a2 * x2
```

When should beginners usually use `True`?

- almost always for ordinary tabular data

When might `False` make sense?

- when the features and target were already centered in a way that makes the intercept unnecessary

Beginner rule:

- start with `fit_intercept=True`

## 5. `positive`

```python
model = LinearRegression(positive=True)
```

This forces all learned coefficients to be non-negative.

That means the model will not learn a negative slope for any feature.

This can be useful when negative coefficients would not make sense in the real problem.

Examples:

- quantity sold
- cost contribution
- count-based features

But be careful:

- this is a constraint
- constraints can make the model easier to interpret
- constraints can also reduce flexibility

Example:

```python
model = LinearRegression(positive=True)
model.fit(X_train, y_train)

print(model.coef_)
```

## 6. `copy_X`

```python
model = LinearRegression(copy_X=True)
```

This controls whether scikit-learn makes a copy of the feature matrix `X`.

For beginners:

- leave this as the default

Reason:

- it is safer
- it avoids accidental surprises if the training process modifies internal data

You usually think about this only when working with larger datasets or memory-sensitive workflows.

## 7. `tol`

```python
model = LinearRegression(tol=1e-6)
```

This is a tolerance setting related to the numerical solver.

For beginners:

- keep the default

Why?

- it is a lower-level numerical setting
- in simple dense-data examples, it is usually not the first thing you change

Mental model:

- this affects how precisely the solver decides the solution is good enough

In an introductory course, it is enough to know that this exists, but it is not usually the first tuning tool you reach for.

## 8. `n_jobs`

```python
model = LinearRegression(n_jobs=-1)
```

This controls parallel work across CPU cores in cases where the implementation can benefit from it.

For beginners:

- leaving it as default is completely fine

When might you change it?

- when training larger problems
- when working with multi-target outputs
- when you want to use all available CPU cores

Common values:

- `None` means default behavior
- `-1` means use all processors

## 9. `sample_weight` in `fit`

This one is different because it is passed during training:

```python
model = LinearRegression()
model.fit(X_train, y_train, sample_weight=[1, 1, 1, 1, 2, 2])
```

`sample_weight` lets some training examples matter more than others.

You can think of it like:

- larger weight means "pay more attention to this row"
- smaller weight means "this row matters less"

This is useful when:

- some observations are more reliable than others
- some data points represent more important cases
- some rows summarize many repeated events

Important:

- the number of weights should match the number of training rows

## 10. Full Example With Chosen Settings

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "sleep_hours": [8, 8, 7, 7, 6, 6, 5, 5],
    "exam_score": [50, 54, 60, 64, 71, 75, 81, 87]
})

X = df[["study_hours", "sleep_hours"]]
y = df["exam_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression(
    fit_intercept=True,
    positive=False,
    copy_X=True,
    tol=1e-6,
    n_jobs=None
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Predictions:", y_pred)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R^2:", r2_score(y_test, y_pred))
```

## 11. Reading the Result

After fitting:

```python
print(model.coef_)
print(model.intercept_)
```

These are not settings chosen by us.

These are learned from the data.

If the output is something like:

```python
[4.8, -1.2]
```

then the model is saying, approximately:

- increasing `study_hours` by `1` raises the prediction by about `4.8`
- increasing `sleep_hours` by `1` lowers the prediction by about `1.2`

This is one reason linear regression is easy to interpret.

## 12. What You Usually Change First

In beginner projects, the most practical choices are:

1. keep `fit_intercept=True`
2. leave `copy_X` and `tol` at their defaults
3. leave `n_jobs` alone unless you have a reason
4. try `positive=True` only if non-negative coefficients are important
5. use `sample_weight` only if some rows should count more than others

This means that, in practice, many beginner `LinearRegression` models look like:

```python
model = LinearRegression()
```

or:

```python
model = LinearRegression(fit_intercept=True, positive=True)
```

## 13. Common Beginner Mistakes

### Mistake 1: Changing settings without a reason

Not every parameter needs tuning.

Sometimes the default version is the best place to start.

### Mistake 2: Confusing configuration with learned coefficients

These are different:

- `fit_intercept=True` is a choice we make
- `model.intercept_` is a value the model learns

### Mistake 3: Passing the wrong shape

For example:

```python
X = df["study_hours"]
```

This creates a 1D object.

For feature input, we usually want:

```python
X = df[["study_hours"]]
```

which keeps a 2D structure.

## 14. Class Practice

### Practice 1

Use the lesson dataset and train three models:

1. `LinearRegression()`
2. `LinearRegression(fit_intercept=False)`
3. `LinearRegression(positive=True)`

Then compare:

- `coef_`
- `intercept_`
- predictions on the test set

### Practice 2

Create your own small dataset and train one model with:

```python
model.fit(X_train, y_train, sample_weight=...)
```

Then explain:

- which rows received larger weights
- why you chose those rows

## 15. Key Takeaways

- `LinearRegression` has a small number of configuration settings
- `fit_intercept` is the most important beginner-friendly setting
- `positive=True` can force non-negative coefficients
- `copy_X`, `tol`, and `n_jobs` are usually left at defaults in beginner examples
- `sample_weight` changes how much each training row influences the fit
- `coef_` and `intercept_` are learned results, not constructor settings
