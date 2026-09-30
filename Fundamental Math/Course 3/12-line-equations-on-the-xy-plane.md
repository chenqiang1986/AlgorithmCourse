# Lesson 12: Line Equations on the $xy$-Plane
*Fundamental Math / Course 3*

An equation with both $x$ and $y$ describes a relationship between two quantities. On the
coordinate plane, the ordered pairs that make a linear equation true form a straight line.
This lesson connects the algebra students have been using to that picture: make a table,
plot its ordered pairs, read a line's rate of change, and write its equation.

## 1. Ordered Pairs and the Coordinate Plane

An **ordered pair** $(x,y)$ names one point on the coordinate plane. Move $x$ units
horizontally first, then $y$ units vertically. The order matters: $(2,-3)$ and $(-3,2)$ are
different points.

For an equation such as

$$y=2x-1,$$

an ordered pair is a **solution** exactly when its coordinates make the equation true.
For example, $(3,5)$ is a solution because $5=2(3)-1$. But $(3,4)$ is not a solution,
because $4\ne2(3)-1$.

Every solution is a point on the graph, and every point on the graph is a solution. A line
is therefore not just a drawing: it is the complete set of ordered-pair solutions to its
equation.

## 2. Make a Table, Then Graph the Points

When an equation is written with $y$ alone on one side, choose convenient $x$-values and
calculate the matching $y$-values.

**Example.** Graph $y=-x+3$.

| $x$ | $y=-x+3$ | point |
| --- | --- | --- |
| $-1$ | $-(-1)+3=4$ | $(-1,4)$ |
| $0$ | $-(0)+3=3$ | $(0,3)$ |
| $1$ | $-(1)+3=2$ | $(1,2)$ |
| $3$ | $-(3)+3=0$ | $(3,0)$ |

Plot the points and use a ruler to draw one straight line through them, with arrows at both
ends. Do not connect the points with a zigzag: the equation has infinitely many solutions,
including values between the entries in the table.

Two points determine one line, so two correctly plotted points are enough to draw it. A
third point is still valuable as a check for a table or plotting error.

## 3. Slope Is Rise Over Run

The **slope** tells how $y$ changes when $x$ changes:

$$m=\frac{\text{change in }y}{\text{change in }x}=\frac{y_2-y_1}{x_2-x_1}.$$

For the points $(0,3)$ and $(1,2)$ from the example,

$$m=\frac{2-3}{1-0}=-1.$$

Starting at any point on this line, a run of $1$ to the right makes a rise of $-1$: go
right $1$ and down $1$. A positive slope rises from left to right; a negative slope falls.
A horizontal line has slope $0$ and equation $y=k$. A vertical line has equation $x=k$ and
an undefined slope, because its run is $0$.

**Keep the subtraction order matched.** If the numerator uses $y_2-y_1$, the denominator
must use $x_2-x_1$. Reversing both differences is fine; reversing only one changes the
sign incorrectly.

## 4. Slope-Intercept Form: $y=mx+b$

Most nonvertical lines can be written in **slope-intercept form**:

$$y=mx+b.$$

- $m$ is the slope.
- $b$ is the **$y$-intercept**, the $y$-value when $x=0$. The line crosses the $y$-axis at
  $(0,b)$.

The **$x$-intercept** is where the line crosses the $x$-axis. Every point on the $x$-axis
has $y=0$, so find the $x$-intercept by setting $y=0$ and solving for $x$. For a line in
slope-intercept form, this looks like

$$0=mx+b.$$

**Example.** For $y=-2x+6$, the $y$-intercept is $(0,6)$. To find the $x$-intercept, set
$y=0$:

$$0=-2x+6\implies 2x=6\implies x=3.$$

So the $x$-intercept is $(3,0)$. Notice the coordinate patterns: a $y$-intercept always
has the form $(0,y)$, while an $x$-intercept always has the form $(x,0)$.

This gives a fast graphing method:

1. Plot the $y$-intercept $(0,b)$.
2. Use the slope as rise/run to find another point.
3. Draw the line through the points and check with one more point if possible.

**Example.** Graph $y=\frac{2}{3}x-2$.

The $y$-intercept is $(0,-2)$. The slope $\frac{2}{3}$ means rise $2$, run $3$: from
$(0,-2)$, move right $3$ and up $2$ to $(3,0)$. Moving left $3$ and down $2$ gives another
point, $(-3,-4)$. Draw the line through these points.

The fraction is a single slope. It does **not** mean “go up $2$, then right $3$ from the
origin” unless the origin happens to be on the line; always start the slope moves at a
point already on the line.

## 5. Point-Slope Form: A Line From Its Slope and One Point

Suppose a line has slope $m$ and passes through a known point $(x_0,y_0)$. Let $(x,y)$ be
any other point on that same line. The slope formula gives

$$m=\frac{y-y_0}{x-x_0}.$$

