# Lesson 6: The Recursive Formula Method
*AMC / Combinatorics*

Some counting problems have no clean closed-form formula — no single application of the multiplication principle, combinations, or stars and bars will finish the job directly. For these, the cleanest approach is to define a sequence $a_n$ for the count you want, find how $a_n$ relates to smaller values like $a_{n-1}$ by looking at the "last piece" of an outcome, and then build the answer up from small base cases.

## 1. The Idea: Reduce to a Smaller Case

Instead of counting all outcomes of size $n$ at once, focus on **one specific feature of a finished outcome** — usually its last element, last step, or last position — and ask what the rest of the outcome must look like once that feature is fixed. Each case for that last feature reduces the problem to counting a *smaller* instance of the same kind of object.

## 2. Core Template

1. Define $a_n$ = the quantity you want to count, as a function of $n$.
2. Look at the "last" position, tile, digit, or choice in an outcome of size $n$.
3. Split into a small, fixed number of cases based on that last piece.
4. Each case leaves a smaller, similarly-shaped counting problem behind → it equals $a_{n-1}$, or $a_{n-2}$, etc.
5. Write $a_n$ as the sum of the smaller-case counts (this is the recurrence).
6. Directly count the base case(s) by hand, usually $n = 1$ and/or $n = 2$.
7. Use the recurrence to build up a table of values from the base cases.

**Non-obvious detail:** the cases in step 3 must be mutually exclusive and must cover every outcome exactly once — this is really just the addition principle from [01-sum-and-product-rules.md](./01-sum-and-product-rules.md) applied to "what does the last piece look like," so the same overlap trap applies here too.

## 3. Reading Example: Tiling a $1 \times n$ Board (Fibonacci-Style)

In how many ways can a $1 \times n$ board be completely covered using $1\times1$ tiles and $1\times2$ tiles?

Let $a_n$ be the number of ways to tile a $1 \times n$ board. Look at the **last cell** (position $n$) and ask what covers it:

- **Case 1:** a $1 \times 1$ tile covers cell $n$ alone. What remains is a $1 \times (n-1)$ board to tile in any valid way: $a_{n-1}$ ways.
- **Case 2:** a $1 \times 2$ tile covers cells $n-1$ and $n$ together. What remains is a $1 \times (n-2)$ board to tile in any valid way: $a_{n-2}$ ways.

These two cases are mutually exclusive (the last cell is covered by exactly one tile, and that tile is either length 1 or length 2) and cover every tiling, so:

$$a_n = a_{n-1} + a_{n-2}$$

Base cases, found by direct counting:

$$a_1 = 1 \ \text{(one } 1\times 1 \text{ tile)}, \qquad a_2 = 2 \ \text{(two } 1\times 1 \text{ tiles, or one } 1\times 2 \text{ tile)}$$

Building up the table:

| $n$   | 1 | 2 | 3 | 4 | 5 | 6  |
|-------|---|---|---|---|---|----|
| $a_n$ | 1 | 2 | 3 | 5 | 8 | 13 |

This is exactly the Fibonacci sequence.

## 4. Reading Example: Binary Strings with No Two Consecutive 1s

How many length-$n$ strings of `0`s and `1`s contain no two consecutive `1`s?

Let $b_n$ be this count. Look at the **last digit**:

- **Case 1:** the last digit is `0`. The first $n - 1$ digits can be *any* valid string of length $n - 1$: $b_{n-1}$ ways.
- **Case 2:** the last digit is `1`. Then the digit before it (position $n - 1$) cannot also be `1`, so it must be `0` — and the first $n - 2$ digits can be any valid string of length $n - 2$: $b_{n-2}$ ways.

$$b_n = b_{n-1} + b_{n-2}$$

Base cases:

$$b_1 = 2 \ \text{(strings "0" and "1")}, \qquad b_2 = 3 \ \text{(strings "00", "01", "10" — "11" is excluded)}$$

| $n$   | 1 | 2 | 3 | 4 | 5  |
|-------|---|---|---|---|----|
| $b_n$ | 2 | 3 | 5 | 8 | 13 |

**Non-obvious detail:** this is again Fibonacci-shaped, but shifted — $b_n$ follows the same recurrence as the tiling problem's $a_n$ because both problems are really asking the same combinatorial question in disguise ("how do you build a length-$n$ sequence where a certain local pattern is forbidden at the end"). Recognizing that two different-looking problems share a recurrence is a powerful shortcut once you've solved one of them.

## 5. Reading Example: Knight Paths Using Only Upward Moves

A knight starts on the bottom-left square of a chessboard (square $a1$) and is only allowed to make moves that increase its row number — moves that go "upward." A knight normally has up to 8 possible move shapes, $(\pm 1, \pm 2)$ and $(\pm 2, \pm 1)$ as (row, column) offsets, but requiring the row to increase leaves only **four** of them:

