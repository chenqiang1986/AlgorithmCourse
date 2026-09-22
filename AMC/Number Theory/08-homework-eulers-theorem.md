# Homework: Euler's Theorem & Powers Modulo $n$
*AMC / Number Theory*

This homework accompanies [Lesson 8](./08-eulers-theorem.md). Before reducing an
exponent with Euler's theorem, explicitly check that the base and modulus are
relatively prime.

## Part A: Conditions and Totients

### Problem 1

For each pair $(a,n)$, decide whether Euler's theorem applies directly:

1. $(7,24)$
2. $(9,27)$
3. $(14,25)$
4. $(21,35)$

<details>
<summary>Solution</summary>

It applies exactly when the GCD is $1$.

1. $\gcd(7,24)=1$: yes.
2. $\gcd(9,27)=9$: no.
3. $\gcd(14,25)=1$: yes.
4. $\gcd(21,35)=7$: no.

</details>

### Problem 2

Find $\varphi(36)$, $\varphi(50)$, and $\varphi(77)$.

<details>
<summary>Solution</summary>

$$\varphi(36)=36\left(1-\frac12\right)\left(1-\frac13\right)=\boxed{12},$$

$$\varphi(50)=50\left(1-\frac12\right)\left(1-\frac15\right)=\boxed{20},$$

and

$$\varphi(77)=77\left(1-\frac17\right)\left(1-\frac1{11}\right)=\boxed{60}. $$

</details>

## Part B: Apply Euler's Theorem

### Problem 3

Find $5^{123}\pmod {28}$.

<details>
<summary>Solution</summary>

$\gcd(5,28)=1$ and $\varphi(28)=12$. Since $123=10\cdot12+3$,

$$5^{123}\equiv5^3=125\equiv\boxed{13}\pmod {28}. $$

</details>

### Problem 4

Find $3^{1000}\pmod {35}$.

<details>
<summary>Solution</summary>

$\gcd(3,35)=1$ and $\varphi(35)=24$. Since $1000=41\cdot24+16$,

$$3^{1000}\equiv3^{16}\pmod {35}.$$

Now $3^4=81\equiv11\pmod {35}$, so

$$3^{16}\equiv11^4\equiv16^2=256\equiv\boxed{11}\pmod {35}. $$

</details>

### Problem 5

Find the last digit of $7^{202}$.

<details>
<summary>Solution</summary>

Work modulo $10$. Since $\gcd(7,10)=1$ and $\varphi(10)=4$,

$$7^{202}\equiv7^2=49\equiv\boxed{9}\pmod {10}. $$

</details>

### Problem 6

Find the last two digits of $7^{100}$.

<details>
<summary>Solution</summary>

Work modulo $100$. Since $\gcd(7,100)=1$ and $\varphi(100)=40$,

$$7^{100}\equiv7^{20}\pmod {100}.$$

Because $7^4=2401\equiv1\pmod {100}$, we get

$$7^{20}=(7^4)^5\equiv\boxed{1}\pmod {100}. $$

The last two digits are $\boxed{01}$.

</details>

## Part C: Reasoning and Proof

### Problem 7

Explain why multiplication by $a$ sends the reduced residue system modulo $n$
to itself, provided that $\gcd(a,n)=1$.

<details>
<summary>Solution</summary>

Every product $ar$ is relatively prime to $n$, because neither $a$ nor $r$
shares a prime factor with $n$. If $ar_i\equiv ar_j\pmod n$, the inverse of
$a$ modulo $n$ gives $r_i\equiv r_j\pmod n$. Thus the products are distinct
coprime residue classes. There are $\varphi(n)$ of them, so they are exactly a
rearrangement of the reduced residue system.

</details>

### Problem 8

Prove that if $\gcd(x,n)=1$ and $\gcd(y,n)=1$, then
$\gcd(xy,n)=1$.

<details>
<summary>Solution</summary>

Suppose a prime $p$ divided both $xy$ and $n$. Since $p$ is prime and divides
$xy$, it divides $x$ or $y$. That would contradict $\gcd(x,n)=1$ or
$\gcd(y,n)=1$. No prime divides both $xy$ and $n$, so

$$\boxed{\gcd(xy,n)=1}.\qquad\square$$

</details>

### Problem 9

Show that $2^{30}\equiv1\pmod {31}$ without calculating $2^{30}$.

<details>
<summary>Solution</summary>

The modulus $31$ is prime, so $\varphi(31)=30$. Also $31\nmid2$. Fermat's
little theorem, or Euler's theorem, gives

$$\boxed{2^{30}\equiv1\pmod {31}.}$$

</details>

## Part D: When the Condition Fails

### Problem 10

Why is it invalid to conclude that $6^8\equiv1\pmod {15}$ from
$\varphi(15)=8$? Find the actual remainder of $6^8$ modulo $15$.

<details>
<summary>Solution</summary>

