# Lesson 2: pandas Series and DataFrames
*ML / D01-Dataframe*

This lesson introduces the two most important pandas objects: `Series` and `DataFrame`.

## 1. What Is pandas?

pandas is a Python library for working with tabular data.

It is especially useful when data has:

- named columns
- row labels or indexes
- missing values
- mixed types such as strings and numbers

Import pattern:

```python
import pandas as pd
```

## 2. What Is a Series?

A `Series` is a one-dimensional labeled data structure.

```python
import pandas as pd

scores = pd.Series([88, 92, 79], index=["Alice", "Bob", "Cindy"])
print(scores)
```

Here:

- the values are `88`, `92`, `79`
- the labels are `"Alice"`, `"Bob"`, `"Cindy"`

You can think of a `Series` as:

- one column of data
- plus labels

## 3. What Is a DataFrame?

A `DataFrame` is a two-dimensional table with named columns.

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Cindy"],
    "math": [88, 92, 79],
    "english": [91, 85, 95]
})

print(df)
```

This is the main pandas object we use in data analysis.

## 4. Rows, Columns, and Index

In a DataFrame:

- columns usually describe features
- rows usually describe records
- the index labels the rows

By default, the index starts at `0`.

```python
print(df.index)
print(df.columns)
```

## 5. Creating a DataFrame

One common way is from a dictionary of lists:

```python
df = pd.DataFrame({
    "product": ["pen", "notebook", "eraser"],
    "price": [1.5, 3.0, 0.8],
    "stock": [100, 50, 200]
})
```

Another common way is from a list of dictionaries:

```python
df = pd.DataFrame([
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 92},
    {"name": "Cindy", "score": 79}
])
```

## 6. Looking at the Data

Useful first commands:

```python
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.describe())
```

Meaning:

- `head()` shows the first few rows
- `shape` shows `(rows, columns)`
- `dtypes` shows each column's data type
- `describe()` gives summary statistics for numeric columns

## 7. Selecting Columns

To get one column:

```python
print(df["name"])
```

To get several columns:

```python
print(df[["name", "score"]])
```

Important difference:

- `df["name"]` returns a `Series`
- `df[["name"]]` returns a `DataFrame`

## 8. Adding a New Column

We can create derived columns directly.

```python
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Cindy"],
    "score": [88, 92, 79]
})

df["passed"] = df["score"] >= 80
print(df)
```

We can also combine columns:

```python
df["bonus_score"] = df["score"] + 5
```

## 9. Reading Example: Classroom Table

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Cindy", "David"],
    "math": [88, 92, 79, 95],
    "english": [91, 85, 95, 87]
})

df["average"] = (df["math"] + df["english"]) / 2
df["passed_math"] = df["math"] >= 80

print(df)
print(df[["name", "average"]])
```

## 10. Class Practice

### Practice 1

Create a DataFrame with these columns:

- `city`
- `population`
- `coastal`

Use three rows of your own choice.

Then print:

- the whole DataFrame
- only the `city` column
- only the `city` and `population` columns

### Practice 2

Create a DataFrame:

```python
{
    "student": ["Ann", "Ben", "Cara"],
    "score": [76, 91, 84]
}
```

Add two new columns:

- `passed`, where score is at least `80`
- `score_plus_10`

Then print the result.

## 11. Key Takeaways

- a `Series` is like one labeled column
- a `DataFrame` is like a whole table
- pandas uses column names, which makes code easier to read
- selecting one column gives a `Series`
- derived columns are one of the most common DataFrame operations
