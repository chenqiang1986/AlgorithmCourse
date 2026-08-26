# Lesson 8: Single-Variable Linear Equations

This lesson opens Unit 2 of the syllabus ([00-syllabus.md](./00-syllabus.md)), Weeks 7–8:
expressions and linear equations. The diagnostic test ([01-diagnostic-test.md](./01-diagnostic-test.md),
Problems 12–13) already checked one- and two-step equations, so this lesson reviews that
skill quickly, then builds it up to two genuinely new cases: equations that need the
distributive property and combining like terms before they're solvable, and equations with
the variable on **both** sides.

## 1. Quick Review: One- and Two-Step Equations

Solving an equation for $x$ means **undoing** whatever operations were done to $x$, in
reverse order, applying the same operation to both sides each time so the equation stays
balanced (whatever you do to one side, you must do to the other).

$$-5x = 35 \implies x = \frac{35}{-5} = -7 \qquad \text{(undo multiplication by dividing)}$$

$$\frac{x}{3} + 4 = 10 \implies \frac{x}{3} = 6 \implies x = 18 \qquad \text{(undo addition, then undo division)}$$

The rest of this lesson is the same "undo, keep both sides balanced" idea applied to
equations that need extra simplification first.

## 2. Distributive Property and Combining Like Terms

Before an equation can be solved by undoing operations, both sides need to be in their
simplest form. Two tools do that:

**Distributive property:** $a(b + c) = ab + ac$ — a factor multiplying a sum multiplies
every term inside.

$$3(x + 4) = 3x + 12 \qquad \qquad -2(x - 5) = -2x + 10$$

