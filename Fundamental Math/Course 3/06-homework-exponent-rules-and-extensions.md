# Homework: Lessons 5–6 — Exponent Rules and Extensions
*Fundamental Math / Course 3*

This homework covers [05-exponent-rules.md](./05-exponent-rules.md) (the primitive
positive-integer definition of an exponent, plus the product, power-of-a-power,
power-of-a-product/quotient, and quotient rules) and
[06-zero-negative-fractional-exponents.md](./06-zero-negative-fractional-exponents.md)
(extending the definition to zero, negative, and fractional exponents).

## Part A: Exponent Notation and Basic Rules

### Problem 1

Evaluate $(-3)^3$ and $(-3)^4$, and explain why one is negative and the other is positive.

<details>
<summary>Solution</summary>

$$(-3)^3 = (-3)(-3)(-3) = -27 \qquad (-3)^4 = (-3)(-3)(-3)(-3) = 81$$

An odd number of negative factors ($3$) multiplies out to a negative product; an even
number of negative factors ($4$) multiplies out to a positive product.

The answer is **$(-3)^3 = -27$ and $(-3)^4 = 81$**.

</details>

### Problem 2

Simplify $5^2 \times 5^4$, leaving the answer as a single power of $5$, then evaluate it.

<details>
<summary>Solution</summary>

Same base, so add the exponents (product of powers):

$$5^2 \times 5^4 = 5^{2+4} = 5^6 = 15625$$

Check directly: $5^2 = 25$, $5^4 = 625$, and $25 \times 625 = 15625$. $\checkmark$

The answer is **$5^6 = 15625$**.

</details>

### Problem 3

Simplify $(3^2)^4$, leaving the answer as a single power of $3$, then evaluate it.

<details>
<summary>Solution</summary>

Power of a power: multiply the exponents.

$$(3^2)^4 = 3^{2 \times 4} = 3^8 = 6561$$

Check directly: $3^2 = 9$, and $9^4 = 6561$. $\checkmark$

The answer is **$3^8 = 6561$**.

</details>

### Problem 4

Simplify $(3x)^2 \times x^3$, leaving the answer with a single numeric coefficient and a
single power of $x$.

<details>
<summary>Solution</summary>

Power of a product first: $(3x)^2 = 3^2 x^2 = 9x^2$.

Then product of powers to combine with $x^3$:

$$9x^2 \times x^3 = 9 \times x^{2+3} = 9x^5$$

The answer is **$9x^5$**.

</details>

## Part B: Quotient Rule and Combining Rules

### Problem 5

Simplify $\dfrac{7^6}{7^2}$, leaving the answer as a single power of $7$, then evaluate it.

<details>
<summary>Solution</summary>

Quotient of powers: subtract the exponents.

$$\frac{7^6}{7^2} = 7^{6-2} = 7^4 = 2401$$

The answer is **$7^4 = 2401$**.

</details>

### Problem 6

Simplify $\dfrac{2^3 \times 2^5}{2^4}$, leaving the answer as a single power of $2$, then
evaluate it.

<details>
<summary>Solution</summary>

Product of powers in the numerator first:

$$2^3 \times 2^5 = 2^{3+5} = 2^8$$

Then quotient of powers:

$$\frac{2^8}{2^4} = 2^{8-4} = 2^4 = 16$$

The answer is **$2^4 = 16$**.

</details>

### Problem 7

Simplify $\dfrac{(4^2)^3 \times 4}{4^5}$, leaving the answer as a single power of $4$, then
evaluate it.

<details>
<summary>Solution</summary>

Power of a power first: $(4^2)^3 = 4^{2 \times 3} = 4^6$.

Product of powers in the numerator: $4^6 \times 4^1 = 4^{6+1} = 4^7$.

Quotient of powers: $\dfrac{4^7}{4^5} = 4^{7-5} = 4^2 = 16$.

The answer is **$4^2 = 16$**.

</details>

### Problem 8

Simplify $\dfrac{(2y)^3}{y^2}$, leaving the answer with a single numeric coefficient and a
single power of $y$.

<details>
<summary>Solution</summary>

Power of a product first: $(2y)^3 = 2^3 y^3 = 8y^3$.

Then quotient of powers:

$$\frac{8y^3}{y^2} = 8 \times y^{3-2} = 8y$$

The answer is **$8y$**.

</details>

## Part C: Zero and Negative Exponents

### Problem 9

Evaluate $9^0$, $(-7)^0$, and $\left(\dfrac{2}{5}\right)^0$.

<details>
<summary>Solution</summary>

Any nonzero base raised to the power $0$ equals $1$:

