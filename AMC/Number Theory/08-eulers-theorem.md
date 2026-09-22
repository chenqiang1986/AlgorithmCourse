# Lesson 8: Euler's Theorem & Powers Modulo $n$
*AMC / Number Theory*

Euler's totient function counts the residue classes that have multiplicative
inverses modulo $n$. Euler's theorem turns that count into a powerful rule for
simplifying large powers.

## Learning Goals

By the end of this lesson, you will be able to:

- state Euler's theorem with its required relative-primality condition;
- use a reduced residue system to explain why the theorem is true;
- reduce large exponents modulo $\varphi(n)$ when the theorem applies; and
- recognize when Euler's theorem cannot be used directly.

## 1. The Theorem

Recall that $\varphi(n)$ is the number of integers from $1$ through $n$ that
are relatively prime to $n$.

### Euler's Theorem

If $\gcd(a,n)=1$, then

$$\boxed{a^{\varphi(n)}\equiv1\pmod n.}$$

The condition $\gcd(a,n)=1$ is not optional. It says that $a$ and the modulus
$n$ share no prime factor.

### Example: A Direct Use

Since $\gcd(2,15)=1$ and $\varphi(15)=8$,

$$2^8\equiv1\pmod{15}.$$

Indeed, $2^8=256=15\cdot17+1$.

### Why Relative Primality Matters

It is false in general that $a^{\varphi(n)}\equiv1\pmod n$. For example,

$$\varphi(8)=4,$$

but $\gcd(2,8)\ne1$ and

$$2^4=16\equiv0\not\equiv1\pmod8.$$

Before using Euler's theorem, always check $\boxed{\gcd(a,n)=1}$.

## 2. The Coprime Residues Modulo $n$

Choose the $\varphi(n)$ numbers between $1$ and $n$ that are relatively prime
to $n$, and call them

$$r_1,r_2,\ldots,r_{\varphi(n)}.$$

They form a **reduced residue system modulo $n$**. For example, modulo $10$ the
coprime residues are

$$1,3,7,9.$$

Now suppose $\gcd(a,n)=1$. Multiplying every member of this list by $a$ gives

$$ar_1,ar_2,\ldots,ar_{\varphi(n)}.$$

When reduced modulo $n$, these are exactly the same coprime residue classes,
only possibly in a different order.

### Why Nothing Disappears or Repeats

First, each $ar_i$ is relatively prime to $n$: a common divisor of $ar_i$ and
$n$ would have to divide either $a$ or $r_i$, but neither has a common prime
factor with $n$.

Also, suppose two products give the same remainder:

$$ar_i\equiv ar_j\pmod n.$$

Because $\gcd(a,n)=1$, $a$ has a multiplicative inverse modulo $n$. Multiply
both sides by that inverse to obtain

$$r_i\equiv r_j\pmod n.$$

The original residues were distinct, so $i=j$. Thus multiplication by $a$
permutes the coprime residue classes.

### Example: Multiplying the Reduced Residues Modulo $10$

Take $a=3$, which is relatively prime to $10$:

$$\begin{array}{c|cccc}
r&1&3&7&9\\ \hline
3r\pmod {10}&3&9&1&7
\end{array}$$

The second row is a rearrangement of $1,3,7,9$.

## 3. Proof of Euler's Theorem

Because multiplying the reduced residue system by $a$ only rearranges it,
the products of its entries are congruent:

$$
(ar_1)(ar_2)\cdots(ar_{\varphi(n)})
\equiv r_1r_2\cdots r_{\varphi(n)}\pmod n.
$$

Factor the left side:

$$a^{\varphi(n)}r_1r_2\cdots r_{\varphi(n)}
\equiv r_1r_2\cdots r_{\varphi(n)}\pmod n.$$

Every $r_i$ is relatively prime to $n$, so their product is also relatively
prime to $n$. It has an inverse modulo $n$, and we may cancel it from both
sides. Therefore

$$\boxed{a^{\varphi(n)}\equiv1\pmod n.}\qquad\square$$

This is a special kind of cancellation: we may cancel a factor modulo $n$ only
when that factor is relatively prime to $n$.

## 4. Reducing Large Exponents

If $\gcd(a,n)=1$, Euler's theorem gives a cycle block:

$$a^{\varphi(n)}\equiv1\pmod n.$$

Write an exponent $E$ as

$$E=q\varphi(n)+r,\qquad 0\le r<\varphi(n).$$

Then

$$a^E=a^{q\varphi(n)+r}=(a^{\varphi(n)})^q a^r
\equiv1^q a^r\equiv a^r\pmod n.$$

