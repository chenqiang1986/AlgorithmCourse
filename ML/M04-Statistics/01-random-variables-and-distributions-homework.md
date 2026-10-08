# Homework: Random Variables, Joint Distributions, Expectation, Variance, and Covariance
*ML / M04 — Statistics*

Use the [Lesson 1 notes](./01-random-variables-and-distributions.md) as a
reference. Show the probability calculation or identity used for each answer.
For any claim of independence, verify the joint-PMF factorization; do not
justify it solely by saying that outcomes “seem unrelated.”

## 1. A discrete distribution

A discrete RV $X$ has PMF

$$
\begin{array}{c|rrrr}
x & -1 & 0 & 2 & 4\\ \hline
P(X=x) & 0.15 & 0.25 & 0.40 & 0.20
\end{array}
$$

1. Verify that this is a valid PMF.
2. Find $P(X\ge 2)$ and $P(-1<X<4)$.
3. Find the CDF values $F_X(-1)$, $F_X(1)$, and $F_X(4)$.
4. Compute $E[X]$, $E[X^2]$, and $\operatorname{Var}(X)$.

## 2. Joint PMF and marginal PMFs

Two binary RVs $X$ and $Y$ have the following joint PMF.

$$
\begin{array}{c|cc}
 & Y=0 & Y=1\\ \hline
X=0 & 0.30 & 0.10\\
X=1 & 0.20 & 0.40
\end{array}
$$

1. Verify that the table is a valid joint PMF.
2. Find $p_X(0)$, $p_X(1)$, $p_Y(0)$, and $p_Y(1)$.
3. Find $P(X=Y)$ and $P(X+Y=1)$.
4. Find $P(X=1\mid Y=1)$.

## 3. Test for independence

Using the joint PMF in Problem 2:

1. Determine whether $X$ and $Y$ are independent. Use a specific cell of the
   table and the factorization criterion.
2. Explain, in terms of the conditional probability from Problem 2, why your
   conclusion is consistent with the meaning of independence.

## 4. Two dice: a joint distribution that factors

Roll two fair six-sided dice. Let $X$ be the first result and $Y$ be the
second result.

1. Write $p_{X,Y}(x,y)$ for $x,y\in\{1,\ldots,6\}$.
2. Find the marginal PMFs $p_X(x)$ and $p_Y(y)$.
3. Prove that $X$ and $Y$ are independent using the joint-PMF criterion.
4. Let $S=X+Y$. Find $P(S=7)$ and $P(S=12)$. Explain why $S$ and $X$ are not
   independent by comparing $P(S=12,X=1)$ with $P(S=12)P(X=1)$.

## 5. Multiple RVs: pairwise versus mutual independence

Let $A$ and $B$ be independent fair bits, each taking values $0$ and $1$.
Define

$$
C=(A+B)\bmod 2.
$$

1. List the four equally likely triples $(A,B,C)$.
2. Show that $A$ and $B$ are independent, and that $A$ and $C$ are
   independent.
3. Calculate $P(A=0,B=0,C=0)$ and compare it with
   $P(A=0)P(B=0)P(C=0)$.
4. Are $A$, $B$, and $C$ mutually independent? Briefly explain how this
   example distinguishes pairwise from mutual independence.

## 6. Expectations and transformations

Let $X$ be the number of successful requests among two independent attempts,
where each attempt succeeds with probability $0.7$. Thus

$$
P(X=0)=0.09,\qquad P(X=1)=0.42,\qquad P(X=2)=0.49.
$$

1. Compute $E[X]$ directly from the PMF.
2. Compute $E[X^2]$ and $\operatorname{Var}(X)$.
3. A service charges $D=5+3X$ dollars. Find $E[D]$ and
   $\operatorname{Var}(D)$.
4. Explain why $E[X^2]$ is not equal to $(E[X])^2$ in this example.

## 7. Indicators and linearity of expectation

In a class of $30$ students, each student independently submits an assignment
on time with probability $0.8$. Let $I_i$ be the indicator that student $i$
submits on time, and let

$$
T=\sum_{i=1}^{30} I_i.
$$

1. Find $E[I_i]$ and explain why it equals a probability.
2. Use linearity of expectation to find $E[T]$.
3. Would the calculation in part 2 require independence among students?
   Explain.
4. Under the stated independence assumption, find $\operatorname{Var}(T)$.

## 8. Proof — linearity of expectation without independence

Let $X$ and $Y$ be discrete RVs with finite support and arbitrary joint PMF
$p_{X,Y}(x,y)$. Prove that

$$
E[X+Y]=E[X]+E[Y].
$$

Begin with

$$
E[X+Y]=\sum_x\sum_y (x+y)p_{X,Y}(x,y).
$$

Split the sum, then use the marginal-PMF identities

$$
p_X(x)=\sum_y p_{X,Y}(x,y),
\qquad
p_Y(y)=\sum_x p_{X,Y}(x,y).
$$

In one final sentence, identify why this proof does **not** require $X$ and
$Y$ to be independent. In particular, state whether you used the
factorization $p_{X,Y}(x,y)=p_X(x)p_Y(y)$.

## 9. Covariance and the variance of a sum

Suppose $X$ and $Y$ satisfy

$$
E[X]=4,\quad E[Y]=10,\quad
\operatorname{Var}(X)=9,\quad \operatorname{Var}(Y)=16,\quad
\operatorname{Cov}(X,Y)=-3.
$$

1. Find $E[2X-Y+5]$.
2. Find $\operatorname{Var}(X+Y)$.
3. Find $\operatorname{Var}(2X-Y)$.
4. Interpret the negative covariance in the context of the spread of $X+Y$.

## 10. Zero covariance need not mean independence

Let $X$ be uniformly distributed on $\{-1,0,1\}$ and let $Y=X^2$.

1. Write the joint PMF of $(X,Y)$ by listing every pair with positive
   probability.
2. Find $E[X]$, $E[Y]$, and $E[XY]$.
3. Compute $\operatorname{Cov}(X,Y)$.
4. Explain why $X$ and $Y$ are not independent even though their covariance
   is zero.

## 11. Feature covariance in a small data set

The following four observations are equally likely draws from a population:

$$
(X,Y)\in\{(1,1),(2,3),(3,2),(4,4)\}.
$$

1. Find $E[X]$ and $E[Y]$.
2. Find $E[XY]$ and $\operatorname{Cov}(X,Y)$.
3. Find $\operatorname{Var}(X)$, $\operatorname{Var}(Y)$, and the covariance
   matrix of $(X,Y)^T$.
4. Does the positive covariance prove that $X$ causes $Y$ to increase?
   Explain what covariance does and does not establish.

## Challenge — covariance matrix of a linear transformation

Let $\mathbf X=(X_1,X_2)^T$ have covariance matrix

$$
\Sigma=
\begin{bmatrix}4&1\\1&9\end{bmatrix},
$$

and define $\mathbf Z=A\mathbf X$, where

$$
A=\begin{bmatrix}1&2\\-1&1\end{bmatrix}.
$$

1. Compute $\operatorname{Cov}(\mathbf Z)=A\Sigma A^T$.
2. Use your matrix to find $\operatorname{Var}(Z_1)$,
   $\operatorname{Var}(Z_2)$, and $\operatorname{Cov}(Z_1,Z_2)$.
3. Verify your value for $\operatorname{Var}(Z_1)$ directly from
   $Z_1=X_1+2X_2$ using the variance-of-a-linear-combination formula.
