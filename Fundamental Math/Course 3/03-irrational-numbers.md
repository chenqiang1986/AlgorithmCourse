# Lesson 3: Reviewing Negative Numbers and Meeting Irrational Numbers
*Fundamental Math / Course 3*

Course 2 covered negative-number and fraction arithmetic in full detail. This lesson opens
Course 3's first unit — the number system — with a quick refresher on those rules, then
extends the number system beyond the rationals to introduce **irrational numbers**.

## 1. Quick Review: Operating With Negative Numbers

A fast recap of the sign rules from Course 2
([Lesson 3](../Course%202/03-negative-integers-addition-subtraction.md),
[Lesson 4](../Course%202/04-integer-multiplication-division.md)) — full explanations and
number-line pictures live there if any of this feels unfamiliar.

**Addition and subtraction:**

- Same sign → add the absolute values, keep the common sign: $(-4) + (-7) = -11$.
- Different signs → subtract the smaller absolute value from the larger, keep the sign of
  the larger: $(-9) + 5 = -4$.
- Subtraction is always "add the opposite": $a - b = a + (-b)$, so $7 - (-3) = 7 + 3 = 10$.

**Multiplication and division** follow one shared rule:

| Signs | Result |
|---|---|
| Same sign | Positive |
| Different signs | Negative |

$$(-8) \times (-3) = 24 \qquad (-8) \times 3 = -24 \qquad (-20) \div (-4) = 5 \qquad 20 \div (-4) = -5$$

With three or more factors, count the negatives: an even count gives a positive product, an
odd count gives a negative product.

### Reading Example: Mixed Operations

Evaluate $(-3) + 4 \times (-2)^2 \div 8$.

Order of operations first — exponent, then multiplication/division left to right, then
addition:

$$(-3) + 4 \times (-2)^2 \div 8 = (-3) + 4 \times 4 \div 8 = (-3) + 16 \div 8 = (-3) + 2 = -1$$

$(-2)^2 = 4$ because squaring is "same sign $\times$ same sign," which is always positive —
this is a common spot to accidentally drop the sign.

### Class Practice 1: Integer Review

#### Problem

Evaluate: $(-5) - (-2) \times 6 \div (-4)$

<details>
<summary>Solution</summary>

Multiplication/division first, left to right:

$$(-2) \times 6 = -12 \qquad \qquad (-12) \div (-4) = 3$$

Then subtract, rewritten as adding the opposite:

$$(-5) - 3 = (-5) + (-3) = -8$$

The answer is **$-8$**.

</details>

## 2. Quick Review: Operating With Fractions

A fast recap of the fraction rules from Course 2
([Lesson 5](../Course%202/05-fraction-multiplication-division.md),
[Lesson 6](../Course%202/06-fraction-addition.md)) — full explanations and pizza-slice
pictures live there if any of this feels unfamiliar.

- A fraction $\dfrac{a}{b}$ means $a \div b$, so it follows the same sign rule as division:
  same sign is positive, different signs is negative.
- **Multiply straight across:** $\dfrac{a}{b} \times \dfrac{c}{d} = \dfrac{a \times c}{b
  \times d}$.
- **Divide by multiplying by the reciprocal** (flip only the divisor):
  $\dfrac{a}{b} \div \dfrac{c}{d} = \dfrac{a}{b} \times \dfrac{d}{c}$.
- **Add/subtract with a common denominator.** Same denominator → combine numerators and
  keep the denominator: $\dfrac{a}{b} + \dfrac{c}{b} = \dfrac{a+c}{b}$. Different
  denominators → build a common one first: $\dfrac{a}{b} + \dfrac{c}{d} = \dfrac{ad +
  bc}{bd}$. Subtraction is still "add the opposite," same as integers.
- **Reduce to simplest form** as the last step: cancel any factor shared by numerator and
  denominator.

### Reading Example: Mixed Fraction Operations

Evaluate $\dfrac{2}{3} + \left(-\dfrac{5}{6}\right) \div \dfrac{5}{9}$.

Division before addition — flip the divisor and multiply:

$$\left(-\frac{5}{6}\right) \div \frac{5}{9} = \left(-\frac{5}{6}\right) \times \frac{9}{5} = -\frac{45}{30} = -\frac{3}{2}$$

Now add, using a common denominator of $6$:

$$\frac{2}{3} + \left(-\frac{3}{2}\right) = \frac{4}{6} + \left(-\frac{9}{6}\right) = \frac{4-9}{6} = -\frac{5}{6}$$

$-\dfrac{5}{6}$ is already in simplest form.

### Class Practice 2: Fraction Review

#### Problem

Evaluate: $\left(-\dfrac{7}{10}\right) - \dfrac{3}{5} \times \dfrac{5}{6}$

<details>
<summary>Solution</summary>

Multiplication before subtraction:

$$\frac{3}{5} \times \frac{5}{6} = \frac{3 \times 5}{5 \times 6} = \frac{15}{30} = \frac{1}{2}$$

Rewrite the subtraction as adding the opposite, using a common denominator of $10$:

$$\left(-\frac{7}{10}\right) - \frac{1}{2} = \left(-\frac{7}{10}\right) + \left(-\frac{5}{10}\right) = \frac{-7 + (-5)}{10} = -\frac{12}{10} = -\frac{6}{5}$$

The answer is **$-\dfrac{6}{5}$**.

</details>

