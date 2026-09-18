# Homework: Lesson 12 — Quadratic Equations and Completing the Square
*Fundamental Math / Algebra I*

This homework covers [Lesson 12](./12-quadratic-equations-square-roots-and-completing-the-square.md):
solving by square roots, completing the square, and identifying whether a quadratic has two,
one, or no real roots. Show every algebra step before revealing a solution. Keep fractions
and radicals exact unless a decimal approximation is requested.

## Part A: Solve by Square Roots

### Problem 1

Solve $x^2-81=0$.

<details>
<summary>Solution</summary>

$$x^2=81 \implies x=\pm9.$$

The roots are $\boxed{x=9\text{ or }x=-9}$.

</details>

### Problem 2

Solve $2(x+4)^2=50$.

<details>
<summary>Solution</summary>

$$
2(x+4)^2=50 \implies (x+4)^2=25 \implies x+4=\pm5.
$$

Thus $\boxed{x=1\text{ or }x=-9}$.

</details>

### Problem 3

Solve $5(x-2)^2+20=0$ over the real numbers.

<details>
<summary>Solution</summary>

$$5(x-2)^2=-20 \implies (x-2)^2=-4.$$

A real number cannot have a negative square, so there are
$\boxed{\text{no real solutions}}$.

</details>

## Part B: Complete the Square When the Leading Coefficient Is 1

### Problem 4

Solve $x^2+8x+7=0$ by completing the square.

<details>
<summary>Solution</summary>

Move the constant, then add $\left(\frac82\right)^2=16$ to both sides:

$$
\begin{aligned}
x^2+8x&=-7\\
x^2+8x+16&=-7+16\\
(x+4)^2&=9\\
x+4&=\pm3.
\end{aligned}
$$

Therefore $\boxed{x=-1\text{ or }x=-7}$.

</details>

### Problem 5

Solve $x^2-6x+9=0$ by completing the square. State how many real roots it has.

<details>
<summary>Solution</summary>

$$
\begin{aligned}
x^2-6x&=-9\\
x^2-6x+9&=-9+9\\
(x-3)^2&=0.
\end{aligned}
$$

So $x-3=0$, and $\boxed{x=3}$. The equation has one real root, a repeated root.

</details>

### Problem 6

Solve $x^2+2x+5=0$ over the real numbers by completing the square.

<details>
<summary>Solution</summary>

$$
\begin{aligned}
x^2+2x&=-5\\
x^2+2x+1&=-5+1\\
(x+1)^2&=-4.
\end{aligned}
$$

There are $\boxed{\text{no real solutions}}$, because no real square equals $-4$.

</details>

## Part C: Divide First, Then Complete the Square

### Problem 7

Solve $3x^2+12x+9=0$ by completing the square.

<details>
<summary>Solution</summary>

Divide every term by $3$:

$$x^2+4x+3=0.$$

Then complete the square:

$$
\begin{aligned}
x^2+4x&=-3\\
x^2+4x+4&=-3+4\\
(x+2)^2&=1\\
x+2&=\pm1.
\end{aligned}
$$

Thus $\boxed{x=-1\text{ or }x=-3}$.

</details>

### Problem 8

Solve $4x^2+4x-3=0$ by completing the square.

<details>
<summary>Solution</summary>

Divide every term by $4$:

$$x^2+x-\frac34=0.$$

Half of $1$ is $\frac12$, so add $\frac14$ to both sides:

$$
\begin{aligned}
x^2+x&=\frac34\\
x^2+x+\frac14&=\frac34+\frac14\\
\left(x+\frac12\right)^2&=1\\
x+\frac12&=\pm1.
\end{aligned}
$$

The roots are $\boxed{x=\frac12\text{ or }x=-\frac32}$.

</details>

### Problem 9

Solve $3x^2+x-2=0$ by completing the square. Do not factor it.

<details>
<summary>Solution</summary>

After dividing by $3$, both non-leading coefficients are fractions:

$$x^2+\frac13x-\frac23=0.$$

Move the constant. Half of $\frac13$ is $\frac16$, and its square is $\frac1{36}$:

$$
\begin{aligned}
x^2+\frac13x&=\frac23\\
x^2+\frac13x+\frac1{36}&=\frac23+\frac1{36}\\
\left(x+\frac16\right)^2&=\frac{25}{36}\\
x+\frac16&=\pm\frac56.
\end{aligned}
$$

So $\boxed{x=\frac23\text{ or }x=-1}$.

</details>

### Problem 10

Solve $5x^2+10x+7=0$ over the real numbers by completing the square.

<details>
<summary>Solution</summary>

Divide every term by $5$:

$$x^2+2x+\frac75=0.$$

$$
\begin{aligned}
x^2+2x&=-\frac75\\
x^2+2x+1&=-\frac75+1\\
(x+1)^2&=-\frac25.
\end{aligned}
$$

There are $\boxed{\text{no real solutions}}$.

</details>

### Problem 11

Solve $9x^2-12x+4=0$ by completing the square. State how many real roots it has.

<details>
<summary>Solution</summary>

Divide every term by $9$:

$$x^2-\frac43x+\frac49=0.$$

Half of $-\frac43$ is $-\frac23$, whose square is $\frac49$:

$$
\begin{aligned}
x^2-\frac43x&=-\frac49\\
x^2-\frac43x+\frac49&=-\frac49+\frac49\\
\left(x-\frac23\right)^2&=0.
\end{aligned}
$$

Thus $\boxed{x=\frac23}$ is the one real root, repeated.

</details>

## Part D: Explain the Result

### Problem 12

Without solving for $x$, state the number of real roots in each equation and explain why.

1. $(x-5)^2=16$
2. $(x+3)^2=0$
3. $(x-1)^2=-\frac72$

<details>
<summary>Solution</summary>

1. Two real roots: a positive number has two real square roots.
2. One repeated real root: only $0^2$ equals $0$.
3. No real roots: no real square can be negative.

</details>

## Before You Submit

- Did you move the constant before adding the number that completes the square?
- Did you add the same number to both sides?
- Did you divide **every** term by the leading coefficient before completing the square?
- Did you write $\pm$ when the completed square equals a positive number?
- Did you state “no real solutions” when the completed square equals a negative number?
