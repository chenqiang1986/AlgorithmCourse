# Lesson 3: Lagrange Multipliers
*ML / M03 — Calculus*

## The question

How can we maximize or minimize a function when the input must remain on a
curve? For example, choose $(x,y)$ to maximize a score $f(x,y)$ subject to a
fixed resource constraint

$$
g(x,y)=c.
$$

We will use the constraint to narrow the possible answers, then compare the
values of $f$ at those candidates. The central condition is

$$
\boxed{\nabla f(x,y)=\lambda\nabla g(x,y),\qquad g(x,y)=c.}
$$

Here $\lambda$ is an additional unknown, called a **Lagrange multiplier**.

## 1. Why the gradients must be parallel

The curves $f(x,y)=k$ are the **contours** (or level curves) of $f$. At a
point on a contour, $\nabla f$ is perpendicular to that contour. Likewise,
$\nabla g$ is perpendicular to the constraint curve $g=c$.

At a constrained maximum or minimum, the contour of $f$ through the point
just touches the constraint: both curves have the same tangent line. Their
normal vectors are therefore parallel.

The diagram uses

$$
f(x,y)=13x^2-8xy+7y^2,\qquad g(x,y)=x^2+y^2,\qquad g=5.
$$

The contours of $f$ are rotated ellipses. At $P=(1,2)$, the $f$-contour and
the constraint circle are tangent, and

$$
\nabla f(P)=(10,20),\qquad \nabla g(P)=(2,4),
\qquad \nabla f(P)=5\nabla g(P).
$$

<svg viewBox="0 0 720 420" width="720" role="img" aria-labelledby="contour-title contour-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="contour-title">An elliptical contour of f tangent to a constraint circle</title>
  <desc id="contour-desc">Several rotated elliptical contours of a quadratic function and a circle g equals 5 touch at P. The gradients of f and g at P point in parallel directions.</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#155e75"/></marker>
    <marker id="arrowOrange" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#c2410c"/></marker>
  </defs>
  <rect width="720" height="420" fill="#fffdf8" rx="12"/>
  <g stroke="#94a3b8" stroke-width="1.5"><path d="M70 350H670"/><path d="M175 390V35"/></g>
  <g fill="#64748b" font-family="sans-serif" font-size="15"><text x="654" y="342">x</text><text x="183" y="51">y</text><text x="160" y="370">0</text></g>
  <!-- Constraint: x squared plus y squared equals 5, centered at the origin -->
  <circle cx="175" cy="350" r="158.1" fill="none" stroke="#c2410c" stroke-width="4"/>
  <text x="292" y="230" fill="#9a3412" font-family="sans-serif" font-size="18">constraint: g(x,y) = 5</text>
  <!-- Rotated elliptical contours of 13x squared minus 8xy plus 7y squared;
       the middle ellipse f=25 is tangent at P=(1,2). -->
  <g fill="none" stroke="#0f766e" stroke-width="2.5" stroke-dasharray="8 6">
    <ellipse cx="175" cy="350" rx="109.5" ry="63.2" transform="rotate(-63.435 175 350)"/>
    <ellipse cx="175" cy="350" rx="158.1" ry="91.3" transform="rotate(-63.435 175 350)" stroke-width="3.5"/>
    <ellipse cx="175" cy="350" rx="212.1" ry="122.5" transform="rotate(-63.435 175 350)"/>
  </g>
  <text x="425" y="88" fill="#0f766e" font-family="sans-serif" font-size="18">elliptical contours of f</text>
  <!-- P is coordinates (1,2), at pixel (245, 208.6) -->
  <circle cx="245.7" cy="208.6" r="6" fill="#111827"/>
  <text x="254" y="202" fill="#111827" font-family="sans-serif" font-size="17">P = (1, 2)</text>
  <!-- The arrow lengths reinforce that gradient f is five times gradient g. -->
  <path d="M245.7 208.6 L335.1 29.8" stroke="#155e75" stroke-width="4" marker-end="url(#arrow)"/>
  <text x="343" y="42" fill="#155e75" font-family="sans-serif" font-size="17">∇f = (10, 20)</text>
  <path d="M245.7 208.6 L263.6 172.8" stroke="#c2410c" stroke-width="4" marker-end="url(#arrowOrange)"/>
  <text x="269" y="175" fill="#c2410c" font-family="sans-serif" font-size="17">∇g = (2, 4)</text>
  <path d="M205 188.25 L335 253.25" stroke="#475569" stroke-width="2"/>
  <text x="335" y="265" fill="#475569" font-family="sans-serif" font-size="15">shared tangent</text>
</svg>

The multiplier equation says exactly “parallel” in algebra: two nonzero
vectors are parallel precisely when one is a scalar multiple of the other.
The multiplier may be positive or negative, so the gradients can point in the
same or opposite directions.

## 2. Deriving the condition from allowable motion

