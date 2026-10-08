# Homework: Classic Discrete Probability Models
*ML / M04 — Statistics*

Use the [Lesson 2 notes](./02-classic-discrete-probability-models.md) as a
reference. For every numerical probability, state the distribution and the
formula before evaluating it. For each modeling question, explain why the
assumptions do or do not fit; naming a distribution alone is not enough.

## 1. One binary outcome

An email sent by a marketing campaign is opened with probability $0.18$. Let
$X=1$ if a randomly selected email is opened and $X=0$ otherwise.

1. State the distribution of $X$, including its parameter.
2. Find $P(X=0)$ and $P(X=1)$.
3. Compute $E[X]$, $E[X^2]$, and $\operatorname{Var}(X)$.
4. Explain in one or two sentences why $E[X]=0.18$ does not mean a single
   email is opened by “$0.18$ of an email.”

## 2. Is a Binomial model justified?

For each setting, decide whether the stated count can reasonably be modeled
as $\operatorname{Binomial}(n,p)$. If yes, identify $n$ and $p$. If no,
identify at least one failed or questionable Binomial assumption.

1. The number of heads in $40$ independent tosses of a fair coin.
2. The number of students who arrive late among $30$ students when all use the
   same bus route, which is either on time or delayed for everyone.
3. The number of defective bulbs in a random sample of $50$ bulbs from a huge
   production run, assuming each bulb's defect status is independent and the
   defect rate is $0.01$.
4. The number of customers who make a purchase during the next hour at a
   website.

## 3. A Binomial probability calculation

A basketball player makes a free throw with probability $0.8$. Assume shots
are independent, and let $S$ be the number made in $12$ attempts.

1. State the distribution of $S$.
2. Find $P(S=10)$.
3. Find $P(S\geq11)$.
4. Find $P(S\leq9)$ using a complement rather than adding ten PMF terms.
5. Find $E[S]$, $\operatorname{Var}(S)$, and the standard deviation of $S$.

## 4. A Binomial count from indicators

Each of $n=25$ independent users completes a sign-up flow with probability
$p=0.6$. Let $X_i$ be the indicator that user $i$ completes the flow, and
let

$$
T=\sum_{i=1}^{25}X_i.
$$

1. Find $E[X_i]$ and $\operatorname{Var}(X_i)$.
2. Use linearity of expectation to calculate $E[T]$.
3. Use independence to calculate $\operatorname{Var}(T)$.
4. State the distribution of $T$ and verify that its standard formulas agree
   with your answers to parts 2 and 3.
5. Would the calculation of $E[T]$ still work if completions were dependent?
   Would your variance calculation still work unchanged? Explain.

## 5. Reading Binomial mean and variance

Suppose $Y\sim\operatorname{Binomial}(80,0.15)$.

1. Find $E[Y]$, $\operatorname{Var}(Y)$, and $\operatorname{SD}(Y)$.
2. A report says: “Exactly $12$ successes will occur, because the expected
   number is $12$.” Explain the error.
3. Compare the variance of $Y$ with the variance of a Poisson random variable
   having the same mean. Which is larger, and why?

## 6. A Poisson arrival model

Calls arrive at a help desk at an average rate of $3$ calls per $15$ minutes.
Assume a Poisson model with a stable rate.

1. State the distribution of the number of calls in the next $15$ minutes.
2. Find the probability of no calls in the next $15$ minutes.
3. Find the probability of exactly five calls in the next $15$ minutes.
4. Find the probability of at least one call in the next $15$ minutes.
5. What are the mean and variance of the call count in the next hour?
6. Find the probability of no calls in a full hour.

## 7. Changing the Poisson exposure interval

An online store receives orders according to a Poisson model at an average
rate of $1.8$ orders per hour.

1. Give the distribution of the number of orders in a $30$-minute interval.
2. Give the distribution of the number of orders in an $8$-hour workday.
3. Find the expected number and variance of orders in each interval.
4. Find the probability of exactly two orders in a $30$-minute interval.
5. Explain why the parameter changes with the length of the interval while
   the underlying per-hour rate does not.

## 8. Diagnosing a Poisson model

