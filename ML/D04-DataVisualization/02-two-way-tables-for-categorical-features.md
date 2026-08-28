# Lesson 2: Two-Way Tables for Categorical Features
*ML / D04-DataVisualization*

[Lesson 1](./01-visualizing-continuous-data.md) visualized continuous data. This lesson covers **categorical data** — values that come from a fixed set of labels, like `gender`, `department`, or `pass_fail` — and how to summarize the relationship between two categorical features at once.

## 1. Continuous vs. Categorical

- continuous: numeric, can take any value in a range (`price`, `temperature`, `score`)
- categorical: a label from a fixed, usually small, set of possibilities (`"red"`/`"blue"`, `"pass"`/`"fail"`, `"Freshman"`/`"Sophomore"`/`"Junior"`/`"Senior"`)

A histogram or scatter plot does not make sense for a categorical column — there is no meaningful distance between `"red"` and `"blue"`. Categorical data needs its own tools.

## 2. The Two-Way Table Idea

A **two-way table** (also called a contingency table) counts how often each combination of two categorical features occurs.

```text
              Female   Male
  Pass          42       35
  Fail           8       15
```

Each row is a category of one feature (`pass_fail`), each column is a category of the other feature (`gender`), and each cell is the count of rows matching both.

This answers questions a single-column summary cannot: *is the pass rate different for each gender?*

## 3. Building a Two-Way Table with `pd.crosstab`

```python
import pandas as pd

df = pd.DataFrame({
    "gender": ["F", "M", "F", "F", "M", "M", "F", "M"],
    "result": ["Pass", "Pass", "Fail", "Pass", "Fail", "Pass", "Pass", "Pass"]
})

table = pd.crosstab(df["result"], df["gender"])
print(table)
```

Output:

```text
gender  F  M
result
Fail    1  1
Pass    3  3
```

`pd.crosstab(rows, columns)` takes two `Series` and builds the count table automatically — no manual `groupby` needed.

## 4. Normalizing: Counts vs. Proportions

Raw counts are hard to compare when group sizes differ. `normalize` converts counts into proportions.

```python
pd.crosstab(df["result"], df["gender"], normalize="index")   # each row sums to 1
pd.crosstab(df["result"], df["gender"], normalize="columns") # each column sums to 1
pd.crosstab(df["result"], df["gender"], normalize="all")     # whole table sums to 1
```

- `normalize="index"`: within each row, what fraction falls in each column? (e.g., "of students who failed, what fraction are male?")
- `normalize="columns"`: within each column, what fraction falls in each row? (e.g., "of male students, what fraction failed?")

Choosing the right `normalize` direction depends on the question being asked — always state the question first, then pick the axis.

## 5. Two-Way Tables with a Numeric Aggregate

A two-way table does not have to count rows. It can summarize a third, continuous column for each combination.

```python
df = pd.DataFrame({
    "department": ["Sales", "Sales", "Eng", "Eng", "Sales", "Eng"],
    "level": ["Junior", "Senior", "Junior", "Senior", "Senior", "Junior"],
    "salary": [55000, 78000, 62000, 95000, 81000, 65000]
})

table = pd.crosstab(
    df["department"], df["level"],
    values=df["salary"], aggfunc="mean"
)
print(table)
```

This gives the average salary for each `department` x `level` combination. `pivot_table` can do the same thing and is worth knowing as an alternative:

```python
df.pivot_table(index="department", columns="level", values="salary", aggfunc="mean")
```

## 6. Visualizing a Two-Way Table: Stacked and Grouped Bar Charts

A `DataFrame` returned by `crosstab` can be plotted directly with pandas' built-in `.plot`, which calls `matplotlib` underneath.

```python
import pandas as pd
import matplotlib.pyplot as plt

table = pd.crosstab(df["result"], df["gender"])

table.plot(kind="bar", stacked=True, color=["#2f6fed", "#e0563f"])
plt.xlabel("Result")
plt.ylabel("Count")
plt.title("Pass/Fail Counts by Gender")
plt.tight_layout()
plt.show()
```

