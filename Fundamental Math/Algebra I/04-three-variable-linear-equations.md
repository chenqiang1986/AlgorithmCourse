# Lesson 4: Three-Variable Linear Equations — Elimination Method
*Fundamental Math / Algebra I*

Lesson 3 solved systems of two equations in two variables. This lesson extends the
**elimination method** to systems of three equations in three variables $x$, $y$, and $z$.
The core idea does not change — combine two equations so a variable cancels — but three
variables means that single trick is no longer enough by itself. This lesson walks through
the fully generic procedure: the one that works no matter how the numbers happen to line
up, not one that depends on getting lucky.

## 1. What Is a System of Three-Variable Linear Equations?

A system of three linear equations in three variables looks like:

$$
\begin{cases}
a_1x + b_1y + c_1z = d_1 \\
a_2x + b_2y + c_2z = d_2 \\
a_3x + b_3y + c_3z = d_3
\end{cases}
$$

A **solution** is an ordered triple $(x, y, z)$ that satisfies **all three** equations at
once.

**Example.** Check that $(2, -1, 3)$ solves the system below:

$$
\begin{cases}
2x + 3y - z = -2 \\
3x - 2y + 4z = 20 \\
4x + y + 2z = 13
\end{cases}
$$

$$
2(2)+3(-1)-3=-2\ \checkmark \qquad 3(2)-2(-1)+4(3)=20\ \checkmark \qquad 4(2)+(-1)+2(3)=13\ \checkmark
$$

All three equations hold, so $(2, -1, 3)$ is a solution. A triple that satisfies only two
of the three equations is not a solution to the system — exactly as a pair satisfying only
one equation wasn't a solution in Lesson 3.

## 2. Core Idea: Reducing Three Variables to Two

With two equations, one elimination step removes one variable and leaves one equation in
one variable — done. With three equations, one elimination step still only removes **one**
variable at a time. Eliminating $x$ from a single pair of equations leaves an equation in
$y$ and $z$ — that's one equation, but there are still two unknowns in it, so it can't be
solved on its own.

The fix: eliminate $x$ a **second time**, from a **different** pair of the three original
equations. That produces a second equation in $y$ and $z$. Two equations in two unknowns
is exactly the system Lesson 3 already knows how to solve. In general this takes two
genuinely separate elimination steps — there is no shortcut that clears two variables in
one combination except by special coincidence (Section 6 shows why that coincidence isn't
something to plan around).

## 3. Core Template: The Elimination Method for Three Variables

1. Label the three equations (1), (2), and (3).
2. Choose a variable to eliminate — say $x$.
3. Eliminate $x$ from one pair, e.g. (1) and (2), using Lesson 3's elimination method.
   Call the result (4): an equation in $y$ and $z$ only.
4. Eliminate $x$ **again**, from a *different* pair — e.g. (1) and (3), or (2) and (3) —
   independently of Step 3, using Lesson 3's method a second time. Call the result (5):
   another equation in $y$ and $z$ only.
5. (4) and (5) form a two-variable system in $y$ and $z$. Solve it with Lesson 3's
   elimination (or substitution) method.
6. Back-substitute the values of $y$ and $z$ into any **one** of the three original
   equations to find $x$.
7. Check all three values in all three **original** equations.

## 4. Reading Example: Eliminating $x$ From Two Different Pairs

$$
\begin{cases}
2x + 3y - z = -2 & (1) \\
3x - 2y + 4z = 20 & (2) \\
4x + y + 2z = 13 & (3)
\end{cases}
$$

**Eliminate $x$ from (1) and (2).** The $x$-coefficients are $2$ and $3$; their LCM is $6$.
Multiply (1) by $3$ and (2) by $2$:

$$
\begin{aligned}
3(2x+3y-z) &= 3(-2) &\implies 6x+9y-3z &= -6 \\
2(3x-2y+4z) &= 2(20) &\implies 6x-4y+8z &= 40
\end{aligned}
$$

Subtract to cancel $x$:

$$
(6x+9y-3z) - (6x-4y+8z) = -6 - 40 \implies 13y - 11z = -46 \qquad (4)
$$

**Eliminate $x$ from (1) and (3) — a different pair.** The $x$-coefficients here are $2$
and $4$, so only (1) needs scaling. Multiply (1) by $2$:

$$
2(2x+3y-z) = 2(-2) \implies 4x+6y-2z = -4
$$

Subtract (3):

$$
(4x+6y-2z) - (4x+y+2z) = -4 - 13 \implies 5y - 4z = -17 \qquad (5)
$$

**Solve the resulting two-variable system**, (4) and (5):

