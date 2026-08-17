# Lesson 5: Special Model — Stars and Bars

Every technique so far — permutations, combinations, adjacency constraints — has counted arrangements of **distinct** items. This lesson covers a different kind of problem: distributing **identical** items into distinct groups. The standard tool is called **stars and bars**.

## 1. The Setup

Suppose you have `n` identical balls (stars) and want to put them into `k` distinct boxes (a box may hold zero or more balls). How many different distributions are there?

Picture the balls in a row as `n` stars. To split them into `k` groups, place `k - 1` **bars** among the stars — the balls before the first bar go in box 1, the balls between the first and second bar go in box 2, and so on:

```text
* * | * * * | | * *
box1  box2   box3 box4
```

(This example shows 7 stars split into 4 boxes: box 1 gets 2, box 2 gets 3, box 3 gets 0, box 4 gets 2.)

A distribution is completely determined by **where the bars go** among the `n + (k - 1)` total symbols. Choosing which `k - 1` of the `n + k - 1` positions are bars (the rest are automatically stars) gives the count.

## 2. Core Formula

```text
number of ways to write n identical balls into k distinct boxes (boxes may be empty)
  = number of nonnegative integer solutions to x1 + x2 + ... + xk = n
  = C(n + k - 1, k - 1)
  = C(n + k - 1, n)
```

If every box must get **at least 1** ball (positive integers only, requires `n >= k`), first place 1 ball in every box to satisfy the minimum, then distribute the remaining `n - k` balls with no restriction, using the same formula with `n - k` balls and `k` boxes:

```text
number of positive integer solutions to x1 + x2 + ... + xk = n   (each xi >= 1)
  = C((n - k) + k - 1, k - 1)
  = C(n - 1, k - 1)
```

**Non-obvious detail:** stars and bars only applies when the `n` items being distributed are **identical** to each other. If the items are distinct (e.g., 5 different books into 3 distinct boxes), this is a different problem entirely, counted with the multiplication principle instead (each of the `n` distinct items independently picks one of `k` boxes: `k^n`).

## 3. Reading Example: No Restriction

How many ways can 10 identical candies be distributed among 3 kids (a kid may get 0 candies)?

This is nonnegative integer solutions to `x1 + x2 + x3 = 10`:

```text
C(10 + 3 - 1, 3 - 1) = C(12, 2) = 66
```

## 4. Reading Example: Everyone Gets At Least One

How many ways can 10 identical candies be distributed among 3 kids, if every kid must get at least 1 candy?

Give each kid 1 candy first (uses 3 of the 10), then distribute the remaining `10 - 3 = 7` candies with no restriction:

```text
C(7 + 3 - 1, 3 - 1) = C(9, 2) = 36
```

Or directly with the positive-solutions formula: `C(10 - 1, 3 - 1) = C(9, 2) = 36`. Same answer.

## 5. Reading Example: A Larger Minimum (the Shift Trick)

How many ways can 15 identical candies be distributed among 4 kids, if every kid must get **at least 2** candies?

Give each kid 2 candies first (uses `2 * 4 = 8` of the 15), leaving `15 - 8 = 7` candies to distribute with no restriction among the 4 kids:

```text
C(7 + 4 - 1, 4 - 1) = C(10, 3) = 120
```

**Non-obvious detail (the general shift trick):** for a minimum of `m` per box, subtract `m * k` from `n` first, then apply the no-restriction formula to the reduced total. This works because setting `yi = xi - m` turns "`xi >= m`" into "`yi >= 0`," and the equation `x1 + ... + xk = n` becomes `y1 + ... + yk = n - m*k`, which is exactly the Section 2 formula.

## 6. Reading Example: An Upper Bound (Complement, Small Case)

How many ways can 8 identical candies be distributed among 3 kids, if no kid may get more than 5?