So, once the GCD condition is checked, reduce the exponent modulo $\varphi(n)$.

### Example: Find $7^{100}\pmod{20}$

First, $\gcd(7,20)=1$. Since

$$\varphi(20)=20\left(1-\frac12\right)\left(1-\frac15\right)=8,$$

Euler's theorem gives $7^8\equiv1\pmod {20}$. Since

$$100=12\cdot8+4,$$

$$7^{100}\equiv7^4\pmod {20}.$$

Finally,

$$7^2=49\equiv9\pmod {20},\qquad7^4\equiv9^2=81\equiv\boxed{1}\pmod {20}.$$

### Example: Find the Last Two Digits of $3^{100}$

The last two digits are the remainder modulo $100$. Because $\gcd(3,100)=1$,

$$\varphi(100)=100\left(1-\frac12\right)\left(1-\frac15\right)=40.$$

Since $100=2\cdot40+20$,

$$3^{100}\equiv3^{20}\pmod {100}.$$

Repeated squaring gives

$$3^4=81\equiv-19\pmod {100},$$

$$3^{20}=(3^4)^5\equiv(-19)^5\equiv1\pmod {100}.$$

Thus the last two digits are $\boxed{01}$. (Alternatively, $3^{20}=3486784401$.)

## 5. Euler's Theorem Is a Tool, Not a License to Cancel Anything

When $\gcd(a,n)\ne1$, Euler's theorem cannot be applied to the whole modulus.
Often, however, it can still be used on the part of the modulus that is coprime
to $a$.

### Split the Modulus, Then Use CRT

Factor $n$ into relatively prime parts

$$n=uv,\qquad\gcd(u,v)=1,$$

where every prime factor of $u$ also divides $a$, while $\gcd(a,v)=1$. For a
large enough exponent $b$, the shared-factor part satisfies

$$a^b\equiv0\pmod u.$$

On the coprime part, Euler's theorem does apply:

$$a^b\equiv a^{b\bmod\varphi(v)}\pmod v.$$

Finally, solve these two congruences with CRT. This method does **not** require
listing powers until a cycle appears.

### Example: Find $6^{100}\pmod {15}$

We cannot apply Euler's theorem directly because $\gcd(6,15)=3$. Split

$$15=3\cdot5.$$

The factor $3$ shares a prime factor with $6$, while $5$ is coprime to $6$.
Therefore

$$6^{100}\equiv0\pmod3.$$

Modulo $5$, Euler's theorem applies. Since $\varphi(5)=4$ and $100\equiv0\pmod4$,

$$6^{100}\equiv1^{100}\equiv1\pmod5.$$

We now solve

$$x\equiv0\pmod3,\qquad x\equiv1\pmod5.$$

Of the numbers congruent to $1$ modulo $5$, $6$ is divisible by $3$, so CRT gives

$$\boxed{6^{100}\equiv6\pmod {15}.}$$

## 6. Fermat's Little Theorem

If $p$ is prime, then $\varphi(p)=p-1$. Euler's theorem immediately gives the
important special case:

> If $p$ is prime and $p\nmid a$, then
> $$\boxed{a^{p-1}\equiv1\pmod p.}$$

For example, since $13$ is prime and $13\nmid2$,

$$2^{12}\equiv1\pmod {13}.$$

This is Fermat's little theorem. It is Euler's theorem with a prime modulus.

## 7. Exponent Towers

For a tower such as

$$a^{b^c}\pmod n,$$

first check whether $\gcd(a,n)=1$. If it is, Euler's theorem says that only
the exponent modulo $\varphi(n)$ is needed:

$$a^{b^c}\equiv a^r\pmod n,$$

where

$$r\equiv b^c\pmod {\varphi(n)}.$$

The new task, finding $b^c\pmod{\varphi(n)}$, is another modular-exponent
problem. If $\gcd(b,\varphi(n))=1$, Euler's theorem may be applied again. If
not, split $\varphi(n)$ into its shared-factor and coprime parts, then use the
factor-power and CRT method from Section 5.

### Example: Find $3^{7^{100}}\pmod {100}$

Since $\gcd(3,100)=1$ and $\varphi(100)=40$, we need

$$7^{100}\pmod {40}.$$

Now $\gcd(7,40)=1$ and $\varphi(40)=16$. Since $100\equiv4\pmod {16}$,

$$7^{100}\equiv7^4=2401\equiv1\pmod {40}.$$

Thus $7^{100}\equiv1\pmod {40}$, and hence

$$\boxed{3^{7^{100}}\equiv3^1\equiv3\pmod {100}.}$$

## 8. Class Practice

### Problem 1

Verify Euler's theorem for $a=3$ and $n=10$.

