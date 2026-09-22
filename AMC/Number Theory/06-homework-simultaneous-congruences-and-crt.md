# Homework: Simultaneous Congruences and CRT
*AMC / Number Theory*

This homework accompanies [Lesson 6](./06-simultaneous-congruences-and-crt.md).
For relatively prime moduli, give the final answer as one residue class modulo the
product of the moduli. Show an organized trial, a substitution, or a Bézout/CRT
construction as requested.

## Part A: Two Simultaneous Congruences

### Problem 1

Use organized trial to solve

$$x\equiv3\pmod7,\qquad x\equiv5\pmod8.$$

<details>
<summary>Solution</summary>

Write $x=3+7k$. Testing values of $k$ modulo $8$ gives $k=6$ as the first choice
that makes $x\equiv5\pmod8$:

$$x=3+7(6)=45.$$

Thus

$$\boxed{x\equiv45\pmod {56}.}$$

</details>

### Problem 2

Use Bézout's identity to solve

$$x\equiv2\pmod5,\qquad x\equiv4\pmod7.$$

<details>
<summary>Solution</summary>

For $m=7$ and $n=5$, one Bézout equation is

$$7(3)+5(-4)=1.$$

Using $a=2$, $b=4$, and $s=3$ gives

$$x_0=(a-b)ms+b=(2-4)\cdot7\cdot3+4=-38\equiv32\pmod {35}.$$

Therefore

$$\boxed{x\equiv32\pmod {35}.}$$

</details>

### Problem 3

Solve by substitution:

$$x\equiv4\pmod9,\qquad x\equiv1\pmod {10}.$$

<details>
<summary>Solution</summary>

Let $x=4+9k$. The second condition gives

$$4+9k\equiv1\pmod {10},$$

so $-k\equiv-3\pmod {10}$ and $k\equiv3\pmod {10}$. Thus

$$x=4+9(3)=31,$$

and

$$\boxed{x\equiv31\pmod {90}.}$$

</details>

### Problem 4

Solve

$$x\equiv5\pmod {12},\qquad x\equiv8\pmod {25}.$$

<details>
<summary>Solution</summary>

Write $x=5+12k$. Then $12k\equiv3\pmod {25}$. Since
$12^{-1}\equiv23\pmod {25}$,

$$k\equiv23\cdot3=69\equiv19\pmod {25}.$$

So $x=5+12(19)=233$, and

$$\boxed{x\equiv233\pmod {300}.}$$

</details>

## Part B: Three Congruences

### Problem 5

Solve

$$x\equiv1\pmod3,\qquad x\equiv2\pmod4,\qquad x\equiv3\pmod5.$$

<details>
<summary>Solution</summary>

The first two conditions give $x\equiv10\pmod {12}$. Write $x=10+12k$. Modulo $5$,

$$10+12k\equiv3\pmod5,$$

so $2k\equiv3\pmod5$, giving $k\equiv4\pmod5$. Hence $x=10+12(4)=58$:

$$\boxed{x\equiv58\pmod {60}.}$$

</details>

### Problem 6

Solve

$$x\equiv2\pmod5,\qquad x\equiv3\pmod7,\qquad x\equiv4\pmod9.$$

<details>
<summary>Solution</summary>

The first two conditions give $x\equiv17\pmod {35}$. Write $x=17+35k$. Modulo $9$,

$$17+35k\equiv4\pmod9,$$

so $8k\equiv5\pmod9$. Since $8^{-1}\equiv8\pmod9$, $k\equiv4\pmod9$. Thus

$$x=17+35(4)=157,$$

and

$$\boxed{x\equiv157\pmod {315}.}$$

</details>

## Part C: When Moduli Share Factors

### Problem 7

Solve

$$x\equiv3\pmod6,\qquad x\equiv5\pmod8.$$

<details>
<summary>Solution</summary>

The moduli have GCD $2$, and $3\equiv5\pmod2$, so a solution can exist. Write
$x=3+6k$. Then

$$3+6k\equiv5\pmod8,$$

which gives $3k\equiv1\pmod4$, hence $k\equiv3\pmod4$. Therefore

$$\boxed{x\equiv21\pmod {24}.}$$

</details>

### Problem 8

Explain why the system below has no solution:

$$x\equiv1\pmod6,\qquad x\equiv5\pmod9.$$

<details>
<summary>Solution</summary>

The GCD of $6$ and $9$ is $3$. A solution would require the two remainders to agree
modulo $3$, but

$$1\not\equiv5\pmod3.$$

Therefore

$$\boxed{\text{there is no solution}.}$$

</details>

### Problem 9

Solve

$$x\equiv7\pmod {12},\qquad x\equiv13\pmod {18}.$$

<details>
<summary>Solution</summary>

The remainders agree modulo $\gcd(12,18)=6$, since both are $1\pmod6$. Let
$x=7+12k$. Then

$$7+12k\equiv13\pmod {18}.$$

After dividing $12k\equiv6\pmod {18}$ by $6$, we get $2k\equiv1\pmod3$, so
$k\equiv2\pmod3$. Thus $x=7+12(2)=31$, and the combined modulus is
$\operatorname{lcm}(12,18)=36$:

$$\boxed{x\equiv31\pmod {36}.}$$

</details>

## Part D: Applications and Reasoning

### Problem 10

A machine is inspected every $9$ minutes starting $2$ minutes after noon and every
$14$ minutes starting $5$ minutes after noon. How many minutes after noon is its
first inspection by both schedules?

<details>
<summary>Solution</summary>

We need

$$x\equiv2\pmod9,\qquad x\equiv5\pmod {14}.$$

Let $x=2+9k$. Then $9k\equiv3\pmod {14}$. Since $9^{-1}\equiv11\pmod {14}$,

$$k\equiv11\cdot3=33\equiv5\pmod {14}.$$

Thus $x=2+9(5)=\boxed{47}$ minutes after noon.

</details>

### Problem 11

Find the smallest positive integer that leaves remainder $4$ when divided by $11$ and
remainder $6$ when divided by $13$.

<details>
<summary>Solution</summary>

Write $x=4+11k$. Then $11k\equiv2\pmod {13}$. Since $11\equiv-2\pmod {13}$,
we get $k\equiv12\pmod {13}$. Therefore

$$x=4+11(12)=\boxed{136}. $$

Indeed, $136\equiv4\pmod {11}$ and $136\equiv6\pmod {13}$.

</details>

### Problem 12

Find the smallest positive integer satisfying

$$x\equiv0\pmod8,\qquad x\equiv1\pmod3,\qquad x\equiv4\pmod5.$$

<details>
<summary>Solution</summary>

The first two conditions give $x\equiv16\pmod {24}$. Write $x=16+24k$. Modulo $5$,

$$16+24k\equiv4\pmod5,$$

so $4k\equiv3\pmod5$. Since $4^{-1}\equiv4\pmod5$, $k\equiv2\pmod5$. Thus

$$x=16+24(2)=\boxed{64}. $$

</details>

## Part E: Challenge

### Problem 13

Suppose $x$ and $y$ both satisfy

$$x\equiv y\pmod m\qquad\text{and}\qquad x\equiv y\pmod n,$$

where $\gcd(m,n)=1$. Prove that $x\equiv y\pmod {mn}$.

<details>
<summary>Solution</summary>

The two congruences say that $m\mid(x-y)$ and $n\mid(x-y)$. Since $m$ and $n$ are
relatively prime, their product divides every common multiple of them; in particular,

$$mn\mid(x-y).$$

Therefore

$$\boxed{x\equiv y\pmod {mn}.}$$

This proves the uniqueness part of the two-modulus Chinese Remainder Theorem.

</details>

### Problem 14

The system

$$x\equiv a\pmod m,\qquad x\equiv b\pmod n$$

has relatively prime moduli. Explain why adding $mn$ to a solution gives another
solution, and use Problem 13 to explain why there is only one solution class modulo
$mn$.

<details>
<summary>Solution</summary>

Because both $m$ and $n$ divide $mn$, adding $mn$ does not change a number's
remainder modulo either modulus. Thus every value congruent to one solution modulo
$mn$ is also a solution.

If two values are solutions, they have the same remainder modulo $m$ and the same
remainder modulo $n$. Problem 13 then gives that they are congruent modulo $mn$.
So all solutions form exactly one class:

$$\boxed{x\equiv x_0\pmod {mn}.}$$

</details>
