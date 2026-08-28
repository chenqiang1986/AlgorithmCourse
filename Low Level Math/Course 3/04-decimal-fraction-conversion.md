# Lesson 4: Converting Between Decimals and Fractions
*Low Level Math / Course 3*

[Lesson 3](./03-irrational-numbers.md) defined a rational number as anything writable as
$\dfrac{p}{q}$, and used the *fact* that terminating and repeating decimals are rational
without showing why. This lesson fills that gap: how to convert a fraction into a decimal
— both the terminating and the repeating kind — and then how to convert a decimal back into
a fraction.

## 1. Fractions to Decimals

Since $\dfrac{a}{b}$ means $a \div b$ ([Course 3, Lesson 3](./03-irrational-numbers.md);
[Course 2, Lesson 5](../Course%202/05-fraction-multiplication-division.md)), long division
turns a fraction directly into a decimal.

### 1.1 Terminating Decimals

Sometimes the division reaches a remainder of $0$ and stops — a **terminating decimal**:

$$\frac{3}{8} = 3 \div 8 = 0.375$$

### Reading Example: Long Division to a Terminating Decimal

Convert $\dfrac{7}{20}$ to a decimal.

| Step | Bring down | Divide | Quotient digit | Remainder |
|---|---|---|---|---|
| 1 | $70$ | $70 \div 20$ | $3$ | $10$ |
| 2 | $100$ | $100 \div 20$ | $5$ | $0$ |

Bring down a $0$, divide, repeat — once the remainder hits $0$ (step 2), there's nothing
left to bring down, so the decimal stops: $\dfrac{7}{20} = 0.35$.

### 1.2 Repeating Decimals

Other times the remainder is never $0$. Since dividing by $b$ can only ever produce a
remainder from $0$ to $b - 1$, a nonzero remainder must eventually **repeat** one it already
saw — and once a remainder reappears, the exact same sequence of digits it produced before
starts over, forever. That's a **repeating decimal**, written with a bar over the repeating
block.

### Reading Example: Long Division to a Repeating Decimal

Convert $\dfrac{5}{6}$ to a decimal.

| Step | Bring down | Divide | Quotient digit | Remainder |
|---|---|---|---|---|
| 1 | $50$ | $50 \div 6$ | $8$ | $2$ |
| 2 | $20$ | $20 \div 6$ | $3$ | $2$ |

At step 2 the remainder ($2$) matches the remainder from step 1 — from here on, "bring down
$20$, get digit $3$, remainder $2$" repeats forever. So the digit $3$ repeats endlessly after
the $8$:

$$\frac{5}{6} = 0.8333\ldots = 0.8\overline{3}$$

**Non-obvious detail:** only the digits produced *after* a remainder repeats belong inside
the bar. The $8$ is produced at step 1, before any remainder has repeated yet, so it sits
outside the bar as a one-digit prefix; the $3$ at step 2 is produced by the remainder ($2$)
that cycles forever afterward, which is why only the $3$ repeats.

### 1.3 Predicting Which Fractions Terminate

Whether the division terminates can be predicted without doing it. A fraction in lowest
terms produces a terminating decimal exactly when its denominator's only prime factors are
$2$ and $5$ — the two primes that divide evenly into powers of $10$. Any other prime factor
in the denominator (like $3$, $7$, or $11$) guarantees a nonzero remainder never hits $0$, so
the decimal repeats instead.

$$\frac{7}{20}: \quad 20 = 2^2 \times 5 \ \longrightarrow \ \text{terminates} \qquad \qquad \frac{5}{6}: \quad 6 = 2 \times 3 \ \longrightarrow \ \text{repeats (the leftover 3)}$$

## 2. Decimals to Fractions

### 2.1 Terminating Decimals to Fractions

Every decimal place is a power of $10$ in the denominator: the first place after the point
is tenths ($\dfrac{1}{10}$), the second is hundredths ($\dfrac{1}{100}$), and so on. A
terminating decimal converts directly: write the digits after the decimal point as the
numerator, and a power of $10$ with as many zeros as there are decimal places as the
denominator, then reduce.

$$0.75 = \frac{75}{100} = \frac{3}{4}$$

### Reading Example: A Three-Place Decimal

Convert $0.024$ to a fraction in simplest form.

There are $3$ digits after the decimal point, so the denominator is $1000$:

$$0.024 = \frac{24}{1000}$$

Reduce by canceling the shared factor: $24 = 8 \times 3$ and $1000 = 8 \times 125$, so:

