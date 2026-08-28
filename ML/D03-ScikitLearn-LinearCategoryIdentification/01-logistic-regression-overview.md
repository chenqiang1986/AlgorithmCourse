# Lesson 1: Logistic Regression Overview
*ML / D03-ScikitLearn-LinearCategoryIdentification*

This lesson gives a first look at the full code flow for training a logistic regression model with scikit-learn.

We already know the linear regression flow from [D02-ScikitLearn-LinearRegression](../D02-ScikitLearn-LinearRegression). The steps are almost identical. What changes is the type of question we are asking the model to answer.

## 1. What Problem Does Classification Solve?

Linear regression predicts a number.

Classification predicts a category.

Examples:

- will a customer churn? (`yes` / `no`)
- is this email spam? (`spam` / `not spam`)
- which digit is in this image? (`0`-`9`)
- what type of contract will a customer choose? (`month-to-month` / `one year` / `two year`)

Same idea as before, just a different kind of output:

```text
features  ->  model  ->  predicted category
```

## 2. Why Not Just Use Linear Regression?

Suppose we tried to predict `churn` (`0` = no, `1` = yes) with ordinary `LinearRegression`.

Problems:

- the output is not bounded between `0` and `1`, so predictions like `-0.3` or `1.4` do not make sense as a "probability of churn"
- the model treats the gap between class `0` and class `1` like a real numeric distance, which is not what we mean by a category
- a straight line is not a natural shape for "probability of belonging to a class"

We need a model whose output can be interpreted as a probability, and a way to turn that probability into a class decision.

## 3. The Sigmoid Function

Logistic regression starts the same way linear regression does: it computes a linear score from the features.

```text
score = a1 * x1 + a2 * x2 + ... + b
```

Then it squeezes that score into the range `0` to `1` using the **sigmoid function**:

```text
probability = 1 / (1 + e^(-score))
```

Key properties of sigmoid:

- very negative scores map close to `0`
- very positive scores map close to `1`
- a score of exactly `0` maps to `0.5`

This output can now be read as "the probability that this row belongs to class `1`."

## 4. From Probability to a Class Label

Once we have a probability, we need a decision rule.

The default rule scikit-learn uses:

```text
if probability >= 0.5: predict class 1
else:                  predict class 0
```

This `0.5` cutoff is called a **decision threshold**. It can be changed, but `0.5` is the sensible beginner default.

## 5. What About More Than Two Classes? Softmax Regression

Logistic regression, as described above, handles two classes (`binary classification`).

When there are more than two classes (for example predicting `Contract` type: `month-to-month`, `one year`, `two year`), we need a generalization called **softmax regression**, also known as **multinomial logistic regression**.

Instead of one score and one sigmoid, softmax regression computes one score per class:

```text
score_class_A = ...
score_class_B = ...
score_class_C = ...
```

Then the **softmax function** turns these scores into probabilities that all add up to `1`:

```text
probability_class_i = e^(score_i) / (e^(score_A) + e^(score_B) + e^(score_C))
```

The predicted class is simply the one with the highest probability.

The good news: in scikit-learn, both cases use the **same class**, `LogisticRegression`. It automatically detects whether the target has two classes or more than two, and switches between sigmoid-style (binary) and softmax-style (multinomial) behavior. We will see the relevant setting, `multi_class`, in the next lesson.

## 6. The Standard Code Flow

The workflow looks almost exactly like linear regression:

1. Import the libraries
2. Prepare the data
3. Split the data into training and testing sets
4. Create the model
5. Train the model with `fit`
6. Make predictions with `predict` (and `predict_proba` for probabilities)
7. Measure how well the model did, with classification metrics instead of MAE/R^2

## 7. A Small Example Dataset

Suppose we want to predict whether a student passes an exam, based on study hours.

```python
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
passed      = [0, 0, 0, 1, 0, 1, 1, 1]
```

Here:

- `study_hours` is the feature
- `passed` is the target, and it is a category (`0` = fail, `1` = pass), not a number to add or average

## 8. Full Example Code

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

