# Lesson 9: Parallel Lines, Perpendicular Lines, and Distance to a Line
*Fundamental Math / Algebra I*

Lesson 8 built a line's equation from its slope. This lesson goes the other direction: given
a line's equation, what does its slope tell you about how it sits relative to *other* lines
and points? Two slope rules let you construct a parallel or perpendicular line through a
given point, and a distance formula measures how far a point sits from a line without ever
graphing it.

## 1. Parallel Lines: Same Slope

Two distinct lines are **parallel** exactly when they have the same slope: $m_1 = m_2$.
This matches the geometric intuition from Lesson 5 — same slope, different intercept means
the lines never cross. To find the equation of the line through a point $(x_1, y_1)$ that
is parallel to a given line:

1. Find the given line's slope $m$ (rewrite in slope-intercept form if needed).
2. Use that same $m$ in point-slope form with the given point: $y - y_1 = m(x - x_1)$.
3. Simplify to the requested form.

**Example.** Find the line through $(2, -1)$ parallel to $y = 4x + 3$.

The given line has slope $m = 4$. Using point-slope form: $y - (-1) = 4(x - 2) \implies
y + 1 = 4x - 8 \implies y = 4x - 9$.

## 2. Perpendicular Lines: Negative Reciprocal Slope

Two lines are **perpendicular** — they cross at a right angle — exactly when their slopes
are **negative reciprocals** of each other:

$$m_1 \cdot m_2 = -1 \qquad \text{equivalently} \qquad m_2 = -\frac{1}{m_1}.$$

"Negative reciprocal" means two things happen to the slope at once: flip the fraction, and
flip the sign. A slope of $\tfrac{2}{3}$ becomes $-\tfrac{3}{2}$; a slope of $-4$ (i.e.
$-\tfrac{4}{1}$) becomes $\tfrac{1}{4}$.

![Two side-by-side panels. Left, "Flip & Negate": a blue line with slope 2/3 and an orange line with slope −3/2 cross at a right angle, marked with a small square; dashed gray guides show the blue line's run of 3 and rise of 2, and the orange line's run of 2 and rise of −3, captioned "flip the fraction, then flip the sign". Right, "Horizontal ↔ Vertical": a blue horizontal line labeled "slope = 0" crosses an orange vertical line labeled "slope: undefined" at a right angle, captioned "recognize this pairing directly, don't force the formula".](./images/perpendicular-slopes.svg)

**Special case — horizontal and vertical lines.** A horizontal line has slope $0$, and $0$
has no reciprocal, so the negative-reciprocal *formula* breaks down exactly where Lesson 8
said slope-intercept form breaks down: a line perpendicular to a horizontal line is
**vertical** (no slope at all), and vice versa. This pairing — horizontal $\leftrightarrow$
vertical — has to be recognized directly; it isn't something $m_2 = -1/m_1$ can compute,
since $m_1 = 0$ would require dividing by $0$.

**To find the equation of a line through a point perpendicular to a given line:**

1. Find the given line's slope $m$.
2. Take the negative reciprocal, $-\tfrac{1}{m}$, as the new slope (or use the
   horizontal/vertical special case).
3. Plug the new slope and the given point into point-slope form.

**Example.** Find the line through $(4, 3)$ perpendicular to $y = \tfrac{2}{3}x - 1$.

The given slope is $\tfrac{2}{3}$, so the perpendicular slope is $-\tfrac{3}{2}$. Point-slope
form: $y - 3 = -\tfrac{3}{2}(x - 4) \implies y - 3 = -\tfrac{3}{2}x + 6 \implies
y = -\tfrac{3}{2}x + 9$.

## 3. Core Template: Distance From a Point to a Line

The (shortest) **distance from a point to a line** is measured along the perpendicular from
the point to the line — any other path is longer. Lesson 8's general form,
$Ax + By + C = 0$, is exactly the form this formula wants: for a point $(x_0, y_0)$ not on
the line,

$$
d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}
$$

![A diagonal blue line labeled "Ax + By + C = 0" runs across the graph. A point labeled (x0, y0) sits off the line, connected to a "foot on the line" point by a dashed orange segment labeled d that meets the line at a right angle, marked with a small square. Caption: d = |Ax0 + By0 + C| / √(A² + B²).](./images/distance-point-to-line.svg)

