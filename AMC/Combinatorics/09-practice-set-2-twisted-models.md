# Practice Set 2: Twisted Models — Adjacency Constraints & Stars and Bars

This set drills the two "special model" lessons: [04-adjacency-constraints.md](./04-adjacency-constraints.md) (bundling and gap methods for arrangements) and [05-stars-and-bars.md](./05-stars-and-bars.md) (distributing identical items). Both lessons take the basic tools from Set 1 and twist them into a new shape — the goal here is recognizing *which* twisted model a problem is hiding, not just running a formula.

## How to Use This Set

Before computing, name the model out loud: "must be adjacent" (bundle), "must not be adjacent" (gap or complement), "not all $k$ together" (complement of the full bundle only), or "distribute identical items" (stars and bars, then check for a minimum/maximum). Mixing these up is the main way these problems go wrong. For a quick self-check, see the answer-only key in [11-practice-set-answer-keys.md](./11-practice-set-answer-keys.md).

## Problem 1: Two Friends Together

### Problem

7 friends, including Mia and Noah, stand in a row for a photo. In how many ways can they stand if Mia and Noah must stand next to each other?

### Answer Choices

(A) 1,440  (B) 1,680  (C) 2,520  (D) 5,040  (E) 10,080

<details>
<summary>Solution</summary>

Glue Mia and Noah into one block: $7 - 1 = 6$ items to arrange, times $2!$ for their internal order.

$$6! \times 2! = 720 \times 2 = 1{,}440$$

The answer is **(A) 1,440**.

</details>

## Problem 2: Two Rivals Apart

### Problem

8 people sit in a row of 8 chairs. Two of them, Priya and Quinn, refuse to sit next to each other. How many valid seatings are there?

### Answer Choices

(A) 10,080  (B) 30,240  (C) 33,600  (D) 35,280  (E) 40,320

<details>
<summary>Solution</summary>

Total unrestricted arrangements: $8! = 40{,}320$. Arrangements with Priya and Quinn forced together: $7! \times 2! = 5{,}040 \times 2 = 10{,}080$.

$$40{,}320 - 10{,}080 = 30{,}240$$

The answer is **(B) 30,240**.

</details>

## Problem 3: No Two of Three Rare Books Adjacent

### Problem

7 books, including 3 specific "rare" books, are placed on a shelf in a row. In how many ways can they be arranged so that no two of the 3 rare books are next to each other?

### Answer Choices

(A) 720  (B) 1,080  (C) 1,440  (D) 1,800  (E) 2,160

<details>
<summary>Solution</summary>

Arrange the other $7 - 3 = 4$ books first: $4! = 24$ ways, creating $4 + 1 = 5$ gaps. Place all 3 rare books into 3 different gaps, in order: $P_5^3 = 5 \times 4 \times 3 = 60$.

$$24 \times 60 = 1{,}440$$

The answer is **(C) 1,440**.

</details>

## Problem 4: Not All Three Together

### Problem

8 people, including Amy, Ben, and Cara, sit in a row of 8 chairs. In how many ways can they sit if Amy, Ben, and Cara are **not** allowed to all sit together (but any two of the three may still be adjacent)?

### Answer Choices

(A) 4,320  (B) 24,000  (C) 30,240  (D) 36,000  (E) 38,880

<details>
<summary>Solution</summary>

"Not all three together" only forbids the single case where all three form one contiguous block — this is the complement of the fully-bundled count, not a gap-method problem.

Total unrestricted arrangements: $8! = 40{,}320$. Bundle all three into one block: $8 - 3 + 1 = 6$ items to arrange, times $3!$ for internal order.

$$6! \times 3! = 720 \times 6 = 4{,}320$$

$$40{,}320 - 4{,}320 = 36{,}000$$

The answer is **(D) 36,000**.

</details>

## Problem 5: Circular Table, Two Rivals

### Problem

8 people sit around a circular table (rotations equivalent). Two of them, Eve and Finn, must **not** sit next to each other. How many valid seatings are there?

