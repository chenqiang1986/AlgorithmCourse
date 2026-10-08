# Homework: Continuous Random Variables and Distributions
*ML / M04 — Statistics*

Use the [Lesson 3 notes](./03-continuous-random-variables-and-distributions.md)
as a reference. For each probability, write an integral or CDF difference
before evaluating it. For every density, state its support clearly.

## 1. Valid PDFs and interval probabilities

For each function below, determine whether it is a valid PDF. Explain using
nonnegativity and total area. If it is valid, find the requested probability.

1. $f(x)=\frac14$ for $0\le x\le4$, and $f(x)=0$ otherwise. Find
   $P(1<X<3)$.
2. $g(x)=3x^2$ for $0\le x\le1$, and $g(x)=0$ otherwise. Find
   $P(X\le1/2)$.
3. $h(x)=2-x$ for $0\le x\le2$, and $h(x)=0$ otherwise.
4. $r(x)=2$ for $0\le x\le1$, and $r(x)=0$ otherwise.

## 2. Density is not point probability

Let $X$ have PDF

$$
f_X(x)=
\begin{cases}
3x^2,&0\le x\le1,\\
0,&\text{otherwise}.
\end{cases}
$$

1. Find $P(X=1/2)$.
2. Find $P(0\le X\le1/2)$.
3. Find $P(1/2<X<1)$.
4. The value $f_X(1/2)=3/4$ is greater than $P(0\le X\le1/2)=3/8$.
   Explain why this is not a contradiction.

## 3. CDFs

Let $X$ have PDF

$$
f_X(x)=
\begin{cases}
\frac{x}{2},&0\le x\le2,\\
0,&\text{otherwise}.
\end{cases}
$$

1. Derive a piecewise formula for $F_X(x)$.
2. Use your CDF to find $P(1<X\le3)$.
3. Use your CDF to find $P(X>1.5)$.
4. Verify your answer to part 2 by integrating the PDF directly.

## 4. Expectation and variance from a PDF

Let $X$ have PDF

$$
f_X(x)=
\begin{cases}
2x,&0\le x\le1,\\
0,&\text{otherwise}.
\end{cases}
$$

1. Verify that $f_X$ is a valid PDF.
2. Compute $E[X]$.
3. Compute $E[X^2]$.
4. Compute $\operatorname{Var}(X)$ using

   $$
   \operatorname{Var}(X)=E[X^2]-(E[X])^2.
   $$

5. Find $E[3X-4]$ and $\operatorname{Var}(3X-4)$.

## 5. A uniform measurement error

A sensor's measurement error $E$ is uniformly distributed from $-0.5$ to
$0.5$ millimeters.

1. Write the PDF of $E$.
2. Find $P(|E|\le0.1)$.
3. Find $P(E>0.3)$.
4. Find $E[E]$ and $\operatorname{Var}(E)$.
5. A true length is $L=12+E$ millimeters. Find $E[L]$ and
   $\operatorname{Var}(L)$.

## 6. Normal distributions

Suppose $Z\sim\mathcal N(50,16)$.

1. State the mean and standard deviation of $Z$.
2. Write the PDF of $Z$.
3. Explain why $P(Z=50)=0$ even though $50$ is the center and mode of the
   distribution.
4. State whether each claim is true or false, and explain briefly.

   - $P(Z<50)=0.5$.
   - $P(Z<46)=P(Z>54)$.
   - $P(Z<0)=0$.

5. Give one reason a Normal model might be inappropriate for modeling a
   variable such as the number of website visits made by a person in one day.

## Practice — variance of the standard Normal distribution

Let $Z\sim\mathcal N(0,1)$ have PDF

$$
\phi(z)=\frac1{\sqrt{2\pi}}e^{-z^2/2},
\quad\text{for }-\infty<z<\infty.
$$

You may use the fact that

$$
\int_{-\infty}^{\infty}\phi(z)\,dz=1.
$$

1. Explain by symmetry why $E[Z]=0$.
2. Differentiate $\phi(z)$ and show that

   $$
   \phi'(z)=-z\phi(z).
   $$

3. For $M>0$, use the identity in part 2 to rewrite

   $$
   \int_{-M}^{M}z^2\phi(z)\,dz
   $$

   in a form suitable for integration by parts.
4. Apply integration by parts on $[-M,M]$ to show that

   $$
   \int_{-M}^{M}z^2\phi(z)\,dz
   =-\bigl[z\phi(z)\bigr]_{-M}^{M}
   +\int_{-M}^{M}\phi(z)\,dz.
   $$

5. Show that $\lim_{M\to\infty}M\phi(M)=0$. Then let $M\to\infty$ in
   part 4 and use the given integral of $\phi$ to prove that

   $$
   E[Z^2]=1.
   $$

6. Conclude that $\operatorname{Var}(Z)=1$. If

   $$
   X=\mu+\sigma Z,
   $$

   use the variance transformation rule to conclude that

   $$
   \operatorname{Var}(X)=\sigma^2.
   $$

## 7. Exponential waiting times

Customers arrive according to a Poisson process at a rate of $4$ customers
per hour. Let $W$ be the waiting time in hours until the next arrival.

1. State the distribution of $W$ and write its PDF.
2. Find $P(W>1/2)$.
3. Find $P(W\le1/4)$.
4. Find $E[W]$ and $\operatorname{Var}(W)$.
5. Interpret $E[W]$ in minutes.
6. In one sentence, explain the connection between the rate here and the
   Poisson count model for the number of arrivals in one hour.

## 8. Marginal densities from a joint density

Let $(X,Y)$ have joint PDF

