# Lesson 5: Special Model — Stars and Bars
*AMC / Combinatorics*

Every technique so far — permutations, combinations, adjacency constraints — has counted arrangements of **distinct** items. This lesson introduces **stars and bars**, the standard tool for counting distributions of **identical** items, and shows that three questions that look completely different are secretly the same problem.

## 1. Three Questions, One Idea

Read these three problems. They sound unrelated, but by the end of this lesson you will see they all have the exact same answer.

**Question A (equation).** How many nonnegative integer solutions does
$$x_1 + x_2 + \cdots + x_k = n$$
have?

**Question B (balls into boxes).** In how many ways can you put $n$ identical balls into $k$ distinct boxes (a box may hold zero or more balls)?

**Question C (selection with repetition).** You have $n + 1$ distinct items. In how many ways can you take $k - 1$ of them, if you're allowed to take the same item more than once (order doesn't matter)?

## 2. The Stars and Bars Model

Start with Question B, since it's the easiest to picture. Line up the $n$ balls in a row as $n$ **stars**. To split them into $k$ groups (one group per box), insert $k - 1$ **bars** among the stars — the stars before the first bar go in box 1, the stars between the first and second bar go in box 2, and so on:

![7 stars split by 3 bars into 4 boxes: box 1 has 2 stars, box 2 has 3 stars, box 3 has 0 stars, box 4 has 2 stars](./images/stars-and-bars-example.svg)

(This example shows 7 stars split into 4 boxes: box 1 gets 2, box 2 gets 3, box 3 gets 0, box 4 gets 2.)

A distribution is completely determined by **where the bars go** among the $n + (k - 1)$ total symbols. Once the bar positions are fixed, everything else is a star.

**Question A is the same picture with different labels.** Let $x_i$ be the number of balls in box $i$. "Put $n$ balls into $k$ boxes" and "find nonnegative integers $x_1, \ldots, x_k$ summing to $n$" describe the exact same object — $(x_1, \ldots, x_k)$ *is* the distribution.

