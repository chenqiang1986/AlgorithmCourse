# Practice Set: Constant Acceleration Kinematics
*AP Physics / Motion*

This practice set covers **one-dimensional motion with constant (uniform) acceleration**.
For each problem, try to solve it yourself first, then expand the solution to check your
work.

## Formula Reference

Let $x_0$ and $v_0$ be the position and velocity at time $t = 0$, and $x$, $v$ be the
position and velocity at a later time $t$. For constant acceleration $a$:

$$
\begin{aligned}
v &= v_0 + at \\
x &= x_0 + v_0 t + \frac{1}{2}at^2 \\
v^2 &= v_0^2 + 2a(x - x_0) \\
x &= x_0 + \frac{v_0 + v}{2}t
\end{aligned}
$$

Sign convention: choose one direction as positive and stay consistent for the whole
problem. For free fall near Earth's surface, use $a = -9.8 \text{ m/s}^2$ if "up" is
positive (or $g = 9.8 \text{ m/s}^2$ downward if "down" is positive).

## Problem 1: Reading a Velocity-Time Graph

A cart moves along a straight track. Its velocity-time graph is a straight line that
starts at $v = 2 \text{ m/s}$ when $t = 0 \text{ s}$ and rises to $v = 10 \text{ m/s}$ at
$t = 4 \text{ s}$.

What is the cart's acceleration, and what does the *area* under this graph represent?

<details>
<summary>Solution</summary>

The acceleration is the slope of the $v$-$t$ graph:

$$
a = \frac{\Delta v}{\Delta t} = \frac{10 - 2}{4 - 0} = 2 \text{ m/s}^2
$$

The area under a $v$-$t$ graph represents the **displacement** over that time interval,
since $\Delta x = \int v \, dt$.

The answer is $a = 2 \text{ m/s}^2$; the area equals the cart's displacement.

</details>

## Problem 2: Basic Velocity Update

A car starts from rest and accelerates at $3 \text{ m/s}^2$. What is its velocity after
$5$ seconds?

<details>
<summary>Solution</summary>

Use $v = v_0 + at$ with $v_0 = 0$, $a = 3 \text{ m/s}^2$, $t = 5 \text{ s}$:

$$
v = 0 + (3)(5) = 15 \text{ m/s}
$$

The answer is $v = 15 \text{ m/s}$.

</details>

## Problem 3: Displacement from Rest

Using the same car from Problem 2 (starts from rest, $a = 3 \text{ m/s}^2$), how far does
it travel in the first $5$ seconds?

<details>
<summary>Solution</summary>

Use $x = x_0 + v_0 t + \frac{1}{2}at^2$ with $x_0 = 0$, $v_0 = 0$:

$$
x = 0 + 0 + \frac{1}{2}(3)(5)^2 = \frac{1}{2}(3)(25) = 37.5 \text{ m}
$$

The answer is $x = 37.5 \text{ m}$.

</details>

## Problem 4: Finding Acceleration from Velocity and Distance

A bicycle traveling at $4 \text{ m/s}$ speeds up uniformly and reaches $12 \text{ m/s}$
after covering $32$ meters. What was its acceleration?

<details>
<summary>Solution</summary>

Use $v^2 = v_0^2 + 2a(x - x_0)$ with $v_0 = 4$, $v = 12$, $\Delta x = 32$:

$$
12^2 = 4^2 + 2a(32) \\
144 = 16 + 64a \\
128 = 64a \\
a = 2 \text{ m/s}^2
$$

The answer is $a = 2 \text{ m/s}^2$.

</details>

## Problem 5: Braking Distance

A car traveling at $20 \text{ m/s}$ brakes with a constant deceleration of
$5 \text{ m/s}^2$. How far does it travel before coming to a stop?

<details>
<summary>Solution</summary>

Take the direction of travel as positive, so $a = -5 \text{ m/s}^2$. At the stop,
$v = 0$. Use $v^2 = v_0^2 + 2a(x - x_0)$:

$$
0 = 20^2 + 2(-5)\Delta x \\
0 = 400 - 10\Delta x \\
\Delta x = 40 \text{ m}
$$

The answer is $40 \text{ m}$.

</details>

## Problem 6: Time to Stop

Using the same car from Problem 5 (initial speed $20 \text{ m/s}$, deceleration
$5 \text{ m/s}^2$), how long does it take to stop?

<details>
<summary>Solution</summary>

Use $v = v_0 + at$ with $v = 0$, $v_0 = 20$, $a = -5$:

$$
0 = 20 + (-5)t \\
t = 4 \text{ s}
$$

The answer is $t = 4 \text{ s}$.

</details>

## Problem 7: Free Fall Drop

A ball is dropped (initial velocity $0$) from a height of $45$ meters. Using
$g = 9.8 \text{ m/s}^2$, how long does it take to hit the ground, and how fast is it
moving when it lands?

<details>
<summary>Solution</summary>

Take downward as positive, so $a = 9.8 \text{ m/s}^2$, $v_0 = 0$, $\Delta x = 45 \text{ m}$.

