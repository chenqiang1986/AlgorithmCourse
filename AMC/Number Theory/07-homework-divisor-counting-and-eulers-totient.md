# Homework: Divisor Counting & Euler's Totient Function
*AMC / Number Theory*

This homework accompanies [Lesson 7](./07-divisor-counting-and-eulers-totient.md).
Factor before counting. For totient questions, list the coprime integers or identify
precisely which prime-factor multiples are excluded.

## Part A: Count Divisors

### Problem 1

How many positive divisors does $540$ have?

<details>
<summary>Solution</summary>

$$540=2^2\cdot3^3\cdot5,$$

so

$$\tau(540)=(2+1)(3+1)(1+1)=\boxed{24}. $$

</details>

### Problem 2

How many positive divisors does $2^6\cdot3^2\cdot5^4$ have?

<details>
<summary>Solution</summary>

$$\tau(n)=(6+1)(2+1)(4+1)=7\cdot3\cdot5=\boxed{105}. $$

</details>

### Problem 3

How many integer divisors, both positive and negative, does $180$ have?

<details>
<summary>Solution</summary>

$$180=2^2\cdot3^2\cdot5,$$

so it has $(2+1)(2+1)(1+1)=18$ positive divisors. Pair each one with its
negative to get

$$\boxed{36}$$

integer divisors.

</details>

### Problem 4

A positive integer has factorization $2^a3^b$, where $a,b\geq1$. If it has
exactly $12$ positive divisors, list all possible ordered pairs $(a,b)$.

<details>
<summary>Solution</summary>

We need $(a+1)(b+1)=12$. Thus

$$\boxed{(a,b)=(1,5),(2,3),(3,2),(5,1).}$$

</details>

## Part B: Divisors with Conditions

### Problem 5

How many positive divisors of $2^5\cdot3^4\cdot7^2$ are multiples of $42$?

<details>
<summary>Solution</summary>

Since $42=2\cdot3\cdot7$, choose exponents $1$ through $5$, $1$ through
$4$, and $1$ through $2$, respectively. The number is

$$\boxed{5\cdot4\cdot2=40}. $$

</details>

### Problem 6

How many positive divisors of $2^6\cdot3^3\cdot5^2$ are perfect squares?

<details>
<summary>Solution</summary>

A square has even exponents. The choices are $0,2,4,6$ for the exponent of $2$,
$0,2$ for $3$, and $0,2$ for $5$. Therefore the count is

$$\boxed{4\cdot2\cdot2=16}. $$

</details>

### Problem 7

What is the smallest positive integer with exactly $15$ positive divisors?

<details>
<summary>Solution</summary>

The exponent patterns must satisfy a product of $15$: either $14$, or $4,2$.
The smallest candidates are $2^{14}$ and $2^4\cdot3^2=144$. Hence the answer is

$$\boxed{144}. $$

</details>

### Problem 8: Proof — Odd Divisor Counts

Prove that if a positive integer has an odd number of positive divisors, then it is
a perfect square.

<details>
<summary>Solution</summary>

For every positive divisor $d$ of $n$, the number

$$\frac nd$$

is also a positive divisor of $n$. Thus divisors pair as

$$d\longleftrightarrow\frac nd.$$

A divisor is unpaired exactly when it equals its partner:

$$d=\frac nd.$$

Multiplying by $d$ gives $d^2=n$. Therefore, if $n$ is not a perfect square, every
divisor belongs to a pair of two distinct divisors, and its divisor count is even.
The contrapositive proves the claim: if $n$ has an odd number of positive divisors,
then $n=d^2$ for some integer $d$, so $n$ is a perfect square. $\square$

</details>

## Part C: Euler's Totient Function

### Problem 9

List the integers from $1$ through $15$ relatively prime to $15$, then find
$\varphi(15)$.

<details>
<summary>Solution</summary>

Exclude multiples of $3$ or $5$. The remaining numbers are

$$1,2,4,7,8,11,13,14,$$

so

$$\boxed{\varphi(15)=8}. $$

</details>

### Problem 10

Find $\varphi(27)$.

<details>
<summary>Solution</summary>

Only multiples of $3$ share a factor with $27=3^3$. There are $27/3=9$
multiples of $3$, so

$$\varphi(27)=27-9=\boxed{18}. $$

</details>

### Problem 11

Find $\varphi(16)$, and explain why every odd number from $1$ through $16$ is
counted.

<details>
<summary>Solution</summary>

The eight even numbers are precisely the multiples of $2$, so

$$\boxed{\varphi(16)=16-8=8}. $$

An odd number has no factor $2$, and $2$ is the only prime factor of $16$.

</details>

### Problem 12

For which positive integers $n$ is $\varphi(n)=1$?

<details>
<summary>Solution</summary>

We have $\varphi(1)=1$ and $\varphi(2)=1$. If $n>2$, both $1$ and $n-1$
are relatively prime to $n$, so $\varphi(n)\geq2$. Thus

$$\boxed{n=1\text{ or }n=2}. $$

</details>

## Part D: Mixed Reasoning

### Problem 13

The positive integer $n=2^a\cdot3^b$, where $a,b\geq1$, has $18$ positive
divisors. Find all possible $(a,b)$, then find the smallest possible $n$.

<details>
<summary>Solution</summary>

Since $(a+1)(b+1)=18$,

$$ (a,b)=(1,8),(2,5),(5,2),(8,1). $$

The corresponding values are $2\cdot3^8$, $2^2\cdot3^5$,
$2^5\cdot3^2$, and $2^8\cdot3$. The smallest is

$$2^5\cdot3^2=\boxed{288}. $$

</details>

### Problem 14

How many integers from $1$ through $49$ are relatively prime to $49$? Explain
without listing all $49$ integers.

<details>
<summary>Solution</summary>

Since $49=7^2$, exactly the seven multiples of $7$ are excluded. Therefore

$$\boxed{\varphi(49)=49-7=42}. $$

</details>

## Key Reminders

- A divisor of $p_1^{a_1}\cdots p_k^{a_k}$ chooses every exponent independently.
- Restrict the allowed exponents first, then multiply their numbers of choices.
- Pair a divisor $d$ with $n/d$; only a perfect square can have an unpaired divisor.
- $\varphi(n)$ counts the integers from $1$ through $n$ with GCD $1$ with
  $n$.
- For a prime power, $\varphi(p^k)=p^k-p^{k-1}$.