$$\frac{24}{1000} = \frac{3}{125}$$

**Non-obvious detail:** the *number of zeros* in the denominator always matches the *number
of digits* after the decimal point, not the number of nonzero digits — $0.024$ has $3$
decimal places (including the leading $0$), so the denominator is $1000$, not $100$.

### 2.2 Pure Repeating Decimals to Fractions

Converting a repeating decimal to a fraction uses algebra, not long division — the key trick
is multiplying by a power of $10$ that shifts the decimal point exactly one repeating block
over, so subtracting cancels the infinite part.

**Worked derivation for $x = 0.\overline{3}$:**

$$
\begin{aligned}
x &= 0.3333\ldots \\
10x &= 3.3333\ldots &&\text{(multiply by 10 — one repeating digit, shift one place)} \\
10x - x &= 3.3333\ldots - 0.3333\ldots \\
9x &= 3 \\
x &= \frac{3}{9} = \frac{1}{3}
\end{aligned}
$$

Subtracting lines up every repeating digit after the point and cancels them exactly, because
both $10x$ and $x$ repeat the same block forever — only the finite part, $3$, survives on the
right.

**Core template:** for a purely repeating decimal with a block of length $k$, multiply by
$10^k$, subtract the original, and solve for $x$:

$$10^k x - x = (\text{the repeating block as a whole number}) \qquad \Longrightarrow \qquad x = \frac{\text{repeating block}}{\underbrace{99\ldots9}_{k \text{ nines}}}$$

### Reading Example: A Two-Digit Repeating Block

Convert $0.\overline{45}$ to a fraction.

The repeating block ($45$) has length $k = 2$, so multiply by $10^2 = 100$:

$$
\begin{aligned}
x &= 0.454545\ldots \\
100x &= 45.454545\ldots \\
100x - x &= 45 \\
99x &= 45 \\
x &= \frac{45}{99} = \frac{5}{11}
\end{aligned}
$$

**Non-obvious detail:** the power of $10$ must match the *length of the repeating block*,
not just "multiply by $10$." Using $10x$ here (a single shift) would misalign the repeat, and
the subtraction wouldn't cancel the infinite part cleanly.

### Reading Example: A Three-Digit Repeating Block

Convert $0.\overline{135}$ to a fraction.

The repeating block ($135$) has length $k = 3$, so multiply by $10^3 = 1000$:

$$
\begin{aligned}
x &= 0.135135135\ldots \\
1000x &= 135.135135\ldots \\
1000x - x &= 135 \\
999x &= 135 \\
x &= \frac{135}{999}
\end{aligned}
$$

Reduce: $135 = 27 \times 5$ and $999 = 27 \times 37$, so:

$$x = \frac{135}{999} = \frac{5}{37}$$

**Non-obvious detail:** the denominator before reducing is always a string of $k$ nines —
here $999$, three of them, matching the block length — regardless of what the repeating
digits are.

### Reading Example: A Repeating Decimal Already in Simplest Form

Convert $0.\overline{7}$ to a fraction.

One repeating digit, so multiply by $10$:

$$
\begin{aligned}
x &= 0.7777\ldots \\
10x &= 7.7777\ldots \\
10x - x &= 7 \\
9x &= 7 \\
x &= \frac{7}{9}
\end{aligned}
$$

$7$ and $9$ share no common factor, so $\dfrac{7}{9}$ is already in simplest form — not
every conversion needs a reducing step (compare $0.\overline{45} = \dfrac{45}{99}$ above,
which did).

### Reading Example: The Curious Case of $0.\overline{9}$

Convert $0.\overline{9}$ to a fraction.

$$
\begin{aligned}
x &= 0.9999\ldots \\
10x &= 9.9999\ldots \\
10x - x &= 9 \\
9x &= 9 \\
x &= \frac{9}{9} = 1
\end{aligned}
$$

The template says $0.\overline{9} = 1$ exactly — not "approximately $1$," and not "just
under $1$." $0.\overline{9}$ is simply another way of writing the whole number $1$, the same
way $\dfrac{2}{2}$ is another way of writing $1$. This is a special case worth noticing, not
a flaw in the method: whenever the algebra produces a result whose numerator equals its
denominator (or whose fraction reduces to an integer), the "repeating" decimal was secretly
naming a number with a terminating (or whole-number) value all along.

### 2.3 Repeating Decimals With a Non-Repeating Prefix

A decimal like $0.8\overline{3}$ has a digit ($8$) that *doesn't* repeat, sitting in front of
the block that does. Rather than a new technique, this **splits into a piece already
covered**: a terminating decimal (Section 2.1) plus a shifted-down pure repeating decimal
(Section 2.2), added together.

