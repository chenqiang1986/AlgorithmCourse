# Lesson 3: Two-Variable Linear Equations — Substitution and Elimination

A **system of equations** is a set of two or more equations that must be satisfied at the
same time. This lesson covers two-variable linear systems: what a solution means
algebraically, and two methods for finding one — the **substitution method** and the
**elimination method**. Substitution works cleanly when a variable already has a
coefficient of $1$; elimination sidesteps the fractions substitution can produce when no
coefficient is $\pm 1$. Both methods always agree on the answer, so which one you reach for
is a matter of which avoids more arithmetic for the system in front of you.

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

## 6. Core Idea: Matching Coefficients

Substitution works, but every system in Sections 4–5 required isolating a variable first.
When every coefficient is something like $3$ or $4$, that isolation creates messy
fractions. The **elimination method** (also called the addition method) sidesteps this by
combining the two equations directly so that one variable cancels out.

If a variable has **opposite** coefficients in the two equations (like $+2y$ and $-2y$),
adding the equations makes that variable disappear. If it has **equal** coefficients (like
$+2y$ and $+2y$), subtracting does the same thing. When neither coefficient matches
naturally, multiply one or both equations by a constant first — this doesn't change either
equation's solution set, since multiplying both sides by the same nonzero number preserves
equality.

## 7. Core Template: The Elimination Method

1. Write both equations in standard form $Ax + By = C$.
2. Pick a variable to eliminate. Multiply one or both equations by constants so that
   variable's coefficients become opposites (or equal).
3. Add the equations (if coefficients are opposite) or subtract them (if coefficients are
   equal) to eliminate that variable.
4. Solve the resulting one-variable equation.
5. Back-substitute the value into either **original** equation to find the other variable.
6. Check both values in both original equations.

## 8. Reading Example: Elimination Without Scaling

$$
\begin{cases}
2x + 3y = 13 \\
2x - y = 1
\end{cases}
$$

The $x$-coefficients are already equal ($2$ and $2$), so subtract the second equation from
the first to eliminate $x$:

$$
\begin{aligned}
(2x + 3y) - (2x - y) &= 13 - 1 \\
4y &= 12 \\
y &= 3
\end{aligned}
$$

Back-substitute into $2x - y = 1$: $2x - 3 = 1 \implies 2x = 4 \implies x = 2$. The
solution is $(2, 3)$.

**Check:** $2(2) + 3(3) = 4 + 9 = 13$ ✓, and $2(2) - 3 = 1$ ✓.

**Non-obvious detail:** subtracting $(2x - y)$ means distributing the minus sign over
*both* terms: $3y - (-y) = 3y + y = 4y$, not $3y - y$. Adding the equations after first
multiplying one of them by $-1$ avoids this sign trap entirely — many students prefer to
always add, never subtract, for exactly this reason.

## 9. Reading Example: Elimination With Scaling

$$
\begin{cases}
3x + 4y = 10 \\
5x + 2y = 12
\end{cases}
$$

Neither variable has matching or opposite coefficients yet. The $y$-coefficients are $4$
and $2$ — multiply the second equation by $-2$ so they become opposites:

$$-2(5x + 2y) = -2(12) \implies -10x - 4y = -24$$

Now add this to the first equation:

$$
\begin{aligned}
(3x + 4y) + (-10x - 4y) &= 10 + (-24) \\
-7x &= -14 \\
x &= 2
\end{aligned}
$$

Back-substitute into $5x + 2y = 12$: $5(2) + 2y = 12 \implies 2y = 2 \implies y = 1$. The
solution is $(2, 1)$.

**Check:** $3(2) + 4(1) = 10$ ✓, and $5(2) + 2(1) = 12$ ✓.

**Non-obvious detail:** scaling multiplies **every** term in the equation, including the
right-hand side — a common slip is scaling only the variable terms and forgetting the
constant on the right.

## 10. Reading Example: Scaling Both Equations

$$
\begin{cases}
4x + 3y = 18 \\
3x - 2y = 5
\end{cases}
$$

This time no single multiplication fixes things — in Section 9 only the second equation
needed scaling, but here **both** equations must be scaled before anything cancels.
The $x$-coefficients ($4$ and $3$) share no easy relationship, and neither do the
$y$-coefficients ($3$ and $-2$). Compare the two pairs: $3$ and $-2$ reach a common
multiple faster ($6$) than $4$ and $3$ do ($12$), so eliminate $y$.

A quick way to find matching multipliers without hunting for the LCM: multiply each
equation by the *other* equation's $y$-coefficient (dropping the sign for now).

$$
\begin{aligned}
2(4x + 3y) &= 2(18) &\implies 8x + 6y &= 36 \\
3(3x - 2y) &= 3(5) &\implies 9x - 6y &= 15
\end{aligned}
$$

The $y$-coefficients are now opposites ($+6$ and $-6$), so add:

$$
\begin{aligned}
(8x + 6y) + (9x - 6y) &= 36 + 15 \\
17x &= 51 \\
x &= 3
\end{aligned}
$$

Back-substitute into $4x + 3y = 18$: $4(3) + 3y = 18 \implies 3y = 6 \implies y = 2$. The
solution is $(3, 2)$.

**Check:** $4(3) + 3(2) = 12 + 6 = 18$ ✓, and $3(3) - 2(2) = 9 - 4 = 5$ ✓.

