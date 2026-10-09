# Lesson 5 Homework: Confidence Intervals from Data
*ML / M04 — Statistics*

Use the [Lesson 5 notes](./05-confidence-intervals-z-and-t-tests.md) as a
reference. Reconstruct each calculation from the standardization and tail
probability logic rather than memorizing a separate formula.

## Coding

**Problem (Confidence-interval planner).** You are given a Python list
`data` of observations, assumed to be an i.i.d. sample from a Normal
population with unknown mean and unknown standard deviation. Write three
functions using `scipy.stats.t`:

```python
def confidence_interval(data: list[float], confidence: float) -> tuple[float, float]:
    ...

def confidence_from_margin(data: list[float], margin: float) -> float:
    ...

def required_sample_size(
    data: list[float], confidence: float, margin: float
) -> int:
    ...
```

First calculate the current sample mean $\bar x$, sample standard deviation
$s$ (with `ddof=1`), and sample size $m=len(data)$. Require at least two
observations.

1. `confidence_interval(data, confidence)` returns the two-sided
   $100C\%$ confidence interval for the population mean, where
   $C=\texttt{confidence}$. Use

   $$
   \bar x\pm t_{m-1,\,1-\alpha/2}\frac{s}{\sqrt m},
   \qquad \alpha=1-C.
   $$

2. `confidence_from_margin(data, margin)` returns the confidence level of
   the interval $[\bar x-E,\ \bar x+E]$, where $E$ is `margin`. Start
   from the standardized event

   $$
   \left|\frac{\bar X-\mu}{s/\sqrt m}\right|
   \le\frac{E}{s/\sqrt m}.
   $$

   If $q=E/(s/\sqrt m)$, use the $t_{m-1}$ CDF to compute

   $$
   C=P(|T|\le q)=2F_{t_{m-1}}(q)-1.
   $$

3. `required_sample_size(data, confidence, margin)` returns the estimated
   **total** number of observations needed to achieve the requested
   confidence level and margin of error. Let $C=\texttt{confidence}$ and
   $E=\texttt{margin}$. Hold the current $s$ fixed as a planning estimate of
   the population standard deviation. Starting at $n=m$, find the smallest
   integer $n$ satisfying

   $$
   t_{n-1,\,1-\alpha/2}\frac{s}{\sqrt n}\le E,
   \qquad \alpha=1-C.
   $$

   A simple loop is appropriate because the critical value changes with
   $n$: its degrees of freedom are $n-1$. If the current sample is already
   sufficient, return $m$.

Use `t.ppf(1 - alpha / 2, df=...)` for a critical value and
`t.cdf(value, df=...)` for a CDF value. Validate that the confidence level is
strictly between 0 and 1 and that the margin is positive.

> **Planning caveat.** Part 3 is an estimate, not a guarantee. The current
> $s$ is only an estimate of the unknown population standard deviation, and
> the standard deviation of a future enlarged sample can change. After
> collecting more data, recompute the confidence interval using the new
> sample standard deviation.

Test your functions with:

```python
data = [4.1, 5.6, 6.2, 4.9, 5.4, 7.0, 5.1, 6.4, 5.8, 4.7]
```

## Simulation verification

The next two investigations test the *behavior* of your functions across
many random samples. We control the population in the simulation, so its
true mean and variance are known. Do not replace `rng` with an unseeded
random-number generator: a fixed seed makes your results reproducible.

### 1. Does `confidence_interval` achieve its claimed coverage?

Let

$$
X\sim\mathcal N(50,10^2).
$$

For a fixed confidence level $C=0.95$, generate many independent batches of
size $n=12$. For every batch, call your `confidence_interval` function and
record whether its interval contains the true population mean $\mu=50$.

**Required work:**

1. Complete and run the starter code below.
2. Report the percentage of intervals that contain the true mean.
3. Compare that percentage with 95%. Explain why the percentage need not be
   exactly 95% in one simulation.
4. State which change affects the simulation's Monte-Carlo noise: increasing
   the number of batches or increasing the number of observations per batch.
   Explain briefly.

