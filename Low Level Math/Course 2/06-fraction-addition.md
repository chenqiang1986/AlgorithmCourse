# Lesson 6: Adding Fractions — Same and Different Denominators

[Lesson 5](./05-fraction-multiplication-division.md) covered fraction signs, multiplication,
and division. This lesson covers **addition**: first the easy case where two fractions
already share a denominator, then the harder case where they don't, using the idea of an
**equivalent fraction** to make the denominators match — and finally how to **reduce** the
result to simplest form.

## 1. Adding Fractions With the Same Denominator (Pizza Model)

A fraction's denominator says how many equal pieces the whole was cut into; the numerator
says how many of those pieces are shaded. If two fractions have the **same** denominator,
their pieces are already the same size — adding them just means counting up the total
number of shaded pieces, out of that same total:

![Three pizzas side by side, each cut into 8 equal wedges. The first pizza has 3 adjacent wedges shaded orange, labeled "3/8 of a pizza," with the caption "3 orange slices of 8" below it. A plus sign separates it from the second pizza, which has 2 adjacent wedges shaded blue, labeled "2/8 of a pizza," captioned "2 blue slices of 8." An equals sign separates that from the third pizza, the same size, which has 3 wedges shaded orange and 2 different wedges shaded blue — 5 shaded wedges total out of 8 — labeled "5/8 of a pizza," captioned "3 + 2 = 5 slices of 8." A line below all three reads: same-size slices — just count the total shaded slices. 3/8 + 2/8 = (3+2)/8 = 5/8.](./images/pizza-fraction-addition-same-denominator.svg)

Nothing about the pieces changes size — only the count of shaded pieces goes up. That gives
the rule: **add the numerators, keep the denominator.**

## 2. Core Template: Same-Denominator Addition

$$\frac{a}{b} + \frac{c}{b} = \frac{a + c}{b} \qquad (b \ne 0)$$

The denominator $b$ never changes — it describes the size of the pieces, and adding two
amounts of same-size pieces doesn't change how big each piece is. Only the numerators, which
count pieces, get added.

$$\frac{3}{8} + \frac{2}{8} = \frac{3+2}{8} = \frac{5}{8}$$

If a numerator is negative, the numerators still combine using the integer addition rule
from [Lesson 3](./03-negative-integers-addition-subtraction.md) — the denominator is just
along for the ride:

$$\frac{-5}{9} + \frac{2}{9} = \frac{-5+2}{9} = \frac{-3}{9} = -\frac{3}{9}$$

