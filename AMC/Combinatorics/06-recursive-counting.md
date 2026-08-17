# Lesson 6: The Recursive Formula Method

Some counting problems have no clean closed-form formula — no single application of the multiplication principle, combinations, or stars and bars will finish the job directly. For these, the cleanest approach is to define a sequence `a_n` for the count you want, find how `a_n` relates to smaller values like `a_{n-1}` by looking at the "last piece" of an outcome, and then build the answer up from small base cases.

## 1. The Idea: Reduce to a Smaller Case

Instead of counting all outcomes of size `n` at once, focus on **one specific feature of a finished outcome** — usually its last element, last step, or last position — and ask what the rest of the outcome must look like once that feature is fixed. Each case for that last feature reduces the problem to counting a *smaller* instance of the same kind of object.

## 2. Core Template

```text
1. Define a_n = the quantity you want to count, as a function of n.
2. Look at the "last" position, tile, digit, or choice in an outcome of size n.
3. Split into a small, fixed number of cases based on that last piece.
4. Each case leaves a smaller, similarly-shaped counting problem behind
   -> it equals a_{n-1}, or a_{n-2}, etc.
5. Write a_n as the sum of the smaller-case counts (this is the recurrence).
6. Directly count the base case(s) by hand, usually n = 1 and/or n = 2.
7. Use the recurrence to build up a table of values from the base cases.
```

**Non-obvious detail:** the cases in step 3 must be mutually exclusive and must cover every outcome exactly once — this is really just the addition principle from [01-sum-and-product-rules.md](./01-sum-and-product-rules.md) applied to "what does the last piece look like," so the same overlap trap applies here too.

## 3. Reading Example: Tiling a 1×n Board (Fibonacci-Style)

In how many ways can a 1×n board be completely covered using 1×1 tiles and 1×2 tiles?

Let `a_n` be the number of ways to tile a 1×n board. Look at the **last cell** (position `n`) and ask what covers it:

- **Case 1:** a 1×1 tile covers cell `n` alone. What remains is a 1×(n-1) board to tile in any valid way: `a_{n-1}` ways.
- **Case 2:** a 1×2 tile covers cells `n-1` and `n` together. What remains is a 1×(n-2) board to tile in any valid way: `a_{n-2}` ways.

These two cases are mutually exclusive (the last cell is covered by exactly one tile, and that tile is either length 1 or length 2) and cover every tiling, so:

```text
a_n = a_{n-1} + a_{n-2}
```

Base cases, found by direct counting:

```text
a_1 = 1   (one 1x1 tile)
a_2 = 2   (two 1x1 tiles, or one 1x2 tile)
```

Building up the table:

```text
n:    1  2  3  4  5   6
a_n:  1  2  3  5  8  13
```

This is exactly the Fibonacci sequence.

## 4. Reading Example: Binary Strings with No Two Consecutive 1s

How many length-`n` strings of `0`s and `1`s contain no two consecutive `1`s?

Let `b_n` be this count. Look at the **last digit**:

- **Case 1:** the last digit is `0`. The first `n - 1` digits can be *any* valid string of length `n - 1`: `b_{n-1}` ways.
- **Case 2:** the last digit is `1`. Then the digit before it (position `n - 1`) cannot also be `1`, so it must be `0` — and the first `n - 2` digits can be any valid string of length `n - 2`: `b_{n-2}` ways.

```text
b_n = b_{n-1} + b_{n-2}
```

Base cases:

```text
b_1 = 2   (strings "0" and "1")
b_2 = 3   (strings "00", "01", "10" -- "11" is excluded)
```

```text
n:    1  2  3  4   5
b_n:  2  3  5  8  13
```

**Non-obvious detail:** this is again Fibonacci-shaped, but shifted — `b_n` follows the same recurrence as the tiling problem's `a_n` because both problems are really asking the same combinatorial question in disguise ("how do you build a length-`n` sequence where a certain local pattern is forbidden at the end"). Recognizing that two different-looking problems share a recurrence is a powerful shortcut once you've solved one of them.

## 5. Reading Example: Derangements (a Harder Recurrence)

A derangement of `n` items is a permutation where **no item stays in its original position**. Let `D_n` be the number of derangements of `n` items.

This one needs a slightly sharper case split. Consider where item `1` goes — it must go to some position `k != 1`, and there are `n - 1` choices for `k`. Fix one such `k`. Now consider what happens to whatever item was originally at position `k`:

- **Case A:** item `k` goes to position `1` in return (a direct swap with item 1). The remaining `n - 2` items must derange themselves among their own `n - 2` positions: `D_{n-2}` ways.
- **Case B:** item `k` does *not* go to position `1`. Then relabeling position `1` as "the new forbidden spot" for item `k`, the remaining `n - 1` items (including item `k`, now barred from position `1` instead of its own original position) must derange themselves: `D_{n-1}` ways.

Since there were `n - 1` choices for where item `1` goes, and each choice splits into these two cases:

```text
D_n = (n - 1) * (D_{n-1} + D_{n-2})
```

