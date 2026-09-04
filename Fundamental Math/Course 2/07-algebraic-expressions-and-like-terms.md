# Lesson 7: Algebraic Expressions — Terms, Like Terms, and the Distributive Property
*Fundamental Math / Course 2*

Lessons 3–6 worked entirely with numbers. This lesson introduces the **variable** — a letter
standing in for an unknown or changing number — and the vocabulary needed to read and simplify
an **algebraic expression**: terms, coefficients, and like terms. It ends with the
**distributive property**, the tool that lets an expression like $3(x + 4)$ be rewritten
without parentheses so its terms can be combined.

## 1. Vocabulary: Variables, Terms, and Coefficients

A **variable** is a letter (commonly $x$, $y$, or $n$) that stands for a number that isn't
fixed yet — its value can change or is unknown.

An **algebraic expression** is built from numbers, variables, and operations, with no equals
sign — for example $3x + 5$ or $7 - 2n$.

A **term** is one piece of an expression, separated from the others by $+$ or $-$. The
expression $3x + 5$ has two terms: $3x$ and $5$.

- A term with a variable, like $3x$, has a **coefficient** — the number multiplied by the
  variable. If no number is written in front of a variable, the coefficient is $1$ (so $x$
  means $1x$); if only a minus sign is written, the coefficient is $-1$ (so $-x$ means $-1x$).
- A term with no variable, like $5$, is called a **constant term**.

$$\underbrace{3x}_{\text{coefficient }3,\text{ variable }x} \;+\; \underbrace{5}_{\text{constant term}}$$

This lesson works only with **linear terms** — a variable raised to the first power (no
$x^2$, $x^3$, etc.) — since that's what's needed to build and solve the linear equations in
[Lesson 8](./08-one-variable-linear-equations.md).

## 2. Core Template: Evaluating an Expression by Substitution

**Evaluating** an expression means replacing the variable with a specific number and computing
the result. Substitute the given value everywhere the variable appears, then follow the order
of operations from earlier lessons.

$$\text{Evaluate } 3x + 5 \text{ at } x = 4: \qquad 3(4) + 5 = 12 + 5 = 17$$

## 3. Reading Example: Evaluating With a Negative Value

Evaluate $2x - 7$ at $x = -3$.

Substitute $-3$ for $x$, keeping it in parentheses so the multiplication sign isn't lost:

$$2(-3) - 7 = -6 - 7 = -13$$

**Non-obvious detail:** wrapping the substituted value in parentheses, $2(-3)$, avoids reading
it as $2 - 3$. This matters most when the value being substituted is negative.

## 4. Class Practice 1: Evaluating an Expression

### Problem

Evaluate $4x - 6$ at $x = 5$.

<details>
<summary>Solution</summary>

$$4(5) - 6 = 20 - 6 = 14$$

The answer is **$14$**.

</details>

## 5. Class Practice 2: Evaluating With a Negative Value

### Problem

Evaluate $-3x + 2$ at $x = -4$.

<details>
<summary>Solution</summary>

$$-3(-4) + 2 = 12 + 2 = 14$$

The answer is **$14$**.

</details>

## 6. Like Terms

Two terms are **like terms** if they have the exact same variable (or are both constants).
Only the coefficient may differ — the variable part must match exactly.

- $3x$ and $7x$ are like terms (both have variable $x$).
- $5$ and $-2$ are like terms (both are constants).
- $3x$ and $5$ are **not** like terms — one has a variable, the other doesn't.
- $3x$ and $3y$ are **not** like terms — the variables are different letters.

![Two bordered panels side by side. The left panel, titled "Before: Mixed Order," shows the expression 3x + 5 + x + 3 written above four colored tiles in that order: a blue tile labeled 3x, an orange tile labeled 5, a smaller blue tile labeled x, and an orange tile labeled 3, with a caption "scattered — not yet grouped" and a legend marking blue tiles as x-terms and orange tiles as constant terms. The right panel, titled "After: Grouped by Type," shows the same four tiles rearranged so both blue tiles sit together on the left with a bracket underneath labeled "3x + x = 4x," and both orange tiles sit together on the right with a bracket labeled "5 + 3 = 8," with the final result "Simplified: 4x + 8" written below. A caption under both panels reads: like terms have the exact same variable part — combine their coefficients; unlike terms stay separate.](./images/like-terms-grouping.svg)

