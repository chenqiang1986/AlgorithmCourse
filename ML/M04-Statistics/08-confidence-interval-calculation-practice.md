# Practice Set: Confidence Intervals for Combined Quantities
*ML / M04 — Statistics*

This practice set extends the one-sample confidence intervals from Lesson 5.
Here the target is a **combination** of population means, not one mean by
itself. In every problem, first define a random variable for the quantity of
interest and derive its sampling distribution. Only then choose a critical
value and calculate an interval.

Unless a problem says otherwise, use a 95% confidence level. Show enough work
that another student can see your random-variable definition, standard error,
critical value, and final interval with units.

## 1. Difference in average adult height: known population standard deviations

A public-health researcher takes independent random samples of adult men and
adult women from the same city. Heights are approximately Normally distributed
in both populations. Prior large studies give the population standard
deviations:

$$
\sigma_M=7.2\text{ cm},\qquad \sigma_F=6.4\text{ cm}.
$$

The new samples give:

| Group | Sample size | Sample mean height |
|---|---:|---:|
| Men | $n_M=36$ | $\bar X_M=176.4$ cm |
| Women | $n_F=49$ | $\bar X_F=163.2$ cm |

Estimate the population mean difference $\mu_M-\mu_F$.

1. Define random variables $X_{M,i}$ and $X_{F,j}$, and state the
   distributions of $\bar X_M$ and $\bar X_F$.
2. Derive the distribution of $D=\bar X_M-\bar X_F$. State its mean and
   variance. Explain where independence is used.
3. Standardize $D$ to a standard Normal random variable and derive a 95%
   confidence interval for $\mu_M-\mu_F$.
4. Calculate the interval. Interpret it in context; do not say that 95% of
   individual heights lie in the interval.
5. A classmate reverses the subtraction and reports an interval for
   $\mu_F-\mu_M$. How can their interval be obtained from yours without
   recomputing the standard error?

> **Hint — start with the estimator.** The unknown target is
> $\mu_M-\mu_F$, so use $D=\bar X_M-\bar X_F$. For independent random
> variables, $\operatorname{Var}(A-B)=\operatorname{Var}(A)+\operatorname{Var}(B)$.
> Here the population standard deviations are supplied, so the critical value
> comes from $N(0,1)$ rather than a $t$ distribution.

## 2. Total monthly telecom spending: paired household data

Twelve households report their monthly spending (in dollars) on home internet
and cellphone service. The two entries in a row belong to the **same
household**.

| Household | Internet $I_i$ | Cellphone $C_i$ |
|---:|---:|---:|
| 1 | 54 | 42 |
| 2 | 62 | 39 |
| 3 | 48 | 51 |
| 4 | 71 | 36 |
| 5 | 59 | 45 |
| 6 | 65 | 40 |
| 7 | 52 | 47 |
| 8 | 76 | 34 |
| 9 | 57 | 44 |
| 10 | 68 | 38 |
| 11 | 61 | 41 |
| 12 | 50 | 49 |

Construct a 95% confidence interval for the population mean **total** monthly
telecom spending per household, $\mu_T=E(I+C)$.

1. Define a household-level random variable $T_i=I_i+C_i$. Write
   $E(T_i)$ and $\operatorname{Var}(T_i)$ in terms of the internet and
   cellphone variables. What extra term appears if the two expenses are
   correlated?
2. Create the 12 totals $t_i$, then calculate $\bar t$ and the sample standard
   deviation $s_T$.
3. Under the assumption that household totals are an i.i.d. sample from an
   approximately Normal population with unknown standard deviation, derive the
   statistic whose distribution is $t_{11}$.
4. Use that statistic to calculate the confidence interval for $\mu_T$.
5. Explain why it is valid to add the two amounts **within each row** before
   making a one-sample $t$ interval. Why would it generally be wrong to treat
   the internet column and cellphone column as two independent samples?

