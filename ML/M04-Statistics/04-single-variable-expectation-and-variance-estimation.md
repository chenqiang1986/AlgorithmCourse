# Lesson 4: Estimating the Mean and Variance of One Random Variable
*ML / M04 — Statistics*

## The question

In the last lessons, a distribution was assumed to be known. In practice, we
usually see data first: a sample of delivery times, model errors, or customer
spending amounts. The population distribution that produced those values is
unknown. This lesson develops two of the most useful ways to summarize it:

- the population mean $\mu=E[X]$, estimated by the **sample mean**; and
- the population variance $\sigma^2=\operatorname{Var}(X)$, estimated by the
  **sample variance**.

The distinction matters. A population parameter is a fixed but unknown
property of the data-generating process. An estimator is a rule that turns a
random sample into a number, so its output changes from sample to sample.

## Learning goals

By the end of this lesson, you should be able to:

1. distinguish a parameter, a sample statistic, and an estimator;
2. calculate and interpret the sample mean and sample variance;
3. explain why the usual variance estimator uses $n-1$, not $n$;
4. find the expectation and variance of the sample mean for an i.i.d. sample;
5. use standard error to describe the sampling variability of a mean; and
6. use NumPy or pandas to estimate the center and spread of one feature.

## 1. Population, sample, parameter, and statistic

Suppose a random variable $X$ represents the prediction error (in dollars) on
one future order. Its population mean and variance are

$$
\mu=E[X],
\qquad
\sigma^2=\operatorname{Var}(X).
$$

They describe the distribution of all relevant orders, including orders not
yet observed. We normally do not know their values.

Instead, collect $n$ observations $X_1,\ldots,X_n$. The standard sampling
model is that they are **independent and identically distributed** (i.i.d.):

$$
X_1,\ldots,X_n\overset{\mathrm{i.i.d.}}{\sim}\text{ a distribution with mean
}\mu\text{ and variance }\sigma^2.
$$

The notation emphasizes an important subtlety:

- $X_i$ is random before data are collected;
- $x_i$ is the observed value after collection;
- $\mu$ and $\sigma^2$ are fixed unknown parameters; and
- a statistic is a numerical function of the observed data.

For a sample of observed values $x_1,\ldots,x_n$, a statistic has no unknown
population quantities in its formula.

| Quantity | Symbol | Role |
| --- | --- | --- |
| Population mean | $\mu$ | Fixed, unknown parameter |
| Population variance | $\sigma^2$ | Fixed, unknown parameter |
| Sample mean | $\bar X$ or $\bar x$ | Estimator/statistic for $\mu$ |
| Sample variance | $S^2$ or $s^2$ | Estimator/statistic for $\sigma^2$ |

The i.i.d. assumption is a modeling assumption, not an automatic fact. For
example, repeated measurements from the same customer may be related, and a
time series may have trends or autocorrelation. In those cases, the formulas
below may still be descriptive, but their usual uncertainty interpretation
needs care.

## 2. Estimating expectation with the sample mean

**Definition (Sample mean).** Given observations $x_1,\ldots,x_n$, their
sample mean is

$$
\boxed{\bar x=\frac1n\sum_{i=1}^n x_i.}
$$

Before observation, the corresponding estimator is the random variable

$$
\bar X=\frac1n\sum_{i=1}^n X_i.
$$

It is our default estimator of $\mu=E[X]$. It is simply the average, but it
is also a random variable with its own distribution: collecting another
sample would generally produce another $\bar X$.

**Theorem (Mean and variance of the sample mean).** If
$X_1,\ldots,X_n$ are i.i.d. with $E[X_i]=\mu$ and
$\operatorname{Var}(X_i)=\sigma^2<\infty$, then

$$
E[\bar X]=\mu,
\qquad
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}.
$$

**Proof:**

By linearity of expectation,

$$
E[\bar X]
=E\left[\frac1n\sum_{i=1}^nX_i\right]
=\frac1n\sum_{i=1}^nE[X_i]
=\frac1n(n\mu)=\mu.
$$

Independence makes every covariance between distinct observations zero.
Therefore,

$$
\operatorname{Var}(\bar X)
=\operatorname{Var}\left(\frac1n\sum_{i=1}^nX_i\right)
=\frac1{n^2}\sum_{i=1}^n\operatorname{Var}(X_i)
=\frac{n\sigma^2}{n^2}
=\frac{\sigma^2}{n}.
$$

$\square$

The first result says that $\bar X$ is **unbiased**: over many repeated
samples of size $n$, its average value is the true mean. The second says that
averaging reduces variability. The spread of a sample mean is not
$\sigma^2$; it is $\sigma^2/n$.

