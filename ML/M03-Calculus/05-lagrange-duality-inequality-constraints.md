# Lesson 5: Lagrange Duality and Inequality Constraints
*ML / M03 — Calculus*

## The question

Last class, a constraint had the form $g(\mathbf x)=c$: our answer had to
stay exactly on a curve. Many real optimization problems instead impose a
limit:

$$
\text{minimize } f(\mathbf x)
\qquad\text{subject to}\qquad g_i(\mathbf x)\leq0
\quad(i=1,\ldots,r).
$$

Here $r$ is the total number of inequality constraints.

For example, a model might minimize loss while keeping latency, memory use,
or a fairness measure below a fixed budget. Lagrange duality turns each
inequality into a price. It gives a second optimization problem whose answer
is a guaranteed bound on the best feasible value, and—under useful convexity
conditions—often the exact same value.

## Learning goals

By the end of this lesson, you should be able to:

1. write a constrained minimization problem in standard inequality form;
2. form its Lagrangian and explain why multipliers must be nonnegative;
3. construct and interpret the dual function and dual problem;
4. use weak duality to certify a lower bound on a constrained minimum; and
5. use the KKT conditions for a differentiable convex problem.

## 1. From equality constraints to limits

An inequality such as

$$
x\geq1
$$

is written in standard form as $1-x\leq0$. The feasible points lie on one
side of a boundary rather than only on the boundary itself.

<svg viewBox="0 0 720 330" width="720" role="img" aria-labelledby="inequality-title inequality-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="inequality-title">Minimizing x squared subject to x at least one</title>
  <desc id="inequality-desc">The graph y equals x squared is shown. The feasible part of the x axis starts at x equals one, and the constrained minimum occurs at the endpoint one, one.</desc>
  <rect width="720" height="330" rx="12" fill="#fffdf8"/>
  <g stroke="#94a3b8" stroke-width="1.5"><path d="M55 255H680"/><path d="M300 288V30"/></g>
  <g font-family="sans-serif" font-size="15" fill="#475569"><text x="665" y="247">x</text><text x="309" y="47">f(x)</text><text x="290" y="273">0</text></g>
  <path d="M90 64 Q300 278 510 64" fill="none" stroke="#0f766e" stroke-width="4"/>
  <path d="M405 255H670" stroke="#c2410c" stroke-width="8" stroke-linecap="round"/>
  <path d="M405 246V264" stroke="#111827" stroke-width="3"/>
  <circle cx="405" cy="148" r="6" fill="#111827"/>
  <path d="M405 148V255" stroke="#64748b" stroke-width="2" stroke-dasharray="6 5"/>
  <g font-family="sans-serif" font-size="17"><text x="430" y="284" fill="#9a3412">feasible: x ≥ 1</text><text x="416" y="142" fill="#111827">(1, 1)</text><text x="416" y="166" fill="#0f766e">constrained minimum</text><text x="397" y="279" fill="#111827">1</text><text x="515" y="85" fill="#0f766e">f(x) = x²</text></g>
</svg>

For a **minimization** problem, we will use

$$
\boxed{
p_*=
\inf_{\mathbf x}\ f(\mathbf x)
\quad\text{subject to}\quad
g_i(\mathbf x)\leq0.}
$$

The symbol $\inf$ means the greatest lower bound. When a minimizer exists,
it is an ordinary minimum and $p_*$ is its value. Writing $\inf$ lets the
definition also cover problems whose best value is approached but not
attained.

## 2. The Lagrangian: a price for violating a limit

Assign one multiplier $\lambda_i\geq0$ to each inequality and define

$$
\boxed{
\mathcal L(\mathbf x,\boldsymbol\lambda)
=f(\mathbf x)+\sum_{i=1}^r\lambda_i g_i(\mathbf x),
\qquad \boldsymbol\lambda\geq\mathbf0.}
$$

The nonnegative multipliers make the constraints part of the objective. To
see this, hold $\mathbf x$ fixed and let the multipliers choose their values:

$$
\sup_{\boldsymbol\lambda\geq\mathbf0}
\mathcal L(\mathbf x,\boldsymbol\lambda)
=
\begin{cases}
f(\mathbf x),&g_i(\mathbf x)\leq0\text{ for every }i,\\
+\infty,&g_j(\mathbf x)>0\text{ for at least one }j.
\end{cases}
$$

