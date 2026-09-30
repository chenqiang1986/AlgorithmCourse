# Lesson 9: One-Variable Linear Inequalities
*Fundamental Math / Course 2*

[Lesson 8](./08-one-variable-linear-equations.md) asked for the one value of $x$ that makes an
equation true. An **inequality** asks for *all* values of $x$ that make a comparison true. In
this lesson, we solve and graph one-variable linear inequalities such as $3x-4\geq 11$.

## 1. What an Inequality Says

An inequality compares two quantities. Its symbol tells how they compare:

| Symbol | Read as | Does the endpoint count? |
| --- | --- | --- |
| $<$ | less than | No |
| $>$ | greater than | No |
| $\leq$ | less than or equal to | Yes |
| $\geq$ | greater than or equal to | Yes |

For example, $x+2>5$ means that $x+2$ is greater than $5$. It is true for $x=4$, since
$4+2>5$, but also for $x=10$, $x=3.1$, and many other values. Its solution is a set of
numbers, not usually just one number.

## 2. Graphing Solutions on a Number Line

We use a number line to show every solution.

- An **open circle** means the endpoint is *not* included. Use it with $<$ or $>$.
- A **closed (filled) circle** means the endpoint *is* included. Use it with $\leq$ or $\geq$.
- Shade or draw an arrow **left** for values less than the endpoint; shade **right** for values
  greater than the endpoint.

| Inequality | Number-line graph (text form) | Meaning |
| --- | --- | --- |
| $x>2$ | open circle at $2$, shade right | all numbers greater than $2$ |
| $x\geq2$ | closed circle at $2$, shade right | $2$ and all greater numbers |
| $x<-3$ | open circle at $-3$, shade left | all numbers less than $-3$ |
| $x\leq-3$ | closed circle at $-3$, shade left | $-3$ and all smaller numbers |

**Quick check:** On a number line, larger numbers are to the right. The word “greater” should
always make the graph point right, and “less” should make it point left.

## 3. Solving by Adding or Subtracting

Just as with equations, adding or subtracting the same number from both sides preserves the
comparison. The inequality sign stays in the same direction.

$$x+a>b \quad\Longrightarrow\quad x>b-a$$

### Reading Example

Solve and graph $x-7\leq 4$.

Add $7$ to both sides:

$$x-7+7\leq4+7$$
$$x\leq11$$

Graph a **closed** circle at $11$ and shade left. The circle is closed because $11$ itself makes
the original inequality true: $11-7=4$.

## 4. Class Practice 1

### Problem

Solve and graph: $x+6>-2$.

<details>
<summary>Solution</summary>

Subtract $6$ from both sides:

$$x+6-6>-2-6$$
$$x>-8$$

Graph an open circle at $-8$ and shade right.

</details>

## 5. Solving by Multiplying or Dividing: The Flip Rule

Multiplying or dividing by a **positive** number preserves the inequality direction, just as for
an equation. But multiplying or dividing by a **negative** number reverses the direction:

$$a<b \quad\Longrightarrow\quad -a>-b$$

For instance, $2<5$. Multiplying both sides by $-1$ gives $-2>-5$, which is true. On the number
line, negatives reverse the order: $-2$ lies to the right of $-5$.

Therefore:

$$-3x<12 \quad\Longrightarrow\quad x>-4$$

The sign changes from $<$ to $>$ because both sides were divided by $-3$.

> **The flip rule:** Flip $<$ to $>$, $>$ to $<$, $\leq$ to $\geq$, or $\geq$ to $\leq$ **only**
> when multiplying or dividing both sides by a negative number. Do not flip when adding or
> subtracting.

## 6. Reading Example: Negative Coefficient

Solve and graph $-4x\geq20$.

Divide both sides by $-4$. Since we divided by a negative, reverse $\geq$ to $\leq$:

$$\frac{-4x}{-4}\leq\frac{20}{-4}$$
$$x\leq-5$$

Graph a closed circle at $-5$ and shade left.

**Check:** Try $x=-6$, which is in the solution. Then $-4(-6)=24$, and $24\geq20$ is true.
Trying $x=0$, which is not in the solution, gives $0\geq20$, which is false.

## 7. Class Practice 2

### Problem

Solve and graph: $5x<-15$.

<details>
<summary>Solution</summary>

Divide both sides by positive $5$, so the sign does not change:

$$x<-3$$

Graph an open circle at $-3$ and shade left.

</details>

## 8. Two-Step Linear Inequalities

Solve a two-step inequality in the same reverse order as a two-step equation: undo
addition/subtraction first, then undo multiplication/division. Watch the coefficient's sign at
the division step.

$$ax+b\leq c \quad\Longrightarrow\quad ax\leq c-b \quad\Longrightarrow\quad x\leq\frac{c-b}{a}$$

The final inequality direction flips if $a$ is negative.

### Reading Example

Solve and graph $3x-5>10$.

Add $5$ to both sides:

$$3x-5+5>10+5 \quad\Longrightarrow\quad 3x>15$$

Divide by positive $3$:

$$x>5$$

Graph an open circle at $5$ and shade right.

## 9. Reading Example: Two Steps With a Negative Coefficient

Solve and graph $-2x+3\leq11$.

Subtract $3$ from both sides. Adding or subtracting does not flip the sign:

$$-2x+3-3\leq11-3 \quad\Longrightarrow\quad -2x\leq8$$

Now divide by $-2$, so flip the inequality:

$$x\geq-4$$

Graph a closed circle at $-4$ and shade right.

## 10. Inequalities With the Variable on Both Sides

Sometimes $x$ appears on both sides of an inequality, such as $5x-2>2x+7$. First use addition
or subtraction to put all the variable terms on one side. Then solve the resulting inequality
as usual. Adding or subtracting terms does **not** reverse the inequality sign.

### Reading Example

Solve and graph $5x-2>2x+7$.

Subtract $2x$ from both sides to collect the $x$-terms on the left:

$$5x-2x-2>2x-2x+7$$
$$3x-2>7$$

Add $2$ to both sides, then divide by positive $3$:

$$3x>9$$
$$x>3$$

Graph an open circle at $3$ and shade right.

### Reading Example: A Negative Coefficient After Collecting Terms

Solve and graph $x+4\leq3x-6$.

Subtract $3x$ from both sides:

$$x-3x+4\leq3x-3x-6$$
$$-2x+4\leq-6$$

Subtract $4$, then divide by $-2$. The division by a negative reverses the sign:

$$-2x\leq-10$$
$$x\geq5$$

Graph a closed circle at $5$ and shade right.

### When the Variable Terms Cancel

If the $x$-terms cancel, decide whether the remaining statement is always true or always false.

- If it is true, **all real numbers** are solutions. For example,
  $2x+1\leq2x+4$ becomes $1\leq4$, which is true for every $x$.
- If it is false, there is **no solution**. For example,
  $3x-2>3x+5$ becomes $-2>5$, which is never true.

## 11. Class Practice 3: Variable on Both Sides

### Problem

Solve and graph: $4x+3<2x+11$.

<details>
<summary>Solution</summary>

Subtract $2x$ from both sides to put the variable terms together:

$$4x-2x+3<2x-2x+11$$
$$2x+3<11$$

Subtract $3$, then divide by positive $2$:

$$2x<8$$
$$x<4$$

Graph an open circle at $4$ and shade left.

</details>

## 12. Class Practice 4

### Problem

Solve and graph: $6x+1\geq25$.

<details>
<summary>Solution</summary>

Subtract $1$ from both sides:

$$6x\geq24$$

Divide by positive $6$:

$$x\geq4$$

Graph a closed circle at $4$ and shade right.

</details>

## 13. Class Practice 5

### Problem

Solve and graph: $-3x-2>7$.

<details>
<summary>Solution</summary>

Add $2$ to both sides:

$$-3x>9$$

Divide by $-3$ and flip the inequality:

$$x<-3$$

Graph an open circle at $-3$ and shade left.

</details>

## 14. Word Problems: “At Least” and “At Most”

Words often tell you which inequality symbol to use:

| Phrase | Symbol | Example |
| --- | --- | --- |
| at least | $\geq$ | at least $10$: $x\geq10$ |
| no less than | $\geq$ | no less than $10$: $x\geq10$ |
| at most | $\leq$ | at most $10$: $x\leq10$ |
| no more than | $\leq$ | no more than $10$: $x\leq10$ |
| more than | $>$ | more than $10$: $x>10$ |
| fewer than | $<$ | fewer than $10$: $x<10$ |

### Class Practice 6: Budget Problem

A movie ticket costs $8 dollars. Maya has at most $40 dollars to spend on tickets. How many
tickets, $x$, can she buy?

<details>
<summary>Solution</summary>

“At most” means $\leq$:

$$8x\leq40$$
$$x\leq5$$

Maya can buy at most **5 tickets**. Since tickets are whole objects, the relevant whole-number
solutions are $0,1,2,3,4,5$.

</details>

## 15. Common Mistakes

### 15.1 Forgetting to flip after dividing by a negative

From $-2x<8$, the correct result is $x>-4$, not $x<-4$. Test a value such as $0$: it satisfies
$0<8$, so $0$ must be in the answer set; $0>-4$ confirms the correct direction.

### 15.2 Flipping after addition or subtraction

From $x-3\geq4$, add $3$ without flipping: $x\geq7$. The flip rule is for multiplication or
division by a negative number only.

### 15.3 Using the wrong endpoint circle

$x>5$ has an open circle, because $5$ is excluded. $x\geq5$ has a closed circle, because $5$
is included.

### 15.4 Shading the wrong direction

Numbers greater than an endpoint are to its right; numbers less than an endpoint are to its
left. Pick a test point if unsure.

### 15.5 Moving a variable term without changing its sign

In $5x-2>2x+7$, subtracting $2x$ from both sides produces $3x-2>7$. A useful shortcut is to
say that $2x$ “moves” across the sign and becomes $-2x$, but the real operation is subtracting
$2x$ from **both** sides. Write that operation when learning the method to avoid sign errors.

## 16. Key Takeaways

- An inequality's solution is usually a **set of numbers**.
- Use an **open circle** for $<$ or $>$ and a **closed circle** for $\leq$ or $\geq$.
- Add or subtract the same amount on both sides without changing the inequality direction.
- Multiply or divide by a negative number and **flip the inequality sign**.
- When $x$ appears on both sides, collect all variable terms on one side before finishing the
  solution.
- If the variable terms cancel, the answer can be all real numbers or no solution.
- Check a solution by substituting a value from the graphed region into the original inequality.

Next, practice these skills in [09-homework-one-variable-linear-inequalities.md](./09-homework-one-variable-linear-inequalities.md).
