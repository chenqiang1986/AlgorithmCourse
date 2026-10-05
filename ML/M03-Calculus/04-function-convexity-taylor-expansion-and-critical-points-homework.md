# Homework: Convexity, Taylor Expansion, and Critical Points
*ML / M03 — Calculus*

Use the [Lesson 4 notes](./04-function-convexity-taylor-expansion-and-critical-points.md)
as a reference. Show derivative and Hessian calculations. When classifying a
critical point, state the test you use rather than reporting only a label.

## 1. One-dimensional convexity: chords and tangents

Let $f(x)=x^2+2x$.

1. Verify directly that, for $x=-1$, $y=3$, and $t=\frac14$,

   $$
   f\bigl(tx+(1-t)y\bigr)\le tf(x)+(1-t)f(y).
   $$

2. Find the tangent line to $f$ at $a=1$.
3. Verify at $x=-2$ and $x=4$ that

   $$
   f(x)\ge f(a)+f'(a)(x-a).
   $$

4. Compute $f''(x)$ and explain how it is consistent with both inequalities.

## 2. Convex, concave, or neither?

For each function, use the second derivative to decide whether it is convex,
concave, or neither on the specified interval. Briefly explain your answer.

1. $f(x)=e^x$ on $\mathbb R$.
2. $g(x)=\log x$ on $(0,\infty)$.
3. $h(x)=x^3$ on $\mathbb R$.
4. $p(x)=x^4$ on $\mathbb R$. Is it strictly convex? Does $p''(x)$ remain
   positive at every point?

## 3. Hessian and convexity

Consider

$$
f(x,y)=3x^2+2xy+2y^2-4x+6y.
$$

1. Compute $\nabla f$ and $H_f$.
2. Verify that $H_f$ is positive definite using the $2\times2$ determinant
   criterion.
3. Find the unique critical point.
4. Explain why that critical point is the global minimum, not merely a local
   minimum.

## 4. Directional curvature

Let

$$
f(x,y)=x^2+4xy+5y^2.
$$

1. Compute $H_f$.
2. Let $\mathbf e=\frac1{\sqrt2}(1,-1)^T$ and define

   $$
   g(t)=f\bigl((1,0)^T+t\mathbf e\bigr).
   $$

   Write $g(t)$ explicitly and compute $g''(t)$.
3. Compute $\mathbf e^TH_f\mathbf e$ and verify that it agrees with part 2.
4. Is $f$ convex on $\mathbb R^2$? Justify your answer using the Hessian.

## 5. Second-order Taylor approximation

Let

$$
f(x,y)=\sin x\,e^y.
$$

1. Find $f(0,0)$, $\nabla f(0,0)$, and $H_f(0,0)$.
2. Write the second-order Taylor polynomial of $f$ about $(0,0)$.
3. Use it to approximate $f(0.1,-0.2)$.
4. Use a calculator to find $\sin(0.1)e^{-0.2}$ and compare it with your
   approximation. Report the absolute error.

## 6. Classify critical points

For each function, find all critical points and classify each as a local
minimum, local maximum, saddle point, or inconclusive under the second-
derivative test. If the test is inconclusive, determine the actual behavior
by examining the function along one or more paths.

1. $f(x,y)=x^2+xy+y^2-6x$.
2. $g(x,y)=x^2-y^2+4x-2y$.
3. $h(x,y)=x^4+y^4$.
4. $q(x,y)=x^4-y^4$.

## 7. Hessians and critical points

At a critical point, a twice-differentiable function has the following Hessian
matrices. Classify the critical point as a strict local minimum, a strict local
maximum, saddle point, or inconclusive from this test.

$$
H_1=\begin{pmatrix}6&1\\1&3\end{pmatrix},
\qquad
H_2=\begin{pmatrix}-2&0\\0&-5\end{pmatrix},
\qquad
H_3=\begin{pmatrix}1&0\\0&-4\end{pmatrix},
\qquad
H_4=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
$$

## 8. Least squares and a global minimum

For the data matrix and target vector

$$
X=\begin{bmatrix}1&0\\1&1\\1&2\end{bmatrix},
\qquad
\mathbf y=\begin{bmatrix}1\\2\\2\end{bmatrix},
$$

consider

$$
L(\boldsymbol\beta)=\frac12\|X\boldsymbol\beta-\mathbf y\|^2,
\qquad
\boldsymbol\beta=\begin{bmatrix}\beta_0\\\beta_1\end{bmatrix}.
$$

1. Compute $X^TX$ and show that it is positive definite.
2. Use $\nabla L=X^T(X\boldsymbol\beta-\mathbf y)$ to solve for the
   minimizer $\boldsymbol\beta_*$.
3. Explain why your answer is the unique global minimizer.

## 9. Derive directional first and second derivatives with index notation

Let $f:\mathbb R^n\to\mathbb R$ be twice continuously differentiable, fix
$\mathbf x_0\in\mathbb R^n$, and let $\mathbf e\in\mathbb R^n$ be a unit
vector. Define

$$
g(t)=f(\mathbf x_0+t\mathbf e).
$$

Using Einstein summation notation (a repeated index is summed from $1$ to
$n$), derive both formulas below. State clearly where the chain rule is used.

$$
g'(t)=\frac{\partial f}{\partial x_i}(\mathbf x_0+t\mathbf e)e_i
=\nabla f(\mathbf x_0+t\mathbf e)^T\mathbf e,
$$

and

$$
g''(t)=\frac{\partial^2f}{\partial x_i\partial x_j}
(\mathbf x_0+t\mathbf e)e_i e_j
=\mathbf e^T H_f(\mathbf x_0+t\mathbf e)\mathbf e.
$$

Then explain in one or two sentences how $g''(t)\ge0$ for every unit vector
$\mathbf e$ leads to the positive-semidefinite Hessian condition.

## 10. Challenge — derive the multivariable second-order Taylor expansion

Let $f:\mathbb R^n\to\mathbb R$ be twice continuously differentiable near
$\mathbf a$, and let $\mathbf h$ be a small displacement vector. Derive the
second-order Taylor approximation

$$
f(\mathbf a+\mathbf h)
=f(\mathbf a)+\nabla f(\mathbf a)^T\mathbf h
+\frac12\mathbf h^TH_f(\mathbf a)\mathbf h+o(\|\mathbf h\|^2).
$$

**Hint:** If $\mathbf h\ne\mathbf0$, write
$\mathbf h=r\mathbf e$, where $r=\|\mathbf h\|$ and $\mathbf e$ is a unit
vector. Restrict $f$ to $g(t)=f(\mathbf a+t\mathbf e)$, then apply the
one-variable second-order Taylor expansion to $g(r)$.