> **Hint — make one observation per household.** Your sampled observations
> for this problem are $T_1,\ldots,T_{12}$, not the 24 separate bill amounts.
> Start from
> $$
> \frac{\bar T-\mu_T}{S_T/\sqrt n}\sim t_{n-1}.
> $$
> Do not try to calculate $s_T$ by adding the two sample standard deviations:
> the within-household covariance matters. With the row totals, it is already
> included in $s_T$.

## 3. A paired difference: commute time before and after a bus route change

Eight workers record their one-way commute time in minutes for a typical week
before and after a new express bus route begins. Each worker supplies both
measurements.

| Worker | Before $B_i$ | After $A_i$ |
|---:|---:|---:|
| 1 | 48 | 40 |
| 2 | 55 | 49 |
| 3 | 42 | 39 |
| 4 | 61 | 50 |
| 5 | 50 | 44 |
| 6 | 46 | 42 |
| 7 | 58 | 51 |
| 8 | 53 | 45 |

Estimate the population mean reduction in commute time, $\mu_D=E(B-A)$, with
a 95% confidence interval.

1. Define $D_i=B_i-A_i$. Derive $E(D_i)$ and
   $\operatorname{Var}(D_i)$; include the covariance term.
2. Calculate the eight differences, $\bar d$, and $s_D$.
3. State the distribution of the standardized sample mean when the differences
   are i.i.d. Normal with unknown variance. Give its degrees of freedom.
4. Calculate and interpret the interval. Does an interval entirely above zero
   support a mean reduction?

> **Hint — the pairing changes the problem.** The uncertainty is determined by
> how much each person's difference varies, not by treating the before and
> after columns as unrelated groups. Use one-sample $t$ inference on the
> eight $D_i$ values.

## 4. Independent samples with unknown, unequal variation

Two independent samples of customer support chats are collected from two
different products. The response variable is resolution time in minutes.

| Product | Sample size | Sample mean | Sample standard deviation |
|---|---:|---:|---:|
| A | 18 | 14.6 | 3.1 |
| B | 25 | 12.8 | 4.5 |

The population variances are unknown, and there is no reason to assume they
are equal. Construct an approximate 95% confidence interval for
$\mu_A-\mu_B$ using Welch's method.

1. Define $D=\bar X_A-\bar X_B$ and derive its estimated standard error.
2. Use the Welch--Satterthwaite approximation
   $$
   \nu=
   \frac{(s_A^2/n_A+s_B^2/n_B)^2}
   {(s_A^2/n_A)^2/(n_A-1)+(s_B^2/n_B)^2/(n_B-1)}.
   $$
   Calculate $\nu$ and use the appropriate $t$ critical value (software may
   use the non-integer degrees of freedom directly).
3. Calculate and interpret the interval. What does it mean if zero is inside
   the interval?

> **Hint — distinguish the models.** Unlike Problem 1, $\sigma_A$ and
> $\sigma_B$ are not known. Unlike Problem 3, the observations are not
> paired. The estimated standard error is
> $\sqrt{s_A^2/n_A+s_B^2/n_B}$.

## Brief check values

Use these only after completing your derivations.

- Problem 1: the point estimate is $13.2$ cm and the 95% interval is
  approximately $(10.24,\ 16.16)$ cm.
- Problem 2: the row totals are
  $96,101,99,107,104,105,99,110,101,106,102,99$; $\bar t\approx102.42$ and
  $s_T\approx4.06$ dollars.
- Problem 3: the paired differences are $8,6,3,11,6,4,7,8$ minutes.
- Problem 4: the point estimate is $1.8$ minutes.

## Reflection

For each problem, answer in one or two sentences:

1. What was the one random variable (or estimator) to which you applied the
   confidence-interval machinery?
2. Which dependence assumption was important: independence between groups,
   pairing within a unit, or neither?
3. What quantity does the interval estimate, and what does it *not* describe?
