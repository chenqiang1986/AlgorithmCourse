# Homework: Lesson 20 — Quadratic Extreme-Value Word Problems
*Fundamental Math / Algebra I*

For every problem, define the input variable and its unit when appropriate, write the
quadratic function being optimized, and find both coordinates of its vertex. State what
each coordinate means in the situation, including units. Unless a problem says otherwise,
use $x=-\dfrac{b}{2a}$ and then substitute back. Check that the input is in the stated or
implied domain.

## Part A: Finding and Interpreting Vertices

### Problem 1: Water Fountain

**Problem (Water Fountain).** The height of water from a fountain is modeled by
$h(t)=-16t^2+96t+8$, where $t$ is time in seconds and $h$ is height in feet. When does the
water reach its greatest height, and what is that height?

<details><summary>Solution</summary>

**Solution:** The leading coefficient is negative, so the vertex is a maximum.

$$t=\frac{-96}{2(-16)}=3.$$

$$h(3)=-16(3)^2+96(3)+8=152.$$

The water reaches a maximum height of $\boxed{152\text{ ft}}$ after
$\boxed{3\text{ seconds}}$.

$\square$

</details>

### Problem 2: Minimum Value

**Problem (Minimum Value).** Find the minimum value of $f(x)=3x^2-18x+41$ and the value
of $x$ where it occurs.

<details><summary>Solution</summary>

**Solution:** Since $a=3>0$, the parabola opens upward and its vertex is a minimum.

$$x=\frac{-(-18)}{2(3)}=3.$$

$$f(3)=3(3)^2-18(3)+41=14.$$

The minimum value is $\boxed{14}$, occurring at $\boxed{x=3}$.

$\square$

</details>

### Problem 3: Maximum Value in Vertex Form

**Problem (Maximum Value in Vertex Form).** Rewrite $g(x)=-2x^2+14x-5$ in vertex form.
Then state its maximum value and where it occurs.

<details><summary>Solution</summary>

**Solution:** Factor $-2$ from the quadratic and linear terms, then complete the square:

$$
\begin{aligned}
g(x)&=-2(x^2-7x)-5\\
&=-2\left[\left(x^2-7x+\frac{49}{4}\right)-\frac{49}{4}\right]-5\\
&=-2\left(x-\frac72\right)^2+\frac{39}{2}.
\end{aligned}
$$

Thus the vertex is $\left(\frac72,\frac{39}{2}\right)$. Because the coefficient of the
squared term is negative, the maximum value is $\boxed{\frac{39}{2}}$, occurring at
$\boxed{x=\frac72}$.

$\square$

</details>

## Part B: Price, Demand, and Revenue

### Problem 4: Museum Admission

**Problem (Museum Admission).** A museum estimates that it will sell $200-8p$ admissions
when the ticket price is $p$ dollars. What ticket price produces the greatest revenue? How
many admissions are sold, and what is the maximum revenue?

<details><summary>Solution</summary>

**Solution:** The demand is nonnegative when $0\le p\le25$. Revenue is

$$R(p)=p(200-8p)=-8p^2+200p.$$

The parabola opens downward. Its vertex occurs at

$$p=\frac{-200}{2(-8)}=12.5.$$

At that price, demand is $200-8(12.5)=100$ admissions, and

$$R(12.5)=12.5(100)=1250.$$

Charge $\boxed{\$12.50}$; the museum sells $\boxed{100\text{ admissions}}$ and earns a
maximum revenue of $\boxed{\$1{,}250}$.

$\square$

</details>

### Problem 5: Club T-Shirts

**Problem (Club T-Shirts).** A club expects to sell $180-5p$ T-shirts if it charges $p$
dollars per shirt. Find the price that maximizes revenue, the number of shirts sold, and
the maximum revenue.

<details><summary>Solution</summary>

**Solution:** The revenue function is

$$R(p)=p(180-5p)=-5p^2+180p.$$

Since $a=-5<0$, its vertex gives the maximum:

$$p=\frac{-180}{2(-5)}=18.$$

The demand is $180-5(18)=90$, and

$$R(18)=18(90)=1620.$$

The club should charge $\boxed{\$18}$, sell $\boxed{90\text{ shirts}}$, and earn
$\boxed{\$1{,}620}$ in maximum revenue.

$\square$

</details>

### Problem 6: Carnival Game

**Problem (Carnival Game).** A carnival predicts that $72-3p$ people will play a game when
the price is $p$ dollars per play. Find the price that produces the greatest revenue and
the greatest revenue.

<details><summary>Solution</summary>

**Solution:** Revenue is

$$R(p)=p(72-3p)=-3p^2+72p.$$

$$p=\frac{-72}{2(-3)}=12.$$

At $p=12$, the carnival has $72-3(12)=36$ players and earns

$$R(12)=12(36)=432.$$

The best price is $\boxed{\$12}$, producing a maximum revenue of $\boxed{\$432}$.

