# Homework: Lesson 14 — Intersections of Two Lines on the $xy$-Plane
*Fundamental Math / Course 3*

Find a point only when it satisfies **both** line equations. For graphing problems, draw
both lines on one labeled coordinate plane and show at least two points on each line.
For all problems, show the equation or substitution that supports your answer. Try each
problem before opening its solution.

## Part A: See the Intersection on a Graph

**Problem 1 (A grid-point intersection).** Graph $y=x+2$ and $y=-x+4$. State their
intersection as an ordered pair and check it in both equations.

<details><summary>Solution</summary>

**Solution:**

The first line passes through $(0,2)$ and $(1,3)$; the second passes through $(0,4)$
and $(1,3)$. They cross at $\boxed{(1,3)}$. Check: $3=1+2$ and $3=-1+4$.

$\square$

</details>

**Problem 2 (A crossing below the $x$-axis).** Graph $y=-2x+1$ and $y=x-5$.
Estimate their intersection from your graph, then find its exact coordinates by algebra.

<details><summary>Solution</summary>

**Solution:**

The first line passes through $(0,1)$ and $(2,-3)$; the second passes through
$(0,-5)$ and $(2,-3)$. The graph shows a crossing near $(2,-3)$. Algebra confirms it:

$$-2x+1=x-5\quad\Longrightarrow\quad 3x=6\quad\Longrightarrow\quad x=2.$$

Then $y=2-5=-3$, so the exact intersection is $\boxed{(2,-3)}$.

$\square$

</details>

## Part B: Find Exact Coordinates

**Problem 3 (Equate the $y$-values).** Find the intersection of $y=4x-7$ and
$y=-x+8$. Check the point in both equations.

<details><summary>Solution</summary>

**Solution:**

$4x-7=-x+8$ gives $5x=15$, so $x=3$. Then $y=4(3)-7=5$. The point is
$\boxed{(3,5)}$; the second equation also gives $-3+8=5$.

$\square$

</details>

**Problem 4 (Fractional slope).** Find the exact intersection of
$y=\frac12x-1$ and $y=-x+5$.

<details><summary>Solution</summary>

**Solution:**

Set $\frac12x-1=-x+5$. Then $\frac32x=6$, so $x=4$. Substitution gives
$y=\frac12(4)-1=1$. The intersection is $\boxed{(4,1)}$; the other line gives
$-4+5=1$.

$\square$

</details>

**Problem 5 (Standard form).** Find the intersection of $3x+2y=13$ and $x-y=1$.

<details><summary>Solution</summary>

**Solution:**

From $x-y=1$, get $y=x-1$. Substitute into the first equation:

$$3x+2(x-1)=13\quad\Longrightarrow\quad 5x=15\quad\Longrightarrow\quad x=3.$$

Then $y=3-1=2$. The intersection is $\boxed{(3,2)}$. Check:
$3(3)+2(2)=13$ and $3-2=1$.

$\square$

</details>

**Problem 6 (A vertical line).** Where do $x=-3$ and $y=2x+7$ intersect?

<details><summary>Solution</summary>

**Solution:**

The vertical line fixes $x=-3$. The other line gives $y=2(-3)+7=1$, so the
intersection is $\boxed{(-3,1)}$.

$\square$

</details>

**Problem 7 (A horizontal line).** Where do $y=-2$ and $3x-y=11$ intersect?

<details><summary>Solution</summary>

**Solution:**

The horizontal line fixes $y=-2$. Substituting into the second equation gives
$3x-(-2)=11$, so $3x=9$ and $x=3$. The intersection is $\boxed{(3,-2)}$.

$\square$

</details>

## Part C: Decide How Many Intersections

For each pair, state whether the lines have one intersection, no intersection, or
infinitely many intersections. Explain using equations, slopes, or both.

**Problem 8 (Equivalent equations).** $y=3x-1$ and $6x-2y=2$.

<details><summary>Solution</summary>

**Solution:**

Dividing $6x-2y=2$ by $2$ gives $3x-y=1$, or $y=3x-1$. Both equations describe the
same line, so there are $\boxed{\text{infinitely many intersections}}$. All solutions
have the form $(x,3x-1)$ for real $x$.

$\square$

</details>

**Problem 9 (Parallel lines).** $y=-x+2$ and $x+y=5$.

<details><summary>Solution</summary>

**Solution:**

The second equation becomes $y=-x+5$. Both lines have slope $-1$, but their
$y$-intercepts are $2$ and $5$. They are distinct parallel lines, so there are
$\boxed{\text{no intersections}}$.

$\square$

</details>

## Part D: Write a Line Equation First

**Problem 10 (Line from two points).** Line $L$ passes through $(-2,1)$ and $(2,9)$.
Write an equation for $L$, then find where it intersects $y=-x+2$.

<details><summary>Solution</summary>

**Solution:**

The slope is $m=\frac{9-1}{2-(-2)}=2$. Using $(-2,1)$ gives
$1=2(-2)+b$, so $b=5$ and $L$ is $y=2x+5$.

Set $2x+5=-x+2$. Then $3x=-3$, so $x=-1$ and $y=3$. The intersection is
$\boxed{(-1,3)}$. Both equations give $3$ when $x=-1$.

$\square$

</details>

**Problem 11 (Line from a slope and a point).** Line $M$ has slope $-3$ and passes
through $(1,4)$. Write its equation, then find where it intersects $2x+y=5$.

<details><summary>Solution</summary>

**Solution:**

Write $M$ as $y=-3x+b$. The point gives $4=-3(1)+b$, so $b=7$ and
$M$ is $y=-3x+7$.

Substitute into $2x+y=5$: $2x+(-3x+7)=5$, so $-x=-2$ and $x=2$.
Then $y=-3(2)+7=1$. The intersection is $\boxed{(2,1)}$.

$\square$

</details>

**Problem 12 (A line that cannot use slope-intercept form).** Line $N$ passes
through $(4,-1)$ and $(4,5)$. Write its equation, then find where it intersects
$y=x-6$.

<details><summary>Solution</summary>

**Solution:**

Both given points have $x=4$, so $N$ is the vertical line $x=4$. Substitute
into the other line: $y=4-6=-2$. The intersection is $\boxed{(4,-2)}$.

$\square$

</details>

## Part E: Interpret an Intersection

**Problem 13 (Two ride plans).** Plan A costs $\$10$ to join plus $\$4$ per ride.
Plan B costs $\$22$ to join plus $\$2$ per ride. Let $x$ be the number of rides and
$y$ the total cost in dollars. Write both equations and find the point where their
graphs intersect. Explain what its coordinates mean.

<details><summary>Solution</summary>

**Solution:**

Plan A is $y=4x+10$ and Plan B is $y=2x+22$. Setting the costs equal gives
$4x+10=2x+22$, so $2x=12$ and $x=6$. Then $y=4(6)+10=34$.

The intersection is $\boxed{(6,34)}$: after **6 rides**, each plan costs
**$\$34$**. The nonnegative whole number of rides makes the result meaningful.

$\square$

</details>
