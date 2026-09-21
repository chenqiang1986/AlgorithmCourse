# Lesson 4: The Euclidean Algorithm for GCD
*AMC / Number Theory*

Prime factorization is excellent when the factors are easy to find. For larger numbers,
we need a faster way to calculate a greatest common divisor without factoring either
number completely. The **Euclidean algorithm** does exactly that: repeated division
turns a GCD problem into smaller and smaller GCD problems.

## 1. The Key Remainder Fact

Suppose $a$ and $b$ are positive integers with $a>b$. Division with remainder gives

$$a=bq+r,\qquad0\le r<b.$$

Then

$$\boxed{\gcd(a,b)=\gcd(b,r).}$$

In words: replacing the larger number by the remainder when it is divided by the
smaller number does not change the GCD.

### Why It Is True

Let $d$ be a common divisor of $a$ and $b$. Since $d\mid a$ and $d\mid b$, it also
divides every integer combination of them. In particular,

$$r=a-bq,$$

so $d\mid r$. Thus every common divisor of $a$ and $b$ is a common divisor of $b$
and $r$.

Conversely, if $d\mid b$ and $d\mid r$, then

$$a=bq+r,$$

so $d\mid a$. Thus every common divisor of $b$ and $r$ is also a common divisor of
$a$ and $b$. The two pairs have exactly the same common divisors, and therefore the
same greatest one.

## 2. One Remainder Step

Find $\gcd(91,35)$.

Divide $91$ by $35$:

$$91=35\cdot2+21.$$

The key fact gives

$$\gcd(91,35)=\gcd(35,21).$$

The second pair is smaller, but it has the same GCD. We continue this process until a
remainder is $0$.

## 3. The Euclidean Algorithm

To find $\gcd(a,b)$ for positive integers:

1. Put the larger number first.
2. Divide the larger number by the smaller number.
3. Replace the pair with **(divisor, remainder)**.
4. Repeat until the remainder is $0$.
5. The last nonzero remainder is the GCD.

The algorithm must stop: every new nonzero remainder is a smaller nonnegative integer
than the previous divisor. Positive integers cannot decrease forever.

### Example: $\gcd(91,35)$

Continue the first step from above:

$$91=35\cdot2+21$$

$$35=21\cdot1+14$$

$$21=14\cdot1+7$$

$$14=7\cdot2+0.$$

Therefore

$$\boxed{\gcd(91,35)=7.}$$

The final line says that $7$ divides $14$ exactly. The previous nonzero remainder,
$7$, is the GCD.

## 4. Organizing the Work in a Table

For longer computations, a table helps prevent a common mistake: replacing the wrong
number. Find $\gcd(1{,}071,462)$.

| Dividend | Divisor | Quotient | Remainder |
| ---: | ---: | ---: | ---: |
| $1{,}071$ | $462$ | $2$ | $147$ |
| $462$ | $147$ | $3$ | $21$ |
| $147$ | $21$ | $7$ | $0$ |

Equivalently,

$$1{,}071=462\cdot2+147$$

$$462=147\cdot3+21$$

$$147=21\cdot7+0.$$

The last nonzero remainder is $21$, so

$$\boxed{\gcd(1{,}071,462)=21.}$$

We did not need to factor $1{,}071$ or $462$.

## 5. A Longer Example

Find $\gcd(12{,}345,6{,}789)$.

$$12{,}345=6{,}789\cdot1+5{,}556$$

$$6{,}789=5{,}556\cdot1+1{,}233$$

$$5{,}556=1{,}233\cdot4+624$$

$$1{,}233=624\cdot1+609$$

$$624=609\cdot1+15$$

$$609=15\cdot40+9$$

$$15=9\cdot1+6$$

$$9=6\cdot1+3$$

$$6=3\cdot2+0.$$

Thus

$$\boxed{\gcd(12{,}345,6{,}789)=3.}$$

This also tells us that the two numbers are not relatively prime. If the last nonzero
remainder had been $1$, they would have been relatively prime.

## 6. Edge Cases and Useful Habits

### When One Number Divides the Other

If $a=bq$, then the first remainder is $0$. Therefore

$$\gcd(a,b)=b.$$

For example,

$$156=39\cdot4+0,$$

so $\gcd(156,39)=39$.

