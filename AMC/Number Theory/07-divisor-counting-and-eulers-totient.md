# Lesson 7: Divisor Counting & Euler's Totient Function
*AMC / Number Theory*

Prime factorization tells us more than which primes divide a number. It lets us count
all of its divisors without listing them. We will then use the familiar idea
$\gcd(a,n)=1$ to introduce Euler's totient function.

## Learning Goals

By the end of this lesson, you will be able to:

- count positive divisors from a prime factorization;
- count divisors satisfying exponent restrictions;
- define and find Euler's totient function for small numbers; and
- explain the totient values for primes and prime powers.

## 1. Divisors Are Choices of Prime Exponents

Suppose

$$72=2^3\cdot3^2.$$

Every positive divisor of $72$ has the form $2^a3^b$, where

$$a\in\{0,1,2,3\}\qquad\text{and}\qquad b\in\{0,1,2\}.$$

There are four choices for $a$ and three independent choices for $b$. By the
product rule, $72$ has $4\cdot3=12$ positive divisors. The choice of exponent
$0$ is important: it allows a prime to be absent, and it includes the divisor $1$.

### Divisor-Count Formula

If

$$n=p_1^{a_1}p_2^{a_2}\cdots p_k^{a_k},$$

then a positive divisor chooses an exponent from $0$ through $a_i$ for each
prime $p_i$. Thus, if $\tau(n)$ denotes the number of positive divisors of $n$,

$$\boxed{\tau(n)=(a_1+1)(a_2+1)\cdots(a_k+1).}$$

This formula counts positive divisors. For a positive $n$, the number of integer
divisors (positive and negative) is $2\tau(n)$.

### Example: Count the Divisors of $360$

$$360=2^3\cdot3^2\cdot5,$$

so

$$\tau(360)=(3+1)(2+1)(1+1)=4\cdot3\cdot2=\boxed{24}. $$

The common error is to multiply the exponents without adding one. Every exponent
range starts at $0$, so an exponent $a_i$ offers $a_i+1$ choices.

## 2. Restrict the Exponent Choices

The same idea counts special types of divisors.

### Example: Divisors That Are Multiples of $14$

How many divisors of $2^4\cdot7^3$ are multiples of $14$?

A divisor has the form $2^a7^b$. Being a multiple of $14=2\cdot7$ requires
$a\geq1$ and $b\geq1$. Therefore

$$a\in\{1,2,3,4\},\qquad b\in\{1,2,3\},$$

and the answer is

$$\boxed{4\cdot3=12}. $$

The prime factorization converts the divisibility condition into a restriction on
exponents.

### Reading a Divisor Count Backward

A positive integer has exactly two positive divisors if and only if it is prime. It
has exactly three positive divisors if and only if it is the square of a prime:

$$\tau(p^2)=2+1=3.$$

For example, if $n=2^a3^b$ and $n$ has $12$ positive divisors, then

$$ (a+1)(b+1)=12. $$

The possible ordered exponent pairs are

$$\boxed{(a,b)=(1,5),(2,3),(3,2),(5,1).}$$

## 3. Euler's Totient Function

Recall that two integers are relatively prime when their GCD is $1$. Euler's
totient function counts the relatively prime numbers in one complete residue set:

> For a positive integer $n$, $\varphi(n)$ is the number of integers $a$ with
> $1\leq a\leq n$ and $\gcd(a,n)=1$.

For $n>1$, this is the same as counting from $1$ through $n-1$, because $n$
is not relatively prime to itself.

### Example: Find $\varphi(12)$

Since $12=2^2\cdot3$, cross out numbers from $1$ through $12$ that are
multiples of $2$ or $3$. The survivors are

$$1,5,7,11.$$

Therefore

$$\boxed{\varphi(12)=4}. $$

## 4. First Totient Facts

If $p$ is prime, every integer from $1$ through $p-1$ is relatively prime to
$p$. Hence

$$\boxed{\varphi(p)=p-1.}$$

For a prime power $p^k$, the only numbers from $1$ through $p^k$ that are not
relatively prime to $p^k$ are multiples of $p$. There are $p^{k-1}$ of those,
so

