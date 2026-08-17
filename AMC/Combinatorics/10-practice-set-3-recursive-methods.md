# Practice Set 3: The Recursive Method — Building Recurrences From Scratch

This set drills [06-recursive-counting.md](./06-recursive-counting.md) and [07-balls-into-buckets.md](./07-balls-into-buckets.md).

**Do not try to memorize $S(n,j) = j \cdot S(n-1,j) + S(n-1,j-1)$, $p(n,k) = p(n,k-1) + p(n-k,k)$, or any of the other specific recurrences from those lessons.** Those formulas are answers to very narrow questions, and a slightly different problem will need a different recurrence — memorizing them doesn't transfer. What *does* transfer, to almost any hard counting problem, is the method that produced them:

1. Define a target function/quantity for the count you want, in terms of a size parameter (or several).
2. Look at one specific feature of a finished outcome — usually the *last* piece — and ask what determines it.
3. Split into mutually exclusive, exhaustive cases based on that last piece.
4. Show each case reduces to the same target function at a strictly smaller size — this is the transition (recurrence).
5. Solve small base cases by hand, then build up the table.

Every problem below can be solved by running this five-step process fresh, from scratch. If you find yourself trying to recall a formula instead of rebuilding it, stop and re-derive it. For a quick self-check, see the answer-only key in [11-practice-set-answer-keys.md](./11-practice-set-answer-keys.md).

## Problem 1: Tiling With 1×1 and 1×3 Tiles

### Problem

In how many ways can a $1 \times 8$ board be completely covered using $1\times1$ tiles and $1\times3$ tiles?

### Answer Choices

(A) 13  (B) 15  (C) 18  (D) 21  (E) 24

<details>
<summary>Solution</summary>

Let $a_n$ be the number of ways to tile a $1 \times n$ board. Look at the tile covering the **last cell**: it's either a $1\times1$ tile (leaving a $1\times(n-1)$ board: $a_{n-1}$ ways) or a $1\times3$ tile (leaving a $1\times(n-3)$ board: $a_{n-3}$ ways). These cases are mutually exclusive and exhaustive:

$$a_n = a_{n-1} + a_{n-3}$$

