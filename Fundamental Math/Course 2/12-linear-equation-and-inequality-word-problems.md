# Lesson 12: Linear Equation and Inequality Word Problems
*Fundamental Math / Course 2*

[Lesson 11](./11-linear-equation-word-problems.md) focused on stories whose answer is one
exact value. This lesson adds **inequality word problems**, where a story gives a limit and
the answer is a range of possible values. We will also use a one-variable strategy for
heads-and-legs problems, including the classic chicken-and-bunny puzzle.

## 1. Decide: Exact Answer or Limit?

Before writing symbols, identify what the story is telling you.

| Story language | Mathematical relationship | Typical answer |
| --- | --- | --- |
| exactly, equals, altogether, is | equation: $=$ | one value or a few related values |
| at least, no fewer than, minimum | inequality: $\geq$ | a lower bound |
| at most, no more than, maximum | inequality: $\leq$ | an upper bound |
| more than | inequality: $>$ | values above a boundary |
| fewer than, less than | inequality: $<$ | values below a boundary |

The context matters. If $x$ counts people, tickets, or animals, then $x$ must be a
whole number and cannot be negative. If $x$ measures time or distance, decimals may
make sense.

## 2. A Five-Step Modeling Routine

1. **Name the unknown.** Define a variable, including its unit.
2. **Mark the relationship word.** Is the story stating an exact equality or a limit?
3. **Write the model.** Translate every amount before solving.
4. **Solve and apply context.** Keep only values that make sense in the story.
5. **Check the story.** Substitute an answer, and for an inequality also test a value
   just outside the boundary when useful.

## 3. Worked Example: An Exact Total

**Example (Concert tickets).** A school club pays a $\$18$ delivery fee and $\$7$ per
concert ticket. Its bill is $\$102$. How many tickets did it buy?

**Solution:**

Let $t$ be the number of tickets. The bill is exactly $\$102$, so use an equation:

$$18+7t=102.$$

Subtract $18$ and divide by $7$:

$$7t=84\quad\Longrightarrow\quad t=12.$$

Check: $18+7(12)=102$. The club bought **12 tickets**.

$\square$

## 4. Worked Example: A Spending Limit

**Example (Snack budget).** Priya has at most $\$26$ to spend on snack boxes that cost
$\$4$ each. What numbers of boxes can she buy?

**Solution:**

Let $b$ be the number of snack boxes. “At most” means no more than, so

$$4b\leq26.$$

Dividing by $4$ gives $b\leq6.5$. Since boxes are whole items, Priya can buy
**$0,1,2,3,4,5,$ or $6$ boxes**. In this context, the largest possible number is
**6 boxes**.

Check: six boxes cost $6(\$4)=\$24$, which is within the budget; seven boxes cost
$\$28$, which is too much.

$\square$

> **Context check:** Do not round $6.5$ up to $7$ here. Rounding up would break the
> “at most $\$26$” condition.

## 5. Worked Example: A Minimum With a Fixed Amount

**Example (Volunteer hours).** Omar has already completed $3$ volunteer hours and earns
$2$ more hours each week. He needs at least $15$ hours. How many more weeks must he work?

**Solution:**

Let $w$ be the number of additional weeks. “At least” means $\geq$, so

$$3+2w\geq15.$$

Subtract $3$ and divide by $2$:

$$2w\geq12\quad\Longrightarrow\quad w\geq6.$$

Omar must work **at least 6 more weeks**. Check: after six weeks, he has
$3+2(6)=15$ hours; after five weeks, he would have only $13$ hours.

$\square$

## 6. Heads-and-Legs Problems: Make One Animal the Variable

A heads-and-legs puzzle gives two facts: every animal has one head, and each type has a
different number of legs. It may look like it requires two variables, but the head count
lets us write one animal count in terms of the other.

For chickens and rabbits, if there are $H$ heads and $r$ rabbits, then:

- rabbits: $r$;
- chickens: $H-r$;
- total legs: $4r+2(H-r)$.

Set that total equal to the known number of legs. The result is a one-variable linear
equation.

**Example (Chickens and bunnies).** A farm pen contains $18$ chickens and bunnies in all.
There are $50$ legs in the pen. How many chickens and how many bunnies are there?

**Solution:**

Let $r$ be the number of bunnies. Since there are $18$ heads altogether, there are
$18-r$ chickens. Bunnies have $4$ legs and chickens have $2$ legs, so

$$4r+2(18-r)=50.$$

Distribute and solve:

$$4r+36-2r=50\quad\Longrightarrow\quad 2r=14\quad\Longrightarrow\quad r=7.$$

There are $18-7=11$ chickens. Check: $7+11=18$ heads and
$7(4)+11(2)=28+22=50$ legs. The pen has **7 bunnies and 11 chickens**.

$\square$

### A Quick Reasonableness Test

With $18$ animals, all chickens would have $18(2)=36$ legs. Each bunny in place of a
chicken adds $2$ legs. The pen has $50-36=14$ extra legs, so there must be
$14\div2=7$ bunnies. This is a useful check, but the equation method works for many
similar situations.

## 7. Worked Example: A Comparison That Is an Inequality