Base cases:

```text
D_0 = 1   (the empty arrangement, by convention)
D_1 = 0   (the single item has nowhere else to go)
```

```text
n:    0  1  2  3   4    5
D_n:  1  0  1  2   9   44
```

**Non-obvious detail:** `D_1 = 0` is the base case that makes everything else work, and it is easy to get wrong by instinct — a single item genuinely cannot be "deranged," since its only possible position is its own.

## 6. Class Practice 1: Staircase Climbing

### Problem

A staircase has `n` steps. Each move, you may climb either 1 step or 2 steps at a time. In how many distinct ways can you climb a 6-step staircase?

### Answer Choices

(A) 8  (B) 13  (C) 21  (D) 34  (E) 55

### Solution

Let `c_n` be the number of ways to climb `n` steps. Looking at the **last move**: it is either a single step from step `n - 1` (`c_{n-1}` ways) or a double step from step `n - 2` (`c_{n-2}` ways):

```text
c_n = c_{n-1} + c_{n-2},   c_1 = 1,   c_2 = 2
```

```text
n:    1  2  3  4   5   6
c_n:  1  2  3  5   8  13
```

The answer is **(B) 13**.

## 7. Class Practice 2: Choosing Non-Adjacent Chairs

### Problem

In how many ways can you choose a subset of chairs from a row of 6 chairs so that no two chosen chairs are next to each other (the empty subset counts as one valid way)?

### Answer Choices

(A) 13  (B) 17  (C) 21  (D) 24  (E) 32

### Solution

Let `f_n` be the number of valid subsets from a row of `n` chairs. Look at the **last chair** (position `n`):

- **Case 1:** the last chair is not chosen. Then any valid subset of the first `n - 1` chairs works: `f_{n-1}` ways.
- **Case 2:** the last chair is chosen. Then chair `n - 1` cannot be chosen, and any valid subset of the first `n - 2` chairs works: `f_{n-2}` ways.

```text
f_n = f_{n-1} + f_{n-2}
```

Base cases: `f_0 = 1` (only the empty subset), `f_1 = 2` (empty, or just the one chair).

```text
n:    0  1  2  3  4   5   6
f_n:  1  2  3  5  8  13  21
```

The answer is **(C) 21**.

**Non-obvious detail:** this problem is the same recurrence as the tiling problem in Section 3, just re-indexed — a chosen chair "blocks" its neighbor the same way a placed tile blocks the next cell, which is why the numbers match up one index apart.

## 8. Class Practice 3: A Three-Term Recurrence

### Problem

In how many ways can a 1×n board be tiled using 1×1, 1×2, and 1×3 tiles? Find the count for `n = 5`.

### Answer Choices

(A) 13  (B) 15  (C) 24  (D) 30  (E) 37

### Solution

Let `g_n` be the count. Looking at the **last tile**, it has length 1, 2, or 3:

```text
g_n = g_{n-1} + g_{n-2} + g_{n-3}
```

Base cases: `g_0 = 1` (empty board, one way to tile nothing), `g_1 = 1`, `g_2 = 2` (found the same way as Section 3).

```text
n:    0  1  2  3   4   5
g_n:  1  1  2  4   7  13
```

The answer is **(A) 13**.

## 9. Common Mistakes

### 9.1 Choosing a base case that doesn't match the recurrence's assumptions

If the recurrence was derived assuming `n >= 2` (it needs `a_{n-2}` to make sense), you need both `a_1` and `a_2` as base cases — supplying only `a_1` and trying to run the recurrence at `n = 2` will reference an undefined `a_0` incorrectly, or silently use the wrong value.

### 9.2 Missing a case in the split

If the case split in step 3 does not cover every possible "last piece" (for example, forgetting that a tile could be length 3 when 1×1, 1×2, and 1×3 tiles are all allowed), the recurrence undercounts.

### 9.3 Letting cases overlap

If two cases in the split can both describe the same outcome, the recurrence overcounts — exactly the addition-principle trap from Lesson 1, now hiding inside a recurrence.

### 9.4 Off-by-one errors when building the table

Recurrences are unforgiving about indices — double-check which `n` each row of your table corresponds to before reading off the final answer.

## 10. Key Takeaways

- When no direct formula is visible, define `a_n`, look at the *last piece* of an outcome, and split into mutually exclusive, exhaustive cases to get a recurrence.
- Solve small base cases directly by hand — this is where the recurrence "anchors" to real counts.
- Build the answer up from the base cases; do not try to guess the closed form first.
- Recognizing that two different-looking problems share the same recurrence (as in tiling vs. non-adjacent selection vs. no-consecutive-1s strings) is a fast way to reuse work.
- This same "define state, find a recurrence, build up from base cases" mindset reappears as **dynamic programming** in the algorithms side of this course — the math and the code are the same idea.

This concludes the introductory sequence of this module. Later lessons can extend these ideas to inclusion–exclusion with more than two sets, generating functions, and probability built on top of these counting techniques.
