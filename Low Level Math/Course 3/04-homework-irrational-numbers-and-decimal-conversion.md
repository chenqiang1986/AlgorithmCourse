# Homework: Lessons 3–4 — Irrational Numbers and Decimal-Fraction Conversion
*Low Level Math / Course 3*

This homework covers [03-irrational-numbers.md](./03-irrational-numbers.md) (a quick
integer/fraction review, rational vs. irrational numbers, and the proof that $\sqrt{2}$ is
irrational) and [04-decimal-fraction-conversion.md](./04-decimal-fraction-conversion.md)
(converting fractions to decimals and back, for both terminating and repeating decimals).

## Part A: Integer and Fraction Quick Review

### Problem 1

Evaluate: $(-6) + 9 \times (-2)^2 \div (-4)$

<details>
<summary>Solution</summary>

Exponent first, then multiplication/division left to right, then addition:

$$(-6) + 9 \times (-2)^2 \div (-4) = (-6) + 9 \times 4 \div (-4) = (-6) + 36 \div (-4) = (-6) + (-9) = -15$$

The answer is **$-15$**.

</details>

### Problem 2

Evaluate: $(-15) - (-4) \times 3 \div (-6)$

<details>
<summary>Solution</summary>

Multiplication/division first, left to right:

$$(-4) \times 3 = -12 \qquad \qquad (-12) \div (-6) = 2$$

Then subtract, rewritten as adding the opposite:

$$(-15) - 2 = (-15) + (-2) = -17$$

The answer is **$-17$**.

</details>

### Problem 3

Evaluate: $\left(-\dfrac{3}{5}\right) \times \dfrac{10}{9} \div \left(-\dfrac{2}{3}\right)$

<details>
<summary>Solution</summary>

Multiply first, left to right. Different signs, so the product is negative:

$$\left(-\frac{3}{5}\right) \times \frac{10}{9} = -\left(\frac{3 \times 10}{5 \times 9}\right) = -\frac{30}{45} = -\frac{2}{3}$$

Now divide by $-\dfrac{2}{3}$: flip to the reciprocal and multiply. Same sign (both
negative), so the result is positive:

$$\left(-\frac{2}{3}\right) \div \left(-\frac{2}{3}\right) = \left(-\frac{2}{3}\right) \times \left(-\frac{3}{2}\right) = \frac{2 \times 3}{3 \times 2} = 1$$

The answer is **$1$**.

</details>

### Problem 4

Evaluate: $\dfrac{5}{8} - \dfrac{1}{4} \times \dfrac{2}{3}$

<details>
<summary>Solution</summary>

Multiply first:

$$\frac{1}{4} \times \frac{2}{3} = \frac{1 \times 2}{4 \times 3} = \frac{2}{12} = \frac{1}{6}$$

Now subtract, using a common denominator of $8 \times 3 = 24$:

$$\frac{5}{8} \times \frac{3}{3} = \frac{15}{24} \qquad \qquad \frac{1}{6} \times \frac{4}{4} = \frac{4}{24}$$

$$\frac{15}{24} - \frac{4}{24} = \frac{15-4}{24} = \frac{11}{24}$$

$11$ is prime and doesn't divide $24$, so $\dfrac{11}{24}$ is already in simplest form.

The answer is **$\dfrac{11}{24}$**.

</details>

## Part B: Rational vs. Irrational Numbers

### Problem 5

Classify each number as rational or irrational: $\sqrt{49}$, $0.\overline{45}$, $\sqrt{7}$,
$-\dfrac{9}{4}$, $\pi$.

<details>
<summary>Solution</summary>

- $\sqrt{49}$ — $49$ is a perfect square, so $\sqrt{49} = 7$. **Rational.**
- $0.\overline{45}$ — a repeating decimal, equal to $\dfrac{45}{99} = \dfrac{5}{11}$.
  **Rational.**
- $\sqrt{7}$ — $7$ is not a perfect square, so (same style of proof as $\sqrt{2}$)
  $\sqrt{7}$ cannot be written as a fraction. **Irrational.**
- $-\dfrac{9}{4}$ — already a ratio of integers. **Rational.**
- $\pi$ — infinite, non-repeating decimal. **Irrational.**

</details>

### Problem 6

Prove that $\sqrt{3}$ is irrational, using the same contradiction method as the proof for
$\sqrt{2}$ in [Lesson 3](./03-irrational-numbers.md).

<details>
<summary>Solution</summary>

