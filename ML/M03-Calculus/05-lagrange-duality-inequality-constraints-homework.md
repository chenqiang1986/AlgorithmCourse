# Homework: Lagrange Duality and Inequality Constraints
*ML / M03 — Calculus*

Use the [Lesson 5 notes](./05-lagrange-duality-inequality-constraints.md)
as a reference. Unless a question explicitly asks about a maximization
problem, use the convention $g_i(\mathbf x)\leq0$ and
$\mathcal L=f+\sum_i\lambda_i g_i$ with $\lambda_i\geq0$.

## 1. Standard form and the Lagrangian

Rewrite each constraint in the form $g(x)\leq0$, then write the Lagrangian
for the stated minimization problem.

1. Minimize $(x-2)^2$ subject to $x\geq4$.
2. Minimize $x^2+y^2$ subject to $x+y\leq1$.
3. Minimize $x^2+y^2$ subject to $x\geq0$ and $y\geq0$.

State the sign restriction on every multiplier.

## 2. The primal min--max form, then weak duality

Consider

$$
p_*=\inf\{f(x):g(x)\leq0\},
\qquad
\mathcal L(x,\lambda)=f(x)+\lambda g(x),\qquad\lambda\geq0.
$$

1. For a fixed $x$, show that

   $$
   \sup_{\lambda\geq0}\mathcal L(x,\lambda)=
   \begin{cases}
   f(x),&g(x)\leq0,\\
   +\infty,&g(x)>0.
   \end{cases}
   $$

2. Deduce that

   $$
   p_*=\inf_x\sup_{\lambda\geq0}\mathcal L(x,\lambda).
   $$

3. Write the dual value by reversing the two operations. State the minimax
   inequality that proves weak duality.

## 3. Solve a primal and its dual

Solve the primal problem

$$
\text{minimize } (x-3)^2
\qquad\text{subject to}\qquad x\leq1.
$$

1. Find the primal optimum $x_*$ and value $p_*$ directly.
2. Form the Lagrangian using $g(x)=x-1\leq0$.
3. Compute $q(\lambda)$ by minimizing the Lagrangian over all real $x$.
4. Maximize $q(\lambda)$ over $\lambda\geq0$.
5. Compare $d_*$ and $p_*$. Verify all four KKT conditions.

## 4. A constraint that is slack

Solve

$$
\text{minimize } (x-1)^2
\qquad\text{subject to}\qquad x\leq4.
$$

Find a primal-dual optimal pair and verify KKT. In particular, explain why
the multiplier must be zero even though the constraint is present.

## 5. Two inequality constraints

Consider

$$
\text{minimize } x^2
\qquad\text{subject to}\qquad 1\leq x\leq3.
$$

1. Write both constraints in standard form and form $\mathcal L(x,\lambda_1,\lambda_2)$.
2. Find the primal optimum directly.
3. Use KKT conditions to find multipliers $\lambda_1,\lambda_2$.
4. Identify which constraint is active and which is slack.

## 6. Convex two-variable KKT problem

Solve

$$
\text{minimize } (x-2)^2+(y-1)^2
\qquad\text{subject to}\qquad x+y\leq1.
$$

1. Explain why the objective and feasible region are convex.
2. Form the Lagrangian.
3. Solve the KKT system.
4. Give the minimum value and explain why KKT certifies a global minimum.

## 7. A dual function is concave

For the problem in Question 3, graph or sketch

$$
q(\lambda)=2\lambda-\frac{\lambda^2}{4}
\quad\text{for }\lambda\geq0.
$$

Mark its maximum. Then explain why it is reasonable that a dual function is
concave even though the primal problem is a minimization.

## 8. Maximization: convert before using the rule

Find the maximum of

$$
F(x)=x
\qquad\text{subject to}\qquad x^2\leq4.
$$

Do this by converting it to a minimization of $-F(x)$. Write the Lagrangian,
the KKT conditions, and the maximizing point. Be explicit about why the
multiplier is nonnegative.

## 9. Challenge — prove KKT sufficiency in a convex problem

Assume $f$ and $g_i$ are differentiable convex functions. Suppose
$(\mathbf x_*,\boldsymbol\lambda_*)$ satisfies all KKT conditions. Prove
that $\mathbf x_*$ minimizes $f$ over all points satisfying
$g_i(\mathbf x)\leq0$.

**Hint:** Use stationarity and the first-order convexity inequalities for
$f$ and each $g_i$ to show that every feasible $\mathbf y$ satisfies
$f(\mathbf y)\geq f(\mathbf x_*)$.