```python
import numpy as np

rng = np.random.default_rng(2026)
true_mean = 50.0
true_sd = 10.0
confidence = 0.95
batch_size = 12
batches = 20_000

# One row is one independently drawn data set.
samples = rng.normal(
    loc=true_mean,
    scale=true_sd,
    size=(batches, batch_size),
)

# TODO: Apply your function to every row. Each item in `intervals` should be
# a pair (lower, upper). Converting the row to a list matches the function
# signature in this homework.
intervals = [
    confidence_interval(row.tolist(), confidence)
    for row in samples
]

lower = np.array([interval[0] for interval in intervals])
upper = np.array([interval[1] for interval in intervals])

# TODO: Find the fraction and percentage of intervals covering the *known*
# population mean. `contains_true_mean` is a Boolean array.
contains_true_mean = ...
coverage = ...

print(f"Intervals containing true mean: {coverage:.2%}")
print(f"Nominal confidence level:        {confidence:.2%}")
```

The exact $t$ interval has 95% coverage here because the simulated population
is Normal and each interval uses the sample standard deviation. The simulated
percentage is an estimate of that probability. With $B$ batches, its typical
simulation error is roughly

$$
\sqrt{\frac{C(1-C)}{B}}.
$$

Increasing `batches` makes the estimated coverage more stable; changing
`batch_size` instead changes the interval procedure being studied.

### 2. How variable is `required_sample_size`?

The function `required_sample_size` uses a pilot sample's $s$ to estimate an
unknown $\sigma$. That means its output changes from one pilot sample to the
next, even when all pilots come from the same population.

Again let $X\sim\mathcal N(50,10^2)$. Generate many independent pilot samples
of size $m=10$. Use the same target confidence $C=0.95$ and margin of error
$E=3$. Call `required_sample_size` on every pilot, then make a histogram of
the resulting required total sample sizes.

For comparison, imagine that the true standard deviation were known. The
Normal (known-variance) planning calculation would use

$$
\boxed{n_z=\left\lceil
\left(\frac{z_{1-\alpha/2}\sigma}{E}\right)^2
\right\rceil,\qquad \alpha=1-C.}
$$

This is a single fixed benchmark because it uses the true $\sigma=10$ and a
$z$ critical value, rather than a variable pilot estimate $s$ and a $t$
critical value.

**Required work:**

1. Complete and run the starter code below.
2. Submit the histogram. Include a labeled vertical line at the known-variance
   $z$ benchmark $n_z$.
3. Report the minimum, median, and maximum output of
   `required_sample_size`, together with $n_z$.
4. Report the percentage of pilot studies whose estimated required sample size
   is less than $n_z$.
5. In 4–6 sentences, explain why the outputs vary, why they can be either
   smaller or larger than $n_z$, and why the histogram does not mean the true
   required sample size itself is random.

```python
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

rng = np.random.default_rng(2027)
true_mean = 50.0
true_sd = 10.0
confidence = 0.95
margin = 3.0
pilot_size = 10
batches = 2_000

pilots = rng.normal(
    loc=true_mean,
    scale=true_sd,
    size=(batches, pilot_size),
)

# TODO: Call your planning function once per pilot sample. Its output is the
# estimated TOTAL n, not the number of additional observations.
planned_n = np.array([
    required_sample_size(pilot.tolist(), confidence, margin)
    for pilot in pilots
])

# Known-variance Normal benchmark: this uses the true sigma, not an estimate.
alpha = 1 - confidence
z_critical = norm.ppf(1 - alpha / 2)
n_z = math.ceil((z_critical * true_sd / margin) ** 2)

# TODO: Calculate and print the requested summaries.
print("Known-variance z benchmark:", n_z)
print("Minimum planned n:", ...)
print("Median planned n:", ...)
print("Maximum planned n:", ...)
print("% below z benchmark:", ...)

# Integer-centered bins make the count for every possible output readable.
bins = np.arange(planned_n.min() - 0.5, planned_n.max() + 1.5)
plt.hist(planned_n, bins=bins, color="#60a5fa", edgecolor="white")
plt.axvline(
    n_z,
    color="#dc2626",
    linewidth=2,
    label=f"known $\\sigma$, z benchmark = {n_z}",
)
plt.xlabel("Estimated required total sample size")
plt.ylabel("Number of pilot samples")
plt.title("Variation in t-based sample-size plans from pilot samples")
plt.legend()
plt.tight_layout()
plt.show()
```

The benchmark $n_z$ is not a replacement for your t-based function: it is a
comparison point made possible only because the simulation tells us the true
variance. In a real study, we do not know $\sigma$, so the pilot-based plan
must estimate it and should be treated as a planning estimate rather than a
guarantee.
