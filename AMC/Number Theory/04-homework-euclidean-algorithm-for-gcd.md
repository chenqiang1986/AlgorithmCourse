# Homework: The Euclidean Algorithm for GCD
*AMC / Number Theory*

This homework accompanies [Lesson 4](./04-euclidean-algorithm-for-gcd.md). For each
Euclidean-algorithm calculation, write every division equation through the first
remainder of $0$. Do not factor the original numbers unless a problem specifically
asks for a check.

## Part A: Euclidean Algorithm Fluency

### Problem 1

Use the Euclidean algorithm to find $\gcd(252,105)$.

<details>
<summary>Solution</summary>

$$252=105\cdot2+42$$

$$105=42\cdot2+21$$

$$42=21\cdot2+0.$$

The last nonzero remainder is $21$, so

$$\boxed{\gcd(252,105)=21.}$$

</details>

### Problem 2

Use the Euclidean algorithm to find $\gcd(935,748)$.

<details>
<summary>Solution</summary>

$$935=748\cdot1+187$$

$$748=187\cdot4+0.$$

Thus

$$\boxed{\gcd(935,748)=187.}$$

</details>

### Problem 3

Find $\gcd(1197,432)$ using the Euclidean algorithm.

<details>
<summary>Solution</summary>

$$1197=432\cdot2+333$$

$$432=333\cdot1+99$$

$$333=99\cdot3+36$$

$$99=36\cdot2+27$$

$$36=27\cdot1+9$$

$$27=9\cdot3+0.$$

Therefore

$$\boxed{\gcd(1197,432)=9.}$$

</details>

### Problem 4

Use the Euclidean algorithm to find $\gcd(1001,143)$. What feature of the first
division makes this calculation especially short?

<details>
<summary>Solution</summary>

$$1001=143\cdot7+0.$$

Thus

$$\boxed{\gcd(1001,143)=143.}$$

The first remainder is $0$, which means $143$ divides $1001$ exactly, so the
smaller number is already the GCD.

</details>

### Problem 5

Use the Euclidean algorithm to decide whether $527$ and $221$ are relatively prime.

<details>
<summary>Solution</summary>

$$527=221\cdot2+85$$

$$221=85\cdot2+51$$

$$85=51\cdot1+34$$

$$51=34\cdot1+17$$

$$34=17\cdot2+0.$$

The GCD is $17$, not $1$, so $527$ and $221$ are **not** relatively prime.

</details>

### Problem 6

Use the Euclidean algorithm to decide whether $415$ and $252$ are relatively prime.

<details>
<summary>Solution</summary>

$$415=252\cdot1+163$$

$$252=163\cdot1+89$$

$$163=89\cdot1+74$$

$$89=74\cdot1+15$$

$$74=15\cdot4+14$$

$$15=14\cdot1+1$$

$$14=1\cdot14+0.$$

The last nonzero remainder is $1$, so

$$\gcd(415,252)=1.$$

Therefore the numbers are relatively prime.

</details>

## Part B: GCDs, LCMs, and Remainders

### Problem 7

Use the Euclidean algorithm, then the product formula, to find
$\operatorname{lcm}(378,280)$.

<details>
<summary>Solution</summary>

First find the GCD:

$$378=280\cdot1+98$$

$$280=98\cdot2+84$$

$$98=84\cdot1+14$$

$$84=14\cdot6+0.$$

Thus $\gcd(378,280)=14$. Therefore

$$\operatorname{lcm}(378,280)=\frac{378\cdot280}{14}=378\cdot20=\boxed{7560}. $$

</details>

### Problem 8

An incorrect calculation says

$$187=73\cdot2+41,$$

then replaces the pair $(187,73)$ with $(2,41)$. Explain the error and state the
correct next pair.

<details>
<summary>Solution</summary>

The next pair in the Euclidean algorithm is always **(divisor, remainder)**, not
(quotient, remainder). Here the divisor is $73$ and the remainder is $41$, so the
correct next pair is

$$\boxed{(73,41)}.$$

</details>

### Problem 9