Multiplying both sides by $x-x_0$ gives the **point-slope form**:

$$y-y_0=m(x-x_0).$$

Adding $y_0$ to both sides gives an equivalent form that is especially convenient here:

$$\boxed{y=m(x-x_0)+y_0}. $$

This formula says: begin at the known point's height $y_0$, then add the slope times the
horizontal change $x-x_0$. It works for every nonvertical line.

**Example.** Find the equation of the line with slope $3$ through $(-2,1)$.

Substitute $m=3$, $x_0=-2$, and $y_0=1$:

$$y=3\bigl(x-(-2)\bigr)+1=3(x+2)+1=3x+7.$$

Check with the given point: when $x=-2$, $y=3(-2)+7=1$ ✓.

## 6. Writing an Equation From Two Points

If two points $(x_1,y_1)$ and $(x_2,y_2)$ are given, first use them to calculate the slope:

$$m=\frac{y_2-y_1}{x_2-x_1}.$$

Then use either of the given points as $(x_0,y_0)$ in point-slope form. Substituting the
slope and the first point directly produces the **two-point equation**:

$$\boxed{y=\frac{y_2-y_1}{x_2-x_1}(x-x_1)+y_1}. $$

Usually it is clearer to calculate the slope first and then write
$y=m(x-x_1)+y_1$, rather than memorizing the longer formula. Either given point may be
used, and both choices simplify to the same line equation.

For a nonvertical line:

1. Find the slope $m$ using two points on the line.
2. Substitute the slope and either point into $y=m(x-x_0)+y_0$.
3. Simplify to slope-intercept form $y=mx+b$, if that form is requested.
4. Check the equation with the other point.

**Example.** Write an equation for the line through $(-1,4)$ and $(3,-4)$.

First find the slope:

$$m=\frac{-4-4}{3-(-1)}=\frac{-8}{4}=-2.$$

Use $(3,-4)$ in point-slope form:

$$y=-2(x-3)+(-4)=-2(x-3)-4.$$

Simplify:

$$y=-2x+6-4=-2x+2.$$

So the equation is

$$\boxed{y=-2x+2}. $$

Check with $(-1,4)$: $-2(-1)+2=4$ ✓.

If both points have the same $x$-coordinate, the line is vertical. Do not force it into
$y=mx+b$; write $x=k$ instead. For example, the line through $(5,-2)$ and $(5,4)$ is
$x=5$.

## 7. From Standard Form to a Graph

Some line equations arrive in **standard form**, $Ax+By=C$. To graph one, either solve for
$y$ or find two easy points. Intercepts are especially handy:

- Set $x=0$ to get the $y$-intercept.
- Set $y=0$ to get the $x$-intercept.

**Example.** Graph $2x+3y=6$.

Set $x=0$: $3y=6$, so $y=2$ and one point is $(0,2)$.

Set $y=0$: $2x=6$, so $x=3$ and another point is $(3,0)$.

The line through $(0,2)$ and $(3,0)$ is the graph. Solving for $y$ confirms its equation
is $y=-\frac{2}{3}x+2$: the slope is $-\frac{2}{3}$ and the $y$-intercept is $2$.

## 8. A Line as a Constant Rate

In $y=mx+b$, $b$ is the starting amount (when $x=0$) and $m$ is the amount of change for
each increase of $1$ in $x$.

**Example.** A bike-rental shop charges a $6$ starting fee and $4$ dollars per hour. If
$x$ is hours and $y$ is total cost in dollars, then

$$y=4x+6.$$

After $3$ hours, $y=4(3)+6=18$, so the cost is $\$18. The point $(3,18)$ lies on the
graph; $(0,6)$ records the starting fee. Units matter: the slope is **dollars per hour**,
not merely the number $4$.

## 9. Class Practice

### Problem 1

Does $(4,7)$ lie on $y=2x-1$? Does $(4,8)$?

<details>
<summary>Solution</summary>

For $x=4$, the equation gives $y=2(4)-1=7$. Therefore $(4,7)$ lies on the line. Since
$8\ne7$, $(4,8)$ does not.

</details>

### Problem 2

Find the slope and equation of the line through $(0,-3)$ and $(4,5)$.

<details>
<summary>Solution</summary>

$$m=\frac{5-(-3)}{4-0}=\frac{8}{4}=2.$$

The point $(0,-3)$ is the $y$-intercept, so $b=-3$. The equation is

$$\boxed{y=2x-3}. $$

</details>

### Problem 3

Graph the line $x=-2$. Is it a function of $x$?

<details>
<summary>Solution</summary>

All points have $x=-2$, so graph a vertical line through $(-2,0)$. It is not a function of
$x$: one input, $x=-2$, corresponds to many outputs such as $-3$, $0$, and $5$. This is why
it cannot be written in the form $y=mx+b$.

</details>

### Problem 4: Checking a List of Points