Because general form already has everything moved to one side, $C$ plugs in directly, sign
and all — there's no separate "subtract $C$" step to get backwards. If a line is given in
some other form, such as $y = mx + b$ or $Ax + By = k$, convert it to general form first
(Lesson 8, Section 5) and *then* read off $A$, $B$, $C$.

Plugging the point into the left-hand side works because a point that satisfies the
equation gives $0$ in the numerator (distance $0$, as expected), and the further a point
sits from the line, the larger that leftover value grows. Dividing by $\sqrt{A^2 + B^2}$
rescales it into an actual distance, and the absolute value keeps the answer non-negative
regardless of which side of the line the point sits on.

## 4. Reading Example: Distance via the Formula

Find the distance from $(1, 2)$ to the line $3x + 4y = 10$.

First convert to general form by moving everything to one side: $3x + 4y - 10 = 0$, so
$A = 3$, $B = 4$, $C = -10$. With $(x_0, y_0) = (1, 2)$:

$$
d = \frac{|3(1) + 4(2) + (-10)|}{\sqrt{3^2 + 4^2}} = \frac{|3 + 8 - 10|}{\sqrt{9 + 16}} =
\frac{1}{5}
$$

## 5. Reading Example: Distance via Perpendicular Line and Intersection

The formula in Section 3 is fast, but it's worth confirming it agrees with the geometric
definition — the length of the perpendicular segment from the point to the line. Redo
Section 4's problem that way.

**Step 1 — find the perpendicular line through $(1, 2)$.** Rewrite $3x + 4y = 10$ in
slope-intercept form: $y = -\tfrac{3}{4}x + \tfrac{5}{2}$, so $m = -\tfrac{3}{4}$. The
perpendicular slope is $\tfrac{4}{3}$. Point-slope form: $y - 2 = \tfrac{4}{3}(x - 1)
\implies y = \tfrac{4}{3}x + \tfrac{2}{3}$.

**Step 2 — find where the two lines intersect** (the foot of the perpendicular). Substitute:

$$
\begin{aligned}
-\tfrac{3}{4}x + \tfrac{5}{2} &= \tfrac{4}{3}x + \tfrac{2}{3} \\
-9x + 30 &= 16x + 8 \quad \text{(multiply by 12)} \\
22 &= 25x \\
x &= \tfrac{22}{25}
\end{aligned}
$$

Then $y = \tfrac{4}{3}\left(\tfrac{22}{25}\right) + \tfrac{2}{3} = \tfrac{88}{75} +
\tfrac{50}{75} = \tfrac{138}{75} = \tfrac{46}{25}$. The foot of the perpendicular is
$\left(\tfrac{22}{25}, \tfrac{46}{25}\right)$.

**Step 3 — distance between the two points**, using $(1, 2) = \left(\tfrac{25}{25},
\tfrac{50}{25}\right)$:

$$
d = \sqrt{\left(\tfrac{25}{25} - \tfrac{22}{25}\right)^2 +
\left(\tfrac{50}{25} - \tfrac{46}{25}\right)^2} =
\sqrt{\left(\tfrac{3}{25}\right)^2 + \left(\tfrac{4}{25}\right)^2} =
\sqrt{\tfrac{9 + 16}{625}} = \sqrt{\tfrac{25}{625}} = \tfrac{1}{5}
$$

**Non-obvious detail:** both methods agree ($d = \tfrac{1}{5}$), confirming the distance
formula *is* the perpendicular-and-intersection method, just algebraically shortcut. Use
the formula for speed; fall back to this longer method when a problem specifically asks you
to find the foot of the perpendicular, not just the distance.

## 6. Class Practice 1: Parallel and Perpendicular Lines Through a Point

### Problem

Given the line $2x - 5y = 10$ and the point $(3, 4)$, find (a) the equation of the line
through $(3, 4)$ parallel to the given line, and (b) the equation of the line through
$(3, 4)$ perpendicular to the given line. Give both in slope-intercept form.

<details>
<summary>Solution</summary>

