# Homework: Lesson 19 — Quadratic-Equation Word Problems
*Fundamental Math / Algebra I*

For every problem, define the variable with a unit when appropriate, write a quadratic
equation, solve it, and interpret every root in context. A negative length, time, or number
of buyers is not a valid final answer. Show a check using the original relationship.

## Part A: Geometry and Product Relationships

### Problem 1: Patio

**Problem (Patio).** A rectangular patio has area $144\text{ ft}^2$. Its length is $7$ feet
more than its width. Find its dimensions.

<details><summary>Solution</summary>

**Solution:** Let $x$ be the width in feet. The length is $x+7$, so

$$x(x+7)=144.$$

$$x^2+7x-144=0$$
$$(x+16)(x-9)=0.$$

The roots are $-16$ and $9$. Reject $-16$ because a length cannot be negative. The patio is
$\boxed{9\text{ ft by }16\text{ ft}}$. Check: $9(16)=144$.

$\square$

</details>

### Problem 2: Rectangle

**Problem (Rectangle).** A rectangle has perimeter $46$ cm and area $120\text{ cm}^2$.
Find its dimensions.

<details><summary>Solution</summary>

**Solution:** Let $x$ be one dimension in centimeters. Since half the perimeter is $23$,
the other dimension is $23-x$. Thus

$$x(23-x)=120.$$

$$x^2-23x+120=0$$
$$(x-8)(x-15)=0.$$

The dimensions are $\boxed{8\text{ cm by }15\text{ cm}}$. Check:
$2(8)+2(15)=46$ and $8(15)=120$.

$\square$

</details>

### Problem 3: Rectangle With a Doubled Side

**Problem (Rectangle With a Doubled Side).** A rectangle has area $98\text{ m}^2$. Its
length is twice its width. Find its dimensions.

<details><summary>Solution</summary>

**Solution:** Let $x$ be the width in meters. The length is $2x$, so

$$x(2x)=98$$
$$x^2=49.$$

Thus $x=\pm7$. Reject $-7$, so the rectangle is
$\boxed{7\text{ m by }14\text{ m}}$. Check: $7(14)=98$.

$\square$

</details>

### Problem 4: Triangle

**Problem (Triangle).** A triangle has area $150\text{ cm}^2$. Its base is $5$ cm longer
than its height. Find its base and height.

<details><summary>Solution</summary>

**Solution:** Let $x$ be the height in centimeters. The base is $x+5$. Using
$A=\frac12bh$ gives

$$\frac12x(x+5)=150.$$

$$x^2+5x-300=0$$
$$(x+20)(x-15)=0.$$

The valid height is $15$ cm, and the base is $20$ cm. Check:
$\frac12(20)(15)=150$. The answer is
$\boxed{15\text{ cm high with a }20\text{ cm base}}$.

$\square$

</details>

### Problem 5: Consecutive Integers

**Problem (Consecutive Integers).** The product of two consecutive positive integers is
$342$. Find the integers.

<details><summary>Solution</summary>

**Solution:** Let $x$ be the smaller integer; the next integer is $x+1$.

$$x(x+1)=342$$
$$x^2+x-342=0$$
$$(x+19)(x-18)=0.$$

The positive root is $18$, so the integers are $\boxed{18\text{ and }19}$. Check:
$18(19)=342$.

$\square$

</details>

### Problem 6: Consecutive Even Integers

**Problem (Consecutive Even Integers).** The product of two consecutive positive even
integers is $224$. Find the integers.

<details><summary>Solution</summary>

**Solution:** Let $x$ be the smaller even integer. The next even integer is $x+2$.

$$x(x+2)=224$$
$$x^2+2x-224=0$$
$$(x+16)(x-14)=0.$$

The valid value is $x=14$. The integers are $\boxed{14\text{ and }16}$. Check:
$14(16)=224$.

$\square$

</details>

## Part B: Price, Demand, and Revenue

### Problem 7: Concert Tickets

**Problem (Concert Tickets).** A venue charges $p$ dollars per ticket and predicts
$120-5p$ buyers. If revenue is $\$700$, find every possible ticket price and the matching
number of buyers.