**Theorem (Lagrange Multiplier Condition).** Let $P$ be a constrained local
extremum of $f$ on the smooth curve $g(x,y)=c$. If
$\nabla g(P)\ne\mathbf0$, then there is a scalar $\lambda$ such that

$$
\nabla f(P)=\lambda\nabla g(P).
$$

**Proof:**

Let $\mathbf r(t)$ be any differentiable path that stays on the constraint
and passes through a constrained extremum $P$ at $t=0$. Since $g(\mathbf
r(t))=c$ is constant, the chain rule gives

$$
\nabla g(P)\cdot\mathbf r'(0)=0.
$$

Thus $\nabla g(P)$ is perpendicular to every allowed tangent direction.
Also, because $f(\mathbf r(t))$ has an ordinary one-variable extremum at
$t=0$,

$$
\nabla f(P)\cdot\mathbf r'(0)=0.
$$

Both gradients are perpendicular to the same tangent line. Provided
$\nabla g(P)\ne\mathbf0$ (a **regular** point of the constraint), they must
be parallel. Hence $\nabla f(P)=\lambda\nabla g(P)$.

$\square$

## 3. The Lagrange helper function

**Definition (Lagrangian).** For an objective $f$ and equality constraint
$g(x,y)=c$, the **Lagrangian** (or Lagrange helper function) is

$$
\mathcal L(x,y,\lambda)=f(x,y)-\lambda\bigl(g(x,y)-c\bigr).
$$

Taking its gradient with respect to all three variables gives

$$
\begin{aligned}
\mathcal L_x&=f_x-\lambda g_x,\\
\mathcal L_y&=f_y-\lambda g_y,\\
\mathcal L_\lambda&=-(g-c).
\end{aligned}
$$

So a critical point of $\mathcal L$ satisfies

$$
\mathcal L_x=\mathcal L_y=\mathcal L_\lambda=0
\quad\Longleftrightarrow\quad
\begin{cases}
\nabla f=\lambda\nabla g,\\
g=c.
\end{cases}
$$

This is not a new condition hidden in notation: the first two equations say
the gradients are parallel, and the third puts the point back on the
constraint. The Lagrangian simply packages all required equations into “find
a critical point.”

## 4. A complete example

**Example (Largest and Smallest Values on a Circle).** Find the largest and
smallest values of

$$
f(x,y)=x+2y
$$

on the circle $x^2+y^2=5$.

**Solution:**

1. Write the Lagrange multiplier helper function:

$$
\mathcal L(x,y,\lambda)=x+2y-\lambda(x^2+y^2-5).
$$

2. Set every partial derivative of $\mathcal L$ equal to zero:

$$
\begin{cases}
\mathcal L_x=1-2\lambda x=0,\\
\mathcal L_y=2-2\lambda y=0,\\
\mathcal L_\lambda=-(x^2+y^2-5)=0.
\end{cases}
$$

3. The first two equations give $x=1/(2\lambda)$ and $y=1/\lambda$.
Substitute into the third equation:

$$
\frac1{4\lambda^2}+\frac1{\lambda^2}=5
\quad\Longrightarrow\quad
\lambda=\pm\frac12.
$$

Thus the candidates are $(1,2)$ and $(-1,-2)$.

4. Check the objective value at each candidate:

$$
\begin{array}{c|c}
(x,y) & f(x,y)\\ \hline
(1,2) & 5\\
(-1,-2) & -5
\end{array}
$$

Because the circle is closed and bounded and $f$ is continuous, absolute
extrema exist. Therefore the maximum is $5$ at $(1,2)$ and the minimum is
$-5$ at $(-1,-2)$.

$\square$

## 5. Reliable workflow

For an extremum of $f$ subject to equality restrictions
$g_i(\mathbf x)=c_i$ (including the one-constraint case):

1. Write the Lagrange multiplier helper function
   $\mathcal L=f-\sum_i\lambda_i(g_i-c_i)$.
2. Set every partial derivative of $\mathcal L$—with respect to the input
   variables and each multiplier—equal to zero.
3. Solve the resulting system, keeping every real feasible candidate.
4. Evaluate $f$ at every candidate and compare the values. State why
   absolute extrema exist when needed, for example when the feasible set is
   closed and bounded and $f$ is continuous.

Do not divide by $x$, $y$, or $\lambda$ before checking whether it could be
zero. That shortcut can silently discard valid candidates.

## 6. Multiple equality constraints

Suppose that $f:\mathbb R^n\to\mathbb R$ is optimized subject to $m$
restrictions

$$
g_1(\mathbf x)=c_1,\qquad \ldots,\qquad g_m(\mathbf x)=c_m.
$$

**Theorem (Multiple-Constraint Lagrange Multiplier Condition).** Let
$\mathbf p$ be a constrained local extremum of $f$. If the constraint
gradients $\nabla g_1(\mathbf p),\ldots,\nabla g_m(\mathbf p)$ are linearly
independent, then scalars $\lambda_1,\ldots,\lambda_m$ exist such that

