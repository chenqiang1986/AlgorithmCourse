# Lesson 7: Scientific Notation

This lesson finishes Weeks 5–6 of the syllabus ([00-syllabus.md](./00-syllabus.md)):
scientific notation. It uses powers of $10$ — including the negative and zero exponents
from [Lesson 6](./06-zero-negative-fractional-exponents.md) — to write very large and very
small numbers compactly, and shows how the Lesson 5 exponent rules make arithmetic on those
numbers manageable.

## 1. Why Powers of 10?

Ordinary decimal notation is unwieldy at the extremes. The distance from Earth to the Sun is
about

$$149{,}600{,}000{,}000 \text{ meters}$$

and the mass of a hydrogen atom is about

$$0.00000000000000000000000000167 \text{ kg}$$

Both numbers are hard to read, hard to compare, and easy to mistype (miscount a zero and the
value is off by a factor of $10$). Multiplying $10$ by itself shifts a decimal point one place
to the right; dividing by $10$ shifts it one place to the left
([Lesson 6, Section 2](./06-zero-negative-fractional-exponents.md#2-negative-exponent)). Scientific
notation uses that shift to record only two things: the digits that matter, and how many places
the decimal point moved.

## 2. The Definition

A number is in **scientific notation** when it is written as

$$a \times 10^n$$

where $1 \le |a| < 10$ (a single nonzero digit before the decimal point) and $n$ is an integer.

$$149{,}600{,}000{,}000 = 1.496 \times 10^{11} \qquad \qquad 0.00000000000000000000000000167 = 1.67 \times 10^{-27}$$

**Converting from standard form:** count how many places the decimal point moves to land
just after the first nonzero digit. Moving it left (a large number) gives a **positive**
exponent; moving it right (a small number) gives a **negative** exponent.

$$45{,}000 = 4.5 \times 10^{4} \qquad (\text{point moved 4 places left})$$

$$0.0032 = 3.2 \times 10^{-3} \qquad (\text{point moved 3 places right})$$

**Converting to standard form:** run the same count in reverse — a positive exponent moves
the decimal point right (pad with zeros if needed), a negative exponent moves it left.

$$6.02 \times 10^{5} = 602{,}000 \qquad \qquad 6.02 \times 10^{-5} = 0.0000602$$

### Reading Example: Checking the $1 \le |a| < 10$ Condition

Is $35.2 \times 10^{6}$ in scientific notation? Is $0.52 \times 10^{6}$?

Neither is — $35.2$ is not less than $10$, and $0.52$ is not at least $1$. Both need to be
rewritten by shifting the decimal point in $a$ and adjusting the exponent to compensate,
using the power-of-a-power idea from [Lesson 5, Section 3](./05-exponent-rules.md#3-power-of-a-power-amn--amn):

$$35.2 \times 10^6 = 3.52 \times 10^1 \times 10^6 = 3.52 \times 10^{1+6} = 3.52 \times 10^7$$

$$0.52 \times 10^6 = 5.2 \times 10^{-1} \times 10^6 = 5.2 \times 10^{-1+6} = 5.2 \times 10^5$$

**Non-obvious detail:** shifting the decimal point one place left in $a$ is the same as
dividing $a$ by $10$, so the exponent must increase by $1$ to compensate (and shifting right
divides the exponent's job the other way) — this is exactly the product-of-powers rule
($10^1 \times 10^6 = 10^{1+6}$) running in the background every time $a$ is renormalized.

## 3. Multiplying and Dividing in Scientific Notation

To multiply, multiply the $a$-parts and add the exponents (product of powers,
[Lesson 5, Section 2](./05-exponent-rules.md#2-product-of-powers-am--an--amn)); to divide,
divide the $a$-parts and subtract the exponents (quotient of powers,
[Lesson 5, Section 5](./05-exponent-rules.md#5-quotient-of-powers-dfracaman--am-n-for-m--n-a--0)).
If the resulting $a$-part falls outside $[1, 10)$, renormalize as in the Reading Example above.

$$(3 \times 10^4) \times (2 \times 10^5) = (3 \times 2) \times 10^{4+5} = 6 \times 10^9$$

$$(8 \times 10^7) \div (4 \times 10^3) = (8 \div 4) \times 10^{7-3} = 2 \times 10^4$$

### Reading Example: Multiplying With Renormalization

Compute $(4 \times 10^6) \times (5 \times 10^3)$.

$$(4 \times 10^6) \times (5 \times 10^3) = (4 \times 5) \times 10^{6+3} = 20 \times 10^9$$

$20$ is not less than $10$, so renormalize the same way as Section 2's Reading Example:

$$20 \times 10^9 = 2.0 \times 10^1 \times 10^9 = 2.0 \times 10^{10}$$

**Non-obvious detail:** the exponent rule (product of powers) always applies cleanly to the
$10^n$ parts — it's only the $a$-parts, which are ordinary decimal multiplication, that can
push the result out of range and require a follow-up renormalization step.

### Class Practice 1: Dividing in Scientific Notation

#### Problem

Compute $(9 \times 10^{-3}) \div (3 \times 10^{5})$, giving the answer in scientific notation.

<details>
<summary>Solution</summary>

Divide the $a$-parts, subtract the exponents (Lesson 5, Section 5, now extended to negative
results by Lesson 6, Section 2):

$$(9 \times 10^{-3}) \div (3 \times 10^{5}) = (9 \div 3) \times 10^{-3-5} = 3 \times 10^{-8}$$

$3$ is already in $[1, 10)$, so no renormalization is needed.

The answer is **$3 \times 10^{-8}$**.

</details>

## 4. Adding and Subtracting in Scientific Notation

Addition and subtraction have no exponent rule to fall back on — $10^m + 10^n \ne 10^{m+n}$
in general. Instead, rewrite both numbers with the **same exponent** first (so the digits
line up the way they would in standard decimal addition), add or subtract the $a$-parts, then
renormalize if needed.

$$3 \times 10^5 + 4.2 \times 10^5 = (3 + 4.2) \times 10^5 = 7.2 \times 10^5$$

$$5 \times 10^6 + 3 \times 10^4 = 5 \times 10^6 + 0.03 \times 10^6 = (5 + 0.03) \times 10^6 = 5.03 \times 10^6$$

In the second line, $3 \times 10^4$ was rewritten as $0.03 \times 10^6$ by shifting its
decimal point left $2$ places and raising its exponent from $4$ to $6$ to compensate — the
same compensating move as Section 2's Reading Example, just run to match a target exponent
instead of to reach $[1, 10)$.

### Class Practice 2: Adding With Different Exponents

#### Problem

Compute $6.4 \times 10^{8} + 5 \times 10^{7}$, giving the answer in scientific notation.

<details>
<summary>Solution</summary>

Rewrite $5 \times 10^7$ with exponent $8$ to match: shifting its decimal point left $1$
place raises the exponent from $7$ to $8$:

$$5 \times 10^7 = 0.5 \times 10^8$$

Now add the $a$-parts:

$$6.4 \times 10^8 + 0.5 \times 10^8 = (6.4 + 0.5) \times 10^8 = 6.9 \times 10^8$$

$6.9$ is already in $[1, 10)$, so this is the final answer.

The answer is **$6.9 \times 10^8$**.

</details>

## 5. Real-World Conversions

Scientific notation is most useful when comparing measurements that span many orders of
magnitude — the whole point of the unit's essential question. Two common tasks:

- **Comparing sizes:** to compare $3.2 \times 10^8$ and $5 \times 10^7$, compare exponents
  first ($8 > 7$, so the first number is larger by roughly a factor of $10$), then use the
  $a$-parts only to compare numbers that share an exponent.
- **Scaling a quantity:** dividing one scientific-notation quantity by another (Section 3)
  answers "how many times bigger/smaller," directly, without first expanding either number
  back to standard form.

### Class Practice 3: Comparing and Scaling

#### Problem

A red blood cell is about $7 \times 10^{-6}$ meters across. A human hair is about
$7 \times 10^{-5}$ meters across. About how many times wider is a human hair than a red blood
cell?

<details>
<summary>Solution</summary>

"How many times wider" is a division (Section 3):

$$\frac{7 \times 10^{-5}}{7 \times 10^{-6}} = (7 \div 7) \times 10^{-5-(-6)} = 1 \times 10^{1} = 10$$

The answer is **$10$** — a human hair is about $10$ times wider than a red blood cell.

</details>

## 6. Common Mistakes

### 6.1 Adding exponents when adding (not multiplying) numbers

$3 \times 10^5 + 4 \times 10^5$ is **not** $7 \times 10^{10}$ — the product-of-powers rule
(Section 3) only applies when multiplying. Addition requires matching exponents first
(Section 4) and adding only the $a$-parts, leaving the shared exponent unchanged.

### 6.2 Leaving the $a$-part outside $[1, 10)$

$20 \times 10^9$ and $0.4 \times 10^{-3}$ are not in scientific notation, even though they
are numerically correct — see Section 2's Reading Example for how to renormalize by shifting
the decimal point in $a$ and adjusting the exponent to compensate.

### 6.3 Forgetting to compensate the exponent when renormalizing

Shifting the decimal point in $a$ one place left divides $a$ by $10$, so the exponent must
**increase** by $1$ to keep the overall value the same — shifting it right does the opposite.
Changing $a$ without adjusting $n$ silently changes the value of the whole expression.

## 7. Key Takeaways

- **Scientific notation:** $a \times 10^n$ with $1 \le |a| < 10$ and $n$ an integer —
  compact notation for very large or very small numbers, built on the negative and zero
  exponents from [Lesson 6](./06-zero-negative-fractional-exponents.md).
- **Multiply/divide:** multiply or divide the $a$-parts, add or subtract the exponents
  (Lesson 5's product and quotient rules), then renormalize if $a$ falls outside $[1, 10)$.
- **Add/subtract:** first rewrite both numbers with the same exponent, then add or subtract
  only the $a$-parts — there is no shortcut through the exponents themselves.
- Comparing exponents alone tells you which of two scientific-notation numbers is roughly
  larger; dividing gives the exact scale factor between them.

[Next lesson](./08-single-variable-linear-equations.md) moves to Unit 2 of the syllabus
([00-syllabus.md](./00-syllabus.md)): simplifying expressions using the distributive
property and combining like terms, then solving single-variable linear equations.
