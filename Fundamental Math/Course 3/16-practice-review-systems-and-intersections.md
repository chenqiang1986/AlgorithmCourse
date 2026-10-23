# Lesson 16: Practice Review — Two-Variable Systems and Line Intersections
*Fundamental Math / Course 3*

Today’s review connects two names for the same mathematical event: solving a two-variable
linear system finds the point where its two lines intersect. Work each problem before
opening its solution. Show enough algebra that another person could check your method.

## Learning Targets

By the end of class, you should be able to:

- solve a two-variable linear system by substitution or elimination;
- choose an efficient method for a given system;
- interpret a system’s solution as the intersection of two lines;
- recognize one solution, no solution, and infinitely many solutions; and
- model and interpret an intersection in context.

## Quick Strategy Check

| If you notice... | A good first choice is... |
| --- | --- |
| A variable is already isolated, such as $y=3x-1$ | Substitution |
| A variable has coefficient $1$ or $-1$ | Usually substitution |
| Coefficients are already opposites or equal | Elimination |
| Small multiples can make coefficients opposites | Elimination |

After finding one coordinate, always find the other and write the answer as an ordered
pair. Check the pair in both original equations.

## Part A: Warm-Up — What Does the System Represent?

**Problem (Checking a solution).** Does $(2,3)$ solve the system?

$$
\begin{cases}
x+y=5\\
2x-y=1
\end{cases}
$$

<details><summary>Solution</summary>

In the first equation, $2+3=5$. In the second, $2(2)-3=1$. Both equations are true, so
$\boxed{(2,3)}$ solves the system.

$\square$

</details>

**Problem (Same line).** Predict the number of solutions without using substitution or
elimination.

$$
\begin{cases}
y=-2x+4\\
2x+y=4
\end{cases}
$$

<details><summary>Solution</summary>

The second equation rearranges to $y=-2x+4$. Both equations describe the same line, so
there are $\boxed{\text{infinitely many solutions}}$.

$\square$

</details>

**Problem (Parallel lines).** Predict the number of solutions without using substitution
or elimination.

$$
\begin{cases}
y=\frac13x-2\\
x-3y=9
\end{cases}
$$

<details><summary>Solution</summary>

The second equation becomes $y=\frac13x-3$. The lines have the same slope but different
intercepts, so they are parallel. There is $\boxed{\text{no solution}}$.

$\square$

</details>

## Part B: Solve by Substitution

**Problem (Substitution from slope-intercept form).** Solve the system.

$$
\begin{cases}
y=4x-5\\
3x+y=16
\end{cases}
$$

<details><summary>Solution</summary>

$$
\begin{aligned}
3x+(4x-5)&=16\\
7x&=21\\
x&=3.
\end{aligned}
$$

Then $y=4(3)-5=7$. The solution, and intersection, is $\boxed{(3,7)}$.

$\square$

</details>

**Problem (Substitution with a fraction).** Solve the system.

$$
\begin{cases}
x=2y+5\\
3x-y=9
\end{cases}
$$

<details><summary>Solution</summary>

$$
\begin{aligned}
3(2y+5)-y&=9\\
5y&=-6\\
y&=-\frac65.
\end{aligned}
$$

Then $x=2\left(-\frac65\right)+5=\frac{13}{5}$. The solution is
$\boxed{\left(\frac{13}{5},-\frac65\right)}$.

$\square$

</details>

**Problem (A vertical line).** Find the intersection of $x=-4$ and
$y=-\frac12x+6$. Which substitution is immediate?

<details><summary>Solution</summary>

The vertical line gives $x=-4$, so substitute that value:

$$y=-\frac12(-4)+6=8.$$

The intersection is $\boxed{(-4,8)}$. Directly substituting the known $x$-value is
immediate.

$\square$

</details>

## Part C: Solve by Elimination

**Problem (Opposite coefficients).** Solve the system by elimination.

$$
\begin{cases}
5x+2y=19\\
3x-2y=5
\end{cases}
$$

<details><summary>Solution</summary>

Add the equations:

$$8x=24\quad\Longrightarrow\quad x=3.$$

From $3x-2y=5$, we get $9-2y=5$, so $y=2$. The solution is $\boxed{(3,2)}$.

