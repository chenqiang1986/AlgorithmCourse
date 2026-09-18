# Lesson 9: Unknown Coefficients and Solution Structure
*Fundamental Math / Course 3*

In [Lesson 8](./08-single-variable-linear-equations.md), an equation either simplified to
one value of $x$, a false statement, or a true statement. Here, a letter such as $k$ is a
**parameter**: it controls the equation, while $x$ is still the variable we are solving for.
Our job is to determine which values of $k$ give **one solution**, **no solution**, or
**infinitely many solutions**.

## 1. The Master Form

After distributing, combining like terms, and moving the $x$-terms to one side, every
single-variable linear equation with a parameter can be written as

$$A(k)x=B(k).$$

Here $A(k)$ and $B(k)$ are expressions involving $k$, but they contain no $x$. The value of
$A(k)$ decides what we can do next.

| What remains after simplifying | Solution structure |
|---|---|
| $A(k)x=B(k)$ with $A(k)\ne0$ | **Exactly one solution:** $x=\dfrac{B(k)}{A(k)}$ |
| $0x=B(k)$ with $B(k)\ne0$ | **No solution:** this says $0=$ a nonzero number |
| $0x=0$ | **Infinitely many solutions:** every value of $x$ works |

The key idea is that division by the coefficient of $x$ is allowed only when that coefficient
is not zero. The parameter values that make $A(k)=0$ are the only values that can cause a
change from the usual one-solution case.

### Reading Example: A Parameter That Creates No Solution

Determine the solution structure of

$$kx+4=3x+10.$$

First collect the $x$-terms:

$$kx-3x=10-4 \implies (k-3)x=6.$$

- If $k\ne3$, then $k-3\ne0$, so divide by $k-3$. There is exactly one solution,
  $x=\dfrac{6}{k-3}$.
- If $k=3$, the equation becomes $0x=6$, or $0=6$. This is false, so there is no solution.

Thus, **$k=3$ gives no solution; every other value of $k$ gives exactly one solution.**
There is no value of $k$ that gives infinitely many solutions.

**Non-obvious detail:** do not divide by $k-3$ before checking whether $k-3$ could be zero.
Doing so would silently discard the special case $k=3$.

## 2. When the Parameter Creates Infinitely Many Solutions

The exceptional value can instead make both sides of the simplified equation zero.

### Reading Example: A Parameter That Creates Infinitely Many Solutions

Determine the solution structure of

$$4x+2=kx+2.$$

Subtract $kx$ and $2$ from both sides:

$$4x-kx=0 \implies (4-k)x=0.$$

- If $k\ne4$, then $4-k\ne0$. Dividing gives $x=0$, so there is exactly one solution.
- If $k=4$, the equation becomes $0x=0$. Both original sides are $4x+2$, so every real
  number $x$ works.

Thus, **$k=4$ gives infinitely many solutions; every other value of $k$ gives exactly one
solution.** There is no value of $k$ that gives no solution.

This is the parameter version of Lesson 8's rule: after the variable terms cancel, a true
statement means infinitely many solutions and a false statement means none.

## 3. A Reliable Procedure

For any equation involving $x$ and a parameter such as $k$:

1. Treat $k$ like a number. Distribute and combine like terms on each side.
2. Move every $x$-term to one side and constants to the other.
3. Factor the coefficient of $x$, writing the equation as $A(k)x=B(k)$.
4. Find the parameter values for which $A(k)=0$. These are the only special cases.
5. Substitute each special value into $B(k)$:
   - nonzero right side: no solution;
   - zero right side: infinitely many solutions.
6. For all remaining parameter values, state the one solution (if requested) by dividing.

### Class Practice 1: One Solution Except for One Value

#### Problem

Determine the solution structure of $5x-7=(k+1)x+2$. Give $x$ when there is exactly one
solution.

<details>
<summary>Solution</summary>

Collect the $x$-terms and constants:

$$5x-(k+1)x=2+7 \implies (4-k)x=9.$$

The coefficient of $x$ is zero when $4-k=0$, so the special value is $k=4$.

- If $k=4$, then $0x=9$, which is false. There is **no solution**.
- If $k\ne4$, then divide by $4-k$: $x=\dfrac{9}{4-k}$. There is **exactly one solution**.

No value of $k$ gives infinitely many solutions.

</details>

### Class Practice 2: Distribute Before Classifying

#### Problem

Determine the solution structure of $2(x+3)+kx=5x+6$.

<details>
<summary>Solution</summary>

Distribute and simplify first:

$$2x+6+kx=5x+6$$