## 3. From Rational to Irrational Numbers

A **rational number** is any number that can be written as a fraction of integers,
$\dfrac{p}{q}$ with $q \ne 0$. This includes every integer ($5 = \dfrac{5}{1}$), every
terminating decimal ($0.75 = \dfrac{3}{4}$), and every *repeating* decimal
($0.\overline{3} = \dfrac{1}{3}$). In every case, the decimal expansion either ends or
eventually falls into a repeating block.

An **irrational number** is a number that *cannot* be written as a fraction of integers. Its
decimal expansion is **infinite and never repeats** — no block of digits ever recurs
forever, no matter how far out you go. Familiar examples:

$$\sqrt{2} = 1.41421356\ldots \qquad \pi = 3.14159265\ldots \qquad \sqrt{3} = 1.73205081\ldots$$

Note that not every square root is irrational — $\sqrt{4} = 2$ and $\sqrt{9} = 3$ are
rational, since $4$ and $9$ are perfect squares. It's specifically the square roots of
non-perfect-squares that turn out to be irrational.

Together, the rationals and irrationals make up the **real numbers** — every point on the
number line is one or the other, never both.

## 4. Proof: $\sqrt{2}$ Is Irrational

This is one of the oldest proofs in mathematics. It works by **contradiction**: assume the
opposite of what we want to prove, then show that assumption leads to something impossible.

**Claim:** $\sqrt{2}$ cannot be written as $\dfrac{p}{q}$ for integers $p, q$.

**Proof.** Suppose, for contradiction, that $\sqrt{2}$ *is* rational. Then it can be written
as a fraction in **lowest terms** — meaning $p$ and $q$ share no common factor:

$$\sqrt{2} = \frac{p}{q}$$

Squaring both sides:

$$2 = \frac{p^2}{q^2} \qquad \Longrightarrow \qquad p^2 = 2q^2$$

Since $p^2$ equals $2$ times an integer, $p^2$ is even. An odd number squared is always odd
($3^2 = 9$, $5^2 = 25$, …), so if $p^2$ is even, $p$ itself must be even. Write
$p = 2k$ for some integer $k$, and substitute back:

$$(2k)^2 = 2q^2 \qquad \Longrightarrow \qquad 4k^2 = 2q^2 \qquad \Longrightarrow \qquad q^2 = 2k^2$$

By the same reasoning, $q^2$ is even, so $q$ is even too.

But now **both** $p$ and $q$ are even — they share a common factor of $2$. That contradicts
the starting assumption that $\dfrac{p}{q}$ was in lowest terms with no common factor.

The contradiction means the original assumption was false: $\sqrt{2}$ cannot be written as
$\dfrac{p}{q}$ at all. So $\sqrt{2}$ is irrational. $\blacksquare$

**Non-obvious detail:** the proof never computes a decimal digit of $\sqrt{2}$. It shows
irrationality purely from the logical impossibility of *any* fraction working — which is
exactly why it settles the question for good, rather than just for however many digits
someone checks.

## 5. Class Practice 3: Classifying Numbers

### Problem

For each number, state whether it is rational or irrational: $0.\overline{6}$, $\sqrt{16}$,
$\sqrt{5}$, $-\dfrac{7}{2}$.

<details>
<summary>Solution</summary>

- $0.\overline{6}$ — repeating decimal, equals $\dfrac{2}{3}$. **Rational.**
- $\sqrt{16}$ — $16$ is a perfect square, so $\sqrt{16} = 4$. **Rational.**
- $\sqrt{5}$ — $5$ is not a perfect square, and (by the same style of contradiction proof as
  $\sqrt{2}$) its square root cannot be written as a fraction. **Irrational.**
- $-\dfrac{7}{2}$ — already a ratio of integers. **Rational.**

</details>

## 6. Common Mistakes

### 6.1 Thinking "infinite decimal" always means irrational

$0.\overline{3} = 0.3333\ldots$ is infinite but **repeats**, so it's rational
($=\dfrac{1}{3}$). The test for irrational isn't "does it go on forever" — it's "does it go
on forever *without ever settling into a repeating pattern*."

### 6.2 Assuming every square root is irrational

$\sqrt{2}$ and $\sqrt{5}$ are irrational, but $\sqrt{4}$, $\sqrt{9}$, $\sqrt{16}$ are not —
check whether the number under the root is a perfect square first.

## 7. Key Takeaways

- Sign rules for $+, -, \times, \div$ carry over unchanged from Course 2: same-sign addition
  adds magnitudes, different-sign addition subtracts them; multiplication/division depend
  only on whether the signs match.
- Fraction rules also carry over unchanged: multiply straight across, divide by the
  reciprocal, and add/subtract only once denominators match — then reduce to simplest form.
- Rational numbers are exactly the numbers writable as $\dfrac{p}{q}$; their decimals
  terminate or repeat.
- Irrational numbers have infinite, non-repeating decimal expansions and cannot be written
  as a fraction of integers — $\pi$ and $\sqrt{2}$ are the classic examples.
- The proof that $\sqrt{2}$ is irrational assumes it *is* a fraction in lowest terms, then
  derives a contradiction (both numerator and denominator turn out even) — a template that
  works for $\sqrt{n}$ whenever $n$ is not a perfect square.

[Next lesson](./04-decimal-fraction-conversion.md) covers converting between decimals and
fractions — the mechanics behind the terminating/repeating facts used above.
