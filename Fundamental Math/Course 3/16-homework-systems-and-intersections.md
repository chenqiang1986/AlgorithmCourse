# Homework: Lesson 16 — Two-Variable Systems and Line Intersections
*Fundamental Math / Course 3*

Each system represents two lines. When a system has one solution, give the intersection as
an ordered pair. Show your chosen method, back-substitute, and check when appropriate.
Attempt every problem before opening its solution.

## Part A: Choose a Method and Solve

**Problem (Substitution).** Solve:

$$\begin{cases}y=5x-8\\2x+y=13\end{cases}$$

<details><summary>Solution</summary>

$$2x+(5x-8)=13\quad\Longrightarrow\quad x=3.$$

Then $y=7$, so the solution is $\boxed{(3,7)}$.

$\square$

</details>

**Problem (Substitution).** Solve:

$$\begin{cases}x=4-y\\3x+2y=9\end{cases}$$

<details><summary>Solution</summary>

$$3(4-y)+2y=9\quad\Longrightarrow\quad 12-y=9\quad\Longrightarrow\quad y=3.$$

Then $x=1$, so the solution is $\boxed{(1,3)}$.

$\square$

</details>

**Problem (Elimination).** Solve:

$$\begin{cases}7x+3y=17\\2x-3y=1\end{cases}$$

<details><summary>Solution</summary>

Adding eliminates $y$: $9x=18$, so $x=2$. Then $2(2)-3y=1$, giving $y=1$.
The solution is $\boxed{(2,1)}$.

$\square$

</details>

**Problem (Elimination).** Solve:

$$\begin{cases}3x+2y=4\\5x-4y=18\end{cases}$$

<details><summary>Solution</summary>

Multiply the first equation by $2$ and add:

$$6x+4y=8,\qquad 5x-4y=18,\qquad 11x=26.$$

Thus $x=\frac{26}{11}$. Substitution gives $y=-\frac{17}{11}$, so the solution is
$\boxed{\left(\frac{26}{11},-\frac{17}{11}\right)}$.

$\square$

</details>

**Problem (Choose efficiently).** Solve the system below. State why your method is
efficient.

$$\begin{cases}6x-y=14\\3x+4y=7\end{cases}$$

<details><summary>Solution</summary>

Substitution is efficient because the first equation has coefficient $-1$ on $y$:
$y=6x-14$.

$$3x+4(6x-14)=7\quad\Longrightarrow\quad 27x=63\quad\Longrightarrow\quad x=\frac73.$$

Then $y=0$. The solution is $\boxed{\left(\frac73,0\right)}$.

$\square$

</details>

## Part B: Special Systems

**Problem (Same line).** State the number of solutions and explain.

$$\begin{cases}y=2x-1\\4x-2y=2\end{cases}$$

<details><summary>Solution</summary>

Dividing the second equation by $-2$ gives $y=2x-1$. The equations represent the same
line, so there are $\boxed{\text{infinitely many solutions}}$.

$\square$

</details>

**Problem (Parallel lines).** State the number of solutions and explain.

$$\begin{cases}3x+y=5\\6x+2y=16\end{cases}$$

<details><summary>Solution</summary>

Doubling the first equation gives $6x+2y=10$, which conflicts with $6x+2y=16$.
The lines are parallel and distinct, so there is $\boxed{\text{no solution}}$.

$\square$

</details>

**Problem (Vertical line).** Find the intersection of $x=5$ and $2x+3y=4$.

<details><summary>Solution</summary>

$$2(5)+3y=4\quad\Longrightarrow\quad y=-2.$$

The intersection is $\boxed{(5,-2)}$.

$\square$

</details>

## Part C: Connect Algebra and Graphs

**Problem (Graph and solve).** Graph $y=-x+6$ and $y=2x$ on the same coordinate plane.
Use algebra to find the exact intersection, then verify it agrees with the graph.

<details><summary>Solution</summary>

Set $-x+6=2x$. Then $3x=6$, so $x=2$ and $y=4$. The intersection is
$\boxed{(2,4)}$. It is also the crossing seen on the graph.

$\square$

</details>

**Problem (Build one equation).** Line $L$ passes through $(-1,4)$ and $(3,-4)$. Write
an equation for $L$, then find where it intersects $x+y=1$.

<details><summary>Solution</summary>

$$m=\frac{-4-4}{3-(-1)}=-2.$$

Using $(-1,4)$ gives $L: y=-2x+2$. The other line is $y=1-x$, so

$$-2x+2=1-x\quad\Longrightarrow\quad x=1,\qquad y=0.$$

The intersection is $\boxed{(1,0)}$.

$\square$

</details>

## Part D: Systems in Context

**Problem (Two item prices).** At one table, $2$ bracelets and $3$ keychains cost
$\$19$. At another, $4$ bracelets and $1$ keychain cost $\$17$. Find the price of one
bracelet and one keychain.

<details><summary>Solution</summary>

Let $b$ and $k$ be the bracelet and keychain prices:

$$\begin{cases}2b+3k=19\\4b+k=17.\end{cases}$$

Multiply the second equation by $-3$ and add to the first, giving $-10b=-32$.
Thus $b=\$3.20$. Then $4(3.20)+k=17$, so $k=\$4.20$.

A bracelet costs $\boxed{\$3.20}$ and a keychain costs $\boxed{\$4.20}$.

$\square$

</details>

**Problem (Taxi comparison).** Taxi A charges a $\$4$ starting fee plus $\$2.50$ per mile.
Taxi B charges a $\$10$ starting fee plus $\$1.50$ per mile.

1. Write an equation for each taxi’s cost $C$ after $m$ miles.
2. At how many miles do the costs match?
3. What is the common cost, and what does the intersection mean?

<details><summary>Solution</summary>

The equations are $C=2.5m+4$ and $C=1.5m+10$.

$$2.5m+4=1.5m+10\quad\Longrightarrow\quad m=6.$$

The common cost is $C=2.5(6)+4=19$. The intersection $\boxed{(6,19)}$ means that after
$\boxed{6\text{ miles}}$, both taxis cost $\boxed{\$19}$.

$\square$

</details>

