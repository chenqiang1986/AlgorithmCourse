# Lesson 1: The Linear Model, Squared Loss, and Normal Equations
*ML / M06 — Supervised Learning*

## The question

Given $n$ input-output pairs, how do we choose the linear rule that predicts
their numerical targets as well as possible?

## Learning goals

By the end of this lesson, you should be able to write linear regression in
matrix form, derive its normal equations, and distinguish positive
semidefinite from positive definite matrices in least squares.

## 1. The model and shapes

For one example with $d$ features, linear regression predicts

$$
\hat y_i=x_i^T w+b,
$$

where $x_i\in\mathbb R^d$, $w\in\mathbb R^d$, and $b\in\mathbb R$ is the
intercept. Stack the examples as rows of a design matrix:

$$
X=\begin{bmatrix}x_1^T\\\vdots\\x_n^T\end{bmatrix}\in\mathbb R^{n\times d},
\qquad y\in\mathbb R^n.
$$

Then $\hat y=Xw+b\mathbf1$. It is often cleaner to absorb the intercept into
the matrix: prepend a column of ones to form $A=[\mathbf1\;X]$ and let
$\theta=(b,w^T)^T$. The model is simply

$$
\boxed{\hat y=A\theta.}
$$

From here on, use $X\in\mathbb R^{n\times p}$ for the design matrix **after**
any intercept column has been added, and $\beta\in\mathbb R^p$ for all
coefficients. Thus $\hat y=X\beta$.

## 2. Squared-error loss

The residual vector is $r(\beta)=y-X\beta$. Ordinary least squares (OLS)
chooses coefficients that minimize the residual sum of squares (RSS):

$$
\operatorname{RSS}(\beta)=\lVert y-X\beta\rVert_2^2.
$$

Machine-learning code commonly uses the mean squared error,

$$
L(\beta)=\frac1n\lVert y-X\beta\rVert_2^2.
$$

The two objectives have the same minimizer; the factor $1/n$ only changes the
loss scale and gradient scale. Squaring makes large errors count more heavily
and gives a smooth, differentiable objective.

## 3. Deriving the normal equations

Expand the RSS and differentiate with respect to the coefficient vector:

$$
\operatorname{RSS}(\beta)
=y^Ty-2\beta^TX^Ty+\beta^TX^TX\beta,
$$

$$
\nabla_\beta\operatorname{RSS}(\beta)=2X^T(X\beta-y).
$$

At a stationary point the gradient is zero, so every least-squares solution
satisfies the **normal equations**

$$
\boxed{X^TX\hat\beta=X^Ty.}
$$

If $X^TX$ is invertible, then the solution is unique and can be written as

$$
\hat\beta=(X^TX)^{-1}X^Ty.
$$

This is a mathematical formula, not the recommended numerical algorithm.
In code, solve the linear system with `np.linalg.solve`, or preferably use
`np.linalg.lstsq`; explicitly forming an inverse can amplify numerical error.

## 4. Geometry: residuals are perpendicular to the column space

The normal equations are equivalent to

$$
X^T(y-X\hat\beta)=0.
$$

So the fitted residual is orthogonal to every column of $X$. The prediction
$X\hat\beta$ is the orthogonal projection of $y$ onto the column space of
$X$. This also explains why correlated or duplicate columns cause trouble:
they describe redundant directions in that space.

## 5. Why $X^TX$ is positive semidefinite

**Theorem (Gram matrix property).** For every real matrix $X$,
$X^TX$ is symmetric positive semidefinite. It is positive definite exactly
when the columns of $X$ are linearly independent.

**Proof:**

Symmetry follows from $(X^TX)^T=X^TX$. For any $v\in\mathbb R^p$,

$$
v^TX^TXv=(Xv)^T(Xv)=\lVert Xv\rVert_2^2\ge0.
$$

Thus $X^TX$ is positive semidefinite. Equality holds exactly when $Xv=0$.
Therefore $v^TX^TXv>0$ for every nonzero $v$ exactly when $Xv=0$ has only
the zero solution—exactly when the columns of $X$ are linearly independent.

$\square$

The Hessian of RSS is $2X^TX$. Hence OLS is always convex. It is strictly
convex, and has one coefficient solution, only at full column rank
$\operatorname{rank}(X)=p$. If rank is deficient, fitted values can still be
unique while multiple coefficient vectors attain them.

**Example (A singular design).** If one feature column is twice another,
then there is a nonzero $v$ with $Xv=0$. Moving coefficients along $v$ changes
neither predictions nor loss, so $(X^TX)^{-1}$ does not exist.

**Solution:**

For columns $x$ and $2x$, choose coefficients changes $v=(2,-1)^T$. Then
$Xv=2x-2x=0$. The Gram matrix is positive semidefinite but not positive
definite, and the coefficient representation is not identifiable.

$\square$

## Key takeaways

- With an intercept column included, linear regression is $\hat y=X\beta$.
- OLS minimizes $\lVert y-X\beta\rVert_2^2$ and yields $X^TX\hat\beta=X^Ty$.
- $X^TX$ is always positive semidefinite; it is positive definite exactly at
  full column rank.
- Use a linear solve or least-squares routine, not an explicit inverse.