# Step 1: Prepare the data in a table
df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "passed": [0, 0, 0, 1, 0, 1, 1, 1]
})

# Step 2: Separate features and target
X = df[["study_hours"]]
y = df["passed"]

# Step 3: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Step 4: Create the model
model = LogisticRegression()

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Make predictions on the test set
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)

# Step 7: Evaluate the model
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_[0])
print("Predicted classes:", y_pred)
print("Predicted probabilities:", y_proba)
print("Accuracy:", acc)
print("Confusion matrix:\n", cm)
```

## 9. Reading the Code Step by Step

### Import

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
```

Notice `LogisticRegression` lives in `sklearn.linear_model`, the same module as `LinearRegression`. Despite the name, it is a classification model, not a regression model, because of the sigmoid/softmax step at the end.

## 10. Separate `X` and `y`

```python
X = df[["study_hours"]]
y = df["passed"]
```

Same rule as before:

- `X` is 2D (double brackets)
- `y` is 1D

The difference is what `y` represents: a class label, not a continuous number.

## 11. Split Training and Testing Data

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
```

Same idea as linear regression: hold out data the model never saw during training, so we can honestly check how well it generalizes.

One extra thing to think about for classification: if the classes are imbalanced (for example `90%` class `0` and `10%` class `1`), the split can accidentally put very few examples of the minority class into the test set. A common fix is `stratify=y`:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
```

`stratify=y` keeps the class proportions similar in both the training and test sets.

## 12. Create and Train the Model

```python
model = LogisticRegression()
model.fit(X_train, y_train)
```

During `fit`, the model learns:

- `model.coef_`, the weight for each feature (like `a1`, `a2`, ... above)
- `model.intercept_`, the bias term (like `b` above)

These feed into the score, which is then passed through sigmoid (two classes) or softmax (more than two classes).

## 13. Make Predictions

```python
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)
```

Two useful outputs:

- `predict` gives the final class label, using the `0.5` threshold internally
- `predict_proba` gives the underlying probability for each class, which is often more informative

For example, `predict_proba` might return:

```text
[[0.83, 0.17],
 [0.05, 0.95]]
```

meaning row 1 has `83%` probability of class `0` and `17%` probability of class `1`, and row 2 has `5%`/`95%`.

## 14. Evaluate the Result

```python
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
```

Unlike linear regression, we cannot use MAE or R^2, because the target is not a continuous number.

Common classification metrics:

- **accuracy**: fraction of predictions that were correct
- **confusion matrix**: a table of correct vs incorrect predictions, broken down by class

We will cover more metrics (precision, recall, F1) in the practice project, because accuracy alone can be misleading on imbalanced data.

## 15. Mental Model for the Whole Script

1. Where is the data?
2. Which columns are the features?
3. Which column is the target, and is it a category?
4. Is `stratify=y` needed for the split?
5. Which model is created: `LogisticRegression`?
6. Where does `fit` happen?
7. Where does `predict` (and `predict_proba`) happen?
8. How is the result evaluated: accuracy, confusion matrix, or something else?

## 16. Class Practice

### Practice 1

Create a small dataset with:

- one feature called `hours_slept`
- one target called `felt_rested` (`0` or `1`)

Then:

1. put the data into a DataFrame
2. split into training and testing sets
3. train a `LogisticRegression` model
4. print both `predict` and `predict_proba` for the test set

### Practice 2

Take the lesson code and answer:

- what does `predict_proba` return that `predict` does not?
- what does the `0.5` threshold mean?
- why can't we use MAE or R^2 here?
- what would change if the target had three classes instead of two?

## 17. Key Takeaways

- classification predicts a category, not a number
- `LogisticRegression` computes a linear score, then applies sigmoid (two classes) or softmax (more than two classes) to get probabilities
- `predict` returns the class label; `predict_proba` returns the underlying probabilities
- `0.5` is the default decision threshold for binary classification
- softmax regression is the natural extension of logistic regression to more than two classes, and scikit-learn's `LogisticRegression` handles both
- classification needs different evaluation metrics than regression