$$
\begin{cases}
13y - 11z = -46 \\
5y - 4z = -17
\end{cases}
$$

The $y$-coefficients are $13$ and $5$; multiply (4) by $5$ and (5) by $13$:

$$
\begin{aligned}
5(13y-11z) &= 5(-46) &\implies 65y-55z &= -230 \\
13(5y-4z) &= 13(-17) &\implies 65y-52z &= -221
\end{aligned}
$$

Subtract:

$$
(65y-55z)-(65y-52z) = -230-(-221) \implies -3z = -9 \implies z = 3
$$

Back-substitute into (5): $5y - 4(3) = -17 \implies 5y = -5 \implies y = -1$.

Back-substitute $y = -1, z = 3$ into original equation (1): $2x + 3(-1) - 3 = -2
\implies 2x - 6 = -2 \implies x = 2$. The solution is $(2, -1, 3)$.

**Check:** (2) gives $3(2)-2(-1)+4(3) = 6+2+12 = 20$ ✓, and (3) gives
$4(2)+(-1)+2(3) = 8-1+6 = 13$ ✓.

**Non-obvious detail:** the multipliers used to eliminate $x$ from (1)&(2) ($3$ and $2$)
have no relationship to the multipliers used to eliminate $x$ from (1)&(3) (just a single
$2$). Each pairwise elimination is worked out on its own — scan *that* pair's coefficients
the same way Lesson 3 scans a two-equation system — rather than trying to reuse a
multiplier from the first elimination.

## 5. Reading Example: Any Two Pairs Work

Section 4 eliminated $x$ using pairs (1)&(2) and (1)&(3). Equation (1) doesn't have to be
part of both eliminations — pairs (2)&(3) work just as well. Reusing the same system:

$$
\begin{cases}
2x + 3y - z = -2 & (1) \\
3x - 2y + 4z = 20 & (2) \\
4x + y + 2z = 13 & (3)
\end{cases}
$$

**Eliminate $x$ from (2) and (3).** The $x$-coefficients are $3$ and $4$; their LCM is
$12$. Multiply (2) by $4$ and (3) by $3$:

$$
\begin{aligned}
4(3x-2y+4z) &= 4(20) &\implies 12x-8y+16z &= 80 \\
3(4x+y+2z) &= 3(13) &\implies 12x+3y+6z &= 39
\end{aligned}
$$

Subtract:

$$
(12x-8y+16z)-(12x+3y+6z) = 80-39 \implies -11y+10z = 41 \qquad (6)
$$

Check (6) against the known solution $y=-1, z=3$: $-11(-1)+10(3) = 11+30 = 41$ ✓. Equation
(6) is a valid $y$-$z$ equation, consistent with (4) and (5) from Section 4, even though it
came from a completely different pair of original equations.

**Non-obvious detail:** whichever two pairs you choose to eliminate $x$ from, the resulting
$y$-$z$ equations are all consistent with the same underlying solution — pairing (1)&(2)
and (1)&(3), or (1)&(2) and (2)&(3), or (1)&(3) and (2)&(3), all lead to the same $(x,y,z)$.
There's no "correct" pair to pick; pick whichever pair has coefficients that are easiest to
scale.

## 6. Why "One Step Removes Two Variables" Doesn't Generalize

Occasionally a system is built so that adding two equations cancels **two** variables at
once, letting you solve for the third variable immediately:

$$
\begin{cases}
x + 2y + 3z = 14 & (1) \\
x - 2y - 3z = -2 & (2)
\end{cases}
$$

Adding (1) and (2):

$$
(x+2y+3z) + (x-2y-3z) = 14+(-2) \implies 2x = 12 \implies x = 6
$$

Both $y$ and $z$ vanished in a single step. This isn't a new technique — it happens only
because equation (2)'s $y$-term and $z$-term are the *exact negatives* of equation (1)'s
$y$-term and $z$-term ($-2y$ is the negative of $2y$, and $-3z$ is the negative of $3z$,
simultaneously). That relationship is a special property of these two equations, not
something a general three-variable system has. Section 4's system had no such
relationship between any pair of its equations, which is why it genuinely needed **two**
separate eliminations of $x$ to get down to a $y$-$z$ system.

Don't search for this shortcut when solving a new system — checking whether it applies
usually takes as long as just running the generic method from Section 3, and most systems
don't have it. Budget for two independent eliminations of your chosen variable every time,
and treat a one-step double-cancellation as a pleasant surprise, not the expected case.

## 7. Class Practice 1: Elimination With Three Variables

### Problem

Solve the system for $(x, y, z)$:

$$
\begin{cases}
3x + 2y - z = 4 \\
2x - 3y + 2z = 14 \\
5x + y + 3z = 16
\end{cases}
$$

<details>
<summary>Solution</summary>

Label the equations (1), (2), (3). Eliminate $x$ from (1) and (2): the $x$-coefficients
are $3$ and $2$, LCM $6$. Multiply (1) by $2$ and (2) by $3$:

$$
\begin{aligned}
2(3x+2y-z) &= 2(4) &\implies 6x+4y-2z &= 8 \\
3(2x-3y+2z) &= 3(14) &\implies 6x-9y+6z &= 42
\end{aligned}
$$

Subtract: $(6x+4y-2z)-(6x-9y+6z) = 8-42 \implies 13y - 8z = -34 \quad (4)$

Eliminate $x$ from (1) and (3) — a different pair. The $x$-coefficients are $3$ and $5$,
LCM $15$. Multiply (1) by $5$ and (3) by $3$:

$$
\begin{aligned}
5(3x+2y-z) &= 5(4) &\implies 15x+10y-5z &= 20 \\
3(5x+y+3z) &= 3(16) &\implies 15x+3y+9z &= 48
\end{aligned}
$$

Subtract: $(15x+10y-5z)-(15x+3y+9z) = 20-48 \implies 7y - 14z = -28$, which simplifies
(dividing by $7$) to $y - 2z = -4 \quad (5)$

Solve (4) and (5). Substitute $y = 2z - 4$ from (5) into (4):

$$
13(2z-4) - 8z = -34 \implies 26z - 52 - 8z = -34 \implies 18z = 18 \implies z = 1
$$

Then $y = 2(1) - 4 = -2$. Back-substitute into (1): $3x + 2(-2) - 1 = 4 \implies
3x - 5 = 4 \implies x = 3$.

Check (2): $2(3)-3(-2)+2(1) = 6+6+2 = 14$ ✓. Check (3): $5(3)+(-2)+3(1) = 15-2+3 = 16$ ✓.

The answer is **$(3, -2, 1)$**.

</details>

## 8. Class Practice 2 (Word Problem): Three Unknowns

### Problem

The sum of three numbers is $12$. The first number minus the second, plus twice the
third, is $11$. Twice the first number, minus the second, plus the third, is $10$. Find
the three numbers.

<details>
<summary>Solution</summary>

Let $x$, $y$, $z$ be the first, second, and third numbers:

$$
\begin{cases}
x + y + z = 12 & (1) \\
x - y + 2z = 11 & (2) \\
2x - y + z = 10 & (3)
\end{cases}
$$

Eliminate $x$ from (1) and (2): the $x$-coefficients already match ($1$ and $1$), so
subtract (B) from (A):

$$(x+y+z) - (x-y+2z) = 12 - 11 \implies 2y - z = 1 \quad (4)$$

Eliminate $x$ from (1) and (3) — a different pair, and a different technique, since the
$x$-coefficients ($1$ and $2$) don't already match. Multiply (1) by $2$:

$$2(x+y+z) = 2(12) \implies 2x+2y+2z = 24$$

Subtract (3): $(2x+2y+2z) - (2x-y+z) = 24 - 10 \implies 3y + z = 14 \quad (5)$

Solve (4) and (5) by adding — the $z$-coefficients are already opposite:

$$(2y-z) + (3y+z) = 1 + 14 \implies 5y = 15 \implies y = 3$$

From (4): $2(3) - z = 1 \implies z = 5$. From (1): $x + 3 + 5 = 12 \implies x = 4$.

Check (2): $4 - 3 + 2(5) = 4-3+10 = 11$ ✓. Check (3): $2(4) - 3 + 5 = 8-3+5 = 10$ ✓.

The three numbers are **$4$, $3$, and $5$**.

</details>

## 9. Class Practice 3: Elimination With Different Multipliers Each Time

### Problem

Solve the system for $(x, y, z)$:

$$
\begin{cases}
4x + 3y - 2z = 4 \\
2x - 5y + 3z = -16 \\
3x + 4y + z = 15
\end{cases}
$$

<details>
<summary>Solution</summary>

Label the equations (1), (2), (3). Eliminate $x$ from (1) and (2): the $x$-coefficients
are $4$ and $2$, so only (2) needs scaling. Multiply (2) by $2$:

$$
2(2x-5y+3z) = 2(-16) \implies 4x-10y+6z = -32
$$

Subtract from (1): $(4x+3y-2z)-(4x-10y+6z) = 4-(-32) \implies 13y - 8z = 36 \quad (4)$

