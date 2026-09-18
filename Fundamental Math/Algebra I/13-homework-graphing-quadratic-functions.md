# Homework: Lesson 13 — Graphing Quadratic Functions
*Fundamental Math / Algebra I*

This homework covers [Lesson 13](./13-graphing-quadratic-functions.md): graphing from vertex and standard form, using symmetry, finding intercepts, and completing the square to reveal a vertex. For every graph, label the vertex, axis of symmetry, and intercepts when they exist. Keep fractions and radicals exact unless an approximation helps a sketch.

## Part A: Read Vertex Form

### Problem 1

For $f(x)=-2(x-3)^2+5$, state the vertex, axis of symmetry, opening direction, and the two points one unit to the left and right of the vertex. Sketch the graph.

<details>
<summary>Solution</summary>

The vertex is $(3,5)$ and the axis is $x=3$. Since $a=-2<0$, the parabola opens downward. One unit from the vertex, $(x-3)^2=1$, so $f(x)=-2(1)+5=3$. The symmetric points are $(2,3)$ and $(4,3)$.

</details>

### Problem 2

For $g(x)=\frac12(x+4)^2-3$, state the vertex, axis of symmetry, opening direction, and the points two units to the left and right of the vertex. Sketch the graph.

<details>
<summary>Solution</summary>

The vertex is $(-4,-3)$ and the axis is $x=-4$. Since $a=\frac12>0$, the parabola opens upward and is wider than $y=x^2$. At a horizontal distance of $2$, the vertical change is $\frac12(2^2)=2$, so the symmetric points are $(-6,-1)$ and $(-2,-1)$.

</details>

## Part B: Graph From Standard Form

### Problem 3

Graph $h(x)=x^2+2x-3$. Find its vertex form, vertex, axis of symmetry, opening direction, and all intercepts.

<details>
<summary>Solution</summary>

$$h(x)=x^2+2x+1-1-3=(x+1)^2-4.$$

The vertex is $(-1,-4)$, the axis is $x=-1$, and the graph opens upward. The $y$-intercept is $(0,-3)$. Since $(x+1)^2-4=0$ gives $x=-1\pm2$, the $x$-intercepts are $(-3,0)$ and $(1,0)$.

</details>

### Problem 4

Graph $j(x)=2x^2-12x+16$. Find its vertex form, vertex, axis of symmetry, opening direction, and all intercepts.

<details>
<summary>Solution</summary>

$$
\begin{aligned}
j(x)&=2(x^2-6x)+16\\
&=2\bigl[(x-3)^2-9\bigr]+16\\
&=2(x-3)^2-2.
\end{aligned}
$$

The vertex is $(3,-2)$, the axis is $x=3$, and the graph opens upward. The $y$-intercept is $(0,16)$. Solving $2(x-3)^2-2=0$ gives $(x-3)^2=1$, so the $x$-intercepts are $(2,0)$ and $(4,0)$.

</details>

### Problem 5

Graph $k(x)=-3x^2-6x+9$. Find its vertex form, vertex, axis of symmetry, opening direction, and all intercepts.

<details>
<summary>Solution</summary>

$$
\begin{aligned}
k(x)&=-3(x^2+2x)+9\\
&=-3\bigl[(x+1)^2-1\bigr]+9\\
&=-3(x+1)^2+12.
\end{aligned}
$$

The vertex is $(-1,12)$ and the axis is $x=-1$. The graph opens downward, and the $y$-intercept is $(0,9)$. Solving $-3(x+1)^2+12=0$ gives $x=-1\pm2$, so the $x$-intercepts are $(-3,0)$ and $(1,0)$.

</details>

## Part C: Complete the Square With Fractions

### Problem 6

Rewrite $m(x)=x^2+5x+1$ in vertex form. State the vertex, axis of symmetry, and exact $x$-intercepts.

<details>
<summary>Solution</summary>

$$
\begin{aligned}
m(x)&=x^2+5x+\frac{25}{4}-\frac{25}{4}+1\\
&=\left(x+\frac52\right)^2-\frac{21}{4}.
\end{aligned}
$$

The vertex is $\left(-\frac52,-\frac{21}{4}\right)$ and the axis is $x=-\frac52$. The roots are $x=-\frac52\pm\frac{\sqrt{21}}2=\frac{-5\pm\sqrt{21}}2$.