### Answer Choices

(A) 720  (B) 1,440  (C) 2,160  (D) 2,880  (E) 3,600

<details>
<summary>Solution</summary>

Total circular arrangements: $(8-1)! = 7! = 5{,}040$. Glue Eve and Finn: $8 - 1 = 7$ items around the circle, so $(7-1)! \times 2! = 720 \times 2 = 1{,}440$ arrangements have them together.

$$5{,}040 - 1{,}440 = 3{,}600$$

The answer is **(E) 3,600**.

</details>

## Problem 6: Marbles Into Jars

### Problem

How many ways can 15 identical marbles be distributed among 4 distinct jars, if a jar may be empty?

### Answer Choices

(A) 816  (B) 900  (C) 969  (D) 1,140  (E) 1,365

<details>
<summary>Solution</summary>

Nonnegative integer solutions to $x_1+x_2+x_3+x_4=15$:

$$C_{15+4-1}^{4-1} = C_{18}^{3} = 816$$

The answer is **(A) 816**.

</details>

## Problem 7: Candies With a Minimum

### Problem

How many ways can 18 identical candies be distributed among 5 kids, if every kid must get at least 2 candies?

### Answer Choices

(A) 330  (B) 495  (C) 560  (D) 680  (E) 792

<details>
<summary>Solution</summary>

Give each kid 2 candies up front ($2 \times 5 = 10$ used), leaving $18 - 10 = 8$ to distribute freely among 5 kids.

$$C_{8+5-1}^{5-1} = C_{12}^{4} = 495$$

The answer is **(B) 495**.

</details>

## Problem 8: Candies With a Maximum

### Problem

How many ways can 10 identical candies be distributed among 3 kids, if no kid may receive more than 6 candies?

### Answer Choices

(A) 27  (B) 30  (C) 36  (D) 42  (E) 45

<details>
<summary>Solution</summary>

Unrestricted count: $C_{10+3-1}^{3-1} = C_{12}^{2} = 66$.

Now subtract the invalid cases where some kid gets 7 or more: give that kid 7 candies first, leaving $10 - 7 = 3$ to distribute freely among the same 3 kids: $C_{3+3-1}^{3-1} = C_5^2 = 10$ ways. Since $10 < 7 + 7 = 14$, no two kids can simultaneously exceed the limit, so there's no overlap to correct for. With 3 choices for which kid exceeds the limit:

$$66 - 3 \times 10 = 66 - 30 = 36$$

The answer is **(C) 36**.

</details>

## Problem 9: Choosing Cookies With Repetition

### Problem

A bakery sells 6 types of cookies. Mateo wants to buy a box of 10 cookies, and may choose more than one of the same type. How many different boxes are possible?

### Answer Choices

(A) 1,001  (B) 2,002  (C) 3,003  (D) 5,005  (E) 8,008

<details>
<summary>Solution</summary>

This is choosing 10 items with repetition from 6 types — $H_6^{10}$:

$$H_6^{10} = C_{10+6-1}^{10} = C_{15}^{10} = C_{15}^{5} = 3{,}003$$

The answer is **(C) 3,003**.

</details>

## Problem 10: A Fixed-Order Block of Three

### Problem

9 people sit in a row. Three specific friends, Ana, Bo, and Chen, must sit together **and in that exact order** (Ana immediately followed by Bo, immediately followed by Chen). In how many ways can the 9 people be seated?

### Answer Choices

(A) 720  (B) 1,440  (C) 2,520  (D) 3,600  (E) 5,040

<details>
<summary>Solution</summary>

Gluing the three friends into a fixed-order block reduces the item count by $3 - 1 = 2$: $9 - 2 = 7$ items to arrange. Since the internal order is pinned down (only "Ana-Bo-Chen," not any of the other $3! - 1$ orders), the block contributes a factor of $1$, not $3!$.

$$7! \times 1 = 5{,}040$$

The answer is **(E) 5,040**.

</details>

## Problem 11: Two Rivals, Smaller Row

