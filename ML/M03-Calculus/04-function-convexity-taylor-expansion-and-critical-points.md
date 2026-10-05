# Lesson 4: Convexity, Second-Order Taylor Expansion, and Critical Points
*ML / M03 — Calculus*

## The question

Many machine-learning tasks amount to minimizing a **loss function**. Before
choosing an optimization method, we want to know the shape of that function:

- Does it curve upward everywhere, so that every local minimum is globally
  best?
- Near a candidate point, does the surface look like a bowl, a hill, or a
  saddle?
- How can derivatives predict that local shape?

This lesson connects those questions through the gradient, the Hessian, and a
second-order Taylor approximation.

## Learning goals

By the end of this lesson, you should be able to:

1. recognize and use the definition of a convex function;
2. write a second-order Taylor approximation for a function of several
   variables;
3. find critical points by solving $\nabla f=\mathbf 0$;
4. classify nondegenerate critical points using a Hessian; and
5. explain why convexity makes optimization more reliable.

## 1. Curvature in one variable

For a twice-differentiable function $f(x)$:

$$
f''(x)>0 \quad\text{means the graph bends upward},
$$

while $f''(x)<0$ means it bends downward. A point with $f'(a)=0$ is a
**critical point**. The one-variable second-derivative test says:

$$
\begin{array}{c|c}
f''(a)>0 & \text{local minimum}\\
f''(a)<0 & \text{local maximum}\\
f''(a)=0 & \text{test is inconclusive}
\end{array}
$$

In U.S. precalculus terminology, a graph that bends upward is **concave up**.
Equivalently, $f$ is convex on an interval if every chord lies on or above
the graph: for all $x,y$ in the interval and $0\le t\le1$,

$$
\boxed{f\bigl(tx+(1-t)y\bigr)\le tf(x)+(1-t)f(y).}
$$

If $f$ is differentiable and convex on an interval, then its graph also lies
above each of its tangent lines: for every $a$ and $x$ in that interval,

