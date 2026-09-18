# Homework: Lesson 9 — Unknown Coefficients and Solution Structure
*Fundamental Math / Course 3*

This homework covers [09-unknown-coefficients-and-solution-structure.md](./09-unknown-coefficients-and-solution-structure.md).
For each problem, classify all values of $k$ as giving exactly one solution, no solution, or
infinitely many solutions. Give the value of $x$ in the one-solution case when requested.
Attempt each problem before revealing its solution.

## Part A: One Exceptional Value

### Problem 1

Determine the solution structure of $kx+9=2x+4$. Give $x$ when there is exactly one
solution.

<details>
<summary>Solution</summary>

$$kx-2x=4-9 \implies (k-2)x=-5.$$

At $k=2$, this is $0x=-5$, so there is **no solution**. For $k\ne2$, there is exactly one
solution:

$$x=-\frac{5}{k-2}.$$

There is no value of $k$ giving infinitely many solutions.

</details>

### Problem 2

Determine the solution structure of $6x-1=kx-1$.

<details>
<summary>Solution</summary>

$$6x-kx=0 \implies (6-k)x=0.$$

At $k=6$, this is $0x=0$, so there are **infinitely many solutions**. For $k\ne6$, divide
by $6-k$ to get $x=0$, so there is **exactly one solution**. There is no no-solution case.

</details>

### Problem 3

Determine the solution structure of $4(x-2)+kx=7x-8$.

<details>
<summary>Solution</summary>

Distribute first:

$$4x-8+kx=7x-8 \implies (k-3)x=0.$$

If $k=3$, then $0x=0$, giving **infinitely many solutions**. If $k\ne3$, then $x=0$, giving
**exactly one solution**. There is no no-solution case.

</details>

### Problem 4

Determine the solution structure of $3(x+2)+kx=5x+1$. Give $x$ when there is exactly one
solution.

<details>
<summary>Solution</summary>

$$3x+6+kx=5x+1 \implies (k-2)x=-5.$$

If $k=2$, this says $0x=-5$, so there is **no solution**. If $k\ne2$, there is exactly one
solution:

$$x=-\frac{5}{k-2}.$$

There is no infinite-solution case.

</details>

## Part B: The Parameter in a Constant Term

### Problem 5

Determine the solution structure of $9x+k=9x-3$.

<details>
<summary>Solution</summary>

Subtract $9x$ from both sides to get $k=-3$.

If $k=-3$, the equation is true for every $x$, so there are **infinitely many solutions**.
For every $k\ne-3$, the statement is false, so there is **no solution**. There is never
exactly one solution.

</details>

### Problem 6

Determine the solution structure of $5x+12=5x+k$.

<details>
<summary>Solution</summary>

Subtract $5x$ from both sides: $12=k$.

Thus $k=12$ gives **infinitely many solutions**, and every $k\ne12$ gives **no solution**.
There is never exactly one solution.

</details>

## Part C: Multiple Exceptional Values

### Problem 7

Determine the solution structure of $(k-4)(k+1)x=k-4$.

<details>
<summary>Solution</summary>

The coefficient of $x$ is zero at $k=4$ and $k=-1$.

- At $k=4$: $0x=0$, so there are **infinitely many solutions**.
- At $k=-1$: $0x=-5$, so there is **no solution**.
- For $k\ne4,-1$, divide to get $x=\dfrac1{k+1}$, so there is **exactly one solution**.

</details>

### Problem 8

Determine the solution structure of $(k-2)(k-5)x+ k-2=0$.

<details>
<summary>Solution</summary>

The coefficient of $x$ is zero at $k=2$ and $k=5$.

- At $k=2$: $0x+0=0$, so there are **infinitely many solutions**.
- At $k=5$: $0x+3=0$, so there is **no solution**.
- For $k\ne2,5$, there is **exactly one solution**:

$$x=-\frac{k-2}{(k-2)(k-5)}=-\frac1{k-5}.$$

</details>

## Part D: Synthesis

### Problem 9

For what value(s) of $k$ does the equation $(k^2-9)x=2k+6$ have no solution, infinitely
many solutions, or exactly one solution?

<details>
<summary>Solution</summary>

Factor the coefficient of $x$:

$$ (k-3)(k+3)x=2(k+3). $$

The special values are $k=3$ and $k=-3$.

- At $k=3$: $0x=12$, so there is **no solution**.
- At $k=-3$: $0x=0$, so there are **infinitely many solutions**.
- For all $k\ne3,-3$, the equation has **exactly one solution**. It can be written as
  $x=\dfrac{2}{k-3}$.

</details>

### Problem 10

Create an equation of the form $A(k)x=B(k)$ such that one value of $k$ gives no solution,
another value gives infinitely many solutions, and all other values give exactly one
solution. State your equation and classify its solution structure.

<details>
<summary>Sample solution</summary>

One possible answer is

$$ (k-1)(k-2)x=k-1. $$

At $k=1$, it becomes $0x=0$, so there are **infinitely many solutions**. At $k=2$, it becomes
$0x=1$, so there is **no solution**. For every $k\ne1,2$, the coefficient of $x$ is nonzero,
so there is **exactly one solution**.

Other equations with the same three cases are also correct.

</details>
