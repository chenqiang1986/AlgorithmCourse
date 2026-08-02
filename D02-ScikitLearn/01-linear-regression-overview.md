# Lesson 1: Linear Regression Overview

This lesson gives a first look at the full code flow for training a linear regression model with scikit-learn.

The goal is not to memorize every function yet. The goal is to understand the order of the steps and what each step does.

## 1. What Is scikit-learn?

scikit-learn is a Python library for machine learning.

It gives us ready-to-use tools for:

- regression
- classification
- clustering
- model evaluation
- preprocessing

For this first lesson, we will use a regression model called `LinearRegression`.

## 2. What Problem Does Linear Regression Solve?

Linear regression predicts a number.

Examples:

- predict a house price
- predict a student's final score
- predict sales next week

The model learns a relationship between:

- input variables, usually called features
- output variable, usually called the target

Simple idea:

```text
features  ->  model  ->  predicted target
```

## 3. The Standard Code Flow

A beginner-friendly machine learning workflow usually looks like this:

1. Import the libraries
2. Prepare the data
3. Split the data into training and testing sets
4. Create the model
5. Train the model with `fit`
6. Make predictions with `predict`
7. Measure how well the model did

This pattern appears again and again in scikit-learn.

## 4. A Small Example Dataset

Suppose we want to predict exam score from study hours.

```python
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
exam_scores = [52, 55, 61, 65, 72, 76, 82, 88]
```

Here:

- `study_hours` is the feature
- `exam_scores` is the target

In scikit-learn, features are usually stored in `X` and targets in `y`.

## 5. Full Example Code

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# Step 1: Prepare the data in a table
df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "exam_score": [52, 55, 61, 65, 72, 76, 82, 88]
})

# Step 2: Separate features and target
X = df[["study_hours"]]
y = df["exam_score"]

# Step 3: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Step 4: Create the model
model = LinearRegression()

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_[0])
print("Predictions:", y_pred)
print("MAE:", mae)
print("R^2:", r2)
```

## 6. Reading the Code Step by Step

### Import

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
```

These give us:

- the model itself
- a helper for splitting the data

We also import evaluation tools such as `mean_absolute_error` and `r2_score`.

## 7. Prepare the Data

```python
df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "exam_score": [52, 55, 61, 65, 72, 76, 82, 88]
})
```

This creates a small table.

Why use a DataFrame?

- it is easy to read
- it gives named columns
- later projects often already store data in a table

## 8. Separate `X` and `y`

```python
X = df[["study_hours"]]
y = df["exam_score"]
```

Important detail:

- `X` is usually a 2D structure
- `y` is usually a 1D structure

That is why `X` uses double brackets:

```python
df[["study_hours"]]
```

This keeps `X` as a table with one column.

## 9. Split Training and Testing Data

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
```

This means:

- `75%` of the data is used for training
- `25%` of the data is used for testing

Why split the data?

Because we want to check whether the model works on data it did not directly train on.

`random_state=42` makes the split reproducible.

## 10. Create and Train the Model

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

The line:

```python
model.fit(X_train, y_train)
```

is where learning happens.

The model looks at the training data and learns a best-fit line.

For a single feature case, we can think of the model roughly as:

```text
predicted_score = a * study_hours + b
```

After training:

- `a` is stored in `model.coef_`
- `b` is stored in `model.intercept_`

## 11. Make Predictions

```python
y_pred = model.predict(X_test)
```

This uses the trained model to predict scores for the test inputs.

If `X_test` contains study hours like `3` and `7`, the model outputs predicted exam scores for those values.

## 12. Evaluate the Result

```python
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

Two common metrics:

- `MAE` measures the average absolute prediction error
- `R^2` measures how well the model explains the variation in the target

General idea:

- lower `MAE` is better
- higher `R^2` is better

For this lesson, the main goal is just to see where evaluation happens in the code flow.

## 13. Predicting a New Value

After training, we can predict a new case.

```python
new_data = pd.DataFrame({
    "study_hours": [9]
})

predicted_score = model.predict(new_data)
print(predicted_score)
```

This asks:

- if a student studies `9` hours
- what score does the model predict?

## 14. Mental Model for the Whole Script

When you read beginner scikit-learn code, try this mental checklist:

1. Where is the data?
2. Which columns are the features?
3. Which column is the target?
4. Where is the train/test split?
5. Which model is created?
6. Where does `fit` happen?
7. Where does `predict` happen?
8. How is the result evaluated?

If you can answer those questions, you can usually follow the whole program.

## 15. Class Practice

### Practice 1

Create a small dataset with:

- one feature called `temperature`
- one target called `ice_cream_sales`

Then:

1. put the data into a DataFrame
2. split into training and testing sets
3. train a `LinearRegression` model
4. print predictions for the test set

### Practice 2

Take the lesson code and answer:

- what is `X`?
- what is `y`?
- what does `fit` do?
- what does `predict` do?
- why do we keep a test set?

## 16. Key Takeaways

- scikit-learn machine learning code usually follows a standard flow
- `X` stores features and `y` stores the target
- `train_test_split` separates learning data from checking data
- `fit` trains the model
- `predict` uses the trained model
- evaluation tells us whether the model is doing a useful job