**Non-obvious detail:** cross-multiplying by the other equation's coefficient (here $2$
and $3$, from swapping the $y$-coefficients $3$ and $2$) always produces *a* common
multiple, so it always works — but it isn't always the *smallest* one. If the
coefficients had been $4$ and $6$ instead of $3$ and $2$, cross-multiplying would give
$24$, while the LCM is only $12$; either works, but the LCM keeps the numbers smaller.

## 11. Class Practice 1: Solve by Substitution

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

## 12. Class Practice 2: Rearrange, Then Substitute

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

## 13. Class Practice 3: Elimination With Scaling

### Problem

Solve the system for $(x, y)$:

$$
\begin{cases}
4x + 3y = -1 \\
3x - 2y = 12
\end{cases}
$$

<details>
<summary>Solution</summary>

Neither variable has matching or opposite coefficients, and the $y$-coefficients ($3$ and
$-2$) have a smaller common multiple than the $x$-coefficients, so eliminate $y$. Multiply
the first equation by $2$ and the second by $3$ so the $y$-coefficients become $+6$ and
$-6$:

$$
\begin{aligned}
2(4x + 3y) &= 2(-1) &\implies 8x + 6y &= -2 \\
3(3x - 2y) &= 3(12) &\implies 9x - 6y &= 36
\end{aligned}
$$

Add the two equations:

$$
\begin{aligned}
(8x + 6y) + (9x - 6y) &= -2 + 36 \\
17x &= 34 \\
x &= 2
\end{aligned}
$$

Back-substitute into $3x - 2y = 12$: $3(2) - 2y = 12 \implies -2y = 6 \implies y = -3$.

**Check:** $4(2) + 3(-3) = 8 - 9 = -1$ ✓, and $3(2) - 2(-3) = 6 + 6 = 12$ ✓.

The answer is **$(2, -3)$**.

</details>

## 14. Class Practice 4: A System With No Solution

### Problem

Solve the system for $(x, y)$, or show that it has no solution:

$$
\begin{cases}
2x + 3y = 6 \\
4x + 6y = 20
\end{cases}
$$

<details>
<summary>Solution</summary>

Eliminate $x$: multiply the first equation by $2$:

$$2(2x+3y) = 2(6) \implies 4x+6y = 12$$

Subtract this from the second equation:

$$(4x+6y) - (4x+6y) = 20 - 12 \implies 0 = 8$$

Both variables vanish, leaving a false statement.

The answer is **no solution**. (Lesson 5 explains what this means geometrically and how to
recognize it without fully solving.)

</details>

## 15. Class Practice 5: A System With Infinitely Many Solutions

### Problem

Solve the system for $(x, y)$, or show that it has infinitely many solutions:

$$
\begin{cases}
2x - y = 4 \\
-6x + 3y = -12
\end{cases}
$$

<details>
<summary>Solution</summary>

Eliminate $x$: multiply the first equation by $3$:

$$3(2x-y) = 3(4) \implies 6x-3y = 12$$

Add this to the second equation:

$$(6x-3y) + (-6x+3y) = 12 + (-12) \implies 0 = 0$$

Both variables vanish, leaving a true statement.

The answer is **infinitely many solutions**. (Lesson 5 explains what this means
geometrically and how to recognize it without fully solving.)

</details>

## 16. Common Mistakes

### 16.1 Solving for only one variable

Finding $x$ and stopping is an incomplete answer — always back-substitute to report both
coordinates of the solution point.

### 16.2 Sign errors when substituting a negative expression

When substituting an expression like $y = 3x - 1$ into $2x + y = 9$, remember the entire
expression $(3x - 1)$ replaces $y$, including its sign — a common error is writing
$2x + 3x - 1 = 9$ correctly here, but dropping a sign when the substituted expression
itself starts with a negative term (e.g., substituting $y = -x + 4$).

### 16.3 Dropping the denominator when substituting a fraction

When the expression you substitute is a fraction, like $x = \dfrac{1-3y}{2}$, the entire
fraction — numerator and denominator together — replaces the variable. A common error is
substituting only the numerator ($1 - 3y$) and forgetting to divide, which silently
multiplies the whole equation by the denominator.

### 16.4 Scaling only part of an equation

When multiplying an equation by a constant, every term — both variable coefficients and
the constant on the right-hand side — must be multiplied. Forgetting the right-hand side
is the single most common elimination error.

### 16.5 Adding when you should subtract (or vice versa)

Adding two equations eliminates a variable only when its coefficients are opposites;
subtracting eliminates it only when they're equal. Mixing this up reintroduces the
variable instead of removing it. When in doubt, multiply one equation by $-1$ first and
always add — see Section 8's non-obvious detail.

## 17. Key Takeaways

- Substitution: solve one equation for one variable, plug into the other equation, solve,
  then back-substitute. You may pick either variable — both choices lead to the same
  solution.
- If no coefficient is $1$ or $-1$, isolating a variable produces a fraction; substitute
  the whole fractional expression and clear the fraction before simplifying.
- Elimination adds or subtracts scaled copies of the two equations so one variable
  cancels — it avoids the fractions substitution can produce.
- Scale an equation by multiplying **every** term, then add (opposite coefficients) or
  subtract (equal coefficients) to eliminate a variable.
- Substitution and elimination always agree on the answer — choose whichever avoids more
  fractions for a given system. Elimination can also make **both** variables vanish at
  once, which reveals whether a system has no solution or infinitely many — covered
  together with the geometric picture in
  [05-geometric-interpretation-and-solution-count.md](./05-geometric-interpretation-and-solution-count.md).

Next lesson: [04-three-variable-linear-equations.md](./04-three-variable-linear-equations.md)
extends the elimination method to systems of three equations in three variables.
