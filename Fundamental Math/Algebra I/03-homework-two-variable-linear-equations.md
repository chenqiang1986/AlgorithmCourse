# Homework: Lesson 3 — Two-Variable Linear Equations
*Fundamental Math / Algebra I*

This homework covers [03-two-variable-linear-equations.md](./03-two-variable-linear-equations.md):
what a solution means, the substitution method, and the elimination method. Attempt each
problem before revealing its solution, and check every answer in **both** original
equations.

## Part A: What Is a Solution?

### Problem 1

Which of the ordered pairs $(2, -1)$ and $(4, -2)$ is a solution of the system? Show the
check for each pair.

$$
\begin{cases}
x + 2y = 0 \\
3x - y = 7
\end{cases}
$$

<details>
<summary>Solution</summary>

Test $(2, -1)$: $2 + 2(-1) = 0$ ✓ and $3(2) - (-1) = 7$ ✓. Both hold.

Test $(4, -2)$: $4 + 2(-2) = 0$ ✓ but $3(4) - (-2) = 14 \ne 7$. The second equation fails.

The answer is **$(2, -1)$ only**. A pair must satisfy both equations at once.

</details>

## Part B: Substitution

### Problem 2

Solve the system for $(x, y)$:

$$
\begin{cases}
y = 2x + 1 \\
3x + 2y = 16
\end{cases}
$$

<details>
<summary>Solution</summary>

$$
\begin{aligned}
3x + 2(2x + 1) &= 16 \\
7x + 2 &= 16 \\
x &= 2
\end{aligned}
$$

Then $y = 2(2) + 1 = 5$. Check: $3(2) + 2(5) = 16$ ✓.

The answer is **$(2, 5)$**.

</details>

### Problem 3

Solve the system for $(x, y)$. Choose the variable that avoids fractions.

$$
\begin{cases}
x + 2y = 7 \\
3x - y = 7
\end{cases}
$$

<details>
<summary>Solution</summary>

Solve the first equation for $x$ (its coefficient is $1$): $x = 7 - 2y$. Substitute:

$$
\begin{aligned}
3(7 - 2y) - y &= 7 \\
21 - 6y - y &= 7 \\
-7y &= -14 \\
y &= 2
\end{aligned}
$$

Then $x = 7 - 2(2) = 3$. Check: $3 + 2(2) = 7$ ✓ and $3(3) - 2 = 7$ ✓.

The answer is **$(3, 2)$**.

</details>

### Problem 4

Solve the system for $(x, y)$. Be careful with the sign when substituting.

$$
\begin{cases}
y = -x + 4 \\
2x - 3y = -2
\end{cases}
$$

<details>
<summary>Solution</summary>

Substitute the whole expression $(-x + 4)$ for $y$:

$$
\begin{aligned}
2x - 3(-x + 4) &= -2 \\
2x + 3x - 12 &= -2 \\
5x &= 10 \\
x &= 2
\end{aligned}
$$

Then $y = -2 + 4 = 2$. Check: $2(2) - 3(2) = -2$ ✓.

The answer is **$(2, 2)$**.

</details>

### Problem 5

Solve the system for $(x, y)$. No coefficient is $\pm 1$, so a fraction is unavoidable.

$$
\begin{cases}
2x + 5y = 1 \\
3x + 4y = 5
\end{cases}
$$

<details>
<summary>Solution</summary>

Solve the first equation for $x$: $x = \dfrac{1 - 5y}{2}$. Substitute and multiply through
by $2$:

$$
\begin{aligned}
3\left(\frac{1 - 5y}{2}\right) + 4y &= 5 \\
3(1 - 5y) + 8y &= 10 \\
3 - 15y + 8y &= 10 \\
-7y &= 7 \\
y &= -1
\end{aligned}
$$

Then $x = \dfrac{1 - 5(-1)}{2} = 3$. Check: $2(3) + 5(-1) = 1$ ✓ and
$3(3) + 4(-1) = 5$ ✓.

The answer is **$(3, -1)$**.

</details>

## Part C: Elimination

### Problem 6

Solve the system for $(x, y)$ by subtracting the equations:

$$
\begin{cases}
3x + 2y = 12 \\
3x - y = 3
\end{cases}
$$

