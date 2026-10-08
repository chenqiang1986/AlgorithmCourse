# Homework: Estimating the Mean and Variance of One Random Variable
*ML / M04 — Statistics*

Use the [Lesson 4 notes](./04-single-variable-expectation-and-variance-estimation.md)
as a reference. State formulas before substituting numbers. Keep population
parameters ($\mu$, $\sigma^2$) distinct from sample statistics ($\bar x$,
$s^2$), and report units where appropriate.

## 1. Parameters, statistics, and estimators

A company records the delivery times of a random sample of $40$ orders. The
sample mean is $31.2$ minutes and the sample variance is $64\text{ min}^2$.

1. Identify the population random variable in context.
2. State the parameter estimated by $31.2$ and the parameter estimated by
   $64\text{ min}^2$.
3. Is the value $31.2$ a parameter, a statistic, or an estimator? Explain
   carefully, using the distinction between the random variable $\bar X$ and
   its observed value $\bar x$.
4. Find the sample standard deviation and state its units.
5. Find the estimated standard error of the sample mean.

## 2. Estimate the mean and variance by hand

The signed errors (prediction minus actual) for six randomly selected orders,
in dollars, are

$$
-4,\quad -1,\quad 0,\quad 2,\quad 3,\quad 6.
$$

1. Compute the sample mean $\bar x$. Interpret its sign in context.
2. Make a table with columns $x_i$, $x_i-\bar x$, and $(x_i-\bar x)^2$.
3. Verify that the deviations in the middle column add to zero.
4. Compute the sample variance $s^2$ using denominator $n-1$.
5. Compute the sample standard deviation $s$.
6. Compute the estimated standard error $s/\sqrt n$. In one sentence,
   distinguish what $s$ and $s/\sqrt n$ measure.

## 3. The center that minimizes squared deviations

For arbitrary observed values $x_1,\ldots,x_n$, define

$$
Q(a)=\sum_{i=1}^n(x_i-a)^2.
$$

1. Expand $Q(a)$ into a quadratic function of $a$.
2. Differentiate $Q(a)$ and show that its unique minimizing value is
   $a=\bar x$.
3. Explain why using $\bar x$ rather than the unknown $\mu$ tends to make the
   observed squared deviations too small.
4. For the data in Problem 2, calculate both

   $$
   \frac1n\sum_{i=1}^n(x_i-\bar x)^2
   \quad\text{and}\quad
   \frac1{n-1}\sum_{i=1}^n(x_i-\bar x)^2.
   $$

   Which is the usual unbiased estimator of the population variance?

## 4. Sampling variability of a mean

Suppose $X_1,\ldots,X_n$ are i.i.d. with mean $\mu=120$ and standard
deviation $\sigma=18$.

1. Find $E[\bar X]$ and $\operatorname{Var}(\bar X)$ for $n=9$.
2. Find the standard error of $\bar X$ for $n=9$.
3. Repeat parts 1 and 2 for $n=36$.
4. By what factor did the sample size increase? By what factor did the
   standard error decrease?
5. How large must $n$ be for the standard error to be at most $1.5$? Show the
   inequality you solve.

## 5. Reading a software summary

The following code summarizes a NumPy array `x` of $12$ measurements:

```python
mean = x.mean()
variance = x.var()
std = x.std()
se = std / np.sqrt(x.size)
```

1. What denominator does `x.var()` use by default?
2. Write corrected code that estimates the population variance with Bessel's
   correction and then computes the matching sample standard deviation and
   estimated standard error.
3. If the original code reports `variance = 20`, what variance would the
   corrected code report for this same data set? Do not rerun the code; use
   the relationship between the two denominators.
4. Why is `mean` unchanged by this correction?

## 6. When the i.i.d. model is doubtful

For each scenario, identify whether independence, identical distribution, or
both are questionable. Then state briefly how the issue could make the usual
standard-error interpretation misleading.

1. A data set contains one row for every purchase made by the same $200$
   customers over a year.
2. A sensor records outdoor temperature once per minute for a month.
3. An analyst combines observations from weekday lunch orders and weekend
   dinner orders, then treats all order values as coming from one population.
4. A survey samples one student from each of $100$ unrelated schools using the
   same random procedure at each school.

## 7. Coding investigation — visualize variance-estimator bias

This exercise uses a population we control, so its true variance is known.
Let

$$
X\sim\mathcal N(50,10^2).
$$

