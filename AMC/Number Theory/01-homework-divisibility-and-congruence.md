# Homework: Divisibility and Congruence Modulo $n$
*AMC / Number Theory*

This homework accompanies [Lesson 1](./01-divisibility-and-congruence-modulo.md).
Parts A and B build fluency with divisibility, remainders, and efficient modular
calculation. Part C proves several divisibility tests from place value, so the tests are
tools to understand rather than rules to memorize.

## Part A: Basic Divisibility and Congruence

### Problem 1

For each statement, write **true** or **false**. If true, exhibit an integer quotient;
if false, explain briefly.

1. $14\mid238$
2. $15\mid245$
3. $-9\mid72$
4. $31\mid31$

<details>
<summary>Solution</summary>

1. True: $238=14\cdot17$.
2. False: $245/15$ is not an integer.
3. True: $72=(-9)(-8)$.
4. True: $31=31\cdot1$.

</details>

### Problem 2

Find the quotient and standard remainder when each number is divided by the indicated
positive divisor.

1. $157$ divided by $12$
2. $-157$ divided by $12$
3. $-89$ divided by $7$

<details>
<summary>Solution</summary>

1. $157=12\cdot13+1$, so the quotient is $13$ and the remainder is $1$.
2. $-157=12(-14)+11$, so the quotient is $-14$ and the remainder is $11$.
3. $-89=7(-13)+2$, so the quotient is $-13$ and the remainder is $2$.

</details>

### Problem 3

Decide whether each congruence is true by checking whether the modulus divides the
difference.

1. $74\equiv4\pmod{14}$
2. $125\equiv6\pmod{17}$
3. $-31\equiv4\pmod7$
4. $91\equiv1\pmod9$

<details>
<summary>Solution</summary>

1. True: $74-4=70=14\cdot5$.
2. True: $125-6=119=17\cdot7$.
3. True: $-31-4=-35=7(-5)$.
4. True: $91-1=90=9\cdot10$.

</details>

### Problem 4

List the standard remainders modulo $8$ of $-19$, $43$, $104$, and $-1$.

<details>
<summary>Solution</summary>

$$-19\equiv5,\qquad43\equiv3,\qquad104\equiv0,\qquad-1\equiv7\pmod8.$$

The remainders are **$5,3,0,7$**, respectively.

</details>

### Problem 5

Show that if $a\mid b$ and $a\mid c$, then $a\mid(5b-2c)$.

<details>
<summary>Solution</summary>

Since $a\mid b$ and $a\mid c$, there are integers $m,n$ with $b=am$ and $c=an$.
Then

$$5b-2c=5(am)-2(an)=a(5m-2n).$$

Because $5m-2n$ is an integer, $a\mid(5b-2c)$.

</details>

## Part B: Calculate Efficiently With Congruences

In each problem, show a useful reduction before computing the final remainder.

### Problem 6

Find $68+97\pmod{13}$.

<details>
<summary>Solution</summary>

$$68+97\equiv3+6=9\pmod{13}.$$

</details>

### Problem 7

Find $18\cdot17\pmod{19}$.

<details>
<summary>Solution</summary>

Choose negative representatives close to $0$:

$$18\cdot17\equiv(-1)(-2)=2\pmod{19}.$$

</details>

### Problem 8

Find $47\cdot38\pmod{11}$.

<details>
<summary>Solution</summary>

$$47\cdot38\equiv3\cdot5=15\equiv4\pmod{11}.$$

</details>

### Problem 9

Find $99^2-101^2\pmod{17}$ without first evaluating either square.

<details>
<summary>Solution</summary>

Use a difference of squares:

$$99^2-101^2=(99-101)(99+101)=(-2)(200).$$

Since $200\equiv13\pmod{17}$,

$$(-2)(200)\equiv(-2)(13)=-26\equiv8\pmod{17}.$$

</details>

### Problem 10

