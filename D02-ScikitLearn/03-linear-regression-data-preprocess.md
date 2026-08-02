# Lesson 3: Data Preprocess for Linear Regression

In real data, columns are often not ready to use directly.

Even if we still use the same `LinearRegression` model, we may need to preprocess the data first.

In this lesson, we focus on three very common cases:

1. some input columns are categorical
2. some input columns are dates
3. some numeric columns have very different magnitudes

## 1. Why Preprocessing Matters

Machine learning models work with numbers.

That means:

- text categories usually need to be encoded
- raw date strings usually need to be transformed into useful numerical features
- numeric columns may need scaling so they are on a more comparable range

In scikit-learn, preprocessing is usually done with:

- transformers such as `OneHotEncoder` and `StandardScaler`
- `ColumnTransformer` to apply different transformations to different columns
- `Pipeline` to connect preprocessing and model training into one flow

## 2. Example Dataset

Suppose we want to predict a student's final score.

```python
import pandas as pd

df = pd.DataFrame({
    "study_hours": [2, 4, 3, 6, 8, 5, 7, 9],
    "practice_questions": [20, 50, 35, 80, 120, 65, 100, 140],
    "course_type": ["online", "offline", "online", "offline", "offline", "online", "online", "offline"],
    "exam_date": [
        "2026-01-10", "2026-01-12", "2026-01-18", "2026-02-01",
        "2026-02-10", "2026-02-12", "2026-03-01", "2026-03-08"
    ],
    "final_score": [55, 63, 60, 74, 85, 70, 81, 90]
})
```

Here:

- `study_hours` is numeric
- `practice_questions` is numeric, but its magnitude is much larger
- `course_type` is categorical
- `exam_date` is a date string

## 3. Categorical Data: Turn Labels Into Numbers

Suppose a column contains:

```python
["online", "offline", "online"]
```

We cannot feed those words directly into ordinary linear regression.

A common solution is one-hot encoding.

### One-hot encoding idea

Instead of one column:

```text
course_type
online
offline
online
```

we create binary columns such as:

```text
course_type_offline  course_type_online
0                    1
1                    0
0                    1
```

In scikit-learn, we usually use `OneHotEncoder`.

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(handle_unknown="ignore")
```

Why `handle_unknown="ignore"` is useful:

- if new category values appear later in test data or future data
- the transform step can still continue without crashing

## 4. Dates: Convert Them Into Useful Features

A raw date string like:

```python
"2026-02-10"
```

is not usually the final feature we want.

First, convert it into datetime form:

```python
df["exam_date"] = pd.to_datetime(df["exam_date"])
```

Then extract useful parts.

### Common date features

```python
df["exam_year"] = df["exam_date"].dt.year
df["exam_month"] = df["exam_date"].dt.month
df["exam_dayofweek"] = df["exam_date"].dt.dayofweek
```

These can capture patterns such as:

- different months behaving differently
- weekdays behaving differently
- long-term trends across years

Another useful idea is elapsed time.

```python
df["days_since_start"] = (df["exam_date"] - df["exam_date"].min()).dt.days
```

This turns dates into a single growing number.

That can be easier for linear regression to use when the main idea is time passing forward.

## 5. Different Magnitudes: Why Scaling Helps

Look at these two columns:

- `study_hours` might range from `2` to `9`
- `practice_questions` might range from `20` to `140`

The scales are very different.

Common scaling methods include:

- standardization with `StandardScaler`
- min-max scaling with `MinMaxScaler`

### Standardization

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
```

This transforms each numeric feature to a centered scale based on the training data.

You can think of it as:

```text
new_value = (value - mean) / standard_deviation
```

### Min-max scaling

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
```

This maps each column into a fixed range, usually `0` to `1`.

Beginner rule:

- `StandardScaler` is a very common default
- `MinMaxScaler` is useful when you specifically want a bounded range like `0` to `1`

## 6. The Best Habit: Split First, Then Fit Preprocessors on Training Data

We should not learn scaling statistics from the full dataset before the train/test split.

Instead:

1. split into training and test sets
2. fit preprocessors on the training data
3. use the same fitted preprocessors to transform the test data

The easiest safe way to do this is a scikit-learn `Pipeline`.

## 7. Full Example: Preprocess and Train

```python
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.DataFrame({
    "study_hours": [2, 4, 3, 6, 8, 5, 7, 9],
    "practice_questions": [20, 50, 35, 80, 120, 65, 100, 140],
    "course_type": ["online", "offline", "online", "offline", "offline", "online", "online", "offline"],
    "exam_date": [
        "2026-01-10", "2026-01-12", "2026-01-18", "2026-02-01",
        "2026-02-10", "2026-02-12", "2026-03-01", "2026-03-08"
    ],
    "final_score": [55, 63, 60, 74, 85, 70, 81, 90]
})

