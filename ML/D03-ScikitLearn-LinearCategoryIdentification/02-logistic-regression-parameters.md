# Lesson 2: Logistic Regression Parameters
*ML / D03-ScikitLearn-LinearCategoryIdentification*

This lesson continues with `LogisticRegression`, focusing on the parameters we can control when training it.

Compared with `LinearRegression`, `LogisticRegression` has more tuning knobs, because it involves an iterative solver and optional regularization.

## 1. Two Kinds of Things We Can Control

Same distinction as [D02 Lesson 2](../D02-ScikitLearn-LinearRegression/02-linear-regression-parameters.md):

### Model configuration

Settings we choose before training, such as:

- `penalty`
- `C`
- `solver`
- `max_iter`
- `multi_class`
- `class_weight`

### Learned parameters

Values the model learns from the data:

- `coef_`
- `intercept_`

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(C=1.0, penalty="l2", solver="lbfgs")
```

## 2. Example Setup

We will use a small dataset with two features.

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "practice_tests": [0, 1, 0, 2, 1, 3, 2, 4, 3, 5],
    "passed": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
})

X = df[["study_hours", "practice_tests"]]
y = df["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
```

## 3. `C`: Inverse Regularization Strength

```python
model = LogisticRegression(C=1.0)
```

`C` controls how much the model is allowed to fit the training data closely versus staying simple.

Important detail: `C` is the **inverse** of regularization strength.

- smaller `C` (e.g. `0.1`) means **stronger** regularization, a simpler model, coefficients pulled closer to `0`
- larger `C` (e.g. `10`) means **weaker** regularization, a model that fits the training data more closely

Beginner rule:

- start with the default `C=1.0`
- if the model overfits (great on training data, poor on test data), try a smaller `C`
- if the model underfits (poor on both), try a larger `C`

## 4. `penalty`: Which Kind of Regularization

```python
model = LogisticRegression(penalty="l2")
```

Common choices:

- `"l2"` (default): shrinks coefficients smoothly, keeps all features but with smaller weights
- `"l1"`: can shrink some coefficients all the way to `0`, effectively performing feature selection
- `"elasticnet"`: a mix of `l1` and `l2`, requires also setting `l1_ratio`
- `None`: no regularization

Beginner rule:

- `"l2"` is a safe default
- try `"l1"` if you want a simpler model that ignores unhelpful features

## 5. `solver`: How the Model Is Optimized

```python
model = LogisticRegression(solver="lbfgs")
```

Unlike `LinearRegression`, which has a closed-form solution, `LogisticRegression` uses an iterative optimizer to find the best coefficients. Different solvers support different penalties and dataset sizes.

Common solvers for beginners:

- `"lbfgs"` (default): good general-purpose choice, supports `l2` and no penalty
- `"liblinear"`: works well for smaller datasets, supports `l1` and `l2`, good for binary classification
- `"saga"`: supports `l1`, `l2`, and `elasticnet`, scales well to larger datasets

Beginner rule:

- keep the default `"lbfgs"` unless you specifically need `l1` or `elasticnet`, in which case use `"saga"`

## 6. `max_iter`: How Long the Solver Is Allowed to Run

```python
model = LogisticRegression(max_iter=1000)
```

Because training is iterative, it can sometimes stop before fully converging, especially with unscaled features.

If you see a warning like:

```text
ConvergenceWarning: lbfgs failed to converge
```

Two common fixes:

1. increase `max_iter` (e.g. from the default `100` to `1000`)
2. scale the numeric features first (see [Lesson 3](./03-classification-data-preprocess.md))

Both are often needed together in real projects.

## 7. `multi_class`: One-vs-Rest or Softmax

```python
model = LogisticRegression(multi_class="auto")
```

This setting matters once the target has more than two classes.