For a feasible $\mathbf x$, every extra term
$\lambda_i g_i(\mathbf x)$ is nonpositive, so the supremum is $f(\mathbf x)$
and is attained at $\boldsymbol\lambda=\mathbf0$. If $\mathbf x$ violates
one constraint, say $g_j(\mathbf x)>0$, choosing
$\lambda_j\to\infty$ sends the Lagrangian to $+\infty$. The multiplier is
therefore a price that makes infeasible choices infinitely bad.

Consequently, the original constrained question is exactly the following
**min--max problem**:

$$
\boxed{
p_*=
\inf_{\mathbf x}\ \sup_{\boldsymbol\lambda\geq\mathbf0}
\mathcal L(\mathbf x,\boldsymbol\lambda).}
$$

We often say “$\min_{\mathbf x}\max_{\boldsymbol\lambda}\mathcal L$.”
Technically, $\sup$ is the correct word above: at an infeasible point the
value grows without a finite maximum.

## 3. Reverse the order: the dual question

The primal asks $\mathbf x$ to move first, while the multipliers then expose
any constraint violation:

$$
\underbrace{\inf_{\mathbf x}\ \sup_{\boldsymbol\lambda\geq0}
\mathcal L(\mathbf x,\boldsymbol\lambda)}_{\text{original primal value }p_*}.
$$

The **Lagrange dual** reverses that order. First choose a nonnegative price
vector; then allow $\mathbf x$ to minimize the resulting Lagrangian over all
points, even infeasible ones:

$$
\boxed{
d_*=
\sup_{\boldsymbol\lambda\geq\mathbf0}\ \inf_{\mathbf x}
\mathcal L(\mathbf x,\boldsymbol\lambda).}
$$

Define the inner value as the **dual function**,

$$
q(\boldsymbol\lambda)=\inf_{\mathbf x}
\mathcal L(\mathbf x,\boldsymbol\lambda),
$$

so the dual question is $d_*=\sup_{\boldsymbol\lambda\geq0}q(\boldsymbol\lambda)$.

The two orders need not give the same number. For every function of two
variables, the minimax inequality says

$$
\boxed{
\sup_{\boldsymbol\lambda\geq\mathbf0}\inf_{\mathbf x}
\mathcal L(\mathbf x,\boldsymbol\lambda)
\ \leq\
\inf_{\mathbf x}\sup_{\boldsymbol\lambda\geq\mathbf0}
\mathcal L(\mathbf x,\boldsymbol\lambda).}
$$

In our notation, this is

$$
\boxed{d_*\leq p_*.}
$$

This guaranteed inequality is **weak duality**. The dual produces lower
bounds on the constrained minimum, but without additional assumptions it
may not reach the primal value. The difference $p_*-d_*$ is the **duality
gap**.

Even when $f$ and the $g_i$ are not convex, $q$ is always concave: it is the
pointwise infimum of functions affine in $\boldsymbol\lambda$. Thus the
dual is a maximization of a concave function over the convex region
$\boldsymbol\lambda\geq0$.

## 4. Complete example: the two orders agree

**Example (Two orders agree).** Solve

$$
\text{minimize } x^2
\qquad\text{subject to}\qquad x\geq1.
$$

**Solution:**

The standard constraint is $g(x)=1-x\leq0$, so

$$
\mathcal L(x,\lambda)=x^2+\lambda(1-x),
\qquad\lambda\geq0.
$$

The primal order reproduces the original question:

$$
\inf_x\sup_{\lambda\geq0}\bigl[x^2+\lambda(1-x)\bigr]
=\inf_{x\geq1}x^2=1.
$$

Indeed, $x<1$ makes the inner supremum $+\infty$, whereas for $x\geq1$
the inner supremum is $x^2$.

Now reverse the order. To find the dual function, minimize with respect to
the unrestricted variable $x$:

$$
\frac{\partial\mathcal L}{\partial x}=2x-\lambda=0
\quad\Longrightarrow\quad x=\frac\lambda2.
$$

Substitution gives

$$
q(\lambda)=\lambda-\frac{\lambda^2}{4},
\qquad\lambda\geq0.
$$

