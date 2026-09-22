# Lesson 6: Simultaneous Congruences & the Chinese Remainder Theorem
*AMC / Number Theory*

Suppose a number leaves remainder $a$ when divided by $n$ and remainder $b$ when
divided by $m$. At first, we can find it just by trying possibilities. Then we will
use the Bézout identity from Lesson 5 to build a solution directly. The goal is not
to memorize a new formula: it is to reuse an equation we already know how to make.

In this lesson, start with the simplest case: the moduli $m$ and $n$ are relatively
prime, so $\gcd(m,n)=1$.

## Learning Goals

By the end of this lesson, you will be able to:

- solve a small pair of simultaneous congruences by organized trial;
- use Bézout's identity to construct a solution to two congruences with relatively
  prime moduli;
- describe every solution modulo $mn$; and
- combine several pairwise relatively prime congruences two at a time.

## 1. The Simple Start: Try the Possibilities

Solve

$$x\equiv2\pmod3,\qquad x\equiv3\pmod5.$$

The first condition says that $x$ is one of

$$2,5,8,11,14,17,20,23,\ldots$$

Try these one at a time modulo $5$. The number $8$ leaves remainder $3$ upon
division by $5$, so it works:

$$\boxed{x\equiv8\pmod {15}.}$$

This method is perfectly reasonable when the numbers are small. More systematically,
write $x=a+nk$ and try $k=0,1,2,\ldots$ until the second condition is met.

Why is the answer modulo $15=3\cdot5$? Adding $15$ changes neither remainder, so
every number $8+15q$ works. Later we will show that there cannot be a second,
different answer modulo $15$.

## 2. Build the Same Answer from Bézout's Identity

Now solve the general pair

$$x\equiv a\pmod n,\qquad x\equiv b\pmod m,$$

where $\gcd(m,n)=1$.

Because $m$ and $n$ are relatively prime, Bézout's identity gives integers $s$ and
$t$ such that

$$\boxed{ms+nt=1.}$$

Reduce the Bézout equation modulo $n$, and also consider $ms$ modulo $m$. Put the two
facts together as one system:

$$\begin{cases}
ms\equiv1\pmod n,\\
ms\equiv0\pmod m.
\end{cases}$$

Multiply both equations by $a-b$:

$$\begin{cases}
(a-b)ms\equiv a-b\pmod n,\\
(a-b)ms\equiv0\pmod m.
\end{cases}$$

Now add $b$ to both equations:

$$\begin{cases}
(a-b)ms+b\equiv(a-b)+b=a\pmod n,\\
(a-b)ms+b\equiv0+b=b\pmod m.
\end{cases}$$

The same expression on the left has exactly the two remainders we wanted. Therefore,
if we call it $x_0$,

$$\boxed{x_0=(a-b)ms+b}$$

is a solution. Nothing new was assumed beyond Bézout's identity and the usual rules
for congruences.

### Example: Revisit $x\equiv2\pmod3$, $x\equiv3\pmod5$

Use Bézout's identity for $m=5$ and $n=3$:

$$5(-1)+3(2)=1.$$

Thus $s=-1$. The construction gives

$$x_0=(a-b)ms+b=(2-3)\cdot5\cdot(-1)+3=8.$$

As before, $8\equiv2\pmod3$ and $8\equiv3\pmod5$.

## 3. Why the Modulus Is $mn$

Adding $mn$ to a solution does not change its remainder modulo either $m$ or $n$.
Therefore

$$x\equiv x_0\pmod {mn}$$

always gives solutions.

These are all the solutions. If $x$ and $y$ both satisfy the two congruences, then

$$x-y\equiv0\pmod n\qquad\text{and}\qquad x-y\equiv0\pmod m.$$

So both $n$ and $m$ divide $x-y$. Since they are relatively prime, their product
$mn$ divides $x-y$. Hence $x\equiv y\pmod {mn}$.

We have proved the two-modulus version of the Chinese Remainder Theorem:

> If $\gcd(m,n)=1$, then the system
>
> $$x\equiv a\pmod n,\qquad x\equiv b\pmod m$$
>
> has exactly one solution class modulo $mn$.

## 4. When the Moduli Are Not Relatively Prime

What changes if $m$ and $n$ have a common factor? Let

$$d=\gcd(m,n).$$

Any solution to

$$x\equiv a\pmod n,\qquad x\equiv b\pmod m$$

must also satisfy both equations modulo $d$. Therefore, the two requested remainders
must agree modulo $d$:

$$\boxed{a\equiv b\pmod d.}$$

This is the only obstruction: the system has a solution exactly when
$a\equiv b\pmod{\gcd(m,n)}$. For example,

