# Lesson 3: GCD, LCM, and Prime-Exponent Methods
*AMC / Number Theory*

Prime factorization lets us compare integers one prime at a time. In this lesson, we
use that viewpoint to find the **greatest common divisor** (GCD), the **least common
multiple** (LCM), and to solve problems involving fractions and repeating events.

## 1. Greatest Common Divisor

For positive integers $a$ and $b$, the **greatest common divisor**, written

$$\gcd(a,b),$$

is the largest positive integer that divides both $a$ and $b$. It is also called the
**greatest common factor** (GCF).

For example, the common positive divisors of $18$ and $30$ are

$$1,2,3,6.$$

Therefore

$$\gcd(18,30)=6.$$

Two positive integers are **relatively prime** (or **coprime**) when their GCD is $1$.
They need not be prime themselves: $8$ and $15$ are relatively prime because they
share no prime factor.

### A Useful Interpretation

If $d=\gcd(a,b)$, then $d$ is the largest size of identical groups into which both
$a$ and $b$ items can be split with no leftovers. For instance, $18$ red beads and
$30$ blue beads can be put into $6$ identical groups, each with $3$ red beads and
$5$ blue beads. No larger number of identical groups is possible.

## 2. Least Common Multiple

For positive integers $a$ and $b$, the **least common multiple**, written

$$\operatorname{lcm}(a,b),$$

is the smallest positive integer divisible by both $a$ and $b$.

The multiples of $6$ and $8$ begin as follows:

$$\begin{array}{c|l}
6&6,12,18,24,30,36,\ldots\\
8&8,16,24,32,40,48,\ldots
\end{array}$$

The first shared positive multiple is $24$, so

$$\operatorname{lcm}(6,8)=24.$$

Listing multiples works for small numbers, but it becomes slow and unreliable for
large numbers. Prime factorization gives a method that works every time.

## 3. Prime Exponents: Minimum for GCD, Maximum for LCM

Write both numbers using the same list of primes, allowing exponent $0$ when a prime
does not occur. For example,

$$360=2^3\cdot3^2\cdot5^1,\qquad840=2^3\cdot3^1\cdot5^1\cdot7^1.$$

To divide **both** numbers, a prime power cannot ask for more copies of a prime than
either number has. Thus a GCD uses the **smaller exponent** for each prime:

$$\gcd(360,840)=2^{\min(3,3)}\cdot3^{\min(2,1)}\cdot5^{\min(1,1)}\cdot7^{\min(0,1)}$$

$$=2^3\cdot3\cdot5=120.$$

To be a multiple of **both** numbers, an LCM must supply enough copies of every prime
for either number. Thus an LCM uses the **larger exponent** for each prime:

$$\operatorname{lcm}(360,840)=2^{\max(3,3)}\cdot3^{\max(2,1)}\cdot5^{\max(1,1)}\cdot7^{\max(0,1)}$$

$$=2^3\cdot3^2\cdot5\cdot7=2{,}520.$$

### The Rule in General

Suppose

$$a=\prod_p p^{\alpha_p},\qquad b=\prod_p p^{\beta_p},$$

where the product ranges over all primes appearing in at least one factorization.
Then

$$\gcd(a,b)=\prod_p p^{\min(\alpha_p,\beta_p)}$$

and

$$\operatorname{lcm}(a,b)=\prod_p p^{\max(\alpha_p,\beta_p)}.$$

An exponent of $0$ means that the prime is absent, since $p^0=1$.

### Why These Rules Work

A number $d$ divides $a$ precisely when every prime exponent in $d$ is at most the
matching exponent in $a$. If $d$ is to divide both $a$ and $b$, each exponent must be
at most both exponents, so the largest possible choice is their minimum.

Likewise, if $m$ is a multiple of both $a$ and $b$, each exponent in $m$ must be at
least both exponents, so the smallest possible choice is their maximum.

## 4. A Reliable Factorization Table

For $252$ and $660$, first factor:

$$252=2^2\cdot3^2\cdot7,\qquad660=2^2\cdot3\cdot5\cdot11.$$

Then align the exponents.

| Prime | exponent in $252$ | exponent in $660$ | GCD: minimum | LCM: maximum |
| --- | ---: | ---: | ---: | ---: |
| $2$ | $2$ | $2$ | $2$ | $2$ |
| $3$ | $2$ | $1$ | $1$ | $2$ |
| $5$ | $0$ | $1$ | $0$ | $1$ |
| $7$ | $1$ | $0$ | $0$ | $1$ |
| $11$ | $0$ | $1$ | $0$ | $1$ |

Therefore

$$\gcd(252,660)=2^2\cdot3=12$$

and

$$\operatorname{lcm}(252,660)=2^2\cdot3^2\cdot5\cdot7\cdot11=13{,}860.$$

This table makes an important detail visible: a prime that occurs in only one number
has exponent $0$ in the other. It contributes nothing to the GCD but must appear in
the LCM.

## 5. The Product Formula

For positive integers $a$ and $b$,

$$\boxed{\gcd(a,b)\operatorname{lcm}(a,b)=ab.}$$

For $252$ and $660$, the formula checks our work:

$$12\cdot13{,}860=166{,}320=252\cdot660.$$

The prime-exponent explanation is especially clean. For any prime $p$ with exponents
$\alpha$ in $a$ and $\beta$ in $b$,

