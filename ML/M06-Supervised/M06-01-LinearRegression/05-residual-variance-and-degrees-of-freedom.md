# Lesson 5: Advanced — Residual Variance and Degrees of Freedom
*ML / M06 — Supervised Learning*

## The question

In the statistical linear model, how can the fitted residuals estimate the
variance of the unobserved noise—and why is the denominator $n-p$ rather than
$n$ or $n-1$?

## 1. The statistical model and assumptions

This lesson adds a probability model to the optimization problem:

$$
\boxed{y=X\beta+\varepsilon,\qquad
\varepsilon\sim\mathcal N(0,\sigma^2I_n).}
$$

Here $X\in\mathbb R^{n\times p}$ is treated as fixed, $\beta$ is an unknown
coefficient vector, and $\sigma^2$ is the variance of each independent error.
The assumption means $E[\varepsilon\mid X]=0$ and
$\operatorname{Var}(\varepsilon\mid X)=\sigma^2I_n$. Normality is needed for
the exact chi-square result below; independence and equal variance are also
substantive modeling assumptions, not consequences of fitting a line.

Assume first that $X$ has full column rank $p<n$. OLS gives

$$
\hat\beta=(X^TX)^{-1}X^Ty.
$$

## 2. Hat matrix, residual-maker, and rank

Define

$$
H=X(X^TX)^{-1}X^T,
\qquad M=I_n-H.
$$

$H$ is called the **hat matrix** because $\hat y=Hy$, and $M$ maps targets to
residuals: $e=y-\hat y=My$. Both are symmetric and idempotent
($H^2=H$, $M^2=M$). They are orthogonal projections onto complementary
subspaces:

$$
\operatorname{rank}(H)=p,
\qquad \operatorname{rank}(M)=n-p.
$$

Because $MX=0$, the residual contains no signal term under the assumed model:

$$
e=My=M(X\beta+\varepsilon)=M\varepsilon.
$$

Thus the RSS is $e^Te=\varepsilon^TM\varepsilon$.

## 3. The degrees-of-freedom theorem

**Theorem (Residual sum of squares).** Under the model above with
$\operatorname{rank}(X)=p$,

$$
\boxed{\frac{\operatorname{RSS}}{\sigma^2}
=\frac{e^Te}{\sigma^2}\sim\chi^2_{n-p}.}
$$

Consequently, $E[\operatorname{RSS}]=(n-p)\sigma^2$ and

$$
\boxed{s^2=\frac{\operatorname{RSS}}{n-p}}
$$

is an unbiased estimator of the error variance $\sigma^2$.

**Proof:**

Since $M$ is symmetric and idempotent with rank $n-p$, an orthogonal matrix
$Q$ diagonalizes it as

$$
M=Q^T\operatorname{diag}(\underbrace{1,\ldots,1}_{n-p},
\underbrace{0,\ldots,0}_{p})Q.
$$

Let $z=Q\varepsilon/\sigma$. Orthogonal rotation preserves a standard normal
distribution, so $z_1,\ldots,z_n$ are independent $\mathcal N(0,1)$ values.
Therefore

$$
\frac{\operatorname{RSS}}{\sigma^2}
=\frac{\varepsilon^TM\varepsilon}{\sigma^2}
=\sum_{i=1}^{n-p}z_i^2
\sim\chi^2_{n-p}.
$$

The expectation of a chi-square random variable with $k$ degrees of freedom
is $k$, yielding both remaining statements.

$\square$

The phrase “degrees of freedom” is not merely a slogan: fitting $p$ independent
coefficient directions uses $p$ dimensions of the $n$-dimensional response
space. Residuals remain only in an $(n-p)$-dimensional orthogonal subspace.
With only an intercept, $p=1$, this reduces to the familiar $n-1$ sample
variance correction.

## 4. Compute it safely

~~~python
import numpy as np

# X_raw has shape (n, d). Add the fitted intercept, so p = d + 1.
X = np.column_stack([np.ones(len(X_raw)), X_raw])
beta_hat, _, rank, _ = np.linalg.lstsq(X, y, rcond=None)
residuals = y - X @ beta_hat
rss = residuals @ residuals
df_resid = len(y) - rank

if df_resid <= 0:
    raise ValueError("Need more observations than the design rank.")

sigma2_hat = rss / df_resid
sigma_hat = np.sqrt(sigma2_hat)
print(rank, df_resid, sigma2_hat, sigma_hat)
~~~

Using \`rank\`, rather than merely the number of matrix columns, makes the
calculation honest when redundant columns are present. In the usual full-rank
case, \`rank == p\` and this is $\operatorname{RSS}/(n-p)$.

## 5. What this estimate does—and does not—mean

$s^2$ estimates the variance of the **irreducible conditional errors**, not
the variance of $y$, nor the average squared error on a fresh test set. Its
units are target-units squared. The residual standard error $s$ is in target
units and describes a typical fitted residual scale.

The exact unbiasedness result depends on a correctly specified linear mean,
independent equal-variance errors, and treating the selected design as fixed.
Heteroskedasticity, correlation, nonlinear mean structure, outliers, or
post-selection inference can invalidate its standard interpretation.

For ridge and lasso, coefficients are not an ordinary rank-$p$ OLS projection;
\`RSS / (n - p)\` is not generally their unbiased noise-variance estimator.
Their effective degrees of freedom require more advanced definitions.

## Key takeaways

- Under $y=X\beta+\varepsilon$ with Gaussian i.i.d. errors, residuals are
  $M\varepsilon$, not raw observations.
- The residual projection has rank $n-p$, giving
  $\operatorname{RSS}/\sigma^2\sim\chi^2_{n-p}$.
- Estimate OLS error variance by $s^2=\operatorname{RSS}/(n-p)$, using the
  design rank and counting an intercept when it was fitted.
