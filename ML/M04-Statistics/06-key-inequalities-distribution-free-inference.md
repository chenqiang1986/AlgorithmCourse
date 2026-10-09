# Lesson 6: Key Inequalities — Markov, Chebyshev, and Hoeffding
*ML / M04 — Statistics*

## The question

Lesson 5 made confidence intervals and sample-size plans using a Normal
population, or an approximately Normal sampling distribution. What can we
guarantee when the population distribution is unknown, skewed, or clearly
not Normal? This lesson develops three probability inequalities and uses them
to make conservative confidence intervals and sample-size plans.

Throughout, $X_1,\ldots,X_n$ are independent observations with common mean
$\mu$, and $\bar X=n^{-1}\sum_i X_i$.

## Learning goals

By the end of this lesson, you should be able to select and apply Markov,
Chebyshev, or Hoeffding's inequality; turn a tail bound into a confidence
interval; plan a sample size for a chosen confidence and margin of error; and
explain why distribution-free guarantees trade sharpness for weaker
assumptions.

## 1. The common pattern: bound a bad event

An inequality starts with an event we want to avoid, such as

$$
|\bar X-\mu|\ge E,
$$

where $E>0$ is a tolerable error. If we can show that this bad event has
probability at most $\alpha$, then its complement has probability at least
$1-\alpha$:

$$
P(|\bar X-\mu|<E)\ge1-\alpha.
$$

Equivalently,

$$
P(\bar X-E<\mu<\bar X+E)\ge1-\alpha.
$$

After observing $\bar x$, the interval $[\bar x-E,\bar x+E]$ therefore has
**at least** $1-\alpha$ coverage. Unlike the exact Normal and $t$ statements
in Lesson 5, this is usually a lower bound, not an equality.

## 2. Markov's inequality: a nonnegative quantity

If $Y\ge0$ and $a>0$, then

$$
\boxed{P(Y\ge a)\le\frac{E[Y]}{a}.}
$$

Markov needs only nonnegativity and a finite mean. For example, if a
nonnegative loss has mean loss $E[Y]=4$, then

$$
P(Y\ge20)\le\frac4{20}=0.20.
$$

This is a one-sided guarantee: no matter how oddly distributed $Y$ is, at
least 80% of outcomes are below 20. The bound can be loose, but it cannot be
invalidated by skewness or outliers.

### Markov's bridge to Chebyshev

Start with the simplest case: suppose $X$ has mean $0$ and variance $1$.
Apply Markov to the nonnegative random variable $Y=X^2$. Then

$$
E[Y]=E[X^2]=\operatorname{Var}(X)=1.
$$

Using the threshold $a=k^2$ gives

$$
P(|X|\ge k)
=P(X^2\ge k^2)
\le\frac1{k^2}.
$$

Now let $W$ be any random variable with mean $\mu$ and finite, nonzero
standard deviation $\sigma$. Shift by its mean and divide by its standard
deviation:

$$
R=\frac{W-\mu}{\sigma}.
$$

This normalized variable has mean 0 and variance 1, so the special-case
inequality applies directly:

$$
P\left(\left|\frac{W-\mu}{\sigma}\right|\ge k\right)
=P(|R|\ge k)
\le\frac1{k^2}.
$$

This is Chebyshev's inequality in standardized form. Markov by itself does
not usually give a useful data-centered interval for an unknown mean: it
needs a known expectation of a nonnegative quantity. Its main roles here are
one-sided risk bounds and the idea underlying Chebyshev.

## 3. Chebyshev's inequality: finite variance is enough

The standardized inequality derived above is the form to remember. Unlike
$Z$ or $T$, the normalized variable need not have a named distribution; it
may be skewed or heavy-tailed. To obtain coverage at least $1-\alpha$, set
$1/k^2=\alpha$, so $k=1/\sqrt\alpha$.

### Applying Chebyshev to a sample mean

For an i.i.d. sample, $\bar X$ has mean $\mu$ and variance $\sigma^2/n$.
Apply the same standardized construction with $X$ replaced by $\bar X$ and
with standard deviation $\sigma/\sqrt n$:

$$
R_{\bar X}=\frac{\bar X-\mu}{\sigma/\sqrt n}.
$$

Thus $R_{\bar X}$ has variance 1, so the interval obtained by scaling back
has radius $\sigma/\sqrt{n\alpha}$.

**Example (Chebyshev confidence interval).** An i.i.d. measurement process
has unknown shape and population variance $\sigma^2=100$. For $n=400$, a sample
has $\bar x=52$. Find a guaranteed 95% interval.

