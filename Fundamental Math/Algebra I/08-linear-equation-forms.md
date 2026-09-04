# Lesson 8: Line Equations — Slope, Intercepts, and Point-Slope Form
*Fundamental Math / Algebra I*

Lessons 3–7 treated a linear equation as one half of a system to be solved. This lesson
turns to a single line on its own: how to describe it with a slope and two kinds of
intercept, how to build its equation from two points, and which of the three common forms
of a line equation can — and cannot — represent every line.

## 1. Slope: The Rate of Change

The **slope** of a line measures how steeply it rises or falls — the ratio of vertical
change to horizontal change between any two points on the line:

$$
m = \frac{\text{rise}}{\text{run}} = \frac{y_2 - y_1}{x_2 - x_1}
$$

Slope is the same number no matter which two points on the line you pick, because a line
is *straight* — its steepness never changes. A positive slope rises left to right, a
negative slope falls, a slope of $0$ is horizontal, and a **vertical** line has no
well-defined slope at all: the run $x_2 - x_1$ is $0$, and division by $0$ is undefined.
Keep that vertical-line case in mind — it resurfaces in Section 5.

**Example.** The slope between $(1, 2)$ and $(4, 11)$ is

$$m = \frac{11 - 2}{4 - 1} = \frac{9}{3} = 3.$$

![A steep red ray of slope 3 and a shallow blue ray of slope 1/4 both start from the same point. A dashed rise/run triangle sits close to the origin on the steep ray, and a second dashed rise/run triangle sits farther out along the gentle ray, showing that the steep line's rise is much bigger than the gentle line's for a similar run. Caption: bigger |m| makes a line climb faster for the same run.](./images/slope-steepness.svg)

![Three rays of the same steepness fan out from one point: a blue ray labeled "increasing (m > 0)" rises to the upper right, a green ray labeled "flat (m = 0)" runs horizontally, and an orange ray labeled "falling (m < 0)" mirrors the blue ray downward. Caption: reading left to right, a positive slope rises, zero stays level, a negative slope falls — only the sign of m changes the direction.](./images/slope-direction.svg)

## 2. Intercepts: Where a Line Crosses Each Axis

- The **$y$-intercept** is the point where the line crosses the $y$-axis — where $x = 0$.
- The **$x$-intercept** is the point where the line crosses the $x$-axis — where $y = 0$.

In **slope-intercept form**,

$$y = mx + b,$$

$m$ is the slope and $b$ is the $y$-value of the $y$-intercept directly — no computation
needed, since plugging in $x = 0$ gives $y = b$. The $x$-intercept still takes a step of
algebra: set $y = 0$ and solve for $x$:

$$0 = mx + b \implies x = -\frac{b}{m} \quad (m \ne 0).$$

**Example.** For $y = 3x - 6$: the $y$-intercept is $(0, -6)$ directly from $b = -6$. The
$x$-intercept solves $0 = 3x - 6 \implies x = 2$, giving $(2, 0)$.

## 3. Core Template: Point-Slope Form

**Point-slope form** builds a line's equation directly from its slope and *any one* point
$(x_1, y_1)$ on the line:

$$y - y_1 = m(x - x_1)$$

It comes straight from the slope definition: for any other point $(x, y)$ on the same
line, $m = \frac{y - y_1}{x - x_1}$, and multiplying both sides by $(x - x_1)$ gives the
formula above. Point-slope form is the workhorse for *writing* an equation — once you have
a slope and one point, you're done — and it converts to slope-intercept form by solving for
$y$, or to standard form by moving terms to one side.

**To find the equation of a line through two points $(x_1, y_1)$ and $(x_2, y_2)$:**

1. Compute the slope: $m = \dfrac{y_2 - y_1}{x_2 - x_1}$.
2. Plug $m$ and *either* point into point-slope form: $y - y_1 = m(x - x_1)$.
3. Simplify to whichever form the problem asks for (slope-intercept or standard).

