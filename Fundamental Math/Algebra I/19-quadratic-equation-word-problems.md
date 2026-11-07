# Lesson 19: Applications of Quadratic Equations — Word Problems
*Fundamental Math / Algebra I*

Quadratic equations are not only abstract expressions to factor or solve. They appear when
two quantities are multiplied together: length times width, one consecutive integer times
the next, or time times a changing rate. In this lesson, the key task is to turn a story into
an equation before choosing a method to solve it.

## Learning Targets

By the end of class, you should be able to:

- define a variable, including its unit, for a quadratic word problem;
- write a quadratic equation from an area, product, or motion relationship;
- solve the equation by factoring, square roots, completing the square, or the quadratic
  formula; and
- reject solutions that do not make sense in the original situation.

## A Modeling Routine

1. **Name one unknown.** For example, let $x$ be the width in meters or the first integer.
2. **Write every related quantity in terms of $x$.** If the length is $4$ more than the
   width, write $x+4$.
3. **Use the relationship in the story.** Area is length times width; a product is one
   factor times the other; height can be set equal to $0$ when an object reaches the ground.
4. **Put the equation in standard form:** $ax^2+bx+c=0$.
5. **Solve, interpret, and check.** A negative length, negative time, or non-whole number
   of objects may be mathematically valid but contextually impossible.

> **Translation warning:** A perimeter gives an addition relationship, while an area gives a
> multiplication relationship. The multiplication is what usually produces the $x^2$ term.

## 1. Rectangle Template: Area and Perimeter

For a rectangle with length $L$ and width $W$,

$$A=LW \qquad\text{and}\qquad P=2L+2W.$$

If its perimeter is known, first use $L+W=\dfrac P2$ to express one dimension in terms of
the other. Then substitute into the area formula.

### Example 1: Given Area and Perimeter

A rectangle has area $60\text{ m}^2$ and perimeter $34\text{ m}$. Find its dimensions.

**Model.** Let $x$ be the width in meters. Half the perimeter is $17$, so

$$L+x=17 \qquad\Longrightarrow\qquad L=17-x.$$

Use the area:

$$x(17-x)=60.$$

Move everything to one side and factor:

$$17x-x^2=60$$
$$x^2-17x+60=0$$
$$(x-5)(x-12)=0.$$

So $x=5$ or $x=12$. These are the two dimensions in either order. The rectangle measures
$\boxed{5\text{ m by }12\text{ m}}$.

**Check:** $5(12)=60$ and $2(5)+2(12)=34$.

### Example 2: One Dimension Is Longer

A rectangular patio has area $96\text{ ft}^2$. Its length is $4$ feet more than its width.
Find the dimensions.

**Model.** Let $x$ be the width in feet. Then the length is $x+4$, so

$$x(x+4)=96.$$

$$x^2+4x-96=0$$
$$(x+12)(x-8)=0.$$

The algebraic solutions are $x=-12$ and $x=8$. A width cannot be negative, so reject $-12$.
The dimensions are $\boxed{8\text{ ft by }12\text{ ft}}$.

## 2. Product Relationships

Words such as *product*, *consecutive*, and *one more than* often lead to a quadratic.
Always define which quantity $x$ represents before multiplying.

### Example 3: Consecutive Integers

The product of two consecutive positive integers is $156$. Find the integers.

**Model.** Let $x$ be the smaller integer. The next integer is $x+1$.

$$x(x+1)=156$$
$$x^2+x-156=0$$
$$(x+13)(x-12)=0.$$

Thus $x=-13$ or $x=12$. The integers must be positive, so use $x=12$.
The integers are $\boxed{12\text{ and }13}$.

**Check:** $12(13)=156$.

### Example 4: Triangle Area

A triangle has area $96\text{ cm}^2$. Its base is $4$ cm longer than its height. Find its
base and height.

**Model.** Let $x$ be the height in centimeters. Then the base is $x+4$. Use
$A=\dfrac12bh$:

$$\frac12x(x+4)=96.$$

Multiply both sides by $2$ before solving:

$$x^2+4x=192$$
$$x^2+4x-192=0$$
$$(x+16)(x-12)=0.$$

The positive solution is $x=12$. The triangle has height $\boxed{12\text{ cm}}$ and base
$\boxed{16\text{ cm}}$.

## 3. Price, Demand, and Revenue

Sometimes the number of buyers changes with the price. If $p$ is the price of one item and
the demand is $100-4p$, then total revenue is

$$R=(\text{price})(\text{number of buyers})=p(100-4p).$$

Because price is multiplied by demand, a revenue question creates a quadratic equation.

### Example 5: Two Prices Can Give the Same Revenue

A club sells event tickets for $p$ dollars each. It predicts that the number of buyers will
be $100-4p$. If total ticket sales are $\$576$, find the possible ticket prices and the
corresponding numbers of buyers.

**Model.** Revenue is price times buyers:

$$p(100-4p)=576.$$

Put the equation in standard form:

$$100p-4p^2=576$$
$$4p^2-100p+576=0.$$

Divide by $4$ and factor:

$$p^2-25p+144=0$$
$$(p-9)(p-16)=0.$$

So the possible prices are $p=9$ and $p=16$.

