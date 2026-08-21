# Lesson 5: Systems of Linear Equations — Geometric Interpretation and Solution Count

Lessons 3 and 4 taught two algebraic techniques — substitution and elimination — for
finding a system's solution. This lesson steps back to ask what a solution *means*: two
linear equations graph as two lines, and their intersection is exactly the system's
solution set. That picture explains why every two-variable linear system has exactly one
solution, no solution, or infinitely many, and it gives a fast way to tell which case
you're in without fully solving.

## 1. Systems and Lines: The Geometric Picture

Every linear equation in two variables graphs as a straight line in the coordinate plane.
A point that satisfies an equation is exactly a point that lies on its line. So a solution
to a system — a point satisfying both equations — is exactly a point that lies on **both**
lines: an **intersection point**. This is the geometric meaning behind the algebra of
Lessons 3 and 4: solving a system by substitution or elimination is a way of *computing*
where two lines cross without having to graph them.

Two distinct lines in a plane relate to each other in exactly one of three ways, which
gives every two-variable linear system exactly one of three possible outcomes:

| Geometric relationship | Slopes and intercepts | Number of solutions | System is called |
|---|---|---|---|
| Lines cross at one point | $m_1 \ne m_2$ | Exactly one | Independent |
| Lines are parallel, never meet | $m_1 = m_2,\ b_1 \ne b_2$ | None | Inconsistent |
| Lines are the same line | $m_1 = m_2,\ b_1 = b_2$ | Infinitely many | Dependent |

Rewriting both equations in slope-intercept form $y = mx + b$ makes the comparison direct:
same slope means the lines are parallel or identical; different slope guarantees exactly
one crossing point.

![Three side-by-side line graphs. Left, "Independent, one solution": the lines y = x + 1 and y = -x + 1 cross at a single marked point. Middle, "Inconsistent, no solution": the parallel lines y = 2x + 3 and y = 2x - 1 have the same slope and never meet. Right, "Dependent, infinitely many solutions": y = 2x + 3 and 2y = 4x + 6 are drawn as a solid line and a dashed line lying exactly on top of each other, labeled "(same line)".](./images/three-line-cases.svg)

## 2. Core Idea: Reading the Leftover Statement

Both substitution and elimination work by combining the two equations into one. Normally
that one equation still has a variable in it, and you solve it. But if the two lines are
parallel or identical, the variable **cancels completely**, leaving a bare numeric
statement with no variable at all. That statement's truth value — not the fact that it
appeared — tells you which case you're in:

- A **false** statement (like $3 = -1$ or $0 = -6$) means the equations contradict each
  other: **no solution**. The lines are parallel with different intercepts.
- A **true** statement (like $6 = 6$ or $0 = 0$) means the second equation carries no new
  information: **infinitely many solutions**. The lines are the same line.
- If a variable survives instead of canceling completely, you get exactly **one**
  solution — the ordinary case from Lessons 3 and 4.

## 3. Reading Example: Detecting the Case via Substitution

**System A:**

$$
\begin{cases}
y = 2x + 3 \\
y = 2x - 1
\end{cases}
$$

Substitute: $2x + 3 = 2x - 1 \implies 3 = -1$. Both copies of $x$ cancel, leaving a
**false** statement. No value of $x$ can make this true, so the system has **no
solution**. Geometrically, both lines have slope $2$ but different $y$-intercepts ($3$ and
$-1$) — they are parallel.

**System B:**

$$
\begin{cases}
y = 2x + 3 \\
2y = 4x + 6
\end{cases}
$$

Substitute: $2(2x + 3) = 4x + 6 \implies 4x + 6 = 4x + 6 \implies 6 = 6$. Both copies of
$x$ cancel again, but this time the statement is **always true**. Every $x$ works, so the
system has **infinitely many solutions**. The second equation is just the first one
multiplied by $2$ — it is the same line.

## 4. Reading Example: Detecting the Case via Elimination

**No solution:**

$$
\begin{cases}
2x + 3y = 6 \\
4x + 6y = 6
\end{cases}
$$