Which points in the list $(0,1)$, $(2,5)$, $(-1,-1)$, $(3,8)$, and $(4,9)$ lie on the
line $y=2x+1$?

<details>
<summary>Solution</summary>

Substitute each point's $x$-coordinate into $y=2x+1$ and compare the result to its
$y$-coordinate:

| Point | Expected $y=2x+1$ | On the line? |
| --- | --- | --- |
| $(0,1)$ | $2(0)+1=1$ | Yes |
| $(2,5)$ | $2(2)+1=5$ | Yes |
| $(-1,-1)$ | $2(-1)+1=-1$ | Yes |
| $(3,8)$ | $2(3)+1=7$ | No; $8\ne7$ |
| $(4,9)$ | $2(4)+1=9$ | Yes |

The points on the line are **$(0,1)$, $(2,5)$, $(-1,-1)$, and $(4,9)$**.

</details>

### Problem 5: Finding a Missing Coordinate

Point $P=(\square,11)$ lies on the line $y=3x-1$. Find the missing $x$-coordinate.

<details>
<summary>Solution</summary>

Because $P$ lies on the line, its coordinates must satisfy the equation. Substitute the
known $y$-value, $11$:

$$11=3x-1\implies 12=3x\implies x=4.$$

Thus $P=\boxed{(4,11)}$. Check: $3(4)-1=11$ ✓.

</details>

### Problem 6: Finding the Other Missing Coordinate

Point $Q=(-6,\square)$ lies on the line $y=-\frac{1}{2}x+4$. Find the missing
$y$-coordinate.

<details>
<summary>Solution</summary>

This time $x$ is known, so substitute $-6$ for $x$:

$$y=-\frac12(-6)+4=3+4=7.$$

Thus $Q=\boxed{(-6,7)}$.

</details>

### Problem 7: Reading Slope and Both Intercepts

For the line $y=-\frac{3}{2}x+6$, find the slope, the $y$-intercept, and the
$x$-intercept.

<details>
<summary>Solution</summary>

The slope is the coefficient of $x$, so $m=-\frac32$. The $y$-intercept is $6$, which is
the point $(0,6)$.

For the $x$-intercept, set $y=0$:

$$0=-\frac32x+6\implies \frac32x=6\implies x=4.$$

So the $x$-intercept is $(4,0)$. The answers are

$$\boxed{m=-\frac32,\quad y\text{-intercept }(0,6),\quad x\text{-intercept }(4,0)}.$$

</details>

### Problem 8: Writing a Line From Its Slope and a Point

Write the equation in slope-intercept form of the line with slope $-4$ through $(2,7)$.

<details>
<summary>Solution</summary>

Start with $y=mx+b$. The slope tells us $m=-4$, so $y=-4x+b$. Substitute the point
$(2,7)$:

$$7=-4(2)+b\implies 7=-8+b\implies b=15.$$

Therefore the equation is $\boxed{y=-4x+15}$. Check: $-4(2)+15=7$ ✓.

</details>

### Problem 9: Writing a Line From Two Points

Write the equation in slope-intercept form of the line through $(-2,3)$ and $(4,0)$.

<details>
<summary>Solution</summary>

First find the slope:

$$m=\frac{0-3}{4-(-2)}=\frac{-3}{6}=-\frac12.$$

Use either point to find $b$. Using $(4,0)$:

$$0=-\frac12(4)+b=-2+b\implies b=2.$$

Therefore the equation is $\boxed{y=-\frac12x+2}$. Checking the other point gives
$-\frac12(-2)+2=3$ ✓.

</details>

### Problem 10: A Vertical-Line Exception

Find the equation of the line through $(3,-2)$ and $(3,6)$. Why is slope-intercept form
not available?

<details>
<summary>Solution</summary>

Both points have $x=3$, so every point on the line has $x=3$. Its equation is
$\boxed{x=3}$.

The slope calculation has a zero denominator:

$$m=\frac{6-(-2)}{3-3}=\frac80,$$

which is undefined. Therefore there is no slope $m$ to use in $y=mx+b$.

</details>

## 11. Common Mistakes

- Treating $(x,y)$ as interchangeable with $(y,x)$. Move horizontally for $x$, then
  vertically for $y$.
- Reading $y=-3x+5$ as slope $3$. The minus sign belongs to the slope: $m=-3$.
- Calling $b$ the point $b$. The intercept is the point $(0,b)$.
- Dividing only one term when solving standard form for $y$. Divide every term on that side.
- Using $y=mx+b$ for a vertical line. Its equation is $x=k$.

## 12. Key Takeaways

- A line graph is the set of all ordered-pair solutions to its equation.
- In $y=mx+b$, $m$ is rate of change and $(0,b)$ is the $y$-intercept.
- Plot an intercept and use rise/run to graph quickly; use two points to find slope.
- Vertical lines have equations $x=k$ and undefined slope.