The population standard deviation is $\sigma=10$ and the population variance
is $\sigma^2=100$. Repeatedly draw independent batches of $n=5$ observations.
For every batch, calculate:

$$
v_n=\frac1n\sum_{i=1}^n(x_i-\bar x)^2,
\qquad
v_{n-1}=\frac1{n-1}\sum_{i=1}^n(x_i-\bar x)^2.
$$

### Required work

1. Complete and run the starter code below. Use the supplied seed so that
   your numerical output is reproducible.
2. Report the average of `var_n` and the average of `var_n_minus_1`. Compare
   each with the true variance $100$.
3. Report the percentage of batches for which `sd_n` is smaller than the true
   standard deviation $10$, and the percentage for which `sd_n_minus_1` is
   smaller than $10$.
4. Submit the figure with both histograms. Each plot must include a vertical
   line at the true variance and a descriptive title.
5. In 3–5 sentences, explain what in your output demonstrates the bias caused
   by using $n$ as the denominator. Explain separately what the percentages
   of sample standard deviations do and do not establish.
6. Change `n` from $5$ to $30$, rerun the simulation, and compare the two
   figures and summaries. What changes? What remains true?

```python
import numpy as np
import matplotlib.pyplot as plt

# A fixed seed makes your results reproducible.
rng = np.random.default_rng(2026)

true_mean = 50
true_sd = 10
true_variance = true_sd**2
n = 5
batches = 20_000

# Shape: one row per independently drawn batch, one column per observation.
samples = rng.normal(loc=true_mean, scale=true_sd, size=(batches, n))

# TODO: Compute one variance estimate for every row. `axis=1` means
# "calculate across each batch." Use both ddof=0 and ddof=1.
var_n = ...
var_n_minus_1 = ...

# TODO: Compute the corresponding sample standard deviations.
sd_n = ...
sd_n_minus_1 = ...

# TODO: Print the two average variance estimates. The theoretical expected
# values are (n - 1) / n * true_variance and true_variance, respectively.
print("Average variance, denominator n:", ...)
print("Average variance, denominator n - 1:", ...)

# TODO: Print the requested percentages. `np.mean(condition)` is the fraction
# of True values, so multiply by 100 to obtain a percentage.
print("% of batches with sd_n < true_sd:", ...)
print("% of batches with sd_n_minus_1 < true_sd:", ...)

# TODO: Make two side-by-side histograms. Use the same bins and x-limits so
# the two estimator distributions can be compared fairly.
fig, axes = plt.subplots(1, 2, figsize=(13, 4), sharey=True)
bins = np.linspace(0, 350, 51)

for ax, estimates, title in [
    (axes[0], var_n, "Variance estimates: denominator n"),
    (axes[1], var_n_minus_1, "Variance estimates: denominator n - 1"),
]:
    ax.hist(estimates, bins=bins, color="steelblue", edgecolor="white")
    ax.axvline(true_variance, color="crimson", linewidth=2,
               label="true variance = 100")
    ax.set_title(title)
    ax.set_xlabel("estimated variance")
    ax.legend()

axes[0].set_ylabel("number of batches")
fig.suptitle(f"{batches:,} samples of size n = {n}")
fig.tight_layout()
plt.show()
```

**Important interpretation note:** The average of `var_n_minus_1` estimates
the true **variance** without bias under this model. Its square root,
`sd_n_minus_1`, is still not exactly an unbiased estimator of the population
standard deviation for small samples. The requested percentages describe how
often an individual batch lands below $10$; they are not, by themselves, the
definition or proof of estimator bias.

## Challenge — prove the denominator-$n$ bias

Let

$$
V_n=\frac1n\sum_{i=1}^n(X_i-\bar X)^2
$$

for an i.i.d. sample with variance $\sigma^2$.

1. Use the identity

   $$
   \sum_{i=1}^n(X_i-\mu)^2
   =\sum_{i=1}^n(X_i-\bar X)^2+n(\bar X-\mu)^2
   $$

   and $\operatorname{Var}(\bar X)=\sigma^2/n$ to show that

   $$
   E[V_n]=\frac{n-1}{n}\sigma^2.
   $$

2. State the bias $E[V_n]-\sigma^2$.
3. Show that the relative bias, expressed as a fraction of $\sigma^2$, is
   $-1/n$. Interpret why the bias becomes less important as $n$ grows.
