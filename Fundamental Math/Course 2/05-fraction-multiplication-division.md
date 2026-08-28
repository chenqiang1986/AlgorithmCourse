# Lesson 5: Fractions — Meaning, Signs, Multiplication, and Division
*Fundamental Math / Course 2*

[Lesson 4](./04-integer-multiplication-division.md) covered integer division, where the
quotient always came out to a whole number, like $(-20) \div (-4) = 5$. This lesson asks
what happens when it doesn't come out even, introduces the **fraction** as the answer to
that question, and covers the sign, multiplication, and division rules for fractions.

## 1. When Division Isn't Divisible

Evaluate $7 \div 2$. No integer, multiplied by $2$, gives $7$: $3 \times 2 = 6$ is too
small, and $4 \times 2 = 8$ is too big. The result lands strictly between two integers.

Two ways to describe that in-between value:

- **Quotient and remainder:** $7 \div 2 = 3$ remainder $1$ — useful for splitting a
  countable pile of objects into groups, but the leftover $1$ is set aside, not really
  part of the answer.
- **A fraction:** $7 \div 2 = \dfrac{7}{2}$ — the *exact* value, with nothing set aside.

Both descriptions come from the same division; the fraction is the one that keeps the
full, exact value in a single number instead of splitting it into a whole part and a
leftover.

## 2. A Fraction Is Division

