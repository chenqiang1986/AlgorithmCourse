# Lesson 5: Bézout's Identity & Linear Congruences
*AMC / Number Theory*

The Euclidean algorithm does more than find a GCD. If we keep track of the
remainders, it produces an equation involving the original numbers. That equation
gives modular inverses and solves linear congruences.

## Learning Goals

By the end of this lesson, you will be able to:

- express a GCD as an integer combination using Bézout's identity;
- use the extended Euclidean algorithm to find a modular inverse;
- decide whether $ax\equiv b\pmod n$ has a solution; and
- find every solution of a linear congruence modulo its original modulus.

## 1. Bézout's Identity

For any integers $a$ and $b$, not both $0$, there are integers $s$ and $t$ such that

$$\boxed{as+bt=\gcd(a,b).}$$

This statement is called **Bézout's identity**. The integers $s$ and $t$ are called
**Bézout coefficients**. They need not be positive, and they are usually not unique.

The Euclidean algorithm finds the GCD; working backward through its equations finds
the coefficients.

### Example: Express $\gcd(56,15)$ as a Linear Combination

First use the Euclidean algorithm:

$$\underline{56}=\underline{15}\cdot3+\underline{11}$$

$$\underline{15}=\underline{11}\cdot1+\underline{4}$$

$$\underline{11}=\underline{4}\cdot2+\underline{3}$$

$$\underline{4}=\underline{3}\cdot1+1.$$

Thus $\gcd(56,15)=1$. Now substitute backward, starting with the last nonzero
remainder. In each division above, the dividend, divisor, and remainder are
underlined; the quotient is not. Carry these underlines into the substitution so the
number being expanded is easy to trace.

$$\begin{aligned}
1&=\underline{4}-\underline{3}.
\end{aligned}$$

Expand $\underline{3}$ using the equation above in which it is the remainder:

$$\underline{11}=\underline{4}\cdot2+\underline{3},$$

so $\underline{3}=\underline{11}-2\cdot\underline{4}$. Substitution gives

$$1=\underline{4}-(\underline{11}-2\cdot\underline{4}).$$

Now simplify by combining like terms. Treat each underlined number as though it were
a variable: for example, $\underline{4}+2\cdot\underline{4}=3\cdot\underline{4}$.
Thus

$$1=3\cdot\underline{4}-\underline{11}.$$

Next expand the smaller underlined number $\underline{4}$, using the equation above
in which $\underline{4}$ is the remainder:

$$\underline{15}=\underline{11}\cdot1+\underline{4},$$

so $\underline{4}=\underline{15}-\underline{11}$. After simplifying, expand
$\underline{11}$ using the first division equation, where
$\underline{11}$ is the remainder. The same substitute-then-simplify pattern gives

$$\begin{aligned}
1&=3(\underline{15}-\underline{11})-\underline{11}\\
 &=3\cdot\underline{15}-4\cdot\underline{11}\\
 &=3\cdot\underline{15}-4(\underline{56}-3\cdot\underline{15})\\
 &=13\cdot\underline{15}-4\cdot\underline{56}.
\end{aligned}$$

Therefore

$$\boxed{1=(-4)\cdot56+13\cdot15.}$$

This is Bézout's identity in action. A quick check confirms it:
$-4(56)+13(15)=-224+195=1$.

A rigorous proof of Bézout's identity follows this same idea, formalized with an
induction argument along the decreasing remainders of the Euclidean algorithm. The
base case is the final nonzero remainder, and each backward substitution expresses
the preceding remainder as an integer combination of the original two numbers. We
will skip those technical induction details here; the example shows the essential
mechanism.

## 2. Linear Diophantine Equation Theorem

Fix integers $a$, $b$, and $c$, with $a$ and $b$ not both $0$. Then the equation

$$ax+by=c$$

has an integer solution $(x,y)$ if and only if

$$\boxed{\gcd(a,b)\mid c.}$$

### Proof

Let $d=\gcd(a,b)$.

**($\Rightarrow$)** Suppose $ax+by=c$ has an integer solution $(x,y)$. Since $d\mid a$
and $d\mid b$, we have $d\mid ax$ and $d\mid by$. Therefore $d$ divides their sum:

$$d\mid(ax+by)=c.$$

Thus $d\mid c$.

**($\Leftarrow$)** Suppose $d\mid c$. Write $c=dk$ for some integer $k$. By Bézout's
identity, there are integers $s$ and $t$ such that

$$as+bt=d.$$

Multiply this equation by $k$:

$$a(ks)+b(kt)=dk=c.$$

Thus $x=ks$ and $y=kt$ are integers satisfying $ax+by=c$.