<details>
<summary>Solution</summary>

Since $\gcd(3,10)=1$ and $\varphi(10)=4$,

$$3^4=81\equiv\boxed{1}\pmod {10}.$$

</details>

### Problem 2

Find $11^{73}\pmod {28}$.

<details>
<summary>Solution</summary>

We have $\gcd(11,28)=1$ and

$$\varphi(28)=28\left(1-\frac12\right)\left(1-\frac17\right)=12.$$

Since $73=6\cdot12+1$,

$$11^{73}\equiv11^1\equiv\boxed{11}\pmod {28}.$$

</details>

### Problem 3

Can Euler's theorem be applied directly to simplify $12^{100}\pmod {35}$?

<details>
<summary>Solution</summary>

Yes. Since $\gcd(12,35)=1$, the condition holds. Also,

$$\varphi(35)=35\left(1-\frac15\right)\left(1-\frac17\right)=24,$$

so $12^{24}\equiv1\pmod {35}$.

</details>

### Problem 4

Can Euler's theorem be applied directly to simplify $14^{100}\pmod {35}$?

<details>
<summary>Solution</summary>

No. Since $\gcd(14,35)=7\ne1$, the theorem's hypothesis fails. In fact,
$14^{\varphi(35)}$ is not congruent to $1$ modulo $35$.

</details>

### Problem 5

Find $18^{100}\pmod {100}$ using a modulus split and CRT, not a cycle of powers.

<details>
<summary>Solution</summary>

Split $100=4\cdot25$. Since $4\mid18^{100}$,

$$18^{100}\equiv0\pmod4.$$

Also $\gcd(18,25)=1$ and $\varphi(25)=20$. Hence

$$18^{100}\equiv18^0\equiv1\pmod {25}.$$

Solve $x\equiv0\pmod4$ and $x\equiv1\pmod {25}$. Write $x=1+25k$.
Then $1+25k\equiv1+k\equiv0\pmod4$, so $k\equiv3\pmod4$. Taking $k=3$ gives

$$\boxed{18^{100}\equiv76\pmod {100}.}$$

</details>

### Problem 6

Find $6^{50}\pmod {35}$ using a modulus split and CRT, not a cycle of powers.

<details>
<summary>Solution</summary>

Split $35=5\cdot7$. Because $5\mid6^{50}$,

$$6^{50}\equiv0\pmod5.$$

Since $\gcd(6,7)=1$ and $\varphi(7)=6$,

$$6^{50}\equiv6^2=36\equiv1\pmod7.$$

Solve $x\equiv0\pmod5$ and $x\equiv1\pmod7$. Writing $x=1+7k$, we need
$1+2k\equiv0\pmod5$, so $k\equiv2\pmod5$. Thus

$$\boxed{6^{50}\equiv15\pmod {35}.}$$

</details>

### Problem 7

Find $18^{7^{100}}\pmod {100}$ using Euler's theorem, a modulus split, and CRT.
Do not enumerate a power cycle.

<details>
<summary>Solution</summary>

Since $\gcd(18,100)\ne1$, split $100=4\cdot25$. The exponent $7^{100}$ is at
least $2$, so

$$18^{7^{100}}\equiv0\pmod4.$$

Modulo $25$, $18$ is coprime to the modulus. Since $\varphi(25)=20$, find
$7^{100}\pmod {20}$. Because $\gcd(7,20)=1$ and $\varphi(20)=8$,

$$7^{100}\equiv7^4=2401\equiv1\pmod {20}.$$

Therefore

$$18^{7^{100}}\equiv18^1\equiv18\pmod {25}.$$

Solve $x\equiv0\pmod4$ and $x\equiv18\pmod {25}$. Write $x=18+25k$.
Then $2+k\equiv0\pmod4$, so $k\equiv2\pmod4$. Thus

$$\boxed{18^{7^{100}}\equiv68\pmod {100}.}$$

</details>

## 9. Exit Ticket

1. State Euler's theorem, including its condition.
2. Find $\varphi(45)$.
3. Find $2^{100}\pmod {15}$.
4. Explain in one sentence why Euler's theorem cannot be applied directly to
   $10^{50}\pmod {30}$.

<details>
<summary>Answers</summary>

1. If $\gcd(a,n)=1$, then $a^{\varphi(n)}\equiv1\pmod n$.
2. $\varphi(45)=45(1-1/3)(1-1/5)=\boxed{24}$.
3. $\varphi(15)=8$ and $100\equiv4\pmod8$, so
   $2^{100}\equiv2^4=16\equiv\boxed{1}\pmod {15}$.
4. $\gcd(10,30)=10\ne1$.