$$2x+kx-5x=0 \implies (k-3)x=0.$$

The special value is $k=3$.

- If $k=3$, then $0x=0$, so there are **infinitely many solutions**.
- If $k\ne3$, then dividing by $k-3$ gives $x=0$, so there is **exactly one solution**.

No value of $k$ gives no solution.

</details>

## 4. When the Parameter Is in a Constant Term

Sometimes the coefficient of $x$ cancels for *every* value of $k$. Then the parameter in
the constant terms alone decides whether the remaining statement is true or false.

### Reading Example: Coefficients Already Match

Determine the solution structure of

$$7x+k=7x-5.$$

Subtract $7x$ from both sides:

$$k=-5.$$

This statement contains no $x$.

- If $k=-5$, it says $-5=-5$, which is true for every $x$: **infinitely many solutions**.
- If $k\ne-5$, it is a false statement: **no solution**.

There is **never exactly one solution**, because the $x$-terms have canceled no matter what
$k$ is.

### Class Practice 3: Parameter in the Constant

#### Problem

Determine the solution structure of $3x+8=3x+k$.

<details>
<summary>Solution</summary>

Subtract $3x$ from both sides:

$$8=k.$$

- If $k=8$, the equation becomes $8=8$, so there are **infinitely many solutions**.
- If $k\ne8$, the equation becomes a false statement, so there is **no solution**.

There is no value of $k$ giving exactly one solution.

</details>

## 5. More Than One Exceptional Value

An equation is still linear in $x$ even if its coefficient contains a more complicated
expression in $k$. If that coefficient can be zero for more than one value of $k$, check
each value separately.

### Reading Example: All Three Outcomes in One Family

Determine the solution structure of

$$ (k-1)(k-2)x+k-1=0. $$

The coefficient of $x$ is $(k-1)(k-2)$, which is zero at $k=1$ and $k=2$. Check both:

- If $k=1$: $0x+0=0$, or $0=0$. There are **infinitely many solutions**.
- If $k=2$: $0x+1=0$, or $1=0$. There is **no solution**.
- If $k\ne1,2$: the coefficient is nonzero, so dividing gives exactly one solution:

$$x=-\frac{k-1}{(k-1)(k-2)}=-\frac{1}{k-2}.$$

The cancellation in the last fraction is valid only when $k\ne1$, which is already included
in this case. The complete classification is: $k=1$ gives infinitely many solutions,
$k=2$ gives no solution, and every other $k$ gives exactly one solution.

### Class Practice 4: Two Special Values

#### Problem

Determine the solution structure of

$$ (k+2)(k-1)x=k+2. $$

<details>
<summary>Solution</summary>

The coefficient of $x$ is zero when $k=-2$ or $k=1$.

- At $k=-2$: $0x=0$, so there are **infinitely many solutions**.
- At $k=1$: $0x=3$, so there is **no solution**.
- For $k\ne-2,1$, divide by $(k+2)(k-1)$:

$$x=\frac{k+2}{(k+2)(k-1)}=\frac{1}{k-1}.$$

So every other value of $k$ gives **exactly one solution**.

</details>

## 6. Common Mistakes

### 6.1 Treating $k$ as another variable to solve at the same time

In $kx+4=3x+10$, $k$ is not a second unknown to solve alongside $x$. It is a chosen number
that changes the equation. Classify the possible values of $k$, then solve for $x$ in each
case.

### 6.2 Dividing before testing for zero

From $(k-3)x=6$, writing $x=\dfrac6{k-3}$ without mentioning $k\ne3$ misses the no-solution
case. Always identify where the divisor equals zero first.

### 6.3 Calling $0x=0$ one solution

$0x=0$ is true for $x=0$, $x=5$, $x=-\pi$, and every other number. It has **infinitely many
solutions**, not just the solution $x=0$.

### 6.4 Canceling a parameter factor across cases

In $(k-1)(k-2)x+k-1=0$, canceling $k-1$ immediately would lose $k=1$. First separate the
values that make a factor zero; only then simplify the ordinary one-solution case.

## 7. Key Takeaways

- Simplify parameter equations to the form **$A(k)x=B(k)$**.
- If $A(k)\ne0$, there is exactly one solution: $x=\dfrac{B(k)}{A(k)}$.
- If $A(k)=0$ and $B(k)\ne0$, there is no solution.
- If $A(k)=0$ and $B(k)=0$, there are infinitely many solutions.
- Find and check every parameter value that makes the coefficient of $x$ zero before
  dividing or canceling.

The next lesson begins systems of two linear equations, where the same three solution
structures describe how two lines can intersect.