$\square$

</details>

## Part C: Area and Dimensions

### Problem 7: Rectangular Pen

**Problem (Rectangular Pen).** A rectangular pen uses $72$ meters of fencing on all four
sides. Find the dimensions that give the greatest possible area and the greatest area.

<details><summary>Solution</summary>

**Solution:** Let $x$ be the width in meters. Then the length is $36-x$, since half the
perimeter is $36$. The area is

$$A(x)=x(36-x)=-x^2+36x.$$

$$x=\frac{-36}{2(-1)}=18.$$

The length is also $36-18=18$, and

$$A(18)=18(18)=324.$$

The dimensions are $\boxed{18\text{ m by }18\text{ m}}$, and the maximum area is
$\boxed{324\text{ m}^2}$.

$\square$

</details>

### Problem 8: Garden Against a Wall

**Problem (Garden Against a Wall).** A gardener has $60$ meters of fencing to enclose
three sides of a rectangular garden; the fourth side lies along a wall. Find the dimensions
that maximize area and the maximum area.

<details><summary>Solution</summary>

**Solution:** Let $x$ be each side perpendicular to the wall. The side parallel to the
wall is $60-2x$. Thus

$$A(x)=x(60-2x)=-2x^2+60x.$$

$$x=\frac{-60}{2(-2)}=15.$$

The side along the wall is $60-2(15)=30$ meters, and

$$A(15)=15(30)=450.$$

The garden should be $\boxed{15\text{ m by }30\text{ m}}$, for a maximum area of
$\boxed{450\text{ m}^2}$.

$\square$

</details>

### Problem 9: Maximum Product

**Problem (Maximum Product).** Two nonnegative numbers have a sum of $50$. What two
numbers have the greatest product, and what is that product?

<details><summary>Solution</summary>

**Solution:** Let one number be $x$; the other is $50-x$. Their product is

$$P(x)=x(50-x)=-x^2+50x,$$

where $0\le x\le50$. The vertex is a maximum because the coefficient of $x^2$ is negative.

$$x=\frac{-50}{2(-1)}=25.$$

The other number is also $50-25=25$, and

$$P(25)=25(25)=625.$$

The numbers are $\boxed{25\text{ and }25}$, and their greatest product is $\boxed{625}$.

$\square$

</details>

## Part D: Minimums and Domain Checks

### Problem 10: Production Cost

**Problem (Production Cost).** The cost of producing $x$ batches is
$C(x)=\frac32x^2-30x+260$ dollars. How many batches minimize cost, and what is the
minimum cost?

<details><summary>Solution</summary>

**Solution:** Since $a=\frac32>0$, the vertex is a minimum.

$$x=\frac{-(-30)}{2\left(\frac32\right)}=10.$$

$$C(10)=\frac32(10)^2-30(10)+260=110.$$

Producing $\boxed{10\text{ batches}}$ gives a minimum cost of $\boxed{\$110}$.

$\square$

</details>

### Problem 11: Whole-Number Orders

**Problem (Whole-Number Orders).** A delivery company models its daily cost, in dollars,
by $C(x)=\frac12x^2-7x+80$, where $x$ is the whole number of delivery routes. How many
routes minimize the cost, and what is that cost?

<details><summary>Solution</summary>

**Solution:** The parabola opens upward, so its vertex gives the minimum.

$$x=\frac{-(-7)}{2\left(\frac12\right)}=7.$$

The vertex input is a permitted whole number. Therefore,

$$C(7)=\frac12(7)^2-7(7)+80=55.5.$$

The company should use $\boxed{7\text{ routes}}$, for a minimum cost of
$\boxed{\$55.50}$.

$\square$

</details>

### Problem 12: Restricted Domain

**Problem (Restricted Domain).** A vendor's profit is modeled by
$P(x)=-x^2+20x-30$, where $x$ is the number of items sold in hundreds. The vendor can sell
at most $8$ hundred items. What is the greatest possible profit on the domain
$0\le x\le8$?

<details><summary>Solution</summary>

**Solution:** The unrestricted vertex occurs at

$$x=\frac{-20}{2(-1)}=10.$$

Although the parabola opens downward, $x=10$ is outside the allowed domain. On the interval
$0\le x\le8$, the highest value occurs at the endpoint closest to the vertex, $x=8$.

$$P(8)=-(8)^2+20(8)-30=66.$$

The greatest possible profit is $\boxed{\$66}$ when the vendor sells
$\boxed{8\text{ hundred items}}$. The vertex cannot be used as the final answer because
the situation limits sales to $8$ hundred items.

$\square$

</details>

## Before You Submit

- Your optimization function names the quantity being maximized or minimized.
- You report both the vertex input and output, not just one of them.
- Your answer includes appropriate units and contextual meaning.
- You use the sign of the leading coefficient to identify a maximum or a minimum.
- You verify that the vertex input fits the practical domain; if it does not, compare valid
  boundary values.