$$
\boxed{f(x)\ge f(a)+f'(a)(x-a).}
$$

For a twice-differentiable function, $f''\ge0$ throughout an interval is a
standard sufficient condition for this convex (concave-up) behavior.

For example, $f(x)=x^2$ has $f'(0)=0$ and $f''(0)=2>0$, so $0$ is a local
minimum. In contrast, $f(x)=x^3$ has $f'(0)=f''(0)=0$, but it has neither a
local minimum nor a local maximum. A zero second derivative does not settle
the question.

## 2. Convex functions: the chord test

A set $C\subseteq\mathbb R^n$ is **convex** if the entire line segment
between any two points in $C$ stays in $C$. A function $f:C\to\mathbb R$ is
**convex** if, for every $\mathbf x,\mathbf y\in C$ and $0\leq t\leq1$,

$$
\boxed{f\bigl(t\mathbf x+(1-t)\mathbf y\bigr)
\leq tf(\mathbf x)+(1-t)f(\mathbf y).}
$$

Geometrically, the graph of a convex function lies on or below the straight
chord joining any two points on its graph.

<svg viewBox="0 0 720 300" width="720" role="img" aria-labelledby="convex-title convex-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="convex-title">Chord above a convex curve</title>
  <desc id="convex-desc">The curve y equals x squared lies below the chord connecting two marked points. A point on the chord corresponds to a weighted average.</desc>
  <rect width="720" height="300" rx="12" fill="#fffdf8"/>
  <g stroke="#94a3b8" stroke-width="1.5"><path d="M60 245H675"/><path d="M365 270V28"/></g>
  <g font-family="sans-serif" font-size="15" fill="#475569"><text x="660" y="237">x</text><text x="374" y="45">f(x)</text><text x="350" y="263">0</text></g>
  <path d="M135 65 Q365 260 595 65" fill="none" stroke="#0f766e" stroke-width="4"/>
  <path d="M135 65 L595 65" stroke="#c2410c" stroke-width="3" stroke-dasharray="8 6"/>
  <circle cx="135" cy="65" r="5" fill="#111827"/><circle cx="595" cy="65" r="5" fill="#111827"/>
  <circle cx="365" cy="162.5" r="5" fill="#0f766e"/><circle cx="365" cy="65" r="5" fill="#c2410c"/>
  <g font-family="sans-serif" font-size="17"><text x="94" y="54" fill="#111827">(x, f(x))</text><text x="542" y="54" fill="#111827">(y, f(y))</text><text x="374" y="157" fill="#0f766e">f(tx+(1−t)y)</text><text x="376" y="88" fill="#9a3412">tf(x)+(1−t)f(y)</text><text x="465" y="193" fill="#0f766e">convex graph</text></g>
</svg>

For a differentiable convex function, the tangent plane is always a global
underestimate:

$$
\boxed{f(\mathbf y)\ge f(\mathbf x)+\nabla f(\mathbf x)^T(\mathbf y-\mathbf x).}
$$

This is the multivariable version of “a convex curve stays above each of its
tangent lines.”

### Why convexity matters

If $f$ is differentiable and convex on a convex domain, then

$$
\nabla f(\mathbf x_*)=\mathbf0
\quad\Longrightarrow\quad
\mathbf x_*\text{ is a global minimum.}
$$

Indeed, substituting $\nabla f(\mathbf x_*)=\mathbf0$ into the tangent-plane
inequality gives $f(\mathbf y)\ge f(\mathbf x_*)$ for every allowed
$\mathbf y$. Thus a stationary point cannot be a misleading local minimum.

## 3. The Hessian: curvature in several directions

For $f(x_1,\ldots,x_n)$, the **gradient** collects first partial derivatives:

$$
\nabla f=
\begin{bmatrix}f_{x_1}\\ \vdots\\ f_{x_n}\end{bmatrix}.
$$

The **Hessian** collects second partial derivatives:

$$
H_f(\mathbf x)=
\begin{bmatrix}
f_{x_1x_1} & \cdots & f_{x_1x_n}\\
\vdots & \ddots & \vdots\\
f_{x_nx_1} & \cdots & f_{x_nx_n}
\end{bmatrix}.
$$

When the mixed partial derivatives are continuous, $f_{x_ix_j}=f_{x_jx_i}$,
so the Hessian is symmetric. For two variables,

$$
H_f(x,y)=\begin{bmatrix}f_{xx}&f_{xy}\\f_{yx}&f_{yy}\end{bmatrix}.
$$

### Deriving the Hessian criterion from one-dimensional convexity

Fix a point $\mathbf x_0$ in the domain and a unit vector $\mathbf e$. Along
the line through $\mathbf x_0$ in direction $\mathbf e$, restrict $f$ to the
one-variable function

$$
g(t)=f(\mathbf x_0+t\mathbf e).
$$

Whenever the relevant part of that line remains in the domain, the
multivariable chord test becomes the ordinary one-dimensional chord test:

$$
\begin{aligned}
g\bigl(ts+(1-t)r\bigr)
&=f\bigl(t(\mathbf x_0+s\mathbf e)+(1-t)(\mathbf x_0+r\mathbf e)\bigr)\\
&\le t g(s)+(1-t)g(r).
\end{aligned}
$$

Thus, $f$ is convex exactly when every such line restriction $g$ is convex.
For a twice-differentiable $g$, the one-dimensional result says convexity is
equivalent to $g''(t)\ge0$ throughout its interval.

Apply the chain rule to $g(t)$:

$$
g'(t)=\nabla f(\mathbf x_0+t\mathbf e)^T\mathbf e,
$$

and differentiate again:

$$
\boxed{g''(t)=\mathbf e^T H_f(\mathbf x_0+t\mathbf e)\mathbf e.}
$$

So convexity requires nonnegative curvature in **every** direction. More
generally, for a vector $\mathbf v\ne\mathbf0$, the quantity

$$
\mathbf v^T H_f(\mathbf x)\mathbf v
$$

measures the second-order curvature at $\mathbf x$ in the direction
$\mathbf v$ (up to the positive scale factor $\|\mathbf v\|^2$). A symmetric
matrix $H$ is:

$$
\begin{array}{c|c}
\mathbf v^TH\mathbf v>0\ \text{for all }\mathbf v\ne0 & \text{positive definite (PD)}\\
\mathbf v^TH\mathbf v\ge0\ \text{for all }\mathbf v & \text{positive semidefinite (PSD)}\\
\mathbf v^TH\mathbf v<0\ \text{for all }\mathbf v\ne0 & \text{negative definite (ND)}
\end{array}
$$

A twice-differentiable function is convex on a convex region when its Hessian
is PSD everywhere in that region: the display for $g''(t)$ proves the
connection in both directions. If the Hessian is PD everywhere, the function
is strictly convex, so it has at most one minimizer. PD is stronger than is
needed for convexity; for example, $f(x)=x^4$ is strictly convex but has
$f''(0)=0$.

For a $2\times2$ symmetric Hessian $\begin{bmatrix}a&b\\b&c\end{bmatrix}$:

$$
\text{PD}\iff a>0\text{ and }ac-b^2>0,
\qquad
\text{ND}\iff a<0\text{ and }ac-b^2>0.
$$

## 4. Second-order Taylor expansion

Near a base point $\mathbf a$, let $\mathbf h=\mathbf x-\mathbf a$. The
second-order Taylor approximation is

$$
\boxed{f(\mathbf a+\mathbf h)\approx
f(\mathbf a)+\nabla f(\mathbf a)^T\mathbf h+
\frac12\mathbf h^T H_f(\mathbf a)\mathbf h.}
$$

The constant term gives the height at $\mathbf a$; the gradient gives the
tilt; the Hessian gives the local curvature. More precisely, if $f$ has
enough smoothness, the omitted error is $o(\|\mathbf h\|^2)$ as
$\mathbf h\to\mathbf0$.

For $f(x,y)$ expanded about $(a,b)$, this becomes

$$
\begin{aligned}
f(x,y)\approx{}&f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b)\\
&+\frac12\left[f_{xx}(a,b)(x-a)^2
+2f_{xy}(a,b)(x-a)(y-b)
+f_{yy}(a,b)(y-b)^2\right].
\end{aligned}
$$

