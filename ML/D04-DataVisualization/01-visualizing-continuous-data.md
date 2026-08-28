# Lesson 1: Visualizing Continuous Data with `matplotlib.pyplot`
*ML / D04-DataVisualization*

This lesson introduces `matplotlib.pyplot`, the standard Python plotting library, and shows how to use it to visualize **continuous data** — numeric values that can fall anywhere in a range, like price, temperature, score, or sales.

## 1. Why Visualize Data?

A table of numbers is hard to read at a glance. A plot makes patterns visible immediately:

- Is the data trending up or down?
- Where do most values cluster?
- Are two variables related?
- Are there outliers?

`groupby` and `describe` (from D01) summarize data with numbers. Plots summarize data with shapes.

## 2. What Is `matplotlib.pyplot`?

`matplotlib.pyplot`, usually imported as `plt`, is a module for drawing charts.

```python
import matplotlib.pyplot as plt
```

Every plot in this lesson follows the same basic template:

```python
plt.plot(x, y)        # or plt.hist(...), plt.scatter(...), etc.
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("chart title")
plt.show()
```

`plt.show()` opens the chart window (or renders it inline in a notebook). Forgetting it is the most common beginner mistake — nothing appears without it.

## 3. Line Plots: Trends Over an Order

A line plot connects points in order. It works best when the x-axis has a natural order, such as time, month, or study hours.

```python
import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
exam_scores = [52, 55, 61, 65, 72, 76, 82, 88]

plt.plot(study_hours, exam_scores, marker="o", color="#2f6fed")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Exam Score vs. Study Hours")
plt.show()
```

`marker="o"` draws a dot at each data point on top of the connecting line, which makes individual values easier to read.

## 4. Histograms: Distribution of One Continuous Variable

A histogram groups values into ranges called **bins** and counts how many values fall in each bin. It answers: *where do values cluster?*

```python
import matplotlib.pyplot as plt

scores = [52, 55, 61, 65, 65, 68, 72, 74, 76, 79, 82, 84, 88, 91, 95]

plt.hist(scores, bins=5, color="#2f6fed", edgecolor="white")
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")
plt.title("Distribution of Exam Scores")
plt.show()
```

`bins` controls how many bars are drawn. Too few bins hides structure; too many bins makes the shape noisy. There is no single correct value — try a few.

## 5. Scatter Plots: Relationship Between Two Continuous Variables

A scatter plot draws one point per row, without connecting them. It works best when there is no natural order between points, and we want to see whether two variables move together.

```python
import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
exam_scores = [52, 60, 58, 65, 78, 74, 85, 88]

plt.scatter(study_hours, exam_scores, color="#e0563f")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Exam Score vs. Study Hours")
plt.show()
```

Line plot vs. scatter plot:

- line plot: x-axis has a meaningful order (time, sequence) and we care about the trend
- scatter plot: we care about the relationship between two variables, not a sequence

## 6. Box Plots: Spread and Outliers

A box plot summarizes a distribution using five numbers: minimum, 25th percentile, median, 75th percentile, and maximum. Points far outside that range are drawn as individual dots (outliers).

```python
import matplotlib.pyplot as plt

class_a_scores = [65, 70, 72, 75, 78, 80, 82, 95]
class_b_scores = [55, 60, 63, 66, 68, 70, 72, 74]

plt.boxplot([class_a_scores, class_b_scores], tick_labels=["Class A", "Class B"])
plt.ylabel("Exam Score")
plt.title("Score Spread by Class")
plt.show()
```

Box plots are the fastest way to compare the spread of a continuous variable across a few groups side by side.

## 7. Choosing a Plot Type

| Question being asked | Plot type |
|---|---|
| How does one value change over time or order? | Line plot |
| Where do values cluster? What is the shape of one variable? | Histogram |
| Are two continuous variables related? | Scatter plot |
| How does the spread of a variable compare across groups? | Box plot |

## 8. Reading Example: A Full Script with Subplots

When several plots belong together, `plt.subplots` arranges them in a grid so they can be compared at once.

```python
import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
exam_scores = [52, 55, 61, 65, 72, 76, 82, 88]
class_a_scores = [65, 70, 72, 75, 78, 80, 82, 95]
class_b_scores = [55, 60, 63, 66, 68, 70, 72, 74]

fig, axes = plt.subplots(2, 2, figsize=(9, 7))

axes[0, 0].plot(study_hours, exam_scores, marker="o", color="#2f6fed")
axes[0, 0].set_title("Line Plot")

axes[0, 1].hist(exam_scores, bins=4, color="#2f6fed", edgecolor="white")
axes[0, 1].set_title("Histogram")

axes[1, 0].scatter(study_hours, exam_scores, color="#e0563f")
axes[1, 0].set_title("Scatter Plot")

axes[1, 1].boxplot([class_a_scores, class_b_scores], tick_labels=["A", "B"])
axes[1, 1].set_title("Box Plot")

fig.suptitle("Four Ways to Look at Continuous Data")
fig.tight_layout()
plt.show()
```

Non-obvious details:

- `plt.subplots(2, 2, ...)` returns a `fig` (the whole figure) and `axes`, a 2D array of individual plot areas. Indexing `axes[row, col]` selects one subplot to draw into.
- Each subplot uses `set_title` instead of `plt.title`, because we are setting the title on one `axes` object, not on the whole figure.
- `fig.tight_layout()` prevents titles and labels from overlapping between subplots. Call it right before `plt.show()`.
- `fig.suptitle` sets one title for the entire grid of subplots.

## 9. Common Mistakes

### 9.1 Forgetting `plt.show()`

Without it, the script runs with no visible output (in some environments) or the figure is silently discarded.

### 9.2 Mismatched `x` and `y` lengths

`plt.plot(x, y)` and `plt.scatter(x, y)` both require `x` and `y` to have the same length. A mismatch raises an error.

### 9.3 Using a line plot when there is no meaningful order

If the x-axis is categories or unordered IDs, a line plot draws a misleading "trend" that does not exist. Use a scatter plot or bar chart instead.

### 9.4 Too few or too many histogram bins

A histogram with 2 bins hides the shape of the data. A histogram with 100 bins on a small dataset looks like noise. Try a few bin counts and pick the one that reveals structure without overfitting to individual points.

## 10. Class Practice: Plotting a Small Dataset

Use this dataset:

```python
import pandas as pd

df = pd.DataFrame({
    "day": [1, 2, 3, 4, 5, 6, 7],
    "temperature": [61, 63, 68, 72, 75, 74, 70],
    "ice_cream_sales": [102, 110, 135, 158, 172, 168, 149]
})
```

Tasks:

1. Draw a line plot of `temperature` over `day`.
2. Draw a histogram of `ice_cream_sales` with `bins=4`.
3. Draw a scatter plot of `temperature` (x-axis) vs. `ice_cream_sales` (y-axis). Does it look related?
4. Put all three plots into one figure with `plt.subplots(1, 3, figsize=(12, 4))`.

## 11. Key Takeaways

- `matplotlib.pyplot` (`plt`) is the standard library for drawing charts in Python
- line plots show trends over an ordered axis; scatter plots show relationships between two variables
- histograms show the distribution (shape) of one continuous variable
- box plots compare the spread of a variable across a few groups
- `plt.subplots` arranges multiple plots into one figure for side-by-side comparison

The next lesson covers a different kind of data: categorical features, and how to summarize two of them together in a two-way table.
