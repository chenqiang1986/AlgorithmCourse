# Lesson 1: NumPy Array Basics
*ML / D01-Dataframe*

This lesson introduces NumPy arrays, the idea of shape, and why vectorized operations are the foundation for data work in Python.

## 1. Why Learn NumPy First?

Before working with pandas tables, it helps to understand NumPy.

NumPy gives us:

- fast numerical arrays
- simple slicing rules
- element-wise arithmetic
- built-in summary operations such as `sum`, `mean`, and `max`

Many pandas operations are built on top of NumPy ideas.

## 2. Python List vs NumPy Array

A Python list can store many types of values.

```python
numbers = [3, 5, 8, 13]
```

A NumPy array is designed for structured numerical work.

```python
import numpy as np

arr = np.array([3, 5, 8, 13])
```

With arrays, we can write:

```python
arr + 10
```

Result:

```python
array([13, 15, 18, 23])
```

That is an element-wise operation. Each value gets `10` added to it.

## 3. Shape Matters

The `shape` tells us the size of an array in each dimension.

```python
import numpy as np

scores = np.array([
    [88, 92, 79],
    [95, 85, 91],
    [76, 80, 84]
])

print(scores.shape)
```

Output:

```python
(3, 3)
```

This means:

- `3` rows
- `3` columns

## 4. One-Dimensional and Two-Dimensional Arrays

Example of a 1D array:

```python
temps = np.array([21, 24, 19, 25, 23])
```

Example of a 2D array:

```python
grid = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

You can think of:

- a 1D array as a line of values
- a 2D array as a table of values

## 5. Indexing and Slicing

For a 1D array:

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])      # 10
print(arr[-1])     # 50
print(arr[1:4])    # [20 30 40]
```

For a 2D array:

```python
grid = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(grid[0, 1])    # 2
print(grid[2, 2])    # 9
print(grid[:, 0])    # first column
print(grid[1, :])    # second row
```

Useful patterns:

- `grid[r, c]` means one cell
- `grid[r, :]` means one whole row
- `grid[:, c]` means one whole column

## 6. Vectorized Operations

Suppose all exam scores receive `5` bonus points.

```python
scores = np.array([72, 85, 91, 67])
new_scores = scores + 5
```

Suppose we want percentages:

```python
percentages = scores / 100
```

Suppose we want to check which students passed:

```python
passed = scores >= 70
```

Output:

```python
array([ True,  True,  True, False])
```

This boolean array is very important. pandas uses the same idea for row filtering.

## 7. Common Summary Operations

```python
scores = np.array([72, 85, 91, 67])

print(scores.sum())
print(scores.mean())
print(scores.max())
print(scores.min())
```

For 2D arrays, we can summarize by row or column.

```python
scores = np.array([
    [88, 92, 79],
    [95, 85, 91],
    [76, 80, 84]
])

print(scores.sum(axis=0))   # column sums
print(scores.sum(axis=1))   # row sums
```

Mental model:

- `axis=0` means move down the rows and summarize each column
- `axis=1` means move across the columns and summarize each row

## 8. Reading Example: Student Scores

```python
import numpy as np

scores = np.array([
    [88, 92, 79],
    [95, 85, 91],
    [76, 80, 84]
])

student_totals = scores.sum(axis=1)
subject_averages = scores.mean(axis=0)

print(student_totals)
print(subject_averages)
```

Questions to think about:

- Which row has the highest total?
- Which column has the highest average?

## 9. Class Practice

### Practice 1

Create a NumPy array:

```python
[4, 7, 9, 12, 15]
```

Then print:

- the first value
- the last value
- the slice from index `1` to index `3`
- the array after adding `2` to every element

### Practice 2

Create this 2D array:

```python
[
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

Then print:

- the value at row `1`, column `2`
- the second row
- the third column
- the row sums
- the column sums

## 10. Key Takeaways

- NumPy arrays are the standard structure for numerical data in Python
- array `shape` tells us how data is organized
- slicing and boolean arrays are foundational tools
- vectorized operations let us work on many values at once
- these same ideas will appear again in pandas DataFrames