Find $2^{20}\pmod7$.

<details>
<summary>Solution</summary>

$$2^3=8\equiv1\pmod7.$$

Therefore

$$2^{20}=2^{18}\cdot2^2=(2^3)^6\cdot2^2\equiv1^6\cdot4=4\pmod7.$$

</details>

### Problem 11

Find the units digit of $3^{27}$.

<details>
<summary>Solution</summary>

Work modulo $10$. The powers of $3$ repeat every four exponents:

$$3^1\equiv3,\quad3^2\equiv9,\quad3^3\equiv7,\quad3^4\equiv1\pmod{10}.$$

Since $27\equiv3\pmod4$, $3^{27}\equiv3^3\equiv7\pmod{10}$. The units digit is
**$7$**.

</details>

### Problem 12

Find the remainder when $4^{15}+5^{15}$ is divided by $9$.

<details>
<summary>Solution</summary>

Since $4^3=64\equiv1\pmod9$,

$$4^{15}=(4^3)^5\equiv1.$$

Also, $5^2=25\equiv7$ and $5^3\equiv35\equiv-1\pmod9$, so

$$5^{15}=(5^3)^5\equiv(-1)^5=-1.$$

Thus $4^{15}+5^{15}\equiv1+(-1)=0\pmod9$. The remainder is **$0$**.

</details>

## Part C: Proving Divisibility Tests

For a decimal integer, letters such as $a,b,c$ denote digits.

### Problem 13: Digit Sums for $3$ and $9$

Let $N=\overline{a_ka_{k-1}\ldots a_0}$. First rewrite $N$ as a sum using the place
values of its digits. Then prove that $N$ is divisible by $3$ (respectively, by $9$) if
and only if its digit sum $a_k+a_{k-1}+\cdots+a_0$ is divisible by $3$ (respectively,
by $9$).


<details>
<summary>Solution</summary>

By place value,

$$N=a_k10^k+a_{k-1}10^{k-1}+\cdots+a_1 10+a_0=\sum_{j=0}^ka_j10^j.$$

Modulo $3$ and modulo $9$, we have $10\equiv1$. Hence every power of $10$ is also
congruent to $1$:

$$10^j\equiv1\pmod3\qquad\text{and}\qquad10^j\equiv1\pmod9.$$

Therefore, for either modulus $m\in\{3,9\}$,

$$N=\sum_{j=0}^k a_j10^j\equiv\sum_{j=0}^k a_j\pmod m.$$

Thus $N\equiv0\pmod m$ exactly when its digit sum is $0\pmod m$, proving both tests.

</details>

### Problem 14: Alternating Digit Sum for $11$

Let $N=\overline{a_ka_{k-1}\ldots a_0}$. First rewrite $N$ using the place values of
its digits. Then prove that $N$ is divisible by $11$ if and only if

$$a_0-a_1+a_2-a_3+\cdots+(-1)^k a_k$$

is divisible by $11$. (Changing every sign gives an equivalent test.)

<details>
<summary>Solution</summary>

Modulo $11$, $10\equiv-1$. Raising both sides to the $j$th power gives

$$10^j\equiv(-1)^j\pmod{11}.$$

The required place-value expansion is

$$N=\sum_{j=0}^ka_j10^j.$$

Substitute the congruence for $10^j$ into that expansion:

$$N=\sum_{j=0}^k a_j10^j\equiv\sum_{j=0}^k a_j(-1)^j\pmod{11}.$$

The expression on the right is exactly the alternating digit sum. Therefore it is
congruent to $0$ modulo $11$ exactly when $N$ is, which proves the test.

</details>

### Problem 15: Alternating Three-Digit Blocks for $7$, $11$, and $13$

Let

$$N=\overline{a_{3k+2}a_{3k+1}a_{3k}\ldots a_2a_1a_0}.$$

For each $m\in\{7,11,13\}$, prove that $N$ is divisible by $m$ if and only if

