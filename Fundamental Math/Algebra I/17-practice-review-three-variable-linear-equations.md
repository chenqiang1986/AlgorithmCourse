# Lesson 17: Practice Review — Three-Variable Linear Equations
*Fundamental Math / Algebra I*

Today is a practice-focused review of solving linear systems in $x$, $y$, and $z$.
The goal is not to memorize one set of multipliers: it is to organize the work so that
each elimination step is clear, accurate, and easy to check.

## Learning Targets

By the end of class, you should be able to:

- solve a three-equation, three-variable linear system by elimination;
- create two independent two-variable equations by eliminating the same variable twice;
- back-substitute to find the remaining variable; and
- check an ordered triple in all three original equations.

## The Review Routine

For a system with equations (1), (2), and (3):

1. Choose a variable to eliminate. Pick one with friendly coefficients when possible.
2. Eliminate that variable from two different pairs of original equations.
3. Solve the resulting two-variable system.
4. Substitute those two values into an original equation to find the third value.
5. Check the ordered triple in the original system.

Keep the original equations visible. The two new equations created in Step 2 are
temporary helper equations, not replacements for the whole system.

## Class Practice 1: Start With Light Scaling

**Example (Direct Elimination).** Solve the system.

$$
\begin{cases}
x+y+z=6 & (1)\\
x-y+z=4 & (2)\\
2x+y-z=3 & (3)
\end{cases}
$$

**Solution:**

Eliminate $x$ using (1) and (2):

$$
(1)-(2):\quad 2y=2,\qquad y=1.
$$

Eliminate $x$ using (1) and (3):

$$
2(1)-(3):\quad (2x+2y+2z)-(2x+y-z)=12-3,
$$
$$
y+3z=9.
$$

Substitute $y=1$ into $y+3z=9$:

$$
1+3z=9\quad\Longrightarrow\quad z=\frac{8}{3}.
$$

Fractions are valid answers. Using the given equations exactly, $y=1$,
$z=\frac{8}{3}$, and then (1) gives $x=\frac{7}{3}$. The solution is

$$
\boxed{\left(\frac{7}{3},1,\frac{8}{3}\right)}.
$$

Checks: $\frac{7}{3}+1+\frac{8}{3}=6$,
$\frac{7}{3}-1+\frac{8}{3}=4$, and
$2\left(\frac{7}{3}\right)+1-\frac{8}{3}=3$.

$\square$

**Class discussion:** Fractions are valid answers. Do not change a problem merely because
the arithmetic is not all integers.

## Class Practice 2: Scale Carefully

**Example (Two Independent Eliminations).** Solve the system.

$$
\begin{cases}
2x+y-z=1 & (1)\\
x-2y+z=6 & (2)\\
3x+y+2z=9 & (3)
\end{cases}
$$

**Solution:**

Eliminate $x$ from (1) and (2):

$$
(1)-2(2):\quad (2x+y-z)-(2x-4y+2z)=1-12,
$$
$$
5y-3z=-11. \tag{4}
$$

Eliminate $x$ from (1) and (3). Multiply (1) by $3$ and (3) by $2$:

$$
3(1):\ 6x+3y-3z=3
$$
$$
2(3):\ 6x+2y+4z=18
$$
$$
3(1)-2(3):\quad y-7z=-15. \tag{5}
$$

Now solve (4) and (5). From (5), $y=7z-15$. Substitute into (4):

$$
5(7z-15)-3z=-11
\quad\Longrightarrow\quad 32z=64
\quad\Longrightarrow\quad z=2.
$$

Then $y=7(2)-15=-1$. Substitute into (2):

$$
x-2(-1)+2=6\quad\Longrightarrow\quad x=2.
$$

The solution is $\boxed{(2,-1,2)}$. Checks give
$2(2)+(-1)-2=1$, $2-2(-1)+2=6$, and $3(2)+(-1)+2(2)=9$.

$\square$

## Class Practice 3: Choose the Convenient Variable

**Example (Eliminating $z$ First).** Solve the system.

$$
\begin{cases}
2x+y+z=3 & (1)\\
x-3y+2z=-7 & (2)\\
3x+2y-z=8 & (3)
\end{cases}
$$

**Solution:**

The coefficients of $z$ are $1$, $2$, and $-1$, so eliminate $z$.

$$
2(1)-(2):\quad (4x+2y+2z)-(x-3y+2z)=6-(-7),
$$
$$
3x+5y=13. \tag{4}
$$

Add (1) and (3):

$$
5x+3y=11. \tag{5}
$$

Eliminate $y$ from (4) and (5):

$$
3(4):\ 9x+15y=39
$$
$$
5(5):\ 25x+15y=55
$$
$$
5(5)-3(4):\quad 16x=16,\qquad x=1.
$$

Equation (5) gives $5(1)+3y=11$, so $y=2$. Finally, (1) gives
$2(1)+2+z=3$, so $z=-1$. The solution is $\boxed{(1,2,-1)}$.
The three left sides evaluate to $3$, $-7$, and $8$, respectively.

$\square$

## Class Practice 4: Find and Repair the Sign Error

**Example (Error Analysis).** A student begins solving the system below and writes
$3y+z=-6$ after subtracting. Identify and repair the error, then finish the problem.

$$
\begin{cases}
x+y+z=6 & (1)\\
2x-y+z=6 & (2)\\
x+3y-2z=-1 & (3)
\end{cases}
$$

**Solution:**

Using $(2)-2(1)$ gives

$$
(2x-y+z)-(2x+2y+2z)=6-12
\quad\Longrightarrow\quad -3y-z=-6.
$$

Multiplying **both sides** by $-1$ gives $3y+z=6$, not $3y+z=-6$.

Use a second pair to eliminate $x$:

$$
(3)-(1):\quad 2y-3z=-7. \tag{4}
$$

Together with $3y+z=6$, solve by substituting $z=6-3y$ into (4):

$$
2y-3(6-3y)=-7
\quad\Longrightarrow\quad 11y=11
\quad\Longrightarrow\quad y=1.
$$

Then $z=6-3(1)=3$, and (1) gives $x+1+3=6$, so $x=2$.
The solution is $\boxed{(2,1,3)}$; the three left sides evaluate to $6$, $6$, and $-1$.

$\square$

## Partner Practice

Work with a partner: agree on a variable to eliminate before doing any scaling. Each
partner should create one of the two helper equations, then compare results.

**Example (Partner System).** Solve the system.

$$
\begin{cases}
x+2y-z=0\\
2x-y+3z=5\\
3x+y+z=2
\end{cases}
$$

**Solution:**

Eliminate $x$ with $2(1)-(2)$ and $3(1)-(3)$:

$$
5y-5z=-5\quad\Longrightarrow\quad y-z=-1,
$$
$$
5y-4z=-2.
$$

Substitute $y=z-1$ into the second equation:

$$
5(z-1)-4z=-2\quad\Longrightarrow\quad z=3.
$$

Thus $y=2$. From the first original equation, $x+2(2)-3=0$, so $x=-1$.
The solution is $\boxed{(-1,2,3)}$; the three left sides evaluate to $0$, $5$, and $2$.

$\square$

## Exit Ticket

Solve without notes. Show the two helper equations you create.

$$
\begin{cases}
x+y+z=4\\
2x-y+z=8\\
x+2y-z=-3
\end{cases}
$$

<details>
<summary>Answer</summary>

The solution is $\boxed{(2,-1,3)}$.

</details>

## Before You Leave

- Did you eliminate the same variable from two different pairs?
- When scaling, did you multiply every term, including the constant?
- Did you return to an original equation for back-substitution?
- Did your final ordered triple make all three original equations true?
