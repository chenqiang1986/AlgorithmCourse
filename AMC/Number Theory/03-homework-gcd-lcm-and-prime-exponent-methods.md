# Homework: GCD, LCM, and Prime-Exponent Methods
*AMC / Number Theory*

This homework accompanies [Lesson 3](./03-gcd-lcm-and-prime-exponent-methods.md).
Show prime factorizations when using prime-exponent methods. For every GCD, explain
which exponents are kept; for every LCM, include every required prime.

## Part A: GCD and LCM Fluency

### Problem 1

Find $\gcd(84,198)$ and $\operatorname{lcm}(84,198)$ using prime factorization.

<details>
<summary>Solution</summary>

$$84=2^2\cdot3\cdot7,\qquad198=2\cdot3^2\cdot11.$$

The minimum exponents give

$$\gcd(84,198)=2\cdot3=6.$$

The maximum exponents give

$$\operatorname{lcm}(84,198)=2^2\cdot3^2\cdot7\cdot11=2{,}772.$$

</details>

### Problem 2

Find $\gcd(360,924)$ and $\operatorname{lcm}(360,924)$.

<details>
<summary>Solution</summary>

$$360=2^3\cdot3^2\cdot5,\qquad924=2^2\cdot3\cdot7\cdot11.$$

Thus

$$\gcd(360,924)=2^2\cdot3=12$$

and

$$\operatorname{lcm}(360,924)=2^3\cdot3^2\cdot5\cdot7\cdot11=27{,}720.$$

</details>

### Problem 3

Without listing all factors or multiples, find $\gcd(96,140)$ and
$\operatorname{lcm}(96,140)$.

<details>
<summary>Solution</summary>

$$96=2^5\cdot3,\qquad140=2^2\cdot5\cdot7.$$

Therefore

$$\gcd(96,140)=2^2=4$$

and

$$\operatorname{lcm}(96,140)=2^5\cdot3\cdot5\cdot7=3{,}360.$$

</details>

### Problem 4

For each pair, decide whether the two numbers are relatively prime. Justify your
answer.

1. $49$ and $64$
2. $45$ and $77$
3. $65$ and $91$
4. $72$ and $125$

<details>
<summary>Solution</summary>

$$49=7^2,\quad64=2^6;\qquad45=3^2\cdot5,\quad77=7\cdot11;$$

$$65=5\cdot13,\quad91=7\cdot13;\qquad72=2^3\cdot3^2,\quad125=5^3.$$

The pairs $(49,64)$, $(45,77)$, and $(72,125)$ have no prime factor in common, so
each is relatively prime. The pair $(65,91)$ is not relatively prime because

$$\gcd(65,91)=13.$$

</details>

### Problem 5

Let

$$N=2^a\cdot3^b\cdot5^2,$$

where $a$ and $b$ are nonnegative integers. Suppose

$$\gcd\bigl(N,2^4\cdot3^3\cdot5\bigr)=2^2\cdot3^2\cdot5$$

and

$$\operatorname{lcm}\bigl(N,2^4\cdot3^3\cdot5\bigr)=2^4\cdot3^3\cdot5^2.$$

Find $N$.

<details>
<summary>Solution</summary>

The exponent of $2$ in the GCD is $\min(a,4)=2$, so $a=2$. Likewise,

the exponent of $3$ in the GCD is $\min(b,3)=2$, so $b=2$. (These values also
agree with the stated LCM.) Therefore

$$N=2^2\cdot3^2\cdot5^2=900.$$

</details>

## Part B: Using the GCD–LCM Relationship

### Problem 6

Use

$$\gcd(a,b)\operatorname{lcm}(a,b)=ab$$

to find $\operatorname{lcm}(144,210)$, given that $\gcd(144,210)=6$.

<details>
<summary>Solution</summary>

$$\operatorname{lcm}(144,210)=\frac{144\cdot210}{6}=144\cdot35=5{,}040.$$

</details>

### Problem 7

Two positive integers have GCD $18$ and LCM $756$. One of the integers is $108$.
Find the other integer, then check both the GCD and LCM by factoring.

<details>
<summary>Solution</summary>

If the other integer is $x$, then

$$18\cdot756=108x.$$

Thus

$$x=\frac{18\cdot756}{108}=126.$$

Now factor:

$$108=2^2\cdot3^3,\qquad126=2\cdot3^2\cdot7.$$

The minimum exponents give $2\cdot3^2=18$, and the maximum exponents give

$$2^2\cdot3^3\cdot7=756.$$

</details>

### Problem 8

If $a$ and $b$ are relatively prime positive integers, prove that

$$\operatorname{lcm}(a,b)=ab.$$

<details>
<summary>Solution</summary>

Because $a$ and $b$ are relatively prime, $\gcd(a,b)=1$. The product formula gives

