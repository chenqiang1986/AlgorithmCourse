# Lesson 6: Systems of Linear Equations — Solving for Unknown Coefficients
*Low Level Math / Algebra I*

Lesson 5 went from a system to its solution count: given the equations, tell whether
there's no solution, one solution, or infinitely many. This lesson runs that process in
reverse. A coefficient in the system is replaced by an unknown like $k$ (or two unknowns,
$k$ and $m$), and the *number of solutions* is given as a condition — find the missing
coefficient(s) that make it true. Sometimes, as several of the practice problems below
show, no coefficient can.

## 1. Reading Example: Solving for an Unknown Coefficient

So far $k$ has been the questions "how many solutions?" — but a coefficient can also be
the unknown, with the *number* of solutions given as a condition instead. The strategy
runs Lesson 5's table in reverse: force the two lines to have matching slopes first,
then use the intercepts to tell no solution from infinitely many.

**Finding $k$ for no solution:**

$$
\begin{cases}
kx + 10y = 6 \\
4x + 5y = 9
\end{cases}
$$

For the lines to be parallel, the coefficient ratios must match: $\dfrac{k}{4} =
\dfrac{10}{5} = 2 \implies k = 8$. Before declaring victory, check the constants: $\dfrac{6}{9} =
\dfrac{2}{3}$, which is **not** $2$. Slopes match, intercepts don't — the lines are
parallel but distinct, so $k = 8$ gives **no solution**.

**Finding $k$ for infinitely many solutions:**

$$
\begin{cases}
9x + 15y = 21 \\
6x + ky = 14
\end{cases}
$$

Here the $x$- and constant-coefficients are already proportional on their own:
$\dfrac{9}{6} = \dfrac{21}{14} = \dfrac32$. That's exactly the ratio infinitely many
solutions needs — so instead of just matching slopes, solve for the $k$ that makes the
$y$-coefficients match that *same* ratio: $\dfrac{15}{k} = \dfrac32 \implies k = 10$. At
$k = 10$, every coefficient ratio is $\tfrac32$, so the second equation is the first one
scaled by $\tfrac32$ — the same line, and **infinitely many solutions**.

**Non-obvious detail:** matching the slopes only tells you the lines are *parallel* — they
could still turn out identical. Always check the constant term afterward: if it fits the
same ratio as the coefficients, you've actually landed on infinitely many solutions, not
no solution. Sections 5 and 6 below show what happens when this check reveals that
**no** value of $k$ can produce the case the problem is asking for.

## 2. Reading Example: Two Unknown Coefficients

A system can hide **two** unknown coefficients instead of one. The strategy doesn't
change — infinitely many solutions still means all three coefficient ratios match — but
now two of the six coefficients are missing instead of one, so solving means anchoring the
common ratio from whatever pair of coefficients *is* fully known, then applying it twice.

**Both unknowns in the same equation:**

$$
\begin{cases}
kx + 3y = m \\
6x + 9y = 15
\end{cases}
$$

The $y$-coefficients are the only pair with no unknown in it, so they anchor the ratio:
$\dfrac{3}{9} = \dfrac13$. Apply that same ratio to the other two pairs to pin down each
unknown separately: $\dfrac{k}{6} = \dfrac13 \implies k = 2$, and $\dfrac{m}{15} = \dfrac13
\implies m = 5$. At $k = 2, m = 5$: the first equation $2x + 3y = 5$ is exactly the second
equation divided by $3$ — the same line, so the system has **infinitely many solutions**.

**Unknowns split across both equations:**

$$
\begin{cases}
kx + 8y = 20 \\
6x + my = 15
\end{cases}
$$

This time the only pair with no unknown is the constants: $\dfrac{20}{15} = \dfrac43$.
Anchor there, then solve each unknown from its own pair: $\dfrac{k}{6} = \dfrac43 \implies
k = 8$, and $\dfrac{8}{m} = \dfrac43 \implies m = 6$. Check: with $k = 8, m = 6$, the first
equation $8x + 8y = 20$ is the second equation $6x + 6y = 15$ scaled by $\dfrac43$ — same
line, **infinitely many solutions**.

**Non-obvious detail:** with two unknowns you need a pair of coefficients where *neither*
side is unknown before you can find the common ratio — pick whichever of the three pairs
(the $x$-coefficients, the $y$-coefficients, or the constants) is fully known, and use it
as the anchor. Once you have the ratio, each remaining unknown is solved the same way as
Section 1's single-unknown case, one at a time.

## 3. Class Practice 1: Find $k$ for No Solution

### Problem

Find the value of $k$ that makes this system have **no solution**:

$$
\begin{cases}
5x + ky = 4 \\
10x + 6y = -3
\end{cases}
$$

<details>
<summary>Solution</summary>

Match the $x$- and $y$-coefficient ratios so the lines are parallel:

$$
\frac{5}{10} = \frac{k}{6} \implies \frac12 = \frac{k}{6} \implies k = 3
$$

Check the constants at $k = 3$: $\dfrac{4}{-3} = -\dfrac43$, which is **not** $\dfrac12$.
Slopes match, intercepts don't, so the lines are parallel and distinct.

The answer is **$k = 3$**.

</details>

## 4. Class Practice 2: Find $k$ for Infinitely Many Solutions

### Problem

Find the value of $k$ that makes this system have **infinitely many solutions**:

$$
\begin{cases}
3x - 6y = 12 \\
kx - 8y = 16
\end{cases}
$$

<details>
<summary>Solution</summary>

