# Lesson 12: Quadratic Equations — Square Roots and Completing the Square
*Fundamental Math / Algebra I*

This begins the quadratic-functions-and-equations unit. A **quadratic equation** has a
variable squared as its highest power. Its **roots** (also called *solutions* or
*zeros*) are the values that make the equation true. We will first solve equations whose
squared term stands alone, then turn any quadratic into that form by **completing the
square**.

## 1. What Does It Mean to Find a Quadratic Root?

In $x^2-9=0$, a root is a number that makes the left side zero. Both $3$ and $-3$ work:

$$3^2-9=0 \qquad\text{and}\qquad (-3)^2-9=0.$$

So the roots are $x=3$ and $x=-3$. A quadratic can have two real roots, one repeated real
root, or no real roots.

## 2. The Square-Root Principle

If $u^2=k$, then for $k>0$,

$$u=\pm\sqrt{k}.$$

The $\pm$ is essential: a positive number and its negative have the same square. If
$k=0$, then $u=0$ is the only solution. If $k<0$, there is no real-number solution,
because a real square cannot be negative.

### Reading Example: No Linear Term

Solve $x^2-49=0$.

$$
\begin{aligned}
x^2-49&=0\\
x^2&=49\\
x&=\pm\sqrt{49}\\
x&=\pm7
\end{aligned}
$$

The roots are $\boxed{x=7}$ and $\boxed{x=-7}$. Always check both values in the original
equation.

## 3. Isolate the Entire Square First

The squared expression does not need to be exactly $x^2$. To solve

$$a(x-h)^2+k=0,$$

1. Move $k$ to the other side.
2. Divide by $a$.
3. Take **both** square roots.
4. Solve the two resulting linear equations.

### Reading Example: A Shifted Square

Solve $3(x-2)^2-75=0$.

$$
\begin{aligned}
3(x-2)^2&=75\\
(x-2)^2&=25\\
x-2&=\pm5.
\end{aligned}
$$

The plus case gives $x=7$; the minus case gives $x=-3$. Thus
$\boxed{x=7\text{ or }x=-3}$.

Writing $x-2=\sqrt{25}=5$ would lose a root. The symbol $\sqrt{25}$ is the principal
(nonnegative) square root, but the equation $(x-2)^2=25$ allows two values for $x-2$.

## 4. Why Completing the Square Works

An ordinary quadratic such as $x^2+6x-7=0$ has a linear term, so there is no isolated
square yet. But adding $9$ makes the first two terms a perfect square:

$$x^2+6x+9=(x+3)^2.$$

The number to add comes from halving the coefficient of $x$, then squaring:

$$\left(\frac{6}{2}\right)^2=3^2=9.$$

Adding the same number to both sides keeps the equation balanced and creates a form where
the square-root principle applies.

## 5. Core Template: Completing the Square

For $x^2+bx+c=0$:

1. Move the constant: $x^2+bx=-c$.
2. Compute $\left(\dfrac b2\right)^2$.
3. Add that number to **both** sides.
4. Factor the left side as a binomial square.
5. Take both square roots and solve for $x$.

Complete the square only after the coefficient of $x^2$ is $1$. If it is not, divide every
term by that coefficient first.

### Reading Example: A Monic Quadratic

Solve $x^2+6x-7=0$.

$$
\begin{aligned}
x^2+6x&=7\\
x^2+6x+9&=7+9\\
(x+3)^2&=16\\
x+3&=\pm4.
\end{aligned}
$$

So $\boxed{x=1\text{ or }x=-7}$. Both values make $x^2+6x-7$ equal zero.

## 6. Leading Coefficient Not Equal to 1

Solve $2x^2+8x-10=0$.

First divide **every term** by $2$:

$$x^2+4x-5=0.$$

Now complete the square. Half of $4$ is $2$, and $2^2=4$:

$$
\begin{aligned}
x^2+4x&=5\\
x^2+4x+4&=5+4\\
(x+2)^2&=9\\
x+2&=\pm3.
\end{aligned}
$$

