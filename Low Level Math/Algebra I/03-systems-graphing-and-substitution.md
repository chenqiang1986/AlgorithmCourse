# Lesson 3: Systems of Linear Equations — Substitution

A **system of equations** is a set of two or more equations that must be satisfied at the
same time. This lesson covers two-variable linear systems: what a solution means
algebraically, and how to find one using the **substitution method**.

## 1. What Is a System of Two-Variable Linear Equations?

A system of two linear equations in two variables $x$ and $y$ looks like:

$$
\begin{cases}
a_1x + b_1y = c_1 \\
a_2x + b_2y = c_2
\end{cases}
$$

A **solution** to the system is an ordered pair $(x, y)$ that satisfies **both** equations
simultaneously — plugging it into either equation alone is not enough.

**Example.** Check that $(3, 1)$ solves the system below:

$$
\begin{cases}
2x + y = 7 \\
x - y = 2
\end{cases}
$$

$$2(3) + 1 = 7 \quad \checkmark \qquad \qquad 3 - 1 = 2 \quad \checkmark$$

Both equations hold, so $(3, 1)$ is a solution. The pair $(0, 7)$ satisfies the first
equation ($2(0)+7=7$) but not the second ($0 - 7 = -7 \ne 2$), so it is **not** a solution
to the system.

## 2. Core Template: The Substitution Method

1. Solve one equation for one variable in terms of the other. If some variable has a
   coefficient of $1$ or $-1$, pick that one — it avoids fractions. If no variable has such
   a coefficient, solve for any variable anyway; the expression will contain a fraction,
   which is fine (Section 4 works through an example of this).
2. Substitute that expression into the **other** equation. This leaves one equation in one
   variable.
3. Solve for the remaining variable.
4. Back-substitute the value into either original equation to find the other variable.
5. Check both values in **both** original equations.

## 3. Reading Example: Solving by Substitution

$$
\begin{cases}
y = 3x - 1 \\
2x + y = 9
\end{cases}
$$

The first equation is already solved for $y$, so substitute $3x - 1$ for $y$ in the second
equation:

$$
\begin{aligned}
2x + (3x - 1) &= 9 \\
5x - 1 &= 9 \\
5x &= 10 \\
x &= 2
\end{aligned}
$$

Back-substitute into $y = 3x - 1$: $y = 3(2) - 1 = 5$. The solution is $(2, 5)$.

**Check:** $y = 3(2) - 1 = 5$ ✓, and $2(2) + 5 = 9$ ✓.

**Non-obvious detail:** substitution is easiest when you substitute into the equation that
is *not* already solved for that variable, using the expression from the equation that
*is*. Doing it backwards (substituting an equation into itself) just reproduces $0 = 0$
and tells you nothing.

## 4. Reading Example: Rearranging Before You Can Substitute

Not every system hands you an equation already solved for a variable. When every
coefficient is something other than $1$ or $-1$, you first isolate a variable by dividing —
producing a fractional expression — and *then* substitute.

$$
\begin{cases}
2x + 3y = 1 \\
4x - y = 9
\end{cases}
$$

Neither equation is solved for a variable, and no coefficient is $\pm 1$ in the first
equation. Solve the first equation for $x$ by dividing both sides by $2$:

$$
2x + 3y = 1 \implies 2x = 1 - 3y \implies x = \frac{1 - 3y}{2}
$$

Substitute the whole expression $\dfrac{1 - 3y}{2}$ for $x$ in the second equation, then
clear the fraction by multiplying through by $2$:

$$
\begin{aligned}
4\left(\frac{1 - 3y}{2}\right) - y &= 9 \\
2(1 - 3y) - y &= 9 \\
2 - 6y - y &= 9 \\
2 - 7y &= 9 \\
-7y &= 7 \\
y &= -1
\end{aligned}
$$

Back-substitute into $x = \dfrac{1 - 3y}{2}$: $x = \dfrac{1 - 3(-1)}{2} = \dfrac{4}{2} = 2$.
The solution is $(2, -1)$.

**Check:** $2(2) + 3(-1) = 4 - 3 = 1$ ✓, and $4(2) - (-1) = 8 + 1 = 9$ ✓.

**Non-obvious detail:** when you multiply $4 \cdot \dfrac{1-3y}{2}$, simplify the fraction
first ($\tfrac{4}{2}=2$) rather than distributing $4$ across the numerator and dividing
later — it keeps the numbers small and avoids arithmetic slips.

## 5. Reading Example: Substitution Works With Either Variable

The template says "solve one equation for one variable" — it doesn't say *which* variable,
or *which* equation to solve first. Revisit the system from Section 4:

$$
\begin{cases}
2x + 3y = 1 \\
4x - y = 9
\end{cases}
$$