Rewrite the given line in slope-intercept form: $2x - 5y = 10 \implies -5y = -2x + 10
\implies y = \tfrac{2}{5}x - 2$, so $m = \tfrac{2}{5}$.

**(a) Parallel:** same slope $\tfrac{2}{5}$. Point-slope: $y - 4 = \tfrac{2}{5}(x - 3)
\implies y = \tfrac{2}{5}x + \tfrac{14}{5}$.

**(b) Perpendicular:** negative reciprocal slope $-\tfrac{5}{2}$. Point-slope:
$y - 4 = -\tfrac{5}{2}(x - 3) \implies y = -\tfrac{5}{2}x + \tfrac{23}{2}$.

The answer is $y = \tfrac{2}{5}x + \tfrac{14}{5}$ (parallel) and
$y = -\tfrac{5}{2}x + \tfrac{23}{2}$ (perpendicular).

</details>

## 7. Class Practice 2: Distance From a Point to a Line

### Problem

Find the distance from the point $(-2, 3)$ to the line $6x - 8y = 5$.

### Answer Choices

(A) $\tfrac{5}{10}$
(B) $\tfrac{29}{10}$
(C) $\tfrac{35}{10}$
(D) $\tfrac{41}{10}$

<details>
<summary>Solution</summary>

Convert to general form: $6x - 8y - 5 = 0$, so $A = 6$, $B = -8$, $C = -5$. With
$(x_0, y_0) = (-2, 3)$:

$$
d = \frac{|6(-2) + (-8)(3) + (-5)|}{\sqrt{6^2 + (-8)^2}} =
\frac{|-12 - 24 - 5|}{\sqrt{36 + 64}} = \frac{41}{\sqrt{100}} = \frac{41}{10}
$$

The answer is **(D) $\tfrac{41}{10}$**.

</details>

## 8. Class Practice 3: Horizontal-Vertical Perpendicularity

### Problem

Find the equation of the line through $(5, -2)$ perpendicular to the horizontal line
$y = 7$.

<details>
<summary>Solution</summary>

$y = 7$ is horizontal (slope $0$). A line perpendicular to a horizontal line is vertical —
the negative-reciprocal formula doesn't apply here since $-\tfrac{1}{0}$ is undefined, but
the geometric fact still holds. A vertical line through $(5, -2)$ has equation

$$x = 5.$$

The answer is $x = 5$.

</details>

## 9. Common Mistakes

### 9.1 Forgetting to flip *and* negate for perpendicular slope

"Negative reciprocal" requires both steps. Flipping without negating (or negating without
flipping) gives a slope that produces neither a parallel nor a perpendicular line.

### 9.2 Using the wrong sign of $C$ in the distance formula

The distance formula assumes the line is already in general form, $Ax + By + C = 0$ — not
$Ax + By = k$. If a line is given in the second form, move $k$ to the left side first
($Ax + By - k = 0$, so $C = -k$) before reading off $C$, as in Sections 4 and 7. Skipping
that conversion and plugging $k$ in with the wrong sign is the single most common error with
this formula.

### 9.3 Applying the reciprocal-slope rule to horizontal or vertical lines

$m_2 = -1/m_1$ breaks down when $m_1 = 0$ (division by zero) and doesn't apply when $m_1$
is undefined (vertical) either. Recognize horizontal $\leftrightarrow$ vertical
perpendicularity directly instead of forcing it through the formula.

## 10. Key Takeaways

- Parallel lines share the same slope: $m_1 = m_2$.
- Perpendicular lines have negative-reciprocal slopes: $m_1 \cdot m_2 = -1$, except for the
  horizontal/vertical pairing, which the formula can't compute directly.
- Distance from $(x_0, y_0)$ to $Ax + By + C = 0$: $d = \dfrac{|Ax_0 + By_0 + C|}{\sqrt{A^2 +
  B^2}}$ — a shortcut for the perpendicular-segment length that the intersection method
  computes directly. Convert to this form first if the line is given any other way.
- Both the distance formula and the "build the perpendicular, find the intersection,
  measure the segment" method agree — use the formula for speed, the longer method when a
  problem needs the foot of the perpendicular itself.