**Example (Estimating an average prediction error).** The signed prediction
errors, in dollars, on five randomly selected orders are

$$
-3,\quad 1,\quad 4,\quad -2,\quad 5.
$$

Estimate the population mean signed error.

**Solution:**

The sample mean is

$$
\bar x=\frac{-3+1+4-2+5}{5}=\frac5{5}=1.
$$

The estimate is $1$ dollar. In context, this sample suggests the model tends
to overpredict by about $1$ dollar on average, since the errors were defined
as prediction minus actual value. It does not prove that the population mean
error is exactly $1$.

$\square$

## 3. Estimating variance: why the denominator is $n-1$

If the true population mean $\mu$ were known, the natural average squared
deviation would be

$$
\frac1n\sum_{i=1}^n(X_i-\mu)^2.
$$

Usually $\mu$ is not known, so we replace it with $\bar X$. This makes the
deviations look slightly too small: $\bar X$ was chosen from the same sample
and is the center that minimizes their squared deviations. The correction is
to divide by $n-1$ instead of $n$.

**Definition (Sample variance).** For $n\ge2$, the unbiased sample variance
is

$$
\boxed{S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2.}
$$

After observing a sample, calculate

$$
\boxed{s^2=\frac1{n-1}\sum_{i=1}^n(x_i-\bar x)^2,\qquad
s=\sqrt{s^2}.}
$$

Here $s$ is the **sample standard deviation**. It has the same units as the
data; $s^2$ has squared units.

**Theorem (Bessel's correction).** If $X_1,\ldots,X_n$ are i.i.d. with
variance $\sigma^2$, then

$$
E\left[\frac1n\sum_{i=1}^n(X_i-\bar X)^2\right]
=\frac{n-1}{n}\sigma^2,
$$

and therefore $E[S^2]=\sigma^2$.

**Proof:**

Start with the identity

$$
\sum_{i=1}^n(X_i-\mu)^2
=\sum_{i=1}^n(X_i-\bar X)^2+n(\bar X-\mu)^2.
$$

Taking expectations, the left side is $n\sigma^2$. The final term has
expectation $n\operatorname{Var}(\bar X)=\sigma^2$, because $\bar X$ is
unbiased. Hence

$$
E\left[\sum_{i=1}^n(X_i-\bar X)^2\right]
=n\sigma^2-\sigma^2=(n-1)\sigma^2.
$$

Dividing by $n$ gives the first statement; dividing by $n-1$ gives
$E[S^2]=\sigma^2$.

$\square$

The name **degrees of freedom** is a helpful accounting story. Once $\bar x$
has been computed, the deviations must add to zero:

$$
\sum_{i=1}^n(x_i-\bar x)=0.
$$

Only $n-1$ deviations can vary freely; the last is determined by the others.
That is why the unbiased variance estimator has $n-1$ in its denominator.

**Example (Computing a sample variance).** For the errors
$-3,1,4,-2,5$, estimate the population variance and standard deviation.

**Solution:**

From the preceding example, $\bar x=1$. The squared deviations are

$$
(-3-1)^2=16,\quad(1-1)^2=0,\quad(4-1)^2=9,
\quad(-2-1)^2=9,\quad(5-1)^2=16.
$$

Their sum is $50$, so

$$
s^2=\frac{50}{5-1}=12.5,
\qquad
s=\sqrt{12.5}\approx3.54.
$$

The estimated variance is $12.5$ dollars $^2$ and the estimated standard
deviation is about $3.54$ dollars.

$\square$

### Two denominators you will see in software

The quantity

$$
\frac1n\sum_{i=1}^n(x_i-\bar x)^2
$$

is sometimes called the **empirical variance** or the maximum-likelihood
variance estimate in a Normal model. It is useful in some optimization
settings, but it is biased downward as an estimator of the population
variance. For ordinary descriptive inference from a sample, use $n-1$.

In common Python tools:

- `pandas.Series.var()` and `pandas.Series.std()` use `ddof=1` by default;
- `numpy.var(x)` and `numpy.std(x)` use `ddof=0` by default; and
- `numpy.var(x, ddof=1)` and `numpy.std(x, ddof=1)` give the usual sample
  variance and standard deviation.

Always state the denominator or `ddof` when the distinction matters.

## 4. Standard deviation versus standard error

These quantities answer different questions and should not be interchanged.

| Quantity | Formula | Meaning |
| --- | --- | --- |
| Population standard deviation | $\sigma$ | Typical spread of individual values around $\mu$ |
| Sample standard deviation | $s$ | Estimated spread of individual values in the population |
| Standard error of the mean | $\operatorname{SE}(\bar X)=\sigma/\sqrt n$ | Typical spread of sample means around $\mu$ |
| Estimated standard error | $\widehat{\operatorname{SE}}(\bar X)=s/\sqrt n$ | Estimated uncertainty in the sample mean |

The standard error follows directly from

$$
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}:
\qquad
\operatorname{SD}(\bar X)=\frac{\sigma}{\sqrt n}.
$$

