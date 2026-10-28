# Lesson 2: The SVM Lagrange Dual and the Intercept
*ML / M06 — Supervised Learning*

## The question

The soft-margin primal problem has a parameter vector, an intercept, and one
slack variable per observation. What does its Lagrange dual look like, and
how do we recover the intercept after it disappears from that dual?

This lesson uses the result of Lagrange duality rather than deriving the
general theory. For that background, see
[Lagrange Duality and Inequality Constraints](../../M03-Calculus/05-lagrange-duality-inequality-constraints.md).

We start from the soft-margin primal:

$$
\begin{aligned}
\underset{\mathbf w,b,\boldsymbol\xi}{\operatorname{minimize}}\quad
&\frac12\lVert\mathbf w\rVert_2^2+C\sum_{i=1}^n\xi_i\\
\text{subject to}\quad
&y_i(\mathbf w^T\mathbf x_i+b)\geq1-\xi_i,\\
&\xi_i\geq0.
\end{aligned}
$$

## 1. Write the Lagrangian

Write the two constraint families in less-than-or-equal-to-zero form:

$$
1-\xi_i-y_i(\mathbf w^T\mathbf x_i+b)\leq0,
\qquad -\xi_i\leq0.
$$

Give them nonnegative multipliers $\alpha_i\geq0$ and $\mu_i\geq0$,
respectively. The Lagrangian is

$$
\begin{aligned}
\mathcal L(\mathbf w,b,\boldsymbol\xi,
\boldsymbol\alpha,\boldsymbol\mu)
= {}& \frac12\lVert\mathbf w\rVert_2^2+C\sum_i\xi_i\\
&+\sum_i\alpha_i\left[1-\xi_i-y_i(\mathbf w^T\mathbf x_i+b)\right]
-\sum_i\mu_i\xi_i.
\end{aligned}
$$

For fixed multipliers $\boldsymbol\alpha,\boldsymbol\mu$, define the dual
function as the minimum of the Lagrangian over the primal variables:

$$
q(\boldsymbol\alpha,\boldsymbol\mu)
=\min_{\mathbf w,b,\boldsymbol\xi}
\mathcal L(\mathbf w,b,\boldsymbol\xi,
\boldsymbol\alpha,\boldsymbol\mu).
$$

To find its explicit form, solve for the critical point of
$\mathcal L$ with respect to $\mathbf w$, $b$, and each $\xi_i$.

$$
\begin{aligned}
\nabla_{\mathbf w}\mathcal L
&=\mathbf w-\sum_{i=1}^n\alpha_i y_i\mathbf x_i=\mathbf0,
&&\Longrightarrow&
\mathbf w&=\sum_{i=1}^n\alpha_i y_i\mathbf x_i,\\
\frac{\partial\mathcal L}{\partial b}
&=-\sum_{i=1}^n\alpha_i y_i=0,
&&\Longrightarrow&
\sum_{i=1}^n\alpha_i y_i&=0,\\
\frac{\partial\mathcal L}{\partial\xi_i}
&=C-\alpha_i-\mu_i=0,
&&\Longrightarrow&
\mu_i&=C-\alpha_i.
\end{aligned}
$$

The last equation, together with $\alpha_i\geq0$ and $\mu_i\geq0$, gives

$$
0\leq\alpha_i\leq C.
$$

Now substitute the critical-point conditions back into the Lagrangian. First,
the terms involving $b$ and $\xi_i$ vanish:

$$
-b\sum_i\alpha_i y_i=0,
\qquad
\sum_i\xi_i(C-\alpha_i-\mu_i)=0.
$$

Thus

$$
\begin{aligned}
q(\boldsymbol\alpha,\boldsymbol\mu)
&=\frac12\lVert\mathbf w\rVert_2^2
-\sum_i\alpha_i y_i\mathbf w^T\mathbf x_i
+\sum_i\alpha_i\\
&=\frac12\lVert\mathbf w\rVert_2^2
-\mathbf w^T\left(\sum_i\alpha_i y_i\mathbf x_i\right)
+\sum_i\alpha_i\\
&=-\frac12\lVert\mathbf w\rVert_2^2+\sum_i\alpha_i\\
&=\sum_i\alpha_i
-\frac12\sum_i\sum_j
\alpha_i\alpha_jy_i y_j\,\mathbf x_i^T\mathbf x_j.
\end{aligned}
$$

After eliminating $\mathbf w$, $b$, $\boldsymbol\xi$, and
$\boldsymbol\mu$, write this simply as $q(\boldsymbol\alpha)$. The dual
problem maximizes this lower bound over the allowed $\boldsymbol\alpha$.

## 2. The dual problem

Substituting the stationarity conditions into the Lagrangian yields the dual:

$$
\boxed{
\begin{aligned}
\underset{\boldsymbol\alpha}{\operatorname{maximize}}\quad
&\sum_{i=1}^n\alpha_i
-\frac12\sum_{i=1}^n\sum_{j=1}^n
\alpha_i\alpha_jy_i y_j\,\mathbf x_i^T\mathbf x_j\\
\text{subject to}\quad
&0\leq\alpha_i\leq C,
&&i=1,\ldots,n,\\
&\sum_{i=1}^n\alpha_i y_i=0.
\end{aligned}}
$$

### Why this dual is exact

The [Strong duality under Slater's condition theorem](../../M03-Calculus/05-lagrange-duality-inequality-constraints.md)
states that a convex problem has equal primal and dual optimal values when
its equality constraints are affine and it has a strictly feasible point.
Those hypotheses hold for the soft-margin SVM:

- its objective $\frac12\lVert\mathbf w\rVert_2^2+C\sum_i\xi_i$ is convex;
- both constraint families are affine in $(\mathbf w,b,\boldsymbol\xi)$; and
- $\mathbf w=\mathbf0$, $b=0$, and $\xi_i=2$ is strictly feasible, since
  $1-\xi_i-y_i(\mathbf w^T\mathbf x_i+b)=-1<0$ and $-\xi_i=-2<0$.

Therefore strong duality holds for this SVM: the dual is faithful to the
primal in the sense that their optimal objective values are equal (there is
no duality gap). The dual does not directly return every primal variable,
but the KKT conditions let us recover $\mathbf w$, $b$, and the slacks from
an optimal dual solution.

This is a concave quadratic maximization problem. Its data enter only through
dot products $\mathbf x_i^T\mathbf x_j$, a fact that later makes kernel SVMs
possible.

The recovered normal vector is

$$
\mathbf w=\sum_i\alpha_i y_i\mathbf x_i.
$$

Thus an observation with $\alpha_i=0$ contributes nothing. The observations
with $\alpha_i>0$ are the support vectors.

## 3. Why the intercept vanishes

The intercept $b$ appears in the Lagrangian only through

$$
-b\sum_i\alpha_i y_i.
$$

When minimizing over an unrestricted $b$, the Lagrangian would be unbounded
below unless $\sum_i\alpha_i y_i=0$. That equality is therefore a dual
constraint. Once it holds, the entire $b$ term is zero, so $b$ does not occur
in the dual objective. The dual solver consequently finds
$\boldsymbol\alpha$, not $b$ directly.

## 4. Recover $b$ with KKT complementary slackness

### The KKT theorem

For a convex minimization problem with differentiable objective and convex
inequality constraints, if Slater's condition holds (there is a strictly
feasible point), a primal-dual tuple is optimal **if and only if** it
satisfies the Karush--Kuhn--Tucker (KKT) conditions:

1. primal feasibility;
2. dual feasibility of the multipliers;
3. stationarity of the Lagrangian with respect to every primal variable; and
4. complementary slackness for every inequality constraint.

The SVM objective is convex and both of its constraint families are affine.
Moreover, Slater's condition holds: for example, take $\mathbf w=\mathbf0$,
$b=0$, and $\xi_i=2$ for every $i$. Thus the KKT conditions below are both
necessary and sufficient for optimality.

### All KKT conditions for the soft-margin SVM

For every training example $i=1,\ldots,n$, the conditions are:

**Primal feasibility**

$$
1-\xi_i-y_i(\mathbf w^T\mathbf x_i+b)\leq0,
\qquad
-\xi_i\leq0.
$$

Equivalently,

$$
y_i(\mathbf w^T\mathbf x_i+b)\geq1-\xi_i,
\qquad
\xi_i\geq0.
$$

**Dual feasibility**

$$
\alpha_i\geq0,
\qquad
\mu_i\geq0.
$$

**Stationarity**

$$
\begin{aligned}
\nabla_{\mathbf w}\mathcal L&=\mathbf w-\sum_i\alpha_i y_i\mathbf x_i=\mathbf0,\\
\frac{\partial\mathcal L}{\partial b}&=-\sum_i\alpha_i y_i=0,\\
\frac{\partial\mathcal L}{\partial\xi_i}&=C-\alpha_i-\mu_i=0.
\end{aligned}
$$

**Complementary slackness**

$$
\alpha_i\left[1-\xi_i-y_i(\mathbf w^T\mathbf x_i+b)\right]=0
$$

and

$$
\mu_i\xi_i=0.
$$

Except for complementary slackness, we have already used all of these KKT
conditions while deriving the dual: primal feasibility defined the original
SVM constraints, dual feasibility required $\alpha_i,\mu_i\geq0$, and
stationarity produced $\mathbf w$, the equality constraint
$\sum_i\alpha_i y_i=0$, and the box constraint $0\leq\alpha_i\leq C$.
Complementary slackness is the remaining condition that lets us recover
information about the primal solution, especially $b$.