Suppose, for contradiction, that $\sqrt{3}$ is rational. Then it can be written as
$\sqrt{3} = \dfrac{p}{q}$ in lowest terms (no common factor between $p$ and $q$). Squaring
both sides:

$$3 = \frac{p^2}{q^2} \qquad \Longrightarrow \qquad p^2 = 3q^2$$

So $p^2$ is a multiple of $3$. This forces $p$ itself to be a multiple of $3$: any integer
not divisible by $3$ leaves remainder $1$ or $2$ when divided by $3$, and squaring a number
of the form $3m+1$ or $3m+2$ always leaves remainder $1$ — never $0$ — so a number's square
is only divisible by $3$ if the number itself was. Write $p = 3k$ and substitute:

$$(3k)^2 = 3q^2 \qquad \Longrightarrow \qquad 9k^2 = 3q^2 \qquad \Longrightarrow \qquad q^2 = 3k^2$$

By the same reasoning, $q$ must also be a multiple of $3$. But then $p$ and $q$ share a
common factor of $3$, contradicting the assumption that $\dfrac{p}{q}$ was in lowest terms.

The contradiction means $\sqrt{3}$ cannot be written as $\dfrac{p}{q}$ at all, so
**$\sqrt{3}$ is irrational**. $\blacksquare$

</details>

### Problem 7

Determine whether $\sqrt{18}$ is rational or irrational, and simplify it as far as possible.

<details>
<summary>Solution</summary>

$18$ is not a perfect square, but it factors as $18 = 9 \times 2$, so:

$$\sqrt{18} = \sqrt{9 \times 2} = \sqrt{9} \times \sqrt{2} = 3\sqrt{2}$$

If $3\sqrt{2}$ were rational, dividing it by the nonzero rational number $3$ would make
$\sqrt{2}$ rational too — but Lesson 3 proved $\sqrt{2}$ is irrational, a contradiction. So
$3\sqrt{2}$ (and therefore $\sqrt{18}$) must be **irrational**.

The answer is **irrational, simplified form $3\sqrt{2}$**.

</details>

### Problem 8

Determine whether $\sqrt{2} + 3$ is rational or irrational. Explain your reasoning.

<details>
<summary>Solution</summary>

Suppose, for contradiction, that $\sqrt{2} + 3$ is rational — call it $r$. Then:

$$\sqrt{2} = r - 3$$

The right side is a rational number minus a rational number, which is always rational. So
this would make $\sqrt{2}$ rational, contradicting Lesson 3's proof that $\sqrt{2}$ is
irrational. So the assumption was false.

The answer is **irrational**.

</details>

### Problem 9

True or False, with a one-sentence justification: "Every repeating decimal is irrational."

<details>
<summary>Solution</summary>

**False.** A repeating decimal is exactly one of the ways a *rational* number can look — for
example, $0.\overline{6} = \dfrac{2}{3}$ repeats forever but is rational. "Infinite" alone
doesn't mean irrational; irrational means infinite **and never falling into a repeating
pattern**.

</details>

## Part C: Fractions to Decimals

### Problem 10

Without dividing, determine whether $\dfrac{9}{25}$ terminates. Then find its decimal value.

<details>
<summary>Solution</summary>

Factor the denominator: $25 = 5^2$ — only $5$s, so it terminates. Long division:

$$\frac{9}{25} = 9 \div 25 = 0.36$$

The answer is **$0.36$**.

</details>

### Problem 11

Without dividing, determine whether $\dfrac{7}{15}$ terminates. Then find its decimal value.

<details>
<summary>Solution</summary>

Factor the denominator: $15 = 3 \times 5$ — the factor of $3$ means it does **not**
terminate; it repeats. Long division:

| Step | Bring down | Divide | Quotient digit | Remainder |
|---|---|---|---|---|
| 1 | $70$ | $70 \div 15$ | $4$ | $10$ |
| 2 | $100$ | $100 \div 15$ | $6$ | $10$ |

The remainder $10$ repeats at step 2, so the digit $6$ repeats forever:

$$\frac{7}{15} = 0.4666\ldots = 0.4\overline{6}$$

The answer is **$0.4\overline{6}$**.

</details>

### Problem 12

Convert $\dfrac{5}{12}$ to a decimal. State whether it terminates or repeats, and why.

<details>
<summary>Solution</summary>

$12 = 2^2 \times 3$ — the factor of $3$ means it repeats. Long division:

| Step | Bring down | Divide | Quotient digit | Remainder |
|---|---|---|---|---|
| 1 | $50$ | $50 \div 12$ | $4$ | $2$ |
| 2 | $20$ | $20 \div 12$ | $1$ | $8$ |
| 3 | $80$ | $80 \div 12$ | $6$ | $8$ |