Suppose $a=bq+r$, where $a,b,q,r$ are integers and $0\le r<b$. Explain why every
common divisor of $a$ and $b$ also divides $r$.

<details>
<summary>Solution</summary>

If $d$ divides both $a$ and $b$, then $d\mid bq$ as well. Since

$$r=a-bq,$$

and $d$ divides both terms on the right, it divides their difference. Therefore

$$d\mid r.$$

This is one direction of the key fact $\gcd(a,b)=\gcd(b,r)$.

</details>

### Problem 10

The Euclidean algorithm for two positive integers ends with

$$65=26\cdot2+13$$

$$26=13\cdot2+0.$$

What is their GCD? Must the original two numbers both be divisible by $13$? Explain.

<details>
<summary>Solution</summary>

The last nonzero remainder is $13$, so the GCD is $13$. The algorithm preserves the
set of common divisors at every step, so the GCD divides both original numbers.
Therefore both original numbers must be divisible by $13$.

</details>

## Part C: Applications

### Problem 11

A school has $168$ vanilla cupcakes and $252$ chocolate cupcakes. It wants to make
the greatest possible number of identical boxes, using every cupcake. How many boxes
can it make, and how many cupcakes of each flavor go in each box?

<details>
<summary>Solution</summary>

Find the GCD:

$$252=168\cdot1+84$$

$$168=84\cdot2+0.$$

The school can make $84$ boxes. Each box contains

$$168\div84=2$$

vanilla cupcakes and

$$252\div84=3$$

chocolate cupcakes.

</details>

### Problem 12

A $231$ cm by $154$ cm rectangular sheet is cut into the largest possible equal
squares with no waste. Find the side length of each square and the number of squares
produced.

<details>
<summary>Solution</summary>

The side length is $\gcd(231,154)$:

$$231=154\cdot1+77$$

$$154=77\cdot2+0.$$

Each square has side length $77$ cm. The sheet has

$$\frac{231}{77}=3$$

squares along one side and

$$\frac{154}{77}=2$$

along the other, for a total of

$$\boxed{3\cdot2=6\text{ squares}}.$$

</details>

### Problem 13

Fractions $\frac{a}{630}$ and $\frac{b}{630}$ are each reduced **to lowest terms** by
dividing numerator and denominator by $90$. What does this tell you about
$\gcd(a,630)$ and $\gcd(b,630)$? Explain.

<details>
<summary>Solution</summary>

For a fraction to be reduced fully by dividing its numerator and denominator by $90$,
that number must be the greatest common divisor of the numerator and denominator.
Therefore

$$\boxed{\gcd(a,630)=90\quad\text{and}\quad\gcd(b,630)=90.}$$

</details>

## Part D: Challenge Reasoning

### Problem 14

Let $d=\gcd(a,b)$, and let $k$ be any integer. Prove that

$$\gcd(a,b)=\gcd(a,b+ka).$$

<details>
<summary>Solution</summary>

Let $c=b+ka$. A number that divides both $a$ and $b$ also divides

$$c=b+ka,$$

so every common divisor of $a$ and $b$ is a common divisor of $a$ and $c$.

Conversely, if a number divides both $a$ and $c$, it divides

$$c-ka=b.$$

So every common divisor of $a$ and $c$ is a common divisor of $a$ and $b$. The two
pairs have exactly the same common divisors, so

$$\gcd(a,b)=\gcd(a,b+ka).$$

</details>

### Problem 15

The Euclidean algorithm begins

$$1089=462\cdot2+165$$

$$462=165\cdot2+132.$$

Continue the algorithm and find the GCD.

<details>
<summary>Solution</summary>

Continue from the given equations:

$$165=132\cdot1+33$$

$$132=33\cdot4+0.$$

The last nonzero remainder is $33$, so

$$\boxed{\gcd(1089,462)=33.}$$

</details>

## Submission Checklist

- Write each division in the form $a=bq+r$ with $0\le r<b$.
- Replace the pair with (divisor, remainder), then continue until the remainder is $0$.
- Report the last nonzero remainder as the GCD.
- Use $\operatorname{lcm}(a,b)=ab/\gcd(a,b)$ only after finding the GCD.
