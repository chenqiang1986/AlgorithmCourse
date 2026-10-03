# Homework: Lagrange Multipliers
*ML / M03 — Calculus*

Use the [Lagrange Multipliers lesson](./03-lagrange-multipliers.md) as a
reference. Show the Lagrange system, all candidate points, and a comparison of
objective values. Unless a problem says otherwise, find **absolute** extrema.

## 1. Read a contour map

Let $f(x,y)=x+2y$ and let the constraint be $g(x,y)=x^2+y^2=5$.

1. Compute $\nabla f$ and $\nabla g$.
2. At $P=(1,2)$, verify that the gradients are parallel.
3. Give a tangent vector to the circle at $P$, and verify that it is
   perpendicular to both gradients.
4. Write the Lagrangian $\mathcal L(x,y,\lambda)$ and its three critical-point
   equations.

## 2. Product on a circle

Find the absolute maximum and minimum of

$$
f(x,y)=xy
$$

subject to

$$
x^2+y^2=8.
$$

## 3. Nearest and farthest points

Find the point(s) on the line

$$
x+2y=6
$$

that are nearest to and farthest from the origin. Use

$$
f(x,y)=x^2+y^2
$$

as the objective. Is a farthest point attained? Explain.

## 4. An ellipse constraint

Find the absolute maximum and minimum of

$$
f(x,y)=x+y
$$

subject to

$$
\frac{x^2}{4}+y^2=1.
$$

## 5. Rectangular area with a fixed perimeter

A rectangle has side lengths $x>0$ and $y>0$, and its perimeter is $40$.
Use Lagrange multipliers to maximize its area $A(x,y)=xy$ subject to

$$
2x+2y=40.
$$

Interpret the result in words.

## 6. A nonlinear constraint

Find the absolute maximum and minimum of

$$
f(x,y)=x^2+2y
$$

subject to

$$
x^2+y^2=9.
$$

Be especially careful not to divide by a variable before considering whether
it can be zero.

## 7. Explain the method

In 4–6 sentences, explain why a constrained extremum on a smooth curve
$g(x,y)=c$ must satisfy

$$
\nabla f=\lambda\nabla g.
$$

Your explanation must mention contours or tangent directions, and it must
explain the role of the equation $g=c$.

## Challenge: two constraints in three dimensions

Find the maximum and minimum of

$$
f(x,y,z)=x+y+z
$$

subject to

$$
x^2+y^2+z^2=1,
\qquad x-y=0.
$$

Use

$$
\nabla f=\lambda\nabla\left(x^2+y^2+z^2\right)+\mu\nabla(x-y).
$$

State both extremal values and all points where they occur.