## 7. Core Template: Combining Like Terms

To combine like terms, add or subtract their coefficients and keep the shared variable part
unchanged — exactly like grouping the tiles above.

$$3x + x = 3x + 1x = (3+1)x = 4x$$

Constants combine the same way, using the integer addition rules from
[Lesson 3](./03-negative-integers-addition-subtraction.md):

$$5 + 3 = 8$$

So $3x + 5 + x + 3$ simplifies to $4x + 8$ — as many terms as there are *distinct* variable
parts, not as many terms as the expression started with.

## 8. Reading Example: Combining Like Terms With Negative Coefficients

Simplify $5x - 8 - 2x + 3$.

Group the $x$-terms and the constants separately (the sign in front of each term travels with
it):

$$\underbrace{5x - 2x}_{x\text{-terms}} + \underbrace{(-8 + 3)}_{\text{constants}}$$

Combine each group using integer addition/subtraction:

$$5x - 2x = 3x \qquad \qquad -8 + 3 = -5$$

$$5x - 8 - 2x + 3 = 3x - 5$$

**Non-obvious detail:** $-8$ keeps its negative sign when it's regrouped — the sign belongs to
the term immediately to its right, not to the operation before it. Rewriting subtraction as
"add a negative" (the same trick from [Lesson 3](./03-negative-integers-addition-subtraction.md))
makes this easy to track.

## 9. Class Practice 3: Identifying Like Terms

### Problem

Which of the following terms are like terms with $6x$? $\quad 2x, \quad 6y, \quad -x, \quad 9$

<details>
<summary>Solution</summary>

A term is a like term with $6x$ only if its variable part is exactly $x$. Checking each:

- $2x$ — variable part $x$. **Like term.**
- $6y$ — variable part $y$, not $x$. Not a like term.
- $-x$ — variable part $x$ (coefficient $-1$). **Like term.**
- $9$ — no variable at all. Not a like term.

The answer is **$2x$ and $-x$**.

</details>

## 10. Class Practice 4: Combining Two Like Terms

### Problem

Simplify: $7x + 4x$

<details>
<summary>Solution</summary>

$$7x + 4x = (7+4)x = 11x$$

The answer is **$11x$**.

</details>

## 11. Class Practice 5: Combining Like Terms With Constants

### Problem

Simplify: $6x + 9 - 2x + 4$

<details>
<summary>Solution</summary>

Group the $x$-terms and constants separately:

$$\underbrace{6x - 2x}_{x\text{-terms}} + \underbrace{9 + 4}_{\text{constants}} = 4x + 13$$

The answer is **$4x + 13$**.

</details>

## 12. Class Practice 6: Combining Like Terms With Negative Coefficients

### Problem

Simplify: $-5x + 3 - x - 8$

<details>
<summary>Solution</summary>

Group the $x$-terms and constants separately (remember $-x$ means $-1x$):

$$\underbrace{-5x - x}_{x\text{-terms}} + \underbrace{3 - 8}_{\text{constants}} = -6x - 5$$

The answer is **$-6x - 5$**.

</details>

## 13. The Distributive Property

Some expressions have a term multiplied by a group in parentheses, like $3(x + 4)$. The
**distributive property** says multiplying a sum by a number is the same as multiplying each
term inside separately, then adding:

$$a(b + c) = ab + ac \qquad \qquad a(b - c) = ab - ac$$

$$3(x + 4) = 3(x) + 3(4) = 3x + 12$$

