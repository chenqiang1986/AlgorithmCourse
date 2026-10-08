# Lesson 3: Continuous Random Variables and Distributions
*ML / M04 — Statistics*

## The question

Some measurements are naturally counts: the number of purchases or the number
of messages received. Others can, at least in principle, take any value in an
interval: a customer's waiting time, a sensor measurement, or the prediction
error of a model. These are modeled by **continuous random variables**.

The ideas from discrete distributions carry over almost unchanged:

- a PMF becomes a **probability density function** (PDF);
- summing probability masses becomes integrating areas;
- expectation remains a weighted average;
- variance remains expected squared distance from the mean; and
- joint distributions, marginals, and independence have the same purpose and
  the same factorization idea.

The important new habit is this: a density is not itself a probability. For a
continuous variable, probability belongs to an interval and is represented by
the area under a density curve.

## Learning goals

By the end of this lesson, you should be able to:

1. distinguish a PDF from a probability and calculate interval probabilities
   as areas or integrals;
2. use a CDF to find continuous probabilities and explain why a single exact
   value has probability zero;
3. calculate expectation and variance of a continuous random variable;
4. find marginal densities from a joint density and test two continuous RVs
   for independence; and
5. recognize the Uniform, Normal, and Exponential distributions and connect
   them to modeling contexts.

## 1. From discrete mass to continuous density

A continuous random variable $X$ is described by a **probability density
function** $f_X$. A valid PDF satisfies

$$
f_X(x)\ge0,
\qquad
\int_{-\infty}^{\infty}f_X(x)\,dx=1.
$$

For any interval $[a,b]$,

$$
\boxed{P(a\le X\le b)=\int_a^b f_X(x)\,dx.}
$$

The integral is the area under the density curve between $a$ and $b$. A PDF
can be greater than $1$; only its total area must equal $1$.

For a continuous random variable,

$$
P(X=c)=\int_c^c f_X(x)\,dx=0.
$$

Therefore, endpoint choices do not matter:

$$
P(a\le X\le b)=P(a<X\le b)=P(a<X<b).
$$

This does not mean that observing an exact measurement is impossible. It
means that any one exact point occupies no width, and therefore has zero area,
in an idealized continuum. Real instruments round measurements, which turns
their recorded values into discrete data.

<svg viewBox="0 0 720 300" width="720" role="img" aria-labelledby="density-title density-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="density-title">Area under a probability density function</title>
  <desc id="density-desc">A smooth density curve with the area between a and b shaded. The probability that X lies between a and b equals the shaded area.</desc>
  <rect width="720" height="300" rx="12" fill="#fffdf8"/>
  <g stroke="#94a3b8" stroke-width="1.5"><path d="M58 245H682"/><path d="M58 245V33"/></g>
  <path d="M93 245 C145 241, 153 224, 185 175 C230 104, 281 57, 363 56 C445 55, 498 101, 542 171 C572 220, 604 240, 652 245" fill="none" stroke="#0f766e" stroke-width="4"/>
  <path d="M233 245 L233 101 C272 68, 312 56, 363 56 C414 56, 459 76, 498 125 L498 245 Z" fill="#99f6e4" opacity="0.85"/>
  <path d="M233 245 L233 101 M498 245 L498 125" stroke="#0f766e" stroke-width="2" stroke-dasharray="5 5"/>
  <g font-family="sans-serif" font-size="16" fill="#334155"><text x="222" y="268">$a$</text><text x="488" y="268">$b$</text><text x="610" y="277">$x$</text><text x="67" y="48">$f_X(x)$</text><text x="310" y="176">$P(a\le X\le b)$</text></g>
</svg>

**Example (A uniform density).** A bus arrives at a uniformly random time
between $0$ and $10$ minutes after the beginning of an observation window.
Let $T$ be its arrival time. Find $P(2\le T\le5)$ and $P(T=4)$.

**Solution:**

The density is

$$
f_T(t)=
\begin{cases}
\frac1{10},&0\le t\le10,\\
0,&\text{otherwise}.
\end{cases}
$$

Thus the interval probability is its length divided by the total length:

$$
P(2\le T\le5)=\int_2^5\frac1{10}\,dt=\frac3{10}.
$$

An individual point has no area, so

$$
P(T=4)=0.
$$

$\square$

## 2. The cumulative distribution function

The CDF definition is exactly the same as for discrete variables:

$$
\boxed{F_X(x)=P(X\le x).}
$$

For a continuous RV with PDF $f_X$,

$$
F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt.
$$

When $f_X$ is continuous, differentiation recovers the density:

$$
f_X(x)=F_X'(x).
$$

The CDF lets us compute an interval probability by subtraction:

$$
\boxed{P(a<X\le b)=F_X(b)-F_X(a).}
$$

The formula mirrors the discrete case. The visual difference is that a
continuous CDF rises smoothly where the density is positive, rather than
jumping at isolated values.

**Example (CDF of a uniform variable).** Let $U\sim\operatorname{Uniform}(0,1)$.
Write its CDF, then find $P(0.2<U<0.7)$.

**Solution:**