Thus $\boxed{x=1\text{ or }x=-5}$.

### Reading Example: Fractions After Dividing

Dividing by the leading coefficient does **not** need to leave integer coefficients. Solve

$$3x^2+5x+1=0.$$

Divide every term by $3$:

$$x^2+\frac53x+\frac13=0.$$

Move the constant. Half of $\frac53$ is $\frac56$, so the number needed to complete the
square is $\left(\frac56\right)^2=\frac{25}{36}$:

$$
\begin{aligned}
x^2+\frac53x&=-\frac13\\
x^2+\frac53x+\frac{25}{36}&=-\frac13+\frac{25}{36}\\
\left(x+\frac56\right)^2&=\frac{13}{36}\\
x+\frac56&=\pm\frac{\sqrt{13}}6.
\end{aligned}
$$

Subtract $\frac56$ from both cases:

$$\boxed{x=\frac{-5+\sqrt{13}}6\text{ or }x=\frac{-5-\sqrt{13}}6}.$$

Fractions are not a sign that the method failed. Keep each fraction exact, use a common
denominator when adding, and do not round the square root unless an approximation is asked
for. Completing the square is a useful way to rewrite a quadratic, not merely a route to a
memorized formula; later lessons will use that rewritten form to reveal other properties of
quadratic functions.

## 7. The Right Side Predicts the Number of Real Roots

After completing the square:

- $(x-h)^2=$ a positive number gives two real roots.
- $(x-h)^2=0$ gives one real root, $x=h$.
- $(x-h)^2=$ a negative number gives no real roots.

For example, $x^2+4x+8=0$ becomes

$$
\begin{aligned}
x^2+4x&=-8\\
x^2+4x+4&=-8+4\\
(x+2)^2&=-4.
\end{aligned}
$$

There are no real roots, since no real number squared equals $-4$.

## 8. Class Practice 1: Square Roots First

### Problem

Solve $4(x+1)^2=36$.

<details>
<summary>Solution</summary>

Divide by $4$: $(x+1)^2=9$. Take both square roots: $x+1=\pm3$.
Therefore, $\boxed{x=2\text{ or }x=-4}$.

</details>

## 9. Class Practice 2: Complete the Square

### Problem

Solve $x^2-10x+21=0$ by completing the square.

<details>
<summary>Solution</summary>

Move the constant: $x^2-10x=-21$. Half of $-10$ is $-5$, whose square is $25$:

$$
\begin{aligned}
x^2-10x+25&=-21+25\\
(x-5)^2&=4\\
x-5&=\pm2.
\end{aligned}
$$

Therefore, $\boxed{x=7\text{ or }x=3}$.

</details>

## 10. Class Practice 3: Leading Coefficient Not Equal to 1

### Problem

Solve $3x^2-12x-15=0$ by completing the square.

<details>
<summary>Solution</summary>

Divide by $3$: $x^2-4x-5=0$, so $x^2-4x=5$. Add
$\left(\frac{-4}{2}\right)^2=4$ to both sides:

$$
\begin{aligned}
x^2-4x+4&=5+4\\
(x-2)^2&=9\\
x-2&=\pm3.
\end{aligned}
$$

So $\boxed{x=5\text{ or }x=-1}$.

</details>

## 11. Class Practice 4: Fractional Coefficients and Irrational Roots

### Problem

Solve $4x^2+6x-1=0$ by completing the square.

<details>
<summary>Solution</summary>

Divide every term by $4$:

$$x^2+\frac32x-\frac14=0.$$

Move the constant, then add the square of half of $\frac32$, which is
$\left(\frac34\right)^2=\frac9{16}$:

$$
\begin{aligned}
x^2+\frac32x&=\frac14\\
x^2+\frac32x+\frac9{16}&=\frac14+\frac9{16}\\
\left(x+\frac34\right)^2&=\frac{13}{16}\\
x+\frac34&=\pm\frac{\sqrt{13}}4.
\end{aligned}
$$

Therefore,