**Solution:** First standardize the sample mean to a variable with variance
1:

$$
R_{\bar X}=\frac{\bar X-\mu}{10/\sqrt{400}}
=2(\bar X-\mu).
$$

For 95% coverage, $\alpha=0.05$. Apply Chebyshev to the unit-variance
variable $R_{\bar X}$ and choose $k$ so its tail bound is 0.05:

$$
\begin{aligned}
P(|R_{\bar X}|\ge k)&\le\frac1{k^2}\\
\frac1{k^2}&=0.05\\
k^2&=20\\
k&=\sqrt{20}.
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
P(-\sqrt{20}<R_{\bar X}<\sqrt{20})&\ge0.95\\
P\left(-\sqrt{20}<2(\bar X-\mu)<\sqrt{20}\right)&\ge0.95\\
P(-\sqrt5<\bar X-\mu<\sqrt5)&\ge0.95\\
P(\bar X-\sqrt5<\mu<\bar X+\sqrt5)&\ge0.95.
\end{aligned}
$$

After observing $\bar x=52$, the interval is

$$
\boxed{[52-\sqrt5,\ 52+\sqrt5]=[49.764,\ 54.236].}
$$

It has at least 95% coverage, without assuming a Normal population.

$\square$

### Chebyshev sample-size analysis

For a planned margin $E$, standardize first, then require the desired event
$|\bar X-\mu|<E$. In terms of $R_{\bar X}$, this is

$$
|R_{\bar X}|<\frac{E\sqrt n}{\sigma}.
$$

Chebyshev makes this event have probability at least $1-\alpha$ when

$$
\frac{E\sqrt n}{\sigma}\ge\frac1{\sqrt\alpha}.
$$

Solving this inequality gives $n\ge\sigma^2/(\alpha E^2)$; always round
up.

**Example (Chebyshev sample size).** With population variance $\sigma^2=100$,
how many independent
observations guarantee a 95% interval with margin at most 1?

**Solution:** For a planned sample size $n$, standardize the sample mean:

$$
R_{\bar X}=\frac{\bar X-\mu}{10/\sqrt n}.
$$

The requested margin is 1, so translate $|\bar X-\mu|<1$ into the scale of
$R_{\bar X}$:

$$
\begin{aligned}
|\bar X-\mu|&<1\\
\left|\frac{\bar X-\mu}{10/\sqrt n}\right|&<\frac{\sqrt n}{10}\\
|R_{\bar X}|&<\frac{\sqrt n}{10}.
\end{aligned}
$$

Now apply Chebyshev explicitly with $k=\sqrt n/10$:

$$
\begin{aligned}
P\left(|R_{\bar X}|\ge\frac{\sqrt n}{10}\right)
&\le\frac{1}{(\sqrt n/10)^2}
=\frac{100}{n},\\
P\left(|R_{\bar X}|<\frac{\sqrt n}{10}\right)
&\ge1-\frac{100}{n}.
\end{aligned}
$$

For 95% confidence, require this lower bound to be at least 0.95. Thus

$$
\begin{aligned}
1-\frac{100}{n}&\ge0.95\\
\frac{100}{n}&\le0.05\\
n&\ge2000.
\end{aligned}
$$

Thus $n=2000$ is sufficient. This large number is the price of protecting
against every finite-variance distribution.

## 4. Hoeffding's inequality: use known bounds

Chebyshev's inequality is much weaker than the $z$-based tail probabilities
from Lesson 5. That is the cost of making no assumption about the shape of
the distribution: the bound protects us even against skewed, heavy-tailed
populations with the stated finite variance.

If we know a different kind of information—deterministic bounds on the
random variable—we can obtain a much sharper distribution-free result.
Hoeffding's inequality makes the tail probability decrease **exponentially
in the squared error** (and in the sample size), rather than only like an
inverse square as in Chebyshev.

Suppose each observation is independent and bounded almost surely:

$$
a_i\le X_i\le b_i.
$$

Hoeffding's inequality states

$$
\boxed{P(|\bar X-\mu|\ge E)
\le2\exp\left(-\frac{2n^2E^2}{\sum_{i=1}^n(b_i-a_i)^2}\right).}
$$

To turn this into a memorable standardized form, define a **worst-case
variance proxy** for each observation:

$$
\sigma_i^2=\left(\frac{b_i-a_i}{2}\right)^2.
$$