**Step 1 — split off the non-repeating part as addition.** $0.8\overline{3}$ is $0.8$ plus
"$0.0\overline{3}$" — the repeating part, pushed one place further right:

$$0.8\overline{3} = 0.8 + 0.0\overline{3}$$

**Step 2 — write the shifted piece as the pure-repeating decimal divided by a power of 10.**
Shifting $0.\overline{3}$ one place to the right is the same as dividing it by $10$:

$$0.0\overline{3} = \frac{0.\overline{3}}{10}$$

$$0.8\overline{3} = 0.8 + \frac{0.\overline{3}}{10}$$

**Step 3 — apply the pure-repeating core template (Section 2.2) to convert
$0.\overline{3}$**, and write $0.8$ as a fraction (Section 2.1):

$$0.8\overline{3} = \frac{4}{5} + \frac{3/9}{10}$$

**Step 4 — simplify the second term, then add using the fraction rules from
[Course 2, Lesson 6](../Course%202/06-fraction-addition.md).** Dividing $\dfrac{3}{9}$ by
$10$ multiplies its denominator by $10$:

$$\frac{3/9}{10} = \frac{3}{90} = \frac{1}{30}$$

$$0.8\overline{3} = \frac{4}{5} + \frac{1}{30} = \frac{24}{30} + \frac{1}{30} = \frac{25}{30} = \frac{5}{6}$$

This matches the $\dfrac{5}{6}$ the long division started from in Section 1.2 — converting a
decimal to a fraction and a fraction to a decimal are exact inverses of each other.

**Core template:** for a decimal with $n$ non-repeating digits after the point followed by a
repeating block of length $k$, split it into a terminating part and a shifted pure-repeating
part, then add:

$$0.\underbrace{d_1 \ldots d_n}_{n \text{ digits}}\overline{\underbrace{r_1 \ldots r_k}_{k \text{ digits}}} = \underbrace{\frac{d_1 \ldots d_n}{10^n}}_{\text{terminating part}} + \underbrace{\frac{r_1 \ldots r_k}{\underbrace{9\ldots9}_{k \text{ nines}} \times 10^n}}_{\text{shifted repeating part}}$$

### Reading Example: A Two-Digit Repeating Block With a One-Digit Prefix

Convert $0.2\overline{45}$ to a fraction.

Split off the non-repeating digit ($n = 1$) from the repeating block ($k = 2$):

$$0.2\overline{45} = 0.2 + \frac{0.\overline{45}}{10} = \frac{1}{5} + \frac{45/99}{10} = \frac{1}{5} + \frac{45}{990}$$

Reduce the second fraction first: $45 = 45 \times 1$ and $990 = 45 \times 22$, so
$\dfrac{45}{990} = \dfrac{1}{22}$. Add using a common denominator of $110$:

$$\frac{1}{5} + \frac{1}{22} = \frac{22}{110} + \frac{5}{110} = \frac{27}{110}$$

**Non-obvious detail:** the denominator of the shifted repeating part is always
$\underbrace{9\ldots9}_{k} \times 10^n$ — here $99 \times 10 = 990$ — combining Section 2.2's
"$k$ nines" with a "$10^n$" for however many places the block was pushed over.

### Reading Example: A One-Digit Repeating Block With a Two-Digit Prefix

Convert $0.13\overline{6}$ to a fraction.

Split off the two non-repeating digits ($n = 2$) from the repeating block ($k = 1$):

$$0.13\overline{6} = 0.13 + \frac{0.\overline{6}}{100} = \frac{13}{100} + \frac{6/9}{100} = \frac{13}{100} + \frac{6}{900}$$

Reduce the second fraction: $6 = 6 \times 1$ and $900 = 6 \times 150$, so $\dfrac{6}{900} =
\dfrac{1}{150}$. Add using a common denominator of $300$:

$$\frac{13}{100} + \frac{1}{150} = \frac{39}{300} + \frac{2}{300} = \frac{41}{300}$$

Checking against long division confirms it: $41 \div 300 = 0.136666\ldots = 0.13\overline{6}$.

## 3. Class Practice 1: Fraction to Terminating Decimal

### Problem

Without dividing, determine whether $\dfrac{11}{40}$ terminates. Then find its decimal
value.

<details>
<summary>Solution</summary>

Factor the denominator: $40 = 2^3 \times 5$ — only $2$s and $5$s, so it terminates. Long
division:

