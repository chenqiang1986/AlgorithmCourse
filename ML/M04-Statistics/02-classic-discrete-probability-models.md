# Lesson 2: Classic Discrete Probability Models — Bernoulli, Binomial, and Poisson
*ML / M04 — Statistics*

## The question

Many data sets contain counts: whether a visitor clicked, how many purchases
were made, or how many support tickets arrived in an hour. The three models in
this lesson turn common data-generating stories into distributions:

- **Bernoulli:** one yes/no trial;
- **Binomial:** the number of successes in a fixed number of independent
  yes/no trials; and
- **Poisson:** the number of events in a fixed interval when events arrive at
  a stable average rate.

The point is not to memorize three formulas. It is to connect a random
variable's meaning to its assumptions, then use its expectation and variance
to describe the typical count and its natural variability.

## Learning goals

By the end of this lesson, you should be able to:

1. recognize when a Bernoulli, Binomial, or Poisson model is appropriate;
2. write and use each model's PMF, support, parameters, expectation, and
   variance;
3. derive the mean and variance of a Binomial random variable from indicator
   variables;
4. explain why a Poisson model has equal mean and variance; and
5. distinguish a fixed-number-of-trials Binomial setting from a
   fixed-time-or-space Poisson setting.

## 1. One trial: the Bernoulli model

**Definition (Bernoulli random variable).** A random variable $X$ has a
Bernoulli distribution with success probability $p$, written

$$
X\sim\operatorname{Bernoulli}(p),\qquad 0\le p\le1,
$$

when it records one trial as

$$
X=
\begin{cases}
1,&\text{success},\\
0,&\text{failure}.
\end{cases}
$$

Its PMF is

$$
P(X=x)=p^x(1-p)^{1-x},\qquad x\in\{0,1\}.
$$

Thus $P(X=1)=p$ and $P(X=0)=1-p$. The labels “success” and “failure” do not
mean good and bad; they identify the outcome being counted. For example,
“a transaction is fraudulent” can be called success when it is the event of
interest.

Because a Bernoulli variable is an indicator, $X^k=X$ for every positive
integer $k$. In particular,

$$
\begin{aligned}
E[X]&=p,\\
E[X^2]&=p,\\
\operatorname{Var}(X)&=p(1-p).
\end{aligned}
$$

The mean $p$ is the long-run fraction of successes. The variance is largest
at $p=1/2$ and is $0$ when the outcome is certain ($p=0$ or $p=1$).

**Example (A click indicator).** A displayed advertisement is clicked with
probability $p=0.03$. Let $C=1$ if it is clicked and $C=0$ otherwise. Find
the probability of no click, the expected value, and the variance of $C$.

**Solution:**

Here $C\sim\operatorname{Bernoulli}(0.03)$. Therefore

$$
P(C=0)=1-0.03=0.97,
$$

and

$$
E[C]=0.03,
\qquad
\operatorname{Var}(C)=0.03(0.97)=0.0291.
$$

An expectation of $0.03$ does not say that one display produces a fractional
click. Across many comparable displays, it says that about $3\%$ are clicked.

$\square$

## 2. A fixed number of trials: the Binomial model

Suppose we repeat the same Bernoulli trial $n$ times. Let $X_i$ equal $1$ if
trial $i$ succeeds and $0$ otherwise. If the trials are independent and each
has the same success probability $p$, then the total number of successes is

$$
S=X_1+X_2+\cdots+X_n.
$$

**Definition (Binomial random variable).** The count $S$ above has a Binomial
distribution with parameters $n$ and $p$, written

$$
\boxed{S\sim\operatorname{Binomial}(n,p).}
$$

The model requires all four conditions below.

1. There are a fixed number $n$ of trials.
2. Each trial has two outcomes after a success category is chosen.
3. Each trial has the same success probability $p$.
4. The trials are independent.

Its support is $0,1,\ldots,n$, and its PMF is

$$
\boxed{P(S=k)=\binom nk p^k(1-p)^{n-k},\qquad k=0,1,\ldots,n.}
$$

To understand the formula, first select which $k$ of the $n$ trials succeed;
there are $\binom nk$ choices. Each particular success/failure pattern has
probability $p^k(1-p)^{n-k}$ by independence. These patterns are disjoint, so
their probabilities add.

### Mean and variance of a Binomial count

**Theorem (Binomial expectation and variance).** If
$S\sim\operatorname{Binomial}(n,p)$, then

$$
\boxed{E[S]=np,\qquad\operatorname{Var}(S)=np(1-p).}
$$

**Proof:**

Write $S=\sum_{i=1}^n X_i$, where the $X_i$ are independent
$\operatorname{Bernoulli}(p)$ variables. By linearity of expectation,