Indeed, an observation in $[a_i,b_i]$ has variance at most this value. The
maximum occurs when it puts probability $1/2$ at each endpoint. By
independence, define the corresponding worst-case variance proxy for the
sample mean as

$$
\sigma_{\bar X}^2
=\frac{\sum_{i=1}^n\sigma_i^2}{n^2}.
$$

This is an upper bound on $\operatorname{Var}(\bar X)$; it is not a sample
variance estimate. Since

$$
\sum_{i=1}^n(b_i-a_i)^2
=4\sum_{i=1}^n\sigma_i^2
=4n^2\sigma_{\bar X}^2,
$$

Hoeffding's bound can therefore be rewritten as

$$
P(|\bar X-\mu|\ge E)
\le2\exp\left(-\frac{E^2}{2\sigma_{\bar X}^2}\right).
$$

This right-hand side has the same Gaussian-shaped exponential kernel as a
Normal density with variance $\sigma_{\bar X}^2$:

$$
f_{\mathcal N(\mu,\sigma_{\bar X}^2)}(\mu+E)
\propto e^{-E^2/(2\sigma_{\bar X}^2)}.
$$

This resemblance is a useful way to recognize the exponent, but it does
**not** assume that $\bar X$ is Normal or turn the Hoeffding bound into a
Normal tail probability. Hoeffding remains a distribution-free inequality.

> **Memorize this form.** Compute the worst-case variance proxy
> $\sigma_{\bar X}^2$ from the known ranges, then use
>
> $$
> \boxed{P(|\bar X-\mu|\ge E)
> \le2e^{-E^2/(2\sigma_{\bar X}^2)}.}
> $$

No Normal model and no variance estimate are needed; the bounded range does
the work. For confidence at least $1-\alpha$, set the right side to
$\alpha$ and solve:

$$
\boxed{E_{\rm Hoeff}
=\sigma_{\bar X}\sqrt{2\ln(2/\alpha)}.}
$$

So $[\bar x-E_{\rm Hoeff},\bar x+E_{\rm Hoeff}]$ has coverage at least
$1-\alpha$. If it extends beyond a known feasible range $[a,b]$, intersect
it with $[a,b]$; this can only shorten the interval.

When all observations have the same range $R=b-a$,
$\sigma_{\bar X}=R/(2\sqrt n)$. The radius can equivalently be written

$$
E_{\rm Hoeff}=R\sqrt{\frac{\ln(2/\alpha)}{2n}}.
$$

**Example (Hoeffding confidence interval).** A user-rating variable lies in
$[1,5]$. From $n=400$ independent ratings, $\bar x=3.70$. Find a 95%
Hoeffding interval for its population mean.

**Solution:** Every rating has range $5-1=4$, so
$\sigma_i^2=(4/2)^2=4$. Therefore

$$
\sigma_{\bar X}^2=\frac{400(4)}{400^2}=0.01,
\qquad
\sigma_{\bar X}=0.1.
$$

Apply Hoeffding's inequality explicitly:

$$
P(|\bar X-\mu|\ge E)
\le2e^{-E^2/(2(0.1)^2)}.
$$

For 95% coverage, $\alpha=0.05$. Make this upper bound equal to $0.05$
and solve for the margin $E$:

$$
\begin{aligned}
2e^{-E^2/(2(0.1)^2)}&=0.05\\
e^{-E^2/(2(0.1)^2)}&=0.025\\
E^2&=2(0.1)^2\ln40.
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
P\left(|\bar X-\mu|<0.1\sqrt{2\ln40}\right)&\ge0.95\\
P\left(\bar X-0.1\sqrt{2\ln40}<\mu
<\bar X+0.1\sqrt{2\ln40}\right)&\ge0.95.
\end{aligned}
$$

The margin in rating units is

$$
E=\sigma_{\bar X}\sqrt{2\ln40}
=0.1\sqrt{2\ln40}
\approx0.272.
$$

The guaranteed interval is

$$
\boxed{[3.428,\ 3.972].}
$$

$\square$

### Hoeffding sample-size analysis

Suppose all observations lie in a known common range $[a,b]$ of width
$R=b-a$, and the desired margin is $E$. Begin with Hoeffding's inequality:

$$
P(|\bar X-\mu|\ge E)\le2e^{-2nE^2/R^2}.
$$

To make the complementary event have probability at least $1-\alpha$, make
the upper bound on this bad event no larger than $\alpha$:

$$
\begin{aligned}
2e^{-2nE^2/R^2}&\le\alpha\\
e^{-2nE^2/R^2}&\le\frac\alpha2\\
-\frac{2nE^2}{R^2}&\le\ln\left(\frac\alpha2\right)\\
n&\ge\frac{R^2\ln(2/\alpha)}{2E^2}.
\end{aligned}
$$

Always round this result up.

**Example (Hoeffding sample size).** For ratings in $[1,5]$, how many
independent ratings guarantee 95% confidence and margin at most $E=0.25$?

**Solution:** The range width is $R=5-1=4$. Start with Hoeffding's tail
bound at the requested margin:

$$
P(|\bar X-\mu|\ge0.25)
\le2e^{-2n(0.25)^2/4^2}
=2e^{-n/128}.
$$

For 95% confidence, require the right-hand side to be at most 0.05:

$$
\begin{aligned}
2e^{-n/128}&\le0.05\\
e^{-n/128}&\le0.025\\
-\frac n{128}&\le\ln(0.025)\\
n&\ge128\ln40\\
n&\ge472.18.
\end{aligned}
$$

Thus $\boxed{n=473}$ ratings suffice.

## 5. Choosing a method

| Method | Assumptions | Two-sided mean-error bound | Radius for confidence $1-\alpha$ |
| --- | --- | --- | --- |
| Markov | nonnegative variable, finite mean | one-sided: $P(Y\ge a)\le E[Y]/a$ | not generally a data-centered mean interval |
| Chebyshev | independent observations, population variance $\sigma^2$ | $P(|R|\ge k)\le1/k^2$ | $\sigma/\sqrt{n\alpha}$ |
| Hoeffding | independent, $X_i\in[a,b]$ | $2e^{-2nE^2/R^2}$ | $R\sqrt{\ln(2/\alpha)/(2n)}$ |
| $z$ / $t$ (Lesson 5) | Normal model, or CLT approximation; $t$ also needs a reliable estimated standard error | model-based tail probability | critical value $\times$ estimated standard error |

The major advantage of Markov, Chebyshev, and Hoeffding over $z$ or $t$
methods is **robust validity**: their advertised coverage does not depend on
a Normal population or a normal approximation. Hoeffding is particularly
useful for bounded scores, rates, and randomized algorithms, and Chebyshev
works even when only a variance bound is known.

The tradeoff is **conservatism**. The inequalities protect against hostile
distributions allowed by their assumptions, so their intervals and required
sample sizes are often much larger than a well-justified $z$ or $t$ analysis.
They also still require the stated conditions: independence is important for
the sample-mean forms, Chebyshev needs a credible variance bound, and
Hoeffding needs genuine deterministic bounds. A bound inferred only from the
observed minimum and maximum is not a valid Hoeffding range unless the data
source itself enforces it.

## 6. Comparing the same planning question

Suppose observations are in $[0,1]$, the desired margin is $E=0.05$, and
confidence is 95%. Hoeffding requires

$$
n\ge\frac{\ln40}{2(0.05)^2}\approx737.8,
$$

so $n=738$ suffices. Chebyshev with the distribution-free fact
$\sigma^2=\operatorname{Var}(X)\le1/4$ requires

$$
n\ge\frac{1/4}{0.05(0.05)^2}=2000.
$$

Both guarantees hold without a Normal model, but Hoeffding makes more use of
the known bounded range and is sharper here. A $z$ or $t$ plan may be much
smaller, but its nominal confidence is conditional on the modeling or
large-sample approximation being appropriate.

## Check your understanding

1. A nonnegative cost has mean 6. What does Markov say about
   $P(Y\ge30)$?
2. An i.i.d. process has variance at most 16. With $n=400$, what
   Chebyshev margin gives at least 90% confidence?
3. Scores lie in $[0,100]$. What Hoeffding sample size guarantees a 99%
   interval with margin at most 2 points?
4. Why is it invalid to use the smallest and largest values in a sample as
   the Hoeffding endpoints when the population has no known bounds?
5. Give one advantage and one disadvantage of Hoeffding relative to a
   well-justified $t$ interval.

## Takeaway

Turn a bound on $P(|\bar X-\mu|\ge E)$ into an interval by making that bound
no larger than $\alpha$. Markov controls a nonnegative tail, Chebyshev turns
a variance bound into a distribution-free mean guarantee, and Hoeffding
turns known bounded support into an exponential mean-concentration guarantee.
These methods give dependable coverage under weaker assumptions than $z$ and
$t$, but the guarantee is commonly wider and more sample-hungry.