### Classifying points by $\alpha_i$

The relation $\mu_i=C-\alpha_i$, together with complementary slackness,
gives three useful cases.

#### Case 1: $\alpha_i=0$

$$
\alpha_i=0
\quad\Longrightarrow\quad
\mu_i=C>0
\quad\Longrightarrow\quad
\xi_i=0
\quad\Longrightarrow\quad
y_i(\mathbf w^T\mathbf x_i+b)\geq1.
$$

These are well-classified points that lie on or outside the margin. Usually
they lie strictly outside it, with
$y_i(\mathbf w^T\mathbf x_i+b)>1$; equality is also possible in a
degenerate solution.

#### Case 2: $0<\alpha_i<C$

$$
0<\alpha_i<C
\quad\Longrightarrow\quad
\mu_i=C-\alpha_i>0
\quad\Longrightarrow\quad
\xi_i=0
\quad\Longrightarrow\quad
y_i(\mathbf w^T\mathbf x_i+b)=1.
$$

These are support vectors exactly on a margin boundary.

#### Case 3: $\alpha_i=C$

$$
\alpha_i=C
\quad\Longrightarrow\quad
\mu_i=0
\quad\Longrightarrow\quad
\xi_i\geq0
\quad\Longrightarrow\quad
y_i(\mathbf w^T\mathbf x_i+b)=1-\xi_i.
$$

These points are on or inside the margin. When $\xi_i>0$, they violate the
margin; when $\xi_i=0$, they lie exactly on it. In particular,
$0<\xi_i\leq1$ means the point is correctly classified but inside the margin,
whereas $\xi_i>1$ means it is misclassified.

### Use a margin support vector to recover $b$

We now use these conditions to recover the intercept. Choose a support vector
with $0<\alpha_i<C$. Because $C-\alpha_i-\mu_i=0$, this implies
$\mu_i=C-\alpha_i>0$, so $\mu_i\xi_i=0$ forces $\xi_i=0$. Also,
$\alpha_i>0$ makes the first complementary-slackness condition force the
margin constraint to be tight:

$$
y_i(\mathbf w^T\mathbf x_i+b)=1.
$$

Therefore this point gives

$$
\boxed{b=y_i-\mathbf w^T\mathbf x_i.}
$$

In practice, compute that quantity for every support vector satisfying
$0<\alpha_i<C$ (allowing a numerical tolerance) and average the results.
Points with $\alpha_i=C$ are on or inside the margin and do not generally
give that equality, so they should not be used in this simple formula.

## 5. Calculation recipe: recover the SVM coefficients

After expressing the SVM in dual form, compute the model parameters in this
order.

1. **Solve for $\boldsymbol\alpha$.** Solve the dual quadratic program:

   $$
   \begin{aligned}
   \underset{\boldsymbol\alpha}{\operatorname{maximize}}\quad
   &\sum_i\alpha_i-\frac12\sum_i\sum_j
   \alpha_i\alpha_jy_i y_j\,\mathbf x_i^T\mathbf x_j\\
   \text{subject to}\quad
   &0\leq\alpha_i\leq C,
   \qquad
   \sum_i\alpha_i y_i=0.
   \end{aligned}
   $$

2. **Recover $\boldsymbol\mu$.** Stationarity with respect to $\xi_i$ gives

   $$
   \boxed{\mu_i=C-\alpha_i.}
   $$

3. **Recover the normal vector $\mathbf w$.**

   $$
   \boxed{\mathbf w=\sum_{i=1}^n\alpha_i y_i\mathbf x_i.}
   $$

4. **Recover the intercept $b$.** For every index satisfying
   $0<\alpha_i<C$, use

   $$
   b_i=y_i-\mathbf w^T\mathbf x_i.
   $$

   In numerical work, average these values:

   $$
   \boxed{b=\frac{1}{|S|}\sum_{i\in S}
   \left(y_i-\mathbf w^T\mathbf x_i\right),\qquad
   S=\{i:0<\alpha_i<C\}.}
   $$

5. **Recover slack variables for points with $\alpha_i=C$.** Since
   $\alpha_i>0$, their margin constraint is tight, so

   $$
   \boxed{\xi_i=1-y_i(\mathbf w^T\mathbf x_i+b)\geq0.}
   $$

## Key takeaways

- The soft-margin dual optimizes one coefficient $\alpha_i$ per training
  example, constrained by $0\leq\alpha_i\leq C$ and
  $\sum_i\alpha_i y_i=0$.
- Only positive-$\alpha_i$ examples contribute to $\mathbf w$; these are the
  support vectors.
- Minimizing over the unrestricted intercept causes it to vanish and imposes
  the equality constraint in the dual.
- KKT complementary slackness recovers $b$ from a support vector with
  $0<\alpha_i<C$.