Now maximize this concave parabola:

$$
q'(\lambda)=1-\frac\lambda2=0
\quad\Longrightarrow\quad \lambda_*=2,
\qquad d_*=q(2)=1.
$$

The original feasible set is $[1,\infty)$, and $x^2$ is smallest there at
$x_*=1$, with $p_*=1$. Hence

$$
d_*=p_*=1.
$$

The dual lower bound is exact. The positive optimal price $\lambda_*=2$
also signals that the constraint is active: the optimum sits at $x=1$.

$\square$

## 5. KKT conditions: why they arise

For differentiable $f$ and $g_i$, a candidate primal-dual pair
$(\mathbf x_*,\boldsymbol\lambda_*)$ satisfies the
**Karush–Kuhn–Tucker (KKT) conditions** when

$$
\begin{aligned}
\text{stationarity:}\quad&
\nabla f(\mathbf x_*)+
\sum_i\lambda_{i*}\nabla g_i(\mathbf x_*)=\mathbf0,\\
\text{primal feasibility:}\quad&g_i(\mathbf x_*)\leq0,\\
\text{dual feasibility:}\quad&\lambda_{i*}\geq0,\\
\text{complementary slackness:}\quad&
\lambda_{i*}g_i(\mathbf x_*)=0\quad\text{for every }i.
\end{aligned}
$$

Here is the informal idea behind these four lines. It is not a full proof;
the standard theorem also needs a regularity condition. In the argument
below, it is enough to assume that the gradients of the active constraints
are linearly independent.

Suppose $\mathbf x_*$ is a local solution. Relabel the constraints, if
needed, so that the first $m$ are **active** and the rest are **slack**:

$$
g_1(\mathbf x_*)=\cdots=g_m(\mathbf x_*)=0,
\qquad
g_{m+1}(\mathbf x_*),\ldots,g_r(\mathbf x_*)<0.
$$

For local questions, a slack constraint stays satisfied after a sufficiently
small move. Therefore $\mathbf x_*$ is also a local minimum of the equality-
constrained problem that keeps only the active boundaries,

$$
\text{minimize } f(\mathbf x)
\qquad\text{subject to}\qquad
g_i(\mathbf x)=0\quad(i=1,\ldots,m).
$$

The ordinary equality-constraint multiplier rule from Lesson 3 gives
numbers $\lambda_1,\ldots,\lambda_m$ for which

$$
\nabla f(\mathbf x_*)+
\sum_{i=1}^m\lambda_i\nabla g_i(\mathbf x_*)=\mathbf0.
$$

This is stationarity. Primal feasibility already holds because
$\mathbf x_*$ came from the original constrained problem.

Why must an active multiplier be nonnegative? Intuitively, a negative
$\lambda_j$ would say that moving inward from the boundary $g_j=0$ lowers
$f$, contradicting optimality. More concretely, the regularity assumption
lets us choose a direction $\mathbf v$ that decreases $g_j$ while leaving
the other active constraints unchanged:

$$
\nabla g_j(\mathbf x_*)^T\mathbf v<0,
\qquad
\nabla g_i(\mathbf x_*)^T\mathbf v=0\quad(i\ne j, i\leq m).
$$

This is a feasible small move: it goes into $g_j<0$, stays on the other
active boundaries to first order, and does not disturb the already-slack
constraints. If $\lambda_j<0$, stationarity would give

$$
\nabla f(\mathbf x_*)^T\mathbf v
=-\lambda_j\nabla g_j(\mathbf x_*)^T\mathbf v<0,
$$

so that same feasible move would decrease $f$—a contradiction. Thus
$\lambda_j\geq0$.

For every slack constraint $i>m$, removing it does not change the local
behavior, so set $\lambda_i=0$. This both preserves stationarity and gives
complementary slackness. Equivalently, each constraint has one of two
states:

| Constraint at the solution | Multiplier | Interpretation |
| --- | --- | --- |
| $g_i(\mathbf x_*)<0$ (slack) | $\lambda_{i*}=0$ | The limit is not binding, so it has no price. |
| $\lambda_{i*}>0$ | $g_i(\mathbf x_*)=0$ | The limit is binding. |