Base cases: $a_0 = 1$ (empty board), $a_1 = 1$, $a_2 = 1$ (only two $1\times1$ tiles fit — a $1\times3$ tile doesn't).

| $n$   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8  |
|-------|---|---|---|---|---|---|---|---|----|
| $a_n$ | 1 | 1 | 1 | 2 | 3 | 4 | 6 | 9 | 13 |

The answer is **(A) 13**.

</details>

## Problem 2: Coloring a Strip, No Two Adjacent Alike

### Problem

A $1 \times 6$ strip of tiles is colored using 3 colors, so that no two adjacent tiles share a color. How many colorings are possible?

### Answer Choices

(A) 64  (B) 96  (C) 108  (D) 120  (E) 128

<details>
<summary>Solution</summary>

Let $a_n$ be the count for a strip of $n$ tiles. Look at the **last tile**: whatever color the first $n-1$ tiles used up to position $n-1$, the last tile has exactly 2 legal colors (any color except the one at position $n-1$), regardless of which valid coloring came before:

$$a_n = 2 \cdot a_{n-1}$$

Base case: $a_1 = 3$ (any of the 3 colors, no neighbor to conflict with).

| $n$   | 1 | 2 | 3  | 4  | 5  | 6  |
|-------|---|---|----|----|----|----|
| $a_n$ | 3 | 6 | 12 | 24 | 48 | 96 |

The answer is **(B) 96**.

</details>

## Problem 3: Grid Paths Around a Blocked Square

### Problem

A counter starts at the bottom-left square of a grid, at position $(0,0)$, and can move only right or up, one square at a time. Rows and columns are numbered $0$ to $3$. The square at row 1, column 2 is blocked and cannot be entered. How many distinct paths lead from $(0,0)$ to $(3,3)$?

### Answer Choices

(A) 7  (B) 9  (C) 11  (D) 15  (E) 20

<details>
<summary>Solution</summary>

Let $f(r,c)$ be the number of ways to reach $(r,c)$. Look at the **last move**: it arrived from either $(r-1,c)$ (a move up) or $(r,c-1)$ (a move right) — mutually exclusive, exhaustive:

$$f(r,c) = f(r-1,c) + f(r,c-1)$$

with $f(1,2) = 0$ forced by the block, and any out-of-grid term treated as $0$. Base case $f(0,0)=1$.

Building the table row by row (rows are $r$, columns are $c$):

| $r \backslash c$ | 0 | 1 | 2 | 3  |
|---|---|---|---|----|
| 0 | 1 | 1 | 1 | 1  |
| 1 | 1 | 2 | 0 | 1  |
| 2 | 1 | 3 | 3 | 4  |
| 3 | 1 | 4 | 7 | 11 |

$$f(3,3) = 11$$

(Without the block, the unrestricted count would be $C_6^3 = 20$ — option (E) is that distractor.)

The answer is **(C) 11**.

</details>

## Problem 4: Partial Derangement

### Problem

5 distinct hats are returned at random to their 5 owners, one hat per owner. In how many ways can **exactly 2** people receive their own hat, with the other 3 all receiving a hat that is not theirs?

### Answer Choices

(A) 10  (B) 15  (C) 18  (D) 20  (E) 24

<details>
<summary>Solution</summary>

First choose *which* 2 of the 5 people get their own hat: $C_5^2 = 10$ ways. The remaining 3 people must each get a hat that is **not** theirs — a derangement of those 3, $D_3$.

From [06-recursive-counting.md](./06-recursive-counting.md)'s derangement table, $D_3 = 2$.

$$C_5^2 \times D_3 = 10 \times 2 = 20$$

The answer is **(D) 20**.

</details>

## Problem 5: Trophies to Athletes (Distinct/Distinct)

### Problem

6 distinct trophies are awarded to 4 distinct athletes. Any athlete may receive any number of trophies, including zero. In how many ways can the trophies be awarded?

### Answer Choices

(A) 1,296  (B) 2,401  (C) 3,125  (D) 4,096  (E) 4,320

<details>
<summary>Solution</summary>

Trophies (balls) are distinct, athletes (buckets) are distinct — Case 1, the product rule. Each of the 6 trophies independently picks one of 4 athletes:

$$4^6 = 4{,}096$$

The answer is **(D) 4,096**.

</details>

## Problem 6: Tokens Into Cups (Indistinct/Distinct)

### Problem

9 identical tokens are distributed into 5 distinct cups. A cup may be empty. In how many ways can this be done?

### Answer Choices

(A) 715  (B) 792  (C) 816  (D) 969  (E) 1,001

<details>
<summary>Solution</summary>

Tokens are indistinguishable, cups are distinct — Case 2, stars and bars:

$$C_{9+5-1}^{5-1} = C_{13}^{4} = 715$$

The answer is **(A) 715**.

</details>

## Problem 7: Beads Into Indistinguishable Boxes (Distinct/Indistinct)

### Problem

6 distinct beads are placed into at most 4 indistinguishable boxes (some boxes may be empty). In how many ways can this be done?

### Answer Choices

(A) 122  (B) 187  (C) 202  (D) 203  (E) 218

<details>
<summary>Solution</summary>

Beads are distinct, boxes are indistinguishable — Case 3, sum the Stirling numbers of the second kind $S(6,j)$ for $j = 0$ to $4$. Extending [07-balls-into-buckets.md](./07-balls-into-buckets.md)'s triangle to row $n=6$ with $S(n,j) = j \cdot S(n-1,j) + S(n-1,j-1)$:

$$S(6,1)=1, \quad S(6,2)=31, \quad S(6,3)=90, \quad S(6,4)=65$$

$$\sum_{j=0}^{4} S(6,j) = 0 + 1 + 31 + 90 + 65 = 187$$

((A) $122$ stops the sum one term too early, at $j=3$. (C) $202$ and (D) $203$ sum one or two terms too far, including $S(6,5)=15$ and/or $S(6,6)=1$.)

The answer is **(B) 187**.

</details>

## Problem 8: Coins Into Indistinguishable Purses (Indistinct/Indistinct)

### Problem

10 identical coins are placed into at most 4 indistinguishable purses (some purses may be empty). In how many ways can this be done?

### Answer Choices

(A) 18  (B) 20  (C) 23  (D) 26  (E) 30

<details>
<summary>Solution</summary>

Coins and purses are both indistinguishable — Case 4, integer partitions of 10 into at most 4 parts, $p(10,4)$. Extending [07-balls-into-buckets.md](./07-balls-into-buckets.md)'s table with $p(n,k) = p(n,k-1) + p(n-k,k)$:

$$p(10,3) = 14, \qquad p(6,4) = 9 \implies p(10,4) = p(10,3) + p(6,4) = 14 + 9 = 23$$

The answer is **(C) 23**.

</details>

## Problem 9: No Three Consecutive 1s

### Problem

How many length-7 strings of `0`s and `1`s contain no three consecutive `1`s?

### Answer Choices

(A) 44  (B) 62  (C) 72  (D) 81  (E) 96

<details>
<summary>Solution</summary>

Let $e_n$ be this count. Look at the **run of 1s ending at the last position**: it ends in either a `0` ($e_{n-1}$ ways for the rest), a `10` ($e_{n-2}$ ways for the rest), or a `110` ($e_{n-3}$ ways for the rest) — every valid string falls into exactly one of these three trailing patterns, since three consecutive 1s are forbidden:

$$e_n = e_{n-1} + e_{n-2} + e_{n-3}$$

Base cases: $e_0 = 1$ (empty string), $e_1 = 2$ (`0`, `1`), $e_2 = 4$ (all 4 strings of length 2 are valid — you need 3 in a row to violate the rule).

| $n$   | 0 | 1 | 2 | 3 | 4  | 5  | 6  | 7  |
|-------|---|---|---|---|----|----|----|----|
| $e_n$ | 1 | 2 | 4 | 7 | 13 | 24 | 44 | 81 |

The answer is **(D) 81**.

</details>

## Problem 10: Grid Paths With Two Blocked Squares

### Problem

A counter starts at $(0,0)$ and can move only right or up, one square at a time, on a grid with rows and columns numbered $0$ to $4$. The squares at $(1,1)$ and $(3,2)$ are both blocked. How many distinct paths lead from $(0,0)$ to $(4,4)$?

### Answer Choices

(A) 7  (B) 10  (C) 13  (D) 16  (E) 18

<details>
<summary>Solution</summary>

Same recurrence as Problem 3, $f(r,c) = f(r-1,c) + f(r,c-1)$, now with **two** forced zeros: $f(1,1) = 0$ and $f(3,2) = 0$.

| $r \backslash c$ | 0 | 1 | 2 | 3 | 4  |
|---|---|---|---|---|----|
| 0 | 1 | 1 | 1 | 1 | 1  |
| 1 | 1 | 0 | 1 | 2 | 3  |
| 2 | 1 | 1 | 2 | 4 | 7  |
| 3 | 1 | 2 | 0 | 4 | 11 |
| 4 | 1 | 3 | 3 | 7 | 18 |

$$f(4,4) = 18$$

**Non-obvious detail:** a zero at a blocked square doesn't just remove that square's own paths — it also zeroes out one of the two terms feeding every square downstream of it, which is why $(3,3)=4$ (much smaller than the unblocked $C_6^3=20$) even though only two squares were ever blocked directly.

The answer is **(E) 18**.

</details>

## Problem 11: Stairs With Steps of 1, 2, or 4

### Problem

A staircase has 7 steps. Each move, you may climb 1, 2, or 4 steps at a time. In how many distinct ways can you climb all 7 steps?

### Answer Choices

(A) 31  (B) 34  (C) 37  (D) 41  (E) 46

<details>
<summary>Solution</summary>

Let $h_n$ be the count for $n$ steps. Look at the **last move**: it covers the final 1, 2, or 4 steps, leaving $h_{n-1}$, $h_{n-2}$, or $h_{n-4}$ ways respectively (a term is $0$ if the index is negative):

$$h_n = h_{n-1} + h_{n-2} + h_{n-4}$$

Base case: $h_0 = 1$ (nothing to climb).

| $n$   | 0 | 1 | 2 | 3 | 4 | 5  | 6  | 7  |
|-------|---|---|---|---|---|----|----|----|
| $h_n$ | 1 | 1 | 2 | 3 | 6 | 10 | 18 | 31 |

The answer is **(A) 31**.

</details>

## Problem 12: At Most One Fixed Point

### Problem

6 distinct keys are returned at random to their 6 owners, one key per owner. In how many ways can **at most 1** person receive their own key (that is, either nobody gets their own key, or exactly one person does)?

### Answer Choices

(A) 265  (B) 529  (C) 600  (D) 649  (E) 720

<details>
<summary>Solution</summary>

Split into two mutually exclusive, exhaustive cases: exactly 0 people get their own key, or exactly 1 does.

**Zero fixed points** is a full derangement: $D_6$. **Exactly one fixed point** is (choose who gets their own key: $C_6^1$) $\times$ (derange the other 5: $D_5$).

From [06-recursive-counting.md](./06-recursive-counting.md)'s derangement recurrence $D_n = (n-1)(D_{n-1}+D_{n-2})$, extending past the lesson's table:

$$D_5 = 44, \qquad D_6 = 5 \times (D_5 + D_4) = 5 \times (44+9) = 265$$

$$D_6 + C_6^1 \times D_5 = 265 + 6 \times 44 = 265 + 264 = 529$$

The answer is **(B) 529**.

</details>

## Problem 13: Non-Adjacent Chairs Around a Circle

### Problem

In how many ways can you choose a subset of chairs from 7 chairs arranged in a **circle** (chair 7 and chair 1 count as adjacent) so that no two chosen chairs are next to each other? (The empty subset counts as one valid way.)

### Answer Choices

(A) 18  (B) 24  (C) 29  (D) 34  (E) 41

<details>
<summary>Solution</summary>

Let $g_n$ be this count for $n$ chairs in a circle, and reuse $f_n$, the count for $n$ chairs in a **row**, already built in [06-recursive-counting.md](./06-recursive-counting.md)'s Class Practice 2 ($f_0=1, f_1=2, f_2=3, f_3=5, f_4=8, f_5=13, f_6=21$).

Split on whether **chair 1** is chosen:

- **Chair 1 not chosen:** the wrap-around constraint (chair $n$ vs. chair 1) is automatically satisfied, so chairs $2$ through $n$ just need to avoid adjacent pairs among themselves — exactly the linear problem on $n-1$ chairs: $f_{n-1}$ ways.
- **Chair 1 chosen:** chairs 2 and $n$ are now forbidden (both adjacent to chair 1). Chairs $3$ through $n-1$ form a linear problem on $n-3$ chairs, with no leftover wrap constraint: $f_{n-3}$ ways.

$$g_n = f_{n-1} + f_{n-3}$$

For $n = 7$:

$$g_7 = f_6 + f_4 = 21 + 8 = 29$$

The answer is **(C) 29**.

</details>

## Problem 14: Tiling a 2×n Board With Dominoes

### Problem

In how many ways can a $2 \times 7$ rectangle be completely tiled using $1\times2$ dominoes (each domino covers two adjacent unit squares, placed either horizontally or vertically)?

### Answer Choices

(A) 13  (B) 16  (C) 18  (D) 21  (E) 34

<details>
<summary>Solution</summary>

Let $T_n$ be the number of tilings of a $2\times n$ board. Look at how the **last column** is covered:

- **Case 1:** one vertical domino fills the last column by itself. What remains is a $2\times(n-1)$ board: $T_{n-1}$ ways.
- **Case 2:** two horizontal dominoes, stacked, span the last two columns together. What remains is a $2\times(n-2)$ board: $T_{n-2}$ ways.

(A single horizontal domino can't be used alone in the last column — it would stick out, or leave one cell of that column uncovered by anything except case 2's pairing.)

$$T_n = T_{n-1} + T_{n-2}$$

Base cases: $T_1 = 1$ (one vertical domino), $T_2 = 2$ (two verticals, or two horizontals stacked).

| $n$   | 1 | 2 | 3 | 4 | 5 | 6  | 7  |
|-------|---|---|---|---|---|----|----|
| $T_n$ | 1 | 2 | 3 | 5 | 8 | 13 | 21 |

**Non-obvious detail:** this is the same Fibonacci-shaped recurrence as the $1\times n$ tiling problem in [06-recursive-counting.md](./06-recursive-counting.md) Section 3 — a different-looking setup (2-row board, dominoes only) reduces to an identical transition once you look at "what covers the last column."

The answer is **(D) 21**.

</details>

## Problem 15: Raffle Tickets, Distinct/Distinct

### Problem

8 distinct raffle tickets are placed into 3 distinct boxes, one box per prize tier. A box may hold any number of tickets, including zero. In how many ways can this be done?

### Answer Choices

(A) 512  (B) 1,296  (C) 2,187  (D) 4,096  (E) 6,561

<details>
<summary>Solution</summary>

Tickets are distinct, boxes are distinct — Case 1, the product rule. Each of the 8 tickets independently picks one of 3 boxes:

$$3^8 = 6{,}561$$

The answer is **(E) 6,561**.

</details>

## Problem 16: Pencils, Indistinct/Distinct

### Problem

11 identical candies are distributed among 6 distinct kids, and a kid may receive none. In how many ways can this be done?

### Answer Choices

(A) 4,368  (B) 5,005  (C) 6,006  (D) 8,008  (E) 11,440

<details>
<summary>Solution</summary>

Candies are indistinguishable, kids are distinct — Case 2, stars and bars:

$$C_{11+6-1}^{6-1} = C_{16}^{5} = 4{,}368$$

The answer is **(A) 4,368**.

</details>

## Problem 17: Gift Bags, Distinct/Indistinct

### Problem

7 distinct gifts are placed into at most 4 indistinguishable gift bags (some bags may be empty). In how many ways can this be done?

### Answer Choices

(A) 364  (B) 715  (C) 847  (D) 1,050  (E) 1,260

<details>
<summary>Solution</summary>

Gifts are distinct, bags are indistinguishable — Case 3, sum $S(7,j)$ for $j=0$ to $4$. Extending the Stirling triangle to row $n=7$ using $S(6,j) = 0,1,31,90,65,15,1$ for $j=0,\ldots,6$:

$$S(7,j) = j \cdot S(6,j) + S(6,j-1)$$

$$S(7,1)=1, \quad S(7,2)=63, \quad S(7,3)=301, \quad S(7,4)=350$$

$$\sum_{j=0}^{4} S(7,j) = 0 + 1 + 63 + 301 + 350 = 715$$

The answer is **(B) 715**.

</details>

## Problem 18: Coins, Indistinct/Indistinct

### Problem

12 identical coins are placed into at most 5 indistinguishable purses (some purses may be empty). In how many ways can this be done?

### Answer Choices

(A) 30  (B) 38  (C) 47  (D) 56  (E) 66

<details>
<summary>Solution</summary>

Coins and purses are both indistinguishable — Case 4, integer partitions of 12 into at most 5 parts, $p(12,5)$.

Extending [07-balls-into-buckets.md](./07-balls-into-buckets.md)'s table with $p(n,k) = p(n,k-1)+p(n-k,k)$ out to $k=5$:

$$p(12,4) = 30, \qquad p(7,5) = 17 \implies p(12,5) = p(12,4) + p(7,5) = 30 + 17 = 47$$

The answer is **(C) 47**.

</details>

## Problem 19: Unlimited Unlabeled Groups (Bell Number)

### Problem

6 distinct students are split into study groups. Any number of groups may form (from 1 group holding everyone, up to 6 groups of 1 student each), every group must be nonempty, and the groups themselves are not labeled. In how many ways can the students be split?

### Answer Choices

(A) 150  (B) 175  (C) 187  (D) 203  (E) 220

<details>
<summary>Solution</summary>

This is Case 3 with **no cap** on the number of groups — sum $S(6,j)$ over *every* possible $j$, from $1$ to $6$ (not "at most 4" as in Problem 7):

$$\sum_{j=1}^{6} S(6,j) = 1 + 31 + 90 + 65 + 15 + 1 = 203$$

This total — partitioning $n$ distinct items into any number of nonempty unlabeled groups — is called the $n$-th **Bell number**.

((C) $187$ is Problem 7's answer, the "at most 4 groups" version of this same row — a reminder to check exactly what range the problem is summing over.)

The answer is **(D) 203**.

</details>

## Problem 20: Unrestricted Integer Partitions

### Problem

In how many ways can the number 9 be written as a sum of positive integers, where the order of the summands does not matter and there is no limit on how many summands are used?

### Answer Choices

(A) 15  (B) 19  (C) 22  (D) 26  (E) 30

<details>
<summary>Solution</summary>

This is $p(9,k)$ with $k$ large enough to be no restriction at all — since a partition of $9$ can never use more than $9$ parts (each part is at least $1$), $p(9,9)$ already equals the fully unrestricted count.

Extending the partition table to $k=9$:

$$p(9,9) = 30$$

As a check, the partitions of 9 are: $9,\ 8{+}1,\ 7{+}2,\ 7{+}1{+}1,\ 6{+}3,\ 6{+}2{+}1,\ 6{+}1{+}1{+}1,\ 5{+}4,\ 5{+}3{+}1,\ 5{+}2{+}2,\ 5{+}2{+}1{+}1,\ 5{+}1{+}1{+}1{+}1,\ 4{+}4{+}1,\ 4{+}3{+}2,\ 4{+}3{+}1{+}1,\ 4{+}2{+}2{+}1,\ 4{+}2{+}1{+}1{+}1,\ 4{+}1{+}1{+}1{+}1{+}1,\ 3{+}3{+}3,\ 3{+}3{+}2{+}1,\ 3{+}3{+}1{+}1{+}1,\ 3{+}2{+}2{+}2,\ 3{+}2{+}2{+}1{+}1,\ 3{+}2{+}1{+}1{+}1{+}1,\ 3{+}1{+}1{+}1{+}1{+}1{+}1,\ 2{+}2{+}2{+}2{+}1,\ 2{+}2{+}2{+}1{+}1{+}1,\ 2{+}2{+}1{+}1{+}1{+}1{+}1,\ 2{+}1{+}1{+}1{+}1{+}1{+}1{+}1,\ 1{+}1{+}1{+}1{+}1{+}1{+}1{+}1{+}1$ — 30 partitions.

The answer is **(E) 30**.

</details>

## Key Reminders

- The formula is never the starting point. The starting point is always: name $a_n$ (or $f(n,k)$, or $S(n,j)$, or $p(n,k)$), look at the last piece of a finished outcome, and ask what determines it.
- A good case split is mutually exclusive and exhaustive — the same addition-principle check from Lesson 01, now applied to "what does the last piece look like."
- The recursive state doesn't have to be one number — the grid-path problems needed two coordinates, and multiple blocked squares just zero out more table entries.
- When a definition phrased as "at most $k$" resists a clean recurrence because the transition needs information the "at most" framing throws away, try tightening it to "exactly $k$" — solve that, then sum over it to recover the "at most" version. And when "at most" becomes "no limit at all," sum all the way to the largest index that could ever matter (Problems 19–20).
- This "define state → find transition → build from base cases" pattern is the same idea that reappears as dynamic programming on the algorithms side of this course.

Answer keys for all three practice sets are collected in [11-practice-set-answer-keys.md](./11-practice-set-answer-keys.md). This concludes the practice-set sequence for the introductory combinatorics module.
