# Lesson 4: Special Model — Adjacency Constraints

Many AMC arrangement problems take the standard permutation setup from [03-permutations-and-combinations.md](./03-permutations-and-combinations.md) and add one extra condition: two particular people or items must sit together, or must never sit together. Two clean techniques handle these — the **bundling method** and the **gap method**.

## 1. When A and B Must Be Adjacent: The Bundling Method

Concept: glue A and B into a single block so they can never be separated. This is a clean application of the product rule, split into two independent steps:

1. Arrange the $n - 1$ items: the $n - 2$ untouched items plus the glued AB block.
2. Arrange A and B *within* their block.

Let $\text{Adj}(n)$ be the number of arrangements of $n$ items with $A$ and $B$ forced adjacent. Step 1 gives $(n-1)!$ ways, and step 2 gives $2!$ ways, so by the product rule:

$$\text{Adj}(n) = (n - 1)! \times 2!$$

The $2!$ is there because inside the block, A and B can still be ordered two ways (`AB` or `BA`).

**Non-obvious detail:** if the problem forces a block of $k$ specific items to stay together in some order, the block reduces the item count by $k - 1$ (not $k$), and the internal factor is $k!$ (not $2!$) if any internal order is allowed, or $1$ if a specific internal order is required.

## 2. When A and B Must NOT Be Adjacent: The Gap Method

Concept: first arrange everyone **except** A and B. This creates "gaps" — slots before the first person, between every consecutive pair, and after the last person — where A and B can be inserted without ever landing next to each other. Again a two-step product rule:

1. Arrange the $n - 2$ other items, which creates $(n - 2) + 1 = n - 1$ gaps.
2. Place A and B into 2 of those $n - 1$ gaps, in order.

Let $\text{NonAdj}(n)$ be the number of arrangements of $n$ items with $A$ and $B$ forced non-adjacent. Step 1 gives $(n-2)!$ ways, and step 2 gives $P_{n-1}^2$ ways, so by the product rule:

$$\text{NonAdj}(n) = (n - 2)! \times P_{n-1}^2$$

### Cross-check via the complement

You can also get this by subtracting the "must be adjacent" count (Section 1) from the total number of unrestricted arrangements:

$$\text{NonAdj}(n) = n! - \text{Adj}(n)$$

Both formulas should always agree — this is a good way to catch an arithmetic mistake.

## 3. Reading Example: Two Friends Sit Together

6 friends, including Amy and Ben, sit in a row of 6 chairs. In how many ways can they sit if Amy and Ben must sit next to each other?

Glue Amy and Ben into one block. Now there are effectively $6 - 1 = 5$ items to arrange (the block plus the other 4 people):

$$5! \times 2! = 120 \times 2 = 240$$

## 4. Reading Example: Two Rivals Never Sit Together

Same 6 friends, but now Cara and Dan (two rivals) must **not** sit next to each other. How many valid seatings are there?

**Method 1 — gap method.** Arrange the other 4 people first: $4! = 24$ ways. This creates $4 + 1 = 5$ gaps. Place Cara and Dan into 2 different gaps, in order: $P_5^2 = 20$.

$$24 \times 20 = 480$$

**Method 2 — complement.** Total unrestricted arrangements: $6! = 720$. Arrangements with Cara and Dan forced together: $5! \times 2! = 240$.

$$720 - 240 = 480$$

Both methods agree: **480**.

## 5. Reading Example: No Two of a Group of Three Adjacent

5 books, including 3 specific "small" books, are placed on a shelf in a row. In how many ways can they be arranged so that **no two** of the 3 small books are next to each other?

Extend the gap method: arrange the other $5 - 3 = 2$ books first ($2! = 2$ ways), which creates $2 + 1 = 3$ gaps. We need to place all 3 small books into 3 *different* gaps (one per gap, since there are exactly 3 gaps and 3 books), in order — that is $P_3^3 = 3! = 6$ ways.

$$2! \times P_3^3 = 2 \times 6 = 12$$

**Non-obvious detail:** the gap method only works cleanly when the number of items being separated is no more than the number of gaps available. If you needed to separate more items than there are gaps, it would be impossible for all of them to be pairwise non-adjacent, and the count would be `0`.

