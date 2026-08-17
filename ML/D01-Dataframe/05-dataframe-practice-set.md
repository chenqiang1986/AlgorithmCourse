# Practice Set: NumPy and pandas Coding

This practice set is for writing code, not just reading notes.

You can solve these problems in:

- a Jupyter notebook
- a Python file
- an online Python editor that supports `numpy` and `pandas`

For each problem:

1. create the data exactly as shown
2. write code to answer the task
3. print the final result

## Problem 1: Warm-Up Array Practice

Create this NumPy array:

```python
import numpy as np

arr = np.array([12, 7, 19, 4, 15, 10])
```

Tasks:

- print the second element
- print the last three elements
- print a new array where every value is multiplied by `3`
- print a boolean array showing which values are greater than or equal to `10`
- print the sum and mean of the array

Suggested topics:

- indexing
- slicing
- vectorized arithmetic
- summary functions

## Problem 2: Student Score Table

Create this DataFrame:

```python
import pandas as pd

df = pd.DataFrame({
    "student": ["Amy", "Brian", "Chloe", "Derek", "Eva"],
    "math": [91, 78, 88, 95, 73],
    "english": [84, 81, 90, 89, 76]
})
```

Tasks:

- add a column `average`
- add a column `passed` where average is at least `80`
- print only the columns `student` and `average`
- find all students whose math score is at least `90`

Suggested topics:

- derived columns
- boolean filtering
- column selection

## Problem 3: Product Inventory Filter

Create this DataFrame:

```python
df = pd.DataFrame({
    "product": ["pen", "notebook", "eraser", "marker", "folder", "tape"],
    "category": ["A", "B", "A", "A", "B", "A"],
    "price": [1.5, 3.2, 0.8, 2.7, 2.1, 1.9],
    "stock": [120, 45, 200, 35, 60, 80]
})
```

Tasks:

- filter products in category `"A"`
- from those, keep only products with `price > 1.0`
- sort the result by `stock` from highest to lowest
- print only `product`, `price`, and `stock`

Suggested topics:

- multiple conditions
- sorting
- final column selection

## Problem 4: Missing Value Cleanup

Create this DataFrame:

```python
df = pd.DataFrame({
    "student": ["Amy", "Brian", "Chloe", "Derek"],
    "science": [85, None, 92, 88],
    "history": [78, 81, None, 90]
})
```

Tasks:

- count the missing values in each column
- fill missing `science` values with the mean of the `science` column
- fill missing `history` values with `0`
- add a column `total` equal to `science + history`

Suggested topics:

- `isna`
- `fillna`
- numeric column updates

## Problem 5: Club Score Summary

Create this DataFrame:

```python
df = pd.DataFrame({
    "student": ["Amy", "Brian", "Chloe", "Derek", "Eva", "Felix"],
    "club": ["music", "robotics", "music", "robotics", "music", "robotics"],
    "grade": [10, 10, 11, 11, 10, 11],
    "score": [82, 94, 88, 91, 79, 85]
})
```

Tasks:

- compute the average `score` for each `club`
- compute the number of students in each `club`
- compute `count`, `mean`, and `max` of `score` for each `grade`

Suggested topics:

- `groupby`
- aggregation

## Problem 6: Merge Student Information

Create these two DataFrames:

```python
students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Amy", "Brian", "Chloe", "Derek"]
})

scores = pd.DataFrame({
    "student_id": [1, 2, 4],
    "math": [91, 78, 95]
})
```

Tasks:

- do a left join on `student_id`
- print the merged table
- identify which student has a missing `math` value after the merge

Suggested topics:

- `merge`
- left join
- missing values after combining tables

## Problem 7: Mini Data Challenge

Create this DataFrame:

```python
df = pd.DataFrame({
    "city": ["LA", "SF", "LA", "NY", "SF", "NY", "LA"],
    "month": ["Jan", "Jan", "Feb", "Jan", "Feb", "Feb", "Mar"],
    "sales": [120, 90, 140, 100, 95, 110, 160],
    "returns": [5, 3, 6, 4, 2, 5, 7]
})
```

Tasks:

- add a column `net_sales = sales - returns`
- find the total `net_sales` for each city
- find the row with the largest `net_sales`
- sort the whole table by `net_sales` from largest to smallest

Suggested topics:

- derived columns
- `groupby`
- sorting

## Extension Challenges

If the student finishes early, try these extra tasks:

1. Rewrite one solution using method chaining across multiple lines.
2. For one dataset, make a bar chart of the grouped result.
3. Save one final DataFrame to a CSV file with `to_csv`.

## Reflection Questions

After finishing, the student should be able to answer:

1. When should we use NumPy arrays instead of plain Python lists?
2. What is the difference between a `Series` and a `DataFrame`?
3. What is the difference between `loc` and `iloc`?
4. Why are boolean filters so useful in pandas?
5. Why is `groupby` one of the most powerful DataFrame operations?
