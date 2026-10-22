# Lesson 2: Regularization — Ridge and Lasso
*ML / M06 — Supervised Learning*

## The question

What should we do when OLS coefficients are unstable, overly large, or prone
to fitting noise rather than a relationship that generalizes?

## 1. The regularization idea

Regularization adds a cost for complex coefficient vectors. It deliberately
accepts some training bias in exchange for lower variance and often better
test performance. Standardize feature columns first: a penalty on a
coefficient has no comparable meaning when one feature is measured in dollars
and another in millimeters.

Usually leave the intercept unpenalized. For centered features and targets,
the fitted intercept is handled separately; in an augmented matrix, set the
intercept's penalty weight to zero.

## 2. Ridge: an $L_2$ penalty

Ridge regression minimizes

$$
J_{\mathrm{ridge}}(\beta)=\lVert y-X\beta\rVert_2^2+
\lambda\lVert\beta\rVert_2^2,
\qquad \lambda\ge0.
$$

For an unpenalized intercept, replace $\lambda I$ below with a diagonal matrix
whose first entry is $0$. Differentiating gives

$$
(X^TX+\lambda I)\hat\beta_{\mathrm{ridge}}=X^Ty.
$$

For $\lambda>0$, $X^TX+\lambda I$ is positive definite: for nonzero $v$,

$$
v^T(X^TX+\lambda I)v=\lVert Xv\rVert_2^2+\lambda\lVert v\rVert_2^2>0.
$$

So ridge has a unique solution even if features are collinear. It shrinks
coefficients smoothly toward zero but typically does not set them exactly to
zero.

## Homework: derive the ridge normal formula

Starting from the ridge objective

$$
J_{mathrm{ridge}}(\beta)=\lVert y-X\beta\rVert_2^2+
\lambda\lVert\beta\rVert_2^2,
$$

derive the closed-form ridge estimator. Expand the squared terms, compute the
gradient with respect to $\beta$, set it equal to zero, and solve the resulting
linear system to show that

$$
\hat\beta_{\mathrm{ridge}}=(X^TX+\lambda I)^{-1}X^Ty.
$$

Then explain why the inverse exists when $\lambda>0$, even if $X$ does not
have full column rank. Finally, state how the formula changes when the design
matrix includes an unpenalized intercept.

## 3. Lasso: an $L_1$ penalty

Lasso regression minimizes

$$
J_{\mathrm{lasso}}(\beta)=\lVert y-X\beta\rVert_2^2+
\lambda\lVert\beta\rVert_1,
\qquad \lVert\beta\rVert_1=\sum_{j=1}^p|\beta_j|.
$$

The absolute-value function has a corner at zero, so ordinary differentiation
does not apply there. Its subgradient is

$$
\partial |t|=
\begin{cases}
\{1\},&t>0,\\
[-1,1],&t=0,\\
\{-1\},&t<0.
\end{cases}
$$

That corner is why lasso can produce exact zeros and therefore a sparse model.
Coordinate-descent implementations repeatedly use a soft-thresholding step,

$$
S_\tau(z)=\operatorname{sign}(z)\max(|z|-\tau,0).
$$

Lasso is valuable for feature selection, but with highly correlated features
it may select one arbitrary representative; do not interpret selection as a
causal verdict.

## 4. Choosing between them

| Method | Penalty | Typical coefficient behavior | Useful when |
| --- | --- | --- |
| OLS | none | May be unstable under collinearity | Data are ample and conditioning is good. |
| Ridge | $L_2$ | All coefficients shrink | Predictors are correlated; stable prediction matters. |
| Lasso | $L_1$ | Some coefficients become exactly zero | A compact feature set is useful. |

Choose $\lambda$ using validation data or cross-validation, with preprocessing
fitted inside each training fold. Never choose it by the training loss alone:
larger $\lambda$ always makes the regularized training objective different and
can mask poor generalization.

## 5. A NumPy ridge solve

~~~python
import numpy as np

# X has a leading ones column. Do not penalize its intercept coefficient.
penalty = np.eye(X.shape[1])
penalty[0, 0] = 0.0
lam = 1.0

beta_ridge = np.linalg.solve(X.T @ X + lam * penalty, X.T @ y)
~~~

The relative scaling of the squared-loss and penalty terms varies across
libraries: some use $(1/n)\lVert y-X\beta\rVert^2+\alpha\lVert\beta\rVert^2$.
Check the documented objective before copying a numeric value of $\lambda$.

## Key takeaways

- Regularization trades bias for lower variance and should be paired with
  feature scaling and validation.
- Ridge adds $L_2$ shrinkage and makes the penalized system positive definite.
- Lasso adds $L_1$ shrinkage; its corner at zero enables sparse coefficients.
- Keep the intercept out of the penalty unless there is a deliberate reason
  not to.