$\square$

</details>

**Problem (Scale once).** Solve the system by elimination.

$$
\begin{cases}
2x+3y=7\\
4x-5y=23
\end{cases}
$$

<details><summary>Solution</summary>

Multiply the first equation by $-2$, then add:

$$
\begin{aligned}
-4x-6y&=-14\\
4x-5y&=23\\
-11y&=9.
\end{aligned}
$$

Thus $y=-\frac9{11}$. Substituting into $2x+3y=7$ gives $x=\frac{52}{11}$.
The solution is $\boxed{\left(\frac{52}{11},-\frac9{11}\right)}$.

$\square$

</details>

**Problem (Scale both equations).** Solve the system by elimination.

$$
\begin{cases}
3x+4y=18\\
5x-6y=4
\end{cases}
$$

<details><summary>Solution</summary>

Multiply the first equation by $3$ and the second by $2$:

$$
\begin{aligned}
9x+12y&=54\\
10x-12y&=8.
\end{aligned}
$$

Adding gives $19x=62$, so $x=\frac{62}{19}$. Substituting into the first original
equation gives $y=\frac{39}{19}$. The solution is
$\boxed{\left(\frac{62}{19},\frac{39}{19}\right)}$.

$\square$

</details>

## Part D: Systems and Their Graphs

**Problem (Graph and solve).** Graph $y=x+1$ and $y=-2x+7$ on the same coordinate plane.
Then use algebra to find their exact intersection. Does your algebraic answer match the
graph?

<details><summary>Solution</summary>

Use $(0,1)$ and $(2,3)$ for the first line, and $(0,7)$ and $(2,3)$ for the second. The
graph shows a crossing at $(2,3)$. Algebra confirms it:

$$x+1=-2x+7\quad\Longrightarrow\quad 3x=6\quad\Longrightarrow\quad x=2.$$

Then $y=3$, so the exact intersection is $\boxed{(2,3)}$, matching the graph.

$\square$

</details>

**Problem (Classify systems).** For each system, state whether it has one solution, no
solution, or infinitely many solutions. If there is one solution, find it.

1. $$\begin{cases}y=3x+2\\y=-x+10\end{cases}$$

2. $$\begin{cases}2x+y=6\\4x+2y=12\end{cases}$$

3. $$\begin{cases}x+y=1\\2x+2y=8\end{cases}$$

<details><summary>Solution</summary>

1. $3x+2=-x+10$ gives $x=2$ and $y=8$, so the one solution is $\boxed{(2,8)}$.
2. The second equation is twice the first, so there are
   $\boxed{\text{infinitely many solutions}}$.
3. Twice the first equation would be $2x+2y=2$, not $8$, so there is
   $\boxed{\text{no solution}}$.

$\square$

</details>

## Part E: Apply the Intersection

**Problem (Filling tanks).** Tank A starts with $18$ liters and gains $6$ liters per
minute. Tank B starts with $42$ liters and gains $2$ liters per minute.

1. Let $t$ be time in minutes and $W$ water in liters. Write an equation for each tank.
2. When do the tanks contain the same amount?
3. How much water does each contain then? Interpret the intersection.

<details><summary>Solution</summary>

The equations are $W=6t+18$ and $W=2t+42$. Set them equal:

$$6t+18=2t+42\quad\Longrightarrow\quad 4t=24\quad\Longrightarrow\quad t=6.$$

At $t=6$, $W=6(6)+18=54$. The intersection is $\boxed{(6,54)}$: after
$\boxed{6\text{ minutes}}$, each tank contains $\boxed{54\text{ liters}}$.

$\square$

</details>

## Exit Ticket

1. Solve:

   $$\begin{cases}y=2x+1\\x+y=10\end{cases}$$

2. Solve by elimination:

   $$\begin{cases}4x+y=11\\2x-y=1\end{cases}$$

3. How many solutions does this system have?

   $$\begin{cases}y=-3x+4\\6x+2y=8\end{cases}$$

<details><summary>Answers</summary>

1. $\boxed{(3,7)}$
2. $\boxed{(2,3)}$
3. $\boxed{\text{infinitely many solutions}}$

</details>