## 6. Reading Example: Adjacency Around a Circular Table

6 people, including Eve and Finn, sit around a circular table (rotations equivalent). In how many ways can they sit if Eve and Finn must sit next to each other?

Glue Eve and Finn into a block. Now there are $6 - 1 = 5$ "items" around the circle, so the circular-arrangement formula from Lesson 2 gives $(5 - 1)! = 4!$ ways to arrange them around the table, times $2!$ for the order inside the block:

$$4! \times 2! = 24 \times 2 = 48$$

**Non-obvious detail:** for circular problems, the item count used in $(n - 1)!$ already accounts for one rotation being "used up," so always glue *first*, then apply the circular formula to the reduced count — do not apply $(n-1)!$ to the original $n$ and then try to glue afterward.

## 7. Class Practice 1: Photo Line-Up

### Problem

5 classmates, including Jin and Kai, stand in a row for a photo. In how many ways can they stand if Jin and Kai must stand next to each other?

### Answer Choices

(A) 24  (B) 48  (C) 60  (D) 120  (E) 240

### Solution

Glue Jin and Kai into one block: $5 - 1 = 4$ items to arrange.

$$4! \times 2! = 24 \times 2 = 48$$

The answer is **(B) 48**.

## 8. Class Practice 2: Avoiding Neighbors

### Problem

7 people sit in a row of 7 chairs. Two of them, Lena and Omar, refuse to sit next to each other. How many valid seatings are there?

### Answer Choices

(A) 720  (B) 1,440  (C) 3,600  (D) 4,320  (E) 5,040

### Solution

Total unrestricted arrangements: $7! = 5{,}040$. Arrangements with Lena and Omar forced together: $6! \times 2! = 720 \times 2 = 1{,}440$.

$$5{,}040 - 1{,}440 = 3{,}600$$

The answer is **(C) 3,600**.

## 9. Class Practice 3: Three Reserved Seats

### Problem

6 people, including a group of 3 friends, sit in a row of 6 chairs. How many arrangements have no two of the 3 friends sitting next to each other?

### Answer Choices

(A) 12  (B) 36  (C) 72  (D) 144  (E) 720

### Solution

Arrange the other $6 - 3 = 3$ people first: $3! = 6$ ways, creating $3 + 1 = 4$ gaps. Place the 3 friends into 3 of the 4 gaps (order matters, one friend per chosen gap): $P_4^3 = 4 \times 3 \times 2 = 24$.

$$3! \times P_4^3 = 6 \times 24 = 144$$

The answer is **(D) 144**.

## 10. Common Mistakes

### 10.1 Forgetting the internal arrangement factor

Gluing A and B into a block reduces the item count correctly, but forgetting to multiply by $2!$ (or $k!$ for a larger block) undercounts by exactly that factor.

### 10.2 Miscounting the number of gaps

With $m$ other items arranged in a row, there are $m + 1$ gaps, not $m$. This off-by-one is the most common gap-method error.

### 10.3 Using the linear gap count in a circular problem

A circular table with $m$ other people seated has exactly $m$ gaps (the seats "wrap around," so there is no separate "before the first" and "after the last" gap) — not $m + 1$.

### 10.4 Applying the gap method when items outnumber gaps

If you need to place more mutually non-adjacent items than there are available gaps, the answer is $0$ — always check $(\text{items to separate}) \le (\text{number of gaps})$ before computing.

## 11. Key Takeaways

- "Must be adjacent" → bundling method: glue into one block, arrange $(n - 1)$ items, multiply by the block's internal arrangements.
- "Must not be adjacent" → gap method: arrange the rest first, then insert the restricted items into distinct gaps; or use the complement (total minus "must be adjacent").
- Circular versions glue first, then apply $(n - 1)!$ to the reduced item count; circular gap counts equal the number of already-seated people, not that number plus one.
- Always sanity-check a "must not be adjacent" answer against the complement method.

Next lesson: [05-stars-and-bars.md](./05-stars-and-bars.md) moves from arranging *distinct* items to distributing *identical* items — a very different kind of counting problem.