$$
E[S]=\sum_{i=1}^n E[X_i]=\sum_{i=1}^n p=np.
$$

Independence makes the covariance between distinct indicators zero. Hence

$$
\operatorname{Var}(S)
=\sum_{i=1}^n\operatorname{Var}(X_i)
=\sum_{i=1}^n p(1-p)
=np(1-p).
$$

$\square$

The mean $np$ is a count: in $n$ opportunities, expect $n$ times the
per-opportunity success rate. The standard deviation is
$\sqrt{np(1-p)}$, the typical scale on which the realized count differs from
that mean.

**Example (Five sales among twenty contacts).** Each of $20$ independently
contacted customers purchases with probability $0.25$. Let $S$ be the number
who purchase. Find $P(S=5)$, $E[S]$, and $\operatorname{Var}(S)$.

**Solution:**

The conditions give $S\sim\operatorname{Binomial}(20,0.25)$. Thus

$$
\begin{aligned}
P(S=5)
&=\binom{20}{5}(0.25)^5(0.75)^{15}\\
&\approx0.2023.
\end{aligned}
$$

The expected number of purchasers and its variance are

$$
E[S]=20(0.25)=5,
\qquad
\operatorname{Var}(S)=20(0.25)(0.75)=3.75.
$$

The expected count happens to equal $5$, but the probability of exactly five
purchases is only about $20\%$; expectation describes the center, not the
most certain outcome.

$\square$

## 3. Events in an interval: the Poisson model

Use a Poisson model when the variable counts events in a fixed interval of
time, area, distance, volume, or other exposure. Let $\lambda>0$ be the
expected number of events in that interval.

**Definition (Poisson random variable).** A random variable $N$ is Poisson
with rate (or mean) $\lambda$, written

$$
N\sim\operatorname{Poisson}(\lambda),
$$

if its PMF is

$$
\boxed{P(N=k)=e^{-\lambda}\frac{\lambda^k}{k!},
\qquad k=0,1,2,\ldots.}
$$

For an event-arrival interpretation, the model assumes a stable average rate,
events occurring independently in nonoverlapping intervals, and an extremely
small chance of two or more events in a sufficiently tiny interval. These are
modeling approximations, not automatic facts about every count.

The parameter has a direct interpretation:

$$
\boxed{E[N]=\lambda,\qquad\operatorname{Var}(N)=\lambda.}
$$

The equality of mean and variance is a hallmark of the basic Poisson model.
If observed counts vary much more than their mean, they are **overdispersed**
relative to a Poisson model; a changing rate or dependence between events may
be responsible. Counts with substantially less variation are underdispersed.

**Theorem (Poisson expectation and variance).** If
$N\sim\operatorname{Poisson}(\lambda)$, then $E[N]=\lambda$ and
$\operatorname{Var}(N)=\lambda$.

**Proof:**

For the expectation, the $k=0$ term vanishes and $k/k!=1/(k-1)!$, so

$$
\begin{aligned}
E[N]
&=\sum_{k=0}^{\infty}k e^{-\lambda}\frac{\lambda^k}{k!}\\
&=\lambda e^{-\lambda}\sum_{j=0}^{\infty}\frac{\lambda^j}{j!}
=\lambda.
\end{aligned}
$$

Similarly,

$$
\begin{aligned}
E[N(N-1)]
&=\sum_{k=0}^{\infty}k(k-1)e^{-\lambda}\frac{\lambda^k}{k!}\\
&=\lambda^2 e^{-\lambda}\sum_{j=0}^{\infty}\frac{\lambda^j}{j!}
=\lambda^2.
\end{aligned}
$$

Since $N^2=N(N-1)+N$,

$$
\operatorname{Var}(N)=E[N^2]-(E[N])^2
=\bigl(\lambda^2+\lambda\bigr)-\lambda^2
=\lambda.
$$

$\square$

**Example (Support tickets).** Support tickets arrive at an average rate of
$2.5$ per hour. Assuming a Poisson model, find the probability of no tickets
in the next hour, the probability of exactly three, and the mean and variance.

**Solution:**

For the next one-hour interval, $N\sim\operatorname{Poisson}(2.5)$. Therefore

$$
P(N=0)=e^{-2.5}\approx0.0821,
$$

and

$$
P(N=3)=e^{-2.5}\frac{2.5^3}{3!}\approx0.2138.
$$

Finally,

$$
E[N]=2.5,
\qquad
\operatorname{Var}(N)=2.5.
$$

$\square$

## 4. How the models relate

The models form a useful hierarchy.