### Example: approximate a nonlinear function

Let

$$
f(x,y)=e^x\cos y
$$

and expand about $(0,0)$. Here $f(0,0)=1$,

$$
\nabla f(0,0)=\begin{bmatrix}1\\0\end{bmatrix},
\qquad
H_f(0,0)=\begin{bmatrix}1&0\\0&-1\end{bmatrix}.
$$

Therefore

$$
e^x\cos y\approx 1+x+\frac12x^2-\frac12y^2.
$$

At $(x,y)=(0.1,0.2)$, this predicts $1+0.1+0.005-0.02=1.085$; the actual
value is about $1.083$. Taylor approximations are local tools: their quality
usually declines farther from the base point.

## 5. Critical points and the second-derivative test

An interior point $\mathbf a$ is a **critical point** if

$$
\nabla f(\mathbf a)=\mathbf0
$$

(or if a needed partial derivative does not exist). At a smooth critical
point, the linear term in the Taylor approximation disappears:

$$
f(\mathbf a+\mathbf h)\approx f(\mathbf a)+
\frac12\mathbf h^TH_f(\mathbf a)\mathbf h.
$$

Thus the Hessian determines the local shape when it is definite.

| Hessian at a critical point | Classification |
| --- | --- |
| Positive definite (all eigenvalues positive) | strict local minimum |
| Negative definite (all eigenvalues negative) | strict local maximum |
| Indefinite (at least one positive and at least one negative eigenvalue; equivalently, positive curvature in some directions and negative curvature in others) | saddle point |
| Positive- or negative-semidefinite but not definite (at least one eigenvalue is zero) | inconclusive; examine higher-order terms or the function directly |

A zero eigenvalue makes the Hessian **singular**. A singular Hessian can still
be indefinite; if it has both a positive and a negative eigenvalue, the point
is still a saddle point.

For a two-variable function, compute

$$
D=f_{xx}f_{yy}-(f_{xy})^2=\det H_f.
$$

Then, at a critical point:

$$
\begin{array}{c|c}
D>0,\ f_{xx}>0 & \text{local minimum}\\
D>0,\ f_{xx}<0 & \text{local maximum}\\
D<0 & \text{saddle point}\\
D=0 & \text{inconclusive}
\end{array}
$$

### Complete example: minimum, maximum, and saddle

Consider

$$
f(x,y)=x^3-3x+y^2.
$$

First find critical points:

$$
\nabla f=(3x^2-3,\,2y)=\mathbf0
\quad\Longrightarrow\quad (x,y)=(1,0),\ (-1,0).
$$

The Hessian is

$$
H_f(x,y)=\begin{bmatrix}6x&0\\0&2\end{bmatrix}.
$$

At $(1,0)$, $H_f=\begin{bmatrix}6&0\\0&2\end{bmatrix}$ is PD, so $(1,0)$
is a local minimum. At $(-1,0)$,

$$
H_f=\begin{bmatrix}-6&0\\0&2\end{bmatrix}
$$

is indefinite, so $(-1,0)$ is a saddle point. There is no local maximum.

## 6. A useful ML example: least squares is convex

For a data matrix $X$, target vector $\mathbf y$, and parameter vector
$\boldsymbol\beta$, define the squared-error loss

$$
L(\boldsymbol\beta)=\frac12\|X\boldsymbol\beta-\mathbf y\|^2.
$$

Its gradient and Hessian are

$$
\nabla L=X^T(X\boldsymbol\beta-\mathbf y),
\qquad H_L=X^TX.
$$

For every vector $\mathbf v$,

$$
\mathbf v^TX^TX\mathbf v=\|X\mathbf v\|^2\ge0.
$$

So $X^TX$ is PSD and least squares is convex. Every solution of
$\nabla L=\mathbf0$ is therefore a global minimizer. If the columns of $X$
are linearly independent, $X^TX$ is PD, and that minimizer is unique.

## 7. Reliable workflow

To analyze an unconstrained smooth function $f(x,y)$:

1. State the domain and check any boundary separately.
2. Compute $f_x$ and $f_y$, then solve $f_x=f_y=0$.
3. Compute $f_{xx}$, $f_{xy}$, and $f_{yy}$.
4. At each critical point, compute $D=f_{xx}f_{yy}-f_{xy}^2$ and apply the
   table above.
5. If $D=0$, do not guess: inspect $f$ along useful paths or use higher-order
   terms.
6. To claim an absolute extremum, also consider the boundary and behavior at
   infinity. A local classification alone is not enough.

## Check your understanding

1. Is $f(x,y)=x^2+y^2$ convex? Use its Hessian to justify your answer.
2. Find and classify the critical point of $g(x,y)=x^2-y^2$.
3. Why does $D<0$ indicate a saddle rather than a maximum or minimum?
4. Give one reason that a singular Hessian cannot settle the classification.

Practice next: [Convexity, Taylor Expansion, and Critical Points Homework](./04-function-convexity-taylor-expansion-and-critical-points-homework.md).