Its density is $1$ on $[0,1]$ and $0$ elsewhere, so

$$
F_U(u)=
\begin{cases}
0,&u<0,\\
u,&0\le u\le1,\\
1,&u>1.
\end{cases}
$$

Therefore,

$$
P(0.2<U<0.7)=F_U(0.7)-F_U(0.2)=0.7-0.2=0.5.
$$

$\square$

## 3. Expectation and variance: sums become integrals

For a discrete RV, expectation is $\sum_x xP(X=x)$. For a continuous RV,
replace the sum of values weighted by their masses with an integral weighted
by density:

$$
\boxed{E[X]=\int_{-\infty}^{\infty}x f_X(x)\,dx.}
$$

More generally, the continuous version of the law of the unconscious
statistician is

$$
\boxed{E[g(X)]=\int_{-\infty}^{\infty}g(x)f_X(x)\,dx.}
$$

The variance still measures expected squared distance from the mean:

$$
\boxed{\operatorname{Var}(X)=E[(X-E[X])^2].}
$$

The computational identity is unchanged:

$$
\boxed{\operatorname{Var}(X)=E[X^2]-(E[X])^2.}
$$

All of the transformation rules from Lesson 1 also carry over. For constants
$a$ and $b$,

$$
E[aX+b]=aE[X]+b,
$$

$$
\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X).
$$

**Example (Mean and variance of a uniform variable).** Let
$U\sim\operatorname{Uniform}(0,1)$. Find $E[U]$ and
$\operatorname{Var}(U)$ directly from its density.

**Solution:**

Because $f_U(u)=1$ for $0\le u\le1$,

$$
E[U]=\int_0^1u\,du=\frac12.
$$

Next,

$$
E[U^2]=\int_0^1u^2\,du=\frac13.
$$

Thus

$$
\operatorname{Var}(U)=E[U^2]-(E[U])^2
=\frac13-\left(\frac12\right)^2=\frac1{12}.
$$

$\square$

For a general uniform variable $X\sim\operatorname{Uniform}(a,b)$,

$$
E[X]=\frac{a+b}{2},
$$

$$
\operatorname{Var}(X)=\frac{(b-a)^2}{12}.
$$

## 4. Two common continuous models

### The Normal distribution

A Normal (or Gaussian) distribution models a continuous variable clustered
symmetrically around a center. Write

$$
X\sim\mathcal N(\mu,\sigma^2),
$$

where $\mu$ is the mean and $\sigma^2>0$ is the variance. Its PDF is

$$
f_X(x)=\frac{1}{\sqrt{2\pi\sigma^2}}
\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right).
$$

The bell shape is symmetric about $\mu$, and

$$
E[X]=\mu,
$$

$$
\operatorname{Var}(X)=\sigma^2.
$$

Normal distributions appear as useful approximations when an outcome combines
many small, roughly independent effects. A Normal model is not suitable for a
quantity that cannot be negative when substantial probability would fall below
zero, such as a very small count.

### The Exponential distribution

An Exponential random variable models a nonnegative waiting time to the next
event when events arrive at a constant Poisson rate $\lambda>0$. Write

$$
W\sim\operatorname{Exponential}(\lambda).
$$

Its PDF and CDF are

$$
f_W(w)=\lambda e^{-\lambda w},\qquad w\ge0,
$$

$$
F_W(w)=1-e^{-\lambda w},\qquad w\ge0.
$$

Here the parameter is a rate, so

$$
E[W]=\frac1\lambda,
$$

$$
\operatorname{Var}(W)=\frac1{\lambda^2}.
$$

The rate has reciprocal units: a rate of $3$ arrivals per hour corresponds to
an expected waiting time of $1/3$ hour. This links Lesson 2's Poisson count
model with a continuous waiting-time model.

**Example (Waiting for an arrival).** Requests arrive at a rate of $2$ per
minute. Under a Poisson-process model, let $W$ be the time in minutes until
the next request. Find $P(W>1)$ and $E[W]$.

**Solution:**

The waiting time has distribution

$$
W\sim\operatorname{Exponential}(2).
$$

The probability of waiting more than one minute is

$$
P(W>1)=1-F_W(1)=e^{-2}\approx0.1353.
$$

Its expected waiting time is

$$
E[W]=\frac12\text{ minute}.
$$

$\square$

## 5. Joint densities, marginal densities, and independence

For two continuous RVs $X$ and $Y$, a **joint PDF** $f_{X,Y}(x,y)$ assigns
density across the plane. Its total volume is one:

$$
\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}
f_{X,Y}(x,y)\,dy\,dx=1.
$$

The probability that $(X,Y)$ lies in a region $R$ is the double integral of
the joint density over that region:

$$
P((X,Y)\in R)=\iint_Rf_{X,Y}(x,y)\,dA.
$$

The **marginal PDFs** are found by integrating out the other variable, just
as marginal PMFs were found by summing:

$$
\boxed{f_X(x)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dy,}
$$

$$
\boxed{f_Y(y)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dx.}
$$

**Definition (Independence of continuous random variables).** Continuous RVs
$X$ and $Y$ are independent when their joint density factors at every point:

$$
\boxed{X\perp Y
\quad\Longleftrightarrow\quad
f_{X,Y}(x,y)=f_X(x)f_Y(y).}
$$

This is the continuous analogue of the discrete joint-PMF factorization.
Independence has the same consequences:

$$
E[XY]=E[X]E[Y],
$$

$$
\operatorname{Cov}(X,Y)=0,
$$

and, conversely, zero covariance alone does not prove independence.

**Example (A uniform point in a rectangle).** A point is chosen uniformly
from the rectangle $0\le x\le2$, $0\le y\le3$. Let $X$ and $Y$ be its two
coordinates. Find the marginal PDFs and determine whether $X$ and $Y$ are
independent.

**Solution:**

The rectangle has area $6$, so the joint PDF is

$$
f_{X,Y}(x,y)=\frac16
$$

on the rectangle and $0$ elsewhere. For $0\le x\le2$,

$$
f_X(x)=\int_0^3\frac16\,dy=\frac12.
$$

Similarly, for $0\le y\le3$,

$$
f_Y(y)=\int_0^2\frac16\,dx=\frac13.
$$

Inside the rectangle,

$$
f_X(x)f_Y(y)=\frac12\cdot\frac13=\frac16=f_{X,Y}(x,y).
$$

The product is also zero outside the rectangle, so $X$ and $Y$ are
independent.

$\square$

## 6. What carries over, and what changes

| Idea | Discrete RV | Continuous RV |
|---|---|---|
| Distribution | PMF $p_X(x)=P(X=x)$ | PDF $f_X(x)$; it is a density, not $P(X=x)$ |
| Total probability | $\sum_xp_X(x)=1$ | $\int f_X(x)\,dx=1$ |
| Probability | Add masses | Integrate area |
| Exact value | May have positive probability | $P(X=x)=0$ |
| Expectation | $\sum_xx p_X(x)$ | $\int x f_X(x)\,dx$ |
| Variance | $E[X^2]-(E[X])^2$ | Same identity |
| Independence | $p_{X,Y}=p_Xp_Y$ | $f_{X,Y}=f_Xf_Y$ |

The mathematical operations change from sums to integrals, but the
interpretations of center, spread, co-movement, and independence remain the
same.

## 7. Common pitfalls

1. **A density is not a point probability.** It is possible to have
   $f_X(x)>1$; probabilities are areas, not heights.
2. **Do not assign positive probability to an exact point for a continuous
   model.** Use intervals, even when the interval is very small.
3. **Check units.** A PDF has reciprocal units. If $X$ is in seconds, then
   $f_X(x)$ is in $1/\text{second}$, so an area is unit-free probability.
4. **A Normal model has support on all real numbers.** It can be a poor model
   for strongly bounded, skewed, or nonnegative data.
5. **Independence remains stronger than zero covariance.** The same warning
   from discrete RVs applies to continuous ones.

## Check your understanding

1. Let $X\sim\operatorname{Uniform}(2,8)$. Find $P(3<X<5)$ and $P(X=4)$.
2. A continuous RV has PDF $f(x)=2x$ for $0\le x\le1$ and $0$ elsewhere.
   Verify that this is a valid PDF, then find $P(X\le1/2)$.
3. For the RV in Question 2, calculate $E[X]$, $E[X^2]$, and
   $\operatorname{Var}(X)$.
4. Let $W\sim\operatorname{Exponential}(0.5)$, with time measured in hours.
   Find $P(W>2)$ and $E[W]$.
5. If $X\sim\mathcal N(10,4)$, state its mean and standard deviation. What
   feature of this distribution makes it symmetric?
6. Two continuous RVs have joint density $f_{X,Y}(x,y)=f_X(x)f_Y(y)$. What
   can you conclude about $\operatorname{Cov}(X,Y)$? What can you *not*
   conclude from the reverse statement, $\operatorname{Cov}(X,Y)=0$?

### Answers

1. $P(3<X<5)=(5-3)/(8-2)=1/3$, and $P(X=4)=0$.
2. $\int_0^1 2x\,dx=1$, so it is valid. Also,
   $P(X\le1/2)=\int_0^{1/2}2x\,dx=1/4$.
3. $E[X]=2/3$, $E[X^2]=1/2$, and
   $\operatorname{Var}(X)=1/2-(2/3)^2=1/18$.
4. $P(W>2)=e^{-0.5(2)}=e^{-1}$, and $E[W]=1/0.5=2$ hours.
5. Its mean is $10$ and its standard deviation is $2$. Its PDF is symmetric
   around the mean $10$.
6. $X$ and $Y$ are independent, so $\operatorname{Cov}(X,Y)=0$. Zero
   covariance alone does not prove independence.

## Takeaway

Continuous distributions use densities and integrals, but they answer the
same questions as discrete distributions: where outcomes tend to lie, how
spread out they are, and how variables behave together. Think of a PDF as a
curve whose **area** gives probability. Then expectation, variance, marginals,
and independence become familiar discrete ideas with sums replaced by
integrals.