$$x\equiv1\pmod4,\qquad x\equiv2\pmod6$$

has no solution, because $\gcd(4,6)=2$, but $1\not\equiv2\pmod2$. We will not
develop the non-coprime construction further in this lesson.

## 5. Three or More Equations: Combine Two, Then Repeat

For several equations whose moduli are pairwise relatively prime, you do not need a
separate formula. Combine the first two into one congruence, then combine that result
with the next equation.

For example, solve

$$x\equiv1\pmod2,\qquad x\equiv2\pmod3,\qquad x\equiv3\pmod5.$$

First combine the first two. A quick trial gives

$$x\equiv5\pmod6,$$

because $5$ is odd and $5\equiv2\pmod3$.

Now combine this with the last condition:

$$x\equiv5\pmod6,\qquad x\equiv3\pmod5.$$

Since $\gcd(6,5)=1$, Bézout gives

$$5(-1)+6(1)=1.$$

Here the first congruence has $a=5$, $n=6$, and the second has $b=3$, $m=5$.
Using $s=-1$,

$$x_0=(5-3)\cdot5\cdot(-1)+3=-7\equiv23\pmod {30}.$$

Therefore

$$\boxed{x\equiv23\pmod {30}.}$$

The new modulus is $6\cdot5=30$. This repeated two-at-a-time process works because
the product of moduli already combined is relatively prime to each remaining modulus.

### Chinese Remainder Theorem

If $n_1,n_2,\ldots,n_k$ are pairwise relatively prime, then the system

$$x\equiv a_i\pmod {n_i}\qquad(i=1,2,\ldots,k)$$

has a solution that is unique modulo

$$\boxed{n_1n_2\cdots n_k.}$$

In other words, after combining the equations two at a time, every solution is in one
residue class modulo the product of all the moduli.

## 6. Class Practice

### Problem 1

Use organized trial to solve

$$x\equiv1\pmod4,\qquad x\equiv2\pmod9.$$

<details>
<summary>Solution</summary>

Numbers congruent to $1\pmod4$ are $1,5,9,13,17,21,25,29,\ldots$. The first that is
$2\pmod9$ is $29$. Thus

$$\boxed{x\equiv29\pmod {36}.}$$

</details>

### Problem 2

Use Bézout's identity to solve

$$x\equiv4\pmod7,\qquad x\equiv3\pmod {11}.$$

<details>
<summary>Solution</summary>

One Bézout equation is

$$11(2)+7(-3)=1.$$

Take $m=11$, $n=7$, and $s=2$. Then

$$x_0=(4-3)\cdot11\cdot2+3=25.$$

Therefore

$$\boxed{x\equiv25\pmod {77}.}$$

</details>

### Problem 3

Combine two equations first, then solve the third:

$$x\equiv2\pmod3,\qquad x\equiv1\pmod4,\qquad x\equiv4\pmod5.$$

<details>
<summary>Solution</summary>

The first two conditions give $x\equiv5\pmod {12}$. Now combine

$$x\equiv5\pmod {12},\qquad x\equiv4\pmod5.$$

Since $5(5)+12(-2)=1$, take $m=5$, $n=12$, and $s=5$. Then

$$x_0=(5-4)\cdot5\cdot5+4=29.$$

Thus

$$\boxed{x\equiv29\pmod {60}.}$$

</details>

## 7. Exit Ticket

1. If $ms+nt=1$, what are the remainders of $ms$ modulo $n$ and modulo $m$?
2. For $x\equiv a\pmod n$ and $x\equiv b\pmod m$ with $\gcd(m,n)=1$, what
   expression produces a solution?
3. When $m$ and $n$ are not relatively prime, what condition must $a$ and $b$ meet
   for the system to have a solution?

<details>
<summary>Answers</summary>

1. $ms\equiv1\pmod n$ and $ms\equiv0\pmod m$.
2. Find $s,t$ with $ms+nt=1$, then use $x_0=(a-b)ms+b$.
3. $a\equiv b\pmod{\gcd(m,n)}$.

</details>

## 8. Summary

For a small system, enumerate the numbers $a,a+n,a+2n,\ldots$ until one also has
the desired remainder modulo $m$. For a direct method, find $ms+nt=1$ and use

$$\boxed{x_0=(a-b)ms+b.}$$

When $m$ and $n$ are relatively prime, every solution is

$$\boxed{x\equiv x_0\pmod {mn}.}$$

If they are not relatively prime, a solution exists exactly when the two remainders
agree modulo $\gcd(m,n)$. For pairwise relatively prime moduli $n_1,\ldots,n_k$, the
Chinese Remainder Theorem gives one solution class modulo $n_1\cdots n_k$; find it by
repeating the same two-equation method.