$$
\nabla f(\mathbf p)
=\lambda_1\nabla g_1(\mathbf p)+\cdots
+\lambda_m\nabla g_m(\mathbf p).
$$

**Proof:**

Assume for contradiction that $\nabla f(\mathbf p)$ is not a linear
combination of the constraint gradients. Apply Gram--Schmidt to the ordered
list

$$
\nabla g_1(\mathbf p),\ \nabla g_2(\mathbf p),\ \ldots,\
\nabla g_m(\mathbf p),\ \nabla f(\mathbf p).
$$

Because the first $m$ vectors are linearly independent, this produces
orthonormal vectors $\mathbf v_1,\ldots,\mathbf v_m,\mathbf r_f$. Each
$\nabla g_i(\mathbf p)$ is a linear combination of
$\mathbf v_1,\ldots,\mathbf v_i$. The final vector $\mathbf r_f$ is
orthogonal to every constraint gradient, so

$$
\nabla g_i(\mathbf p)\cdot\mathbf r_f=0
\qquad (i=1,\ldots,m).
$$

Thus $\mathbf r_f$ is a tangent direction of the constrained surface: moving
in that direction preserves every constraint to first order. At a regular
point, every such tangent direction is realized by a curve on the constrained
surface. But Gram--Schmidt also writes

$$
\nabla f(\mathbf p)=a_1\mathbf v_1+\cdots+a_m\mathbf v_m
+a_{m+1}\mathbf r_f,
$$

where $a_{m+1}\ne0$; otherwise $\nabla f(\mathbf p)$ would have been a
linear combination of the constraint gradients. Therefore

$$
\nabla f(\mathbf p)\cdot\mathbf r_f=a_{m+1}\ne0.
$$

This says that $f$ changes to first order along an allowable curve, which is
impossible at a constrained extremum. The assumption was false, so
$\nabla f(\mathbf p)$ is a linear combination of the constraint gradients.

$\square$

The one-constraint formula is the case $m=1$. With several restrictions,
there is one multiplier for each restriction. The corresponding Lagrangian is

$$
\mathcal L(\mathbf x,\lambda_1,\ldots,\lambda_m)
=f(\mathbf x)-\sum_{i=1}^{m}\lambda_i\bigl(g_i(\mathbf x)-c_i\bigr).
$$

Taking derivatives with respect to $\mathbf x$ and every multiplier gives

$$
\begin{cases}
\nabla f=\displaystyle\sum_{i=1}^{m}\lambda_i\nabla g_i,\\
g_1=c_1,\\
\vdots\\
g_m=c_m.
\end{cases}
$$

Thus solve the gradient equation together with **all** $m$ constraint
equations, retain every feasible candidate, and compare their objective
values. In particular, $m$ independent constraints in $\mathbb R^n$ usually
leave an $(n-m)$-dimensional set of allowable points.

**Example (Two Constraints in Three Dimensions).** Find the maximum and
minimum of $f(x,y,z)=x+y+z$ subject to

$$
x^2+y^2+z^2=1,\qquad x-y=0.
$$

**Solution:**

1. Write the Lagrange multiplier helper function:

$$
\mathcal L(x,y,z,\lambda,\mu)
=x+y+z-\lambda(x^2+y^2+z^2-1)-\mu(x-y).
$$

2. Set every partial derivative equal to zero:

$$
\begin{cases}
\mathcal L_x=1-2\lambda x-\mu=0,\\
\mathcal L_y=1-2\lambda y+\mu=0,\\
\mathcal L_z=1-2\lambda z=0,\\
\mathcal L_\lambda=-(x^2+y^2+z^2-1)=0,\\
\mathcal L_\mu=-(x-y)=0.
\end{cases}
$$

3. The last equation gives $x=y$. Adding the first two equations then gives
$1=2\lambda x$; comparing with the third equation gives $x=z$. The sphere
constraint now yields

$$
x=y=z=\pm\frac1{\sqrt3}.
$$

4. At $(1/\sqrt3,1/\sqrt3,1/\sqrt3)$, $f=\sqrt3$; at
$(-1/\sqrt3,-1/\sqrt3,-1/\sqrt3)$, $f=-\sqrt3$. These are the absolute
maximum and minimum because the feasible set is closed and bounded.

$\square$

## 7. Scope and cautions

- The method produces **candidates**. Compare objective values to decide
  maximum versus minimum.
- For several constraints, the standard theorem requires the constraint
  gradients to be linearly independent. If they are dependent or a constraint
  is singular, check such points separately.
- A constraint that is not closed and bounded may have no absolute extrema;
  investigate its domain and behavior at its ends.

## Check your understanding

1. Why is $\nabla f$ perpendicular to an $f$-contour?
2. In the diagram, why are the $f$-contour and $g=5$ tangent at an extremum?
3. Explain in one sentence why $\mathcal L_\lambda=0$ is necessary.

Practice next: [Lagrange Multipliers Homework](./03-lagrange-multipliers-homework.md).
