# Lesson 2: Primes, Composites, and Prime Factorization
*AMC / Number Theory*

Every positive integer greater than $1$ is either a prime number, which cannot be
broken into smaller positive factors, or a composite number, which can. This lesson
introduces primes as the building blocks of the positive integers and develops a
reliable way to factor a number completely.

## 1. Factors and Factor Pairs

A **factor** of a positive integer $n$ is a positive integer that divides $n$ evenly.
Factors occur in pairs: if $d\mid n$, then there is a matching factor $n/d$.

For example, the factor pairs of $36$ are

$$1\cdot36,\qquad2\cdot18,\qquad3\cdot12,\qquad4\cdot9,\qquad6\cdot6.$$

Thus the positive factors of $36$ are

$$1,2,3,4,6,9,12,18,36.$$

The pair $6\cdot6$ sits in the middle because $36$ is a perfect square. A number that
is not a square has no repeated middle pair; for instance, the factor pairs of $30$
are $1\cdot30$, $2\cdot15$, $3\cdot10$, and $5\cdot6$.

## 2. Prime, Composite, and Neither

A positive integer $p>1$ is **prime** if its only positive factors are $1$ and $p$.
A positive integer $n>1$ is **composite** if it has a positive factor other than $1$
and itself. Equivalently, a composite number can be written as

$$n=ab\qquad\text{with }1<a<n\text{ and }1<b<n.$$

Here are the first few primes:

$$2,3,5,7,11,13,17,19,23,29,31,\ldots$$

- $2$ is prime. It is the **only even prime**.
- $15$ is composite because $15=3\cdot5$.
- $49$ is composite because $49=7\cdot7$.
- $1$ is **neither prime nor composite**: it has exactly one positive factor, namely
  itself. A prime must have exactly two positive factors.

The number $1$ is deliberately excluded from the primes. This convention makes the
prime factorization of every integer greater than $1$ unique; for example, allowing
$1$ as prime would turn $6=2\cdot3$ into endlessly many supposed factorizations such
as $6=1\cdot2\cdot3$ and $6=1\cdot1\cdot2\cdot3$.

### Quick Consequences

- Every even integer greater than $2$ is composite, since it is divisible by $2$.
- Every multiple of $5$ greater than $5$ is composite.
- A number ending in $0$, $2$, $4$, $5$, $6$, or $8$ is not prime unless it is $2$ or
  $5$. This is only a quick filter: a number ending in $1$, $3$, $7$, or $9$ may still
  be composite. For example, $91=7\cdot13$.

## 3. Testing Whether a Number Is Prime

To show that a number is composite, it is enough to find one divisor besides $1$ and
itself. To show that a number is prime, we need a method that rules out every possible
proper divisor.

### The Square-Root Test

If $n>1$ is composite, then $n$ has a factor $d$ with

$$2\le d\le\sqrt n.$$

Why? If $n=ab$ with $1<a\le b$, then $a^2\le ab=n$, so $a\le\sqrt n$. Thus if a
number has no prime divisor at most its square root, it is prime.

In practice, test only **prime** divisors up to the square root. There is no need to
test a composite divisor: if $12$ divided $n$, then a prime factor of $12$, such as
$2$ or $3$, would also divide $n$.

### Example: Is $97$ Prime?

Since $9^2=81<97<100=10^2$, we only need to test primes at most $\sqrt{97}$:

$$2,3,5,7.$$

$97$ is not divisible by $2$, $3$, $5$, or $7$. Therefore **$97$ is prime**.

### Example: Is $221$ Prime?

Because $14^2=196<221<225=15^2$, test primes at most $14$:

$$2,3,5,7,11,13.$$

The first five do not divide $221$, but

$$221=13\cdot17.$$

Therefore **$221$ is composite**. Finding the factor $13$ ends the test.

## 4. Prime Factorization

A **prime factorization** writes a positive integer greater than $1$ as a product of
primes. We usually group repeated primes with exponents.

For example,

$$360=2\cdot2\cdot2\cdot3\cdot3\cdot5=2^3\cdot3^2\cdot5.$$

The exponent tells how many times a prime occurs: $2^3$ means three factors of $2$,
not $2\times3$.

### Method: Divide by Small Primes

Keep dividing by a prime factor until the quotient is $1$. The factors collected along
the way are the prime factorization.

Factor $756$:

$$756=2\cdot378=2^2\cdot189=2^2\cdot3\cdot63=2^2\cdot3^2\cdot21$$

$$=2^2\cdot3^3\cdot7.$$

A quick check confirms the result:

$$2^2\cdot3^3\cdot7=4\cdot27\cdot7=756.$$