Time to fall, from $x = x_0 + v_0 t + \frac{1}{2}at^2$:

$$
45 = 0 + \frac{1}{2}(9.8)t^2 \\
t^2 = \frac{90}{9.8} \approx 9.18 \\
t \approx 3.03 \text{ s}
$$

Landing speed, from $v = v_0 + at$:

$$
v = 0 + (9.8)(3.03) \approx 29.7 \text{ m/s}
$$

(Check with $v^2 = v_0^2 + 2a\Delta x = 2(9.8)(45) = 882$, so
$v = \sqrt{882} \approx 29.7 \text{ m/s}$ — matches.)

The answer is $t \approx 3.03 \text{ s}$, $v \approx 29.7 \text{ m/s}$.

</details>

## Problem 8: Ball Thrown Upward

A ball is thrown straight up with an initial velocity of $19.6 \text{ m/s}$. Using
$g = 9.8 \text{ m/s}^2$, find (a) the maximum height it reaches and (b) the total time
until it returns to the launch height.

<details>
<summary>Solution</summary>

Take upward as positive, so $a = -9.8 \text{ m/s}^2$, $v_0 = 19.6 \text{ m/s}$.

**(a) Maximum height:** at the top, $v = 0$. Use $v^2 = v_0^2 + 2a\Delta x$:

$$
0 = 19.6^2 + 2(-9.8)\Delta x \\
0 = 384.16 - 19.6\Delta x \\
\Delta x = 19.6 \text{ m}
$$

**(b) Time to return to launch height:** by symmetry, the ball returns to its starting
height with the opposite velocity, $v = -19.6 \text{ m/s}$. Use $v = v_0 + at$:

$$
-19.6 = 19.6 + (-9.8)t \\
-39.2 = -9.8t \\
t = 4 \text{ s}
$$

The answer is: max height $= 19.6 \text{ m}$, total time $= 4 \text{ s}$.

</details>

## Problem 9: Reaction Time + Braking (Two-Stage Motion)

A driver traveling at $24 \text{ m/s}$ takes $0.75 \text{ s}$ to react before braking
(during reaction time, velocity stays constant). Once braking begins, the car
decelerates at $6 \text{ m/s}^2$ until it stops. Find the **total** stopping distance,
including the reaction-time distance.

<details>
<summary>Solution</summary>

**Stage 1 (reaction time):** constant velocity, no acceleration.

$$
x_1 = v_0 t = (24)(0.75) = 18 \text{ m}
$$

**Stage 2 (braking):** starts at $v_0 = 24 \text{ m/s}$, ends at $v = 0$,
$a = -6 \text{ m/s}^2$. Use $v^2 = v_0^2 + 2a\Delta x$:

$$
0 = 24^2 + 2(-6)x_2 \\
0 = 576 - 12x_2 \\
x_2 = 48 \text{ m}
$$

**Total distance:**

$$
x_{\text{total}} = x_1 + x_2 = 18 + 48 = 66 \text{ m}
$$

The answer is $66 \text{ m}$.

</details>

## Problem 10: Conceptual — Same Acceleration, Different Interpretation

Two objects, A and B, both have a constant acceleration of $-4 \text{ m/s}^2$. Object A
starts at $v_0 = 10 \text{ m/s}$ (moving forward) and object B starts at
$v_0 = -10 \text{ m/s}$ (moving backward). Without calculating any numbers, describe what
each object is doing (speeding up or slowing down) over the next few seconds, and explain
your reasoning.

<details>
<summary>Solution</summary>

An object **speeds up** when velocity and acceleration have the **same sign**, and
**slows down** when they have **opposite signs**, because acceleration always pushes
velocity toward its own sign.

- **Object A:** $v_0 = +10$, $a = -4$ — opposite signs, so A is **slowing down**. It will
  keep decelerating, momentarily stop, then start moving backward (speeding up in the
  negative direction).
- **Object B:** $v_0 = -10$, $a = -4$ — same sign, so B is **speeding up** in the negative
  direction (moving backward faster and faster).

The answer is: A is slowing down (and will eventually reverse direction); B is speeding
up in the negative direction. The key idea is comparing the *sign* of $v$ to the *sign*
of $a$, not their magnitudes.

</details>

## Answer Key

| # | Answer |
|---|--------|
| 1 | $a = 2 \text{ m/s}^2$; area under $v$-$t$ graph = displacement |
| 2 | $v = 15 \text{ m/s}$ |
| 3 | $x = 37.5 \text{ m}$ |
| 4 | $a = 2 \text{ m/s}^2$ |
| 5 | $40 \text{ m}$ |
| 6 | $t = 4 \text{ s}$ |
| 7 | $t \approx 3.03 \text{ s}$, $v \approx 29.7 \text{ m/s}$ |
| 8 | max height $= 19.6 \text{ m}$, total time $= 4 \text{ s}$ |
| 9 | $66 \text{ m}$ |
| 10 | A slows down then reverses; B speeds up backward |