$$(+1, +2), \quad (+1, -2), \quad (+2, +1), \quad (+2, -1)$$

In how many distinct ways can the knight reach the top-right corner square?

Number the rows and columns $0$ through $7$, with row $0$ the bottom row and column $0$ the leftmost column, so the knight starts at $(0,0)$ and the target is $(7,7)$.

Let $f(r, c)$ be the number of ways to reach square $(r, c)$ using only upward moves. Instead of looking at the last *digit* or *tile* as in the previous examples, look at the knight's **last move**. Whatever path it took, that move landed it on $(r,c)$ from exactly one of four possible squares — the four upward moves, run in reverse:

$$f(r, c) = f(r-1, c-2) + f(r-1, c+2) + f(r-2, c-1) + f(r-2, c+1)$$

(a term is $0$ whenever its square falls off the board — the same convention as an out-of-range index contributing nothing in the earlier recurrences.)

These four cases are mutually exclusive (a knight move has one specific shape) and exhaustive (every arrival has some last move), so the addition principle applies exactly as before.

**Base case:** the knight starts at $(0,0)$ with zero moves, so $f(0,0) = 1$. Every other square in row $0$ is unreachable, because *every* allowed move increases the row: $f(0, c) = 0$ for $c \ne 0$.

Because $f(r,c)$ only depends on rows $r-1$ and $r-2$, the table can be filled row by row, exactly like the 1-D tables in Sections 3 and 4 — just indexed by two coordinates instead of one. The figure below works this out on a smaller $5 \times 5$ board:

![Left: a diagram showing that the last move into square (r,c) must arrive from one of four squares f(r-1,c-2), f(r-1,c+2), f(r-2,c-1), or f(r-2,c+1), giving the recurrence f(r,c) = sum of those four terms. Right: a 5x5 board with each square filled in with its computed path count, built up row by row from the bottom; the knight starts at the bottom-left corner with count 1, and the top-right corner is reached in 2 ways.](./images/knight-upward-paths.svg)

Working row by row on the $5\times5$ board gives $f(4,4) = 2$. Applying the exact same recurrence and base case to a full, standard $8\times8$ board gives:

$$f(7,7) = 18$$

**Non-obvious detail:** this is the same "define the count, split on the last piece, build up from a base case" template as every recurrence in this lesson — the only new idea is that the *state* now needs two coordinates $(r,c)$ instead of one index $n$, since a knight's position isn't described by a single number. The recurrence still only ever refers to strictly smaller states (rows $r-1$ and $r-2$), which is exactly what makes the row-by-row build-up valid.

## 6. Reading Example: Derangements (a Harder Recurrence)

A derangement of $n$ items is a permutation where **no item stays in its original position**. Let $D_n$ be the number of derangements of $n$ items.

This one needs a slightly sharper case split. Consider where item $1$ goes — it must go to some position $k \ne 1$, and there are $n - 1$ choices for $k$. Fix one such $k$. Now consider what happens to whatever item was originally at position $k$:

- **Case A:** item $k$ goes to position $1$ in return (a direct swap with item 1). The remaining $n - 2$ items must derange themselves among their own $n - 2$ positions: $D_{n-2}$ ways.
- **Case B:** item $k$ does *not* go to position $1$. Then relabeling position $1$ as "the new forbidden spot" for item $k$, the remaining $n - 1$ items (including item $k$, now barred from position $1$ instead of its own original position) must derange themselves: $D_{n-1}$ ways.

Since there were $n - 1$ choices for where item $1$ goes, and each choice splits into these two cases:

$$D_n = (n - 1)\,(D_{n-1} + D_{n-2})$$

Base cases:

$$D_0 = 1 \ \text{(the empty arrangement, by convention)}, \qquad D_1 = 0 \ \text{(the single item has nowhere else to go)}$$

| $n$   | 0 | 1 | 2 | 3 | 4 | 5  |
|-------|---|---|---|---|---|----|
| $D_n$ | 1 | 0 | 1 | 2 | 9 | 44 |

**Non-obvious detail:** $D_1 = 0$ is the base case that makes everything else work, and it is easy to get wrong by instinct — a single item genuinely cannot be "deranged," since its only possible position is its own.

## 7. Class Practice 1: Staircase Climbing

### Problem

A staircase has $n$ steps. Each move, you may climb either 1 step or 2 steps at a time. In how many distinct ways can you climb a 6-step staircase?

### Answer Choices

(A) 8  (B) 13  (C) 21  (D) 34  (E) 55

<details>
<summary>Solution</summary>

Let $c_n$ be the number of ways to climb $n$ steps. Looking at the **last move**: it is either a single step from step $n - 1$ ($c_{n-1}$ ways) or a double step from step $n - 2$ ($c_{n-2}$ ways):

