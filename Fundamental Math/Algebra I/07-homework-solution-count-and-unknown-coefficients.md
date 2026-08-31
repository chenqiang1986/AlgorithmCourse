# Homework: Lessons 5–6 — Solution Count and Unknown Coefficients
*Fundamental Math / Algebra I*

This homework covers
[05-geometric-interpretation-and-solution-count.md](./05-geometric-interpretation-and-solution-count.md)
(classifying a system's number of solutions) and
[06-unknown-coefficients.md](./06-unknown-coefficients.md) (solving for a missing
coefficient given the number of solutions). Attempt each problem before revealing its
solution.

## Part A: Solution Count

### Problem 1

Without fully solving, determine how many solutions this system has:

$$
\begin{cases}
6x + 4y = 10 \\
3x + 2y = 5
\end{cases}
$$

<details>
<summary>Solution</summary>

Multiply the second equation by $2$: $6x + 4y = 10$ — identical to the first equation. Every
coefficient ratio matches ($\tfrac{6}{3} = \tfrac{4}{2} = \tfrac{10}{5} = 2$), so the two
equations describe the same line.

The answer is **infinitely many solutions**.

</details>

### Problem 2

Without fully solving, determine how many solutions this system has:

$$
\begin{cases}
2x - 5y = 7 \\
4x - 10y = 9
\end{cases}
$$

<details>
<summary>Solution</summary>

Compare coefficient ratios: $\dfrac{4}{2} = 2$ and $\dfrac{-10}{-5} = 2$, but
$\dfrac{9}{7} \ne 2$. The slopes match but the constants don't, so the lines are parallel
and distinct.

The answer is **no solution**.

</details>

### Problem 3

Without fully solving, determine how many solutions this system has:

$$
\begin{cases}
3x + y = 7 \\
x - 2y = 0
\end{cases}
$$

<details>
<summary>Solution</summary>

Rewrite both in slope-intercept form. From $3x + y = 7$: $y = -3x + 7$, slope $-3$. From
$x - 2y = 0$: $y = \tfrac12 x$, slope $\tfrac12$. The slopes differ, so the lines cross at
exactly one point.

The answer is **exactly one solution**.

</details>

## Part B: Unknown Coefficients

### Problem 4

Find the value of $k$ that makes this system have **no solution**:

$$
\begin{cases}
4x + ky = 7 \\
8x + 10y = 3
\end{cases}
$$

<details>
<summary>Solution</summary>

Match the $x$- and $y$-coefficient ratios so the lines are parallel:

$$
\frac{4}{8} = \frac12 \qquad \qquad \frac{k}{10} = \frac12 \implies k = 5
$$

Check the constants at $k = 5$: $\dfrac{7}{3}$, which is **not** $\dfrac12$. Slopes match,
intercepts don't, so the lines are parallel and distinct.

The answer is **$k = 5$**.

</details>

### Problem 5

Find the value of $k$ that makes this system have **infinitely many solutions**:

$$
\begin{cases}
6x + 9y = 15 \\
2x + ky = 5
\end{cases}
$$

<details>
<summary>Solution</summary>

The $x$-coefficients and constants are already proportional: $\dfrac{6}{2} = \dfrac{15}{5}
= 3$. Solve for the $k$ that makes the $y$-coefficient ratio match that same value:

$$
\frac{9}{k} = 3 \implies k = 3
$$

At $k = 3$, the second equation $2x + 3y = 5$ scaled by $3$ gives exactly the first
equation — the same line.

The answer is **$k = 3$**.

</details>

### Problem 6

Find the values of $k$ and $m$ that make this system have **infinitely many solutions**:

$$
\begin{cases}
kx + 5y = 20 \\
6x + my = 8
\end{cases}
$$

<details>
<summary>Solution</summary>

The constants are the only pair with no unknown in it, so anchor the ratio there:
$\dfrac{20}{8} = \dfrac52$. Apply that ratio to the other two pairs:

$$
\frac{k}{6} = \frac52 \implies k = 15 \qquad \qquad \frac{5}{m} = \frac52 \implies m = 2
$$

Check: at $k = 15, m = 2$, the first equation $15x + 5y = 20$ divides down to
$3x + y = 4$, and the second equation $6x + 2y = 8$ divides down to the same
$3x + y = 4$ — the same line.

The answer is **$k = 15$, $m = 2$**.

</details>

### Problem 7

Determine whether any value of $k$ makes this system have **no solution**. If so, find it;
if not, explain why no such $k$ exists.

$$
\begin{cases}
3x + ky = 6 \\
9x + 15y = 18
\end{cases}
$$

<details>
<summary>Solution</summary>

The $x$-coefficient and constant ratios don't involve $k$, and they already match:
$\dfrac{3}{9} = \dfrac{6}{18} = \dfrac13$. No solution needs the $y$-coefficient ratio to
equal $\tfrac13$ **and** the constants to disagree — but the constants already agree.
Matching the $y$-ratio ($\tfrac{k}{15} = \tfrac13 \implies k = 5$) produces infinitely many
solutions instead. For every other $k$, the $y$-ratio misses $\tfrac13$, giving different
slopes and exactly one solution.

The answer is **no such value of $k$ exists** — this system is either infinitely many
solutions ($k = 5$) or exactly one solution (any other $k$), never zero.

</details>