$$\boxed{\varphi(p^k)=p^k-p^{k-1}.}$$

For example,

$$\varphi(25)=25-5=\boxed{20}.$$

## 5. The General Totient Formula

Let

$$n=p_1^{a_1}p_2^{a_2}\cdots p_k^{a_k}$$

be the prime factorization of $n$. Then

$$\boxed{\varphi(n)=\prod_{i=1}^{k}p_i^{a_i-1}(p_i-1).}$$

An equivalent form, often useful for calculations, is

$$\boxed{\varphi(n)=n\prod_{i=1}^{k}\left(1-\frac1{p_i}\right).}$$

The product is over the **distinct** prime factors of $n$, not over every copy of a
prime. We will prove this formula by combining two facts.

### Lemma 1: Coprimality Can Be Checked One Prime Power at a Time

For every integer $x$,

$$\boxed{\gcd(x,n)=1\quad\Longleftrightarrow\quad
\gcd(x,p_i^{a_i})=1\text{ for every }i.}$$

**Proof.** If $\gcd(x,n)=1$, then no prime factor of $n$ divides $x$. In particular,
no $p_i$ divides $x$, so $x$ shares no prime factor with $p_i^{a_i}$. Thus
$\gcd(x,p_i^{a_i})=1$ for every $i$.

Conversely, suppose $\gcd(x,p_i^{a_i})=1$ for every $i$. Then no $p_i$ divides
$x$. Since $p_1,\ldots,p_k$ are all the prime factors of $n$, $x$ and $n$ have no
prime factor in common. Therefore $\gcd(x,n)=1$. $\square$

### Lemma 2: CRT Gives Independent Remainder Coordinates

The prime powers

$$p_1^{a_1},p_2^{a_2},\ldots,p_k^{a_k}$$

are pairwise relatively prime. Therefore, by the Chinese Remainder Theorem, every
list of remainder classes

$$\left(r_1\pmod {p_1^{a_1}},\ r_2\pmod {p_2^{a_2}},\ \ldots,\
r_k\pmod {p_k^{a_k}}\right)$$

corresponds to exactly one remainder class

$$x\pmod n.$$

In other words, CRT makes a bijection between the residue classes modulo $n$ and
the lists of residue classes modulo its prime-power factors.

### Proof of the General Formula

For $i=1,\ldots,k$, define

$$\varphi_i=\varphi(p_i^{a_i})
=p_i^{a_i}-p_i^{a_i-1}
=p_i^{a_i-1}(p_i-1).$$

List the $\varphi_i$ residue classes modulo $p_i^{a_i}$ that are relatively prime to
$p_i^{a_i}$ as

$$r_{i,1},r_{i,2},\ldots,r_{i,\varphi_i}.$$

Consider all lists

$$\left(r_{1,j_1},r_{2,j_2},\ldots,r_{k,j_k}\right),
\qquad 1\leq j_i\leq\varphi_i\quad(i=1,\ldots,k).$$

There are

$$\varphi_1\varphi_2\cdots\varphi_k$$

such lists. By Lemma 2, each list determines a unique residue class $x\pmod n$
such that

$$x\equiv r_{i,j_i}\pmod {p_i^{a_i}}\qquad(i=1,\ldots,k).$$

For this $x$,

$$\gcd(x,p_i^{a_i})=\gcd(r_{i,j_i},p_i^{a_i})=1$$

for every $i$. Lemma 1 therefore gives $\gcd(x,n)=1$.

Conversely, if $\gcd(x,n)=1$, Lemma 1 gives

$$\gcd(x,p_i^{a_i})=1\qquad(i=1,\ldots,k).$$

Thus the remainder of $x$ modulo $p_i^{a_i}$ is exactly one $r_{i,j_i}$ in the
list above. CRT uniqueness shows that different index lists give different residue
classes $x\pmod n$. Hence the index lists are in bijection with the residue classes
relatively prime to $n$, and

$$\begin{aligned}
\varphi(n)
&=\varphi_1\varphi_2\cdots\varphi_k\\
&=\prod_{i=1}^{k}p_i^{a_i-1}(p_i-1).
\end{aligned}$$