$$\frac{11}{40} = 11 \div 40 = 0.275$$

The answer is **$0.275$**.

</details>

## 4. Class Practice 2: Fraction to Repeating Decimal

### Problem

Convert $\dfrac{2}{3}$ to a decimal, and explain why it doesn't terminate.

<details>
<summary>Solution</summary>

The denominator $3$ is not $2$ or $5$, so (Section 1.3) the decimal must repeat. Long
division: $20 \div 3 = 6$ remainder $2$, and that remainder $2$ repeats every step, so the
digit $6$ repeats forever:

$$\frac{2}{3} = 0.6666\ldots = 0.\overline{6}$$

The answer is **$0.\overline{6}$**.

</details>

## 5. Class Practice 3: Terminating Decimal to Fraction

### Problem

Convert $0.625$ to a fraction in simplest form.

<details>
<summary>Solution</summary>

Three decimal places, so the denominator is $1000$:

$$0.625 = \frac{625}{1000}$$

Reduce: $625 = 125 \times 5$ and $1000 = 125 \times 8$, so:

$$\frac{625}{1000} = \frac{5}{8}$$

The answer is **$\dfrac{5}{8}$**.

</details>

## 6. Class Practice 4: Repeating Decimal to Fraction

### Problem

Convert $0.\overline{27}$ to a fraction in simplest form.

<details>
<summary>Solution</summary>

The repeating block ($27$) has length $k = 2$, so multiply by $100$:

$$
\begin{aligned}
x &= 0.272727\ldots \\
100x &= 27.272727\ldots \\
100x - x &= 27 \\
99x &= 27 \\
x &= \frac{27}{99} = \frac{3}{11}
\end{aligned}
$$

The answer is **$\dfrac{3}{11}$**.

</details>

## 7. Common Mistakes

### 7.1 Using the wrong power of 10

The multiplier must match the length of the repeating block: a $1$-digit repeat needs
$\times 10$, a $2$-digit repeat needs $\times 100$, and so on. Using $\times 10$ on a
$2$-digit block (like $0.\overline{45}$) misaligns the subtraction and produces a wrong
fraction.

### 7.2 Forgetting to reduce

$0.75 = \dfrac{75}{100}$ and $0.\overline{27} = \dfrac{27}{99}$ are both correct but
unreduced — always cancel the shared factor to reach simplest form, as in
[Course 2, Lesson 6, Section 6](../Course%202/06-fraction-addition.md).

### 7.3 Applying the pure-repeat template to a mixed decimal

$0.8\overline{3}$ is **not** $\dfrac{83}{99}$ — that template only works when the repeating
block starts *immediately* after the decimal point. A non-repeating prefix needs the
split-and-add approach instead (Section 2.3): peel off the non-repeating part first, convert
only the repeating part with the pure-repeat template, then add the two fractions.

### 7.4 Forgetting to shift the repeating part's denominator

In Section 2.3's split, the repeating part isn't just $\dfrac{\text{block}}{9\ldots9}$ — it
also gets divided by $10^n$ for however many non-repeating digits came before it. Skipping
that extra $10^n$ (e.g. using $\dfrac{3}{9}$ instead of $\dfrac{3}{90}$ for $0.8\overline{3}$)
gives a fraction for the wrong decimal.

### 7.5 Stopping long division too early

A remainder has to actually **repeat** before it's safe to conclude the decimal is
repeating with that block — stopping after just one or two digits risks mistaking the start
of a longer repeating block for a short one. Keep dividing until the same remainder shows up
a second time (Section 1.2).

## 8. Key Takeaways

- A fraction converts to a decimal by long division; the decimal terminates once a remainder
  of $0$ appears, or repeats forever once a nonzero remainder reappears.
- A fraction in lowest terms terminates exactly when its denominator's only prime factors
  are $2$ and $5$ — any other prime factor forces a repeating decimal.
- A terminating decimal converts back to a fraction directly: digits after the point over a
  power of $10$ with matching zeros, then reduced.
- A purely repeating decimal converts back via algebra: let $x$ equal the decimal, multiply
  by $10^k$ (where $k$ is the repeat length) to shift one full block, subtract $x$, and
  solve.
- A repeating decimal with a non-repeating prefix splits into a terminating part plus the
  pure-repeating part shifted down by $10^n$ ($n$ = prefix length), then the two fractions
  are added together.

Next lesson moves to Weeks 3–4 of the syllabus ([00-syllabus.md](./00-syllabus.md)): the laws
of exponents.