For instance, $56x+15y=1$ has a solution because $\gcd(56,15)=1$, and the work above
already found one: $x=-4$, $y=13$. In contrast, $12x+18y=5$ has no integer solution:
$\gcd(12,18)=6$, and $6\nmid5$.

Our main use of this theorem today is modular arithmetic.

## 3. Modular Inverses

An integer $u$ is a **multiplicative inverse of $a$ modulo $n$** if

$$au\equiv1\pmod n.$$

We write this inverse as $a^{-1}\pmod n$. An inverse exists precisely when

$$\boxed{\gcd(a,n)=1.}$$

Why? If $au\equiv1\pmod n$, then $au+nv=1$ for some integer $v$, so Bézout's identity
shows that $a$ and $n$ must be relatively prime. Conversely, when $\gcd(a,n)=1$,
Bézout gives $au+nv=1$; reducing modulo $n$ leaves $au\equiv1\pmod n$.

### Example: Find $15^{-1}\pmod {56}$

From the previous example,

$$1=(-4)\cdot56+13\cdot15.$$

Reduce both sides modulo $56$. The $-4\cdot56$ term becomes $0$, giving

$$13\cdot15\equiv1\pmod {56}.$$

So

$$\boxed{15^{-1}\equiv13\pmod {56}.}$$

Notice that $-43$ is also an inverse, since $-43\equiv13\pmod {56}$. We normally
report the least nonnegative representative, $13$.

### A Crucial Warning About “Dividing”

In a congruence, canceling $a$ is valid only when $a$ has an inverse modulo the modulus;
equivalently, only when $\gcd(a,n)=1$.

For example, $2x\equiv2\pmod6$ does **not** imply $x\equiv1\pmod6$. In fact,
$x\equiv1$ and $x\equiv4\pmod6$ both work. Since $\gcd(2,6)=2$, the number $2$ has no
inverse modulo $6$.

## 4. Solving $ax\equiv b\pmod n$

Let

$$d=\gcd(a,n).$$

Then the congruence

$$ax\equiv b\pmod n$$

has a solution **if and only if**

$$\boxed{d\mid b.}$$

This is the modular version of the linear-equation criterion. Indeed,

$$ax\equiv b\pmod n$$

means that $ax-nk=b$ for some integer $k$. The left side is an integer combination
of $a$ and $n$, so it must be divisible by $d$.

When $d\mid b$, divide the entire congruence and modulus by $d$:

$$\frac{a}{d}x\equiv\frac{b}{d}\pmod {\frac{n}{d}}.$$

Now $\gcd(a/d,n/d)=1$, so $a/d$ has an inverse modulo $n/d$. This reduced congruence
has one solution modulo $n/d$, which produces exactly $d$ solutions modulo $n$.

### Reliable Method

To solve $ax\equiv b\pmod n$, use one extended-Euclidean calculation from start to
finish:

1. Run the Euclidean algorithm on $a$ and $n$, then back-substitute to obtain
   Bézout's identity $as+nt=d$. The value $d=\gcd(a,n)$ is a byproduct of this
   process; it need not be calculated in advance.
2. Check whether $d\mid b$. If not, there is **no solution**.
3. When $d\mid b$, divide the congruence and Bézout's identity by $d$. They become
   $$\frac{a}{d}x\equiv\frac{b}{d}\pmod {n/d},\qquad
   \frac{a}{d}s+\frac{n}{d}t=1.$$
4. Read $s$ as an inverse:
   $$\left(\frac{a}{d}\right)^{-1}\equiv s\pmod {n/d}.$$
5. Multiply the rescaled congruence by this inverse. The answer is one class modulo
   $n/d$. If $n/d$ is smaller than the original modulus $n$, that class naturally
   gives multiple solutions modulo $n$.

### Example A: One Solution Class

Solve

$$7x\equiv5\pmod {26}.$$

**Step 1: Run the Euclidean algorithm and find Bézout's identity.**

$$\underline{26}=\underline{7}\cdot3+\underline{5},\qquad
\underline{7}=\underline{5}\cdot1+\underline{2},\qquad
\underline{5}=\underline{2}\cdot2+1.$$

Back-substitution yields

$$1=(-11)\cdot7+3\cdot26.$$

The final remainder is $d=1$.

**Step 2: Check existence.** Since $1\mid5$, a solution exists.

**Step 3: Rescale.** Dividing by $d=1$ changes nothing:

$$7x\equiv5\pmod {26},\qquad(-11)\cdot7+3\cdot26=1.$$

**Step 4: Identify the inverse.** The Bézout coefficient of $7$ gives

$$7^{-1}\equiv-11\equiv15\pmod {26}.$$

**Step 5: Apply the inverse.**