- `stacked=True` piles the bars on top of each other (total height = total count per row)
- `stacked=False` (the default) places bars for each column side by side, which is easier for comparing exact group sizes

## 7. Visualizing a Two-Way Table: Heatmap

A heatmap colors each cell by its value, which makes patterns in a bigger table easier to spot than reading raw numbers.

```python
import matplotlib.pyplot as plt

table = pd.crosstab(df["department"], df["level"], values=df["salary"], aggfunc="mean")

fig, ax = plt.subplots()
im = ax.imshow(table.values, cmap="Blues")

ax.set_xticks(range(len(table.columns)))
ax.set_xticklabels(table.columns)
ax.set_yticks(range(len(table.index)))
ax.set_yticklabels(table.index)

for i in range(table.shape[0]):
    for j in range(table.shape[1]):
        ax.text(j, i, f"{table.values[i, j]:.0f}", ha="center", va="center", color="black")

fig.colorbar(im)
ax.set_title("Average Salary by Department and Level")
plt.tight_layout()
plt.show()
```

Non-obvious details:

- `ax.imshow` plots a 2D array, so `table.values` (a NumPy array) is passed, not the `DataFrame` itself.
- rows and columns need their tick labels set manually (`set_xticklabels`/`set_yticklabels`) using `table.columns` and `table.index`, since `imshow` has no idea those labels exist.
- the `for i in ... for j in ...` loop writes the actual number on top of each colored cell — without it, the reader can only compare colors, not exact values.

## 8. Reading Example: Full Script

```python
import pandas as pd
import matplotlib.pyplot as plt

survey = pd.DataFrame({
    "team": ["Design", "Design", "Eng", "Eng", "Eng", "Sales", "Sales", "Design"],
    "satisfaction": ["High", "Medium", "High", "High", "Low", "Medium", "High", "High"]
})

# Step 1: build the two-way table
table = pd.crosstab(survey["team"], survey["satisfaction"])
print(table)

# Step 2: visualize as a grouped bar chart
table.plot(kind="bar", stacked=False, figsize=(6, 4))
plt.xlabel("Team")
plt.ylabel("Number of Responses")
plt.title("Satisfaction by Team")
plt.legend(title="Satisfaction")
plt.tight_layout()
plt.show()
```

## 9. Common Mistakes

### 9.1 Confusing counts and proportions

A table of raw counts and a table normalized with `normalize="index"` look similar but answer different questions. Always check which one is being read.

### 9.2 Normalizing on the wrong axis

`normalize="index"` and `normalize="columns"` give different numbers. Picking the wrong one answers a question that was not asked.

### 9.3 Passing a `DataFrame` where `imshow` expects an array

`ax.imshow(table)` may error or behave unexpectedly. Use `ax.imshow(table.values)`.

## 10. Class Practice: Building and Visualizing a Two-Way Table

Use this dataset:

```python
import pandas as pd

df = pd.DataFrame({
    "class": ["A", "A", "B", "B", "A", "B", "A", "B", "A", "B"],
    "device": ["laptop", "phone", "laptop", "laptop", "phone",
               "phone", "laptop", "laptop", "phone", "phone"]
})
```

Tasks:

1. Build a two-way table of `class` (rows) vs. `device` (columns) with `pd.crosstab`.
2. Normalize the table by row (`normalize="index"`). Which class has a higher share of `"phone"` users?
3. Plot the raw-count table as a stacked bar chart.
4. Plot the raw-count table as a heatmap using `imshow`.

## 11. Key Takeaways

- categorical data needs a different summary than continuous data — counts and proportions, not histograms
- `pd.crosstab(rows, columns)` builds a two-way table of counts in one line
- `normalize="index"` / `"columns"` / `"all"` turns counts into proportions along a chosen direction
- `values=` and `aggfunc=` let a two-way table summarize a numeric column instead of counting rows
- a two-way table can be visualized as a stacked/grouped bar chart (`.plot(kind="bar")`) or a heatmap (`ax.imshow`)

The next lesson is a practice set that combines the pandas skills from D01 with everything learned in this module.