<details>
<summary>Solution</summary>

The $x$-coefficients are equal. Subtract the second equation from the first:

$$(3x + 2y) - (3x - y) = 12 - 3 \implies 3y = 9 \implies y = 3$$

Then $3x - 3 = 3 \implies x = 2$. Check: $3(2) + 2(3) = 12$ ✓.

The answer is **$(2, 3)$**.

</details>

### Problem 7

Solve the system for $(x, y)$ by adding the equations:

$$
\begin{cases}
2x + 3y = 7 \\
4x - 3y = 5
\end{cases}
$$

<details>
<summary>Solution</summary>

The $y$-coefficients are opposites. Add:

$$6x = 12 \implies x = 2$$

Then $2(2) + 3y = 7 \implies y = 1$. Check: $4(2) - 3(1) = 5$ ✓.

The answer is **$(2, 1)$**.

</details>

### Problem 8

Solve the system for $(x, y)$. Scale one equation first.

$$
\begin{cases}
5x + 2y = 4 \\
3x - 4y = 18
\end{cases}
$$

<details>
<summary>Solution</summary>

Multiply the first equation by $2$ (every term) so the $y$-coefficients are $+4$ and $-4$:

$$10x + 4y = 8$$

Add to the second equation:

$$13x = 26 \implies x = 2$$

Then $5(2) + 2y = 4 \implies y = -3$. Check: $3(2) - 4(-3) = 18$ ✓.

The answer is **$(2, -3)$**.

</details>

### Problem 9

Solve the system for $(x, y)$. Both equations must be scaled.

$$
\begin{cases}
3x + 2y = 6 \\
2x + 5y = -7
\end{cases}
$$

<details>
<summary>Solution</summary>

Eliminate $x$ (coefficients $3$ and $2$, common multiple $6$). Multiply the first equation
by $2$ and the second by $3$:

$$
\begin{aligned}
6x + 4y &= 12 \\
6x + 15y &= -21
\end{aligned}
$$

Subtract the first from the second: $11y = -33 \implies y = -3$.

Then $3x + 2(-3) = 6 \implies 3x = 12 \implies x = 4$. Check: $2(4) + 5(-3) = -7$ ✓.

The answer is **$(4, -3)$**.

</details>

## Part D: Special Systems

### Problem 10

Solve the system, or state that it has no solution or infinitely many solutions:

$$
\begin{cases}
3x - 2y = 4 \\
6x - 4y = 9
\end{cases}
$$

<details>
<summary>Solution</summary>

Multiply the first equation by $2$: $6x - 4y = 8$. Subtract it from the second equation:

$$0 = 1$$

Both variables vanish and the statement is false.

The answer is **no solution**.

</details>

### Problem 11

Solve the system, or state that it has no solution or infinitely many solutions:

$$
\begin{cases}
x + 3y = 2 \\
2x + 6y = 4
\end{cases}
$$

<details>
<summary>Solution</summary>

Multiply the first equation by $2$: $2x + 6y = 4$. Subtract it from the second equation:

$$0 = 0$$

Both variables vanish and the statement is true.

The answer is **infinitely many solutions**.

</details>

## Part E: Find the Error

### Problem 12

A student solved the system below and got $y = \dfrac{11}{7}$. Find the mistake, then give
the correct solution.

$$
\begin{cases}
2x + 3y = 8 \\
x - 2y = -3
\end{cases}
$$

Student's work: multiply the second equation by $2$ to get $2x - 4y = -3$, subtract from the
first to get $7y = 11$.

<details>
<summary>Solution</summary>

The student multiplied $x - 2y$ by $2$ but left the right-hand side as $-3$. Every term must
be scaled: $2(-3) = -6$, so the equation is $2x - 4y = -6$.

Subtract from the first equation: $7y = 14 \implies y = 2$. Then $x - 2(2) = -3 \implies
x = 1$. Check: $2(1) + 3(2) = 8$ ✓.

The correct answer is **$(1, 2)$**.

</details>

## Before You Submit

- Did you report **both** $x$ and $y$?
- Did you check the pair in **both** original equations?
- When you scaled an equation, did you multiply the right-hand side too?