First count with no restriction: `C(8 + 3 - 1, 3 - 1) = C(10, 2) = 45`. Now subtract the invalid distributions where some kid gets 6 or more. If one particular kid gets at least 6, give that kid 6 candies first, leaving `8 - 6 = 2` to distribute freely among the 3 kids: `C(2 + 3 - 1, 3 - 1) = C(4, 2) = 6` ways. Since `8 < 6 + 6`, at most one kid can possibly exceed the limit, so there is no double-counted overlap to correct for. With 3 choices for *which* kid is the one exceeding the limit:

```text
45 - 3 * 6 = 45 - 18 = 27
```

**Non-obvious detail:** this "subtract the over-limit cases" approach is inclusion–exclusion (see [02-inclusion-exclusion-principle.md](./02-inclusion-exclusion-principle.md)) layered on top of stars and bars. It only stays this simple when the total `n` is small enough that two kids cannot simultaneously exceed the limit — always check that before trusting a single subtraction.

## 7. Class Practice 1: Distributing Stickers

### Problem

How many ways can 12 identical stickers be distributed among 5 children, if a child may receive zero stickers?

### Answer Choices

(A) 1,001  (B) 1,365  (C) 1,820  (D) 3,003  (E) 4,368

### Solution

Nonnegative integer solutions to `x1 + ... + x5 = 12`:

```text
C(12 + 5 - 1, 5 - 1) = C(16, 4) = 1,820
```

The answer is **(C) 1,820**.

## 8. Class Practice 2: Minimum Requirement

### Problem

How many ways can 9 identical marbles be distributed among 3 bags, if each bag must contain at least 1 marble?

### Answer Choices

(A) 10  (B) 28  (C) 36  (D) 45  (E) 55

### Solution

Positive integer solutions to `x1 + x2 + x3 = 9`:

```text
C(9 - 1, 3 - 1) = C(8, 2) = 28
```

The answer is **(B) 28**.

## 9. Class Practice 3: Shifted Minimum

### Problem

How many ways can 20 identical apples be distributed among 4 baskets, if each basket must contain at least 3 apples?

### Answer Choices

(A) 45  (B) 84  (C) 120  (D) 165  (E) 220

### Solution

Give each basket 3 apples first (`3 * 4 = 12` used), leaving `20 - 12 = 8` to distribute freely among 4 baskets:

```text
C(8 + 4 - 1, 4 - 1) = C(11, 3) = 165
```

The answer is **(D) 165**.

## 10. Common Mistakes

### 10.1 Using stars and bars on distinct items

If the items being distributed are distinguishable (numbered balls, named people), stars and bars overcounts or miscounts — use the multiplication principle (`k^n`, each item independently picks a box) or a direct case analysis instead.

### 10.2 Using `k` bars instead of `k - 1`

Splitting a row into `k` groups needs exactly `k - 1` dividers, not `k`. Using `k` bars is the single most common stars-and-bars arithmetic error.

### 10.3 Forgetting to shift before applying the formula

When there is a minimum-per-box requirement, applying `C(n + k - 1, k - 1)` directly (without first subtracting `m * k`) silently assumes boxes can be empty, which contradicts the minimum.

### 10.4 Applying stars and bars directly to an upper-bound problem

There is no "stars and bars formula" for upper bounds — you must use the no-restriction formula plus inclusion–exclusion to subtract the over-limit cases, as in Section 6.

## 11. Key Takeaways

- Distributing `n` identical items into `k` distinct boxes (empty boxes allowed): `C(n + k - 1, k - 1)`.
- Same, but every box needs at least 1: `C(n - 1, k - 1)`.
- Same, but every box needs at least `m`: shift by subtracting `m * k` from `n` first, then apply the no-restriction formula.
- Stars and bars requires identical items and distinct boxes — check both conditions before reaching for the formula.
- Upper bounds require inclusion–exclusion on top of the basic formula, not a new formula.

Next lesson: [06-recursive-counting.md](./06-recursive-counting.md) covers problems where no closed-form formula exists at all, and the cleanest path is to build up a recursive relationship instead.