# Step 1: convert raw dates
df["exam_date"] = pd.to_datetime(df["exam_date"])

# Step 2: create date features
df["exam_month"] = df["exam_date"].dt.month
df["exam_dayofweek"] = df["exam_date"].dt.dayofweek
df["days_since_start"] = (df["exam_date"] - df["exam_date"].min()).dt.days

# Step 3: choose features and target
X = df[[
    "study_hours",
    "practice_questions",
    "course_type",
    "exam_month",
    "exam_dayofweek",
    "days_since_start"
]]
y = df["final_score"]

# Step 4: split first
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Step 5: tell sklearn which columns need which preprocessing
numeric_features = [
    "study_hours",
    "practice_questions",
    "exam_month",
    "exam_dayofweek",
    "days_since_start"
]
categorical_features = ["course_type"]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# Step 6: combine preprocessing and model into one pipeline
model = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        ("regressor", LinearRegression())
    ]
)

# Step 7: fit on training data only
model.fit(X_train, y_train)

# Step 8: predict on test data
y_pred = model.predict(X_test)

print(y_pred)
```

## 8. What `ColumnTransformer` Does

This part:

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)
```

means:

- apply `StandardScaler` to numeric columns
- apply `OneHotEncoder` to categorical columns
- combine the results into one transformed feature table

This is very common in real projects because different columns need different treatment.

## 9. What `Pipeline` Does

This part:

```python
model = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        ("regressor", LinearRegression())
    ]
)
```

means:

1. preprocess the input data
2. train or use the regression model on the transformed data

The nice thing is that we can now call:

```python
model.fit(X_train, y_train)
model.predict(X_test)
```

and scikit-learn handles the preprocessing steps in the correct order.

## 10. When to Use `StandardScaler` vs `MinMaxScaler`

### Use `StandardScaler` when:

- you want a common default choice
- you want features centered around `0`
- you want unit-variance style scaling

### Use `MinMaxScaler` when:

- you want all values in a bounded range
- you want outputs typically between `0` and `1`

Example change:

```python
from sklearn.preprocessing import MinMaxScaler

preprocessor = ColumnTransformer(
    transformers=[
        ("num", MinMaxScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)
```

## 11. Common Beginner Questions

### Do we scale one-hot encoded columns?

Usually we do not need to scale the one-hot output in a beginner linear regression pipeline.

The `0` and `1` values are already on a simple numeric scale.

### Do we always need date columns?

Not always.

Sometimes dates are not useful.

Sometimes they are very useful after being turned into:

- month
- weekday
- elapsed days
- holiday indicators

### Can we keep the raw string date column?

Usually no.

We usually transform it into more meaningful numeric features first.

## 12. A Simpler Manual Version

If you are not ready for `ColumnTransformer` yet, you can still understand the core idea manually:

```python
df["exam_date"] = pd.to_datetime(df["exam_date"])
df["exam_month"] = df["exam_date"].dt.month
df["exam_dayofweek"] = df["exam_date"].dt.dayofweek

df = pd.get_dummies(df, columns=["course_type"])
```

This is useful for learning.

But for repeatable machine learning workflows, the scikit-learn pipeline approach is usually better.

## 13. Common Mistakes

### Mistake 1: Label-encoding categories as random integers

For example:

```python
online = 0
offline = 1
```

This can accidentally suggest an order or distance that may not be meaningful.

For linear regression, one-hot encoding is often the safer beginner choice.

### Mistake 2: Using the full dataset to fit the scaler

This causes data leakage.

The test data should not help decide the training-time scaling values.

### Mistake 3: Keeping the raw date string unchanged

Raw strings are usually not useful input for linear regression.

We usually convert and extract better features first.

## 14. Class Practice

### Practice 1

Take this dataset idea:

- numeric: `hours_studied`
- numeric: `practice_count`
- categorical: `class_mode`
- date: `test_date`

Then:

1. create a DataFrame
2. convert `test_date` with `pd.to_datetime`
3. create at least two date features
4. use `OneHotEncoder` for `class_mode`
5. use `StandardScaler` for numeric columns
6. train a `LinearRegression` pipeline

### Practice 2

Change the preprocessing so that:

- `StandardScaler` becomes `MinMaxScaler`

Then compare:

- predictions
- learned coefficients if you inspect the final model

## 15. Key Takeaways

- categorical columns usually need encoding before linear regression
- `OneHotEncoder` is a common scikit-learn tool for categorical features
- raw dates are often turned into month, weekday, or elapsed-time features
- scaling helps when numeric columns have very different magnitudes
- `ColumnTransformer` lets us preprocess different columns in different ways
- `Pipeline` helps keep preprocessing and model training in one safe workflow
