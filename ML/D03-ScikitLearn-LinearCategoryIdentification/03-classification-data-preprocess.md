# Lesson 3: Data Preprocess for Classification
*ML / D03-ScikitLearn-LinearCategoryIdentification*

This lesson is a deliberate repeat of [D02 Lesson 3](../D02-ScikitLearn-LinearRegression/03-linear-regression-data-preprocess.md).

Preprocessing for classification overlaps heavily with preprocessing for regression: categorical columns, dates, and differently scaled numeric columns are common in both. Going through the same ideas again, this time with a classification target, is intentional repetition to help the pattern stick.

We focus on four cases:

1. some input columns are categorical
2. some input columns are dates
3. some numeric columns have very different magnitudes
4. the **target** itself is a category, which needs its own handling

## 1. Why Preprocessing Matters (Same as Before)

Machine learning models work with numbers.

That means:

- text categories usually need to be encoded
- raw date strings usually need to be transformed into useful numerical features
- numeric columns may need scaling so they are on a more comparable range

For classification specifically, scaling has an extra benefit: `LogisticRegression` uses an iterative solver (see [Lesson 2](./02-logistic-regression-parameters.md#6-max_iter-how-long-the-solver-is-allowed-to-run)), and that solver typically converges faster and more reliably when numeric features are on a similar scale.

## 2. Example Dataset

Suppose we want to predict whether a customer churns.

```python
import pandas as pd

df = pd.DataFrame({
    "tenure_months": [1, 34, 2, 45, 8, 22, 10, 60],
    "monthly_charges": [70.5, 56.9, 89.1, 42.3, 99.9, 60.0, 75.2, 30.1],
    "contract_type": [
        "month-to-month", "one year", "month-to-month", "two year",
        "month-to-month", "one year", "month-to-month", "two year"
    ],
    "signup_date": [
        "2025-01-05", "2022-03-10", "2025-06-01", "2020-11-20",
        "2024-12-01", "2023-04-15", "2024-09-01", "2019-05-30"
    ],
    "churn": ["Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No"]
})
```

Here:

- `tenure_months` is numeric
- `monthly_charges` is numeric, on a different scale than tenure
- `contract_type` is categorical
- `signup_date` is a date string
- `churn` is the **target**, and it is text, not a number

This mirrors the structure of the linear regression example on purpose, so the pattern is recognizable: numeric column, larger-magnitude numeric column, categorical column, date column, target.

## 3. Categorical Input Columns: Same as Regression

Just like in [D02 Lesson 3](../D02-ScikitLearn-LinearRegression/03-linear-regression-data-preprocess.md#3-categorical-data-turn-labels-into-numbers), text categories in the input columns need encoding.

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(handle_unknown="ignore")
```

`contract_type` becomes something like:

```text
contract_type_month-to-month  contract_type_one year  contract_type_two year
1                              0                        0
0                              1                        0
```

`handle_unknown="ignore"` still matters for the same reason: new category values showing up later should not crash the pipeline.

## 4. Dates: Same as Regression

```python
df["signup_date"] = pd.to_datetime(df["signup_date"])

df["signup_year"] = df["signup_date"].dt.year
df["signup_month"] = df["signup_date"].dt.month
df["days_since_start"] = (df["signup_date"] - df["signup_date"].min()).dt.days
```

Same reasoning as before: raw date strings are not useful input directly, but year, month, weekday, or elapsed time can capture real patterns (for example, customers who signed up longer ago may behave differently from very recent signups).

## 5. Different Magnitudes: Same as Regression, With One More Reason to Care

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
```

`tenure_months` (roughly `1` to `70`) and `monthly_charges` (roughly `20` to `120`) are on different scales, exactly like `study_hours` and `practice_questions` were in the regression lesson.

The reasoning from before still applies: unscaled magnitudes can make one feature dominate simply because its numbers are bigger, not because it is more important.

For classification with `LogisticRegression`, there is an additional practical reason: the iterative solver converges faster and is less likely to trigger a convergence warning when features are scaled.

## 6. The Target Is Different: Encoding `y`

This part is new compared with regression.

In regression, the target was already a number (`exam_score`). Here, the target `churn` is text (`"Yes"` / `"No"`).

Most scikit-learn classifiers can actually accept string labels directly:

```python
model.fit(X_train, y_train)  # y_train can be ["Yes", "No", ...]
```

But it is still a very common and useful habit to convert the target into `0`/`1` explicitly, especially for binary classification:

```python
df["churn"] = df["churn"].map({"Yes": 1, "No": 0})
```

Why do this explicitly?

- `predict_proba` output order lines up clearly with `0`/`1` label meaning
- metrics like precision/recall need a clear idea of which class counts as "positive"
- it avoids ambiguity if the labels were something like `"Y"`/`"N"` or `"1"`/`"0"` as text

For a target with more than two categories (softmax case), `LabelEncoder` is a common tool:

```python
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(df["contract_type"])
```

Important distinction:

- `OneHotEncoder` is for **input features**, where category order should not imply rank
- `LabelEncoder` is for the **target**, where scikit-learn just needs consistent integer codes for each class, not a meaningful numeric distance between them

## 7. The Best Habit: Split First, Then Fit Preprocessors on Training Data

Same rule as regression: fit scalers and encoders only on the training data, then apply the same fitted transformation to the test data. Otherwise, information from the test set leaks into training.

```python
1. split into training and test sets
2. fit preprocessors on the training data
3. use the same fitted preprocessors to transform the test data
```

A `Pipeline` is still the easiest safe way to do this.

## 8. Full Example: Preprocess and Train

```python
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.DataFrame({
    "tenure_months": [1, 34, 2, 45, 8, 22, 10, 60],
    "monthly_charges": [70.5, 56.9, 89.1, 42.3, 99.9, 60.0, 75.2, 30.1],
    "contract_type": [
        "month-to-month", "one year", "month-to-month", "two year",
        "month-to-month", "one year", "month-to-month", "two year"
    ],
    "signup_date": [
        "2025-01-05", "2022-03-10", "2025-06-01", "2020-11-20",
        "2024-12-01", "2023-04-15", "2024-09-01", "2019-05-30"
    ],
    "churn": ["Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No"]
})

# Step 1: convert raw dates
df["signup_date"] = pd.to_datetime(df["signup_date"])

# Step 2: create date features
df["signup_month"] = df["signup_date"].dt.month
df["days_since_start"] = (df["signup_date"] - df["signup_date"].min()).dt.days

# Step 3: encode the target explicitly
df["churn"] = df["churn"].map({"Yes": 1, "No": 0})

# Step 4: choose features and target
X = df[[
    "tenure_months",
    "monthly_charges",
    "contract_type",
    "signup_month",
    "days_since_start"
]]
y = df["churn"]

# Step 5: split first, with stratify because churn is often imbalanced
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Step 6: tell sklearn which columns need which preprocessing
numeric_features = ["tenure_months", "monthly_charges", "signup_month", "days_since_start"]
categorical_features = ["contract_type"]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# Step 7: combine preprocessing and model into one pipeline
model = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
    ]
)

# Step 8: fit on training data only
model.fit(X_train, y_train)

# Step 9: predict on test data
y_pred = model.predict(X_test)

print("Predictions:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
```

Notice this is almost identical to the regression pipeline from D02, except:

- the last step is `LogisticRegression` instead of `LinearRegression`
- the target is encoded to `0`/`1` first
- the split uses `stratify=y`
- evaluation uses classification metrics

## 9. `ColumnTransformer` and `Pipeline`: Same Roles as Before

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)
```

Exactly the same idea as regression: apply the right transformation to the right columns, then combine the results.

```python
model = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000))
    ]
)
```

Exactly the same idea as regression: chain preprocessing and the model so `fit`/`predict` handle both steps together, in the correct order, without leaking test data into training.

## 10. A New Wrinkle: Missing or Malformed Values

Real classification datasets, like the Telco Customer Churn dataset used in [Lesson 5](./05-logistic-regression-practice.md), often have a column that looks numeric but is stored as text, sometimes with blank entries.

A common pattern:

```python
df["total_charges"] = pd.to_numeric(df["total_charges"], errors="coerce")
```

`errors="coerce"` turns anything that cannot be converted into a number into `NaN` (missing), instead of crashing.

Once you have real `NaN` values, you need a strategy, such as:

```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")
```

This can be added into the `ColumnTransformer` alongside scaling, and is covered hands-on in the practice project.

## 11. Common Beginner Questions

### Do we one-hot encode the target too?

Not for binary classification. We map it to `0`/`1` directly, or let `LabelEncoder` assign integer codes for a multi-class target. One-hot encoding is for input features, not typically for the target in scikit-learn classifiers.

### Do we scale one-hot encoded columns?

Same answer as regression: usually not needed. `0`/`1` values are already on a simple, comparable scale.

### Why `stratify=y` here but not always mentioned in regression?

Regression targets are continuous, so there is no discrete class balance to preserve. Classification targets can be imbalanced (see [Lesson 5](./05-logistic-regression-practice.md)), so preserving class proportions in the split matters more.

## 12. Common Mistakes

### Mistake 1: Label-encoding an input feature that has no natural order

Same warning as regression: encoding `contract_type` as `0`, `1`, `2` implies an order and distance that may not be meaningful. Prefer one-hot encoding for nominal input categories.

### Mistake 2: Using the full dataset to fit the scaler or imputer

Same data leakage risk as regression: fit only on training data.

### Mistake 3: Leaving the target as text without a clear mapping

If `churn` were coded as `"Y"`/`"N"` in one place and `"Yes"`/`"No"` in another, results become inconsistent. Decide the mapping once, explicitly, near the top of the script.

### Mistake 4: Forgetting that a "numeric-looking" column can hide text

A column like `total_charges` can silently be stored as text if even one row contains a blank string. Always check `df.dtypes` before assuming a column is numeric.

## 13. Class Practice

### Practice 1

Take this dataset idea:

- numeric: `tenure_months`
- numeric: `monthly_charges`
- categorical: `internet_service`
- date: `signup_date`
- target: `churn` (`"Yes"`/`"No"`)

Then:

1. create a DataFrame
2. convert `signup_date` with `pd.to_datetime`
3. create at least two date features
4. map `churn` to `0`/`1`
5. use `OneHotEncoder` for `internet_service`
6. use `StandardScaler` for numeric columns
7. train a `LogisticRegression` pipeline with `stratify=y` in the split

### Practice 2

Take a column of your choice and intentionally insert a few blank string values (`""`). Then:

1. check `df.dtypes` before and after
2. use `pd.to_numeric(..., errors="coerce")` to reveal the missing values
3. add a `SimpleImputer` to the numeric pipeline branch
4. confirm the pipeline still runs end to end

## 14. Key Takeaways

- categorical input columns still need `OneHotEncoder`, exactly like regression
- date columns are still converted into year/month/weekday/elapsed-time features, exactly like regression
- numeric columns with different magnitudes still benefit from scaling, and scaling also helps the logistic regression solver converge
- what's new: the **target** needs its own encoding, usually `0`/`1` for binary classification or `LabelEncoder` for multi-class
- `stratify=y` in `train_test_split` matters more here because classes can be imbalanced
- real-world columns can look numeric but be stored as text; `pd.to_numeric(..., errors="coerce")` plus `SimpleImputer` is a common fix
- `ColumnTransformer` and `Pipeline` still keep everything safe and repeatable, exactly like regression