($-\dfrac{3}{9}$ isn't yet in simplest form — Section 6 covers how to reduce it.)

## 3. Reading Example: Same-Denominator Addition With a Negative Numerator

Evaluate $\dfrac{4}{7} + \left(-\dfrac{6}{7}\right)$.

The denominators already match ($7$), so add the numerators directly, using the integer
addition rule for $4$ and $-6$:

$$\frac{4}{7} + \left(-\frac{6}{7}\right) = \frac{4 + (-6)}{7} = \frac{-2}{7} = -\frac{2}{7}$$

**Non-obvious detail:** the denominator $7$ is written exactly once in the final answer, not
added to itself. A common slip is adding *both* parts of the fraction, giving a wrong
denominator like $14$ — but the denominator names the piece size, and the pieces didn't get
smaller or bigger, so it stays $7$.

## 4. Why Different Denominators Need Equivalent Fractions First

The same-denominator trick only works because the pieces are the same size. $\dfrac{1}{3} +
\dfrac{1}{6}$ can't be added by counting pieces directly — thirds and sixths are different
sizes, so "$1$ piece plus $1$ piece" doesn't mean anything until the pieces match.

The fix: rewrite one or both fractions using **different-sized pieces that represent the
same amount**, until the denominators match. This relies on a fact used constantly from here
on: multiplying a fraction by $\dfrac{c}{c}$ never changes its value, because $\dfrac{c}{c} =
1$ for any nonzero $c$, and multiplying by $1$ changes nothing:

$$\frac{a}{b} = \frac{a}{b} \times 1 = \frac{a}{b} \times \frac{c}{c} = \frac{a \times c}{b \times c} \qquad (c \ne 0)$$

Two fractions related this way — $\dfrac{a}{b}$ and $\dfrac{ac}{bc}$ — are called
**equivalent fractions**: different-looking fractions that name the same value.

![Two pizzas side by side, the same size. The first pizza is cut into 3 equal wedges with 1 wedge shaded orange, labeled "1/3," captioned "1 shaded slice of 3." An equals sign points to the second pizza, cut into 6 equal wedges (each of the first pizza's cuts split in half), where the same physical area — now 2 adjacent wedges — is shaded orange, labeled "2/6," captioned "2 shaded slices of 6." A line below reads: same shaded area, twice as many cuts — 1/3 = (1×2)/(3×2) = 2/6.](./images/pizza-fraction-equivalence.svg)

Cutting every piece of the pizza in half doubles both the number of shaded pieces and the
total number of pieces — the shaded *amount* of pizza never changes, only how finely it's
sliced. That's exactly $\dfrac{1}{3} \times \dfrac{2}{2} = \dfrac{1 \times 2}{3 \times 2} =
\dfrac{2}{6}$.

## 5. Core Template: Adding Fractions With Different Denominators

To add $\dfrac{a}{b} + \dfrac{c}{d}$ when $b \ne d$, use the multiply-by-$\dfrac{c}{c}$ idea
to turn both fractions into equivalent fractions with a **common denominator**. Multiplying
the first fraction's denominator by $d$ and the second's by $b$ always produces a match,
since $b \times d = d \times b$:

$$
\begin{aligned}
\frac{a}{b} + \frac{c}{d} &= \left(\frac{a}{b} \times \frac{d}{d}\right) + \left(\frac{c}{d} \times \frac{b}{b}\right) \\
&= \frac{ad}{bd} + \frac{cb}{bd} \\
&= \frac{ad + cb}{bd} \qquad \text{(Section 2: same denominator now, add the numerators)}
\end{aligned}
$$

$$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$$

**The product $b \times d$ always works as a common denominator**, even if it isn't the
smallest possible one — finding the *smallest* common denominator (the least common
multiple of $b$ and $d$) is a shortcut covered in a later lesson. For now, multiplying the
denominators together is always a safe, correct choice — Section 6 covers how to reduce the
resulting sum to simplest form.

## 6. Core Template: Reducing a Fraction to Simplest Form

Section 5's template always produces a *correct* sum, but not always the smallest-looking
one. Section 4's equivalence rule also works **in reverse**: suppose the numerator and
denominator share a common factor $c$ — that is, $a = a' \times c$ and $b = b' \times c$ for
some nonzero $c$. Then that shared factor can be split off and canceled, using the very same
$\dfrac{c}{c} = 1$ fact from Section 4, just read right to left:

$$\frac{a}{b} = \frac{a' \times c}{b' \times c} = \frac{a'}{b'} \times \frac{c}{c} = \frac{a'}{b'} \times 1 = \frac{a'}{b'}$$

Multiplying by $\dfrac{c}{c}$ built a bigger-looking equivalent fraction in Section 4;
dividing out a shared factor $c$ shrinks it back down. A fraction is in **simplest form**
(or "lowest terms") once its numerator and denominator have no common factor greater than
$1$.

For example, $a = 6 = 3 \times 2$ and $b = 8 = 4 \times 2$ share the factor $c = 2$
($a' = 3$, $b' = 4$), so:

$$\frac{6}{8} = \frac{3 \times 2}{4 \times 2} = \frac{3}{4}$$

The Section 4 pizza picture reduces the same way, read right to left: the $2$ shaded sixths
in the second pizza are the *same* physical area as the $1$ shaded third in the first, so
canceling the shared factor $c = 2$ turns $\dfrac{2}{6}$ back into $\dfrac{1}{3}$.

From here on, **reduce every fraction answer to simplest form as the last step.**

## 7. Reading Example: Adding Fractions With Different Denominators

Evaluate $\dfrac{1}{3} + \dfrac{1}{6}$ from Section 4, using the template.

Multiply each fraction so both denominators become $3 \times 6 = 18$:

$$\frac{1}{3} \times \frac{6}{6} = \frac{6}{18} \qquad \qquad \frac{1}{6} \times \frac{3}{3} = \frac{3}{18}$$

Now the denominators match, so add the numerators:

$$\frac{6}{18} + \frac{3}{18} = \frac{6+3}{18} = \frac{9}{18}$$

$\dfrac{9}{18}$ isn't yet in simplest form. Applying Section 6's rule: $9 = 1 \times 9$ and
$18 = 2 \times 9$ share the factor $c = 9$, so:

$$\frac{9}{18} = \frac{1 \times 9}{2 \times 9} = \frac{1}{2}$$

**Non-obvious detail:** Section 4's pizza picture already showed $\dfrac13 = \dfrac26$ using
denominator $6$, smaller than the $18$ this template produced — multiplying straight across
($3 \times 6$) always gives a *correct* common denominator, just not always the smallest
one. Reducing at the end (Section 6) fixes that regardless of which common denominator was
used to add: $\dfrac{9}{18}$ and $\dfrac26 + \dfrac16 = \dfrac36$ both reduce to the same
simplest form, $\dfrac12$.

## 8. Reading Example: Adding Fractions With a Negative Numerator, Different Denominators

Evaluate $-\dfrac{2}{5} + \dfrac{3}{4}$.

Multiply each fraction so both denominators become $5 \times 4 = 20$:

$$-\frac{2}{5} \times \frac{4}{4} = -\frac{8}{20} \qquad \qquad \frac{3}{4} \times \frac{5}{5} = \frac{15}{20}$$

Add the numerators using the integer addition rule:

$$-\frac{8}{20} + \frac{15}{20} = \frac{-8 + 15}{20} = \frac{7}{20}$$

$\dfrac{7}{20}$ is already in simplest form: $7$ is prime and doesn't divide $20$, so there's
no shared factor $c > 1$ to cancel (Section 6) — not every sum needs reducing.

**Non-obvious detail:** the sign only ever attaches to the numerator during this process —
$-\dfrac25$ is rewritten as $\dfrac{-8}{20}$, not $\dfrac{8}{-20}$, keeping the denominator
positive throughout so "add the numerators" (Section 2) applies without also having to track
a sign on the denominator.

## 9. Class Practice 1: Same-Denominator Addition

### Problem

Evaluate: $\dfrac{5}{9} + \dfrac{7}{9}$

<details>
<summary>Solution</summary>

The denominators already match, so add the numerators and keep the denominator:

$$\frac{5}{9} + \frac{7}{9} = \frac{5+7}{9} = \frac{12}{9}$$

$12$ and $9$ share the factor $c = 3$ ($12 = 4 \times 3$, $9 = 3 \times 3$), so reduce:

$$\frac{12}{9} = \frac{4 \times 3}{3 \times 3} = \frac{4}{3}$$

The answer is **$\dfrac{4}{3}$**.

</details>

## 10. Class Practice 2: Different-Denominator Addition

### Problem

Evaluate: $\dfrac{2}{3} + \dfrac{1}{5}$

<details>
<summary>Solution</summary>

Multiply each fraction so both denominators become $3 \times 5 = 15$:

$$\frac{2}{3} \times \frac{5}{5} = \frac{10}{15} \qquad \qquad \frac{1}{5} \times \frac{3}{3} = \frac{3}{15}$$

Add the numerators:

$$\frac{10}{15} + \frac{3}{15} = \frac{10+3}{15} = \frac{13}{15}$$

$13$ is prime and doesn't divide $15$, so $\dfrac{13}{15}$ is already in simplest form —
nothing left to reduce.

The answer is **$\dfrac{13}{15}$**.

</details>

## 11. Class Practice 3: Negative Fraction, Different Denominators

### Problem

Evaluate: $\dfrac{3}{4} + \left(-\dfrac{5}{6}\right)$

<details>
<summary>Solution</summary>

Multiply each fraction so both denominators become $4 \times 6 = 24$:

$$\frac{3}{4} \times \frac{6}{6} = \frac{18}{24} \qquad \qquad -\frac{5}{6} \times \frac{4}{4} = -\frac{20}{24}$$

Add the numerators using the integer addition rule:

$$\frac{18}{24} + \left(-\frac{20}{24}\right) = \frac{18 + (-20)}{24} = \frac{-2}{24} = -\frac{2}{24}$$

$2$ and $24$ share the factor $c = 2$ ($2 = 1 \times 2$, $24 = 12 \times 2$), so reduce:

$$-\frac{2}{24} = -\frac{1 \times 2}{12 \times 2} = -\frac{1}{12}$$

The answer is **$-\dfrac{1}{12}$**.

</details>

## 12. Common Mistakes

### 12.1 Adding the denominators together

$\dfrac{a}{b} + \dfrac{c}{d}$ is **not** $\dfrac{a+c}{b+d}$ — that isn't even true when
$b = d$ (Section 2 shows the denominator stays $b$, it doesn't double). Denominators are
never added; they're only combined by multiplying, to build a common denominator.

### 12.2 Multiplying only one side of a fraction when building the common denominator

Turning $\dfrac{a}{b}$ into an equivalent fraction requires multiplying by $\dfrac{c}{c}$ —
**both** the numerator and the denominator get multiplied by $c$. Multiplying only the
denominator (or only the numerator) changes the fraction's value instead of preserving it.

### 12.3 Adding numerators before the denominators match

The same-denominator rule (Section 2) only applies once both fractions describe same-size
pieces. Adding numerators while the denominators are still different — like turning
$\dfrac13 + \dfrac16$ straight into $\dfrac{1+1}{6}$ — skips the equivalence step and gives
a wrong answer.

### 12.4 Reducing only the numerator or only the denominator

Canceling a common factor $c$ (Section 6) means dividing **both** $a$ and $b$ by $c$ — the
same "both parts together" requirement as building an equivalent fraction, just in reverse.
Dividing only the numerator, or only the denominator, by $c$ changes the fraction's value
instead of preserving it.

## 13. Key Takeaways

- Fractions with the **same denominator** add by adding the numerators and keeping the
  denominator: $\dfrac{a}{b} + \dfrac{c}{b} = \dfrac{a+c}{b}$.
- A fraction's value doesn't change when both numerator and denominator are multiplied by
  the same nonzero number $c$, since $\dfrac{c}{c} = 1$: $\dfrac{a}{b} = \dfrac{ac}{bc}$.
  Two fractions related this way are **equivalent fractions**.
- For **different denominators**, multiply each fraction by the other fraction's
  denominator over itself to build a shared denominator, then add:
  $\dfrac{a}{b} + \dfrac{c}{d} = \dfrac{ad+bc}{bd}$.
- The product $b \times d$ always works as a common denominator, even when it isn't the
  smallest one possible.
- **Reduce every answer to simplest form** by running the equivalence rule in reverse: if
  $a = a' \times c$ and $b = b' \times c$, cancel the shared factor $c$ to get
  $\dfrac{a}{b} = \dfrac{a'}{b'}$.

Next lesson covers **subtracting fractions** — "add the opposite," the same move used for
integer subtraction in [Lesson 3](./03-negative-integers-addition-subtraction.md) — and the
**least common denominator**, a shortcut for finding a smaller common denominator than the
plain product $b \times d$ used in this lesson.
