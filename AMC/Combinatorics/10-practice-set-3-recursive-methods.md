# Practice Set 3: The Recursive Method — Building Recurrences From Scratch

This set drills [06-recursive-counting.md](./06-recursive-counting.md) and [07-balls-into-buckets.md](./07-balls-into-buckets.md).

**Do not try to memorize $S(n,j) = j \cdot S(n-1,j) + S(n-1,j-1)$, $p(n,k) = p(n,k-1) + p(n-k,k)$, or any of the other specific recurrences from those lessons.** Those formulas are answers to very narrow questions, and a slightly different problem will need a different recurrence — memorizing them doesn't transfer. What *does* transfer, to almost any hard counting problem, is the method that produced them:

1. Define a target function/quantity for the count you want, in terms of a size parameter (or several).
2. Look at one specific feature of a finished outcome — usually the *last* piece — and ask what determines it.
3. Split into mutually exclusive, exhaustive cases based on that last piece.
4. Show each case reduces to the same target function at a strictly smaller size — this is the transition (recurrence).
5. Solve small base cases by hand, then build up the table.

Every problem below can be solved by running this five-step process fresh, from scratch. If you find yourself trying to recall a formula instead of rebuilding it, stop and re-derive it. This file holds problems only; the answer key and full worked solutions live in [13-practice-set-3-solutions.md](./13-practice-set-3-solutions.md).

## Problem 1: Tiling With 1×1 and 1×3 Tiles

In how many ways can a $1 \times 8$ board be completely covered using $1\times1$ tiles and $1\times3$ tiles?

(A) 13  (B) 15  (C) 18  (D) 21  (E) 24

## Problem 2: Coloring a Strip, No Two Adjacent Alike

A $1 \times 6$ strip of tiles is colored using 3 colors, so that no two adjacent tiles share a color. How many colorings are possible?

(A) 64  (B) 96  (C) 108  (D) 120  (E) 128

## Problem 3: Grid Paths Around a Blocked Square

A counter starts at the bottom-left square of a grid, at position $(0,0)$, and can move only right or up, one square at a time. Rows and columns are numbered $0$ to $3$. The square at row 1, column 2 is blocked and cannot be entered. How many distinct paths lead from $(0,0)$ to $(3,3)$?

(A) 7  (B) 9  (C) 11  (D) 15  (E) 20

## Problem 4: Partial Derangement

5 distinct hats are returned at random to their 5 owners, one hat per owner. In how many ways can **exactly 2** people receive their own hat, with the other 3 all receiving a hat that is not theirs?

(A) 10  (B) 15  (C) 18  (D) 20  (E) 24

## Problem 5: Trophies to Athletes (Distinct/Distinct)

6 distinct trophies are awarded to 4 distinct athletes. Any athlete may receive any number of trophies, including zero. In how many ways can the trophies be awarded?

(A) 1,296  (B) 2,401  (C) 3,125  (D) 4,096  (E) 4,320

## Problem 6: Tokens Into Cups (Indistinct/Distinct)

9 identical tokens are distributed into 5 distinct cups. A cup may be empty. In how many ways can this be done?

(A) 715  (B) 792  (C) 816  (D) 969  (E) 1,001

## Problem 7: Beads Into Indistinguishable Boxes (Distinct/Indistinct)

6 distinct beads are placed into at most 4 indistinguishable boxes (some boxes may be empty). In how many ways can this be done?

(A) 122  (B) 187  (C) 202  (D) 203  (E) 218

## Problem 8: Coins Into Indistinguishable Purses (Indistinct/Indistinct)

10 identical coins are placed into at most 4 indistinguishable purses (some purses may be empty). In how many ways can this be done?

(A) 18  (B) 20  (C) 23  (D) 26  (E) 30

## Problem 9: No Three Consecutive 1s

How many length-7 strings of `0`s and `1`s contain no three consecutive `1`s?

(A) 44  (B) 62  (C) 72  (D) 81  (E) 96

## Problem 10: Grid Paths With Two Blocked Squares

A counter starts at $(0,0)$ and can move only right or up, one square at a time, on a grid with rows and columns numbered $0$ to $4$. The squares at $(1,1)$ and $(3,2)$ are both blocked. How many distinct paths lead from $(0,0)$ to $(4,4)$?