Section 4 solved the *first* equation for $x$, which produced a fraction ($x =
\tfrac{1-3y}{2}$) because no coefficient there is $\pm 1$, and arrived at $(2, -1)$. Here's
a different path to the same point.

**Solving for $y$ instead:** the *second* equation has a coefficient of $-1$ on $y$, so
solving it for $y$ avoids a fraction entirely:

$$
4x - y = 9 \implies -y = 9 - 4x \implies y = 4x - 9
$$

Substitute this into the first equation:

$$
\begin{aligned}
2x + 3(4x - 9) &= 1 \\
2x + 12x - 27 &= 1 \\
14x &= 28 \\
x &= 2
\end{aligned}
$$

Back-substitute into $y = 4x - 9$: $y = 4(2) - 9 = -1$. The solution is $(2, -1)$ —
matching Section 4.

**Check:** $2(2) + 3(-1) = 4 - 3 = 1$ ✓, and $4(2) - (-1) = 8 + 1 = 9$ ✓.

**Non-obvious detail:** both paths are algebraically equivalent, not just coincidentally
matching — a system has one fixed solution set, and substitution just walks toward it from
a different starting equation and variable. Section 4's choice (solve the first equation for
$x$) forced a fraction; this section's choice (solve the second equation for $y$, since its
coefficient is $-1$) avoided one. Scanning all the coefficients in a system before picking
where to start — not just defaulting to the first equation — is what keeps the arithmetic
light.

## 6. Class Practice 1: Solve by Substitution

### Problem

Solve the system for $(x, y)$:

$$
\begin{cases}
x = y + 4 \\
3x - 2y = 17
\end{cases}
$$

<details>
<summary>Solution</summary>

Substitute $x = y + 4$ into the second equation:

$$
\begin{aligned}
3(y + 4) - 2y &= 17 \\
3y + 12 - 2y &= 17 \\
y + 12 &= 17 \\
y &= 5
\end{aligned}
$$

Then $x = y + 4 = 9$. Check: $3(9) - 2(5) = 27 - 10 = 17$ ✓.

The answer is **$(9, 5)$**.

</details>

## 7. Class Practice 2: Rearrange, Then Substitute

### Problem

Solve the system for $(x, y)$:

$$
\begin{cases}
4x + 3y = 5 \\
2x - 4y = 8
\end{cases}
$$

<details>
<summary>Solution</summary>

Neither equation is solved for a variable. Solve the first for $x$:

$$
4x = 5 - 3y \implies x = \frac{5 - 3y}{4}
$$

Substitute into the second equation and clear the fraction by multiplying by $2$:

$$
\begin{aligned}
2\left(\frac{5 - 3y}{4}\right) - 4y &= 8 \\
\frac{5 - 3y}{2} - 4y &= 8 \\
5 - 3y - 8y &= 16 \\
5 - 11y &= 16 \\
-11y &= 11 \\
y &= -1
\end{aligned}
$$

Back-substitute: $x = \dfrac{5 - 3(-1)}{4} = \dfrac{8}{4} = 2$.

Check: $4(2) + 3(-1) = 8 - 3 = 5$ ✓, and $2(2) - 4(-1) = 4 + 4 = 8$ ✓.

The answer is **$(2, -1)$**.

</details>

## 8. Common Mistakes

### 8.1 Solving for only one variable

Finding $x$ and stopping is an incomplete answer — always back-substitute to report both
coordinates of the solution point.

### 8.2 Sign errors when substituting a negative expression

When substituting an expression like $y = 3x - 1$ into $2x + y = 9$, remember the entire
expression $(3x - 1)$ replaces $y$, including its sign — a common error is writing
$2x + 3x - 1 = 9$ correctly here, but dropping a sign when the substituted expression
itself starts with a negative term (e.g., substituting $y = -x + 4$).

### 8.3 Dropping the denominator when substituting a fraction

When the expression you substitute is a fraction, like $x = \dfrac{1-3y}{2}$, the entire
fraction — numerator and denominator together — replaces the variable. A common error is
substituting only the numerator ($1 - 3y$) and forgetting to divide, which silently
multiplies the whole equation by the denominator.

## 9. Key Takeaways

- Substitution: solve one equation for one variable, plug into the other equation, solve,
  then back-substitute. You may pick either variable — both choices lead to the same
  solution.
- If no coefficient is $1$ or $-1$, isolating a variable produces a fraction; substitute
  the whole fractional expression and clear the fraction before simplifying.
- A solution to a two-variable linear system is a point $(x, y)$ satisfying both
  equations. What that means geometrically, and how to tell whether a system has one
  solution, no solution, or infinitely many without fully solving it, is covered once
  you've also seen elimination — in
  [05-geometric-interpretation-and-solution-count.md](./05-geometric-interpretation-and-solution-count.md).

Next lesson: [04-elimination-method.md](./04-elimination-method.md) covers the elimination
method, which avoids fractions when no variable has a coefficient of $1$.
