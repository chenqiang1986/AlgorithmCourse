# Number Theory Syllabus
*AMC / Number Theory*

A 12-week introduction to elementary number theory. The course develops the language of
divisibility, then uses that language to solve increasingly powerful problems involving
factorization, greatest common divisors, congruences, and counting.

## Course Goals

By the end of the course, students will be able to:

- use divisibility and congruence notation precisely;
- factor integers into primes and apply prime exponents to divisor problems;
- compute and use the greatest common divisor and least common multiple;
- apply the Euclidean and extended Euclidean algorithms;
- solve linear congruences and systems of congruences; and
- use Euler's totient function and Euler's theorem in modular arithmetic.

## Unit 1: Divisibility & Congruences (Weeks 1–2)

**Core Focus:** Building the vocabulary for describing how integers divide one another and
how remainders organize integers into classes.

- Week 1: Divisibility: the definition $a \mid b$, divisors (factors), multiples, and
  basic divisibility properties.
- Week 2: Division with remainder and modular congruence:
  $a \equiv b \pmod n$ means that $n \mid (a-b)$; addition, subtraction, and
  multiplication with congruences.

**Essential Question:** When do two integers behave the same way with respect to a given
divisor?

## Unit 2: Primes & Prime Factorization (Weeks 3–4)

**Core Focus:** Seeing prime numbers as the irreducible building blocks of the positive
integers.

- Week 3: Prime and composite numbers, testing for primality, and the role of $1$.
- Week 4: The Fundamental Theorem of Arithmetic: unique prime factorization; representing
  an integer as $p_1^{a_1}p_2^{a_2}\cdots p_k^{a_k}$.

**Essential Question:** Why does every positive integer have a unique collection of prime
building blocks?

## Unit 3: GCD, LCM & Prime-Exponent Methods (Weeks 5–6)

**Core Focus:** Comparing factor structures to find shared factors and the smallest shared
multiple.

- Week 5: Greatest common divisor, least common multiple, relatively prime integers, and
  the relationship $\gcd(a,b)\operatorname{lcm}(a,b)=ab$ for positive integers.
- Week 6: Finding $\gcd$ and $\operatorname{lcm}$ from prime decompositions by selecting
  minimum and maximum prime exponents; applications to fractions and periodic events.

**Essential Question:** How does an integer's prime factorization reveal what it shares
with another integer?

## Unit 4: The Euclidean Algorithm (Weeks 7–8)

**Core Focus:** Replacing factor lists with a fast, reliable procedure for finding a
greatest common divisor.

- Week 7: The division algorithm and the fact that
  $\gcd(a,b)=\gcd(b,r)$ when $a=bq+r$.
- Week 8: Executing the Euclidean algorithm, interpreting its final nonzero remainder,
  and using it to decide whether two integers are relatively prime.

**Essential Question:** Why can repeated division find the common factors of even very
large integers?

## Unit 5: Bézout's Identity, Linear Congruences & CRT (Weeks 9–10)

**Core Focus:** Turning greatest-common-divisor information into solutions of equations
and simultaneous remainder conditions.

- Week 9: Bézout's identity and the extended Euclidean algorithm; solving
  $ax+by=c$ and determining when integer solutions exist.
- Week 10: Solving linear congruences $ax\equiv b\pmod n$, modular inverses, and the
  Chinese Remainder Theorem for systems with pairwise relatively prime moduli.

**Essential Question:** How can a common-divisor calculation unlock an equation or a set
of remainder constraints?

## Unit 6: Divisor Counting, Euler's Totient & Euler's Theorem (Weeks 11–12)

**Core Focus:** Counting arithmetic structures from prime factorizations and applying the
result to powers modulo $n$.

- Week 11: Counting positive divisors of
  $n=p_1^{a_1}p_2^{a_2}\cdots p_k^{a_k}$ using
  $\tau(n)=(a_1+1)(a_2+1)\cdots(a_k+1)$; introduction to Euler's totient function
  $\varphi(n)$, which counts integers from $1$ to $n$ that are relatively prime to $n$.
- Week 12: Computing $\varphi(n)$ from a prime factorization and applying Euler's theorem:
  if $\gcd(a,n)=1$, then $a^{\varphi(n)}\equiv1\pmod n$; review and cumulative problem
  solving.

**Essential Question:** How can prime factorization count both divisors and the numbers
that are relatively prime to a given integer?

## Suggested Assessment Sequence

- End of Week 4: Quiz on divisibility, congruences, primes, and factorization.
- End of Week 8: Quiz on gcd/lcm and the Euclidean algorithm.
- End of Week 10: Problem set on Bézout's identity, linear congruences, and CRT.
- Week 12: Cumulative assessment connecting factorization, gcd, congruences, and Euler's
  theorem.