$$
\text{one binary opportunity}
\;\longrightarrow\;
\operatorname{Bernoulli}(p)
\;\longrightarrow\;
\text{sum of $n$ independent opportunities}
\;\longrightarrow\;
\operatorname{Binomial}(n,p).
$$

When there are many opportunities, each is rare, and the expected number of
successes $np$ stays near a moderate number $\lambda$, a Binomial count is
well approximated by a Poisson count:

$$
\operatorname{Binomial}(n,p)\approx\operatorname{Poisson}(\lambda=np).
$$

This is the **rare-event approximation**. It is often useful for a large
number of small-probability opportunities; it is not a license to replace a
Binomial model when $p$ is not small.

**Example (Rare defects).** A factory inspects $n=1{,}000$ independent items,
each defective with probability $p=0.002$. Approximate the probability of no
defects with a Poisson model, then compare it to the exact Binomial value.

**Solution:**

Here $np=2$, so the Poisson approximation uses
$N\sim\operatorname{Poisson}(2)$. It gives

$$
P(N=0)=e^{-2}\approx0.1353.
$$

The exact Binomial probability is

$$
P(S=0)=(1-0.002)^{1000}\approx0.1351.
$$

The values are close because there are many trials and individual defects are
rare.

$\square$

## 5. Choosing the model

| Question about the random quantity | Appropriate model | Key parameters | Mean and variance |
|---|---|---|---|
| Did one event occur? | $\operatorname{Bernoulli}(p)$ | $p$ | $p$, $p(1-p)$ |
| How many successes in exactly $n$ independent, equal-probability trials? | $\operatorname{Binomial}(n,p)$ | $n,p$ | $np$, $np(1-p)$ |
| How many arrivals occur during a fixed exposure interval? | $\operatorname{Poisson}(\lambda)$ | $\lambda$ | $\lambda$, $\lambda$ |

“There are 100 users, each either purchases or does not purchase” points to a
Binomial model. “How many users arrive in the next minute?” points to a
Poisson model. The distinction is whether the story starts with a **fixed
number of trials** or a **fixed exposure interval**.

## 6. Modeling cautions for data science

These distributions are useful baselines, but their assumptions deserve a
reality check.

- A Binomial model can fail when different customers have different purchase
  probabilities, or when one customer's action influences another's.
- A Poisson model can fail when the arrival rate changes over time, such as
  website traffic that spikes at lunchtime, or when events cluster.
- A count can be zero-heavy: for example, some users may be structurally
  unable to make a purchase. Such data can have more zeros than a simple
  Binomial or Poisson model expects.

In ML, a Bernoulli distribution underlies binary classification probabilities.
Binomial and Poisson distributions provide likelihoods for aggregate binary
outcomes and count targets. The distribution gives both a prediction target
and a principled statement of how uncertain that target should be.

## Check your understanding

1. Let $X\sim\operatorname{Bernoulli}(0.8)$. Find $P(X=0)$, $E[X]$, and
   $\operatorname{Var}(X)$.
2. A player makes each free throw independently with probability $0.7$. In
   ten throws, let $S$ be the number made. State the distribution of $S$, then
   find $E[S]$ and $\operatorname{Var}(S)$.
3. A bookstore receives an average of four online orders per hour and uses a
   Poisson model. Find $P(N=0)$ and $P(N=1)$ for the next hour.
4. Which model is more appropriate for each quantity: (a) whether a single
   loan defaults, (b) the number of defaults among $500$ independent loans
   with the same default probability, and (c) the number of calls received by
   a help desk in the next ten minutes? State why.
5. A count data set has sample mean $3.1$ and sample variance $11.8$. What
   does this suggest about the adequacy of a basic Poisson model?

### Answers

1. $P(X=0)=0.2$, $E[X]=0.8$, and
   $\operatorname{Var}(X)=0.8(0.2)=0.16$.
2. $S\sim\operatorname{Binomial}(10,0.7)$,
   $E[S]=7$, and $\operatorname{Var}(S)=2.1$.
3. $P(N=0)=e^{-4}\approx0.0183$ and
   $P(N=1)=4e^{-4}\approx0.0733$.
4. (a) Bernoulli, one binary outcome; (b) Binomial, a fixed number of
   independent equal-probability binary trials; (c) Poisson, a count of
   arrivals over a fixed time interval.
5. The variance far exceeds the mean, so the data are overdispersed relative
   to a basic Poisson model. Investigate changing rates, clustering, or a more
   flexible count model.

## Takeaway

Use Bernoulli for one binary outcome, Binomial for a fixed number of
independent binary opportunities, and Poisson for a count of independent
arrivals over fixed exposure. Their means locate typical counts; their
variances describe how much those counts naturally fluctuate. Choosing the
model begins with the process that generated the count—not with the formula.
