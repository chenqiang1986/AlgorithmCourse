# Practice Set: Data Visualization

This practice set combines the pandas skills from [D01-Dataframe](../D01-Dataframe) with the plotting skills from this module: [01-visualizing-continuous-data.md](./01-visualizing-continuous-data.md) and [02-two-way-tables-for-categorical-features.md](./02-two-way-tables-for-categorical-features.md).

You can solve these problems in:

- a Jupyter notebook
- a Python file
- an online Python editor that supports `numpy`, `pandas`, and `matplotlib`

For each problem:

1. create the data exactly as shown
2. do any pandas step listed in the tasks
3. draw the requested plot(s) with `matplotlib.pyplot`, including axis labels and a title

## Problem 1: Warm-Up Continuous Plots

Create this DataFrame:

```python
import pandas as pd

df = pd.DataFrame({
    "day": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "temperature": [58, 60, 63, 67, 70, 74, 77, 75, 71, 66],
    "visitors": [80, 95, 110, 140, 165, 200, 230, 210, 175, 130]
})
```

Tasks:

- draw a line plot of `temperature` over `day`
- draw a histogram of `visitors` with `bins=5`
- draw a scatter plot of `temperature` (x-axis) vs. `visitors` (y-axis)
- add a derived column `visitors_per_degree = visitors / temperature`, then draw a line plot of it over `day`

Suggested topics:

- line plots
- histograms
- scatter plots
- derived columns (D01)

## Problem 2: Store Sales Over Time

Create this DataFrame:

```python
df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "store": ["North", "North", "North", "South", "South", "South"],
    "sales": [12000, 13500, 11800, 9800, 10500, 11200]
})
```

Tasks:

- filter the DataFrame to rows where `store == "North"`
- draw a line plot of `sales` over `month` for the North store only
- compute the total `sales` per `store` with `groupby`
- draw a bar chart of the `groupby` result (`.plot(kind="bar")`)

Suggested topics:

- boolean filtering (D01)
- `groupby` (D01)
- line plots
- bar charts

## Problem 3: Pass/Fail by Study Group

Create this DataFrame:

```python
df = pd.DataFrame({
    "study_group": ["A", "B", "A", "A", "B", "B", "A", "B", "A", "B"],
    "result": ["Pass", "Pass", "Fail", "Pass", "Pass",
               "Fail", "Pass", "Pass", "Fail", "Pass"]
})
```

Tasks:

- build a two-way table of `study_group` (rows) vs. `result` (columns) with `pd.crosstab`
- normalize the table by row — which study group has a higher pass rate?
- plot the raw-count table as a stacked bar chart

Suggested topics:

- `pd.crosstab`
- `normalize="index"`
- stacked bar charts

## Problem 4: Product Ratings by Category

Create this DataFrame:

```python
df = pd.DataFrame({
    "category": ["Electronics", "Electronics", "Home", "Home",
                 "Electronics", "Home", "Toys", "Toys", "Toys", "Electronics"],
    "rating": [4, 5, 3, 4, 5, 2, 4, 3, 5, 4]
})
```

Tasks:

- draw a box plot comparing `rating` across the three `category` groups (hint: build one list of ratings per category first)
- compute the average `rating` per `category` with `groupby`
- add a column `above_average` marking whether each row's `rating` is above the overall mean rating

Suggested topics:

- box plots
- `groupby` (D01)
- boolean/derived columns (D01)

## Problem 5: Two-Way Table with a Numeric Aggregate

Create this DataFrame:

```python
df = pd.DataFrame({
    "department": ["Sales", "Sales", "Eng", "Eng", "Eng",
                   "Sales", "Support", "Support", "Eng", "Support"],
    "level": ["Junior", "Senior", "Junior", "Senior", "Senior",
              "Senior", "Junior", "Senior", "Junior", "Junior"],
    "salary": [52000, 78000, 61000, 96000, 91000, 82000, 47000, 60000, 63000, 45000]
})
```

Tasks:

- build a two-way table of average `salary` by `department` (rows) and `level` (columns), using `values="salary", aggfunc="mean"`
- visualize the table as a heatmap with `ax.imshow`, including the numeric value written on each cell
- separately, find the `department` with the highest overall average `salary` using `groupby`

Suggested topics:

- `pd.crosstab` with `values`/`aggfunc`
- heatmaps
- `groupby` (D01)

## Problem 6: Mini Data Challenge

Create this DataFrame:

```python
df = pd.DataFrame({
    "city": ["LA", "SF", "LA", "NY", "SF", "NY", "LA", "SF", "NY", "LA"],
    "plan": ["Basic", "Pro", "Pro", "Basic", "Basic",
             "Pro", "Basic", "Pro", "Pro", "Basic"],
    "monthly_spend": [15, 40, 42, 14, 16, 45, 13, 39, 44, 15]
})
```

Tasks:

- add a column `annual_spend = monthly_spend * 12`
- draw a histogram of `annual_spend`
- build a two-way table of `city` (rows) vs. `plan` (columns) — counts, not an aggregate
- plot that table as a grouped (not stacked) bar chart
- draw a box plot comparing `monthly_spend` across the two `plan` groups

Suggested topics:

- derived columns (D01)
- histograms
- `pd.crosstab`
- grouped bar charts
- box plots

## Extension Challenges

If the student finishes early, try these extra tasks:

1. Put two related plots from the same problem into one figure using `plt.subplots`.
2. For one two-way table, try all three `normalize` options (`"index"`, `"columns"`, `"all"`) and explain in one sentence what question each answers.
3. Save one chart to a file with `plt.savefig("chart.png")` instead of `plt.show()`.

## Reflection Questions

After finishing, the student should be able to answer:

1. When should a line plot be used instead of a scatter plot?
2. What does a histogram show that a single summary number (like the mean) cannot?
3. What is the difference between a two-way table of counts and a two-way table built with `values=`/`aggfunc=`?
4. When would a stacked bar chart be more useful than a grouped bar chart, and vice versa?
5. Why does a heatmap need tick labels and cell text added manually, unlike `df.plot(kind="bar")`?