### When the Numbers Are Given in Reverse Order

Start with the larger number, or simply make one division first. For example,

$$\gcd(28,75)=\gcd(75,28),$$

then proceed:

$$75=28\cdot2+19,\qquad28=19\cdot1+9,\qquad19=9\cdot2+1,$$

$$9=1\cdot9+0.$$

Thus $\gcd(28,75)=1$.

### Connecting Back to LCM

Once the Euclidean algorithm gives the GCD of two positive integers, Lesson 3's
product formula gives their LCM:

$$\operatorname{lcm}(a,b)=\frac{ab}{\gcd(a,b)}.$$

For $91$ and $35$, the algorithm found a GCD of $7$, so

$$\operatorname{lcm}(91,35)=\frac{91\cdot35}{7}=455.$$

## 7. Class Practice

### Problem 1

Use the Euclidean algorithm to find $\gcd(414,662)$.

<details>
<summary>Solution</summary>

Start with $662$:

$$662=414\cdot1+248$$

$$414=248\cdot1+166$$

$$248=166\cdot1+82$$

$$166=82\cdot2+2,$$

and then

$$82=2\cdot41+0.$$

Therefore

$$\boxed{\gcd(414,662)=2.}$$

</details>

### Problem 2

Are $391$ and $299$ relatively prime? Use the Euclidean algorithm.

<details>
<summary>Solution</summary>

$$391=299\cdot1+92$$

$$299=92\cdot3+23$$

$$92=23\cdot4+0.$$

The last nonzero remainder is $23$, so

$$\gcd(391,299)=23.$$

Therefore $391$ and $299$ are **not** relatively prime.

</details>

### Problem 3

Use the Euclidean algorithm to find $\operatorname{lcm}(252,198)$.

<details>
<summary>Solution</summary>

First find the GCD:

$$252=198\cdot1+54$$

$$198=54\cdot3+36$$

$$54=36\cdot1+18$$

$$36=18\cdot2+0.$$

So $\gcd(252,198)=18$. Now use the product formula:

$$\operatorname{lcm}(252,198)=\frac{252\cdot198}{18}=252\cdot11=2{,}772.$$

</details>

### Problem 4

Explain why $\gcd(a,b)=\gcd(b,a)$ for positive integers $a$ and $b$.

<details>
<summary>Solution</summary>

The common divisors of $a$ and $b$ are exactly the same as the common divisors of $b$
and $a$; only the order of the pair has changed. Therefore their greatest common
divisor is the same:

$$\gcd(a,b)=\gcd(b,a).$$

</details>

### Problem 5

Two rectangular tiles have side lengths $154$ cm by $98$ cm. They must be cut into
the largest possible square pieces with no waste. What is the side length of each
square piece?

<details>
<summary>Solution</summary>

The side length must divide both $154$ and $98$, so it is their GCD.

$$154=98\cdot1+56$$

$$98=56\cdot1+42$$

$$56=42\cdot1+14$$

$$42=14\cdot3+0.$$

Thus the greatest possible side length is $\boxed{14\text{ cm}}$.

</details>

## 8. Common Mistakes

### 8.1 Stopping at the last quotient

The GCD is the **last nonzero remainder**, not the last quotient. In

$$147=21\cdot7+0,$$

the quotient is $7$, but the final nonzero remainder from the previous line is $21$.
The GCD is $21$.

### 8.2 Replacing the pair incorrectly

From

$$a=bq+r,$$

the next pair is $(b,r)$, not $(a,r)$ and not $(q,r)$. Keep the divisor and the
remainder.

### 8.3 Using a remainder that is too large

Each remainder must satisfy $0\le r<b$, where $b$ is the divisor. If a supposed
remainder is at least the divisor, divide again.

### 8.4 Assuming a small remainder is automatically the GCD

A remainder is only an intermediate value unless the next division has remainder $0$.
Continue until the algorithm ends.

## Takeaway

The Euclidean algorithm repeatedly applies

$$\gcd(a,b)=\gcd(b,r)\qquad\text{when }a=bq+r.$$

Each step makes the numbers smaller without changing their common divisors. When the
remainder reaches $0$, the last nonzero remainder is the GCD. This is usually much
faster than prime factorization and prepares us for later work with linear equations
and congruences.