$$c_n = c_{n-1} + c_{n-2}, \qquad c_1 = 1, \qquad c_2 = 2$$

| $n$   | 1 | 2 | 3 | 4 | 5 | 6  |
|-------|---|---|---|---|---|----|
| $c_n$ | 1 | 2 | 3 | 5 | 8 | 13 |

The answer is **(B) 13**.

</details>

## 8. Class Practice 2: Choosing Non-Adjacent Chairs

### Problem

In how many ways can you choose a subset of chairs from a row of 6 chairs so that no two chosen chairs are next to each other (the empty subset counts as one valid way)?

### Answer Choices

(A) 13  (B) 17  (C) 21  (D) 24  (E) 32

<details>
<summary>Solution</summary>

Let $f_n$ be the number of valid subsets from a row of $n$ chairs. Look at the **last chair** (position $n$):

- **Case 1:** the last chair is not chosen. Then any valid subset of the first $n - 1$ chairs works: $f_{n-1}$ ways.
- **Case 2:** the last chair is chosen. Then chair $n - 1$ cannot be chosen, and any valid subset of the first $n - 2$ chairs works: $f_{n-2}$ ways.

$$f_n = f_{n-1} + f_{n-2}$$

Base cases: $f_0 = 1$ (only the empty subset), $f_1 = 2$ (empty, or just the one chair).

| $n$   | 0 | 1 | 2 | 3 | 4 | 5  | 6  |
|-------|---|---|---|---|---|----|----|
| $f_n$ | 1 | 2 | 3 | 5 | 8 | 13 | 21 |

The answer is **(C) 21**.

</details>

**Non-obvious detail:** this problem is the same recurrence as the tiling problem in Section 3, just re-indexed — a chosen chair "blocks" its neighbor the same way a placed tile blocks the next cell, which is why the numbers match up one index apart.

## 9. Class Practice 3: A Three-Term Recurrence

### Problem

In how many ways can a $1 \times n$ board be tiled using $1\times1$, $1\times2$, and $1\times3$ tiles? Find the count for $n = 5$.

### Answer Choices

(A) 13  (B) 15  (C) 24  (D) 30  (E) 37

<details>
<summary>Solution</summary>

Let $g_n$ be the count. Looking at the **last tile**, it has length 1, 2, or 3:

$$g_n = g_{n-1} + g_{n-2} + g_{n-3}$$

Base cases: $g_0 = 1$ (empty board, one way to tile nothing), $g_1 = 1$, $g_2 = 2$ (found the same way as Section 3).

| $n$   | 0 | 1 | 2 | 3 | 4 | 5  |
|-------|---|---|---|---|---|----|
| $g_n$ | 1 | 1 | 2 | 4 | 7 | 13 |

The answer is **(A) 13**.

</details>

## 10. Common Mistakes

### 10.1 Choosing a base case that doesn't match the recurrence's assumptions

If the recurrence was derived assuming $n \ge 2$ (it needs $a_{n-2}$ to make sense), you need both $a_1$ and $a_2$ as base cases — supplying only $a_1$ and trying to run the recurrence at $n = 2$ will reference an undefined $a_0$ incorrectly, or silently use the wrong value.

### 10.2 Missing a case in the split

If the case split in step 3 does not cover every possible "last piece" (for example, forgetting that a tile could be length 3 when $1\times1$, $1\times2$, and $1\times3$ tiles are all allowed), the recurrence undercounts.

### 10.3 Letting cases overlap

If two cases in the split can both describe the same outcome, the recurrence overcounts — exactly the addition-principle trap from Lesson 1, now hiding inside a recurrence.

### 10.4 Off-by-one errors when building the table

Recurrences are unforgiving about indices — double-check which $n$ each row of your table corresponds to before reading off the final answer.

## 11. Key Takeaways

- When no direct formula is visible, define $a_n$, look at the *last piece* of an outcome, and split into mutually exclusive, exhaustive cases to get a recurrence.
- Solve small base cases directly by hand — this is where the recurrence "anchors" to real counts.
- Build the answer up from the base cases; do not try to guess the closed form first.
- Recognizing that two different-looking problems share the same recurrence (as in tiling vs. non-adjacent selection vs. no-consecutive-1s strings) is a fast way to reuse work.
- The state you recurse on doesn't have to be a single index — the knight-paths example needed a row *and* a column — as long as every case in the split points to a strictly smaller state, the same build-up-from-base-cases approach still works.
- This same "define state, find a recurrence, build up from base cases" mindset reappears as **dynamic programming** in the algorithms side of this course — the math and the code are the same idea.

Next lesson: [07-balls-into-buckets.md](./07-balls-into-buckets.md) uses this same recursive-counting method to build two new counting tools — Stirling numbers and integer partitions — as part of a unified framework for distributing balls into buckets.
