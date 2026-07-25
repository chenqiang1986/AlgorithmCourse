# Lesson 4: Cleaning, GroupBy, and Joining

This lesson introduces three common tasks in practical DataFrame work: fixing missing data, summarizing by category, and combining tables.

## 1. Missing Data

Real datasets often have missing values.

In pandas, missing values may appear as `NaN`.

Example:

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Cindy", "David"],
    "math": [88, None, 79, 95],
    "english": [91, 85, None, 87]
})

print(df)
```

## 2. Detecting Missing Values

```python
print(df.isna())
print(df.isna().sum())
```

Useful ideas:

- `isna()` gives a True/False table
- `isna().sum()` counts missing values in each column

## 3. Filling or Dropping Missing Values

Fill missing values:

```python
df["math"] = df["math"].fillna(df["math"].mean())
df["english"] = df["english"].fillna(0)
```

Drop rows with missing values:

```python
clean_df = df.dropna()
```

Choice depends on the situation:

- sometimes we should fill values
- sometimes we should remove incomplete rows

## 4. Creating Derived Columns

```python
df["average"] = (df["math"] + df["english"]) / 2
df["passed"] = df["average"] >= 80
```

Derived columns help us move from raw data to useful data.

## 5. GroupBy Basics

`groupby` means:

1. split rows into groups
2. compute a summary inside each group
3. combine the results

Example:

```python
import pandas as pd

df = pd.DataFrame({
    "team": ["red", "blue", "red", "blue", "red"],
    "points": [8, 11, 10, 7, 9]
})

print(df.groupby("team")["points"].mean())
```

This computes the average points for each team.

## 6. Grouping by More Than One Summary

```python
summary = df.groupby("team")["points"].agg(["count", "mean", "max"])
print(summary)
```

This is useful when one metric is not enough.

## 7. Grouping a Classroom Table

```python
import pandas as pd

df = pd.DataFrame({
    "student": ["Ann", "Ben", "Cara", "Dan", "Ella"],
    "grade": [10, 10, 11, 11, 10],
    "club": ["music", "robotics", "music", "robotics", "music"],
    "score": [82, 94, 88, 91, 79]
})

print(df.groupby("grade")["score"].mean())
print(df.groupby("club")["score"].agg(["count", "mean", "max"]))
```

Questions to think about:

- Which grade has the higher average score?
- Which club has more students?

## 8. Joining Tables

Sometimes information is split across multiple tables.

Example:

```python
students = pd.DataFrame({
    "student_id": [1, 2, 3],
    "name": ["Ann", "Ben", "Cara"]
})

scores = pd.DataFrame({
    "student_id": [1, 2, 3],
    "math": [82, 94, 88]
})
```

We can join them:

```python
merged = students.merge(scores, on="student_id")
print(merged)
```

This matches rows using the shared key column `student_id`.

## 9. Left Join Example

```python
students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Ann", "Ben", "Cara", "Dan"]
})

scores = pd.DataFrame({
    "student_id": [1, 2, 3],
    "math": [82, 94, 88]
})

merged = students.merge(scores, on="student_id", how="left")
print(merged)
```

This keeps all students, even if one student has no matching score yet.

## 10. Class Practice

### Practice 1

Create a DataFrame with one missing value in a numeric column.

Then:

- count the missing values
- fill the missing value with the column mean

### Practice 2

Create a table of sales:

```python
{
    "store": ["north", "south", "north", "south", "north"],
    "sales": [120, 150, 90, 130, 110]
}
```

Use `groupby` to compute:

- the total sales by store
- the average sales by store
- the maximum sales by store

### Practice 3

Create two small DataFrames:

- one for `student_id` and `name`
- one for `student_id` and `science_score`

Merge them into one table.

## 11. Key Takeaways

- missing data is normal and must be handled carefully
- derived columns help turn raw values into useful features
- `groupby` is one of pandas' most important tools
- `merge` lets us combine related tables through a shared key