For integers $a$ and $b$ with $b \ne 0$, the fraction $\dfrac{a}{b}$ **means** $a \div b$.
$a$ is the **numerator** (the amount being divided) and $b$ is the **denominator** (the
number of parts it's divided into).

$$\frac{a}{b} = a \div b$$

This single definition explains two things that otherwise look like separate rules:

- **Every whole number is a fraction with denominator $1$:** $\dfrac{a}{1} = a \div 1 = a$.
- **A fraction can equal a whole number when the division is exact:**
  $\dfrac{6}{2} = 6 \div 2 = 3$.

So fractions don't replace integer division — they're the same operation, written in a
form that stays exact even when the division doesn't come out even.

## 3. Core Template: Sign Rules for Fractions

Because $\dfrac{a}{b}$ *is* $a \div b$, the sign rule from
[Lesson 4](./04-integer-multiplication-division.md) applies directly:

| Signs of numerator and denominator | Sign of the fraction |
|---|---|
| Same sign (both $+$ or both $-$) | Positive |
| Different signs (one $+$, one $-$) | Negative |

$$\frac{-8}{-2} = +(8 \div 2) = 4 \qquad \qquad \frac{-8}{2} = -(8 \div 2) = -4 \qquad \qquad \frac{8}{-2} = -(8 \div 2) = -4$$

**A negative fraction has three equivalent forms.** The minus sign can sit in front of the
whole fraction, on the numerator, or on the denominator — all three name the same number,
because moving the sign doesn't change whether numerator and denominator have the *same*
sign or *different* signs:

$$-\frac{a}{b} = \frac{-a}{b} = \frac{a}{-b}$$

By convention, the first form — one minus sign in front — is the standard way to write a
negative fraction; the other two are simplified into that form when they show up.

## 4. Reading Example: Rewriting a Negative Fraction

Rewrite $\dfrac{5}{-9}$ in standard form, then evaluate its sign.

The numerator ($5$) and denominator ($-9$) have different signs, so the fraction is
negative. Move the minus sign from the denominator to the front of the whole fraction:

$$\frac{5}{-9} = -\frac{5}{9}$$

**Non-obvious detail:** this is the same move as rewriting $5 \div (-9) = -(5 \div 9)$ from
Lesson 4's sign rule — a fraction with a negative denominator isn't a new case, it's
integer division with different signs, just written with a fraction bar instead of a
$\div$ symbol.

## 5. Core Template: Multiplying Fractions

Before treating "multiply the numerators, multiply the denominators" as a rule to
memorize, here's *why* it's true — starting from what a fraction actually means
(Section 2).

**A concrete case: $\dfrac{1}{4} \times \dfrac{1}{5}$.** $\dfrac{1}{4}$ of a pizza means
cutting the whole pizza into $4$ equal pieces and keeping $1$. Multiplying that by
$\dfrac{1}{5}$ means cutting *that* one piece into $5$ equal pieces and keeping $1$ of
those smaller pieces:

![Three pizzas, each cut from a whole circle into equal wedges. The first pizza is cut into 4 equal quarters, with one quarter shaded orange and labeled 1/4. An arrow points to the second pizza, the same size, where that same shaded quarter is now subdivided into 5 thin equal slices, one of which is shaded orange and labeled with a leader line "1/4 of 1/5" — the other three quarters are left uncut. An equals sign points to the third pizza, where the entire circle is cut into 4 times 5 = 20 equal thin slices, with the one slice in the same position as before shaded orange and labeled "1/20." A caption below reads: cutting a piece into smaller pieces multiplies the number of cuts, 4 times 5 = 20 equal pieces.](./images/pizza-fraction-multiplication.svg)

Cutting one of the $4$ pieces into $5$ smaller pieces is the same as cutting *every* one
of the $4$ pieces into $5$ — the whole pizza ends up sliced into $4 \times 5 = 20$ equal
pieces, and the piece in hand is exactly $1$ of those $20$:

$$\frac{1}{4} \times \frac{1}{5} = \frac{1}{4 \times 5} = \frac{1}{20}$$

**The general rule follows the same logic.** Since $\dfrac{a}{b}$ is division
(Section 2), it's the same as $a$ copies of the unit fraction $\dfrac1b$:
$\dfrac{a}{b} = a \times \dfrac1b$. Write both fractions that way, then regroup the
factors — multiplication can be reordered and regrouped freely:

$$
\begin{aligned}
\frac{a}{b} \times \frac{c}{d} &= \left(a \times \frac1b\right) \times \left(c \times \frac1d\right) \\
&= (a \times c) \times \left(\frac1b \times \frac1d\right) \\
&= (a \times c) \times \frac{1}{b \times d} \qquad \text{(the same "cut into $b$, then into $d$" logic as the pizza)} \\
&= \frac{a \times c}{b \times d}
\end{aligned}
$$

So multiplying straight across the numerators and denominators isn't an arbitrary
shortcut — it's what "cut into $b$ pieces, then cut one of those into $d$ pieces, and
keep $a \times c$ of them" works out to:

$$\frac{a}{b} \times \frac{c}{d} = \frac{a \times c}{b \times d}$$

Handle the sign first using Section 3's table, then multiply the absolute values of the
numerators and the absolute values of the denominators:

$$\frac{2}{3} \times \frac{4}{5} = \frac{2 \times 4}{3 \times 5} = \frac{8}{15}$$

$$\left(-\frac{2}{3}\right) \times \frac{4}{5} = -\left(\frac{2 \times 4}{3 \times 5}\right) = -\frac{8}{15}$$

If the result can be reduced to a whole number or a smaller-looking fraction (like
$\dfrac{4}{6} = \dfrac{2}{3}$), it's fine to reduce it — but *why* that reduction is valid
is the subject of the next lesson's equivalence rules. For now, either form is an
acceptable answer.

## 6. Reading Example: Multiplying Fractions With Different Signs

Evaluate $\left(-\dfrac{3}{4}\right) \times \left(-\dfrac{5}{7}\right)$.

Both fractions are negative — same sign — so the product is positive:

$$\left(-\frac{3}{4}\right) \times \left(-\frac{5}{7}\right) = +\left(\frac{3 \times 5}{4 \times 7}\right) = \frac{15}{28}$$

**Non-obvious detail:** the sign of a fraction (Section 3) and the sign of a *product* of
fractions (Section 5) are found the same way — same signs give positive, different signs
give negative — because a fraction is itself a quotient. There's no separate multiplication
sign rule to learn for fractions; it's the integer rule from Lesson 4, applied twice: once
to the fraction's own sign, once to the product's sign.

## 7. Core Template: Dividing Fractions — the Reciprocal

Division can be read two ways: "split $a$ into $b$ equal groups" (Section 2's reading), or
"how many copies of $b$ fit inside $a$." Both give the same answer for whole numbers — but
the second reading, *how many fit*, is the one that makes dividing by a fraction easy to
picture.

**A concrete case: how many $\dfrac15$'s fit in $1$ pizza, and in $3$ pizzas?** Cut a pizza
into fifths and count the slices — there are $5$ of them, so $5$ copies of $\dfrac15$ fit
inside $1$ pizza:

$$1 \div \frac15 = 5$$

Every pizza holds $5$ fifths, so $3$ pizzas hold $3$ groups of $5$ fifths:

![Two labeled pizza diagrams side by side. Left: a single pizza cut into 5 equal slices, numbered 1 through 5, with the caption "1 divided by 1/5 = 5." Right: three smaller pizzas, each cut into 5 equal slices, numbered consecutively 1 through 15 across all three pizzas, with the caption "3 divided by 1/5 = 3 times 5 = 15." A note beneath both reads: in general, dividing by 1/b counts how many b-ths fit into the amount, so a divided by 1/b equals a times b.](./images/pizza-fraction-division-unit.svg)

$$3 \div \frac15 = 3 \times 5 = 15$$

Nothing here depended on the specific numbers $3$ and $5$: dividing *any* amount $a$ by the
unit fraction $\dfrac1b$ counts how many $b$-ths fit inside $a$, and that count is always
$a$ groups of $b$:

$$a \div \frac1b = a \times b$$

**Extending this to a full fraction $\dfrac{c}{d}$.** Since $\dfrac{c}{d} = c \times
\dfrac1d$ (Section 2), dividing by $\dfrac{c}{d}$ is dividing by two factors in a row —
first by the whole number $c$, then by the unit fraction $\dfrac1d$:

$$
\begin{aligned}
\frac{a}{b} \div \frac{c}{d} &= a \div b \div \left(c \times \frac1d\right) &&\text{Section 2: } \tfrac{a}{b} = a \div b \\
&= a \div b \div c \div \frac1d &&\text{dividing by a product = dividing by each factor in turn} \\
&= a \div (b \times c) \div \frac1d &&\text{dividing by } b\text{, then by } c\text{, is dividing by } b \times c \\
&= a \div (b \times c) \times d &&\text{dividing by a unit fraction: the rule just found} \\
&= \frac{a}{b \times c} \times d \\
&= \frac{a \times d}{b \times c}
\end{aligned}
$$

That last line, $\dfrac{a \times d}{b \times c}$, is exactly $\dfrac{a}{b} \times
\dfrac{d}{c}$ — the first fraction unchanged, the second fraction flipped. So "flip the
second fraction and multiply" isn't a separate rule to memorize; it's what "how many
$\dfrac{c}{d}$'s fit inside $\dfrac{a}{b}$" works out to once it's broken into two ordinary
divisions.

**The reciprocal, named.** The **reciprocal** of a nonzero fraction $\dfrac{c}{d}$ is
$\dfrac{d}{c}$ — numerator and denominator swapped. A fraction times its reciprocal always
equals $1$:

$$\frac{c}{d} \times \frac{d}{c} = \frac{c \times d}{d \times c} = 1$$

Dividing by a fraction means multiplying by its reciprocal:

$$\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c}$$

Only the **second** fraction (the divisor) gets flipped; the first stays exactly as it is:

$$\frac{2}{3} \div \frac{4}{5} = \frac{2}{3} \times \frac{5}{4} = \frac{2 \times 5}{3 \times 4} = \frac{10}{12}$$

## 8. Reading Example: Dividing Fractions With a Negative Sign

Evaluate $\left(-\dfrac{3}{5}\right) \div \dfrac{2}{7}$.

Flip the second fraction (the divisor) to its reciprocal, and change division to
multiplication:

$$\left(-\frac{3}{5}\right) \div \frac{2}{7} = \left(-\frac{3}{5}\right) \times \frac{7}{2}$$

Different signs, so the product is negative; multiply the absolute values:

$$\left(-\frac{3}{5}\right) \times \frac{7}{2} = -\left(\frac{3 \times 7}{5 \times 2}\right) = -\frac{21}{10}$$

**Non-obvious detail:** the sign is decided *before* flipping anything — flipping a
fraction to its reciprocal never changes its sign, since $\dfrac{a}{b}$ and $\dfrac{b}{a}$
have the same numerator/denominator sign relationship. So $\dfrac{7}{2}$ stays positive
even though it came from flipping $\dfrac{2}{7}$, and the negative sign carried in this
problem comes entirely from the first fraction.

## 9. Class Practice 1: Sign of a Fraction

### Problem

Rewrite $\dfrac{-6}{-11}$ in the simplest sign form, and state whether it's positive or
negative.

<details>
<summary>Solution</summary>

Numerator and denominator have the same sign (both negative), so the fraction is positive.
The two negatives cancel, leaving:

$$\frac{-6}{-11} = \frac{6}{11}$$

The answer is **$\dfrac{6}{11}$, positive**.

</details>

## 10. Class Practice 2: Multiplying Fractions

### Problem

Evaluate: $\left(-\dfrac{5}{6}\right) \times \dfrac{3}{8}$

<details>
<summary>Solution</summary>

Different signs, so the product is negative. Multiply the absolute values of the
numerators and denominators:

$$\left(-\frac{5}{6}\right) \times \frac{3}{8} = -\left(\frac{5 \times 3}{6 \times 8}\right) = -\frac{15}{48}$$

The answer is **$-\dfrac{15}{48}$**.

</details>

## 11. Class Practice 3: Dividing Fractions

### Problem

Evaluate: $\dfrac{4}{9} \div \left(-\dfrac{2}{3}\right)$

<details>
<summary>Solution</summary>

Flip the divisor to its reciprocal and multiply:

$$\frac{4}{9} \div \left(-\frac{2}{3}\right) = \frac{4}{9} \times \left(-\frac{3}{2}\right)$$

Different signs, so the product is negative:

$$\frac{4}{9} \times \left(-\frac{3}{2}\right) = -\left(\frac{4 \times 3}{9 \times 2}\right) = -\frac{12}{18}$$

The answer is **$-\dfrac{12}{18}$**.

</details>

## 12. Common Mistakes

### 12.1 Flipping the wrong fraction in division

In $\dfrac{a}{b} \div \dfrac{c}{d}$, only the **second** fraction (the one being divided
by) gets flipped. Flipping the first fraction instead, or flipping both, gives a different
— and wrong — answer. If it helps, say the operation out loud first: "divided by
$\dfrac{c}{d}$" names exactly which fraction turns into its reciprocal.

### 12.2 Forgetting that a fraction's sign depends on both parts

A fraction with a negative numerator *or* a negative denominator is negative — but a
fraction with both negative is positive, same as $(-1) \times (-1) = 1$ from Lesson 4.
Check numerator and denominator signs the same way you'd check two factors, not just by
glancing for a minus sign anywhere in the fraction.

### 12.3 Multiplying only the numerators, or only the denominators

Fraction multiplication touches *both* parts: numerator times numerator, denominator times
denominator. A common slip is multiplying the numerators but leaving one denominator
unchanged, or vice versa — always update both parts of the result together.

## 13. Key Takeaways

- A fraction $\dfrac{a}{b}$ is exactly $a \div b$ — the value that keeps a division exact
  even when it doesn't come out to a whole number.
- Every integer is a fraction with denominator $1$, and a fraction reduces to an integer
  exactly when its division is exact.
- Fraction signs follow the integer division rule: same sign (numerator/denominator) is
  positive, different signs is negative. A negative fraction can be written
  $-\dfrac{a}{b} = \dfrac{-a}{b} = \dfrac{a}{-b}$ — all three are the same number.
- Multiply fractions straight across: numerator times numerator, denominator times
  denominator, with the sign decided first.
- Dividing by a fraction means multiplying by its **reciprocal** (flip the divisor only) —
  this undoes division the same way Lesson 4's "division is the inverse of multiplication"
  explained integer division.

[Next lesson](./06-fraction-addition.md) covers **adding fractions**: first with a shared
denominator, then the equivalence rules that let two fractions with different denominators
be rewritten so they share one, so they can be added too.