<details><summary>Solution</summary>

**Solution:** Revenue is price times buyers:

$$p(120-5p)=700.$$

$$5p^2-120p+700=0$$
$$p^2-24p+140=0$$
$$(p-10)(p-14)=0.$$

At $p=10$, there are $120-5(10)=70$ buyers. At $p=14$, there are
$120-5(14)=50$ buyers. Both are valid:
$\boxed{\$10\text{ for }70\text{ buyers}}$ or
$\boxed{\$14\text{ for }50\text{ buyers}}$.

Check: $10(70)=700$ and $14(50)=700$.

$\square$

</details>

### Problem 8: Fundraiser Shirts

**Problem (Fundraiser Shirts).** A club charges $p$ dollars per shirt and expects
$150-6p$ buyers. If total shirt sales are $\$864$, find every possible price and the
corresponding number of buyers.

<details><summary>Solution</summary>

**Solution:**

$$p(150-6p)=864$$
$$6p^2-150p+864=0$$
$$p^2-25p+144=0$$
$$(p-9)(p-16)=0.$$

At $p=9$, demand is $96$ buyers; at $p=16$, demand is $54$ buyers. The possibilities are
$\boxed{\$9\text{ for }96\text{ buyers}}$ or
$\boxed{\$16\text{ for }54\text{ buyers}}$.

Check: $9(96)=864$ and $16(54)=864$.

$\square$

</details>

### Problem 9: Game Entries

**Problem (Game Entries).** A game charges $p$ dollars per entry and predicts $90-3p$
entries. Its revenue is $\$600$. Find every possible entry price and the corresponding
number of entries.

<details><summary>Solution</summary>

**Solution:**

$$p(90-3p)=600$$
$$3p^2-90p+600=0$$
$$p^2-30p+200=0$$
$$(p-10)(p-20)=0.$$

At $p=10$, there are $60$ entries. At $p=20$, there are $30$ entries. Thus the outcomes
are $\boxed{\$10\text{ for }60\text{ entries}}$ or
$\boxed{\$20\text{ for }30\text{ entries}}$.

Check: $10(60)=600$ and $20(30)=600$.

$\square$

</details>

## Part C: Vertical Motion

### Problem 10: Launched Ball

**Problem (Launched Ball).** The height of a ball in feet after $t$ seconds is
$h(t)=-16t^2+80t+96$. When does it hit the ground?

<details><summary>Solution</summary>

**Solution:** The ball reaches the ground when $h(t)=0$:

$$-16t^2+80t+96=0.$$

Divide by $-16$:

$$t^2-5t-6=0$$
$$(t-6)(t+1)=0.$$

The roots are $6$ and $-1$. Reject negative time. The ball hits the ground after
$\boxed{6\text{ seconds}}$.

$\square$

</details>

### Problem 11: Toy Rocket

**Problem (Toy Rocket).** The height of a toy rocket in feet after $t$ seconds is
$h(t)=-16t^2+32t+48$. When does it hit the ground?

<details><summary>Solution</summary>

**Solution:** Set height equal to $0$:

$$-16t^2+32t+48=0$$
$$t^2-2t-3=0$$
$$(t-3)(t+1)=0.$$

The valid root is $t=3$. The rocket hits the ground after $\boxed{3\text{ seconds}}$.

$\square$

</details>

### Problem 12: Height Check

**Problem (Height Check).** A model rocket has height
$h(t)=-16t^2+112t+128$ feet after $t$ seconds. When does it hit the ground?

<details><summary>Solution</summary>

**Solution:**

$$-16t^2+112t+128=0$$
$$t^2-7t-8=0$$
$$(t-8)(t+1)=0.$$

The roots are $8$ and $-1$. Only $8$ represents time after launch, so the rocket hits the
ground after $\boxed{8\text{ seconds}}$.

$\square$

</details>

## Before You Submit

- Every variable is defined before it is used.
- Your equation matches the relationship in the situation.
- Every answer has units.
- Every rejected root has a contextual reason.
- In price-demand problems, check whether **both** positive price-and-buyer pairs are valid.
