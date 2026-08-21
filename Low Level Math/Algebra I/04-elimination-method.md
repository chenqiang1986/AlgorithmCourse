# Lesson 4: Systems of Linear Equations — Elimination Method

Substitution (Lesson 3) works cleanly when a variable already has a coefficient of $1$.
When every coefficient is something like $3$ or $4$, substitution creates messy fractions.
The **elimination method** (also called the addition method) sidesteps this by combining
the two equations directly so that one variable cancels out.

## 1. Core Idea: Matching Coefficients

If a variable has **opposite** coefficients in the two equations (like $+2y$ and $-2y$),
adding the equations makes that variable disappear. If it has **equal** coefficients (like
$+2y$ and $+2y$), subtracting does the same thing. When neither coefficient matches
naturally, multiply one or both equations by a constant first — this doesn't change either
equation's solution set, since multiplying both sides by the same nonzero number preserves
equality.

## 2. Core Template: The Elimination Method

1. Write both equations in standard form $Ax + By = C$.
2. Pick a variable to eliminate. Multiply one or both equations by constants so that
   variable's coefficients become opposites (or equal).
3. Add the equations (if coefficients are opposite) or subtract them (if coefficients are
   equal) to eliminate that variable.
4. Solve the resulting one-variable equation.
5. Back-substitute the value into either **original** equation to find the other variable.
6. Check both values in both original equations.

## 3. Reading Example: Elimination Without Scaling

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

## 4. Reading Example: Elimination With Scaling

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

## 5. Reading Example: Scaling Both Equations

$$
\begin{cases}
4x + 3y = 18 \\
3x - 2y = 5
\end{cases}
$$

This time no single multiplication fixes things — in Section 4 only the second equation
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

## 6. Class Practice 1: Elimination With Scaling

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

## 7. Common Mistakes

### 7.1 Scaling only part of an equation

When multiplying an equation by a constant, every term — both variable coefficients and
the constant on the right-hand side — must be multiplied. Forgetting the right-hand side
is the single most common elimination error.

### 7.2 Adding when you should subtract (or vice versa)

Adding two equations eliminates a variable only when its coefficients are opposites;
subtracting eliminates it only when they're equal. Mixing this up reintroduces the
variable instead of removing it. When in doubt, multiply one equation by $-1$ first and
always add — see Section 3's non-obvious detail.

## 8. Key Takeaways

- Elimination adds or subtracts scaled copies of the two equations so one variable
  cancels — it avoids the fractions substitution can produce.
- Scale an equation by multiplying **every** term, then add (opposite coefficients) or
  subtract (equal coefficients) to eliminate a variable.
- Substitution and elimination always agree on the answer — choose whichever avoids more
  fractions for a given system.
- Elimination can also make **both** variables vanish at once, which reveals whether a
  system has no solution or infinitely many — covered together with the geometric picture
  in [05-geometric-interpretation-and-solution-count.md](./05-geometric-interpretation-and-solution-count.md).

Next lesson: [05-geometric-interpretation-and-solution-count.md](./05-geometric-interpretation-and-solution-count.md)
covers the geometric meaning of a system's solutions and how to recognize the no-solution
and infinite-solution cases using either substitution or elimination.
