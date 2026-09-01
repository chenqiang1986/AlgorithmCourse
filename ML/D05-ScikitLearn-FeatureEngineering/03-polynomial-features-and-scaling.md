# Lesson 3: PolynomialFeatures and Why Scaling Matters
*ML / D05-ScikitLearn-FeatureEngineering*

`PolynomialFeatures` expands a column into powers and interaction terms so a linear model can fit curves, not just straight lines. The one habit many beginners skip — scaling *after* expanding — is exactly what breaks the model. This lesson shows the break, with real numbers.

## 1. What PolynomialFeatures Actually Builds

For a single input $x$ and a chosen `degree` $d$, `PolynomialFeatures(degree=d, include_bias=False)` produces:

$$
x \;\longrightarrow\; x,\; x^2,\; x^3,\; \ldots,\; x^d
$$

With more than one input column it also builds cross-interaction terms (e.g. $x_1 x_2$). `include_bias=False` drops the constant $1$ column, since `LinearRegression` already fits its own intercept.

## 2. Why Raw High-Order Terms Are Dangerous

Say $x$ is a month number, ranging from $1$ to $12$. Then:

$$
x = 12 \;\Rightarrow\; x^5 = 248{,}832
$$

Feed both $x$ (max $12$) and $x^5$ (max $248{,}832$) into the same `LinearRegression` fit, and the model must find coefficients that behave sensibly for a feature near $10$ *and* a feature near $250{,}000$ at the same time. The least-squares math that `LinearRegression` solves becomes ill-conditioned when its input columns sit on wildly different scales — small amounts of noise in the data get amplified into huge, unstable coefficients. That instability is often invisible on training data and shows up as a sudden collapse in test-set accuracy, as Section 5 demonstrates.

## 3. The Fix: Scale After Expanding

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

poly_transformer = make_pipeline(
    PolynomialFeatures(degree, include_bias=False),
    StandardScaler(),
)
```

This is the fit/transform chaining from Lesson 1: `PolynomialFeatures.fit_transform` expands the column into $x, x^2, \ldots, x^d$, and `StandardScaler.fit_transform` then re-centers and rescales every expanded column onto a comparable range. No single power dominates the regression just because it happens to have a bigger raw magnitude.

## 4. Reading Example: Walmart Month → Polynomial

From `practice_ws/1_training_poly.py`:

```python
poly_features = ["Month"]
...
poly_transformer = make_pipeline(
    PolynomialFeatures(3, include_bias=False),
    StandardScaler()
)
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
    ("num", StandardScaler(), numeric_features),
    ("poly", poly_transformer, poly_features),
])
```

`Month` (values `1`–`12`) is expanded to degree `3` and then scaled, all inside one `ColumnTransformer` slot, right next to the ordinary numeric and categorical columns.

## 5. Class Practice: Break It, Then Fix It

### Practice 1 — Break it

Open `practice_ws/1_training_poly.py`. In `poly_transformer`, remove `StandardScaler()` so the transformer is just:

```python
poly_transformer = PolynomialFeatures(3, include_bias=False)
```

Then raise the degree one step at a time — `1`, `2`, `3`, `4`, `5` — rerunning the script each time and recording the printed **Testing Metric** block.

Running this exact experiment gives:

| degree (no scaler) | Test $R^2$ | Test MAPE |
|---|---|---|
| 1 | 0.9237 | 8.47% |
| 2 | 0.9237 | 8.47% |
| 3 | 0.9338 | 7.83% |
| 4 | 0.9342 | 7.84% |
| 5 | **0.7385** | **19.79%** |

The metric holds steady, even improves slightly, through degree `4` — then collapses at degree `5`. Nothing about the underlying data changed; only the input scale did.

### Practice 2 — Fix it

Put `StandardScaler()` back:

```python
poly_transformer = make_pipeline(
    PolynomialFeatures(degree, include_bias=False),
    StandardScaler(),
)
```

Rerun degrees `3` through `6`:

| degree (with scaler) | Test $R^2$ | Test MAPE |
|---|---|---|
| 3 | 0.9338 | 7.83% |
| 4 | 0.9347 | 7.78% |
| 5 | 0.9356 | 7.71% |
| 6 | 0.9376 | 7.64% |

With scaling, raising the degree keeps improving the fit smoothly — no collapse.

### Question to answer

Scaling doesn't change *which* polynomial terms the model is allowed to use, only their magnitude. Why does that alone fix the collapse seen in Practice 1?

## 6. Key Takeaways

- `PolynomialFeatures(degree=d)` expands a column into $x, x^2, \ldots, x^d$ (plus cross terms for multiple columns).
- Raw high-degree terms can have magnitudes many orders larger than the original feature, which destabilizes `LinearRegression`'s fit.
- The instability doesn't show up gradually — it can appear suddenly at a specific degree, as seen going from degree `4` to `5` above.
- Always chain `PolynomialFeatures` into a scaler (`make_pipeline(PolynomialFeatures(...), StandardScaler())`) before raising the degree past `2` or `3`.

Lesson 4 introduces `FourierFeatures` — a transformer built specifically for the kind of repeating, periodic pattern that polynomial terms struggle to approximate without needing dangerously high degrees.
