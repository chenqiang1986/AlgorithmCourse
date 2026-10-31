# Lesson 18: Applications of Linear Systems — Word Problems
*Fundamental Math / Algebra I*

Linear systems are useful when several facts describe the **same situation**. Each fact
becomes one equation; the common solution is the combination of quantities that makes all
the facts true at once. In this lesson, the difficult part is usually not elimination. It
is deciding what the variables mean and translating each sentence faithfully.

## Learning Targets

By the end of class, you should be able to:

- define variables with units for a word problem;
- translate a two- or three-category situation into a linear system;
- solve the system using a sensible method; and
- interpret and check an answer in the original context.

## Start Every System Here: Name the Unknowns

Before writing any equation, identify exactly what each variable represents. A correct
calculation cannot repair a model whose variables are unclear.

## A Modeling Routine

1. **Name the unknowns.** State what each variable counts or measures. Do this before
   writing any equation.
2. **Find the total.** Words such as *altogether*, *in all*, and *total* often create an
   addition equation.
3. **Match rates to quantities.** A price, weight, distance, or resource use is multiplied
   by the number of that item.
4. **Solve the system.** Use substitution or elimination.
5. **Return to the story.** Include units and check every condition. Counts should normally
   be whole, nonnegative numbers.

> **Translation warning:** In a price problem, $8s$ means "$8 for each student ticket, for
> $s$ student tickets." It does **not** mean that every ticket costs $8.

## Example 1: Two Ticket Types

The neighborhood theater sold $140$ tickets for a matinee. Adult tickets cost $12$ and
student tickets cost $7$. Total ticket revenue was $1{,}330$. How many tickets of each
type were sold?

**Model.** **Let $a$ be the number of adult tickets and $s$ be the number of student tickets.**

$$
\begin{cases}
a+s=140 & \text{total tickets}\\
12a+7s=1330 & \text{total revenue}
\end{cases}
$$

**Solve.** Multiply the first equation by $-7$ and add:

$$
-7a-7s=-980
$$
$$
12a+7s=1330
$$
$$
5a=350,\qquad a=70.
$$

Then $s=140-70=70$. The theater sold
$\boxed{70\text{ adult tickets and }70\text{ student tickets}}$.

**Check:** $70+70=140$, and $12(70)+7(70)=840+490=1330$.

## Example 2: Finding a Linear Pricing Rule

A bike-share service charges a one-time unlock fee plus the same charge per minute.
A $20$-minute ride costs $8$, and a $50$-minute ride costs $14$. Find the unlock fee and
the per-minute charge. Then find the cost of a $35$-minute ride.

**Model.** **Let $f$ be the unlock fee in dollars and $r$ be the charge in dollars per minute.**

$$
\begin{cases}
f+20r=8\\
f+50r=14
\end{cases}
$$

Subtract the first equation from the second:

$$
30r=6,\qquad r=0.20.
$$

Substitute into $f+20r=8$:

$$
f+20(0.20)=8\quad\Longrightarrow\quad f=4.
$$

The rule is $C=4+0.20m$, where $m$ is the number of minutes. For $35$ minutes,

$$
C=4+0.20(35)=\boxed{\$11}.
$$

The $4$ is a fixed cost; the $0.20$ is the cost for each additional minute.

## Example 3: Three Types of Shipping Crates

A food pantry receives $60$ crates: small, medium, and large. Their storage volumes are
$2$, $4$, and $6$ cubic feet, respectively, for a total of $238$ cubic feet. Their shipping
weights are $1$, $2$, and $4$ weight units, respectively, for a total of $136$ weight units.
How many crates of each size arrived?

**Model.** **Let $x$, $y$, and $z$ be the numbers of small, medium, and large crates.**

$$
\begin{cases}
x+y+z=60 & \text{crate count}\\
2x+4y+6z=238 & \text{storage volume}\\
x+2y+4z=136 & \text{shipping weight}
\end{cases}
$$

To keep the numbers smaller, divide the volume equation by $2$:

$$
x+2y+3z=119. \tag{2}
$$

Now eliminate $x$ using the count equation $(1)$:

$$
(2)-(1):\quad y+2z=59, \tag{4}
$$
$$
(3)-(1):\quad y+3z=76. \tag{5}
$$

Subtract (4) from (5): $z=17$. Then $y+2(17)=59$, so $y=25$.
Finally, $x+25+17=60$, so $x=18$.

The shipment contained $\boxed{18\text{ small},\ 25\text{ medium},\text{ and }17\text{ large crates}}$.

**Context check:** The volumes are $36+100+102=238$ cubic feet; the weights are
$18+50+68=136$ units.

## Example 4: Three Donation Options

At a school fundraiser, families chose a $5$ dollar donation, a $10$ dollar donation, or a
$20$ dollar donation. There were $80$ donations totaling $850$. The number of $10$ dollar
donations was $10$ more than the number of $20$ dollar donations. How many donations of
each amount were made?

**Model.** **Let $f$, $t$, and $w$ be the numbers of $5$, $10$, and $20$ donations.**

$$
\begin{cases}
f+t+w=80\\
5f+10t+20w=850\\
t-w=10
\end{cases}
$$

The third equation says $t=w+10$. Substitute this into the first equation:

$$
f+(w+10)+w=80\quad\Longrightarrow\quad f=70-2w.
$$

Use both expressions in the money equation:

$$
5(70-2w)+10(w+10)+20w=850.
$$

$$
450+20w=850\quad\Longrightarrow\quad w=20.
$$

So $t=30$ and $f=30$. The fundraiser received
$\boxed{30\text{ donations of }\$5,\ 30\text{ of }\$10,\text{ and }20\text{ of }\$20}$.

Notice that a statement comparing two categories, such as "10 more than," is also a
linear equation. It can provide the third condition needed for three unknowns.

## Guided Practice

### Problem 1: School Supplies

A classroom orders $32$ packs of pencils and markers. Pencil packs cost $3$ each and
marker packs cost $5$ each. The total cost is $124$. How many packs of each were ordered?

<details><summary>Solution</summary>

**Let $p$ be pencil packs and $m$ be marker packs.**

$$p+m=32,\qquad 3p+5m=124.$$

Subtract $3(p+m)=96$ from the cost equation: $2m=28$, so $m=14$ and $p=18$.
The order has $\boxed{18\text{ pencil packs and }14\text{ marker packs}}$.

</details>

### Problem 2: Recycling Drive

A recycling drive collected $90$ bags of paper, plastic, and aluminum. Each bag weighs
$4$, $3$, and $2$ kilograms, respectively. The total weight was $290$ kilograms. There
were twice as many paper bags as aluminum bags. Find the number of bags of each material.

<details><summary>Solution</summary>

**Let $p$, $l$, and $a$ be paper, plastic, and aluminum bags.**

$$
p+l+a=90,\qquad 4p+3l+2a=290,\qquad p=2a.
$$

Substitute $p=2a$ into the count equation: $l=90-3a$. Then

$$4(2a)+3(90-3a)+2a=290,$$

so $a=20$, $p=40$, and $l=30$. Thus the stated conditions describe
$\boxed{40\text{ paper},\ 30\text{ plastic},\text{ and }20\text{ aluminum bags}}$.

Check: $40+30+20=90$ and $4(40)+3(30)+2(20)=290$.

</details>

## Exit Ticket

1. A streaming service has a fixed monthly fee plus a per-movie rental fee. A customer who
   rents $3$ movies pays $15$; a customer who rents $7$ movies pays $23$. Find the fixed fee
   and the per-movie fee.
2. Explain why a three-variable system needs three independent pieces of information to
   determine one unique ordered triple.

<details><summary>Answers</summary>

1. **Let $f$ be the fixed fee and $r$ be the rental fee.** Then $f+3r=15$ and
   $f+7r=23$. Subtraction gives $4r=8$, so $r=2$ and $f=9$.
   The fees are $\boxed{\$9\text{ fixed and }\$2\text{ per movie}}$.
2. Each independent equation adds a constraint. With only two independent conditions,
   three unknowns generally still have more than one possible combination.

</details>