$$\gcd(a,b)\operatorname{lcm}(a,b)=ab.$$

Substitute $\gcd(a,b)=1$:

$$1\cdot\operatorname{lcm}(a,b)=ab.$$

Therefore $\operatorname{lcm}(a,b)=ab$.

</details>

### Problem 9

Reduce each fraction to lowest terms.

1. $\frac{198}{462}$
2. $\frac{504}{1{,}176}$

<details>
<summary>Solution</summary>

For the first fraction,

$$198=2\cdot3^2\cdot11,\qquad462=2\cdot3\cdot7\cdot11,$$

so the GCD is $66$. Hence

$$\frac{198}{462}=\frac{3}{7}.$$

For the second fraction,

$$504=2^3\cdot3^2\cdot7,\qquad1{,}176=2^3\cdot3\cdot7^2,$$

so the GCD is $168$. Hence

$$\frac{504}{1{,}176}=\frac{3}{7}.$$

</details>

## Part C: Common-Denominator and Repeating-Event Applications

### Problem 10

Compute $\frac{7}{24}+\frac{5}{36}$ using the least common denominator. Give the
answer in lowest terms.

<details>
<summary>Solution</summary>

$$24=2^3\cdot3,\qquad36=2^2\cdot3^2,$$

so the least common denominator is

$$\operatorname{lcm}(24,36)=2^3\cdot3^2=72.$$

Therefore

$$\frac{7}{24}+\frac{5}{36}=\frac{21}{72}+\frac{10}{72}=\frac{31}{72}.$$

Since $31$ is prime and does not divide $72$, the fraction is already in lowest terms.

</details>

### Problem 11

A teacher has $96$ pencils and $144$ erasers. She wants to make the greatest possible
number of identical prize bags, using all the items. How many bags can she make, and
what goes in each bag?

<details>
<summary>Solution</summary>

The greatest possible number of bags is

$$\gcd(96,144)=48.$$

Each bag contains

$$96\div48=2\text{ pencils and }144\div48=3\text{ erasers}.$$

</details>

### Problem 12

Three buses leave a terminal together at 7:30 AM. Their routes take $20$, $30$, and
$45$ minutes, respectively. At what time will all three next leave the terminal
together?

<details>
<summary>Solution</summary>

$$20=2^2\cdot5,\qquad30=2\cdot3\cdot5,\qquad45=3^2\cdot5.$$

Thus

$$\operatorname{lcm}(20,30,45)=2^2\cdot3^2\cdot5=180$$

minutes. This is $3$ hours, so the buses next leave together at **10:30 AM**.

</details>

### Problem 13

Find the smallest positive integer that leaves remainder $0$ when divided by both
$42$ and $56$, and leaves remainder $1$ when divided by $5$.

<details>
<summary>Solution</summary>

The number must be a multiple of

$$\operatorname{lcm}(42,56).$$

Since

$$42=2\cdot3\cdot7,\qquad56=2^3\cdot7,$$

we have

$$\operatorname{lcm}(42,56)=2^3\cdot3\cdot7=168.$$

The multiples of $168$ are $168,336,504,672,840,\ldots$. Their remainders modulo $5$
are $3,1,4,2,0,\ldots$, so the first with remainder $1$ is

$$\boxed{336}.$$

</details>

## Part D: Challenge

### Problem 14

Suppose

$$\gcd(m,n)=12\qquad\text{and}\qquad\operatorname{lcm}(m,n)=720.$$

Can $m+n=100$? Explain.

<details>
<summary>Solution</summary>

The product formula requires

$$mn=12\cdot720=8{,}640.$$

If $m+n=100$, then $m$ and $n$ would be roots of

$$x^2-100x+8{,}640=0.$$

Its discriminant is

$$100^2-4(8{,}640)=10{,}000-34{,}560<0,$$

so there are not even real numbers, and therefore no positive integers, with this sum
and product. Thus **$m+n$ cannot equal $100$**.

</details>

### Problem 15

Prove that if $d=\gcd(a,b)$, then $d\mid(a+b)$ and $d\mid(a-b)$.

<details>
<summary>Solution</summary>

By definition of GCD, $d\mid a$ and $d\mid b$. Thus there are integers $r$ and $s$
such that

$$a=dr,\qquad b=ds.$$

Then

$$a+b=dr+ds=d(r+s)$$

and

$$a-b=dr-ds=d(r-s).$$

Because $r+s$ and $r-s$ are integers, $d\mid(a+b)$ and $d\mid(a-b)$.

</details>

## Submission Checklist

- Use minimum exponents for GCDs and maximum exponents for LCMs.
- Include primes with exponent $0$ when comparing factorizations.
- Reduce a fraction by its GCD.
- Convert time units before applying an LCM to a schedule problem.