Eliminate $x$ from (1) and (3) — a different pair. The $x$-coefficients are $4$ and $3$,
LCM $12$, so this time **both** equations need scaling. Multiply (1) by $3$ and (3) by
$4$:

$$
\begin{aligned}
3(4x+3y-2z) &= 3(4) &\implies 12x+9y-6z &= 12 \\
4(3x+4y+z) &= 4(15) &\implies 12x+16y+4z &= 60
\end{aligned}
$$

Subtract: $(12x+9y-6z)-(12x+16y+4z) = 12-60 \implies -7y-10z = -48$, i.e.
$7y + 10z = 48 \quad (5)$

Solve (4) and (5). The $y$-coefficients are $13$ and $7$; multiply (4) by $10$ and (5) by
$8$ so the $z$-coefficients become opposites ($-80$ and $80$):

$$
\begin{aligned}
10(13y-8z) &= 10(36) &\implies 130y-80z &= 360 \\
8(7y+10z) &= 8(48) &\implies 56y+80z &= 384
\end{aligned}
$$

Add: $(130y-80z)+(56y+80z) = 360+384 \implies 186y = 744 \implies y = 4$.

From (5): $7(4) + 10z = 48 \implies 10z = 20 \implies z = 2$. Back-substitute into (1):
$4x + 3(4) - 2(2) = 4 \implies 4x + 8 = 4 \implies x = -1$.

Check (2): $2(-1)-5(4)+3(2) = -2-20+6 = -16$ ✓. Check (3): $3(-1)+4(4)+2 = -3+16+2 = 15$ ✓.

The answer is **$(-1, 4, 2)$**.

</details>

## 10. Class Practice 4 (Word Problem): The Angles of a Triangle

### Problem

The three angles of a triangle sum to $180°$. Twice the first angle minus the second angle
plus the third angle is $140°$. The first angle plus twice the second angle minus the
third angle is $160°$. Find all three angles.

<details>
<summary>Solution</summary>

Let $A$, $B$, $C$ be the first, second, and third angles:

$$
\begin{cases}
A + B + C = 180 & (1) \\
2A - B + C = 140 & (2) \\
A + 2B - C = 160 & (3)
\end{cases}
$$

Eliminate $A$ from (1) and (2): the $A$-coefficients are $1$ and $2$, so multiply (1) by
$2$:

$$
2(A+B+C) = 2(180) \implies 2A+2B+2C = 360
$$

Subtract (2): $(2A+2B+2C)-(2A-B+C) = 360-140 \implies 3B+C = 220 \quad (4)$

Eliminate $A$ from (1) and (3) — a different pair, and this time no scaling is needed at
all, since the $A$-coefficients already match ($1$ and $1$). Subtract (3) from (1):

$$(A+B+C)-(A+2B-C) = 180-160 \implies -B+2C = 20 \quad (5)$$

Solve (4) and (5). From (5): $B = 2C - 20$. Substitute into (4):

$$
3(2C-20) + C = 220 \implies 6C - 60 + C = 220 \implies 7C = 280 \implies C = 40
$$

Then $B = 2(40) - 20 = 60$. Back-substitute into (1): $A + 60 + 40 = 180 \implies A = 80$.

Check (2): $2(80)-60+40 = 160-60+40 = 140$ ✓. Check (3): $80+2(60)-40 = 80+120-40 = 160$ ✓.

The three angles are **$80°$, $60°$, and $40°$**.

</details>

## 11. Class Practice 5: No Solution, Even Though No Two Equations Conflict

### Problem

Solve the system for $(x, y, z)$, or show that it has no solution:

$$
\begin{cases}
x + 2y + 3z = 6 \\
2x + y - z = 3 \\
3x + 3y + 2z = 10
\end{cases}
$$

<details>
<summary>Solution</summary>

Label the equations (1), (2), (3). Unlike the two-variable no-solution case (Lesson 3),
none of these three equations are parallel planes — check any pair, and the coefficients
aren't proportional to each other. So no single pair of equations looks broken; each pair
alone shares a whole line of common solutions. The trouble only shows up once all three are
combined.

Eliminate $x$ from (1) and (2): coefficients $1$ and $2$, so multiply (1) by $2$:

$$2(x+2y+3z) = 2(6) \implies 2x+4y+6z = 12$$

Subtract (2):

$$(2x+4y+6z) - (2x+y-z) = 12-3 \implies 3y+7z = 9 \quad (4)$$

Eliminate $x$ from (1) and (3) — a different pair. Coefficients $1$ and $3$, so multiply
(1) by $3$:

$$3(x+2y+3z) = 3(6) \implies 3x+6y+9z = 18$$

