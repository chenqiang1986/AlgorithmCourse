# Homework: Residual Variance and Degrees of Freedom
*ML / M06 — Supervised Learning*

Use the [Lesson 5 notes](./05-residual-variance-and-degrees-of-freedom.md)
as a reference. This homework fills in the linear-algebra and expectation
steps behind the degrees-of-freedom result. Show each matrix identity and state
which assumptions you use.

Throughout, assume the fixed design matrix $X\in\mathbb R^{n\times p}$ has
full column rank $p<n$, and that

$$
y=X\beta+\varepsilon,
\qquad
E[\varepsilon]=0,
\qquad
\operatorname{Cov}(\varepsilon)=\sigma^2I_n.
$$

Define the hat matrix and residual-maker matrix by

$$
H=X(X^TX)^{-1}X^T,
\qquad M=I_n-H.
$$

For this homework, $X$, $\beta$, and $\sigma$ are fixed; the only source of
randomness is $\varepsilon$. Normality is not needed for the expectation
calculation below.

## A. Diagonalize $H$ and $M$

### 1. Basic identities

1. Verify directly that $HX=X$.
2. Verify that $H^2=H$.
3. Use the definition of $M$ and your result from part 1 to prove that
   $MX=0$.
4. Show that $H$ and $M$ are symmetric. Then show that $M^2=M$.

### 2. Rank of the hat matrix

1. From $HX=X$, use the rank inequality

   $$
   \operatorname{rank}(AB)\leq \operatorname{rank}(A)
   $$

   to prove $\operatorname{rank}(X)\leq\operatorname{rank}(H)$.
2. Write $H$ as a product whose leftmost factor is $X$. Apply the same rank
   inequality to prove $\operatorname{rank}(H)\leq\operatorname{rank}(X)$.
3. Conclude that

   $$
   \operatorname{rank}(H)=\operatorname{rank}(X)=p.
   $$

### 3. Eigenvalues and diagonal form

1. Suppose $Hv=\lambda v$ for a nonzero vector $v$. Apply $H$ to both sides
   and use $H^2=H$ to prove that $\lambda^2=\lambda$. What are the only
   possible eigenvalues of $H$?
2. Since $H$ is symmetric, it can be orthogonally diagonalized. Explain why
   the diagonal form has exactly $p$ entries equal to $1$ and $n-p$ entries
   equal to $0$.
3. If

   $$
   H=Q^T\operatorname{diag}(I_p,0_{n-p})Q
   $$

   for an orthogonal matrix $Q$, calculate $M=I_n-H$ in terms of $Q$.
4. State the rank of $M$ and explain why its diagonalized form has $n-p$ ones
   and $p$ zeros. You may reorder the columns of $Q$, so either order of the
   diagonal entries is acceptable.

## B. Connection with the error estimate

### 1. Which quantities are random?

The fitted residual vector is $e=y-\hat y$. It is a random vector, because it
is computed from the random response $y$.

For each quantity below, state its shape (scalar, vector, or matrix) and
whether it is fixed or random under the assumptions of this homework. If it is
fixed but unknown, say so.

$$
\beta,\qquad X,\qquad \varepsilon,\qquad y,\qquad
\hat\beta,\qquad \hat y.
$$

### 2. Express the residual in terms of the error

1. Starting from $\hat y=Hy$, show that

   $$
   e=y-\hat y=My.
   $$

2. Substitute $y=X\beta+\varepsilon$ into this expression. Use $MX=0$ to
   prove

   $$
   \boxed{e=M\varepsilon.}
   $$

### 3. Express RSS in terms of the error

The residual sum of squares is

$$
\operatorname{RSS}=e^Te.
$$

Use $e=M\varepsilon$, the symmetry of $M$, and $M^2=M$ to show that

$$
\boxed{\operatorname{RSS}=\varepsilon^TM\varepsilon.}
$$

### 4. Rotate and standardize the errors

Choose the orthogonal matrix $Q$ so that

$$
M=Q^T\operatorname{diag}(\underbrace{1,\ldots,1}_{n-p},
\underbrace{0,\ldots,0}_{p})Q,
$$

and define

$$
z=\frac{Q\varepsilon}{\sigma}.
$$

1. Calculate $E[z]$.
2. Starting with

   $$
   \operatorname{Cov}(z)=E[(z-E[z])(z-E[z])^T],
   $$

   show that $\operatorname{Cov}(z)=I_n$.
3. Conclude that, for all $i,j$,

   $$
   E[z_i]=0,
   \qquad \operatorname{Cov}(z_i,z_j)=\delta_{ij},
   $$

   where $\delta_{ij}$ is the Kronecker delta. Do not try to prove
   independence; it is not needed for the next part.

### 5. Expected residual sum of squares

1. Use the diagonal form of $M$ and $z=Q\varepsilon/\sigma$ to rewrite RSS
   as

   $$
   \operatorname{RSS}=\sigma^2\sum_{i=1}^{n-p}z_i^2.
   $$

2. Use $E[z_i]=0$ and $\operatorname{Var}(z_i)=1$ to calculate $E[z_i^2]$.
3. Hence prove

   $$
   \boxed{E[\operatorname{RSS}]=(n-p)\sigma^2.}
   $$

4. Conclude that

   $$
   s^2=\frac{\operatorname{RSS}}{n-p}
   $$

   is an unbiased estimator of $\sigma^2$. In 2–3 sentences, explain why the
   denominator is $n-p$ rather than $n$: what happened to the other $p$
   directions?
