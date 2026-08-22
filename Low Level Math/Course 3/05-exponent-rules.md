# Lesson 5: Exponent Notation and the Laws of Exponents

This lesson opens Weeks 3–4 of the syllabus ([00-syllabus.md](./00-syllabus.md)): exponents.
It starts from the most basic definition — a positive integer exponent as repeated
multiplication — and derives the core exponent rules directly from that definition. Every
rule here assumes a **positive integer** exponent; [Lesson 6](./06-zero-negative-fractional-exponents.md)
extends the definition to zero, negative, and fractional exponents.

## 1. The Primitive Definition: Positive Integer Exponents

For a real number $a$ (the **base**) and a positive integer $n$ (the **exponent**), $a^n$
(read "$a$ to the power of $n$") means $a$ multiplied by itself $n$ times:

$$a^n = \underbrace{a \times a \times \cdots \times a}_{n \text{ factors}}$$

$$2^3 = 2 \times 2 \times 2 = 8 \qquad (-3)^2 = (-3) \times (-3) = 9 \qquad \left(\frac{1}{2}\right)^4 = \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{16}$$

$a^1 = a$ (a single factor). Everything else in this lesson — every rule — is a direct
consequence of this "count the factors" definition, not a separate fact to memorize.

### Reading Example: Sign Behavior in Powers

Evaluate $(-2)^4$ and $(-2)^5$.

$$(-2)^4 = (-2)(-2)(-2)(-2) = 16 \qquad (-2)^5 = (-2)(-2)(-2)(-2)(-2) = -32$$

**Non-obvious detail:** this is the same "count the negatives" rule from
[Lesson 3](./03-irrational-numbers.md#1-quick-review-operating-with-negative-numbers) — an
even number of negative factors gives a positive product, an odd number gives a negative
product. A negative base raised to an even exponent is always positive; raised to an odd
exponent, always negative.

## 2. Product of Powers: $a^m \times a^n = a^{m+n}$

Expand both sides using the definition and count factors:

$$a^m \times a^n = \underbrace{(a \times \cdots \times a)}_{m \text{ factors}} \times \underbrace{(a \times \cdots \times a)}_{n \text{ factors}} = \underbrace{a \times \cdots \times a}_{m+n \text{ factors}} = a^{m+n}$$

Multiplying $a^m$ by $a^n$ just concatenates the factor lists — $m$ factors followed by $n$
more factors is $m+n$ factors total.

$$2^3 \times 2^2 = 2^{3+2} = 2^5 = 32 \qquad \text{check: } 8 \times 4 = 32 \ \checkmark$$

**This rule requires the same base on both sides.** $2^3 \times 3^2$ cannot be combined into
a single power this way — the factors aren't all the same number, so there's nothing to
concatenate.

## 3. Power of a Power: $(a^m)^n = a^{mn}$

$(a^m)^n$ means "$a^m$, multiplied by itself $n$ times":

$$(a^m)^n = \underbrace{a^m \times a^m \times \cdots \times a^m}_{n \text{ factors of } a^m} = \underbrace{(a \times \cdots \times a)}_{m} \times \underbrace{(a \times \cdots \times a)}_{m} \times \cdots \ (n \text{ groups}) = \underbrace{a \times \cdots \times a}_{m \times n \text{ factors}} = a^{mn}$$

$n$ groups of $m$ factors each is $m \times n$ factors total.

$$(2^3)^2 = 2^{3 \times 2} = 2^6 = 64 \qquad \text{check: } (2^3)^2 = 8^2 = 64 \ \checkmark$$

### Reading Example: Telling $a^m \times a^n$ Apart From $(a^m)^n$

Evaluate $2^3 \times 2^2$ and $(2^3)^2$, and compare.

$$2^3 \times 2^2 = 2^5 = 32 \qquad \qquad (2^3)^2 = 2^6 = 64$$

**Non-obvious detail:** these look similar but are different operations — the first
**adds** the exponents ($3 + 2$) because it's two separate groups of factors placed side by
side; the second **multiplies** the exponents ($3 \times 2$) because it's $n$ copies of an
already-$m$-factor group. Mixing these up (e.g., multiplying when the rule calls for adding)
is one of the most common exponent errors.

## 4. Power of a Product: $(ab)^n = a^n b^n$

Expand $(ab)^n$ and use the fact that multiplication can be reordered (commutative property):

$$(ab)^n = \underbrace{(ab) \times (ab) \times \cdots \times (ab)}_{n \text{ factors}} = \underbrace{(a \times a \times \cdots \times a)}_{n} \times \underbrace{(b \times b \times \cdots \times b)}_{n} = a^n b^n$$

$$(2 \times 3)^3 = 6^3 = 216 \qquad \text{check: } 2^3 \times 3^3 = 8 \times 27 = 216 \ \checkmark$$

The same reordering argument applies to a quotient, as long as the denominator isn't zero:

$$\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n} \qquad (b \ne 0) \qquad \qquad \left(\frac{3}{4}\right)^2 = \frac{3^2}{4^2} = \frac{9}{16}$$

