# Homework: Lessons 8–9 — Line Equations and Their Geometric Relationships
*Fundamental Math / Algebra I*

Homework covering [08-linear-equation-forms.md](./08-linear-equation-forms.md) (slope,
intercepts, point-slope form, general form, and slope-intercept form's blind spot) and
[09-parallel-perpendicular-and-distance.md](./09-parallel-perpendicular-and-distance.md)
(parallel and perpendicular lines, distance from a point to a line).

## Part A: Slope, Intercepts, and Point-Slope Form

### Problem 1

Find the slope of the line through $(-3, 4)$ and $(5, -2)$.

<details>
<summary>Solution</summary>

$$m = \frac{-2 - 4}{5 - (-3)} = \frac{-6}{8} = -\frac{3}{4}$$

The answer is $-\dfrac{3}{4}$.

</details>

### Problem 2

For the line $y = -2x + 7$, find the $x$-intercept and the $y$-intercept.

<details>
<summary>Solution</summary>

$y$-intercept: read directly from the equation, $b = 7$, giving $(0, 7)$.

$x$-intercept: set $y = 0$: $0 = -2x + 7 \implies x = \tfrac{7}{2}$, giving
$\left(\tfrac{7}{2}, 0\right)$.

The answer is $x$-intercept $\left(\tfrac{7}{2}, 0\right)$, $y$-intercept $(0, 7)$.

</details>

### Problem 3

Find the equation, in slope-intercept form, of the line through $(2, -5)$ and $(-4, 7)$.

<details>
<summary>Solution</summary>

Slope: $m = \dfrac{7 - (-5)}{-4 - 2} = \dfrac{12}{-6} = -2$.

Point-slope form using $(2, -5)$: $y - (-5) = -2(x - 2) \implies y + 5 = -2x + 4 \implies
y = -2x - 1$.

The answer is $y = -2x - 1$.

</details>

### Problem 4

Find the equation of the line through $(1, 1)$ and $(6, 1)$. Give it in the simplest form
you can.

<details>
<summary>Solution</summary>

Both points share $y = 1$, so the line is horizontal with slope $0$. Its equation is simply

$$y = 1.$$

The answer is $y = 1$.

</details>

### Problem 5

Given the line $5x + 2y = 20$, find its slope, $x$-intercept, and $y$-intercept.

<details>
<summary>Solution</summary>

Solve for $y$: $2y = -5x + 20 \implies y = -\tfrac{5}{2}x + 10$, so $m = -\tfrac{5}{2}$.

$x$-intercept ($y = 0$): $5x = 20 \implies x = 4$, giving $(4, 0)$.

$y$-intercept ($x = 0$): $2y = 20 \implies y = 10$, giving $(0, 10)$.

The answer is $m = -\tfrac{5}{2}$, $x$-intercept $(4, 0)$, $y$-intercept $(0, 10)$.

</details>

### Problem 6

A line passes through $(-6, 2)$ and $(-6, -9)$. Explain why it has no slope-intercept form,
and write its equation in general form instead.

<details>
<summary>Solution</summary>

Both points share $x = -6$, so the slope would be $m = \dfrac{-9 - 2}{-6 - (-6)} =
\dfrac{-11}{0}$, undefined. The line is vertical, and slope-intercept form $y = mx + b$
requires a finite slope, so no such $m$ exists. Its equation is

$$x + 6 = 0,$$

general form with $A = 1$, $B = 0$, $C = 6$.

</details>

## Part B: Parallel Lines, Perpendicular Lines, and Distance

### Problem 7

Find the equation, in slope-intercept form, of the line through $(4, -1)$ parallel to
$y = -3x + 2$.

<details>
<summary>Solution</summary>

The given line has slope $-3$; a parallel line has the same slope. Point-slope form:
$y - (-1) = -3(x - 4) \implies y + 1 = -3x + 12 \implies y = -3x + 11$.

The answer is $y = -3x + 11$.

</details>

### Problem 8

Find the equation, in slope-intercept form, of the line through $(-2, 6)$ perpendicular to
$y = \tfrac{1}{4}x - 5$.

<details>
<summary>Solution</summary>

The given slope is $\tfrac{1}{4}$; the perpendicular slope is the negative reciprocal,
$-4$. Point-slope form: $y - 6 = -4(x + 2) \implies y - 6 = -4x - 8 \implies y = -4x - 2$.

The answer is $y = -4x - 2$.

</details>

### Problem 9

Determine whether the lines $4x - 6y = 12$ and $6x - 9y = -18$ are parallel, perpendicular,
or neither.

<details>
<summary>Solution</summary>

First line: $4x - 6y = 12 \implies y = \tfrac{2}{3}x - 2$, slope $\tfrac{2}{3}$.

Second line: $6x - 9y = -18 \implies -9y = -6x - 18 \implies y = \tfrac{2}{3}x + 2$, slope
$\tfrac{2}{3}$.

Same slope, different $y$-intercepts ($-2$ vs. $2$), so the lines are distinct and parallel.

The answer is **parallel**.

</details>

### Problem 10

Find the equation of the line through $(3, -4)$ perpendicular to the vertical line $x = 3$.
(Careful — this point is *on* the given line.)

<details>
<summary>Solution</summary>

A line perpendicular to a vertical line is horizontal (slope $0$); the negative-reciprocal
formula doesn't apply since the vertical line's slope is undefined. A horizontal line
through $(3, -4)$ has equation

$$y = -4.$$

That the point also lies on $x = 3$ doesn't change anything — it's simply the intersection
point of the two perpendicular lines.

The answer is $y = -4$.

</details>

### Problem 11

Find the distance from the point $(2, -3)$ to the line $x + y = 10$.

<details>
<summary>Solution</summary>

Convert to general form: $x + y - 10 = 0$, so $A = 1$, $B = 1$, $C = -10$. With
$(x_0, y_0) = (2, -3)$:

$$
d = \frac{|1(2) + 1(-3) + (-10)|}{\sqrt{1^2 + 1^2}} = \frac{|2 - 3 - 10|}{\sqrt{2}} =
\frac{11}{\sqrt{2}} = \frac{11\sqrt{2}}{2}
$$

The answer is $\dfrac{11\sqrt{2}}{2}$.

</details>

### Problem 12

Find the distance from the origin $(0, 0)$ to the line $12x - 5y = 26$.

<details>
<summary>Solution</summary>

Convert to general form: $12x - 5y - 26 = 0$, so $A = 12$, $B = -5$, $C = -26$. With
$(x_0, y_0) = (0, 0)$:

$$
d = \frac{|12(0) + (-5)(0) + (-26)|}{\sqrt{12^2 + (-5)^2}} = \frac{26}{\sqrt{144 + 25}} =
\frac{26}{13} = 2
$$

The answer is $2$.

</details>

### Problem 13

Find the equation of the line through $(0, 0)$ perpendicular to the line through $(1, 2)$
and $(3, 6)$, in slope-intercept form. Then find the distance from the point $(3, 6)$ to
the line you just found, and confirm it's consistent with $(3,6)$ *not* lying on your new
line.

<details>
<summary>Solution</summary>

**Slope of the given line:** $m = \dfrac{6-2}{3-1} = \dfrac{4}{2} = 2$.

**Perpendicular slope:** $-\tfrac{1}{2}$. Through $(0,0)$: $y = -\tfrac{1}{2}x$, i.e.
$x + 2y = 0$.

**Distance from $(3, 6)$ to $x + 2y = 0$:** already in general form with $A=1, B=2, C=0$,

$$
d = \frac{|1(3) + 2(6) + 0|}{\sqrt{1^2+2^2}} = \frac{|3+12|}{\sqrt{5}} =
\frac{15}{\sqrt{5}} = 3\sqrt{5}
$$

Since $3\sqrt{5} \ne 0$, the distance confirms $(3, 6)$ does **not** lie on the
perpendicular line — consistent with it being a different point used only to define the
original line's slope.

The answer is $y = -\tfrac{1}{2}x$ (or $x + 2y = 0$), with distance $3\sqrt{5}$ from
$(3, 6)$.

</details>