**Question C is the same picture, read as gaps instead of boxes.** Line the $n$ stars up in a row. They create $n + 1$ **gaps**: one before the first star, one between each pair of adjacent stars, and one after the last star — these are the "$n + 1$ distinct items" of Question C. Placing a bar in a gap is a "pick," and more than one bar is allowed to land in the same gap (that's what lets a box hold more than one ball). So choosing where to put the $k - 1$ bars is exactly "choose $k - 1$ of the $n + 1$ gaps, repetition allowed, order doesn't matter" — which is Question C, item for item. Splitting the stars with bars and picking $k - 1$ items from $n + 1$ with repetition are the same act, just described from two different angles: one names the bar positions, the other names the gaps they land in.

All three questions ask "where do the bars go among a row of stars" — they only differ in what the stars and boxes are called.

## 3. Core Formula

**Step 1: name the answer.** Section 2 showed Questions A, B, and C are the same picture wearing three different disguises, so they share one answer. Call it $f(n, k)$ — the answer to "$n$ identical items into $k$ distinct boxes," however the question happens to be phrased.

**Step 2: turn the picture into a string.** Take the row of $n$ stars and $k - 1$ bars from Section 2 and relabel every star as the letter A and every bar as the letter B. This is a string of length $n + k - 1$ made of $n$ A's and $k - 1$ B's — for example the picture in Section 2 becomes `AABAAABBAA`. Every distribution corresponds to exactly one such string, and every such string corresponds to exactly one distribution, so counting distributions is the same as counting these strings.

Counting the strings is now a permutation-with-repeated-items problem you already know how to solve: out of $n + k - 1$ total positions, choose which $k - 1$ of them hold a B (the rest are automatically A's). That's a direct combination count:

$$f(n, k) = C_{n+k-1}^{k-1} = C_{n+k-1}^{n}$$

**Step 3: name it, then derive it.** Define $H_n^k$ = the number of ways to choose $k$ items, repetition allowed (order doesn't matter), from $n$ distinct types — just a name for now, no formula yet.

Question C is exactly this with $n+1$ types and $k-1$ picks, i.e. $H_{n+1}^{k-1}$. But Question C is also just Question A/B relabeled (Section 2's gap argument), so it equals $f(n,k)$:

$$H_{n+1}^{\,k-1} = f(n,k) = C_{n+k-1}^{k-1}$$

Relabel $n+1 \to n$ and $k - 1\to k$ (i.e. substitute $n \to n - 1$, $k \to k+1$ on the right):

$$H_n^k = C_{n+k-1}^{k}$$

**All three original questions have the same answer**, $C_{n+k-1}^{k-1}$, and $H_n^k$ is just a name for this same count when a problem is phrased as "choose $k$ with repetition from $n$ types."

**Memory trick — rebuild it, don't memorize it.** Every stars-and-bars problem reduces to the same short process, so run it fresh each time instead of recalling a formula:

1. Name $n$ (the stars) and $k$ (the boxes/types).
2. Gaps $= n + 1$ — easy to picture: $n$ stars in a row always make one more gap than there are stars. Picks $= k - 1$ — that's how many bars you're placing into those gaps, and more than one bar can share a gap.
3. That's exactly $H_{n+1}^{\,k-1}$: choose $k-1$ with repetition from $n+1$ gaps.
4. Convert $H \to C$ with the one-step shortcut: **top index stays the same; bottom index becomes the two indices added together, minus 1.**

$$H_{n+1}^{\,k-1} = C_{\,(n+1)+(k-1)-1}^{\,k-1} = C_{\,n+k-1}^{\,k-1} \qquad (\text{top: } k-1 \to k-1, \quad \text{bottom: } (n+1) \to n+k-1)$$

General shortcut, same rule: $H_n^k = C_{\,n+k-1}^{\,k}$.

**Non-obvious detail:** stars and bars only applies when the $n$ items being distributed (the stars) are **identical** to each other. If the items are distinct (e.g., 5 different books into 3 distinct boxes), this is a different problem entirely, counted with the multiplication principle instead (each of the $n$ distinct items independently picks one of $k$ boxes: $k^n$).

## 4. Positive Integer Solutions (the Shift Trick)

A common variant of Question A requires every $x_i$ to be **positive** instead of nonnegative:

$$x_1 + x_2 + \cdots + x_k = n, \qquad x_i \ge 1 \text{ for every } i$$

Define $y_i = x_i - 1$. Since $x_i \ge 1$, each $y_i \ge 0$ — the positive-solutions problem in $x$ becomes a nonnegative-solutions problem in $y$. Substituting into the equation:

$$(y_1 + 1) + (y_2 + 1) + \cdots + (y_k + 1) = n \implies y_1 + y_2 + \cdots + y_k = n - k$$

This is now Question A's nonnegative case with total $n - k$ instead of $n$, so apply the Section 3 formula directly:

$$g(n, k) = f(n - k, \, k) = C_{(n-k)+k-1}^{k-1} = C_{n-1}^{k-1}$$

Equivalently, in balls-and-boxes language: give every box 1 ball up front (using $k$ of the $n$ balls to satisfy the minimum), then distribute the remaining $n - k$ balls with no restriction.

## 5. Reading Example: No Restriction

How many ways can 10 identical candies be distributed among 3 kids (a kid may get 0 candies)?

This is nonnegative integer solutions to $x_1 + x_2 + x_3 = 10$.

$$
\begin{aligned}
n &= 10 \text{ stars} \implies n+1 = 11 \text{ gaps} \\
k &= 3 \text{ boxes} \implies k-1 = 2 \text{ bars}
\end{aligned}
$$

$$H_{11}^{2} = C_{11+2-1}^{2} = C_{12}^{2} = 66$$

## 6. Reading Example: Everyone Gets At Least One

How many ways can 10 identical candies be distributed among 3 kids, if every kid must get at least 1 candy?

This is positive integer solutions to $x_1 + x_2 + x_3 = 10$ with $x_i \ge 1$ for each $i$. Substitute $y_i = x_i - 1$ so every $y_i \ge 0$ — this is the same as giving each kid 1 candy up front, then distributing what's left:

$$x_1+x_2+x_3=10,\ x_i\ge 1 \quad\xrightarrow{\ y_i=x_i-1\ }\quad y_1+y_2+y_3=10-3=7$$

$$
\begin{aligned}
n &= 7 \text{ stars} \implies n+1 = 8 \text{ gaps} \\
k &= 3 \text{ boxes} \implies k-1 = 2 \text{ bars}
\end{aligned}
$$

$$H_{8}^{2} = C_{8+2-1}^{2} = C_{9}^{2} = 36$$

(This matches the Section 4 shortcut $C_{n-1}^{k-1} = C_9^2 = 36$ — but the substitution above rebuilds the answer without needing to recall that formula.)

## 7. Reading Example: A Larger Minimum (General Shift)

How many ways can 15 identical candies be distributed among 4 kids, if every kid must get **at least 2** candies?

This is positive integer solutions with a minimum of 2: $x_1+\cdots+x_4=15$ with $x_i \ge 2$ for each $i$. Substitute $y_i = x_i - 2$ so every $y_i \ge 0$ — give each kid 2 candies up front, then distribute what's left:

$$x_1+\cdots+x_4=15,\ x_i\ge2 \quad\xrightarrow{\ y_i=x_i-2\ }\quad y_1+\cdots+y_4=15-2\times4=7$$

$$
\begin{aligned}
n &= 7 \text{ stars} \implies n+1 = 8 \text{ gaps} \\
k &= 4 \text{ boxes} \implies k-1 = 3 \text{ bars}
\end{aligned}
$$

$$H_{8}^{3} = C_{8+3-1}^{3} = C_{10}^{3} = 120$$

**Non-obvious detail:** for a minimum of $m$ per box, subtract $m \times k$ from $n$ first, then apply the no-restriction formula to the reduced total. This is the same $y_i = x_i - m$ idea as Section 4, just with $m$ instead of $1$.

## 8. Reading Example: An Upper Bound (Complement, Small Case)

How many ways can 8 identical candies be distributed among 3 kids, if no kid may get more than 5?

First count with no restriction.

$$
\begin{aligned}
n &= 8 \text{ stars} \implies n+1 = 9 \text{ gaps} \\
k &= 3 \text{ boxes} \implies k-1 = 2 \text{ bars}
\end{aligned}
$$

$$H_{9}^{2} = C_{9+2-1}^{2} = C_{10}^{2} = 45$$

Now subtract the invalid distributions where some kid gets 6 or more. If one particular kid gets at least 6, give that kid 6 candies first, leaving $n' = 8 - 6 = 2$ to distribute freely among the same 3 kids.

$$
\begin{aligned}
n' &= 2 \text{ stars} \implies n'+1 = 3 \text{ gaps} \\
k &= 3 \text{ boxes} \implies k-1 = 2 \text{ bars}
\end{aligned}
$$

$$H_{3}^{2} = C_{3+2-1}^{2} = C_{4}^{2} = 6 \text{ ways}$$

Since $8 < 6 + 6$, at most one kid can possibly exceed the limit, so there is no double-counted overlap to correct for. With 3 choices for *which* kid is the one exceeding the limit:

$$45 - 3 \times 6 = 45 - 18 = 27$$

**Non-obvious detail:** this "subtract the over-limit cases" approach is inclusion–exclusion (see [02-inclusion-exclusion-principle.md](./02-inclusion-exclusion-principle.md)) layered on top of stars and bars. It only stays this simple when the total $n$ is small enough that two kids cannot simultaneously exceed the limit — always check that before trusting a single subtraction.

## 9. Class Practice 1: Distributing Stickers

### Problem

How many ways can 12 identical stickers be distributed among 5 children, if a child may receive zero stickers?

### Answer Choices

(A) 1,001  (B) 1,365  (C) 1,820  (D) 3,003  (E) 4,368

<details>
<summary>Solution</summary>

Nonnegative integer solutions to $x_1 + \cdots + x_5 = 12$:

$$C_{12+5-1}^{5-1} = C_{16}^{4} = 1{,}820$$

The answer is **(C) 1,820**.

</details>

## 10. Class Practice 2: Minimum Requirement

### Problem

How many ways can 9 identical marbles be distributed among 3 bags, if each bag must contain at least 1 marble?

### Answer Choices

(A) 10  (B) 28  (C) 36  (D) 45  (E) 55

<details>
<summary>Solution</summary>

Positive integer solutions to $x_1 + x_2 + x_3 = 9$:

$$C_{9-1}^{3-1} = C_{8}^{2} = 28$$

The answer is **(B) 28**.

</details>

## 11. Class Practice 3: Shifted Minimum

### Problem

How many ways can 20 identical apples be distributed among 4 baskets, if each basket must contain at least 3 apples?

### Answer Choices

(A) 45  (B) 84  (C) 120  (D) 165  (E) 220

<details>
<summary>Solution</summary>

Give each basket 3 apples first ($3 \times 4 = 12$ used), leaving $20 - 12 = 8$ to distribute freely among 4 baskets:

$$C_{8+4-1}^{4-1} = C_{11}^{3} = 165$$

The answer is **(D) 165**.

</details>

## 12. Common Mistakes

### 12.1 Using stars and bars on distinct items

If the items being distributed are distinguishable (numbered balls, named people), stars and bars overcounts or miscounts — use the multiplication principle ($k^n$, each item independently picks a box) or a direct case analysis instead.

### 12.2 Using $k$ bars instead of $k - 1$

Splitting a row into $k$ groups needs exactly $k - 1$ dividers, not $k$. Using $k$ bars is the single most common stars-and-bars arithmetic error.

### 12.3 Forgetting to shift before applying the formula

When there is a minimum-per-box requirement, applying $C_{n+k-1}^{k-1}$ directly (without first subtracting $mk$, or substituting $y_i = x_i - m$) silently assumes boxes can be empty, which contradicts the minimum.

### 12.4 Applying stars and bars directly to an upper-bound problem

There is no "stars and bars formula" for upper bounds — you must use the no-restriction formula plus inclusion–exclusion to subtract the over-limit cases, as in Section 8.

### 12.5 Mixing up $H_n^k$'s subscript and superscript

In $H_n^k$, $n$ is the number of distinct **types** available and $k$ is how many are **picked** (with repetition, unordered) — the same subscript/superscript roles as $C_n^k$. Swapping them silently swaps which variable is the box count and which is the ball count.

## 13. Key Takeaways

- Questions A (equation), B (balls into boxes), and C (selection with repetition) are the same stars-and-bars picture in different words — recognize the picture, not just the wording.
- Nonnegative integer solutions to $x_1 + \cdots + x_k = n$, equivalently $n$ identical items into $k$ distinct boxes: $f(n,k) = C_{n+k-1}^{k-1}$.
- Choosing $k$ items with repetition from $n$ types (order doesn't matter): $H_n^k = C_{n+k-1}^{k}$ — the same formula, relabeled.
- Memory trick: don't memorize the formula, rebuild it — gaps $= n+1$, picks $= k-1$, so the answer is $H_{n+1}^{\,k-1}$. Convert $H \to C$ with "top index stays, bottom index becomes sum of both minus 1."
- Positive integer solutions (every box needs at least 1): substitute $y_i = x_i - 1$ to get $g(n,k) = C_{n-1}^{k-1}$. A minimum of $m$ generalizes to $y_i = x_i - m$.
- Stars and bars requires identical items and distinct boxes — check both conditions before reaching for the formula.
- Upper bounds require inclusion–exclusion on top of the basic formula, not a new formula.

Next lesson: [06-recursive-counting.md](./06-recursive-counting.md) covers problems where no closed-form formula exists at all, and the cleanest path is to build up a recursive relationship instead.
