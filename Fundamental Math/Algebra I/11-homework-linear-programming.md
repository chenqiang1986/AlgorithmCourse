# Homework: Lesson 11 — Linear Programming
*Fundamental Math / Algebra I*

For each problem, write the constraints and objective, find the feasible-region vertices,
evaluate the objective at every feasible vertex, and state the result in context.

## Problem 1: Maximize Revenue

A bakery sells loaves of bread ($x$) for $\$6$ and cakes ($y$) for $\$10$. It can make at
most 30 items total and at most 18 cakes. What combination maximizes revenue?

<details>
<summary>Solution</summary>

$$x+y\le30,\qquad y\le18,\qquad x,y\ge0,\qquad R=6x+10y.$$

The vertices are $(0,0)$, $(30,0)$, $(12,18)$, and $(0,18)$. Their revenues are,
respectively, $\$0$, $\$180$, $\$252$, and $\$180$.

The maximum revenue is $\boxed{\$252}$ by making $\boxed{12}$ loaves and $\boxed{18}$
cakes.

</details>

## Problem 2: Maximize Profit With Two Resources

A workshop makes stools ($x$) and tables ($y$). Each stool requires 2 hours of cutting and
1 hour of finishing; each table requires 1 hour of cutting and 3 hours of finishing. The
workshop has at most 18 cutting hours and 18 finishing hours. Profit is $\$30$ per stool and
$\$50$ per table. Find the maximum profit.

<details>
<summary>Solution</summary>

$$2x+y\le18,\qquad x+3y\le18,\qquad x,y\ge0,\qquad P=30x+50y.$$

The boundary intersection solves $2x+y=18$ and $x+3y=18$, giving
$x=\tfrac{36}{5}$ and $y=\tfrac{18}{5}$. The vertices are $(0,0)$, $(9,0)$,
$\left(\tfrac{36}{5},\tfrac{18}{5}\right)$, and $(0,6)$.

Their profits are $\$0$, $\$270$, $\$396$, and $\$300$. The maximum profit is
$\boxed{\$396}$ by making $\boxed{\tfrac{36}{5}}$ stools and
$\boxed{\tfrac{18}{5}}$ tables. If whole items are required, test nearby whole-number
points separately.

</details>

## Problem 3: Minimize Cost

A student needs at least 24 minutes of practice and at least 12 review points. One
flashcard set ($x$) takes 3 minutes, earns 2 review points, and costs $\$1$. One practice
problem ($y$) takes 2 minutes, earns 1 review point, and costs $\$2$. What is the least
cost?

<details>
<summary>Solution</summary>

$$3x+2y\ge24,\qquad2x+y\ge12,\qquad x,y\ge0,\qquad C=x+2y.$$

The boundaries meet at $(0,12)$. The lower-edge vertices are therefore $(0,12)$ and
$(8,0)$: at $y=0$, the time constraint gives $3x\ge24$, so $x=8$. Their costs are
$\$24$ and $\$8$, respectively.

The least cost is $\boxed{\$8}$ at $\boxed{(8,0)}$: 8 flashcard sets and no practice
problems. Check: $3(8)+2(0)=24\ge24$ and $2(8)+0=16\ge12$.

</details>