For each of $60$ comparable one-hour periods, a service records the number of
incoming requests. The sample mean is $4.2$ and the sample variance is $13.7$.

1. If a basic Poisson model were adequate, what relationship would you expect
   between the population mean and variance?
2. Describe what the reported summary suggests.
3. Give two plausible process-level reasons for this result.
4. Why is the comparison of a sample mean and sample variance evidence about a
   model rather than a mathematical proof that the model is false?

## 9. Rare-event approximation

Each of $2{,}000$ independently manufactured sensors has probability $0.001$
of failing its initial quality check. Let $F$ be the number that fail.

1. State the exact distribution of $F$ and find its mean and variance.
2. Give the Poisson approximation to the distribution of $F$.
3. Use the approximation to estimate $P(F=0)$ and $P(F\geq1)$.
4. Compute the exact expressions for $P(F=0)$ and $P(F\geq1)$; numerical
   evaluation is optional.
5. Explain why the Poisson approximation is appropriate here, referring to
   both $n$ and $p$.

## 10. Modeling a data-generating process

For each situation below, define a random variable and choose the most
appropriate model from Bernoulli, Binomial, or Poisson. State its parameter or
parameters, then write its PMF.

1. Whether a patient misses a scheduled appointment, given a fixed estimated
   miss probability of $0.09$.
2. How many of $75$ independently chosen patients miss their appointments,
   where every patient has miss probability $0.09$.
3. How many patients arrive at a walk-in clinic during the next two hours,
   given a stable average arrival rate of $7$ patients per hour.
4. A social-media post is shared by $300$ followers, but the chance of a share
   depends strongly on whether each follower is in one of two user groups.
   Explain why a simple $\operatorname{Binomial}(300,p)$ model is
   questionable, even though each follower has a binary outcome.

## Challenge — derive the Poisson variance

Let $N\sim\operatorname{Poisson}(\lambda)$. Starting from the PMF,

$$
P(N=k)=e^{-\lambda}\frac{\lambda^k}{k!},
$$

derive $E[N(N-1)]$. Then use

$$
N^2=N(N-1)+N
$$

and $E[N]=\lambda$ to prove that

$$
\operatorname{Var}(N)=\lambda.
$$

Show the index change that converts the relevant infinite series into the
series for $e^\lambda$.

## Challenge — derive the Poisson distribution as a rare-event limit

Fix $\lambda>0$. For each $n>\lambda$, let

$$
S_n\sim\operatorname{Binomial}\left(n,\frac{\lambda}{n}\right).
$$

For a fixed nonnegative integer $k$, prove that

$$
\lim_{n\to\infty}P(S_n=k)
=e^{-\lambda}\frac{\lambda^k}{k!}.
$$

In other words, derive the PMF of $\operatorname{Poisson}(\lambda)$ as the
limit of Binomial PMFs whose number of trials grows while the per-trial event
probability shrinks.

1. Begin with

   $$
   P(S_n=k)=\binom nk
   \left(\frac{\lambda}{n}\right)^k
   \left(1-\frac{\lambda}{n}\right)^{n-k}.
   $$

2. Show that

   $$
   \binom nk\left(\frac{\lambda}{n}\right)^k
   =\frac{\lambda^k}{k!}
   \prod_{j=0}^{k-1}\left(1-\frac{j}{n}\right).
   $$

   Deduce its limit as $n\to\infty$. (For $k=0$, interpret the empty product
   as $1$.)

3. Use the standard limit

   $$
   \lim_{n\to\infty}\left(1-\frac{\lambda}{n}\right)^n=e^{-\lambda}
   $$

   to show that

   $$
   \lim_{n\to\infty}\left(1-\frac{\lambda}{n}\right)^{n-k}
   =e^{-\lambda}.
   $$

4. Combine parts 2 and 3 to establish the stated limit. Then explain the
   approximation process in context: divide one fixed time interval into $n$
   equal segments, assume that an event occurs in each segment with probability
   $\lambda/n$, and count the total events. Describe what it means to let
   $n\to\infty$: the segments become arbitrarily short, so the model considers
   the opportunity for an event continuously throughout the interval while the
   expected total count remains $\lambda$.
