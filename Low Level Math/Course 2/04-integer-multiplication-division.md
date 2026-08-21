# Lesson 4: Integer Multiplication and Division

[Lesson 3](./03-negative-integers-addition-subtraction.md) covered adding and subtracting
negative integers. This lesson covers the sign rules for **multiplying** and **dividing**
integers, and *why* those rules — especially "negative times negative is positive" — are
true rather than arbitrary.

## 1. Where the Sign Rules Come From

Multiplication by a positive integer is repeated addition, and that idea still works when
the other factor is negative:

$$3 \times (-2) = (-2) + (-2) + (-2) = -6$$

So **positive $\times$ negative $=$ negative** — that much follows directly from repeated
addition. But repeated addition doesn't obviously explain $(-3) \times (-2)$: you can't
add something $-3$ times. Instead, look at a pattern that's already known to be true, and
extend it:

$$
\begin{aligned}
3 \times (-2) &= -6 \\
2 \times (-2) &= -4 \\
1 \times (-2) &= -2 \\
0 \times (-2) &= 0 \\
-1 \times (-2) &= \;? \\
-2 \times (-2) &= \;?
\end{aligned}
$$

Each time the first factor drops by $1$, the product goes *up* by $2$. Continuing that
pattern below $0$ forces $-1 \times (-2) = 2$ and $-2\times(-2) = 4$ — the only values
consistent with the pattern already established. So negative $\times$ negative must be
positive; it isn't a separate rule someone invented, it's the value that keeps
multiplication's own pattern consistent.

## 2. Core Template: Sign Rules for Multiplication and Division

**Multiplication and division follow the same sign rule:**

| Signs of the two numbers | Sign of the result |
|---|---|
| Same sign (both $+$ or both $-$) | Positive |
| Different signs (one $+$, one $-$) | Negative |

Find the sign first using the table, then multiply or divide the absolute values:

$$(-8) \times (-3) = +(8 \times 3) = 24 \qquad \qquad (-8) \times 3 = -(8 \times 3) = -24$$

$$(-20) \div (-4) = +(20 \div 4) = 5 \qquad \qquad 20 \div (-4) = -(20 \div 4) = -5$$

**Division by zero is undefined** — no rule applies, because no number times $0$ gives a
nonzero result, and every number times $0$ gives $0$ (so there isn't a unique answer
either). This holds regardless of sign.

## 3. Reading Example: Multiplying With More Than Two Factors

Evaluate $(-2) \times 3 \times (-5)$.

Apply the sign rule pairwise, left to right. First $(-2) \times 3$: different signs, so
negative.

$$(-2) \times 3 = -6$$

Now $(-6) \times (-5)$: same sign (both negative), so positive.

$$(-6) \times (-5) = 30$$

**Non-obvious detail:** with more than two factors, a shortcut is to just count the
negative factors: an **even** count of negative factors gives a positive product, an
**odd** count gives a negative product (positive factors don't affect the sign at all).
Here there are two negative factors ($-2$ and $-5$) — an even count — matching the
positive result found above. This shortcut only tells you the *sign*; you still multiply
all the absolute values together to get the magnitude.

## 4. Reading Example: Division as the Inverse of Multiplication

Evaluate $(-45) \div 9$.

Division undoes multiplication: $(-45) \div 9$ asks "what number times $9$ gives
$-45$?" Since $9$ is positive and $-45$ is negative, that unknown number must be
negative (different signs needed to produce a negative product):

$$(-45) \div 9 = -5 \qquad \text{because} \qquad (-5) \times 9 = -45$$

**Non-obvious detail:** the sign rule for division is identical to multiplication's *because*
division is defined in terms of multiplication — $a \div b$ is the number that, multiplied
by $b$, gives $a$. There's no independent rule to memorize for division; it's inherited
directly from Section 2's multiplication table.

## 5. Class Practice 1: Multiplying Two Integers

### Problem

Evaluate: $(-7) \times (-6)$

<details>
<summary>Solution</summary>

Same sign (both negative), so the product is positive:

$$(-7) \times (-6) = +(7 \times 6) = 42$$

The answer is **$42$**.

</details>

## 6. Class Practice 2: Multiplying Several Factors

### Problem

Evaluate: $(-1) \times (-4) \times (-5) \times 2$

<details>
<summary>Solution</summary>

Count the negative factors: $-1$, $-4$, $-5$ — three negative factors, which is odd, so
the product is negative. Multiply the absolute values:

$$1 \times 4 \times 5 \times 2 = 40$$

Applying the negative sign:

$$(-1) \times (-4) \times (-5) \times 2 = -40$$

The answer is **$-40$**.

</details>

## 7. Class Practice 3: Division

### Problem

Evaluate: $(-72) \div (-8)$

<details>
<summary>Solution</summary>

Same sign (both negative), so the quotient is positive:

$$(-72) \div (-8) = +(72 \div 8) = 9$$

The answer is **$9$**.

</details>

## 8. Common Mistakes

### 8.1 Applying the addition sign rule to multiplication

Adding integers (Lesson 3) compares *absolute values* to pick the sign; multiplying and
dividing integers never compares absolute values — the sign depends only on whether the
signs *match*, regardless of which number is larger. $(-2) \times 100$ is negative even
though $100$ is much larger than $2$ in absolute value.

### 8.2 Losing track of the sign with three or more factors

Multiplying the absolute values correctly but guessing the final sign is a common error
in problems like $(-2)\times(-3)\times(-4)$. Count the negative factors first (three here
— odd — so the result is negative), separately from computing the magnitude
($2\times3\times4=24$), then combine: $-24$.

### 8.3 Treating $0 \div n$ and $n \div 0$ as the same

$0 \div n = 0$ for any nonzero $n$ (zero split into any number of groups is still zero in
each group), but $n \div 0$ is **undefined** for any $n$, including $n = 0$. These are not
symmetric — don't assume one follows from the other.

## 9. Key Takeaways

- Multiplying/dividing integers: same signs give a positive result, different signs give a
  negative result — this is unlike adding integers, which depends on comparing absolute
  values.
- With three or more factors, count the negative factors: an even count gives a positive
  product, an odd count gives a negative product.
- Division inherits its sign rule from multiplication, since $a \div b$ is defined as "the
  number that, times $b$, gives $a$."
- Division by $0$ is always undefined, regardless of sign.

This completes the integer operations covered in Weeks 1–4 of the syllabus
([00-syllabus.md](./00-syllabus.md)). The next unit applies these same operations to
rational decimals and fractions.
