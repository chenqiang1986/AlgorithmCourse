# Lesson 17: Parallel Lines in Coordinate Geometry
*Fundamental Math / Course 3*

In Lesson 14, equal slopes helped us recognize two lines that never meet. This lesson
develops that observation into a reliable coordinate-geometry tool: we will identify
parallel lines and write an equation for the unique parallel line through a given point.

## Learning Targets

By the end of this lesson, you should be able to:

- decide whether two lines on the coordinate plane are parallel;
- recognize parallel vertical and horizontal lines;
- write an equation for a line parallel to a given line through a given point; and
- distinguish parallel lines from two equations that describe the same line.

## 1. What Does Parallel Mean?

**Parallel lines** are coplanar lines that do not intersect. They remain the same
distance apart everywhere. In coordinate geometry, their direction is described by
their slope.

For nonvertical lines, the rule is:

$$\boxed{\text{Distinct lines are parallel exactly when they have the same slope.}}$$

For example, $y=\frac23x+1$ and $y=\frac23x-4$ both rise $2$ units for every run of
$3$ units. Their slopes agree, so they point in the same direction. Their different
$y$-intercepts place them on different paths; therefore, they never meet.

It is important that the lines be **distinct**. The equations $y=2x+5$ and
$2x-y=-5$ have the same slope because the second equation rearranges to $y=2x+5$.
They are not parallel lines; they are the very same line, so they share infinitely many
points.

## 2. Compare Slopes Carefully

To determine whether two nonvertical lines are parallel:

1. Write each equation in slope-intercept form, $y=mx+b$, if needed.
2. Compare the slopes, not the intercepts.
3. If the slopes are equal, check whether the equations describe different lines.

**Example 1.** Are $3x+2y=8$ and $y=-\frac32x+7$ parallel?

**Solution:**

Rewrite the first equation:

$$3x+2y=8\quad\Longrightarrow\quad 2y=-3x+8\quad\Longrightarrow\quad
y=-\frac32x+4.$$

Both lines have slope $-\frac32$, but their $y$-intercepts are $4$ and $7$. They are
distinct lines with the same slope, so they are $\boxed{\text{parallel}}$.

$\square$

**Example 2.** Are $4x-6y=12$ and $2x-3y=6$ parallel?

**Solution:**

Dividing the first equation by $2$ gives

$$2x-3y=6,$$

which is exactly the second equation. They describe the same line, so the answer is
$\boxed{\text{no; the lines coincide}}$, not parallel.

$\square$

## 3. Horizontal and Vertical Lines

Horizontal lines have slope $0$ and equations of the form $y=k$. Two horizontal lines
with different $y$-values are parallel:

$$y=3\quad\text{and}\quad y=-2.$$

Vertical lines have undefined slope and equations of the form $x=k$. Two vertical lines
with different $x$-values are parallel:

$$x=5\quad\text{and}\quad x=-1.$$

Never use “both slopes are undefined” in a fraction calculation: vertical slope is not a
number. Instead, recognize the two equations as vertical. A vertical line and a
nonvertical line cannot be parallel, because they intersect once.

**Example 3.** Classify each pair.

$$\text{(a) }y=-6\text{ and }y=\frac12x-6\qquad
\text{(b) }x=4\text{ and }x=-3$$

**Solution:**

In (a), the first line is horizontal and the second is not, so they are not parallel.
In (b), both lines are vertical and have different $x$-values, so they are
$\boxed{\text{parallel}}$.

$\square$

## 4. Write a Parallel Line Through a Point

Through a point not on a given line, exactly one parallel line can be drawn. It must
have the same slope as the given line. Then use point-slope form to place that slope
through the required point:

$$y-y_0=m(x-x_0).$$

**Example 4.** Write an equation for the line through $(2,-5)$ parallel to
$y=3x+1$.

**Solution:**

The given line has slope $3$, so the new line also has slope $3$. Use $(2,-5)$:

$$y-(-5)=3(x-2).$$

Thus $y+5=3x-6$, and

$$\boxed{y=3x-11}.$$

The new line has slope $3$, like the original, and its $y$-intercept $-11$ differs from
$1$, so it is a distinct parallel line.

$\square$

**Example 5.** Write an equation for the line through $(-4,7)$ parallel to
$2x+5y=10$.