Doubling the sample size does not halve the standard error. To cut it in
half, we need four times as many independent observations. This square-root
relationship is one reason large reductions in uncertainty can be expensive.

**Example (Comparing precision).** A feature has estimated standard deviation
$s=12$ units. Compare the estimated standard error of its mean from samples
of size $25$ and $100$.

**Solution:**

$$
\widehat{\operatorname{SE}}(\bar X)_{n=25}=\frac{12}{\sqrt{25}}=2.4,
\qquad
\widehat{\operatorname{SE}}(\bar X)_{n=100}=\frac{12}{\sqrt{100}}=1.2.
$$

The larger sample has one-half the standard error. It has four times as many
observations, not merely twice as many.

$\square$

## 5. Why averaging works

The **law of large numbers** says that, under suitable conditions,

$$
\bar X\longrightarrow\mu
\quad\text{as }n\to\infty.
$$

In plain language, the average of many independent observations tends to
settle near the population mean. This is not a claim that every large sample
is exact, nor does it repair a biased sampling process. It explains why the
sample mean is a sensible estimator when data are representative and the
observations are effectively independent.

The **central limit theorem** adds a practical approximation: when $n$ is
large enough and no extreme tail dominates,

$$
\frac{\bar X-\mu}{\sigma/\sqrt n}\approx\mathcal N(0,1).
$$

Thus, even if the individual observations are not Normal, the distribution
of their average is often approximately Normal. Later statistical methods,
such as confidence intervals and hypothesis tests, build on this result.

## 6. Estimating one feature in Python

For a one-dimensional NumPy array `x` with missing values already handled:

```python
import numpy as np

x = np.array([-3, 1, 4, -2, 5], dtype=float)

n = x.size
mean_estimate = x.mean()
variance_estimate = x.var(ddof=1)  # divide by n - 1
std_estimate = x.std(ddof=1)
se_mean = std_estimate / np.sqrt(n)

print(mean_estimate)       # 1.0
print(variance_estimate)   # 12.5
print(std_estimate)        # about 3.536
print(se_mean)             # about 1.581
```

For a pandas column, missing values are skipped by default:

```python
summary = {
    "n": df["prediction_error"].count(),
    "mean": df["prediction_error"].mean(),
    "variance": df["prediction_error"].var(),  # ddof=1 by default
    "std": df["prediction_error"].std(),
}
summary["se_mean"] = summary["std"] / np.sqrt(summary["n"])
```

Before interpreting these numbers, inspect the data. A single numerical mean
can conceal skew, outliers, multiple groups, missing-data patterns, or a
change over time. A histogram or a plot by time/group is often the next good
step.

## 7. Common mistakes

1. **Treating $\bar x$ as the true mean.** It is an estimate based on one
   sample, not the population parameter itself.
2. **Using $s$ as the uncertainty of the mean.** Use $s/\sqrt n$ for the
   estimated standard error of $\bar x$.
3. **Forgetting the $n-1$ correction.** When estimating a population variance
   from a sample centered at its own mean, use `ddof=1` unless a different
   convention is explicitly intended.
4. **Assuming more rows always means more independent information.** Repeated,
   clustered, or time-correlated observations can make the standard error
   formula too optimistic.
5. **Ignoring units.** Variance has squared units; standard deviation and
   standard error have the original units.

## Check your understanding

1. A random sample of $16$ battery lifetimes has sample mean $8.4$ hours and
   sample standard deviation $2.0$ hours. What are the estimates of $\mu$,
   $\sigma^2$, and the standard error of the sample mean?
2. A teammate computes `np.var(x)` and reports it as the unbiased estimate of
   a population variance. What one change should they make, and why?
3. Two independent samples are drawn from the same population. One has size
   $50$ and the other size $200$. How do their standard errors compare?
4. Give one realistic reason why $X_1,\ldots,X_n$ might fail to be independent
   in an ML data set.

## Takeaway

For an i.i.d. sample from one random variable, use

$$
\bar X=\frac1n\sum_{i=1}^nX_i
\quad\text{to estimate }\mu,
\qquad
S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2
\quad\text{to estimate }\sigma^2.
$$

The sample mean is unbiased and has variance $\sigma^2/n$. The sample
variance uses $n-1$ because the same data were used to estimate the center.
Finally, distinguish the spread of individual observations ($s$) from the
uncertainty in their average ($s/\sqrt n$).