![Two side-by-side panels. Left, "Point-Slope Form": a blue line passes through a filled point labeled (x1, y1) and an open point labeled (x, y) — any other point on the line. Dashed gray guides mark "run = x − x1" horizontally and "rise = y − y1" vertically between the two points, with the formula y − y1 = m(x − x1) below. Right, "Line Through Two Points": an orange line passes through two filled points labeled (x1, y1) and (x2, y2), both already known. Dashed gray guides mark "run = x2 − x1" and "rise = y2 − y1" between them, with the formula m = (y2 − y1) / (x2 − x1), then point-slope below.](./images/point-slope-and-two-points.svg)

## 4. Reading Example: Equation From Two Points

Find the equation of the line through $(1, 2)$ and $(4, 11)$, in slope-intercept form.

**Step 1 — slope:** $m = \dfrac{11 - 2}{4 - 1} = 3$ (computed in Section 1).

**Step 2 — point-slope form**, using $(1, 2)$:

$$y - 2 = 3(x - 1)$$

**Step 3 — simplify:**

$$
\begin{aligned}
y - 2 &= 3x - 3 \\
y &= 3x - 1
\end{aligned}
$$

**Check with the other point:** $y = 3(4) - 1 = 11$ ✓, matching $(4, 11)$.

**Non-obvious detail:** either point works in Step 2 — point-slope form doesn't care which
one you pick, since both points satisfy the final equation. Picking the point with smaller
or simpler numbers usually means less arithmetic.

## 5. General Form, and What Slope-Intercept Can't See

**General form** writes a line with everything moved to one side of the equation:

$$Ax + By + C = 0,$$

with $A$, $B$, $C$ typically integers and $A \ge 0$. Writing it this way — rather than
$Ax + By = C$ — keeps the constant's sign attached to it permanently, so there's no separate
"move it to the other side and flip the sign" step to forget. That matters once Lesson 9
reuses these same $A$, $B$, $C$ in its distance formula.

From this form: the slope is $m = -\dfrac{A}{B}$ (when $B \ne 0$), the $y$-intercept is
$\left(0, -\dfrac{C}{B}\right)$ (set $x = 0$ and solve $By + C = 0$), and the $x$-intercept
is $\left(-\dfrac{C}{A}, 0\right)$ (set $y = 0$ and solve $Ax + C = 0$) — the same
set-$x$-or-$y$-to-zero idea from Section 2, just applied before isolating $y$.

**Converting into general form:** move every term to the left side and set it equal to $0$.
From slope-intercept form: $y = mx + b \implies mx - y + b = 0$.

**The blind spot of slope-intercept form:** $y = mx + b$ requires a slope $m$, but Section 1
showed vertical lines have *no* slope. A vertical line like $x = 3$ cannot be written as
$y = mx + b$ for any $m$ — there is no way to isolate a single $y$ for a given $x$, because
every point on a vertical line shares the same $x$ for infinitely many $y$-values. General
form has no such blind spot: $x = 3$ is just $x - 3 = 0$, i.e. $Ax + By + C = 0$ with
$A = 1$, $B = 0$, $C = -3$. This is the one class of line that slope-intercept form is
structurally unable to describe, while general form handles it without any special case.

**Example.** The line through $(3, 1)$ and $(3, 5)$ has slope
$m = \frac{5-1}{3-3} = \frac{4}{0}$, undefined — confirming it's vertical. Its equation is
simply $x - 3 = 0$; asking for its "slope-intercept form" has no answer.

## 6. Class Practice 1: Equation From Two Points, in General Form

### Problem

Find the equation of the line through $(-2, 5)$ and $(2, -3)$, and write it in general form
$Ax + By + C = 0$ with $A > 0$.

<details>
<summary>Solution</summary>

Slope: $m = \dfrac{-3 - 5}{2 - (-2)} = \dfrac{-8}{4} = -2$.

