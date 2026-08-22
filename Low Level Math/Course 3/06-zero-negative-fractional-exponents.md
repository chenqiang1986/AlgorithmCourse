# Lesson 6: Zero, Negative, and Fractional Exponents

[Lesson 5](./05-exponent-rules.md) defined $a^n$ only for positive integer $n$, as $n$
copies of $a$ multiplied together, and restricted the quotient rule to $\dfrac{a^m}{a^n} =
a^{m-n}$ with $m > n$. This lesson extends the definition of $a^n$ to $n = 0$, negative
integers, and fractions — not as new, unrelated rules, but as the *only* choices that keep
every rule from Lesson 5 working with no exceptions.

## 1. Zero Exponent

What should $a^n$ mean when the quotient rule's condition $m > n$ fails at $m = n$? Apply
the quotient rule from [Lesson 5, Section 5](./05-exponent-rules.md) anyway:

$$\frac{a^n}{a^n} = a^{n-n} = a^0$$

But $\dfrac{a^n}{a^n}$ is also just "a nonzero number divided by itself," which is always
$1$. For both to be true, the definition has to be:

$$a^0 = 1 \qquad (a \ne 0)$$

$$5^0 = 1 \qquad (-3)^0 = 1 \qquad \left(\frac{2}{7}\right)^0 = 1$$

**Non-obvious detail:** $0^0$ is deliberately left undefined here — the argument above
divides $a^n$ by $a^n$, which requires $a \ne 0$. The base being raised to the zero power
must be nonzero for this definition to apply.

### Reading Example: Zero Exponent Inside a Larger Expression

Simplify $\dfrac{7x^0}{1}$ for $x \ne 0$.

$x^0 = 1$ regardless of what $x$ is (as long as $x \ne 0$), so:

$$7x^0 = 7 \times 1 = 7$$

**Non-obvious detail:** the exponent $0$ only applies to $x$, not to the $7$ in front — only
the base directly under the exponent is affected, the same way $(2x)^3$ (Lesson 5, Common
Mistake 6.3) differs from $2x^3$.

## 2. Negative Exponent

Now push further: what should $a^{-k}$ (for a positive integer $k$) mean? Apply the quotient
rule where $m < n$, say $\dfrac{a^m}{a^n}$ with $n - m = k$:

$$\frac{a^m}{a^n} = a^{m-n} = a^{-k}$$