$$\min(\alpha,\beta)+\max(\alpha,\beta)=\alpha+\beta.$$

So multiplying the GCD and LCM supplies exactly the same total exponent of every
prime as multiplying $a$ and $b$.

The formula can also be used to find an LCM efficiently once a GCD is known:

$$\operatorname{lcm}(a,b)=\frac{ab}{\gcd(a,b)}.$$

For example, since $\gcd(84,150)=6$,

$$\operatorname{lcm}(84,150)=\frac{84\cdot150}{6}=2{,}100.$$

This formula is for **positive** integers in this course. When calculating by hand,
divide by the GCD before multiplying when possible; it keeps numbers smaller.

## 6. Applications

### Reducing a Fraction

To reduce $\frac{84}{150}$, divide numerator and denominator by their GCD:

$$\gcd(84,150)=6,$$

so

$$\frac{84}{150}=\frac{84\div6}{150\div6}=\frac{14}{25}.$$

The result is in lowest terms because $\gcd(14,25)=1$.

In prime-exponent language, reducing a fraction removes the prime powers shared by
the numerator and denominator—exactly the GCD.

### Adding Fractions

The least common denominator of $\frac{5}{12}$ and $\frac{7}{18}$ is

$$\operatorname{lcm}(12,18)=36.$$

Thus

$$\frac{5}{12}+\frac{7}{18}=\frac{15}{36}+\frac{14}{36}=\frac{29}{36}.$$

The product $12\cdot18=216$ would also be a common denominator, but it is not the
least one and creates unnecessary work.

### Repeating Events

Two lights flash together at noon. One flashes every $18$ seconds and the other every
$24$ seconds. They next flash together after

$$\operatorname{lcm}(18,24)=72$$

seconds, so the next simultaneous flash is at **12:01:12**.

An LCM answers “when do repeating schedules next line up?” It is a time interval, so
be sure all periods use the same unit before finding it.

## 7. Class Practice

### Problem 1

Find $\gcd(72,126)$ and $\operatorname{lcm}(72,126)$ using prime factorizations.

<details>
<summary>Solution</summary>

$$72=2^3\cdot3^2,\qquad126=2\cdot3^2\cdot7.$$

For the GCD, take minimum exponents:

$$\gcd(72,126)=2\cdot3^2=18.$$

For the LCM, take maximum exponents:

$$\operatorname{lcm}(72,126)=2^3\cdot3^2\cdot7=504.$$

</details>

### Problem 2

Are $35$ and $48$ relatively prime? Explain using prime factorization.

<details>
<summary>Solution</summary>

$$35=5\cdot7,\qquad48=2^4\cdot3.$$

They have no prime factor in common, so

$$\gcd(35,48)=1.$$

Therefore they are relatively prime.

</details>

### Problem 3

Find the least positive integer that is divisible by $24$, $90$, and $140$.

<details>
<summary>Solution</summary>

Factor all three numbers:

$$24=2^3\cdot3,\qquad90=2\cdot3^2\cdot5,\qquad140=2^2\cdot5\cdot7.$$

Take the largest exponent of each prime:

$$2^3\cdot3^2\cdot5\cdot7=2{,}520.$$

The answer is $\boxed{2{,}520}$.

</details>

### Problem 4

Two positive integers have GCD $12$ and LCM $420$. If one integer is $60$, find the
other.

<details>
<summary>Solution</summary>

Use the product formula. If the other number is $x$, then

$$12\cdot420=60x.$$

Therefore

$$x=\frac{12\cdot420}{60}=84.$$

A check: $\gcd(60,84)=12$ and $\operatorname{lcm}(60,84)=420$.

</details>

### Problem 5

Three bells ring together at 9:00 AM. They ring every $8$, $12$, and $18$ minutes,
respectively. When will all three next ring together?

<details>
<summary>Solution</summary>

$$8=2^3,\qquad12=2^2\cdot3,\qquad18=2\cdot3^2.$$

Thus

$$\operatorname{lcm}(8,12,18)=2^3\cdot3^2=72.$$

They next ring together $72$ minutes after 9:00 AM, at **10:12 AM**.

</details>

## 8. Common Mistakes

### 8.1 Using maximum exponents for the GCD

Maximum exponents make a number large enough to be a multiple of both numbers. That
is the LCM. A common divisor must fit inside both factorizations, so use minimum
exponents for the GCD.

### 8.2 Omitting a prime that occurs in only one number

For $12=2^2\cdot3$ and $25=5^2$, the GCD is $1$, but the LCM is

$$2^2\cdot3\cdot5^2=300.$$

The $5^2$ must appear in the LCM even though it does not divide $12$.

### 8.3 Confusing “relatively prime” with “both prime”

$8$ and $15$ are relatively prime, even though both are composite. Conversely, two
different primes are relatively prime, but primality is not required.

### 8.4 Multiplying denominators automatically

For fraction addition, the product of denominators is always a common denominator,
but it may be much larger than needed. Use the LCM for the least common denominator.

## Takeaway

Prime factorizations turn GCD and LCM into an exponent comparison:

- For a **GCD**, keep every prime at its **smallest** exponent.
- For an **LCM**, keep every prime at its **largest** exponent.

For positive integers,

$$\gcd(a,b)\operatorname{lcm}(a,b)=ab.$$

Use GCDs to remove shared factors and LCMs to coordinate quantities that must work
for every number at once.