For the example, stationarity gives $2x-\lambda=0$. At
$(x_*,\lambda_*)=(1,2)$, feasibility holds and

$$
\lambda_*g(x_*)=2(1-1)=0.
$$

So all KKT conditions hold.

### How to use KKT to find candidates

Let $\mathbf x\in\mathbb R^d$ and suppose there are $r$ inequality
constraints. Treat both $\mathbf x$ and
$\boldsymbol\lambda=(\lambda_1,\ldots,\lambda_r)$ as unknowns. Solve the
following $d+r$ equations in the $d+r$ unknowns:

$$
\begin{cases}
\nabla f(\mathbf x)+\displaystyle\sum_{i=1}^r\lambda_i\nabla g_i(\mathbf x)=\mathbf0,
&\text{($d$ stationarity equations)},\\
\lambda_i g_i(\mathbf x)=0\quad(i=1,\ldots,r).
&\text{($r$ complementary-slackness equations)}
\end{cases}
$$

Generically, this produces a discrete collection of candidate pairs. The
product equations create cases: for each $i$, either $g_i(\mathbf x)=0$ or
$\lambda_i=0$. After solving, discard every pair that fails either

$$
g_i(\mathbf x)\leq0
\qquad\text{or}\qquad
\lambda_i\geq0.
$$

Then compare objective values when several feasible candidates remain. For a
convex problem with the regularity conditions in the next section, a feasible
KKT pair certifies a global optimum. Without those assumptions, KKT gives
candidates rather than an automatic global conclusion.

### Worked example: solve the dual first, then use KKT

**Example (Quadratic below a line).** Solve

$$
\text{minimize } (x-2)^2+(y-1)^2
\qquad\text{subject to}\qquad x+y\leq1.
$$

**Solution:**

The unconstrained minimum is $(2,1)$, but it has $x+y=3$, so it is not
feasible. Write the constraint as $g(x,y)=x+y-1\leq0$. There is one
multiplier $\lambda\geq0$, and the Lagrangian is

$$
\mathcal L(x,y,\lambda)
=(x-2)^2+(y-1)^2+\lambda(x+y-1).
$$

#### Method 1: form and solve the Lagrange dual

The dual function minimizes the Lagrangian over unrestricted $x,y$:

$$
q(\lambda)=\inf_{x,y}\mathcal L(x,y,\lambda),
\qquad \lambda\geq0.
$$

For fixed $\lambda$, complete the squares:

$$
\mathcal L(x,y,\lambda)
=\left(x-2+\frac\lambda2\right)^2
+\left(y-1+\frac\lambda2\right)^2
+2\lambda-\frac{\lambda^2}{2}.
$$

The squares are minimized at

$$
x(\lambda)=2-\frac\lambda2,
\qquad y(\lambda)=1-\frac\lambda2,
$$

so the dual function and dual problem are

$$
q(\lambda)=2\lambda-\frac{\lambda^2}{2},
\qquad
\boxed{\ \text{maximize}_{\lambda\geq0}\quad
2\lambda-\frac{\lambda^2}{2}\ }.
$$

This concave parabola has

$$
q'(\lambda)=2-\lambda=0
\quad\Longrightarrow\quad
\lambda_*=2,
\qquad d_*=q(2)=2.
$$

The minimizer of $\mathcal L(\cdot,\cdot,2)$ is

$$
(x_*,y_*)=(x(2),y(2))=(1,0).
$$

It is primal feasible and has $f(1,0)=2=d_*$. Weak duality gives
$d_*\leq p_*$, while this feasible point gives $p_*\leq2$. Therefore

$$
\boxed{p_*=d_*=2.}
$$

#### Method 2: solve the same problem using KKT

KKT treats $x$, $y$, and $\lambda$ as unknowns. Stationarity gives

$$
\begin{aligned}
\frac{\partial\mathcal L}{\partial x}&=2(x-2)+\lambda=0,
&\Longrightarrow&&x=2-\frac\lambda2,\\
\frac{\partial\mathcal L}{\partial y}&=2(y-1)+\lambda=0,
&\Longrightarrow&&y=1-\frac\lambda2.
\end{aligned}
$$

Complementary slackness supplies the remaining equation:

$$
\lambda(x+y-1)
=\lambda\left[\left(2-\frac\lambda2\right)
+\left(1-\frac\lambda2\right)-1\right]
=\lambda(2-\lambda)=0.
$$

Thus there are two cases:

| Case | Candidate | Result |
| --- | --- | --- |
| $\lambda=0$ | $(x,y)=(2,1)$ | Not primal feasible: $2+1>1$. Discard it. |
| $\lambda=2$ | $(x,y)=(1,0)$ | Primal and dual feasible. Keep it. |

At $(x_*,y_*,\lambda_*)=(1,0,2)$, primal feasibility, dual feasibility,
stationarity, and complementary slackness all hold. The objective value is

$$
f(1,0)=(1-2)^2+(0-1)^2=2.
$$

This is a global, not merely local, answer: the objective is convex, the
constraint is affine (hence convex), and $(0,0)$ is strictly feasible. The
KKT sufficiency result therefore applies.

Both methods produce the same triple

$$
(x_*,y_*,\lambda_*)=(1,0,2)
$$

and the same optimal value $2$. The dual method first finds the best price
$\lambda_*$ and then minimizes the Lagrangian at that price. KKT combines
that minimization condition with feasibility and complementary slackness in
one system. The positive multiplier confirms that the constraint is active.

$\square$

## 6. When does the dual give the exact answer?

Weak duality always holds, but equality $d_*=p_*$ needs additional
assumptions. A widely used sufficient set is:

- $f$ and every $g_i$ are convex;
- any equality constraints are affine; and
- there is a strictly feasible point with $g_i(\mathbf x)<0$ for every
  inequality (the **Slater condition**).

Under these conditions, strong duality holds: $d_*=p_*$. In a differentiable
convex problem satisfying this regularity condition, KKT conditions are both
necessary and sufficient for optimality. Outside this setting, KKT may still
find useful candidates, but it is not by itself a universal proof of a global
minimum.

## 7. Maximization problems and a common sign error

Our convention is built for minimization. For

$$
\text{maximize } F(\mathbf x)
\qquad\text{subject to}\qquad g_i(\mathbf x)\leq0,
$$

first rewrite it as minimizing $f=-F$. The Lagrangian is then

$$
\mathcal L=-F+\sum_i\lambda_i g_i,
\qquad\lambda_i\geq0.
$$

The dual supplies a lower bound on $-F$, equivalently an upper bound on the
largest feasible value of $F$. Keeping this conversion explicit prevents the
most common sign mistake: using a negative multiplier with a $\leq0$
constraint.

## 8. Reliable workflow

For a differentiable constrained minimization problem:

1. Rewrite every inequality as $g_i(\mathbf x)\leq0$.
2. Form $\mathcal L=f+\sum_i\lambda_i g_i$ with $\lambda_i\geq0$.
3. For a dual bound, compute $q(\boldsymbol\lambda)=\inf_{\mathbf x}\mathcal L$
   and maximize it over nonnegative multipliers.
4. To find KKT candidates, solve stationarity and complementary slackness,
   then discard any candidate violating primal or dual feasibility.
5. Compare objective values if several feasible candidates remain.
6. State whether your conclusion uses only weak duality (a bound) or strong
   duality/KKT assumptions (an exact optimum).

## Check your understanding

1. For fixed $\mathbf x$, explain why
   $\sup_{\boldsymbol\lambda\geq0}\mathcal L(\mathbf x,\boldsymbol\lambda)$
   equals $f(\mathbf x)$ when $\mathbf x$ is feasible and $+\infty$ when it
   is infeasible.
2. Which order, $\inf_{\mathbf x}\sup_{\boldsymbol\lambda}\mathcal L$ or
   $\sup_{\boldsymbol\lambda}\inf_{\mathbf x}\mathcal L$, is the primal
   problem? State the weak-duality inequality between them.
3. For $\min_x (x-3)^2$ subject to $x\leq1$, is the constraint active at the
   optimum? What must complementary slackness say about its multiplier?
4. What is the difference between weak duality and strong duality?
5. Why does a positive multiplier imply that its constraint is tight?

Practice next: [Lagrange Duality and Inequality Constraints Homework](./05-lagrange-duality-inequality-constraints-homework.md).
