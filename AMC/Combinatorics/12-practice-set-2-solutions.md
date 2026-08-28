# Practice Set 2 Solutions
*AMC / Combinatorics*

Answer key and full worked solutions for [09-practice-set-2-twisted-models.md](./09-practice-set-2-twisted-models.md). Try every problem first — checking the key or opening a solution before attempting a problem defeats the point of a drill set.

## Answer Key

| Problem | Answer | Problem | Answer |
|---|---|---|---|
| 1 | (A) 1,440 | 11 | (A) 480 |
| 2 | (B) 30,240 | 12 | (B) 43,200 |
| 3 | (C) 1,440 | 13 | (C) 345,600 |
| 4 | (D) 36,000 | 14 | (D) 240 |
| 5 | (E) 3,600 | 15 | (E) 30,240 |
| 6 | (A) 816 | 16 | (A) 53,130 |
| 7 | (B) 495 | 17 | (B) 462 |
| 8 | (C) 36 | 18 | (C) 1,001 |
| 9 | (D) 3,003 | 19 | (D) 125 |
| 10 | (E) 5,040 | 20 | (E) 210 |

## Full Solutions

### Problem 1: Two Friends Together

<details>
<summary>Solution</summary>

Glue Mia and Noah into one block: $7 - 1 = 6$ items to arrange, times $2!$ for their internal order.

$$6! \times 2! = 720 \times 2 = 1{,}440$$

The answer is **(A) 1,440**.

</details>

### Problem 2: Two Rivals Apart

<details>
<summary>Solution</summary>

Total unrestricted arrangements: $8! = 40{,}320$. Arrangements with Priya and Quinn forced together: $7! \times 2! = 5{,}040 \times 2 = 10{,}080$.

$$40{,}320 - 10{,}080 = 30{,}240$$

The answer is **(B) 30,240**.

</details>

### Problem 3: No Two of Three Rare Books Adjacent

<details>
<summary>Solution</summary>

Arrange the other $7 - 3 = 4$ books first: $4! = 24$ ways, creating $4 + 1 = 5$ gaps. Place all 3 rare books into 3 different gaps, in order: $P_5^3 = 5 \times 4 \times 3 = 60$.

$$24 \times 60 = 1{,}440$$

The answer is **(C) 1,440**.

</details>

### Problem 4: Not All Three Together

<details>
<summary>Solution</summary>

"Not all three together" only forbids the single case where all three form one contiguous block — this is the complement of the fully-bundled count, not a gap-method problem.

Total unrestricted arrangements: $8! = 40{,}320$. Bundle all three into one block: $8 - 3 + 1 = 6$ items to arrange, times $3!$ for internal order.

$$6! \times 3! = 720 \times 6 = 4{,}320$$

$$40{,}320 - 4{,}320 = 36{,}000$$

The answer is **(D) 36,000**.

</details>

### Problem 5: Circular Table, Two Rivals

<details>
<summary>Solution</summary>

Total circular arrangements: $(8-1)! = 7! = 5{,}040$. Glue Eve and Finn: $8 - 1 = 7$ items around the circle, so $(7-1)! \times 2! = 720 \times 2 = 1{,}440$ arrangements have them together.

$$5{,}040 - 1{,}440 = 3{,}600$$

The answer is **(E) 3,600**.

</details>

### Problem 6: Marbles Into Jars

<details>
<summary>Solution</summary>

Nonnegative integer solutions to $x_1+x_2+x_3+x_4=15$:

$$C_{15+4-1}^{4-1} = C_{18}^{3} = 816$$

The answer is **(A) 816**.

</details>

### Problem 7: Candies With a Minimum

<details>
<summary>Solution</summary>

Give each kid 2 candies up front ($2 \times 5 = 10$ used), leaving $18 - 10 = 8$ to distribute freely among 5 kids.

$$C_{8+5-1}^{5-1} = C_{12}^{4} = 495$$

The answer is **(B) 495**.

</details>

### Problem 8: Candies With a Maximum

<details>
<summary>Solution</summary>

Unrestricted count: $C_{10+3-1}^{3-1} = C_{12}^{2} = 66$.

Now subtract the invalid cases where some kid gets 7 or more: give that kid 7 candies first, leaving $10 - 7 = 3$ to distribute freely among the same 3 kids: $C_{3+3-1}^{3-1} = C_5^2 = 10$ ways. Since $10 < 7 + 7 = 14$, no two kids can simultaneously exceed the limit, so there's no overlap to correct for. With 3 choices for which kid exceeds the limit:

$$66 - 3 \times 10 = 66 - 30 = 36$$

The answer is **(C) 36**.

</details>

### Problem 9: Choosing Cookies With Repetition

<details>
<summary>Solution</summary>

This is choosing 10 items with repetition from 6 types — $H_6^{10}$:

$$H_6^{10} = C_{10+6-1}^{10} = C_{15}^{10} = C_{15}^{5} = 3{,}003$$

The answer is **(C) 3,003**.

</details>

### Problem 10: A Fixed-Order Block of Three

<details>
<summary>Solution</summary>

