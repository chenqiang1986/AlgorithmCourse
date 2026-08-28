# Homework: Lessons 3–4 — Solving Linear Equations
*Low Level Math / Algebra I*

This homework covers [03-two-variable-linear-equations.md](./03-two-variable-linear-equations.md)
(substitution, elimination, and choosing between them) and
[04-three-variable-linear-equations.md](./04-three-variable-linear-equations.md)
(extending elimination to three variables). Attempt each problem before revealing its
solution.

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

## Part D: Three-Variable Systems

Each problem below needs two independent eliminations of the same variable, from two
different pairs of equations, before it reduces to a two-variable system.

### Problem 8

Solve the system for $(x, y, z)$:

$$
\begin{cases}
3x - 2y + z = 16 \\
x + 4y - 3z = -22 \\
2x - y + 2z = 15
\end{cases}
$$

<details>
<summary>Solution</summary>

Label the equations (1), (2), (3). Eliminate $x$ from (1) and (2): the $x$-coefficients
are $3$ and $1$, so multiply (2) by $3$:

$$
3(x+4y-3z) = 3(-22) \implies 3x+12y-9z = -66
$$

Subtract from (1): $(3x-2y+z)-(3x+12y-9z) = 16-(-66) \implies -14y+10z = 82$, which
simplifies (dividing by $-2$) to $7y - 5z = -41 \quad (4)$

Eliminate $x$ from (1) and (3) — a different pair. The $x$-coefficients are $3$ and $2$,
LCM $6$. Multiply (1) by $2$ and (3) by $3$:

$$
\begin{aligned}
2(3x-2y+z) &= 2(16) &\implies 6x-4y+2z &= 32 \\
3(2x-y+2z) &= 3(15) &\implies 6x-3y+6z &= 45
\end{aligned}
$$

Subtract: $(6x-4y+2z)-(6x-3y+6z) = 32-45 \implies -y-4z = -13$, i.e.
$y + 4z = 13 \quad (5)$

Solve (4) and (5). From (5): $y = 13 - 4z$. Substitute into (4):

$$
7(13-4z) - 5z = -41 \implies 91 - 28z - 5z = -41 \implies -33z = -132 \implies z = 4
$$

Then $y = 13 - 4(4) = -3$. Back-substitute into (1): $3x - 2(-3) + 4 = 16 \implies
3x + 10 = 16 \implies x = 2$.

Check (2): $2+4(-3)-3(4) = 2-12-12 = -22$ ✓. Check (3): $2(2)-(-3)+2(4) = 4+3+8 = 15$ ✓.

The answer is **$(2, -3, 4)$**.

</details>

### Problem 9

Solve the system for $(x, y, z)$:

$$
\begin{cases}
2x + 3y - z = -9 \\
x - 2y + 3z = 20 \\
3x - y + 2z = 15
\end{cases}
$$

<details>
<summary>Solution</summary>

Label the equations (1), (2), (3). Eliminate $x$ from (1) and (2): the $x$-coefficients
are $2$ and $1$, so multiply (2) by $2$:

$$
2(x-2y+3z) = 2(20) \implies 2x-4y+6z = 40
$$

Subtract from (1): $(2x+3y-z)-(2x-4y+6z) = -9-40 \implies 7y-7z = -49$, which simplifies
(dividing by $7$) to $y - z = -7 \quad (4)$

Eliminate $x$ from (1) and (3) — a different pair. The $x$-coefficients are $2$ and $3$,
LCM $6$. Multiply (1) by $3$ and (3) by $2$:

$$
\begin{aligned}
3(2x+3y-z) &= 3(-9) &\implies 6x+9y-3z &= -27 \\
2(3x-y+2z) &= 2(15) &\implies 6x-2y+4z &= 30
\end{aligned}
$$

Subtract: $(6x+9y-3z)-(6x-2y+4z) = -27-30 \implies 11y-7z = -57 \quad (5)$

Solve (4) and (5). From (4): $y = z - 7$. Substitute into (5):

$$
11(z-7) - 7z = -57 \implies 11z - 77 - 7z = -57 \implies 4z = 20 \implies z = 5
$$

Then $y = 5 - 7 = -2$. Back-substitute into (1): $2x + 3(-2) - 5 = -9 \implies
2x - 11 = -9 \implies x = 1$.

Check (2): $1-2(-2)+3(5) = 1+4+15 = 20$ ✓. Check (3): $3(1)-(-2)+2(5) = 3+2+10 = 15$ ✓.

The answer is **$(1, -2, 5)$**.

</details>

### Problem 10 (Word Problem)

The sum of three numbers is $20$. The first number plus twice the second number minus the
third number is $9$. Twice the first number minus the second number plus the third number
is $17$. Find the three numbers.

<details>
<summary>Solution</summary>

Let $x$, $y$, $z$ be the first, second, and third numbers:

$$
\begin{cases}
x + y + z = 20 & (1) \\
x + 2y - z = 9 & (2) \\
2x - y + z = 17 & (3)
\end{cases}
$$

Eliminate $x$ from (1) and (2): the $x$-coefficients already match ($1$ and $1$), so
subtract (2) from (1):

$$(x+y+z) - (x+2y-z) = 20-9 \implies -y+2z = 11 \quad (4)$$

Eliminate $x$ from (1) and (3) — a different pair, and a different technique, since the
$x$-coefficients ($1$ and $2$) don't already match. Multiply (1) by $2$:

$$2(x+y+z) = 2(20) \implies 2x+2y+2z = 40$$

Subtract (3): $(2x+2y+2z) - (2x-y+z) = 40-17 \implies 3y+z = 23 \quad (5)$

Solve (4) and (5). From (4): $y = 2z - 11$. Substitute into (5):

$$
3(2z-11) + z = 23 \implies 6z - 33 + z = 23 \implies 7z = 56 \implies z = 8
$$

Then $y = 2(8) - 11 = 5$. Back-substitute into (1): $x + 5 + 8 = 20 \implies x = 7$.

Check (2): $7+2(5)-8 = 7+10-8 = 9$ ✓. Check (3): $2(7)-5+8 = 14-5+8 = 17$ ✓.

The three numbers are **$7$, $5$, and $8$**.

</details>