Subtract (3):

$$(3x+6y+9z) - (3x+3y+2z) = 18-10 \implies 3y+7z = 8 \quad (5)$$

(4) and (5) have the **exact same left-hand side** but different right-hand sides.
Subtracting them:

$$(3y+7z) - (3y+7z) = 9 - 8 \implies 0 = 1$$

A false statement. The answer is **no solution** — even though (1)&(2), (1)&(3), and
(2)&(3) each individually describe two planes crossing in a whole line of shared points.
Only combining all three constraints at once exposes the contradiction; inspecting any two
equations by themselves gives no warning that something is wrong.

</details>

## 12. Class Practice 6: Infinitely Many Solutions, Even Though No Two Equations Match

### Problem

Solve the system for $(x, y, z)$, or show that it has infinitely many solutions:

$$
\begin{cases}
x + 2y + 3z = 6 \\
2x + y - z = 3 \\
3x + 3y + 2z = 9
\end{cases}
$$

<details>
<summary>Solution</summary>

This is the same system as Class Practice 5, with only the constant in equation (3)
changed from $10$ to $9$ — and, as before, no two of the three equations are proportional,
so no pair looks unusual on its own. Label the equations (1), (2), (3) and run the same
elimination.

Eliminate $x$ from (1) and (2), exactly as in Class Practice 5:

$$3y+7z = 9 \quad (4)$$

Eliminate $x$ from (1) and (3):

$$3(x+2y+3z) = 3(6) \implies 3x+6y+9z = 18$$

Subtract (3):

$$(3x+6y+9z) - (3x+3y+2z) = 18-9 \implies 3y+7z = 9 \quad (5)$$

This time (4) and (5) are the **exact same equation**. Equation (3) turned out to be
redundant — it's exactly equation (1) plus equation (2), adding no new constraint beyond
what (1) and (2) already say. One equation in two unknowns, $3y+7z=9$, has infinitely many
solutions: pick any $z$, then $y = \dfrac{9-7z}{3}$, then back-substitute into (1) for $x$.

The answer is **infinitely many solutions**, forming a line in $(x,y,z)$-space — even
though no two of the three planes are parallel or identical by themselves. Only the
specific combination of all three reveals that the third equation was never independent.

</details>

## 13. Common Mistakes

### 13.1 Reusing a derived equation instead of a different original pair

After eliminating $x$ from (1)&(2) to get equation (4), it's tempting to try to "eliminate
$x$ again" from (4) and (2) — but (4) no longer contains $x$, so there's nothing left to
eliminate there. The second elimination must go back to two of the three **original**
equations (a different pair than the first), not reuse a result from the first step.

### 13.2 Assuming a one-step shortcut always exists

Hoping that adding two equations will conveniently cancel two variables at once (Section 6)
usually wastes time checking for a coincidence that isn't there. Default to the two-step
generic method from Section 3 unless the coincidence is already obvious from the
coefficients.

### 13.3 Forgetting to check all three original equations

Back-substituting $y$ and $z$ into just one original equation to find $x$ is required, but
not sufficient to confirm the whole solution — an arithmetic slip earlier in the
elimination can still produce a triple that satisfies one original equation by chance.
Always verify against all three.

## 14. Key Takeaways

- A three-variable system reduces to a two-variable system by eliminating one variable
  **twice**, from two different pairs of the original three equations — each elimination
  is worked out independently, the way Lesson 3 handles any two-equation system.
- Any two of the three possible pairs work for the first round of eliminations; when the
  system has a solution, the resulting $y$-$z$ equations from different pairs are always
  consistent with each other, no matter which pairs you picked.
- A single combination that cancels two variables at once can happen, but only when one
  equation's non-eliminated terms are already exact negatives (or multiples) of another's —
  a special relationship, not something to plan around. The reliable method always budgets
  for two separate eliminations.
- Checking equations two at a time never rules out no solution or infinitely many
  solutions — any two non-parallel planes always share a line of points, even when all
  three together share nothing (Class Practice 5) or share that entire line (Class
  Practice 6). Only running the full elimination on all three equations reveals which case
  you're in; this is genuinely more subtle than the two-variable case, where checking the
  two equations directly is enough.
- The same idea extends to four or more variables: eliminate one variable from enough
  different pairs to strip it out of every remaining equation, then repeat on the smaller
  system.

Next lesson: [05-geometric-interpretation-and-solution-count.md](./05-geometric-interpretation-and-solution-count.md)
returns to two-variable systems to explore what a solution means geometrically, and how to
classify the no-solution and infinite-solution cases.