Multiply the first equation by $-2$: $-4x - 6y = -12$. Add to the second equation:

$$(4x + 6y) + (-4x - 6y) = 6 + (-12) \implies 0 = -6$$

Both variables vanish, leaving a **false** statement — **no solution**. The left-hand
sides are proportional ($4x + 6y$ is exactly $2x + 3y$ doubled), but the right-hand sides
are not, so the lines are parallel with different intercepts.

**Infinitely many solutions:**

$$
\begin{cases}
x + 2y = 5 \\
2x + 4y = 10
\end{cases}
$$

Multiply the first equation by $-2$: $-2x - 4y = -10$. Add to the second equation:

$$(2x + 4y) + (-2x - 4y) = 10 + (-10) \implies 0 = 0$$

Both variables vanish, leaving a **true** statement — **infinitely many solutions**. The
second equation is exactly the first one multiplied by $2$: same line.

**Non-obvious detail:** substitution and elimination always agree on which case a system
falls into — they're two different routes to combining the same two equations, so a
contradiction or a tautology shows up under either method.

## 5. Class Practice 1: Identify the Number of Solutions

### Problem

Without fully solving, determine how many solutions this system has:

$$
\begin{cases}
6x - 3y = 12 \\
4x - 2y = 8
\end{cases}
$$

### Answer Choices

(A) Exactly one solution
(B) No solution
(C) Infinitely many solutions
(D) Cannot be determined without more information

<details>
<summary>Solution</summary>

Rewrite both in slope-intercept form. From $6x - 3y = 12$: $y = 2x - 4$. From
$4x - 2y = 8$: $y = 2x - 4$. Both equations describe the exact same line (the second is the
first multiplied by $\tfrac{2}{3}$), so every point on the line is a solution.

The answer is **(C) Infinitely many solutions**.

</details>

## 6. Class Practice 2: Determine Solution Type via Elimination

### Problem

Use elimination to determine how many solutions this system has, without finding the
exact solution:

$$
\begin{cases}
5x - 2y = 8 \\
-10x + 4y = -16
\end{cases}
$$

<details>
<summary>Solution</summary>

Multiply the first equation by $2$: $10x - 4y = 16$. Add to the second equation:

$$(10x - 4y) + (-10x + 4y) = 16 + (-16) \implies 0 = 0$$

Both variables vanish and the leftover statement is true, so every point satisfying the
first equation also satisfies the second.

The answer is **infinitely many solutions**.

</details>

## 7. Common Mistakes

### 7.1 Assuming "variable vanishes" always means no solution

A vanished variable can mean no solution ($3 = -1$) *or* infinitely many solutions
($6 = 6$). Check whether the leftover numeric statement is true or false — the vanishing
itself only tells you the lines are parallel or identical, not which of the two.

### 7.2 Reading $0 = 0$ and $0 = k$ backwards

A true leftover statement ($0 = 0$) means infinitely many solutions (the equations
describe the same line); a false one ($0 = -6$, or any $0 = k$ with $k \ne 0$) means no
solution (parallel lines). It's easy to swap these under time pressure — anchor it to the
statement's truth value, not its shape.

### 7.3 Comparing only slopes, not intercepts

Equal slopes alone don't distinguish "no solution" from "infinitely many" — that split
depends on whether the intercepts also match. Two lines with the same slope are either
parallel (different intercepts) or identical (same intercept); always check both.

## 8. Key Takeaways

- A solution to a two-variable linear system is a point $(x, y)$ satisfying both
  equations — geometrically, the intersection of their two lines.
- Comparing slopes and intercepts predicts the outcome: different slopes give one
  solution, same slope with different intercepts gives no solution, and identical lines
  give infinitely many solutions.
- If both variables cancel during substitution or elimination, the resulting numeric
  statement (not the vanishing itself) tells you no solution (false) vs. infinitely many
  (true).
- Substitution and elimination always agree on which case a system falls into — use
  whichever method you'd already use to solve it.

Next lesson: [06-unknown-coefficients.md](./06-unknown-coefficients.md) turns this
lesson's classification around — given the desired number of solutions, solve for a
missing coefficient (or two).
