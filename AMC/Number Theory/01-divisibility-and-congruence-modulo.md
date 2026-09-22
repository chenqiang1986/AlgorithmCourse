# Lesson 1: Divisibility and Congruence Modulo $n$
*AMC / Number Theory*

Number theory studies whole numbers. This opening lesson gives precise names to two
familiar ideas: one integer may divide another evenly, and two integers may leave the
same remainder when divided by a fixed positive integer.

## 1. Divisibility

For integers $a$ and $b$, with $a\ne0$, write

$$a\mid b$$

and say “$a$ divides $b$” when there is an integer $k$ such that

$$b=ak.$$

Here $a$ is a **divisor** (or factor) of $b$, and $b$ is a **multiple** of $a$.
The quotient must be an integer: divisibility means “divides evenly.”

- $7\mid56$ because $56=7\cdot8$.
- $-4\mid20$ because $20=(-4)(-5)$.
- $6\nmid25$ because no integer $k$ satisfies $25=6k$.

The notation is directional: $3\mid12$ is true, but $12\mid3$ is false.

### Basic Facts

Let $a,b,c$ be integers, with divisors nonzero.

1. $a\mid a$.
2. If $a\mid b$, then $a\mid bc$.
3. If $a\mid b$ and $a\mid c$, then $a\mid(b+c)$ and $a\mid(b-c)$.
4. If $a\mid b$ and $b\mid c$, then $a\mid c$.

For instance, if $6\mid42$ and $6\mid18$, then $42=6\cdot7$ and $18=6\cdot3$.
Therefore

$$42-18=6\cdot7-6\cdot3=6(7-3),$$

so $6\mid(42-18)$. When proving divisibility, translate “$a$ divides $b$” into
“$b$ equals $a$ times an integer.”

## 2. Division With Remainder

When $n>0$, every integer $a$ can be written in exactly one way as

$$a=nq+r,\qquad0\le r<n.$$

This is the **division algorithm**. The integer $q$ is the quotient and $r$ is the
remainder on division by $n$. For example,

$$29=6\cdot4+5,$$

so $29$ leaves remainder $5$ when divided by $6$. Although $29=6\cdot5-1$ is true,
$-1$ is not the standard remainder: it is not between $0$ and $5$.

Negative integers also have ordinary nonnegative remainders:

$$-17=5(-4)+3.$$

Thus $-17$ leaves remainder $3$ when divided by $5$.

## 3. Congruence Modulo $n$

Let $n>0$. We write

$$a\equiv b\pmod n$$

and say “$a$ is congruent to $b$ modulo $n$” when $a$ and $b$ leave the same
remainder after division by $n$. Equivalently,

$$a\equiv b\pmod n\quad\Longleftrightarrow\quad n\mid(a-b).$$

This difference test is usually the fastest way to check a congruence.

### Example

Is $38\equiv8\pmod{10}$?

$$38-8=30=10\cdot3.$$

Since $10\mid(38-8)$, the congruence is true. Likewise,

$$-13\equiv2\pmod5$$

because $-13-2=-15=5(-3)$. Modulo $5$, the values $-13$, $2$, $7$, and $-3$
all belong to the same class.

Every integer is congruent to exactly one of

$$0,1,2,\ldots,n-1\pmod n.$$

For example, modulo $4$ the four classes are:

| Remainder | Integers in the class |
| --- | --- |
| $0$ | $\ldots,-8,-4,0,4,8,\ldots$ |
| $1$ | $\ldots,-7,-3,1,5,9,\ldots$ |
| $2$ | $\ldots,-6,-2,2,6,10,\ldots$ |
| $3$ | $\ldots,-5,-1,3,7,11,\ldots$ |

Congruence is not equality. $17\ne2$, but $17\equiv2\pmod5$: they are different
integers with the same remainder modulo $5$.

## 4. Calculating With Congruences

If $a\equiv b\pmod n$ and $c\equiv d\pmod n$, then

$$a+c\equiv b+d\pmod n,$$

$$a-c\equiv b-d\pmod n,$$

and

$$ac\equiv bd\pmod n.$$

So a number may be replaced with any congruent number while adding, subtracting, or
multiplying. Reducing to small remainders makes large calculations manageable.

### Example: A Large Product

Find the remainder when $47\cdot83$ is divided by $10$.

$$47\cdot83\equiv7\cdot3=21\equiv1\pmod{10}.$$

The remainder is **$1$**. There was no need to multiply the original numbers first.

### Example: A Power

Find the remainder when $3^{10}$ is divided by $7$.

$$3^2=9\equiv2\pmod7,$$

so

$$3^{10}=(3^2)^5\equiv2^5=32\equiv4\pmod7.$$

The remainder is **$4$**.

## 5. What You May *Not* Do: Divide Automatically