$$\boxed{x=\frac{-3+\sqrt{13}}4\text{ or }x=\frac{-3-\sqrt{13}}4}.$$

</details>

## 12. Class Practice 5: Fractional Coefficients and Rational Roots

### Problem

Solve $5x^2-7x-6=0$ by completing the square.

<details>
<summary>Solution</summary>

After dividing by $5$, both remaining coefficients are fractions:

$$x^2-\frac75x-\frac65=0.$$

Move the constant. Half of $-\frac75$ is $-\frac7{10}$, whose square is
$\frac{49}{100}$:

$$
\begin{aligned}
x^2-\frac75x&=\frac65\\
x^2-\frac75x+\frac{49}{100}&=\frac65+\frac{49}{100}\\
\left(x-\frac7{10}\right)^2&=\frac{169}{100}\\
x-\frac7{10}&=\pm\frac{13}{10}.
\end{aligned}
$$

The plus case gives $x=2$; the minus case gives $x=-\frac35$. Thus
$\boxed{x=2\text{ or }x=-\frac35}$.

</details>

## 13. Class Practice 6: A Repeated Real Root

### Problem

Solve $4x^2-12x+9=0$ by completing the square.

<details>
<summary>Solution</summary>

Divide every term by $4$:

$$x^2-3x+\frac94=0.$$

Move the constant. Half of $-3$ is $-\frac32$, and its square is $\frac94$:

$$
\begin{aligned}
x^2-3x&=-\frac94\\
x^2-3x+\frac94&=-\frac94+\frac94\\
\left(x-\frac32\right)^2&=0.
\end{aligned}
$$

Taking the square root gives $x-\frac32=0$, so the only real root is
$\boxed{x=\frac32}$. It is called a **repeated root** because the two square-root cases
are the same when the right side is zero.

</details>

## 14. Class Practice 7: No Real Roots

### Problem

Solve $2x^2+4x+5=0$ by completing the square.

<details>
<summary>Solution</summary>

Divide every term by $2$:

$$x^2+2x+\frac52=0.$$

Move the constant and add $\left(\frac22\right)^2=1$ to both sides:

$$
\begin{aligned}
x^2+2x&=-\frac52\\
x^2+2x+1&=-\frac52+1\\
(x+1)^2&=-\frac32.
\end{aligned}
$$

There is no real number whose square is $-\frac32$, so the equation has
$\boxed{\text{no real solutions}}$.

</details>

## 15. Common Mistakes

### 15.1 Forgetting the $\pm$

From $(x-4)^2=25$, writing only $x-4=5$ misses one root. Write $x-4=\pm5$.

### 15.2 Adding to Only One Side

Changing $x^2+6x=7$ into $(x+3)^2=7$ changes the equation. Add $9$ to both sides, giving
$(x+3)^2=16$.

### 15.3 Using the Wrong Number

For $x^2+bx$, add $\left(\frac b2\right)^2$, not $b^2$. For $x^2-10x$, add $25$, not
$100$.

### 15.4 Skipping the Division Step

For $2x^2+8x-10=0$, first divide by $2$. Completing the square directly from the original
coefficients does not make a simple binomial square.

### 15.5 Rounding Fractions or Radicals Too Soon

In an equation such as $\left(x+\frac56\right)^2=\frac{13}{36}$, keep
$\frac{\sqrt{13}}6$ exact. Replacing it with a decimal early makes subsequent arithmetic
less accurate and hides the exact roots.

## 16. Key Takeaways

- A root is a value that makes a quadratic equation true; a quadratic can have two, one,
  or no real roots.
- Isolate a squared expression and use $u^2=k \Rightarrow u=\pm\sqrt{k}$.
- To complete the square in $x^2+bx$, add $\left(\dfrac b2\right)^2$ to both sides.
- Divide by the leading coefficient before completing the square when it is not $1$.
- Fractional coefficients after dividing are normal; use exact fraction arithmetic to
  complete the square.
- Completing the square transforms any quadratic equation into a form solvable with square
  roots.