**Solution:**

First find the slope of the given line:

$$2x+5y=10\quad\Longrightarrow\quad y=-\frac25x+2.$$

The required line has slope $-\frac25$. Point-slope form gives

$$y-7=-\frac25\bigl(x-(-4)\bigr)=-\frac25(x+4).$$

One convenient answer is $\boxed{y-7=-\frac25(x+4)}$. In slope-intercept form, this is
$\boxed{y=-\frac25x+\frac{27}{5}}$.

$\square$

For a vertical given line, keep the line vertical. For instance, the line through
$(-2,6)$ parallel to $x=4$ is $\boxed{x=-2}$; point-slope form is not used.

## 5. A Fast Test in Standard Form

For lines in standard form,

$$A_1x+B_1y=C_1\qquad\text{and}\qquad A_2x+B_2y=C_2,$$

you may first solve each for $y$. When $B\ne0$, the slope of $Ax+By=C$ is

$$m=-\frac{A}{B}.$$

Thus equal slopes mean $-\frac{A_1}{B_1}=-\frac{A_2}{B_2}$. This is useful, but
rewriting in $y=mx+b$ form is often clearer while learning. Remember to check whether
one entire equation is a multiple of the other: if so, the lines coincide rather than
being distinct parallel lines.

**Example 6.** Decide whether $6x-9y=12$ and $2x-3y=-5$ are parallel.

**Solution:**

Both equations have slope

$$-\frac{6}{-9}=\frac23\qquad\text{and}\qquad -\frac{2}{-3}=\frac23.$$

Their constants are not in the same ratio as the coefficients: dividing the first
equation by $3$ gives $2x-3y=4$, not $2x-3y=-5$. The lines are distinct, so they are
$\boxed{\text{parallel}}$.

$\square$

## 6. Class Practice

Try each problem before opening its solution.

**Problem 1.** Are $y=\frac34x-2$ and $3x-4y=12$ parallel? Explain.

<details><summary>Solution</summary>

Rewrite the second equation:

$$3x-4y=12\quad\Longrightarrow\quad y=\frac34x-3.$$

Both slopes are $\frac34$, and the intercepts differ. The lines are
$\boxed{\text{parallel}}$.

</details>

**Problem 2.** Are $5x+2y=8$ and $10x+4y=16$ parallel, the same line, or intersecting?

<details><summary>Solution</summary>

Multiplying $5x+2y=8$ by $2$ gives $10x+4y=16$. The equations are equivalent, so they
are $\boxed{\text{the same line}}.

</details>

**Problem 3.** Write an equation for the line through $(3,4)$ parallel to
$y=-2x+9$.

<details><summary>Solution</summary>

Use slope $-2$ through $(3,4)$:

$$y-4=-2(x-3).$$

Simplifying gives $\boxed{y=-2x+10}$.

</details>

**Problem 4.** Write an equation for the line through $(6,-1)$ parallel to $x=-4$.

<details><summary>Solution</summary>

The given line is vertical. A parallel line through $(6,-1)$ is also vertical, so its
equation is $\boxed{x=6}$.

</details>

**Problem 5.** A line passes through $(-1,2)$ and $(3,10)$. Write an equation of the
line through $(5,0)$ parallel to it.

<details><summary>Solution</summary>

The given slope is

$$m=\frac{10-2}{3-(-1)}=\frac84=2.$$

Use slope $2$ and point $(5,0)$:

$$y-0=2(x-5),$$

so $\boxed{y=2x-10}$.

</details>

## Exit Ticket

1. Decide whether $4x+y=1$ and $y=-4x+6$ are parallel, the same line, or intersecting.
2. Write an equation for the line through $(-3,1)$ parallel to $3x-2y=8$.
3. What must be true of two distinct nonvertical parallel lines?

<details><summary>Answers</summary>

1. $4x+y=1$ becomes $y=-4x+1$. The slopes agree and the intercepts differ, so the
   lines are $\boxed{\text{parallel}}$.
2. $3x-2y=8$ becomes $y=\frac32x-4$. Thus
   $y-1=\frac32(x+3)$, or $\boxed{y=\frac32x+\frac{11}{2}}$.
3. They have $\boxed{\text{the same slope}}$ and different positions (so they do not
   share any point).

</details>
