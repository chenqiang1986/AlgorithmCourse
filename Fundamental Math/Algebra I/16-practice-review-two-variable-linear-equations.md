# Lesson 16: Practice Review — Two-Variable Linear Equations
*Fundamental Math / Algebra I*

This review revisits two-variable linear systems from Lessons 3–7. A solution is an
ordered pair that makes **both** equations true. Choose substitution when a variable is
already easy to isolate; choose elimination when matching coefficients keeps the arithmetic
clean. Show every transformation and check the final point in both original equations.

## Learning Targets

By the end of class, you should be able to:

- identify whether an ordered pair solves a system;
- solve a two-variable linear system by substitution or elimination;
- choose an efficient method and scale equations accurately;
- classify a system as having one, no, or infinitely many solutions; and
- model and interpret a situation with two linear equations.

## Quick Reference

For a system

$$
\begin{cases}
a_1x+b_1y=c_1\\
a_2x+b_2y=c_2,
\end{cases}
$$

- **Substitution:** isolate a variable, substitute it into the other equation, solve, and
  back-substitute.
- **Elimination:** multiply one or both equations so one pair of coefficients is opposite,
  then add the equations.
- One intersection means one solution; distinct parallel lines mean no solution; equivalent
  equations mean infinitely many solutions.

## Part A: Meaning of a Solution

### Problem 1

Does $(2,3)$ solve the system below? Justify your answer.

$$
\begin{cases}
x+y=5\\
2x-y=1
\end{cases}
$$

<details><summary>Solution</summary>

For $(2,3)$, the first equation gives $2+3=5$, and the second gives
$2(2)-3=1$. Both statements are true, so $\boxed{(2,3)}$ solves the system.

</details>

### Problem 2

Does $(1,4)$ solve the system below? Justify your answer.

$$
\begin{cases}
3x+y=7\\
x-2y=-7
\end{cases}
$$

<details><summary>Solution</summary>

The first equation works: $3(1)+4=7$. But $1-2(4)=-7$ is also true, so
$\boxed{(1,4)}$ solves the system.

</details>

## Part B: Substitution

### Problem 3

Solve by substitution.

$$
\begin{cases}
y=2x+1\\
3x+y=16
\end{cases}
$$

<details><summary>Solution</summary>

Substitute $2x+1$ for $y$:

$$3x+(2x+1)=16\quad\Longrightarrow\quad 5x=15\quad\Longrightarrow\quad x=3.$$

Then $y=2(3)+1=7$. The solution is $\boxed{(3,7)}$.

</details>

### Problem 4

Solve by substitution.

$$
\begin{cases}
x=3y-2\\
2x+y=11
\end{cases}
$$

<details><summary>Solution</summary>

$$2(3y-2)+y=11\quad\Longrightarrow\quad 7y=15\quad\Longrightarrow\quad y=\frac{15}{7}.$$

Then $x=3\left(\frac{15}{7}\right)-2=\frac{31}{7}$. Thus the solution is
$\boxed{\left(\frac{31}{7},\frac{15}{7}\right)}$.

</details>

## Part C: Elimination

### Problem 5

Solve by elimination.

$$
\begin{cases}
4x+3y=18\\
4x-y=6
\end{cases}
$$

<details><summary>Solution</summary>

Subtract the second equation from the first:

$$4y=12\quad\Longrightarrow\quad y=3.$$

Then $4x-3=6$, so $x=\frac94$. The solution is $\boxed{\left(\frac94,3\right)}$.

</details>

### Problem 6

Solve by elimination. State the multipliers you use.

$$
\begin{cases}
2x+5y=19\\
3x-2y=4
\end{cases}
$$

<details><summary>Solution</summary>

Multiply the first equation by $2$ and the second by $5$:

$$4x+10y=38$$
$$15x-10y=20$$

Adding gives $19x=58$, so $x=\frac{58}{19}$. Substituting into $3x-2y=4$ gives $y=0$.
The solution is $\boxed{\left(\frac{58}{19},0\right)}$.

</details>

## Part D: Number of Solutions

### Problem 7

Classify the system as having one solution, no solution, or infinitely many solutions.

$$
\begin{cases}
2x-3y=8\\
4x-6y=16
\end{cases}
$$

<details><summary>Solution</summary>

The second equation is twice the first, so both equations describe the same line. There
are $\boxed{\text{infinitely many solutions}}$.

</details>

### Problem 8

Classify the system as having one solution, no solution, or infinitely many solutions.

$$
\begin{cases}
x+2y=5\\
2x+4y=14
\end{cases}
$$

<details><summary>Solution</summary>

Doubling the first equation gives $2x+4y=10$, not $14$. The lines have matching
left-hand-side coefficients but different constants, so they are parallel. There is
$\boxed{\text{no solution}}$.

</details>

## Part E: Modeling

### Problem 9

At a school event, adult tickets cost $8$ dollars and student tickets cost $5$ dollars.
There were $43$ tickets sold for a total of $281$ dollars. How many of each kind were sold?

<details><summary>Solution</summary>

Let $a$ be adult tickets and $s$ be student tickets:

$$a+s=43\qquad 8a+5s=281.$$

Multiply the first equation by $-5$ and add:

$$-5a-5s=-215$$
$$8a+5s=281$$
$$3a=66,$$

so $a=22$ and $s=21$. The event sold $\boxed{22\text{ adult tickets and }21\text{ student tickets}}$.

</details>

## Exit Ticket

1. Solve $y=x-4$ and $2x+y=11$.
2. Classify $3x+y=6$ and $6x+2y=12$.
3. In one sentence, explain why a final ordered pair must be checked in both equations.

<details><summary>Answers</summary>

1. $x=5$, $y=1$: $\boxed{(5,1)}$.
2. $\boxed{\text{Infinitely many solutions}}$; the second equation is twice the first.
3. A system's solution must satisfy every equation in the system.

</details>