- At $p=9$, demand is $100-4(9)=64$ buyers.
- At $p=16$, demand is $100-4(16)=36$ buyers.

Therefore, the club can earn $\$576$ by charging
$\boxed{\$9\text{ to }64\text{ buyers}}$ or $\boxed{\$16\text{ to }36\text{ buyers}}$.

**Check:** $9(64)=576$ and $16(36)=576$. Unlike a negative length, neither result should be
discarded: both have a positive price and a nonnegative number of buyers.

## 4. Motion: When Does an Object Reach the Ground?

For vertical motion measured in feet, a common model is

$$h(t)=-16t^2+v_0t+h_0,$$

where $h(t)$ is height in feet, $t$ is time in seconds, $v_0$ is initial vertical velocity,
and $h_0$ is initial height. The object reaches the ground when its height is $0$.

### Example 6: A Thrown Ball

A ball's height is modeled by $h(t)=-16t^2+48t+64$. When does it hit the ground?

Set $h(t)$ equal to $0$:

$$-16t^2+48t+64=0.$$

Divide by $-16$:

$$t^2-3t-4=0$$
$$(t-4)(t+1)=0.$$

The solutions are $t=4$ and $t=-1$. Negative time is not part of this situation, so the ball
hits the ground after $\boxed{4\text{ seconds}}$.

## Choosing and Interpreting a Solution

The equation may have two roots, but the story determines which roots can be answers.

| Context | Usually reject |
| --- | --- |
| Length, width, area dimension | Negative values |
| Time after an event begins | Negative values |
| Number of people or objects | Negative or non-whole values |
| Rectangle dimensions from area and perimeter | Neither positive root; they are the two dimensions |

Do not discard a root just because it is inconvenient. State the contextual reason it cannot
represent the quantity you defined.

## Guided Practice

### Problem 1: Rectangle Dimensions

A garden has area $70\text{ m}^2$. Its length is $3$ meters more than its width. Find its
dimensions.

<details><summary>Solution</summary>

Let $x$ be the width. Then the length is $x+3$:

$$x(x+3)=70$$
$$x^2+3x-70=0$$
$$(x+10)(x-7)=0.$$

$x=7$ is the valid width, so the garden is $\boxed{7\text{ m by }10\text{ m}}$.

</details>

### Problem 2: Perimeter and Area

A rectangle has perimeter $30$ cm and area $56\text{ cm}^2$. Find its dimensions.

<details><summary>Solution</summary>

Let the width be $x$. Since $L+W=15$, the length is $15-x$.

$$x(15-x)=56$$
$$x^2-15x+56=0$$
$$(x-7)(x-8)=0.$$

The dimensions are $\boxed{7\text{ cm by }8\text{ cm}}$.

</details>

### Problem 3: Consecutive Integers

The product of two consecutive positive integers is $210$. Find the integers.

<details><summary>Solution</summary>

Let $x$ be the smaller integer:

$$x(x+1)=210$$
$$x^2+x-210=0$$
$$(x+15)(x-14)=0.$$

The positive solution gives $\boxed{14\text{ and }15}$.

</details>

### Problem 4: Price and Buyers

A snack stand charges $p$ dollars for a specialty item and expects $80-2p$ buyers. If total
sales revenue is $600$, find every possible price and the corresponding number of buyers.

<details><summary>Solution</summary>

$$p(80-2p)=600$$
$$2p^2-80p+600=0$$
$$p^2-40p+300=0$$
$$(p-10)(p-30)=0.$$

At $p=10$, there are $80-2(10)=60$ buyers. At $p=30$, there are
$80-2(30)=20$ buyers. The possible combinations are
$\boxed{\$10\text{ and }60\text{ buyers}}$ or
$\boxed{\$30\text{ and }20\text{ buyers}}$.

</details>

## Exit Ticket

1. A rectangular photo has area $120\text{ in}^2$. Its length is $7$ inches more than its
   width. Find its dimensions.
2. A toy rocket has height $h(t)=-16t^2+64t+80$. How long after launch does it hit the
   ground?
3. Explain why a rectangle problem can have two positive solutions for the variable but
   still describe just one rectangle.
4. A game charges $p$ dollars per entry and predicts $60-3p$ entries. Its revenue is
   $\$225$. Find the possible entry prices and the corresponding numbers of entries.

<details><summary>Answers</summary>

1. Let the width be $x$. Then $x(x+7)=120$, so
   $x^2+7x-120=0=(x+15)(x-8)$. The dimensions are
   $\boxed{8\text{ in by }15\text{ in}}$.
2. Set height equal to $0$: $-16t^2+64t+80=0$. Dividing by $-16$ gives
   $t^2-4t-5=0=(t-5)(t+1)$. The valid time is $\boxed{5\text{ seconds}}$.
3. If $x$ is called the width, the two positive roots give the same pair of dimensions in
   opposite order. For example, $5$ and $12$ describe one $5$-by-$12$ rectangle, not two
   different rectangles.
4. $p(60-3p)=225$ gives $p^2-20p+75=0=(p-5)(p-15)$. At $p=5$, there are
   $45$ entries; at $p=15$, there are $15$ entries. The possibilities are
   $\boxed{\$5\text{ with }45\text{ entries}}$ or
   $\boxed{\$15\text{ with }15\text{ entries}}$.

</details>