</details>

## 10. Summary

Euler's theorem states

$$\boxed{\gcd(a,n)=1\quad\Longrightarrow\quad a^{\varphi(n)}\equiv1\pmod n.}$$

To use it:

1. Check that $a$ and $n$ are relatively prime.
2. Find $\varphi(n)$ from the prime factorization of $n$.
3. Reduce the exponent modulo $\varphi(n)$, then finish the smaller power.

The condition comes first. If $\gcd(a,n)\ne1$, Euler's theorem does not apply
directly. When possible, split $n$ into its shared-factor prime-power part and
its coprime part, use Euler's theorem only on the latter, and combine the two
remainders with CRT.

For $a^{b^c}\pmod n$, first reduce $b^c$ modulo $\varphi(n)$ when $a$ is
coprime to $n$. That exponent-reduction problem may require Euler's theorem
again, or a modulus split and CRT if its own base is not coprime to its modulus.

## Further Reading: The LCM Strengthening of Euler's Theorem

Euler's theorem always gives the exponent $\varphi(n)$, but that exponent can
often be made smaller. Suppose the prime factorization of $n$ is

$$n=\prod_{i=1}^k p_i^{a_i}.$$

Define

$$C(n)=\operatorname{lcm}\left(p_1^{a_1-1}(p_1-1),
p_2^{a_2-1}(p_2-1),\ldots,p_k^{a_k-1}(p_k-1)\right).$$

Equivalently,

$$C(n)=\operatorname{lcm}\left(\varphi(p_1^{a_1}),
\varphi(p_2^{a_2}),\ldots,\varphi(p_k^{a_k})\right).$$

We will call the following result the **LCM strengthening of Euler's theorem**:

> If $\gcd(a,n)=1$, then
> $$\boxed{a^{C(n)}\equiv1\pmod n.}$$

There is no widely used separate name for this exact choice of $C(n)$. It is a
useful universal exponent for the units modulo $n$ and is often smaller than
$\varphi(n)$.

### Proof

Fix a prime-power factor $p_i^{a_i}$ of $n$. Since $\gcd(a,n)=1$, we also have

$$\gcd(a,p_i^{a_i})=1.$$

Euler's theorem modulo $p_i^{a_i}$ gives

$$a^{\varphi(p_i^{a_i})}=a^{p_i^{a_i-1}(p_i-1)}\equiv1\pmod {p_i^{a_i}}.$$

By definition, $C(n)$ is a multiple of $\varphi(p_i^{a_i})$. Thus

$$a^{C(n)}\equiv1\pmod {p_i^{a_i}}$$

for every $i$. The prime powers $p_1^{a_1},\ldots,p_k^{a_k}$ are pairwise
relatively prime. Therefore CRT says that the simultaneous congruences

$$a^{C(n)}\equiv1\pmod {p_i^{a_i}}\qquad(i=1,\ldots,k)$$

are equivalent to

$$\boxed{a^{C(n)}\equiv1\pmod n.}\qquad\square$$

### Example: A Smaller Exponent Modulo $45$

Since $45=3^2\cdot5$,

$$C(45)=\operatorname{lcm}(\varphi(9),\varphi(5))
=\operatorname{lcm}(6,4)=12.$$

Thus every $a$ with $\gcd(a,45)=1$ satisfies

$$a^{12}\equiv1\pmod {45}.$$

Euler's theorem would use $\varphi(45)=24$, so this LCM strengthening cuts the
universal exponent in half.

### The Standard Sharp Version: Carmichael's Theorem

The standard named refinement is **Carmichael's theorem**. The Carmichael
function $\lambda(n)$ is the *smallest* positive universal exponent: if
$\gcd(a,n)=1$, then

$$\boxed{a^{\lambda(n)}\equiv1\pmod n.}$$

For odd prime powers, it agrees with Euler's totient:

$$\lambda(p^r)=p^{r-1}(p-1)\qquad(p\text{ odd}).$$

The exception is a power of $2$:

$$\lambda(2)=1,\qquad\lambda(4)=2,\qquad
\lambda(2^r)=2^{r-2}\quad(r\ge3).$$

For relatively prime prime-power factors, take the LCM:

$$\lambda(n)=\operatorname{lcm}\left(\lambda(p_1^{a_1}),\ldots,
\lambda(p_k^{a_k})\right).$$

Thus $C(n)$ above is always valid, but $\lambda(n)$ can be smaller when the
factorization contains a sufficiently high power of $2$. For example,

$$C(8)=\varphi(8)=4,\qquad\lambda(8)=2,$$

and indeed every odd $a$ satisfies $a^2\equiv1\pmod8$.
