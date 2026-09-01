# Lesson 5: Group Interaction Features
*ML / D05-ScikitLearn-FeatureEngineering*

Every model so far has used one shared coefficient per feature across the whole dataset — one `Temperature` coefficient for all 45 Walmart stores, one `Fuel_Price` coefficient for all of them, and so on. But a store in a cold climate might respond to temperature very differently than one in a warm climate. `GroupInteraction` lets the model learn a separate coefficient per feature *per group*, while still being an ordinary linear regression underneath.

## 1. The Idea: One Coefficient Set Per Group

A normal linear regression shares one $\beta_{\text{temp}}$ coefficient across every row, no matter which store it came from:

$$
\hat{y} = \beta_0 + \beta_{\text{temp}} \cdot \text{temp} + \cdots
$$

A store in a cold climate can respond to temperature very differently than one in a warm climate, so forcing every store to share $\beta_{\text{temp}}$ may be inaccurate — the shared value is a compromise that fits neither store well.

Suppose, to start simple, there are only 2 stores, and each should get its own temperature coefficient:

$$
\begin{aligned}
\text{Store 1: } & \hat{y} = \beta_0 + \beta_{\text{temp},1} \cdot \text{temp} + \cdots \qquad (*) \\
\text{Store 2: } & \hat{y} = \beta_0 + \beta_{\text{temp},2} \cdot \text{temp} + \cdots \qquad (**)
\end{aligned}
$$

This pair of separate per-store equations is equivalent to a single equation that carries both coefficients at once, each multiplied by an indicator for its own store:

$$
\hat{y} = \beta_0 + \beta_{\text{temp},1} \cdot [\text{store}=1] \cdot \text{temp} + \beta_{\text{temp},2} \cdot [\text{store}=2] \cdot \text{temp} + \cdots
$$

Check the equivalence by plugging in each store: when $\text{store}=1$, $[\text{store}=1]=1$ and $[\text{store}=2]=0$, so this reduces exactly to $(*)$; when $\text{store}=2$, it reduces exactly to $(**)$. One combined equation, fit once by ordinary least squares, silently behaves like two independent per-store equations.

The key move is what each term is: $[\text{store}=g] \cdot \text{temp}$ isn't two features glued together, it's a single new **composite feature** — a column equal to `temp` on that store's rows and $0$ everywhere else. Generalizing from 2 stores to every group $g$ gives exactly the formula this lesson is built around:

$$
\hat{y} = \beta_0 + \sum_{g \in \text{stores}} \beta_{\text{temp}, g} \cdot [\text{store} = g] \cdot \text{temp} + \cdots
$$

Store $g$'s coefficient $\beta_{\text{temp}, g}$ only affects rows where `store = g`; every other store's rows get $0$ in that column. `LinearRegression` is still solving one ordinary least-squares problem — it just has more composite-feature columns to work with, one block per group.

## 2. Building It: One-Hot Times Numeric

Mechanically, this is an outer product per row: take the one-hot group vector (length = number of groups, a single `1` and the rest `0`) and the numeric feature vector (length = number of numeric features), and multiply every pair. The result has `n_groups * n_features` columns, all zero except the block belonging to that row's own group — exactly what "group × feature interaction" means numerically.

## 3. Reading Example: GroupInteraction

From `ML/lib/group_features.py`:

```python
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder, StandardScaler


class GroupInteraction(BaseEstimator, TransformerMixin):
    def __init__(self, group_col):
        self.group_col = group_col

    def fit(self, X, y=None):
        self.numeric_cols_ = [c for c in X.columns if c != self.group_col]
        self.ohe_ = OneHotEncoder(handle_unknown="ignore")
        self.ohe_.fit(X[[self.group_col]])
        self.scaler_ = StandardScaler()
        self.scaler_.fit(X[self.numeric_cols_])
        return self

    def transform(self, X):
        groups = self.ohe_.transform(X[[self.group_col]]).toarray()  # (n, n_groups)
        nums = self.scaler_.transform(X[self.numeric_cols_])         # (n, n_features)
        # outer product per row -> (n, n_groups * n_features)
        return (groups[:, :, None] * nums[:, None, :]).reshape(len(X), -1)

    def get_feature_names_out(self, input_features=None):
        groups = self.ohe_.categories_[0]
        return [f"{g}_{f}" for g in groups for f in self.numeric_cols_]
```

Notice what `fit` stores: a fitted `OneHotEncoder` for the group column and a fitted `StandardScaler` for the numeric columns — the *same* scaler shared across every group, not a separate scaler per store. Scaling here works exactly as in every earlier lesson; the only new step is the outer-product multiplication inside `transform`, which turns "one shared numeric block" into "one numeric block per group."

`transform` reuses those fitted `ohe_`/`scaler_` objects the same way `FourierFeatures.transform` reuses `period_` in Lesson 2 — nothing is re-learned from whatever data is passed to `transform`.