- `"auto"` (default): picks `"ovr"` for binary problems, and generally picks the multinomial (softmax) approach when the solver supports it and there are more than two classes
- `"ovr"` (one-vs-rest): trains one binary logistic regression per class ("is it class A or not?", "is it class B or not?", ...), then picks the class with the highest score
- `"multinomial"`: trains one true softmax model that considers all classes together, matching the softmax idea from [Lesson 1](./01-logistic-regression-overview.md#5-what-about-more-than-two-classes-softmax-regression)

Beginner rule:

- leave this as `"auto"` unless you are specifically comparing one-vs-rest with softmax behavior

## 8. `class_weight`: Handling Imbalanced Classes

```python
model = LogisticRegression(class_weight="balanced")
```

Real datasets are often imbalanced. For example, if only `20%` of customers churn, a model can reach high accuracy just by always predicting "no churn."

`class_weight="balanced"` automatically gives more weight to the minority class during training, so mistakes on that class are penalized more.

Beginner rule:

- if your target classes are noticeably imbalanced (like churn data), try `class_weight="balanced"` and compare it against the default

## 9. `fit_intercept`

```python
model = LogisticRegression(fit_intercept=True)
```

Same meaning as in `LinearRegression`: whether the model learns a bias term `b` in the score.

Beginner rule:

- keep the default `True`

## 10. Full Example With Chosen Settings

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "practice_tests": [0, 1, 0, 2, 1, 3, 2, 4, 3, 5],
    "passed": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
})

X = df[["study_hours", "practice_tests"]]
y = df["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

model = LogisticRegression(
    C=1.0,
    penalty="l2",
    solver="lbfgs",
    max_iter=1000,
    class_weight="balanced",
    fit_intercept=True
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Predictions:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
```

## 11. Reading the Result

```python
print(model.coef_)
print(model.intercept_)
```

These are learned, not chosen.

If `coef_` for `study_hours` is positive and large, it means more study hours push the score toward class `1` (pass) more strongly, before the sigmoid squeezes it into a probability.

Unlike `LinearRegression`, the raw coefficient value is harder to interpret directly as "one unit change equals this much output change," because of the sigmoid step in between. It is still true, though, that a positive coefficient pushes the prediction toward class `1`, and a negative coefficient pushes it toward class `0`.

## 12. What You Usually Change First

In beginner projects, the most practical choices are:

1. keep `solver="lbfgs"` and `penalty="l2"` unless you have a reason to change them
2. increase `max_iter` if you see a convergence warning
3. scale numeric features so the solver converges faster and more reliably
4. try `class_weight="balanced"` when classes are imbalanced
5. leave `multi_class="auto"` unless comparing one-vs-rest with softmax on purpose

This means many beginner `LogisticRegression` models look like:

```python
model = LogisticRegression(max_iter=1000)
```

or, for imbalanced data:

```python
model = LogisticRegression(max_iter=1000, class_weight="balanced")
```

## 13. Common Beginner Mistakes

### Mistake 1: Confusing `C` direction

Remember: smaller `C` means more regularization, not less. This is the opposite of how "strength" settings usually work, and it trips people up.

### Mistake 2: Ignoring convergence warnings

A model that has not converged may have unreliable coefficients. Increase `max_iter` or scale the features rather than ignoring the warning.

### Mistake 3: Trusting accuracy alone on imbalanced data

High accuracy can hide a model that never predicts the minority class. This is covered further in [Lesson 4](./04-classification-metrics.md).

### Mistake 4: Forgetting `stratify=y` on imbalanced targets

Without it, a train/test split can end up with very few examples of the minority class in one of the sets.

## 14. Class Practice

### Practice 1

Use the lesson dataset and train three models:

1. `LogisticRegression()`
2. `LogisticRegression(C=0.1)`
3. `LogisticRegression(C=10)`

Then compare:

- `coef_`
- `intercept_`
- predictions on the test set

### Practice 2

Create a dataset where one class is rare (for example, `9` rows of class `0` and only `1` row of class `1`). Train one model with `class_weight=None` and one with `class_weight="balanced"`. Compare predictions and explain the difference.

## 15. Key Takeaways

- `LogisticRegression` has more configuration options than `LinearRegression` because it uses an iterative solver
- `C` controls regularization strength, but smaller `C` means stronger regularization
- `penalty` and `solver` work together; not every combination is supported
- `max_iter` may need to be increased to avoid convergence warnings
- `multi_class` chooses between one-vs-rest and softmax (multinomial) behavior
- `class_weight="balanced"` helps when classes are imbalanced
- `coef_` and `intercept_` are learned results, not constructor settings