### Problem

6 people sit in a row of 6 chairs. Two of them, Ravi and Sam, refuse to sit next to each other. How many valid seatings are there?

### Answer Choices

(A) 480  (B) 540  (C) 600  (D) 660  (E) 720

<details>
<summary>Solution</summary>

Total: $6! = 720$. Bundled together: $5! \times 2! = 120 \times 2 = 240$.

$$720 - 240 = 480$$

The answer is **(A) 480**.

</details>

## Problem 12: No Two of Four Special Items Adjacent

### Problem

9 items are arranged in a row, including 4 specific "special" items. In how many ways can they be arranged so that no two of the 4 special items are adjacent?

### Answer Choices

(A) 21,600  (B) 43,200  (C) 51,840  (D) 64,800  (E) 86,400

<details>
<summary>Solution</summary>

Arrange the other $9 - 4 = 5$ items first: $5! = 120$ ways, creating $5 + 1 = 6$ gaps. Place all 4 special items into 4 distinct gaps, in order: $P_6^4 = 6 \times 5 \times 4 \times 3 = 360$.

$$120 \times 360 = 43{,}200$$

The answer is **(B) 43,200**.

</details>

## Problem 13: Not All Four Friends Together

### Problem

9 people, including a group of 4 friends, sit in a row of 9 chairs. In how many ways can they sit if the 4 friends are **not** allowed to all sit together (but smaller subgroups of them may still be adjacent)?

### Answer Choices

(A) 308,880  (B) 327,600  (C) 345,600  (D) 354,240  (E) 362,880

<details>
<summary>Solution</summary>

Total: $9! = 362{,}880$. Bundle all 4 friends: $9 - 4 + 1 = 6$ items, times $4!$ for internal order.

$$6! \times 4! = 720 \times 24 = 17{,}280$$

$$362{,}880 - 17{,}280 = 345{,}600$$

((E) $362{,}880$ is the unrestricted total — a reminder that this restriction is not a gap-method problem, and skipping the subtraction entirely just gives back the total.)

The answer is **(C) 345,600**.

</details>

## Problem 14: Circular Table, Two Friends Together

### Problem

7 people sit around a circular table (rotations equivalent). Two of them, Tom and Uma, must sit next to each other. In how many ways can they sit?

### Answer Choices

(A) 72  (B) 96  (C) 120  (D) 240  (E) 720

<details>
<summary>Solution</summary>

Glue Tom and Uma: $7 - 1 = 6$ items around the circle, so $(6-1)!$ arrangements, times $2!$ for internal order.

$$(6-1)! \times 2! = 120 \times 2 = 240$$

The answer is **(D) 240**.

</details>

## Problem 15: Circular Table, Larger Group Apart

### Problem

9 people sit around a circular table (rotations equivalent). Two of them, Vik and Wren, must **not** sit next to each other. How many valid seatings are there?

### Answer Choices

(A) 10,080  (B) 15,120  (C) 20,160  (D) 25,200  (E) 30,240

<details>
<summary>Solution</summary>

Total circular arrangements: $(9-1)! = 8! = 40{,}320$. Glue Vik and Wren: $9 - 1 = 8$ items around the circle, so $(8-1)! \times 2! = 5{,}040 \times 2 = 10{,}080$ arrangements have them together.

$$40{,}320 - 10{,}080 = 30{,}240$$

The answer is **(E) 30,240**.

</details>

## Problem 16: Pencils to Students

### Problem

How many ways can 20 identical pencils be distributed among 6 distinct students, if a student may receive none?

### Answer Choices

(A) 53,130  (B) 54,264  (C) 58,905  (D) 65,780  (E) 77,520

<details>
<summary>Solution</summary>

Nonnegative integer solutions to $x_1 + \cdots + x_6 = 20$:

$$C_{20+6-1}^{6-1} = C_{25}^{5} = 53{,}130$$

The answer is **(A) 53,130**.

</details>

## Problem 17: Chocolates With a Minimum

### Problem

