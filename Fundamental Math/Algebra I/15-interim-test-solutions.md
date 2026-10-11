# Algebra I Interim Test — Solutions
*Fundamental Math / Algebra I*

This key accompanies [15-interim-test.md](./15-interim-test.md). The test is worth
**100 points** and is designed for **60 minutes**.

## Coverage and Pacing

| Part | Lessons assessed | Points | Suggested time |
| --- | --- | ---: | ---: |
| A | 3–7: two- and three-variable systems, solution count, unknown coefficients, determinants | 34 | 20 min |
| B | 8–9: line equations, perpendicular lines, intercepts, point-to-line distance | 16 | 10 min |
| C | 10–11: feasible regions, vertices, linear optimization | 20 | 12 min |
| D | 12–14: square roots, completing the square, graphing, factoring | 30 | 18 min |
| **Total** | | **100** | **60 min** |

## Answer Summary

| Problem | Answer |
| --- | --- |
| 1 | $(3,1)$ |
| 2 | $(1,2,3)$ |
| 3 | (1) $k=6,c=14$; (2) $k=6$ |
| 4 | Determinant $0$; infinitely many solutions $(t,t,-2t)$ |
| 5 | (1) $y=\frac12x+2$; (2) $y=-2x+3$ |
| 6 | $(4,0)$ and $(0,3)$; distance $\frac{12}{5}$ |
| 7 | $(0,0),(4,0),(2,4),(0,6)$ |
| 8 | Maximum $14$ at $(2,4)$ |
| 9 | (1) $x=3\pm2\sqrt3$; (2) $x=1,5$ |
| 10 | $y=(x-2)^2-1$; vertex $(2,-1)$, axis $x=2$, opens up; intercepts $(1,0),(3,0),(0,3)$ |
| 11 | (1) $x=\pm3$; (2) $x=0,-5$; (3) $x=3,-\frac12$ |

## Part A: Systems of Linear Equations

### Problem 1 (8 points)

From $x-y=2$, $x=y+2$. Substitute into the first equation:

$$3(y+2)+2y=11\implies5y=5\implies y=1.$$

Then $x=3$, so $\boxed{(x,y)=(3,1)}$.

Award 3 points for a valid substitution or elimination setup, 3 for solving one
variable, and 2 for the ordered pair and check or correct back-substitution.

### Problem 2 (10 points)

Subtract the first equation from the second and third equations:

$$x-2y=-3,\qquad y-2z=-4.$$

From the first reduced equation, $x=2y-3$; from the second, $y=2z-4$.
Substitute into $x+y+z=6$:

$$
(2y-3)+y+z=6\implies3y+z=9.
$$

Now $3(2z-4)+z=9$, so $7z=21$ and $z=3$. Thus $y=2$ and $x=1$:
$\boxed{(x,y,z)=(1,2,3)}$.

Award 4 points for two independent reduced equations, 3 for solving the reduced
system, and 3 for the full ordered triple. Equivalent elimination paths earn full credit.

### Problem 3 (8 points)

Doubling $2x+3y=7$ gives $4x+6y=14$.

1. The equations are identical when $\boxed{k=6,c=14}$, giving infinitely many
   solutions. Award 2 points for each value with a valid reason.
2. With $c=15$ and $k=6$, the equations have the same left side but different right
   sides: $4x+6y=14$ and $4x+6y=15$. They cannot both hold, so $\boxed{k=6}$ gives no
   solution. Award 2 points for $k$ and 2 for the contradiction.

### Problem 4 (8 points)

The coefficient matrix is

$$A=\begin{pmatrix}1&1&1\\1&-1&0\\2&0&1\end{pmatrix}.$$

Its third row is the sum of its first two rows, so $\det(A)=\boxed{0}$.
Equivalently, expansion along the first row gives

$$\det(A)=(-1)-1+2=0.$$

Since the system is homogeneous, it has at least the zero solution. A zero determinant
means a free variable, so it has **infinitely many** solutions. From $x-y=0$, let
$x=y=t$. Then $x+y+z=0$ gives $z=-2t$, and the third equation also holds. All solutions
are $\boxed{(x,y,z)=(t,t,-2t),\ t\in\mathbb R}$.

Award 3 points for the determinant, 2 for the correct solution-count reasoning, and 3
for the parameterization.