</details>

### Problem 7

Graph $n(x)=2x^2+2x-1$. Complete the square and state the vertex, axis of symmetry, opening direction, and exact $x$-intercepts.

<details>
<summary>Solution</summary>

$$
\begin{aligned}
n(x)&=2(x^2+x)-1\\
&=2\left[\left(x+\frac12\right)^2-\frac14\right]-1\\
&=2\left(x+\frac12\right)^2-\frac32.
\end{aligned}
$$

The vertex is $\left(-\frac12,-\frac32\right)$ and the axis is $x=-\frac12$. The graph opens upward. Solving gives $\left(x+\frac12\right)^2=\frac34$, so the $x$-intercepts are $\left(\frac{-1-\sqrt3}{2},0\right)$ and $\left(\frac{-1+\sqrt3}{2},0\right)$.

</details>

## Part D: Intercept Cases and Reasoning

### Problem 8

Graph the key features of $p(x)=x^2-4x+4$. Does the graph cross, touch, or miss the $x$-axis? Explain.

<details>
<summary>Solution</summary>

$$p(x)=x^2-4x+4=(x-2)^2.$$

The vertex is $(2,0)$ and the axis is $x=2$. It opens upward, and its $y$-intercept is $(0,4)$. Since the vertex lies on the $x$-axis, the graph **touches** the axis once at $(2,0)$; this is a repeated root.

</details>

### Problem 9

Graph the key features of $q(x)=x^2+2x+5$. Does the graph have real $x$-intercepts? Explain.

<details>
<summary>Solution</summary>

$$q(x)=x^2+2x+1-1+5=(x+1)^2+4.$$

The vertex is $(-1,4)$ and the axis is $x=-1$. It opens upward and has $y$-intercept $(0,5)$. Because its lowest point is above the $x$-axis, it has no real $x$-intercepts.

</details>

### Problem 10

A parabola has vertex $(2,4)$, opens downward, and has $x$-intercepts at $0$ and $4$. Write an equation in vertex form and in standard form.

<details>
<summary>Solution</summary>

Use $y=a(x-2)^2+4$. Since $(0,0)$ is on the parabola,

$$0=a(0-2)^2+4=4a+4,$$

so $a=-1$. The vertex form is $y=-(x-2)^2+4$, and expanding gives $\boxed{y=-x^2+4x}$.

</details>

## Part E: Mixed Review

### Problem 11

A student writes $3x^2+12x+1=3(x+2)^2+1$. Identify the error, correct the vertex form, and state the vertex.

<details>
<summary>Solution</summary>

The student added $4$ inside the parentheses but did not subtract the equivalent amount. Because the outside factor is $3$, the correction is $3\cdot4=12$:

$$
\begin{aligned}
3x^2+12x+1&=3(x^2+4x)+1\\
&=3\bigl[(x+2)^2-4\bigr]+1\\
&=3(x+2)^2-11.
\end{aligned}
$$

The correct vertex is $(-2,-11)$.

</details>

### Problem 12

Graph $r(x)=\frac12x^2-3x+\frac52$. Find vertex form, the vertex, axis of symmetry, opening direction, and all intercepts.

<details>
<summary>Solution</summary>

$$
\begin{aligned}
r(x)&=\frac12(x^2-6x)+\frac52\\
&=\frac12\bigl[(x-3)^2-9\bigr]+\frac52\\
&=\frac12(x-3)^2-2.
\end{aligned}
$$

The vertex is $(3,-2)$ and the axis is $x=3$. The graph opens upward and is wider than $y=x^2$. The $y$-intercept is $\left(0,\frac52\right)$. Solving $\frac12(x-3)^2-2=0$ gives $x=1$ or $x=5$, so the $x$-intercepts are $(1,0)$ and $(5,0)$.

</details>

## Before You Submit

- Did you label the vertex and axis of symmetry on every sketch?
- Did you find the $y$-intercept by substituting $x=0$?
- Did you solve $f(x)=0$ to find the $x$-intercepts?
- When $a\ne1$, did you factor $a$ from the first two terms before completing the square?
- Did you keep fractions and radicals exact?