$$x\equiv15\cdot5=75\equiv\boxed{23}\pmod {26}.$$

Check: $7\cdot23=161\equiv5\pmod {26}$.

### Example B: Several Solution Classes

Solve

$$14x\equiv12\pmod {30}.$$

**Step 1: Run the Euclidean algorithm and find Bézout's identity.**

$$\underline{30}=\underline{14}\cdot2+\underline{2}.$$

Thus $d=2$, and rearranging the same equation gives

$$(-2)\cdot14+1\cdot30=2.$$

**Step 2: Check existence.** Since $2\mid12$, solutions exist.

**Step 3: Rescale the congruence and Bézout's identity.** Divide both by $2$:

$$7x\equiv6\pmod {15}.$$

The rescaled Bézout identity is

$$(-2)\cdot7+1\cdot15=1.$$

**Step 4: Identify the inverse.** The coefficient $-2$ is the inverse of $7$ modulo
$15$:

$$7^{-1}\equiv-2\equiv13\pmod {15}.$$

**Step 5: Apply the inverse.**

$$x\equiv13\cdot6=78\equiv3\pmod {15}.$$

The result is modulo $15$, while the original congruence was modulo $30$. Therefore
the class $x\equiv3\pmod {15}$ naturally gives two classes modulo $30$:

$$\boxed{x\equiv3\text{ or }18\pmod {30}.}$$

Both check: $14(3)=42\equiv12\pmod {30}$ and $14(18)=252\equiv12\pmod {30}$.

### Example C: No Solution

Does

$$12x\equiv5\pmod {18}$$

have a solution?

**Step 1: Run the Euclidean algorithm and find Bézout's identity.**

$$\underline{18}=\underline{12}\cdot1+\underline{6}.$$

So the final nonzero remainder is $d=6$, and

$$(-1)\cdot12+1\cdot18=6.$$

**Step 2: Check existence.** Since $6\nmid5$, the congruence has

$$\boxed{\text{no solution}.}$$

There is no rescaling or inverse to find, because the existence test has already
failed.

## 5. Class Practice

### Problem 1

Use the extended Euclidean algorithm to write $1$ as a linear combination of $31$ and
$12$. Hence find $12^{-1}\pmod {31}$.

<details>
<summary>Solution</summary>

$$\underline{31}=\underline{12}\cdot2+\underline{7},\qquad
\underline{12}=\underline{7}\cdot1+\underline{5},$$

$$\underline{7}=\underline{5}\cdot1+\underline{2},\qquad
\underline{5}=\underline{2}\cdot2+1.$$

Work backward:

$$\begin{aligned}
1&=\underline{5}-2\cdot\underline{2}\\
 &=\underline{5}-2(\underline{7}-\underline{5})\\
 &=3\cdot\underline{5}-2\cdot\underline{7}\\
 &=3(\underline{12}-\underline{7})-2\cdot\underline{7}\\
 &=3\cdot\underline{12}-5\cdot\underline{7}\\
 &=3\cdot\underline{12}-5(\underline{31}-2\cdot\underline{12})\\
 &=13\cdot\underline{12}-5\cdot\underline{31}.
\end{aligned}$$

Thus $12^{-1}\equiv\boxed{13}\pmod {31}$.

</details>

### Problem 2

Solve $9x\equiv4\pmod {23}$.

<details>
<summary>Solution</summary>

Since $\underline{23}=\underline{9}\cdot2+\underline{5}$,
$\underline{9}=\underline{5}\cdot1+\underline{4}$, and
$\underline{5}=\underline{4}\cdot1+1$, we get

$$\begin{aligned}
1&=\underline{5}-\underline{4}\\
 &=\underline{5}-(\underline{9}-\underline{5})\\
 &=2\cdot\underline{5}-\underline{9}\\
 &=2(\underline{23}-2\cdot\underline{9})-\underline{9}\\
 &=2\cdot\underline{23}-5\cdot\underline{9}.
\end{aligned}$$

So $9^{-1}\equiv-5\equiv18\pmod {23}$. Therefore

$$x\equiv18\cdot4=72\equiv\boxed{3}\pmod {23}.$$

</details>

### Problem 3

Solve $18x\equiv30\pmod {42}$, giving all solutions modulo $42$.

<details>
<summary>Solution</summary>

$\gcd(18,42)=6$, and $6\mid30$, so solutions exist. Divide by $6$:

$$3x\equiv5\pmod7.$$

Since $3^{-1}\equiv5\pmod7$,

$$x\equiv5\cdot5=25\equiv4\pmod7.$$

There are $6$ solutions modulo $42$:

$$\boxed{x\equiv4,11,18,25,32,39\pmod {42}.}$$