### Method: Factor Trees

A factor tree is another way to record repeated splitting. Each branch must end in a
prime.

$$84=6\cdot14=(2\cdot3)(2\cdot7)=2^2\cdot3\cdot7.$$

Different first splits lead to the same prime factors:

$$84=4\cdot21=(2\cdot2)(3\cdot7)=2^2\cdot3\cdot7.$$

This is not an accident. The **Fundamental Theorem of Arithmetic** says that every
integer greater than $1$ has one prime factorization, apart from the order of its
factors. Thus

$$2^2\cdot3\cdot7=3\cdot2\cdot7\cdot2$$

is the same factorization written in a different order.

We will use this theorem as an organizing idea now, but postpone its proof. A complete
proof will come in later classes after we have developed **Bézout's identity**. One
key step in that proof is the prime-product theorem below.

### Advanced Aside: Why This Is a Theorem

Unique factorization is not automatic merely because an object has things that seem
like “prime building blocks.” For ordinary positive integers, we cannot have two
genuinely different prime factorizations such as

$$3\cdot11=5\cdot7,$$

but that fact needs proof.

For a striking contrast, consider the larger number system

$$\mathbb Z[\sqrt{-5}]=\{a+b\sqrt{-5}:a,b\in\mathbb Z\}.$$

Within this system,

$$6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5}).$$

All four displayed factors are **irreducible** in this system: none can be written as
a product of two non-unit elements. Yet the two factorizations are genuinely
different, even after rearranging factors or multiplying factors by the only units,
$1$ and $-1$. Thus unique factorization fails in $\mathbb Z[\sqrt{-5}]$.

This example is beyond the scope of this course, but it shows why the Fundamental
Theorem of Arithmetic deserves a proof. In fact, the prime-product theorem below is
exactly the property that prevents this kind of failure for ordinary integers.

## 5. Reading Prime Exponents

When

$$n=p_1^{a_1}p_2^{a_2}\cdots p_k^{a_k},$$

each $p_i$ is a different prime and each exponent $a_i$ is a positive integer. This
compact form records exactly which prime building blocks occur and how many of each.

For example,

$$1{,}260=2^2\cdot3^2\cdot5\cdot7.$$

So $1{,}260$ has two factors of $2$, two factors of $3$, one factor of $5$, and one
factor of $7$. It is divisible by $2^2\cdot3\cdot7$, but not by $2^3$, because its
factorization contains only two factors of $2$.

## 6. Two Essential Divisibility Theorems

The following results are easy to overlook, but they let us reason about divisibility
one prime at a time. We will prove them rigorously later, after Bézout's identity.

### Theorem 1: Prime-Product Theorem (Euclid's Lemma)

If $p$ is prime and

$$p\mid ab,$$

then

$$p\mid a\qquad\text{or}\qquad p\mid b.$$

In words: when a prime divides a product, it must divide at least one factor. The word
**prime** matters. For example, $6\mid2\cdot3$, but $6\nmid2$ and $6\nmid3$.

### Theorem 2: Prime-Power Divisibility Criterion

Suppose

$$n=p_1^{k_1}p_2^{k_2}\cdots p_r^{k_r},$$

where $p_1,p_2,\ldots,p_r$ are distinct primes and each $k_i$ is positive. Then, for
any integer $a$,

$$n\mid a\quad\Longleftrightarrow\quad p_i^{k_i}\mid a\text{ for every }i=1,2,\ldots,r.$$

In words: $n$ divides $a$ exactly when every complete prime-power piece of $n$ divides
$a$. Notice that the condition is “for every **$i$**,” one condition for each distinct
prime factor.

For example,

$$360=2^3\cdot3^2\cdot5.$$

To decide whether $360\mid5{,}400$, check its three prime-power pieces:

$$2^3\mid5{,}400,\qquad3^2\mid5{,}400,\qquad5\mid5{,}400.$$

All three are true, so $360\mid5{,}400$. This theorem will be a central tool for
working with divisors, gcds, and lcms.

## 7. Class Practice

### Problem 1

Classify each number as prime, composite, or neither: $1$, $2$, $27$, $31$, $51$.

<details>
<summary>Solution</summary>

- $1$ is neither prime nor composite.
- $2$ is prime.
- $27=3^3$, so it is composite.
- $31$ is prime: its square root is less than $6$, and it is not divisible by $2$, $3$,
  or $5$.
- $51=3\cdot17$, so it is composite.

</details>

### Problem 2

Determine whether $113$ is prime.

<details>
<summary>Solution</summary>

Since $10^2=100<113<121=11^2$, test primes up to $10$: $2,3,5,7$.
The number $113$ is divisible by none of them. Therefore **$113$ is prime**.

