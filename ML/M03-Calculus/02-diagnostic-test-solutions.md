# Calculus Diagnostic Test — Solutions
*ML / M03 — Calculus*

Worked solutions for [01-diagnostic-test.md](./01-diagnostic-test.md).

## Problem 1: Tangent Vector to a Parametrized Curve

Differentiate component by component:

$$
\mathbf r'(t)=\left(2t-2,\ e^t,\ \frac{1}{t+1}\right).
$$

Therefore, at $t=1$ a tangent vector is

$$
\mathbf r'(1)=\left(0,e,\frac12\right).
$$

Any nonzero scalar multiple of this vector is also a tangent vector.

## Problem 2: Gradient

The partial derivatives are

$$
f_x(x,y)=2xy+3e^y,
\qquad
f_y(x,y)=x^2+3xe^y-3y^2.
$$

Hence

$$
\nabla f(x,y)=\left(2xy+3e^y,\ x^2+3xe^y-3y^2\right).
$$

At $(1,0)$,

$$
\nabla f(1,0)=(3,4).
$$

## Problem 3: Gradients and Level Sets

Let $\boldsymbol\gamma(t)$ be any differentiable curve in $L_c$ with
$\boldsymbol\gamma(t_0)=p$. Because every point of this curve lies in the
level set,

$$
f(\boldsymbol\gamma(t))=c
$$

for all $t$ near $t_0$. Differentiate both sides with respect to $t$. The chain
rule gives

$$
\frac{d}{dt}f(\boldsymbol\gamma(t))
=\nabla f(\boldsymbol\gamma(t))\cdot\boldsymbol\gamma'(t)=0.
$$

Evaluating at $t=t_0$ yields

$$
\nabla f(p)\cdot\boldsymbol\gamma'(t_0)=0.
$$

Since $\boldsymbol\gamma'(t_0)$ is an arbitrary tangent vector to the level
set at $p$, $\nabla f(p)$ is orthogonal to every such tangent vector. The
assumption $\nabla f(p)\ne\mathbf0$ ensures that it is a nonzero normal vector.

## Problem 4: Extremum on an Unbounded Region

The gradient is

$$
\nabla F(x,y)=\left(-2(x-2)+y,\ -2(y+1)+x\right).
$$

Setting both components equal to zero gives

$$
2x-y=4,
\qquad
x-2y=2,
$$

so the only critical point is

$$
(x,y)=(2,0).
$$

To identify it globally, complete the square after translating $x$:

$$
\begin{aligned}
F(x,y)
&=9-\left(x-2-\frac y2\right)^2-\frac34y^2\\
&\le9.
\end{aligned}
$$

Equality holds precisely when $y=0$ and $x-2-\frac y2=0$, which is the point
$(2,0)$. Thus the global maximum is $9$, attained at $(2,0)$.

There is no global minimum. For example, with $y=0$,

$$
F(x,0)=9-(x-2)^2\longrightarrow-\infty
\quad\text{as }x\longrightarrow\infty.
$$

Likewise, $F(0,y)=6-(y+1)^2\to-\infty$ as $y\to\infty$. Hence there is no
global minimum.

## Problem 5: Extremum Subject to a Curve Constraint

Let

$$
g(x,y)=x^2+y^2.
$$

The Lagrange-multiplier equations for $g(x,y)=5$ are

$$
\nabla f=\lambda\nabla g,
$$

so

$$
(y,x)=\lambda(2x,2y).
$$

Equivalently,

$$
y=2\lambda x,
\qquad x=2\lambda y,
\qquad x^2+y^2=5.
$$

Neither $x$ nor $y$ can be zero: if one were zero, the first two equations
would force the other to be zero, contradicting the constraint. Substituting
the first equation into the second therefore gives

$$
x=4\lambda^2x,
\qquad\text{so}\qquad \lambda=\pm\frac12.
$$

When $\lambda=\frac12$, $y=x$. The constraint gives

$$
(x,y)=\left(\sqrt{\frac52},\sqrt{\frac52}\right)
\quad\text{or}\quad
\left(-\sqrt{\frac52},-\sqrt{\frac52}\right),
$$

and $f(x,y)=\frac52$. When $\lambda=-\frac12$, $y=-x$. This gives

$$
(x,y)=\left(\sqrt{\frac52},-\sqrt{\frac52}\right)
\quad\text{or}\quad
\left(-\sqrt{\frac52},\sqrt{\frac52}\right),
$$

and $f(x,y)=-\frac52$.

Because the constraint is a closed and bounded circle and $f$ is continuous,
these extrema are absolute. Therefore the absolute maximum is $\frac52$, and
the absolute minimum is $-\frac52$.
