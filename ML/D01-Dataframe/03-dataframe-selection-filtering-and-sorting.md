# Lesson 3: DataFrame Selection, Filtering, and Sorting
*ML / D01-Dataframe*

This lesson focuses on the everyday skills that make DataFrames useful: picking rows, choosing columns, filtering by conditions, and sorting results.

## 1. Why Selection Matters

Real data tables are often much larger than the piece we need.

Typical questions are:

- Which rows match a condition?
- Which columns do we want to show?
- Which records have the highest value?

These are all selection tasks.

## 2. Sample DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Cindy", "David", "Eva"],
    "grade": [10, 10, 11, 11, 10],
    "math": [88, 92, 79, 95, 84],
    "club": ["robotics", "music", "robotics", "sports", "music"]
})
```

## 3. Column Selection

One column:

```python
df["math"]
```

Several columns:

```python
df[["name", "math"]]
```

## 4. Row Selection with `iloc`

`iloc` uses integer position.

```python
df.iloc[0]
df.iloc[0:3]
df.iloc[2, 3]
```

Examples:

- `df.iloc[0]` means the first row
- `df.iloc[0:3]` means rows `0`, `1`, and `2`
- `df.iloc[2, 3]` means one cell at row index `2`, column index `3`

## 5. Row Selection with `loc`

`loc` uses labels.

If we set a custom index:

```python
df = df.set_index("name")
print(df)
```

Then:

```python
df.loc["Alice"]
df.loc["Alice", "math"]
df.loc[["Alice", "Eva"], ["grade", "math"]]
```

Use:

- `iloc` for position
- `loc` for labels

## 6. Boolean Filtering

This is one of the most important pandas skills.

Students with math score at least `90`:

```python
df[df["math"] >= 90]
```

Students in grade `10`:

```python
df[df["grade"] == 10]
```

Students in grade `10` and in music club:

```python
df[(df["grade"] == 10) & (df["club"] == "music")]
```

Important syntax:

- use `&` for and
- use `|` for or
- wrap each condition in parentheses

## 7. Sorting

Sort by one column:

```python
df.sort_values("math")
```

Sort from highest to lowest:

```python
df.sort_values("math", ascending=False)
```

Sort by multiple columns:

```python
df.sort_values(["grade", "math"], ascending=[True, False])
```

That means:

- smaller `grade` first
- within the same grade, larger `math` first

## 8. Resetting the Index

After filtering or sorting, the index may look messy.

```python
top_students = df[df["math"] >= 90].reset_index(drop=True)
print(top_students)
```

This is useful when we want a clean row numbering again.

## 9. Reading Example: Top Robotics Students

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Cindy", "David", "Eva"],
    "grade": [10, 10, 11, 11, 10],
    "math": [88, 92, 79, 95, 84],
    "club": ["robotics", "music", "robotics", "sports", "robotics"]
})

answer = df[
    (df["club"] == "robotics") & (df["math"] >= 80)
][["name", "grade", "math"]].sort_values("math", ascending=False)

print(answer)
```

This code:

1. filters the rows
2. keeps selected columns
3. sorts the final result

That is a very common pandas workflow.

## 10. Class Practice

Use this DataFrame:

```python
import pandas as pd

df = pd.DataFrame({
    "product": ["pen", "notebook", "eraser", "ruler", "marker"],
    "category": ["A", "B", "A", "B", "A"],
    "price": [1.5, 3.2, 0.8, 2.1, 2.7],
    "stock": [100, 50, 200, 80, 40]
})
```

### Practice 1

Select only the `product` and `price` columns.

### Practice 2

Filter all rows where:

- `category` is `"A"`
- `price` is greater than `1.0`

### Practice 3

Sort the table by:

- `stock` from largest to smallest

### Practice 4

Create a new table containing only products with stock less than `90`, then reset the index.

## 11. Key Takeaways

- `df["col"]` selects columns
- `iloc` selects by position
- `loc` selects by labels
- boolean filtering is central to real data analysis
- sorting and filtering are often chained together