**Combining like terms:** terms with the exact same variable part can be added or subtracted
by adding their coefficients — this is the product-of-powers idea from
[Lesson 5](./05-exponent-rules.md#2-product-of-powers-am--an--amn) run in reverse, treating
$x + x + x$ as $3x$ the same way $a \times a \times a$ is $a^3$.

$$3x + 5x = 8x \qquad \qquad 7x - 2x + 4 = 5x + 4$$

### Reading Example: Distribute, Then Combine

Simplify $2(x + 3) + 4x$.

$$2(x + 3) + 4x = 2x + 6 + 4x = (2x + 4x) + 6 = 6x + 6$$

**Non-obvious detail:** distribute before combining, not the other way around — $2(x+3)$
cannot be combined with $4x$ while it's still in parentheses, since $x + 3$ is not a single
"like term" until the $2$ is distributed across it.

### Class Practice 1: Simplify, Then Solve

#### Problem

Solve $3(x + 2) - x = 16$.

<details>
<summary>Solution</summary>

Distribute the $3$, then combine like terms on the left:

$$3(x + 2) - x = 3x + 6 - x = 2x + 6$$

So the equation becomes $2x + 6 = 16$. Undo addition, then undo multiplication:

$$2x = 10 \implies x = 5$$

Check: $3(5 + 2) - 5 = 3(7) - 5 = 21 - 5 = 16$. $\checkmark$

The answer is **$x = 5$**.

</details>

## 3. Variables on Both Sides

Some equations have $x$ terms on both sides, like $5x + 3 = 2x + 12$. These can't be solved
by undoing operations on one side alone — first, move all the $x$ terms to one side by
adding or subtracting an $x$ term from **both** sides (the same balance rule as Section 1,
just applied to a variable term instead of a number), collapsing the equation to a one- or
two-step equation.

$$5x + 3 = 2x + 12$$

$$5x - 2x + 3 = 2x - 2x + 12 \qquad \text{(subtract $2x$ from both sides)}$$

$$3x + 3 = 12$$

$$3x = 9 \implies x = 3$$

**Which side to move the $x$ terms to is a free choice** — moving $5x$ to the right instead
($5x - 5x + 3 = 2x - 5x + 12$, giving $3 = -3x + 12$) leads to the same answer, $x = 3$. Pick
whichever side keeps the $x$ coefficient positive, since it avoids an extra sign to track.

### Reading Example: Distributing on Both Sides First

Solve $2(x + 5) = 3x - 4$.

Distribute the left side first — Section 2's tool applies before Section 3's, since neither
side is in simplest form yet:

$$2x + 10 = 3x - 4$$

Now move the $x$ terms — subtract $2x$ from both sides:

$$10 = x - 4$$

$$x = 14$$

**Non-obvious detail:** the order matters — distributing and combining like terms
(Section 2) always happens first, on each side separately, *before* moving terms across the
equal sign (Section 3). Moving terms across the equal sign too early, before a side is fully
simplified, makes it easy to move only part of an expression by mistake.

### Special Case: One Solution, No Solution, or Infinitely Many

Collecting the $x$ terms onto one side can also eliminate $x$ entirely, and what's left
decides the outcome:

$$4x + 1 = 4x + 5 \implies 1 = 5 \quad \text{(false for every $x$)} \implies \textbf{no solution}$$

$$4x + 1 = 4x + 1 \implies 1 = 1 \quad \text{(true for every $x$)} \implies \textbf{infinitely many solutions}$$

**Non-obvious detail:** both equations have identical $x$-coefficients on both sides ($4x$),
which is exactly what makes $x$ cancel out — the number left over then decides everything: a
false statement means no value of $x$ works, a true statement means every value of $x$ works.

### Class Practice 2: Variables on Both Sides

#### Problem

Solve $7x - 3 = 4x + 15$.

<details>
<summary>Solution</summary>

Subtract $4x$ from both sides to collect $x$ terms on the left (keeping the coefficient
positive):

$$7x - 4x - 3 = 4x - 4x + 15 \implies 3x - 3 = 15$$

Undo subtraction, then undo multiplication:

$$3x = 18 \implies x = 6$$

Check: $7(6) - 3 = 39$ and $4(6) + 15 = 39$. $\checkmark$

The answer is **$x = 6$**.

</details>

### Class Practice 3: Identifying the Solution Count

#### Problem

Without fully solving, determine whether $6x + 2(x - 3) = 8x + 5$ has one solution, no
solution, or infinitely many solutions. Then find the solution if there is exactly one.

<details>
<summary>Solution</summary>

Simplify the left side first (Section 2):

$$6x + 2(x - 3) = 6x + 2x - 6 = 8x - 6$$

The equation is now $8x - 6 = 8x + 5$. Subtract $8x$ from both sides:

$$-6 = 5$$

This is false for every $x$, so there is **no solution**.

</details>

## 4. Word Problems

Translating a word problem into an equation is mostly a matter of naming the unknown and
converting each phrase into its matching operation:

| Phrase | Operation |
|---|---|
| "sum of," "more than," "increased by" | addition |
| "difference," "less than," "decreased by" | subtraction |
| "times," "product of," "twice" | multiplication |
| "consecutive integers" | $n$, $n+1$, $n+2$, $\ldots$ |

### Reading Example: Consecutive Integers

Find three consecutive integers whose sum is $54$.

Let the first integer be $n$; the next two are $n+1$ and $n+2$ (each "consecutive" integer is
one more than the last):

$$n + (n + 1) + (n + 2) = 54$$

Combine like terms, then solve as a two-step equation:

$$3n + 3 = 54 \implies 3n = 51 \implies n = 17$$

The three integers are $17$, $18$, $19$.

**Non-obvious detail:** naming only the *first* unknown ($n$) and writing the rest in terms
of it ($n+1$, $n+2$) turns a three-unknown problem into a single-variable equation — the
same trick works for "consecutive even integers" ($n$, $n+2$, $n+4$) by stepping by $2$
instead of $1$.

### Class Practice 4: A "Both Sides" Word Problem

#### Problem

Ana has $x$ dollars. Ben has $3$ dollars more than twice what Ana has. Combined, they have
the same amount as $4$ times what Ana has, minus $9$ dollars. How much money does Ana have?

<details>
<summary>Solution</summary>

Translate each phrase. Ana has $x$. Ben has "$3$ more than twice Ana's amount":

$$\text{Ben} = 2x + 3$$

"Combined" is addition; the right side is "$4$ times Ana's amount, minus $9$":

$$x + (2x + 3) = 4x - 9$$

Combine like terms on the left, then move $x$ terms to one side (Section 3):

$$3x + 3 = 4x - 9$$

$$3 + 9 = 4x - 3x \implies 12 = x$$

Check: Ana has $12$, Ben has $2(12) + 3 = 27$, combined $= 39$; and $4(12) - 9 = 39$.
$\checkmark$

The answer is **Ana has \$12**.

</details>

## 5. Common Mistakes

### 5.1 Distributing to only the first term

$3(x + 4)$ is $3x + 12$, **not** $3x + 4$ — every term inside the parentheses gets
multiplied by the outside factor, the same distribution rule as
[Lesson 5, Common Mistake 6.3](./05-exponent-rules.md#63-forgetting-the-power-of-a-product-distributes-to-every-factor)
for exponents.

### 5.2 Forgetting to distribute a negative sign

$-2(x - 5)$ is $-2x + 10$, **not** $-2x - 10$ — the negative sign is part of the factor
being distributed, so it flips the sign of every term inside, including the one that was
already negative.

### 5.3 Moving a term without changing its sign

Moving $2x$ from the right side of $5x + 3 = 2x + 12$ means **subtracting** $2x$ from both
sides, which turns the $2x$ on the right into $0$ — it does not just "hop over" the equal
sign and flip sign on its own. Writing out the subtraction on both sides (Section 3) avoids
this error.

### 5.4 Confusing "no solution" with "$x = 0$"

$4x + 1 = 4x + 5$ simplifying to $1 = 5$ means **no value of $x$** makes the equation true —
it does not mean $x = 0$. $x = 0$ would be the answer only if solving had produced an
equation like $x = 0$, with the variable still present.

## 6. Key Takeaways

- Solving an equation means undoing operations on $x$ in reverse order, keeping both sides
  balanced at every step.
- **Distribute, then combine like terms**, on each side separately, before doing anything
  else — $a(b+c) = ab + ac$, and like terms combine by adding coefficients.
- **Variables on both sides:** add or subtract an $x$ term from both sides to collect $x$
  onto one side, turning the equation into a one- or two-step equation.
- If collecting $x$ terms eliminates $x$ entirely, the leftover statement decides the
  outcome: false means no solution, true means infinitely many solutions.
- Word problems translate phrase-by-phrase into an equation; for related unknowns (like
  consecutive integers), name only the first one and write the rest in terms of it.

Next lesson continues Unit 2: introducing systems of two linear equations and solving them
by graphing and substitution.