**Example (Two phone plans).** Plan A costs $\$12$ plus $\$3$ per gigabyte. Plan B costs
$\$30$ plus $\$1$ per gigabyte. For what amounts of data is Plan A no more expensive than
Plan B?

**Solution:**

Let $g$ be the number of gigabytes. “No more expensive than” means less than or equal
to, so

$$12+3g\leq30+g.$$

Subtract $g$ and then $12$:

$$2g\leq18\quad\Longrightarrow\quad g\leq9.$$

Plan A is no more expensive for **$g\leq9$ gigabytes**. Check the boundary:
at $9$ GB, both plans cost $\$39$. At $10$ GB, Plan A costs $\$42$ while Plan B costs
$\$40$, so Plan A is no longer cheaper.

$\square$

## 8. Class Practice

For each problem, define a variable, write an equation or inequality, solve it, and
explain why the answer fits the context. Open a solution after trying.

### Practice 1: Exact Amount

**Problem (Art supplies).** A class pays a $\$6$ shipping fee plus $\$5$ for each sketchbook.
The bill is $\$46$. How many sketchbooks did the class buy?

<details>
<summary>Solution</summary>

**Solution:**

Let $s$ be the number of sketchbooks. The equation is $6+5s=46$. Then $5s=40$,
so $s=8$. Check: $6+5(8)=46$. The class bought **8 sketchbooks**.

$\square$

</details>

### Practice 2: Maximum

**Problem (Bus seats).** A bus has $52$ seats. There are already $17$ students aboard.
How many more students can board?

<details>
<summary>Solution</summary>

**Solution:**

Let $s$ be the number of additional students. The total cannot exceed $52$, so
$17+s\leq52$. Thus $s\leq35$. At most **35 more students** can board.

$\square$

</details>

### Practice 3: Minimum

**Problem (Reading goal).** Elena has read $42$ pages and reads $9$ pages each day. She
wants to read at least $105$ pages. How many more days does she need to read?

<details>
<summary>Solution</summary>

**Solution:**

Let $d$ be the number of additional days. The inequality is $42+9d\geq105$.
Then $9d\geq63$, so $d\geq7$. Elena needs to read for **at least 7 more days**.

$\square$

</details>

### Practice 4: Heads and Legs

**Problem (Birds and dogs).** At an animal shelter, there are $23$ birds and dogs in all.
Together they have $62$ legs. Each bird has $2$ legs and each dog has $4$ legs. How many
of each animal are there?

<details>
<summary>Solution</summary>

**Solution:**

Let $d$ be the number of dogs. Then $23-d$ is the number of birds. The leg equation is
$4d+2(23-d)=62$. Simplifying gives $2d+46=62$, so $2d=16$ and $d=8$.
There are $23-8=15$ birds. Check: $8(4)+15(2)=62$.
The shelter has **8 dogs and 15 birds**.

$\square$

</details>

### Practice 5: A Harder Heads-and-Legs Question

**Problem (Robots and scooters).** A display has $31$ robots and scooters. Every robot has
$2$ wheels, and every scooter has $3$ wheels. There are $79$ wheels altogether. How many
robots and scooters are in the display?

<details>
<summary>Solution</summary>

**Solution:**

Let $s$ be the number of scooters. Then there are $31-s$ robots. The wheel equation is
$3s+2(31-s)=79$. Thus $3s+62-2s=79$, so $s=17$.
There are $31-17=14$ robots. Check: $17(3)+14(2)=51+28=79$.
The display has **17 scooters and 14 robots**.

$\square$

</details>

### Practice 6: Compare Costs

**Problem (Streaming plans).** Plan C costs $\$8$ plus $\$2$ per movie. Plan D costs
$\$20$ plus $\$1$ per movie. For how many movies is Plan C less expensive than Plan D?

<details>
<summary>Solution</summary>

**Solution:**

Let $m$ be the number of movies. “Less expensive” gives $8+2m<20+m$.
Subtract $m$ and $8$: $m<12$. For whole-number movie counts, Plan C is cheaper for
**$0$ through $11$ movies**. At $12$ movies, the plans cost the same, so it is not
included.

$\square$

</details>

## 9. Common Mistakes

- **Using $=$ for a limit.** “At most” and “at least” need inequality symbols.
- **Forgetting the starting amount.** A rule such as $3+2w\geq15$ includes both the
  $3$ hours already completed and the hours added later.
- **Rounding the wrong way.** For a maximum, round a non-whole boundary down; for a
  minimum, round it up when the quantity must be whole.
- **Counting each animal twice.** In a heads-and-legs problem, $H-r$ already represents
  all the non-rabbits, because the total head count is $H$.
- **Giving an impossible answer.** Animal and ticket counts must be nonnegative whole
  numbers; a negative or fractional result signals that the model or data should be checked.

## 10. Key Takeaways

- An equation models an exact relationship; an inequality models a limit or comparison.
- Translate the relationship word before doing algebra.
- Use the story's units and restrictions to interpret the algebraic solution.
- In heads-and-legs problems, use the total number of heads to express one animal count
  in terms of the other, then write one leg equation.