Gluing the three friends into a fixed-order block reduces the item count by $3 - 1 = 2$: $9 - 2 = 7$ items to arrange. Since the internal order is pinned down (only "Ana-Bo-Chen," not any of the other $3! - 1$ orders), the block contributes a factor of $1$, not $3!$.

$$7! \times 1 = 5{,}040$$

The answer is **(E) 5,040**.

</details>

### Problem 11: Two Rivals, Smaller Row

<details>
<summary>Solution</summary>

Total: $6! = 720$. Bundled together: $5! \times 2! = 120 \times 2 = 240$.

$$720 - 240 = 480$$

The answer is **(A) 480**.

</details>

### Problem 12: No Two of Four Special Items Adjacent

<details>
<summary>Solution</summary>

Arrange the other $9 - 4 = 5$ items first: $5! = 120$ ways, creating $5 + 1 = 6$ gaps. Place all 4 special items into 4 distinct gaps, in order: $P_6^4 = 6 \times 5 \times 4 \times 3 = 360$.

$$120 \times 360 = 43{,}200$$

The answer is **(B) 43,200**.

</details>

### Problem 13: Not All Four Friends Together

<details>
<summary>Solution</summary>

Total: $9! = 362{,}880$. Bundle all 4 friends: $9 - 4 + 1 = 6$ items, times $4!$ for internal order.

$$6! \times 4! = 720 \times 24 = 17{,}280$$

$$362{,}880 - 17{,}280 = 345{,}600$$

((E) $362{,}880$ is the unrestricted total — a reminder that this restriction is not a gap-method problem, and skipping the subtraction entirely just gives back the total.)

The answer is **(C) 345,600**.

</details>

### Problem 14: Circular Table, Two Friends Together

<details>
<summary>Solution</summary>

Glue Tom and Uma: $7 - 1 = 6$ items around the circle, so $(6-1)!$ arrangements, times $2!$ for internal order.

$$(6-1)! \times 2! = 120 \times 2 = 240$$

The answer is **(D) 240**.

</details>

### Problem 15: Circular Table, Larger Group Apart

<details>
<summary>Solution</summary>

Total circular arrangements: $(9-1)! = 8! = 40{,}320$. Glue Vik and Wren: $9 - 1 = 8$ items around the circle, so $(8-1)! \times 2! = 5{,}040 \times 2 = 10{,}080$ arrangements have them together.

$$40{,}320 - 10{,}080 = 30{,}240$$

The answer is **(E) 30,240**.

</details>

### Problem 16: Pencils to Students

<details>
<summary>Solution</summary>

Nonnegative integer solutions to $x_1 + \cdots + x_6 = 20$:

$$C_{20+6-1}^{6-1} = C_{25}^{5} = 53{,}130$$

The answer is **(A) 53,130**.

</details>

### Problem 17: Chocolates With a Minimum

<details>
<summary>Solution</summary>

Give each kid 3 chocolates up front ($3 \times 6 = 18$ used), leaving $24 - 18 = 6$ to distribute freely among 6 kids.

$$C_{6+6-1}^{6-1} = C_{11}^{5} = 462$$

The answer is **(B) 462**.

</details>

### Problem 18: Marbles With a Larger Minimum

<details>
<summary>Solution</summary>

Give each jar 4 marbles up front ($4 \times 5 = 20$ used), leaving $30 - 20 = 10$ to distribute freely among 5 jars.

$$C_{10+5-1}^{5-1} = C_{14}^{4} = 1{,}001$$

The answer is **(C) 1,001**.

</details>

### Problem 19: A Maximum That Two Kids Can Simultaneously Hit

<details>
<summary>Solution</summary>

Unrestricted count: $C_{12+4-1}^{4-1} = C_{15}^{3} = 455$.

Subtract cases where some kid gets 6 or more: give that kid 6 up front, leaving $12-6=6$ among 4 kids: $C_{6+4-1}^{4-1} = C_9^3 = 84$ ways; times 4 kids: $336$.

**Non-obvious detail:** here $12 = 6 + 6$, so unlike the "maximum" problem in [05-stars-and-bars.md](./05-stars-and-bars.md), *two* kids **can** simultaneously exceed the limit (each getting exactly 6, the other two getting 0), so a single subtraction double-counts those cases. Add them back: give two specific kids 6 each up front, leaving $12 - 12 = 0$ among all 4 kids: $C_{0+4-1}^{4-1} = C_3^3 = 1$ way; times $C_4^2 = 6$ pairs of kids: $6$.

$$455 - 336 + 6 = 125$$

The answer is **(D) 125**.

</details>

### Problem 20: Ice Cream With Repetition

<details>
<summary>Solution</summary>

Choosing 6 scoops with repetition from 5 flavors is $H_5^6$:

$$H_5^6 = C_{6+5-1}^{6} = C_{10}^{6} = C_{10}^{4} = 210$$

The answer is **(E) 210**.

</details>

Back to [09-practice-set-2-twisted-models.md](./09-practice-set-2-twisted-models.md). Next: [10-practice-set-3-recursive-methods.md](./10-practice-set-3-recursive-methods.md).
