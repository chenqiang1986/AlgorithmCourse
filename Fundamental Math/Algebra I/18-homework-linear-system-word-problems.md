# Homework: Lesson 18 — Linear-System Word Problems
*Fundamental Math / Algebra I*

**Name the unknowns first.** Before writing any equation, state exactly what each variable
counts or measures. **If you do not write a variable-definition statement, you receive no
credit.**

For Problems 1–5, **do not solve**. Define each variable clearly, then write a system of
linear equations that models the situation. For Problem 6, define variables, write a
system, solve it, and check your answer in the context.

## Part A: Define Variables and Model the Situation

### Problem 1: Smoothie Cart

A student-run smoothie cart sold $36$ smoothies. Fruit smoothies cost $6$ dollars and
protein smoothies cost $8$ dollars. The cart collected $252$ dollars. Define variables and
write a system that could determine how many of each type were sold.

<details><summary>Model</summary>

Let $f$ be the number of fruit smoothies and $p$ be the number of protein smoothies.

$$
\begin{cases}
f+p=36\\
6f+8p=252
\end{cases}
$$

</details>

### Problem 2: Data Plan

A phone plan has a fixed monthly fee plus the same cost for each gigabyte of data used.
Using $10$ gigabytes costs $35$ dollars, while using $25$ gigabytes costs $65$ dollars.
Define variables and write a system that could determine the fixed fee and the cost per
gigabyte.

<details><summary>Model</summary>

Let $f$ be the fixed monthly fee in dollars and $g$ be the cost per gigabyte in dollars.

$$
\begin{cases}
f+10g=35\\
f+25g=65
\end{cases}
$$

</details>

### Problem 3: Community Garden

A rectangular community garden has a perimeter of $76$ meters. Its length is $5$ meters
more than twice its width. Define variables and write a system that could determine its
length and width.

<details><summary>Model</summary>

Let $l$ be the length in meters and $w$ be the width in meters.

$$
\begin{cases}
2l+2w=76\\
l=2w+5
\end{cases}
$$

</details>

### Problem 4: Seedling Sale

A garden club sold $75$ trays of vegetable, herb, and flower seedlings. Vegetable trays
cost $4$ dollars, herb trays cost $2$ dollars, and flower trays cost $1$ dollar, for total
sales of $188$ dollars. The club sold $5$ more herb trays than vegetable trays. Define
variables and write a three-variable system.

<details><summary>Model</summary>

Let $v$, $h$, and $f$ be the numbers of vegetable, herb, and flower trays.

$$
\begin{cases}
v+h+f=75\\
4v+2h+f=188\\
h-v=5
\end{cases}
$$

</details>

### Problem 5: Supply Shipment

A relief center receives $44$ boxes of small, medium, and large supplies. The boxes weigh
$2$, $5$, and $8$ kilograms, respectively, and weigh $196$ kilograms altogether. There are
$4$ more medium boxes than small boxes. Define variables and write a three-variable system.

<details><summary>Model</summary>

Let $s$, $m$, and $l$ be the numbers of small, medium, and large boxes.

$$
\begin{cases}
s+m+l=44\\
2s+5m+8l=196\\
m-s=4
\end{cases}
$$

</details>

## Part B: Model and Solve

### Problem 6: Concession Stand

At a school game, the concession stand sold $40$ drinks: small, medium, and large. Small
drinks cost $3$ dollars, medium drinks cost $5$ dollars, and large drinks cost $7$ dollars.
The total drink revenue was $196$ dollars. The stand sold $6$ more medium drinks than small
drinks. How many drinks of each size were sold?

<details><summary>Solution</summary>

Let $s$, $m$, and $l$ be the numbers of small, medium, and large drinks.

$$
\begin{cases}
s+m+l=40 & \text{total drinks}\\
3s+5m+7l=196 & \text{total revenue}\\
m-s=6 & \text{comparison of medium and small drinks}
\end{cases}
$$

From the third equation, $m=s+6$. Substitute into the first equation:

$$
s+(s+6)+l=40\quad\Longrightarrow\quad l=34-2s.
$$

Now substitute both expressions into the revenue equation:

$$
3s+5(s+6)+7(34-2s)=196.
$$

$$
3s+5s+30+238-14s=196
$$
$$
-6s+268=196\quad\Longrightarrow\quad s=12.
$$

Then $m=12+6=18$ and $l=34-2(12)=10$. The stand sold
$\boxed{12\text{ small drinks},\ 18\text{ medium drinks},\text{ and }10\text{ large drinks}}$.

**Check:** $12+18+10=40$;
$3(12)+5(18)+7(10)=36+90+70=196$; and $18-12=6$.

</details>

## Before You Submit

- **Every variable has a stated meaning and unit when appropriate; without this statement,
  there is no credit.**
- Each "total" sentence is represented by an equation.
- A rate or price is multiplied by the number of items it describes.
- For Problem 6, the final answer includes labels and checks all three conditions.