The remainder $8$ repeats at step 3, so the digit $6$ repeats forever from there:

$$\frac{5}{12} = 0.41666\ldots = 0.41\overline{6}$$

The answer is **$0.41\overline{6}$**, repeating.

</details>

### Problem 13

Convert $\dfrac{11}{6}$ to a decimal.

<details>
<summary>Solution</summary>

$6 = 2 \times 3$ has a factor of $3$, so it repeats. Since $11 > 6$, the whole-number part is
$11 \div 6 = 1$ remainder $5$; continue dividing the remainder as a decimal:

| Step | Bring down | Divide | Quotient digit | Remainder |
|---|---|---|---|---|
| 1 | $50$ | $50 \div 6$ | $8$ | $2$ |
| 2 | $20$ | $20 \div 6$ | $3$ | $2$ |

The remainder $2$ repeats at step 2, so the digit $3$ repeats forever:

$$\frac{11}{6} = 1.8333\ldots = 1.8\overline{3}$$

The answer is **$1.8\overline{3}$**.

</details>

## Part D: Decimals to Fractions

### Problem 14

Convert $0.48$ to a fraction in simplest form.

<details>
<summary>Solution</summary>

Two decimal places, so the denominator is $100$:

$$0.48 = \frac{48}{100}$$

Reduce: $48 = 4 \times 12$ and $100 = 4 \times 25$, so:

$$\frac{48}{100} = \frac{12}{25}$$

The answer is **$\dfrac{12}{25}$**.

</details>

### Problem 15

Convert $0.\overline{18}$ to a fraction in simplest form.

<details>
<summary>Solution</summary>

The repeating block ($18$) has length $k = 2$, so multiply by $100$:

$$
\begin{aligned}
x &= 0.181818\ldots \\
100x &= 18.181818\ldots \\
100x - x &= 18 \\
99x &= 18 \\
x &= \frac{18}{99} = \frac{2}{11}
\end{aligned}
$$

The answer is **$\dfrac{2}{11}$**.

</details>

### Problem 16

Convert $0.\overline{4}$ to a fraction in simplest form.

<details>
<summary>Solution</summary>

One repeating digit, so multiply by $10$:

$$
\begin{aligned}
x &= 0.4444\ldots \\
10x &= 4.4444\ldots \\
10x - x &= 4 \\
9x &= 4 \\
x &= \frac{4}{9}
\end{aligned}
$$

$4$ and $9$ share no common factor, so $\dfrac{4}{9}$ is already in simplest form.

The answer is **$\dfrac{4}{9}$**.

</details>

### Problem 17

Convert $0.5\overline{2}$ to a fraction in simplest form, using the split-and-add method
from [Lesson 4, Section 2.3](./04-decimal-fraction-conversion.md).

<details>
<summary>Solution</summary>

Split off the non-repeating digit ($n = 1$) from the repeating digit ($k = 1$):

$$0.5\overline{2} = 0.5 + \frac{0.\overline{2}}{10} = \frac{1}{2} + \frac{2/9}{10} = \frac{1}{2} + \frac{2}{90} = \frac{1}{2} + \frac{1}{45}$$

Add using a common denominator of $90$:

$$\frac{1}{2} + \frac{1}{45} = \frac{45}{90} + \frac{2}{90} = \frac{47}{90}$$

$47$ is prime and doesn't divide $90$, so $\dfrac{47}{90}$ is already in simplest form.

The answer is **$\dfrac{47}{90}$**.

</details>

### Problem 18

Convert $0.12\overline{45}$ to a fraction in simplest form.

<details>
<summary>Solution</summary>

Split off the two non-repeating digits ($n = 2$) from the repeating block ($k = 2$):

$$0.12\overline{45} = 0.12 + \frac{0.\overline{45}}{100} = \frac{12}{100} + \frac{45/99}{100} = \frac{3}{25} + \frac{45}{9900}$$

Reduce the second fraction: $45 = 45 \times 1$ and $9900 = 45 \times 220$, so
$\dfrac{45}{9900} = \dfrac{1}{220}$. Add using a common denominator of $1100$:

$$\frac{3}{25} + \frac{1}{220} = \frac{132}{1100} + \frac{5}{1100} = \frac{137}{1100}$$

$137$ is prime and doesn't divide $1100$, so $\dfrac{137}{1100}$ is already in simplest
form.

The answer is **$\dfrac{137}{1100}$**.

</details>
