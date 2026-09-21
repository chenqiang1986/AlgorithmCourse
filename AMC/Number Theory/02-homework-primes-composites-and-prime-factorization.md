# Homework: Primes, Composites, and Prime Factorization
*AMC / Number Theory*

This homework accompanies [Lesson 2](./02-primes-composites-and-prime-factorization.md).
Show enough work to make your reasoning clear. In particular, when you decide that a
number is prime, state which prime divisors up to its square root you checked.

## Part A: Factors, Primes, and Composites

### Problem 1

List all positive factors of $48$. Then state how many positive factors $48$ has.

<details>
<summary>Solution</summary>

The factor pairs are

$$1\cdot48,\quad2\cdot24,\quad3\cdot16,\quad4\cdot12,\quad6\cdot8.$$

Thus the positive factors are

$$1,2,3,4,6,8,12,16,24,48,$$

so $48$ has $10$ positive factors.

</details>

### Problem 2

Classify each number as **prime**, **composite**, or **neither**. Give a reason for
each answer.

$$1,\qquad2,\qquad57,\qquad79,\qquad121$$

<details>
<summary>Solution</summary>

- $1$ is neither: it has only one positive factor.
- $2$ is prime: its only positive factors are $1$ and $2$.
- $57$ is composite because $57=3\cdot19$.
- $79$ is prime. Since $\sqrt{79}<9$, check $2,3,5,7$; none divides $79$.
- $121$ is composite because $121=11^2$.

</details>

### Problem 3

Explain why every integer greater than $5$ whose units digit is $0$, $2$, $4$, $5$,
$6$, or $8$ is composite.

<details>
<summary>Solution</summary>

An integer ending in $0$, $2$, $4$, $6$, or $8$ is even, so it is divisible by $2$.
Since it is greater than $2$, it is composite. An integer ending in $5$ is divisible
by $5$; since it is greater than $5$, it is composite.

</details>

### Problem 4

Find all prime numbers $p<30$ for which $p+10$ is also prime.

<details>
<summary>Solution</summary>

The primes below $30$ are

$$2,3,5,7,11,13,17,19,23,29.$$

Testing $p+10$ for each gives the answers

$$p=3,7,13,19.$$

</details>

### Problem 5

Is $143$ prime? Justify your answer without testing every integer less than $143$.

<details>
<summary>Solution</summary>

Since $11^2=121<143<144=12^2$, it is enough to test prime divisors at most $11$:
$2,3,5,7,11$. We find

$$143=11\cdot13,$$

so $143$ is composite.

</details>

## Part B: The Square-Root Test

### Problem 6

Determine whether $97$ is prime. Show the complete list of prime divisors that must
be tested.

<details>
<summary>Solution</summary>

Because $9^2<97<10^2$, test primes at most $9$: $2,3,5,7$. None divides $97$.
Therefore $97$ is prime.

</details>

### Problem 7

Determine whether $167$ is prime.

<details>
<summary>Solution</summary>

Since $12^2=144<167<169=13^2$, test $2,3,5,7,11$. The number $167$ is divisible by
none of these primes. Therefore $167$ is prime.

</details>

### Problem 8

Determine whether $299$ is prime. If it is composite, write it as a product of two
integers greater than $1$.

<details>
<summary>Solution</summary>

Since $17^2=289<299<324=18^2$, test primes at most $17$. It is not divisible by
$2,3,5,7,$ or $11$, but

$$299=13\cdot23.$$

Thus $299$ is composite.

</details>

### Problem 9

Why is it enough to test **prime** possible divisors in the square-root test? Explain
why testing $2$, $3$, $5$, and $7$ is enough to rule out all divisors at most $9$.

<details>
<summary>Solution</summary>

Every composite divisor has a prime factor. If a number were divisible by $4$, $6$,
$8$, or $9$, it would also be divisible by $2$ or $3$. Thus after testing $2$, $3$,
$5$, and $7$, every integer from $2$ through $9$ has been covered either directly or
through one of its prime factors.

</details>

## Part C: Prime Factorization and Exponents

### Problem 10

Write each number as a prime factorization using exponents.

1. $84$
2. $180$
3. $504$
4. $1{,}155$

<details>
<summary>Solution</summary>

$$84=2^2\cdot3\cdot7$$

$$180=2^2\cdot3^2\cdot5$$

$$504=2^3\cdot3^2\cdot7$$

$$1{,}155=3\cdot5\cdot7\cdot11$$

</details>

### Problem 11

The number $N$ has prime factorization

$$N=2^4\cdot3^2\cdot5^3\cdot7.$$

For each number below, decide whether it divides $N$.

1. $120$
2. $420$
3. $1{,}000$
4. $480$

<details>
<summary>Solution</summary>

$$120=2^3\cdot3\cdot5,$$
so $120\mid N$.

$$420=2^2\cdot3\cdot5\cdot7,$$
so $420\mid N$.

$$1{,}000=2^3\cdot5^3,$$
so $1{,}000\mid N$.

$$480=2^5\cdot3\cdot5.$$

The exponent of $2$ is too large: $N$ contains $2^4$, not $2^5$. Therefore
$480\nmid N$.

The first three numbers divide $N$; the fourth does not.

</details>

### Problem 12

Find the smallest positive integer that is divisible by both $72$ and $105$.

<details>
<summary>Solution</summary>

Factor the numbers:

$$72=2^3\cdot3^2,\qquad105=3\cdot5\cdot7.$$

To be divisible by both, a number needs every prime with the larger required exponent:

$$2^3\cdot3^2\cdot5\cdot7=2{,}520.$$

The smallest such positive integer is $\boxed{2{,}520}$.

</details>

### Problem 13

Suppose $n=2^a\cdot3^b$, where $a$ and $b$ are nonnegative integers. If $n$ is
divisible by $72$ and $n<10{,}000$, what is the greatest possible value of $n$?

<details>
<summary>Solution</summary>

Because $72=2^3\cdot3^2$, we need $a\ge3$ and $b\ge2$. Also $b\le6$, since
$2^3\cdot3^7>10{,}000$. For each possible exponent of $3$, take the largest allowed
power of $2$:

$$\begin{array}{c|ccccc}
b&2&3&4&5&6\\ \hline
\text{largest }2^a3^b<10{,}000&9{,}216&6{,}912&5{,}184&7{,}776&5{,}832
\end{array}$$

The largest value in the table is $9{,}216$. Thus the maximum is

$$\boxed{9{,}216=2^{10}\cdot3^2}.$$

</details>

## Part D: Reasoning With Prime Factors

### Problem 14

If $p$ is prime and $p\mid 84$, list every possible value of $p$. Explain why there
can be no other values.

<details>
<summary>Solution</summary>

The prime factorization is

$$84=2^2\cdot3\cdot7.$$

Therefore the possible prime divisors are $\boxed{2,3,7}$. Any prime dividing $84$
must occur among the prime factors in its unique prime factorization.

</details>

### Problem 15

Prove that if $n>1$ is composite, then $n$ has a prime divisor.

<details>
<summary>Solution</summary>

If $n$ is composite, it has a factor $d$ with $1<d<n$. If $d$ is prime, then $d$ is
a prime divisor of $n$. If $d$ is composite, it has a factor greater than $1$ that is
smaller than $d$. Continue factoring any composite factor. Since the positive factors
strictly decrease and cannot decrease forever, this process eventually reaches a
prime factor. That prime divides $d$, and $d\mid n$, so it also divides $n$.

</details>