$$
f_{X,Y}(x,y)=
\begin{cases}
2,&0\le y\le x\le1,\\
0,&\text{otherwise}.
\end{cases}
$$

1. Sketch the region in the $xy$-plane where the joint density is positive.
2. Verify that the joint PDF integrates to $1$.
3. Find the marginal PDF $f_X(x)$.
4. Find the marginal PDF $f_Y(y)$.
5. Are $X$ and $Y$ independent? Justify your answer using either the support
   or the factorization criterion.
6. Find $P(X<1/2)$.

## 9. An independent joint density

Let $(X,Y)$ have joint PDF

$$
f_{X,Y}(x,y)=
\begin{cases}
6xy^2,&0\le x\le1,\ 0\le y\le1,\\
0,&\text{otherwise}.
\end{cases}
$$

1. Verify that this is a valid joint PDF.
2. Find $f_X(x)$ and $f_Y(y)$.
3. Determine whether $X$ and $Y$ are independent using the factorization
   criterion.
4. Find $P(X\le1/2,\,Y\le1/2)$.
5. If they are independent, compute the same probability by multiplying two
   marginal probabilities and verify that it agrees with part 4.

## 10. Continuous or discrete?

For each quantity, decide whether a continuous or discrete random variable is
the more natural model. Then name a reasonable distribution, if one of the
models from Lessons 2 or 3 applies. State any assumption needed for your
choice.

1. The number of defective chips in a shipment of $500$ chips.
2. The time until the next server request, assuming a stable arrival rate.
3. The temperature recorded by a high-precision thermometer.
4. Whether one customer renews a subscription.
5. The total number of calls received by a call center over the next hour.

## Challenge — derive the Exponential CDF and survival probability

Let $W\sim\operatorname{Exponential}(\lambda)$, where $\lambda>0$, with PDF

$$
f_W(w)=\lambda e^{-\lambda w}\quad\text{for }w\ge0.
$$

1. Derive the CDF $F_W(w)$ for $w<0$ and for $w\ge0$.
2. Show that the survival probability is

   $$
   P(W>t)=e^{-\lambda t}\quad\text{for }t\ge0.
   $$

3. Use the survival probability to prove the memoryless property: for
   $s,t\ge0$,

   $$
   P(W>s+t\mid W>s)=P(W>t).
   $$

4. Explain in words why this property makes the Exponential distribution a
   useful model for waiting until the next event under a constant-rate Poisson
   process.

## Challenge — transforming a random variable with an increasing function

Let $Y=c(X)$, where $c$ is a fixed strictly increasing function. This problem
compares how a transformation changes a discrete distribution and a continuous
distribution.

### A. Discrete transformation

Let $X$ have PMF

$$
\begin{array}{c|rrrr}
x&-1&0&2&3\\ \hline
P(X=x)&0.10&0.20&0.40&0.30
\end{array}
$$

and define

$$
Y=c(X)=X^3+X.
$$

1. Verify that $c(x)=x^3+x$ is strictly increasing.
2. List every possible value of $Y$ and find its PMF.
3. Find $P(Y\le10)$ in two ways: first from the PMF of $Y$, then by rewriting
   the event in terms of $X$.
4. Let $c$ be any strictly increasing function on the support of a discrete
   random variable $X$. State a formula for $P(Y=c(x))$ in terms of the PMF
   of $X$. Explain why no derivative appears in this discrete formula.

### B. Continuous transformation

Let $X$ have PDF

$$
f_X(x)=
\begin{cases}
2x,&0\le x\le1,\\
0,&\text{otherwise},
\end{cases}
$$

and define

$$
Y=c(X)=e^X.
$$

1. State the support of $Y$ and find the inverse function $c^{-1}(y)$ on that
   support.
2. Derive $F_Y(y)$ piecewise. Begin with the fact that $c$ is increasing and
   write

   $$
   F_Y(y)=P(Y\le y)=P\bigl(X\le c^{-1}(y)\bigr).
   $$

3. Differentiate your CDF to find $f_Y(y)$.
4. Verify directly that your density integrates to $1$ over the support of
   $Y$.
5. Find $P(\sqrt e\le Y\le e)$ using your density or CDF. Then find the same
   probability by rewriting the event in terms of $X$.
6. Verify the differential probability relation directly for this example.
   Since $y=e^x$, first find $dy$ in terms of $dx$. Then use $x=\ln y$ and
   your answer for $f_Y(y)$ from part 3 to show that

   $$
   f_X(x)\,dx=f_Y(y)\,dy.
   $$

   Interpret both sides as the probability in the corresponding tiny intervals
   $[x,x+dx]$ and $[y,y+dy]$.

> **Note (Visualizing a PDF transformation without calculating a CDF).** A
> density has probability meaning only when paired with a small interval:
>
> $$
> f_X(x)\,dx
> $$
>
> represents the probability that $X$ falls in $[x,x+dx]$. If
> $Y=c(X)$ and $c$ is differentiable and strictly increasing, then a small
> interval near $x$ maps to one near $y=c(x)$. They contain the same
> probability mass, so
>
> $$
> f_X(x)\,dx=f_Y(y)\,dy.
> $$
>
> Because $dy=c'(x)\,dx$, stretching an interval decreases its density and
> compressing an interval increases its density:
>
> $$
> f_Y(c(x))=\frac{f_X(x)}{c'(x)}.
> $$
>
> Equivalently, using $x=c^{-1}(y)$,
>
> $$
> f_Y(y)=f_X\bigl(c^{-1}(y)\bigr)
> \frac{d}{dy}c^{-1}(y).
> $$