## 4. Using It in a ColumnTransformer

From `practice_ws/3_training_fourier_group.py`, the plain numeric block from Lesson 4 is swapped out:

```python
# Lesson 4's version:
("num", StandardScaler(), numeric_features),

# This lesson's version:
("group", GroupInteraction("Store"), ["Store"] + numeric_features),
```

`GroupInteraction` needs the `Store` column bundled in with the numeric columns — it has to read the group label itself to know which one-hot slot each row's numeric values belong to.

## 5. Class Practice

### Practice 1 — Trace the ColumnTransformer by hand

Given this tiny dataset (2 stores, 2 numeric features, 4 rows total):

| Row | Store | Temp | Fuel |
|---|---|---|---|
| 1 | A | 40 | 2 |
| 2 | A | 60 | 8 |
| 3 | B | 40 | 8 |
| 4 | B | 60 | 2 |

By hand, work out what `GroupInteraction("Store")` produces when fit and transformed on this data, following the same steps `fit`/`transform` take:

1. One-hot encode `Store` (categories come out alphabetically: `A`, `B`).
2. Standardize `Temp` and `Fuel` using the **shared** scaler fit across all 4 rows (`StandardScaler` uses the population mean/std, i.e. divide by $n$, not $n-1$).
3. Take the outer product of each row's one-hot vector with its standardized numeric vector, in column order `A_Temp, A_Fuel, B_Temp, B_Fuel` (matching `get_feature_names_out`).

Fill in the final $4 \times 4$ output table, then check your answer by running `GroupInteraction("Store").fit_transform(df)` on this same data.

<details>
<summary>Solution</summary>

**Step 1 — standardize.** `Temp` has mean $50$ and population std $10$; `Fuel` has mean $5$ and population std $3$:

| Row | Store | $z_{\text{temp}}$ | $z_{\text{fuel}}$ |
|---|---|---|---|
| 1 | A | $-1$ | $-1$ |
| 2 | A | $+1$ | $+1$ |
| 3 | B | $-1$ | $+1$ |
| 4 | B | $+1$ | $-1$ |

**Step 2 — one-hot `Store`.** Row 1-2 get $[1, 0]$ (A), rows 3-4 get $[0, 1]$ (B).

**Step 3 — outer product.** Multiply each row's one-hot slot into its own standardized values; the other group's columns are forced to $0$:

| Row | `A_Temp` | `A_Fuel` | `B_Temp` | `B_Fuel` |
|---|---|---|---|---|
| 1 | $-1$ | $-1$ | $0$ | $0$ |
| 2 | $+1$ | $+1$ | $0$ | $0$ |
| 3 | $0$ | $0$ | $-1$ | $+1$ |
| 4 | $0$ | $0$ | $+1$ | $-1$ |

Two things worth noticing: rows 1-2 (store A) are exactly $0$ in the `B_*` columns and vice versa — the block structure from Section 2 — and the standardization itself used all 4 rows together, not a per-store mean/std, matching the "shared scaler" point from Section 3.

</details>

### Practice 2 — Measure the gain

Run `practice_ws/3_training_fourier_group.py` as-is and compare its testing metrics to the plain Fourier model from Lesson 4 (`2_training_fourier.py`, no group interaction). Recorded result:

| Model | Test $R^2$ | Test MAPE |
|---|---|---|
| Fourier only (Lesson 4) | 0.9404 | 7.57% |
| Fourier + GroupInteraction("Store") | **0.9453** | **6.52%** |

Letting each store learn its own weather/fuel/CPI sensitivity improves both metrics.

### Practice 3 — The cost of flexibility

`GroupInteraction("Store")` with 45 stores and 5 numeric features produces $45 \times 5 = 225$ columns, replacing the 5 shared columns it stood in for. The dataset has 6,435 rows total across 45 stores — about 143 rows per store, or roughly 114 per store after an 80/20 train split.

Discuss: with only ~114 training rows backing each store's own 5 coefficients, is that enough data to trust each store's individual estimate, or could some of the improvement in Practice 1 come from overfitting to store-specific noise? If you had a coarser grouping available (e.g. a region column covering several stores each), how would trading "fewer, larger groups" for "more, smaller groups" change this trade-off?

## 6. Key Takeaways

- `GroupInteraction` lets the same feature get a different learned coefficient per group, instead of one shared coefficient for every row.
- Mechanically, it's a one-hot(group) × numeric-feature outer product, still fed into an ordinary `LinearRegression`.
- More groups means more parameters — always check how many rows actually back each group before trusting its coefficients.
- `GroupInteraction` composes with everything else in this module: it can sit in the same `ColumnTransformer` next to `FourierFeatures`, `PolynomialFeatures`, and `OneHotEncoder`, because all of them share the same `fit`/`transform` contract from Lesson 1.