This works because $x + 4$ added $3$ times is the same as $3x$ (three $x$'s) plus $12$ (three
$4$'s) — multiplication is repeated addition, applied to each part of the sum.

## 14. Reading Example: Distributing a Negative Sign

Simplify $-2(x - 5) + 7$.

Distribute $-2$ to both terms inside the parentheses. Subtracting $5$ is the same as adding
$-5$, so both signs must be tracked carefully:

$$-2(x - 5) = -2(x) + (-2)(-5) = -2x + 10$$

Now combine with the remaining term:

$$-2x + 10 + 7 = -2x + 17$$

**Non-obvious detail:** distributing a negative number flips the sign of *every* term inside
the parentheses, not just the first one — $(-2)(-5) = +10$ is a common place to drop the sign
by accident (Section 20.1 covers this mistake directly).

## 15. Class Practice 7: Applying the Distributive Property

### Problem

Simplify: $4(x + 3)$

<details>
<summary>Solution</summary>

Distribute $4$ to both terms inside the parentheses:

$$4(x + 3) = 4(x) + 4(3) = 4x + 12$$

The answer is **$4x + 12$**.

</details>

## 16. Class Practice 8: Distributing a Negative Sign

### Problem

Simplify: $-3(x - 2)$

<details>
<summary>Solution</summary>

Distribute $-3$ to both terms inside the parentheses:

$$-3(x - 2) = -3(x) + (-3)(-2) = -3x + 6$$

The answer is **$-3x + 6$**.

</details>

## 17. Class Practice 9: Distribute, Then Combine Like Terms

### Problem

Simplify: $2(x + 5) + 3x$

<details>
<summary>Solution</summary>

Distribute first:

$$2(x + 5) = 2x + 10$$

Now combine with the remaining term:

$$2x + 10 + 3x = (2x + 3x) + 10 = 5x + 10$$

The answer is **$5x + 10$**.

</details>

## 18. Class Practice 10: Distribute a Negative, Then Combine Like Terms

### Problem

Simplify: $-2(x - 4) - 3x + 1$

<details>
<summary>Solution</summary>

Distribute first:

$$-2(x - 4) = -2x + 8$$

Combine with the remaining terms:

$$-2x + 8 - 3x + 1 = \underbrace{(-2x - 3x)}_{x\text{-terms}} + \underbrace{(8 + 1)}_{\text{constants}} = -5x + 9$$

The answer is **$-5x + 9$**.

</details>

## 19. Class Practice 11: Word Problem — Building an Expression

### Problem

A rope costs $\$2$ per foot, plus a one-time $\$5$ cutting fee. Write an expression for the
total cost of $x$ feet of rope, then evaluate it for $x = 6$.

<details>
<summary>Solution</summary>

The rope itself costs $2x$ dollars, plus the fixed $\$5$ fee:

$$2x + 5$$

Evaluate at $x = 6$:

$$2(6) + 5 = 12 + 5 = 17$$

The answer is **$2x + 5$ dollars; $\$17$ when $x = 6$**.

</details>

## 20. Common Mistakes

### 20.1 Dropping the sign when distributing a negative number

$-2(x - 5)$ distributes to $-2x + 10$, **not** $-2x - 10$ — multiplying $-2$ by $-5$ gives a
positive $10$. Every term inside the parentheses gets multiplied by the number *and its sign*
out front.

### 20.2 Combining terms that aren't alike

$3x$ and $5$ cannot be combined into $8x$ or $8$ — they don't have matching variable parts. Only
terms with the exact same variable (or terms that are all constants) can be combined.

### 20.3 Losing a sign when regrouping terms

In $5x - 8 - 2x + 3$, the $-8$ stays negative when it's moved next to the other constants. A
term's sign is attached to the term itself (rewrite subtraction as "add a negative" to keep
track of it), not to its position in the expression.

## 21. Key Takeaways

- A **term** is one piece of an expression; its **coefficient** is the number multiplied by
  its variable (no number written means coefficient $1$; a lone minus sign means $-1$).
- **Evaluate** an expression by substituting the given value for the variable, then following
  the order of operations.
- **Like terms** share the exact same variable part and can be combined by adding or
  subtracting their coefficients: $3x + x = 4x$.
- The **distributive property** removes parentheses: $a(b+c) = ab+ac$. Distributing a negative
  number flips the sign of every term inside.
- To fully simplify an expression: **distribute first**, then **combine like terms**.

Next lesson uses these simplification skills to **solve one-variable linear equations** — the
same balance idea, now with an unknown to isolate.