</details>

## 6. Exit Ticket

1. Why does $a^{-1}\pmod n$ exist exactly when $\gcd(a,n)=1$?
2. How many solutions modulo $n$ can $ax\equiv b\pmod n$ have when
   $d=\gcd(a,n)$ divides $b$?

<details>
<summary>Answers</summary>

1. Bézout gives $au+nv=1$ exactly when $a$ and $n$ are relatively prime; modulo $n$,
   this says $au\equiv1$.
2. Exactly $d$ solutions modulo $n$.
</details>

## 7. Summary

The ideas form a chain:

$$\text{Euclidean algorithm}
\;\longrightarrow\;
\text{Bézout coefficients}
\;\longrightarrow\;
\text{modular inverses}
\;\longrightarrow\;
\text{linear congruences}. $$

When stuck, begin with a GCD. It tells you whether an inverse or a linear-congruence
solution can exist, and the extended Euclidean algorithm supplies the inverse needed
to construct it.

## 8. Enhanced Reading: Why Prime Factorization Is Unique

Lesson 2 stated the Fundamental Theorem of Arithmetic: every positive integer greater
than $1$ can be written as a product of primes, and that product is unique except for
the order of its factors. Bézout's identity now gives us the missing tool to prove it.

### 8.1 Irreducible Integers Are Prime

Call a positive integer $p>1$ **irreducible** if its only positive factors are $1$
and $p$. We will prove that it has the prime-product property:

> **Theorem (Euclid's Lemma).** If $p$ is irreducible and $p\mid ab$, then
> $$\boxed{p\mid a\quad\text{or}\quad p\mid b.}$$

This is the step that turns an irreducible number into a prime number in the stronger
divisibility sense.

#### Proof

Suppose $p\mid ab$. If $p\mid a$, we are done. Otherwise, $p\nmid a$.

Any positive common divisor of $p$ and $a$ must divide $p$. Since $p$ is irreducible,
that common divisor can only be $1$ or $p$. The second possibility would imply
$p\mid a$, contrary to our assumption. Therefore

$$\gcd(p,a)=1.$$

By Bézout's identity, there are integers $s$ and $t$ such that

$$sp+ta=1.$$

Multiply by $b$:

$$spb+tab=b.$$

The first term is divisible by $p$, and the second is divisible by $p$ because
$p\mid ab$. Hence their sum, $b$, is divisible by $p$. Thus $p\mid b$.

In either case, $p\mid a$ or $p\mid b$. $\square$

Repeated use of this result shows that if a prime $p$ divides a product of any finite
number of integers, then it divides at least one factor of that product.

### 8.2 Fundamental Theorem of Arithmetic

> **Theorem.** Every integer $n>1$ has a factorization into primes. This
> factorization is unique up to rearranging the prime factors.

#### Existence: Strong Induction

We prove that every integer $n>1$ is a product of primes by strong induction on $n$.

- **Base case:** $2$ is prime, so it is already a product of primes.
- **Inductive step:** Assume every integer $m$ with $2\le m<n$ is a product of
  primes. If $n$ is prime, there is nothing to prove. If $n$ is composite, write
  $n=ab$ with $1<a<n$ and $1<b<n$. By the induction hypothesis, both $a$ and $b$
  are products of primes. Combining those two products gives a prime factorization
  of $n$.

Thus every $n>1$ has at least one prime factorization.

#### Uniqueness: Strong Induction

We now prove that no two genuinely different prime factorizations are possible.
Assume, by strong induction, that factorization is unique for every integer from $2$
through $n-1$. Suppose $n$ has two prime factorizations:

$$n=p_1p_2\cdots p_r=q_1q_2\cdots q_s.$$

Since $p_1$ divides the product on the right, repeated Euclid's Lemma shows that
$p_1\mid q_j$ for some $j$. But $q_j$ is irreducible, so its only positive divisors
greater than $1$ are itself. Since $p_1>1$, this forces

$$p_1=q_j.$$

Rearrange the factors on the right so that $q_j$ is first, then cancel the common
factor $p_1$:

$$\frac{n}{p_1}=p_2\cdots p_r=q_2\cdots q_s.$$

Because $n/p_1<n$, the induction hypothesis says the remaining two prime
factorizations are the same up to order. Restoring the common factor $p_1$ shows that
the original factorizations of $n$ are also the same up to order.

Therefore prime factorization is unique. $\square$

**Why this proof is valid.** Bézout's identity was obtained from the Euclidean
algorithm and backward substitution alone. That process never uses prime
factorization or assumes that factorization is unique. Therefore using Bézout's
identity to prove Euclid's Lemma, and then unique factorization, is not circular.