The $y$-coefficients and constants are already proportional: $\dfrac{-6}{-8} =
\dfrac{12}{16} = \dfrac34$. Solve for the $k$ that makes the $x$-coefficients match that
same ratio:

$$
\frac{3}{k} = \frac34 \implies k = 4
$$

At $k = 4$, every coefficient ratio is $\tfrac34$ — the second equation is the first one
scaled by $\tfrac34$, so it's the same line.

The answer is **$k = 4$**.

</details>

## 5. Class Practice 3: When No Value of $k$ Gives Infinitely Many Solutions

### Problem

Determine whether any value of $k$ makes this system have **infinitely many solutions**.
If so, find it; if not, explain why no such $k$ exists.

$$
\begin{cases}
2x + ky = 7 \\
4x + 6y = 9
\end{cases}
$$

<details>
<summary>Solution</summary>

Infinitely many solutions requires **all three** coefficient ratios to match. The
$x$-coefficient and constant ratios don't involve $k$ at all, so check them first:

$$
\frac{2}{4} = \frac12 \qquad \qquad \frac{7}{9}
$$

These are already unequal ($\tfrac12 \ne \tfrac79$), and no choice of $k$ can change
either of them — $k$ only appears in the $y$-coefficient. Since two of the three ratios
are locked in disagreement before $k$ even enters the picture, no value of $k$ can make
all three match.

The answer is **no such value of $k$ exists**.

</details>

## 6. Class Practice 4: When No Value of $k$ Gives No Solution

### Problem

Determine whether any value of $k$ makes this system have **no solution**. If so, find
it; if not, explain why no such $k$ exists.

$$
\begin{cases}
3x + ky = 6 \\
9x + 12y = 18
\end{cases}
$$

<details>
<summary>Solution</summary>

The $x$-coefficient and constant ratios don't involve $k$, and they already match:
$\dfrac{3}{9} = \dfrac{6}{18} = \dfrac13$. No solution needs the $y$-coefficient ratio to
equal this **and** the constants to disagree — but the constants already agree, so
matching the $y$-ratio ($\tfrac{k}{12} = \tfrac13 \implies k = 4$) produces infinitely many
solutions, not no solution. For every other value of $k$, the $y$-ratio misses $\tfrac13$,
so the slopes differ and the system has exactly one solution instead. Neither case is "no
solution."

The answer is **no such value of $k$ exists** — this system is either infinitely many
solutions ($k = 4$) or exactly one solution (any other $k$), never zero.

</details>

## 7. Class Practice 5: Find $k$ and $m$, Unknowns in One Equation

### Problem

Find the values of $k$ and $m$ that make this system have **infinitely many solutions**:

$$
\begin{cases}
kx + 4y = m \\
9x + 6y = 21
\end{cases}
$$

<details>
<summary>Solution</summary>

The $y$-coefficients are the only pair with no unknown, so anchor the ratio there:
$\dfrac{4}{6} = \dfrac23$. Apply it to the other two pairs:

$$
\frac{k}{9} = \frac23 \implies k = 6 \qquad \qquad \frac{m}{21} = \frac23 \implies m = 14
$$

Check: at $k = 6, m = 14$, the first equation $6x + 4y = 14$ is the second equation
$9x + 6y = 21$ scaled by $\dfrac23$ — the same line.

The answer is **$k = 6$, $m = 14$**.

</details>

## 8. Class Practice 6: Find $k$ and $m$, Unknowns in Different Equations

### Problem

Find the values of $k$ and $m$ that make this system have **infinitely many solutions**:

$$
\begin{cases}
5x + ky = 12 \\
10x + 6y = m
\end{cases}
$$

<details>
<summary>Solution</summary>

The $x$-coefficients are the only pair with no unknown, so anchor the ratio there:
$\dfrac{5}{10} = \dfrac12$. Apply it to the other two pairs:

$$
\frac{k}{6} = \frac12 \implies k = 3 \qquad \qquad \frac{12}{m} = \frac12 \implies m = 24
$$

Check: at $k = 3, m = 24$, the second equation $10x + 6y = 24$ is the first equation
$5x + 3y = 12$ scaled by $2$ — the same line.

The answer is **$k = 3$, $m = 24$**.

</details>

## 9. Common Mistakes

### 9.1 Assuming a valid $k$ must exist

When a problem asks for the coefficient that gives no solution (or infinitely many),
it's tempting to assume some answer is out there waiting to be found. Sections 5 and 6
show that isn't guaranteed: whenever the ratios that *don't* involve the unknown already
agree or already disagree, that agreement is fixed no matter what $k$ turns out to be —
so check those $k$-free ratios first, before solving for $k$, to see whether the
requested case is even reachable.

### 9.2 Anchoring the ratio on a pair that still has an unknown in it

With two unknowns, the common ratio can only come from the one pair of coefficients where
**both** sides are known numbers — trying to anchor on a pair containing $k$ or $m$ leaves
you with one equation in two unknowns, which doesn't pin down either value. Scan all three
pairs (the $x$-coefficients, the $y$-coefficients, the constants) first, and anchor on
whichever one has no unknown in it.

## 10. Key Takeaways

- When a coefficient is unknown, match the ratios that force parallel slopes, then check
  the constant term to tell no solution from infinitely many — and check the ratios that
  don't involve the unknown *first*, since a fixed disagreement (or agreement) among them
  can rule out the requested case entirely, no matter what the unknown turns out to be.
- With two unknown coefficients, infinitely many solutions is the case to ask for: it
  pins down both unknowns at once by anchoring the shared ratio on whichever coefficient
  pair is fully known, then applying that same ratio to solve for each unknown in turn.