$$\overline{a_2a_1a_0}-\overline{a_5a_4a_3}+\overline{a_8a_7a_6}
-\cdots+(-1)^k\overline{a_{3k+2}a_{3k+1}a_{3k}}$$

is divisible by $m$.

<details>
<summary>Solution</summary>

The place-value expansion in three-digit groups is

$$\begin{aligned}
N={}&\overline{a_{3k+2}a_{3k+1}a_{3k}}\,1000^k
+\overline{a_{3k-1}a_{3k-2}a_{3k-3}}\,1000^{k-1}+\cdots\\
&+\overline{a_5a_4a_3}\,1000+\overline{a_2a_1a_0}.
\end{aligned}$$

The key factorization is

$$1001=7\cdot11\cdot13.$$

Thus $1000\equiv-1\pmod m$ for each $m\in\{7,11,13\}$. Consequently,

$$1000^j\equiv(-1)^j\pmod m.$$

Using this block expansion,

$$\begin{aligned}
N\equiv{}&(-1)^k\overline{a_{3k+2}a_{3k+1}a_{3k}}
+(-1)^{k-1}\overline{a_{3k-1}a_{3k-2}a_{3k-3}}+\cdots\\
&-\overline{a_5a_4a_3}+\overline{a_2a_1a_0}\pmod m.
\end{aligned}$$

Reordering the sum gives the stated alternating three-digit sum. It is congruent to
$0$ modulo $m$ exactly when $N$ is. This proves the test for all three divisors.

</details>

### Problem 16: A Repeated Test for $7$

Let

$$N=\overline{a_ka_{k-1}\ldots a_1a_0}.$$

Prove

$$7\mid N\quad\Longleftrightarrow\quad
7\mid\left(\overline{a_ka_{k-1}\ldots a_1}-2a_0\right).$$

Then use the test repeatedly to decide whether $203{,}126$ is divisible by $7$.

<details>
<summary>Solution</summary>

Let $A=\overline{a_ka_{k-1}\ldots a_1}$ and $c=a_0$. By place value,
$N=10A+c$. Multiply $A-2c$ by $10$:

$$10(A-2c)=10A-20c=(10A+c)-21c=N-21c.$$

Thus $10(A-2c)\equiv N\pmod7$. Also, multiplying an integer by $10$ does not change
whether it is divisible by $7$: if $7\mid10X$, then $7\mid5(10X)=50X$, and
$X=50X-49X$ is also divisible by $7$. Therefore

$$7\mid N\quad\Longleftrightarrow\quad7\mid(A-2c).$$

Apply the transformation:

$$203126\longmapsto20312-2(6)=20300,$$

$$20300\longmapsto2030-2(0)=2030,$$

$$2030\longmapsto203-2(0)=203,$$

$$203\longmapsto20-2(3)=14.$$

Because $7\mid14$, we conclude $7\mid203126$.

</details>

### Problem 17: Use Two Tests Together

Without long division, determine whether $4{,}284{,}735{,}294$ is divisible by $7$, by
$11$, and by $13$. Use the three-digit-block test from Problem 15.

<details>
<summary>Solution</summary>

Split into blocks:

$$4{,}284{,}735{,}294=4\mid284\mid735\mid294.$$

The alternating block sum, starting on the right, is

$$294-735+284-4=-161.$$

Now $161=7\cdot23$, so $-161$ is divisible by $7$. But $161$ is not divisible by
$11$ or $13$. Therefore the original number is divisible by **$7$ only**, not by $11$
or $13$.

</details>

## Checklist Before Submitting

- Write the modulus in every congruence statement.
- Give a remainder from $0$ through $n-1$ when a standard remainder is requested.
- In Part B, show the congruent replacements that make the arithmetic shorter.
- In Part C, first convert the barred digit or block notation into its place-value
  expansion, then state the congruence for $10$ or $1000$ that drives the test.
