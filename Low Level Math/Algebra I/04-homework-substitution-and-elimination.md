# Homework: Lessons 3–4 — Substitution and Elimination

This homework covers [03-systems-graphing-and-substitution.md](./03-systems-graphing-and-substitution.md)
(substitution) and [04-elimination-method.md](./04-elimination-method.md) (elimination).
Attempt each problem before revealing its solution.

## Part A: Substitution

### Problem 1

Solve the system for $(x, y)$:

$$
\begin{cases}
y = 2x - 3 \\
3x + y = 12
\end{cases}
$$

<details>
<summary>Solution</summary>

Substitute $2x - 3$ for $y$ in the second equation:

$$
\begin{aligned}
3x + (2x - 3) &= 12 \\
5x - 3 &= 12 \\
5x &= 15 \\
x &= 3
\end{aligned}
$$

Back-substitute into $y = 2x - 3$: $y = 2(3) - 3 = 3$.

Check: $y = 2(3) - 3 = 3$ ✓, and $3(3) + 3 = 12$ ✓.

The answer is **$(3, 3)$**.

</details>

### Problem 2

Solve the system for $(x, y)$:

$$
\begin{cases}
3x + 4y = 2 \\
5x - 2y = 12
\end{cases}
$$

<details>
<summary>Solution</summary>

Neither equation is solved for a variable, and no coefficient is $\pm 1$. Solve the first
equation for $x$:

$$
3x = 2 - 4y \implies x = \frac{2 - 4y}{3}
$$

Substitute into the second equation and clear the fraction by multiplying by $3$:

$$
\begin{aligned}
5\left(\frac{2 - 4y}{3}\right) - 2y &= 12 \\
5(2 - 4y) - 6y &= 36 \\
10 - 20y - 6y &= 36 \\
10 - 26y &= 36 \\
-26y &= 26 \\
y &= -1
\end{aligned}
$$

Back-substitute into $x = \dfrac{2 - 4y}{3}$: $x = \dfrac{2 - 4(-1)}{3} = \dfrac{6}{3} = 2$.

Check: $3(2) + 4(-1) = 6 - 4 = 2$ ✓, and $5(2) - 2(-1) = 10 + 2 = 12$ ✓.

The answer is **$(2, -1)$**.

</details>

## Part B: Elimination

### Problem 3

Solve the system for $(x, y)$:

$$
\begin{cases}
4x - y = 9 \\
2x + y = 3
\end{cases}
$$

<details>
<summary>Solution</summary>

The $y$-coefficients are already opposites ($-1$ and $+1$), so add the equations:

$$
\begin{aligned}
(4x - y) + (2x + y) &= 9 + 3 \\
6x &= 12 \\
x &= 2
\end{aligned}
$$

Back-substitute into $2x + y = 3$: $2(2) + y = 3 \implies y = -1$.

Check: $4(2) - (-1) = 8 + 1 = 9$ ✓, and $2(2) + (-1) = 4 - 1 = 3$ ✓.

The answer is **$(2, -1)$**.

</details>

### Problem 4

Solve the system for $(x, y)$:

$$
\begin{cases}
3x + 2y = 16 \\
5x - 3y = 14
\end{cases}
$$

<details>
<summary>Solution</summary>

Neither variable has matching or opposite coefficients. The $y$-coefficients are $2$ and
$-3$; multiply the first equation by $3$ and the second by $2$ so they become opposites:

$$
\begin{aligned}
3(3x + 2y) &= 3(16) &\implies 9x + 6y &= 48 \\
2(5x - 3y) &= 2(14) &\implies 10x - 6y &= 28
\end{aligned}
$$

Add the two equations:

$$
\begin{aligned}
(9x + 6y) + (10x - 6y) &= 48 + 28 \\
19x &= 76 \\
x &= 4
\end{aligned}
$$

Back-substitute into $3x + 2y = 16$: $3(4) + 2y = 16 \implies 2y = 4 \implies y = 2$.

Check: $3(4) + 2(2) = 12 + 4 = 16$ ✓, and $5(4) - 3(2) = 20 - 6 = 14$ ✓.

The answer is **$(4, 2)$**.

</details>

## Part C: Choose Your Method

Each problem below can be solved by either substitution or elimination — pick whichever
avoids more fractions before you start.

### Problem 5

Solve the system for $(x, y)$:

$$
\begin{cases}
x = 3y + 1 \\
2x - 5y = 11
\end{cases}
$$

<details>
<summary>Solution</summary>

One equation is already solved for $x$, so substitution is the natural choice. Substitute
$3y + 1$ for $x$ in the second equation:

$$
\begin{aligned}
2(3y + 1) - 5y &= 11 \\
6y + 2 - 5y &= 11 \\
y + 2 &= 11 \\
y &= 9
\end{aligned}
$$

Back-substitute into $x = 3y + 1$: $x = 3(9) + 1 = 28$.

Check: $x = 3(9) + 1 = 28$ ✓, and $2(28) - 5(9) = 56 - 45 = 11$ ✓.

The answer is **$(28, 9)$**.

</details>

### Problem 6

Solve the system for $(x, y)$:

$$
\begin{cases}
7x + 2y = 1 \\
7x - 3y = 16
\end{cases}
$$

<details>
<summary>Solution</summary>

The $x$-coefficients are already equal ($7$ and $7$), so elimination is the natural
choice — subtract the second equation from the first:

$$
\begin{aligned}
(7x + 2y) - (7x - 3y) &= 1 - 16 \\
5y &= -15 \\
y &= -3
\end{aligned}
$$

Back-substitute into $7x + 2y = 1$: $7x + 2(-3) = 1 \implies 7x = 7 \implies x = 1$.

Check: $7(1) + 2(-3) = 7 - 6 = 1$ ✓, and $7(1) - 3(-3) = 7 + 9 = 16$ ✓.

The answer is **$(1, -3)$**.

</details>

### Problem 7 (Word Problem)

The sum of two numbers is $15$. Twice the first number minus the second number is $3$.
Find the two numbers.

<details>
<summary>Solution</summary>

Let $x$ be the first number and $y$ be the second number:

$$
\begin{cases}
x + y = 15 \\
2x - y = 3
\end{cases}
$$

The $y$-coefficients are already opposites, so add the equations:

$$
\begin{aligned}
(x + y) + (2x - y) &= 15 + 3 \\
3x &= 18 \\
x &= 6
\end{aligned}
$$

Back-substitute into $x + y = 15$: $6 + y = 15 \implies y = 9$.

Check: $6 + 9 = 15$ ✓, and $2(6) - 9 = 12 - 9 = 3$ ✓.

The two numbers are **$6$ and $9$**.

</details>