$$9^0 = 1 \qquad (-7)^0 = 1 \qquad \left(\frac{2}{5}\right)^0 = 1$$

</details>

### Problem 10

True or False, with a one-sentence justification: "$a^0 = 0$ for every nonzero $a$."

<details>
<summary>Solution</summary>

**False.** $a^0 = 1$, not $0$ — it comes from $\dfrac{a^n}{a^n} = a^{n-n} = a^0$ agreeing
with $\dfrac{a^n}{a^n} = 1$ (a nonzero number divided by itself), not from multiplying by
zero.

</details>

### Problem 11

Evaluate $3^{-4}$.

<details>
<summary>Solution</summary>

A negative exponent means "reciprocal of the positive power":

$$3^{-4} = \frac{1}{3^4} = \frac{1}{81}$$

The answer is **$\dfrac{1}{81}$**.

</details>

### Problem 12

Evaluate $\left(\dfrac{2}{3}\right)^{-2}$.

<details>
<summary>Solution</summary>

$$\left(\frac{2}{3}\right)^{-2} = \frac{1}{(2/3)^2} = \frac{1}{4/9} = \frac{9}{4}$$

The answer is **$\dfrac{9}{4}$**.

</details>

### Problem 13

Simplify $x^5 \times x^{-2} \times x^{-3}$, leaving the answer as a single power of $x$.
Then use that result to evaluate $2^5 \times 2^{-2} \times 2^{-3}$.

<details>
<summary>Solution</summary>

Same base throughout, so add all the exponents:

$$x^5 \times x^{-2} \times x^{-3} = x^{5 + (-2) + (-3)} = x^0 = 1 \quad (x \ne 0)$$

Since the simplified form is just $1$ regardless of the base:

$$2^5 \times 2^{-2} \times 2^{-3} = 1$$

The answer is **$1$**.

</details>

## Part D: Fractional Exponents

### Problem 14

Evaluate $25^{1/2}$.

<details>
<summary>Solution</summary>

$a^{1/2}$ is the square root of $a$:

$$25^{1/2} = \sqrt{25} = 5$$

The answer is **$5$**.

</details>

### Problem 15

Evaluate $27^{1/3}$.

<details>
<summary>Solution</summary>

$a^{1/3}$ is the cube root of $a$:

$$27^{1/3} = \sqrt[3]{27} = 3$$

The answer is **$3$**.

</details>

### Problem 16

Evaluate $16^{3/4}$.

<details>
<summary>Solution</summary>

Root first, since $16$ is a perfect fourth power:

$$16^{3/4} = \left(16^{1/4}\right)^3 = \left(\sqrt[4]{16}\right)^3 = 2^3 = 8$$

The answer is **$8$**.

</details>

### Problem 17

Evaluate $8^{-2/3}$.

<details>
<summary>Solution</summary>

Handle the negative exponent first — take the reciprocal:

$$8^{-2/3} = \frac{1}{8^{2/3}}$$

Then the fractional exponent, root first:

$$8^{2/3} = \left(8^{1/3}\right)^2 = \left(\sqrt[3]{8}\right)^2 = 2^2 = 4$$

$$8^{-2/3} = \frac{1}{4}$$

The answer is **$\dfrac{1}{4}$**.

</details>

### Problem 18

Determine whether $5^{1/2}$ is rational or irrational. Justify your answer using the same
style of reasoning as [Lesson 3](./03-irrational-numbers.md)'s proof that $\sqrt{2}$ is
irrational.

<details>
<summary>Solution</summary>

$5^{1/2} = \sqrt{5}$ (Lesson 6, Section 3). Suppose, for contradiction, that $\sqrt{5}$ is
rational — writable in lowest terms as $\sqrt{5} = \dfrac{p}{q}$. Squaring both sides:

$$5 = \frac{p^2}{q^2} \qquad \Longrightarrow \qquad p^2 = 5q^2$$

So $p^2$ is a multiple of $5$, which forces $p$ itself to be a multiple of $5$ (an integer
not divisible by $5$ never has a square divisible by $5$). Write $p = 5k$ and substitute:

$$(5k)^2 = 5q^2 \qquad \Longrightarrow \qquad 25k^2 = 5q^2 \qquad \Longrightarrow \qquad q^2 = 5k^2$$

By the same reasoning, $q$ must also be a multiple of $5$. But then $p$ and $q$ share a
common factor of $5$, contradicting the assumption that $\dfrac{p}{q}$ was in lowest terms.

The contradiction means $\sqrt{5}$ cannot be written as $\dfrac{p}{q}$ at all.

The answer is **irrational**.

</details>