Multiplication is always safe, but division is not automatically safe. For example,

$$2\cdot1\equiv2\cdot4\pmod6$$

is true, because $2\equiv8\pmod6$. But $1\not\equiv4\pmod6$. Dividing both sides by
$2$ while keeping the modulus $6$ would turn a true statement into a false one.

Here is the division rule we may use. If

$$a\equiv b\pmod n,$$

and a nonzero integer $d$ divides $a$, $b$, and $n$, then

$$\frac{a}{d}\equiv\frac{b}{d}\pmod{n/d}.$$

All three divisions must be exact. In general, this does **not** mean

$$\frac{a}{d}\equiv\frac{b}{d}\pmod n\qquad\text{❌}$$

The modulus must also be divided by $d$. For example, since $18\equiv6\pmod{12}$ and
$6$ divides $18$, $6$, and $12$, we get

$$\frac{18}{6}\equiv\frac{6}{6}\pmod{12/6},$$

or $3\equiv1\pmod2$, which is true.

> Add, subtract, and multiply congruences freely. Divide only when the divisor divides
> both numbers and the modulus; then divide the modulus as well.

## 6. Divisibility Tests as Congruences

The familiar divisibility tests are modular arithmetic in disguise.

- An integer is divisible by $2$ exactly when it is congruent to $0\pmod2$.
- It is divisible by $5$ exactly when its last digit is $0$ or $5$, since
  $10\equiv0\pmod5$.
- It is divisible by $3$ exactly when its digit sum is divisible by $3$, since
  $10\equiv1\pmod3$.

To see the last fact, write a three-digit number as $100a+10b+c$. Then

$$100a+10b+c\equiv a+b+c\pmod3.$$

The number and its digit sum therefore have the same remainder modulo $3$.

## 7. Class Practice

### Problem 1

Determine whether each statement is true or false:

1. $9\mid117$
2. $8\mid52$
3. $-6\mid42$

<details>
<summary>Solution</summary>

1. True: $117=9\cdot13$.
2. False: $52/8=6.5$, not an integer.
3. True: $42=(-6)(-7)$.

</details>

### Problem 2

Find the standard remainder when $-46$ is divided by $7$.

<details>
<summary>Solution</summary>

We need $-46=7q+r$ with $0\le r<7$. Since $-46=7(-7)+3$, the remainder is **$3$**.
Equivalently, $-46\equiv3\pmod7$.

</details>

### Problem 3

Find the remainder when $1234+5678$ is divided by $9$.

<details>
<summary>Solution</summary>

Use digit sums:

$$1234\equiv1+2+3+4=10\equiv1\pmod9,$$

$$5678\equiv5+6+7+8=26\equiv8\pmod9.$$

Thus $1234+5678\equiv1+8=9\equiv0\pmod9$. The remainder is **$0$**.

</details>

### Problem 4

What is the units digit of $7^{23}$?

<details>
<summary>Solution</summary>

The units digit is the remainder modulo $10$. The powers of $7$ cycle:

$$7^1\equiv7,\quad7^2\equiv9,\quad7^3\equiv3,\quad7^4\equiv1\pmod{10}.$$

The cycle has length $4$, and $23\equiv3\pmod4$. Therefore

$$7^{23}\equiv7^3\equiv3\pmod{10}.$$

The units digit is **$3$**.

</details>

## 8. Common Mistakes

### 8.1 Reversing the divisibility symbol

$a\mid b$ means $b$ is a multiple of $a$, not the other way around. Read it as
“$a$ divides $b$,” then check whether $b/a$ is an integer.

### 8.2 Treating congruence as equality

$a\equiv b\pmod n$ does not say $a=b$; it says $n$ divides their difference. Always
keep the modulus attached to a congruence statement.

### 8.3 Using an invalid remainder

For division by $n$, standard remainders are $0,1,\ldots,n-1$. A negative number such
as $-1$ may be congruent to a valid remainder, but it is not itself the standard remainder.

### 8.4 Cancelling without checking

From $ca\equiv cb\pmod n$, one cannot generally conclude $a\equiv b\pmod n$. If $c$
divides both sides and $n$, the safe division rule gives $a\equiv b\pmod{n/c}$ instead.

## 9. Key Takeaways

- $a\mid b$ means $b=ak$ for some integer $k$.
- Every integer has one standard remainder $r$ modulo $n$, where $0\le r<n$.
- $a\equiv b\pmod n$ exactly when $n\mid(a-b)$, or when $a$ and $b$ have the same
  remainder on division by $n$.
- Congruences can be added, subtracted, and multiplied.
- Division is allowed when the divisor divides both numbers and the modulus; the new
  modulus is the original modulus divided by that divisor.

The next lesson will use this language to study prime numbers and factorization.