(A) 7  (B) 10  (C) 13  (D) 16  (E) 18

## Problem 11: Stairs With Steps of 1, 2, or 4

A staircase has 7 steps. Each move, you may climb 1, 2, or 4 steps at a time. In how many distinct ways can you climb all 7 steps?

(A) 31  (B) 34  (C) 37  (D) 41  (E) 46

## Problem 12: At Most One Fixed Point

6 distinct keys are returned at random to their 6 owners, one key per owner. In how many ways can **at most 1** person receive their own key (that is, either nobody gets their own key, or exactly one person does)?

(A) 265  (B) 529  (C) 600  (D) 649  (E) 720

## Problem 13: Non-Adjacent Chairs Around a Circle

In how many ways can you choose a subset of chairs from 7 chairs arranged in a **circle** (chair 7 and chair 1 count as adjacent) so that no two chosen chairs are next to each other? (The empty subset counts as one valid way.)

(A) 18  (B) 24  (C) 29  (D) 34  (E) 41

## Problem 14: Tiling a 2×n Board With Dominoes

In how many ways can a $2 \times 7$ rectangle be completely tiled using $1\times2$ dominoes (each domino covers two adjacent unit squares, placed either horizontally or vertically)?

(A) 13  (B) 16  (C) 18  (D) 21  (E) 34

## Problem 15: Raffle Tickets, Distinct/Distinct

8 distinct raffle tickets are placed into 3 distinct boxes, one box per prize tier. A box may hold any number of tickets, including zero. In how many ways can this be done?

(A) 512  (B) 1,296  (C) 2,187  (D) 4,096  (E) 6,561

## Problem 16: Pencils, Indistinct/Distinct

11 identical candies are distributed among 6 distinct kids, and a kid may receive none. In how many ways can this be done?

(A) 4,368  (B) 5,005  (C) 6,006  (D) 8,008  (E) 11,440

## Problem 17: Gift Bags, Distinct/Indistinct

7 distinct gifts are placed into at most 4 indistinguishable gift bags (some bags may be empty). In how many ways can this be done?

(A) 364  (B) 715  (C) 847  (D) 1,050  (E) 1,260

## Problem 18: Coins, Indistinct/Indistinct

12 identical coins are placed into at most 5 indistinguishable purses (some purses may be empty). In how many ways can this be done?

(A) 30  (B) 38  (C) 47  (D) 56  (E) 66

## Problem 19: Unlimited Unlabeled Groups (Bell Number)

6 distinct students are split into study groups. Any number of groups may form (from 1 group holding everyone, up to 6 groups of 1 student each), every group must be nonempty, and the groups themselves are not labeled. In how many ways can the students be split?

(A) 150  (B) 175  (C) 187  (D) 203  (E) 220

## Problem 20: Unrestricted Integer Partitions

In how many ways can the number 9 be written as a sum of positive integers, where the order of the summands does not matter and there is no limit on how many summands are used?

(A) 15  (B) 19  (C) 22  (D) 26  (E) 30

## Key Reminders

- The formula is never the starting point. The starting point is always: name $a_n$ (or $f(n,k)$, or $S(n,j)$, or $p(n,k)$), look at the last piece of a finished outcome, and ask what determines it.
- A good case split is mutually exclusive and exhaustive — the same addition-principle check from Lesson 01, now applied to "what does the last piece look like."
- The recursive state doesn't have to be one number — the grid-path problems needed two coordinates, and multiple blocked squares just zero out more table entries.
- When a definition phrased as "at most $k$" resists a clean recurrence because the transition needs information the "at most" framing throws away, try tightening it to "exactly $k$" — solve that, then sum over it to recover the "at most" version. And when "at most" becomes "no limit at all," sum all the way to the largest index that could ever matter (Problems 19–20).
- This "define state → find transition → build from base cases" pattern is the same idea that reappears as dynamic programming on the algorithms side of this course.

Check your work against [13-practice-set-3-solutions.md](./13-practice-set-3-solutions.md). This concludes the practice-set sequence for the introductory combinatorics module.