## Part B: Lines and Distance

### Problem 5 (8 points)

The slope through the two points is

$$m=\frac{3-1}{2-(-2)}=\frac12.$$

Using $(2,3)$, $3=\frac12(2)+b$ gives $b=2$, so the first line is
$\boxed{y=\frac12x+2}$.

A perpendicular line has slope $-2$. Through $(2,-1)$, its equation is

$$y+1=-2(x-2)\implies\boxed{y=-2x+3}.$$

Award 2 points for each slope and 2 for each correct equation.

### Problem 6 (8 points)

Set $y=0$ for the $x$-intercept: $3x=12$, giving $\boxed{(4,0)}$.
Set $x=0$ for the $y$-intercept: $4y=12$, giving $\boxed{(0,3)}$.

Write the line as $3x+4y-12=0$. The distance from $(0,0)$ is

$$d=\frac{|3(0)+4(0)-12|}{\sqrt{3^2+4^2}}=\boxed{\frac{12}{5}}.$$

Award 2 points per intercept, 2 for the correct distance setup, and 2 for the exact
distance.

## Part C: Inequalities and Linear Programming

### Problem 7 (12 points)

All four boundaries are **solid** because the inequalities include equality. The
feasible region is in the first quadrant and lies below both $x+y=6$ and $2x+y=8$.

The sloping lines intersect at

$$
\begin{cases}x+y=6\\2x+y=8\end{cases}
\implies x=2,\quad y=4.
$$

On the $x$-axis, $2x\le8$ limits the region to $x=4$; on the $y$-axis,
$y\le6$ limits it to $y=6$. Going around the region, the vertices are
$\boxed{(0,0),(4,0),(2,4),(0,6)}$.

Award 4 points for correct labeled solid boundaries, 2 for the correct shaded overlap,
and 6 for all four vertices (including the intersection calculation). A clear equivalent
graph earns full credit.

### Problem 8 (8 points)

Evaluate $P=3x+2y$ at each vertex from Problem 7:

| Vertex | $P$ |
| --- | ---: |
| $(0,0)$ | $0$ |
| $(4,0)$ | $12$ |
| $(2,4)$ | $14$ |
| $(0,6)$ | $12$ |

Thus the maximum is $\boxed{14}$ at $\boxed{(2,4)}$.

Award 1 point for each vertex evaluation, 2 for the maximum value, and 2 for its
location. Use the student's feasible vertices consistently for follow-through credit.

## Part D: Quadratics

### Problem 9 (10 points)

1. $x-3=\pm\sqrt{12}=\pm2\sqrt3$, so
   $\boxed{x=3\pm2\sqrt3}$. Award 2 points for both signs and 2 for simplified exact
   answers.
2. Move the constant and add $9$ to both sides:

   $$x^2-6x=-5\implies x^2-6x+9=4\implies(x-3)^2=4.$$

   Hence $x-3=\pm2$, giving $\boxed{x=1,5}$. Award 2 points for rearranging and adding
   to both sides, 2 for the completed square, and 2 for both roots.

### Problem 10 (10 points)

Complete the square:

$$y=x^2-4x+3=(x-2)^2-1.$$

The vertex is $\boxed{(2,-1)}$, the axis is $\boxed{x=2}$, and the parabola opens
**upward**. Factoring $x^2-4x+3=(x-1)(x-3)$ gives $x$-intercepts
$\boxed{(1,0),(3,0)}$. At $x=0$, $y=3$, so the $y$-intercept is $\boxed{(0,3)}$.
The sketch should show a symmetric upward-opening parabola through these points.

Award 2 points for vertex form, 2 for vertex and axis, 1 for opening direction, 2 for
both $x$-intercepts, 1 for the $y$-intercept, and 2 for a consistent labeled sketch.

### Problem 11 (10 points)

1. $x^2-9=(x-3)(x+3)=0$, so $\boxed{x=3,-3}$. Award 1 point for factoring and 2 for
   both roots.
2. $x^2+5x=x(x+5)=0$, so $\boxed{x=0,-5}$. Award 1 point for factoring and 2 for both
   roots.
3. $2x^2-5x-3=(2x+1)(x-3)=0$, so $\boxed{x=-\frac12,3}$. Award 2 points for factoring
   and 2 for both roots.
