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
f(x,y)=x+2y,\qquad g(x,y)=x^2+y^2,\qquad g=5.
$$

At $P=(1,2)$, the $f$-contour and the constraint circle are tangent, and

$$
\nabla f(P)=(1,2),\qquad \nabla g(P)=(2,4)=2\nabla f(P).
$$

<svg viewBox="0 0 720 420" width="720" role="img" aria-labelledby="contour-title contour-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="contour-title">A contour of f tangent to a constraint circle</title>
  <desc id="contour-desc">Several parallel contours of f and a circle g equals 5 touch at P. The gradients of f and g at P point in parallel directions.</desc>
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
  <!-- Parallel contours x+2y=k; the middle one is tangent at P=(1,2) -->
  <g fill="none" stroke="#0f766e" stroke-width="2.5" stroke-dasharray="8 6">
    <path d="M80 60 L670 355"/><path d="M80 105 L650 390"/><path d="M80 125.75 L608.5 390"/><path d="M80 170 L520 390"/>
  </g>
  <text x="440" y="88" fill="#0f766e" font-family="sans-serif" font-size="18">contours of f</text>
  <!-- P is coordinates (1,2), at pixel (245, 208.6) -->
  <circle cx="245.7" cy="208.6" r="6" fill="#111827"/>
  <text x="254" y="202" fill="#111827" font-family="sans-serif" font-size="17">P = (1, 2)</text>
  <path d="M245.7 208.6 L290.5 119" stroke="#155e75" stroke-width="4" marker-end="url(#arrow)"/>
  <text x="262" y="107" fill="#155e75" font-family="sans-serif" font-size="17">∇f = (1, 2)</text>
  <path d="M245.7 208.6 L318.3 63.4" stroke="#c2410c" stroke-width="4" marker-end="url(#arrowOrange)"/>
  <text x="319" y="52" fill="#c2410c" font-family="sans-serif" font-size="17">∇g = (2, 4)</text>
  <path d="M205 188.25 L335 253.25" stroke="#475569" stroke-width="2"/>
  <text x="335" y="265" fill="#475569" font-family="sans-serif" font-size="15">shared tangent</text>
</svg>

The multiplier equation says exactly “parallel” in algebra: two nonzero
vectors are parallel precisely when one is a scalar multiple of the other.
The multiplier may be positive or negative, so the gradients can point in the
same or opposite directions.

## 2. Deriving the condition from allowable motion

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

## 3. The Lagrange helper function

Define the **Lagrangian** (or Lagrange helper function)

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

Find the largest and smallest values of

$$
f(x,y)=x+2y
$$

on the circle $x^2+y^2=5$.

Set $g(x,y)=x^2+y^2$. The Lagrange system is

$$
(1,2)=\lambda(2x,2y),\qquad x^2+y^2=5.
$$

From the first vector equation,

$$
1=2\lambda x,\qquad 2=2\lambda y.
$$

Thus $x=1/(2\lambda)$ and $y=1/\lambda$. Substitute into the constraint:

$$
\frac1{4\lambda^2}+\frac1{\lambda^2}=5
\quad\Longrightarrow\quad
\lambda=\pm\frac12.
$$

The candidate points and values are

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

## 5. Reliable workflow

For an extremum of $f$ subject to one equality constraint $g=c$:

1. Compute $\nabla f$ and $\nabla g$.
2. Solve $\nabla f=\lambda\nabla g$ together with $g=c$.
3. Keep every real solution $(x,y)$ on the constraint.
4. Evaluate $f$ at every candidate and compare the values.
5. State why absolute extrema exist when needed (for example, a continuous
   function on a closed, bounded constraint).

Do not divide by $x$, $y$, or $\lambda$ before checking whether it could be
zero. That shortcut can silently discard valid candidates.

## 6. Scope and cautions

- The method produces **candidates**. Compare objective values to decide
  maximum versus minimum.
- The standard theorem assumes $\nabla g\ne\mathbf0$ at the point. If the
  constraint has a singular point, check it separately.
- With two variables and two independent constraints, use
  $\nabla f=\lambda\nabla g+\mu\nabla h$ along with $g=c$ and $h=d$.
- A constraint that is not closed and bounded may have no absolute extrema;
  investigate its domain and behavior at its ends.

## Check your understanding

1. Why is $\nabla f$ perpendicular to an $f$-contour?
2. In the diagram, why are the $f$-contour and $g=5$ tangent at an extremum?
3. Explain in one sentence why $\mathcal L_\lambda=0$ is necessary.

Practice next: [Lagrange Multipliers Homework](./03-homework-lagrange-multipliers.md).