Point-slope form using $(-2, 5)$: $y - 5 = -2(x + 2)$.

Simplify, moving everything to one side: $y - 5 = -2x - 4 \implies 2x + y - 1 = 0$.

The answer is $2x + y - 1 = 0$.

</details>

## 7. Class Practice 2: Reading Slope and Intercepts From General Form

### Problem

For the line $4x - 3y - 12 = 0$, find the slope, the $x$-intercept, and the $y$-intercept.

### Answer Choices

(A) $m = \tfrac{4}{3}$, $x$-intercept $(3, 0)$, $y$-intercept $(0, -4)$
(B) $m = \tfrac{4}{3}$, $x$-intercept $(0, -4)$, $y$-intercept $(3, 0)$
(C) $m = -\tfrac{4}{3}$, $x$-intercept $(3, 0)$, $y$-intercept $(0, -4)$
(D) $m = \tfrac{3}{4}$, $x$-intercept $(3, 0)$, $y$-intercept $(0, -4)$

<details>
<summary>Solution</summary>

Here $A = 4$, $B = -3$, $C = -12$. Slope: $m = -\dfrac{A}{B} = -\dfrac{4}{-3} =
\tfrac{4}{3}$.

$x$-intercept: $-\dfrac{C}{A} = -\dfrac{-12}{4} = 3$, giving $(3, 0)$.

$y$-intercept: $-\dfrac{C}{B} = -\dfrac{-12}{-3} = -4$, giving $(0, -4)$.

The answer is **(A)**.

</details>

## 8. Class Practice 3: Identifying the Blind Spot

### Problem

A line passes through $(5, -1)$ and $(5, 7)$. Explain why this line has no slope-intercept
form, and give its equation in general form instead.

<details>
<summary>Solution</summary>

Both points share $x = 5$, so the slope would be $m = \dfrac{7 - (-1)}{5 - 5} =
\dfrac{8}{0}$, which is undefined — the line is vertical. Slope-intercept form $y = mx + b$
requires a finite slope, so no value of $m$ and $b$ can represent this line. Every point on
it has $x = 5$ regardless of $y$, so its equation is simply

$$x - 5 = 0,$$

which is general form with $A = 1$, $B = 0$, $C = -5$.

</details>

## 9. Common Mistakes

### 9.1 Forgetting that only slope-intercept form has a "blind spot"

Vertical lines have no slope-intercept form, but they graph and have a general-form equation
just fine ($x - k = 0$). Don't conclude a vertical line "has no equation" — it has no
equation of *that particular form*.

### 9.2 Mixing up which axis each intercept sits on

The $x$-intercept is a point *on the $x$-axis*, found by setting $y = 0$ — not $x = 0$. It's
easy to swap these under time pressure; anchor it to "the intercept is named after the axis
it touches."

### 9.3 Picking the "wrong" point in point-slope form

Any point on the line works in point-slope form — there is no canonically "right" one. If
your simplified answer doesn't match a partner's who used the other point, that's a sign to
recheck arithmetic, not evidence that the point choice was wrong.

## 10. Key Takeaways

- Slope $m = \dfrac{y_2 - y_1}{x_2 - x_1}$ is constant along a line; vertical lines have no
  slope.
- $y$-intercept: set $x = 0$. $x$-intercept: set $y = 0$. In $y = mx + b$, the $y$-intercept
  is $b$ directly.
- Point-slope form $y - y_1 = m(x - x_1)$ builds an equation from a slope and any one point
  — the standard tool for finding an equation from two points.
- General form $Ax + By + C = 0$ can represent every line, including vertical ones, which is
  exactly the case slope-intercept form cannot express.

Next lesson: [09-parallel-perpendicular-and-distance.md](./09-parallel-perpendicular-and-distance.md)
uses slope to connect a line's equation to its geometry — how to recognize and construct
parallel and perpendicular lines, and how to measure the distance from a point to a line.