Finally, factor $p_i^{a_i}$ from each term:

$$p_i^{a_i-1}(p_i-1)=p_i^{a_i}\left(1-\frac1{p_i}\right).$$

Multiplying these identities gives

$$\varphi(n)=\left(\prod_{i=1}^{k}p_i^{a_i}\right)
\left(\prod_{i=1}^{k}\left(1-\frac1{p_i}\right)\right)
=n\prod_{i=1}^{k}\left(1-\frac1{p_i}\right),$$

which proves the equivalent formula. $\square$

### Example: Find $\varphi(360)$

Because $360=2^3\cdot3^2\cdot5$,

$$\begin{aligned}
\varphi(360)
&=360\left(1-\frac12\right)\left(1-\frac13\right)
\left(1-\frac15\right)\\
&=360\cdot\frac12\cdot\frac23\cdot\frac45
=\boxed{96}.
\end{aligned}$$

The next lesson will use this count of coprime residues to simplify large powers
modulo $n$.

## 6. Class Practice

### Problem 1

Find the number of positive divisors of $840$.

<details>
<summary>Solution</summary>

$$840=2^3\cdot3\cdot5\cdot7,$$

so

$$\tau(840)=(3+1)(1+1)^3=4\cdot2\cdot2\cdot2=\boxed{32}. $$

</details>

### Problem 2

How many positive divisors of $2^5\cdot3^4$ are divisible by $12$?

<details>
<summary>Solution</summary>

Since $12=2^2\cdot3$, the exponents satisfy $2\leq a\leq5$ and
$1\leq b\leq4$. There are four choices for each, giving

$$\boxed{16}. $$

</details>

### Problem 3

Find $\varphi(18)$.

<details>
<summary>Solution</summary>

Since $18=2\cdot3^2$, exclude multiples of $2$ and $3$. The numbers remaining
are $1,5,7,11,13,17$, so

$$\boxed{\varphi(18)=6}. $$

</details>

### Problem 4

Find $\varphi(84)$ using the general formula.

<details>
<summary>Solution</summary>

Since $84=2^2\cdot3\cdot7$,

$$\begin{aligned}
\varphi(84)
&=84\left(1-\frac12\right)\left(1-\frac13\right)\left(1-\frac17\right)\\
&=84\cdot\frac12\cdot\frac23\cdot\frac67
=\boxed{24}.
\end{aligned}$$

</details>

## 7. Exit Ticket

1. If $n=2^4\cdot3^2\cdot11$, find $\tau(n)$.
2. State what $\varphi(n)$ counts.
3. State the two conditions that Lemma 1 says are equivalent.
4. Find $\varphi(19)$ and explain why.

<details>
<summary>Answers</summary>

1. $(4+1)(2+1)(1+1)=\boxed{30}$.
2. The integers $a$ from $1$ through $n$ for which $\gcd(a,n)=1$.
3. $\gcd(x,n)=1$; and $\gcd(x,p_i^{a_i})=1$ for every prime-power factor of $n$.
4. $\boxed{18}$, because $19$ is prime.

</details>

## 8. Summary

For

$$n=p_1^{a_1}\cdots p_k^{a_k},$$

each divisor independently chooses each prime exponent, so

$$\boxed{\tau(n)=\prod_{i=1}^k(a_i+1).}$$

Euler's totient counts coprime residues:

$$\boxed{\varphi(n)=\#\{a:1\leq a\leq n,\ \gcd(a,n)=1\}.}$$

For a prime factorization $n=p_1^{a_1}\cdots p_k^{a_k}$,

$$\boxed{\varphi(n)=\prod_{i=1}^{k}p_i^{a_i-1}(p_i-1)
=n\prod_{i=1}^{k}\left(1-\frac1{p_i}\right).}$$

Lemma 1 says that being coprime to $n$ is the same as being coprime to each
prime-power factor. Lemma 2 uses CRT to make the allowable prime-power remainders
independent, so their counts multiply.

The first special cases are

$$\boxed{\varphi(p)=p-1}\qquad\text{and}\qquad
\boxed{\varphi(p^k)=p^k-p^{k-1}}.$$