$\gcd(6,15)=3\ne1$, so Euler's theorem does not apply to modulus $15$ as a
whole. Split $15=3\cdot5$. Then

$$6^8\equiv0\pmod3.$$

Modulo $5$, the base is coprime to the modulus and $6\equiv1\pmod5$, so

$$6^8\equiv1\pmod5.$$

The CRT system $x\equiv0\pmod3$, $x\equiv1\pmod5$ has solution $x\equiv6\pmod {15}$.
Therefore

$$\boxed{6^8\equiv6\pmod {15}.}$$

</details>

### Problem 11

Find $18^{100}\pmod {100}$ by splitting the modulus and using CRT. Do not find
a power cycle by enumeration.

<details>
<summary>Solution</summary>

Euler's theorem does not apply directly because $\gcd(18,100)=2$. Split

$$100=4\cdot25.$$

Since $4\mid18^{100}$,

$$18^{100}\equiv0\pmod4.$$

Since $\gcd(18,25)=1$ and $\varphi(25)=20$,

$$18^{100}\equiv18^{100\bmod20}=18^0\equiv1\pmod {25}.$$

Write $x=1+25k$. The condition $x\equiv0\pmod4$ becomes

$$1+k\equiv0\pmod4,$$

so $k\equiv3\pmod4$. Taking $k=3$ gives

$$\boxed{18^{100}\equiv76\pmod {100}.}$$

</details>

### Problem 12

Find $30^{100}\pmod {196}$ by splitting the modulus and using CRT. Do not find
a power cycle by enumeration.

<details>
<summary>Solution</summary>

Split $196=4\cdot49$. Since $4\mid30^{100}$,

$$30^{100}\equiv0\pmod4.$$

Also $\gcd(30,49)=1$, and $\varphi(49)=42$. Because $100\equiv16\pmod {42}$,

$$30^{100}\equiv30^{16}\pmod {49}.$$

Repeated squaring, not cycle enumeration, gives

$$30^2\equiv18\pmod {49},\qquad30^4\equiv18^2\equiv30\pmod {49},$$

so $30^{16}\equiv30\pmod {49}$. Solve

$$x\equiv0\pmod4,\qquad x\equiv30\pmod {49}.$$

Writing $x=30+49k$, the first congruence gives $2+k\equiv0\pmod4$.
Take $k=2$, yielding

$$\boxed{30^{100}\equiv128\pmod {196}.}$$

</details>

### Problem 13

Find $12^{50}\pmod {18}$ without using Euler's theorem directly.

<details>
<summary>Solution</summary>

Euler's theorem does not apply because $\gcd(12,18)=6$. Instead,

$$12^2=144\equiv0\pmod {18}.$$

Thus every power of $12$ with exponent at least $2$ is congruent to $0$, and

$$\boxed{12^{50}\equiv0\pmod {18}.}$$

</details>

## Part E: Exponent Towers

### Problem 14

Find $12^{5^{100}}\pmod {175}$. Use Euler's theorem repeatedly where it applies,
and split a modulus with CRT where it does not. Do not enumerate power cycles.

<details>
<summary>Solution</summary>

Since $\gcd(12,175)=1$ and $\varphi(175)=120$, we first need

$$5^{100}\pmod {120}.$$

Euler's theorem does not apply directly here because $\gcd(5,120)=5$. Split

$$120=5\cdot24.$$

The shared-factor part is

$$5^{100}\equiv0\pmod5.$$

For the coprime part, $\gcd(5,24)=1$ and $\varphi(24)=8$. Thus

$$5^{100}\equiv5^4=625\equiv1\pmod {24}.$$

Solve $e\equiv0\pmod5$ and $e\equiv1\pmod {24}$. Write $e=1+24k$.
Since $1+24k\equiv1-k\equiv0\pmod5$, we may take $k=1$, so

$$5^{100}\equiv25\pmod {120}.$$

Therefore

$$12^{5^{100}}\equiv12^{25}\pmod {175}.$$

Repeated squaring gives

$$12^4\equiv86\pmod {175},\qquad12^8\equiv46\pmod {175},
\qquad12^{16}\equiv16\pmod {175}.$$

Hence

$$12^{25}=12^{16}12^8\cdot12\equiv16\cdot46\cdot12
\equiv\boxed{82}\pmod {175}. $$

</details>

## Key Reminders

- Euler's theorem is $a^{\varphi(n)}\equiv1\pmod n$ only when $\gcd(a,n)=1$.
- Find $\varphi(n)$ using the distinct prime factors of $n$.
- Reduce the exponent modulo $\varphi(n)$ only after the GCD check.
- If the GCD is not $1$, split the modulus into a shared-factor part and a
  coprime part when possible; then use CRT to recombine the remainders.
- For $a^{b^c}\pmod n$, reduce $b^c$ modulo $\varphi(n)$ when the outer base is
  coprime to $n$; apply the same reasoning again to that inner power.