How many ways can 24 identical chocolates be distributed among 6 kids, if every kid must get at least 3?

### Answer Choices

(A) 252  (B) 462  (C) 495  (D) 539  (E) 792

<details>
<summary>Solution</summary>

Give each kid 3 chocolates up front ($3 \times 6 = 18$ used), leaving $24 - 18 = 6$ to distribute freely among 6 kids.

$$C_{6+6-1}^{6-1} = C_{11}^{5} = 462$$

The answer is **(B) 462**.

</details>

## Problem 18: Marbles With a Larger Minimum

### Problem

How many ways can 30 identical marbles be distributed among 5 jars, if every jar must contain at least 4 marbles?

### Answer Choices

(A) 715  (B) 840  (C) 1,001  (D) 1,365  (E) 1,820

<details>
<summary>Solution</summary>

Give each jar 4 marbles up front ($4 \times 5 = 20$ used), leaving $30 - 20 = 10$ to distribute freely among 5 jars.

$$C_{10+5-1}^{5-1} = C_{14}^{4} = 1{,}001$$

The answer is **(C) 1,001**.

</details>

## Problem 19: A Maximum That Two Kids Can Simultaneously Hit

### Problem

How many ways can 12 identical candies be distributed among 4 kids, if no kid may receive more than 5 candies?

### Answer Choices

(A) 84  (B) 99  (C) 112  (D) 125  (E) 140

<details>
<summary>Solution</summary>

Unrestricted count: $C_{12+4-1}^{4-1} = C_{15}^{3} = 455$.

Subtract cases where some kid gets 6 or more: give that kid 6 up front, leaving $12-6=6$ among 4 kids: $C_{6+4-1}^{4-1} = C_9^3 = 84$ ways; times 4 kids: $336$.

**Non-obvious detail:** here $12 = 6 + 6$, so unlike the "maximum" problem in [05-stars-and-bars.md](./05-stars-and-bars.md), *two* kids **can** simultaneously exceed the limit (each getting exactly 6, the other two getting 0), so a single subtraction double-counts those cases. Add them back: give two specific kids 6 each up front, leaving $12 - 12 = 0$ among all 4 kids: $C_{0+4-1}^{4-1} = C_3^3 = 1$ way; times $C_4^2 = 6$ pairs of kids: $6$.

$$455 - 336 + 6 = 125$$

The answer is **(D) 125**.

</details>

## Problem 20: Ice Cream With Repetition

### Problem

An ice cream shop offers 5 flavors. Sofia orders a cone with 6 scoops, and may repeat flavors (the order of scoops on the cone doesn't matter). How many different cones are possible?

### Answer Choices

(A) 56  (B) 84  (C) 126  (D) 168  (E) 210

<details>
<summary>Solution</summary>

Choosing 6 scoops with repetition from 5 flavors is $H_5^6$:

$$H_5^6 = C_{6+5-1}^{6} = C_{10}^{6} = C_{10}^{4} = 210$$

The answer is **(E) 210**.

</details>

## Key Reminders

- Bundling glues items together and shrinks the item count by (block size − 1); the block's internal arrangements multiply back in — unless a specific internal order is required, in which case that factor is $1$.
- The gap method works for "no two adjacent" — but "not all $k$ together" needs the complement of the full bundle instead, since partial adjacency is still allowed.
- Circular versions glue first, *then* apply $(n-1)!$ to the reduced count; circular gaps equal the number of already-seated people, not that number plus one.
- Stars and bars needs identical items and distinct boxes. A minimum shifts the total down before applying the formula; a maximum needs inclusion–exclusion layered on top.
- Before trusting a single subtraction on a "maximum" problem, check whether two restricted items can *simultaneously* exceed the limit — if the total is small enough, they can, and you need to add the double-counted overlap back (Problem 19).

Next: [10-practice-set-3-recursive-methods.md](./10-practice-set-3-recursive-methods.md) drills the recursive-counting method and the balls-into-buckets framework from Lessons 06–07.