But this same division, worked out by canceling factors directly, leaves $k$ factors in the
**denominator** instead of the numerator (there are more $a$'s to cancel below than above):

$$\frac{a^m}{a^n} = \frac{\overbrace{a \times \cdots \times a}^{m}}{\underbrace{a \times \cdots \times a}_{n}} = \frac{1}{\underbrace{a \times \cdots \times a}_{n - m}} = \frac{1}{a^k}$$

Matching the two results gives the definition:

$$a^{-k} = \frac{1}{a^k} \qquad (a \ne 0)$$

$$2^{-3} = \frac{1}{2^3} = \frac{1}{8} \qquad \qquad 5^{-1} = \frac{1}{5} \qquad \qquad \left(\frac{2}{3}\right)^{-2} = \frac{1}{(2/3)^2} = \frac{9}{4}$$

**A negative exponent means "reciprocal," not "negative number."** $2^{-3} = \dfrac{1}{8}$ is
positive — the sign of the exponent flips which side of the fraction the power sits on, it
does not make the value negative.

### Reading Example: Verifying the Product Rule Still Holds

Check that $a^n \times a^{-n} = a^0$ using the definitions above, with $a = 3$, $n = 4$.

$$3^4 \times 3^{-4} = 81 \times \frac{1}{81} = 1 = 3^0$$

**Non-obvious detail:** this is exactly why $a^{-k}$ had to be defined as $\dfrac{1}{a^k}$
and nothing else — it's the unique value that makes the product-of-powers rule
($a^n \times a^m = a^{n+m}$, Lesson 5 Section 2) keep working even when one exponent is
negative. Every rule from Lesson 5 — product, power of a power, power of a product — applies
unchanged to zero and negative integer exponents.

### Class Practice 1: Negative Exponents

#### Problem

Simplify $4^{-2} \times 4^5$, leaving the answer as a single power, then evaluate it.

<details>
<summary>Solution</summary>

Same base, so add the exponents (Lesson 5, Section 2), even though one is negative:

$$4^{-2} \times 4^5 = 4^{-2+5} = 4^3 = 64$$

Check directly: $4^{-2} = \dfrac{1}{16}$, and $\dfrac{1}{16} \times 4^5 = \dfrac{1024}{16} =
64$. $\checkmark$

The answer is **$64$**.

</details>

## 3. Fractional Exponent

Last, what should $a^{1/n}$ mean? Use the power-of-a-power rule
([Lesson 5, Section 3](./05-exponent-rules.md#3-power-of-a-power-amn--amn)) and demand it
still hold:

$$\left(a^{1/n}\right)^n = a^{(1/n) \times n} = a^1 = a$$

So $a^{1/n}$ must be **a number which, raised to the $n$-th power, gives $a$** — that is
exactly the definition of the $n$-th root:

$$a^{1/n} = \sqrt[n]{a}$$

$$8^{1/3} = \sqrt[3]{8} = 2 \qquad (\text{check: } 2^3 = 8) \qquad \qquad 16^{1/4} = \sqrt[4]{16} = 2 \qquad (\text{check: } 2^4 = 16)$$

For a general fractional exponent $\dfrac{m}{n}$, combine this with power of a power two
ways — both give the same result, since $\dfrac{m}{n} = \dfrac{1}{n} \times m = m \times
\dfrac{1}{n}$:

$$a^{m/n} = \left(a^{1/n}\right)^m = \left(\sqrt[n]{a}\right)^m \qquad \qquad a^{m/n} = \left(a^m\right)^{1/n} = \sqrt[n]{a^m}$$

**Connection to irrational numbers:** unlike $8^{1/3} = 2$, most fractional powers are not
whole numbers. $2^{1/2} = \sqrt{2}$, and [Lesson 3](./03-irrational-numbers.md#4-proof-sqrt2-is-irrational)
proved $\sqrt{2}$ has an infinite, non-repeating decimal expansion — it's irrational.
Fractional exponents are exactly how square roots (and cube roots, and so on) fit into the
same exponent notation as everything else in this unit, whether the result turns out
rational (like $8^{1/3}$) or irrational (like $2^{1/2}$).

### Reading Example: A Fractional Exponent Both Ways

Evaluate $4^{3/2}$ using both orders from the boxed rule above.

**Root first, then power:**

$$4^{3/2} = \left(4^{1/2}\right)^3 = \left(\sqrt{4}\right)^3 = 2^3 = 8$$

**Power first, then root:**

$$4^{3/2} = \left(4^3\right)^{1/2} = \sqrt{64} = 8$$

**Non-obvious detail:** both orders agree, but "root first" is usually easier arithmetic —
$\sqrt{4} = 2$ is simple, while $\sqrt{64}$ (from computing $4^3 = 64$ first) requires
recognizing a larger perfect square. When the base is a perfect $n$-th power, take the root
before applying the outer exponent.

Negative fractional exponents combine both extensions: $a^{-m/n} = \dfrac{1}{a^{m/n}} =
\dfrac{1}{\sqrt[n]{a^m}}$.

### Class Practice 2: Fractional Exponents

#### Problem

Evaluate $27^{2/3}$.

<details>
<summary>Solution</summary>

Root first, since $27$ is a perfect cube:

$$27^{2/3} = \left(27^{1/3}\right)^2 = \left(\sqrt[3]{27}\right)^2 = 3^2 = 9$$

The answer is **$9$**.

</details>

### Class Practice 3: Negative Fractional Exponents

#### Problem

Evaluate $16^{-3/4}$.

<details>
<summary>Solution</summary>

Handle the negative exponent first (Section 2) — take the reciprocal:

$$16^{-3/4} = \frac{1}{16^{3/4}}$$

Then the fractional exponent, root first:

$$16^{3/4} = \left(16^{1/4}\right)^3 = \left(\sqrt[4]{16}\right)^3 = 2^3 = 8$$

$$16^{-3/4} = \frac{1}{8}$$

The answer is **$\dfrac{1}{8}$**.

</details>

## 4. Common Mistakes

### 4.1 Thinking $a^0 = 0$

$a^0 = 1$ for any $a \ne 0$ — it comes from $\dfrac{a^n}{a^n} = 1$, not from "anything times
zero." $0^0$ itself is left undefined, which is a different situation from $a^0$ with a
nonzero base.

### 4.2 Thinking a negative exponent makes the value negative

$a^{-k} = \dfrac{1}{a^k}$ is a **reciprocal**, not a sign flip: $2^{-3} = \dfrac{1}{8}$, a
positive number. The base's own sign (Lesson 5, Reading Example in Section 1) is what
controls whether the result is positive or negative — the exponent's sign only controls
whether the power sits in the numerator or the denominator.

### 4.3 Forgetting which order is easier for fractional exponents

$a^{m/n}$ can be computed as $\left(\sqrt[n]{a}\right)^m$ or $\sqrt[n]{a^m}$ — both are
correct, but computing $a^m$ first (Class Practice 2's $27^2 = 729$, then $\sqrt[3]{729}$)
is needless extra work compared to taking the root first ($\sqrt[3]{27} = 3$, then $3^2$).
Take the root first whenever the base is a recognizable perfect power.

## 5. Key Takeaways

- **Zero exponent:** $a^0 = 1$ for $a \ne 0$ — forced by $\dfrac{a^n}{a^n} = a^{n-n} = a^0$
  and $\dfrac{a^n}{a^n} = 1$ agreeing with each other.
- **Negative exponent:** $a^{-k} = \dfrac{1}{a^k}$ for $a \ne 0$ — forced by the quotient
  rule when the denominator's exponent is larger, and it means "reciprocal," not "negative."
- **Fractional exponent:** $a^{1/n} = \sqrt[n]{a}$ — forced by demanding
  $\left(a^{1/n}\right)^n = a$ — and more generally $a^{m/n} = \left(\sqrt[n]{a}\right)^m =
  \sqrt[n]{a^m}$.
- All four Lesson 5 rules (product, power of a power, power of a product/quotient, quotient
  of powers) hold for every real-number exponent — zero, negative, or fractional — with no
  extra cases to memorize.
- Fractional exponents connect directly back to [Lesson 3](./03-irrational-numbers.md): a
  root like $2^{1/2} = \sqrt{2}$ is often irrational, even when the base is a whole number.

Next lesson moves to Weeks 5–6 of the syllabus ([00-syllabus.md](./00-syllabus.md)):
scientific notation, which relies on powers of $10$ — including the negative exponents
defined here — to represent very large and very small quantities.