## 5. Quotient of Powers: $\dfrac{a^m}{a^n} = a^{m-n}$ (for $m > n$, $a \ne 0$)

Write out the division as a fraction and cancel matching factors from top and bottom, the
same way a fraction reduces to simplest form
([Lesson 3, Section 2](./03-irrational-numbers.md#2-quick-review-operating-with-fractions)):

$$\frac{a^m}{a^n} = \frac{\overbrace{a \times \cdots \times a}^{m}}{\underbrace{a \times \cdots \times a}_{n}} = \underbrace{a \times \cdots \times a}_{m - n \text{ factors remain}} = a^{m-n}$$

Each of the $n$ factors in the denominator cancels one factor in the numerator, leaving
$m - n$ factors.

$$\frac{2^5}{2^2} = 2^{5-2} = 2^3 = 8 \qquad \text{check: } \frac{32}{4} = 8 \ \checkmark$$

**This rule is restricted to $m > n$ for now** — that keeps $m - n$ a positive integer, so
the result still fits the primitive definition from Section 1. What happens when $m = n$ or
$m < n$ is exactly the question [Lesson 6](./06-zero-negative-fractional-exponents.md) answers.

### Class Practice 1: Combining the Rules

#### Problem

Simplify $\dfrac{(3^2)^3 \times 3^4}{3^5}$, leaving the answer as a single power of $3$.

<details>
<summary>Solution</summary>

Power of a power first (Section 3): $(3^2)^3 = 3^{2 \times 3} = 3^6$.

Product of powers in the numerator (Section 2): $3^6 \times 3^4 = 3^{6+4} = 3^{10}$.

Quotient of powers (Section 5): $\dfrac{3^{10}}{3^5} = 3^{10-5} = 3^5$.

The answer is **$3^5$** (which equals $243$).

</details>

### Class Practice 2: Power of a Product and a Quotient

#### Problem

Simplify $(2x)^3 \times \left(\dfrac{x}{2}\right)^2$, leaving the answer with a single power
of $x$ and a single numeric coefficient.

<details>
<summary>Solution</summary>

Apply power of a product and power of a quotient (Section 4) separately:

$$(2x)^3 = 2^3 x^3 = 8x^3 \qquad \qquad \left(\frac{x}{2}\right)^2 = \frac{x^2}{2^2} = \frac{x^2}{4}$$

Multiply, then combine the powers of $x$ with the product rule (Section 2):

$$8x^3 \times \frac{x^2}{4} = \frac{8}{4} \times x^3 \times x^2 = 2 \times x^5$$

The answer is **$2x^5$**.

</details>

### Class Practice 3: Spotting Which Rule Applies

#### Problem

For each expression, state which rule applies and simplify: (a) $5^3 \times 5^6$,
(b) $(5^3)^6$, (c) $\dfrac{5^9}{5^4}$.

<details>
<summary>Solution</summary>

- (a) Same base, multiplied → **product of powers**, add exponents: $5^{3+6} = 5^9$.
- (b) A power raised to another power → **power of a power**, multiply exponents:
  $5^{3 \times 6} = 5^{18}$.
- (c) Same base, divided → **quotient of powers**, subtract exponents: $5^{9-4} = 5^5$.

</details>

## 6. Common Mistakes

### 6.1 Adding exponents with different bases

$2^3 \times 3^2$ is **not** $6^5$ — the product-of-powers rule (Section 2) only combines
exponents when the base is identical on both sides. With different bases, evaluate each
power separately first: $2^3 \times 3^2 = 8 \times 9 = 72$.

### 6.2 Adding exponents instead of multiplying (or vice versa) for a power of a power

$(a^m)^n$ multiplies the exponents ($a^{mn}$); $a^m \times a^n$ adds them ($a^{m+n}$). These
are different operations that happen to look similar — see the Reading Example in Section 3.

### 6.3 Forgetting the power of a product distributes to every factor

$(2x)^3$ is $2^3 x^3 = 8x^3$, **not** $2x^3$ — the exponent applies to every factor inside
the parentheses, not just the variable.

## 7. Key Takeaways

- $a^n$ means $n$ copies of $a$ multiplied together; every rule below follows from counting
  factors under this definition.
- **Product of powers:** $a^m \times a^n = a^{m+n}$ (same base only — concatenate factors).
- **Power of a power:** $(a^m)^n = a^{mn}$ ($n$ groups of $m$ factors each).
- **Power of a product/quotient:** $(ab)^n = a^n b^n$ and $\left(\dfrac{a}{b}\right)^n =
  \dfrac{a^n}{b^n}$ (the exponent distributes to every factor).
- **Quotient of powers:** $\dfrac{a^m}{a^n} = a^{m-n}$, valid here only for $m > n$ so the
  exponent stays a positive integer.

[Next lesson](./06-zero-negative-fractional-exponents.md) extends the definition of $a^n$
to $n = 0$, negative integers, and fractions — chosen so that all four rules above keep
working without exception.