</details>

### Problem 3

Write $1{,}176$ as a product of prime powers.

<details>
<summary>Solution</summary>

$$1{,}176=2\cdot588=2^2\cdot294=2^3\cdot147=2^3\cdot3\cdot49$$

$$=2^3\cdot3\cdot7^2.$$

</details>

### Problem 4

Suppose $13\mid91x$. What must be true about $x$?

<details>
<summary>Solution</summary>

Write $91x$ as a product:

$$91x=(7\cdot13)x.$$

This already shows that $13\mid91$, so the Prime-Product Theorem alone does **not**
force any conclusion about $x$. For example, $x=1$ works, but $13\nmid1$.

This is a useful warning: from $p\mid ab$, we may conclude that $p\mid a$ **or**
$p\mid b$; we cannot always choose which factor it divides.

</details>

### Problem 5

Use the Prime-Product Theorem to show: if $7\mid45x$, then $7\mid x$.

<details>
<summary>Solution</summary>

Since $7$ is prime and $7\mid45x$, the theorem says that $7\mid45$ or $7\mid x$.
But $45=7\cdot6+3$, so $7\nmid45$. Therefore the remaining possibility is

$$7\mid x.$$

</details>

### Problem 6

Let

$$n=2^3\cdot3^2\cdot5.$$

Use the Prime-Power Divisibility Criterion to determine whether $n$ divides each
number.

1. $a=2^4\cdot3^2\cdot5\cdot11$
2. $b=2^3\cdot3\cdot5^4$

<details>
<summary>Solution</summary>

For $a$, each required prime-power piece divides $a$:

$$2^3\mid a,\qquad3^2\mid a,\qquad5\mid a.$$

Therefore $n\mid a$.

For $b$, the factorization contains only one factor of $3$, so

$$3^2\nmid b.$$

Therefore $n\nmid b$.

</details>

### Problem 7

Without dividing the number by $12$, $21$, or $35$, determine whether

$$N=999{,}999{,}999{,}999{,}840$$

is a multiple of each of these three numbers. Decompose each divisor into prime-power
pieces, then use the Prime-Power Divisibility Criterion.

<details>
<summary>Solution</summary>

First establish the small prime divisors we need. The digit sum of $N$ is

$$12\cdot9+8+4=120,$$

so $3\mid N$. Its last two digits are $40$, so $4\mid N$, and its last digit is $0$,
so $5\mid N$.

To check $7$, separate the number into two convenient pieces:

$$N=999{,}999{,}999{,}999\cdot1{,}000+840.$$

Since

$$999{,}999{,}999{,}999=999{,}999\cdot1{,}000{,}001$$

and $999{,}999=7\cdot142{,}857$, the first piece is divisible by $7$. Also,
$840=7\cdot120$. Therefore $7\mid N$.

Now decompose the requested divisors:

$$12=2^2\cdot3,\qquad21=3\cdot7,\qquad35=5\cdot7.$$

We have shown $2^2\mid N$, $3\mid N$, $5\mid N$, and $7\mid N$. The
Prime-Power Divisibility Criterion therefore gives

$$12\mid N,\qquad21\mid N,\qquad35\mid N.$$

So **$N$ is a multiple of all three numbers**, without dividing $N$ by any of them.

</details>

### Problem 8

Find the smallest prime factor of $143$, then factor $143$ completely.

<details>
<summary>Solution</summary>

$143$ is not divisible by $2$, $3$, $5$, or $7$. Since

$$143=11\cdot13,$$

its smallest prime factor is **$11$**, and its complete prime factorization is
$11\cdot13$.

</details>

## 8. Common Mistakes

### 8.1 Calling $1$ prime

$1$ has only one positive factor, while a prime has exactly two. Therefore $1$ is
neither prime nor composite.

### 8.2 Stopping before all factors are prime

The statement $72=8\cdot9$ is a factorization, but not a **prime** factorization.
Continue:

$$72=2^3\cdot3^2.$$

### 8.3 Testing too many possible divisors

For primality, do not test all numbers below $n$. Once every prime at most $\sqrt n$
has been checked, the test is complete.

### 8.4 Assuming an odd number is prime

Odd numbers are not divisible by $2$, but many are composite: $39=3\cdot13$ and
$91=7\cdot13$.

## Takeaway

For a positive integer greater than $1$, there are exactly two possibilities:

- **prime:** its only positive factors are $1$ and itself;
- **composite:** it can be expressed as a product of two smaller positive integers.

To test a number for primality, check prime divisors through its square root. To prime
factor a composite number, keep splitting or dividing until every remaining factor is
prime.
