# Practice Set 1 Solutions

Answer key and full worked solutions for [08-practice-set-1-foundations.md](./08-practice-set-1-foundations.md). Try every problem first — checking the key or opening a solution before attempting a problem defeats the point of a drill set.

## Answer Key

| Problem | Answer | Problem | Answer |
|---|---|---|---|
| 1 | (A) 90 | 11 | (A) 81 |
| 2 | (B) 22 | 12 | (B) 23 |
| 3 | (C) 23 | 13 | (C) 35 |
| 4 | (D) 43 | 14 | (D) 51 |
| 5 | (E) 504 | 15 | (E) 5,040 |
| 6 | (A) 792 | 16 | (A) 1,365 |
| 7 | (B) 34,650 | 17 | (B) 210 |
| 8 | (C) 720 | 18 | (C) 60 |
| 9 | (D) 5,775 | 19 | (D) 210 |
| 10 | (E) 1,800 | 20 | (E) 456 |

## Full Solutions

### Problem 1: Restaurant Combos

<details>
<summary>Solution</summary>

Every meal needs an appetizer **and** a main **and** a dessert — three sequential, independent choices, so multiply:

$$6 \times 5 \times 3 = 90$$

The answer is **(A) 90**.

</details>

### Problem 2: Routes Between Towns

<details>
<summary>Solution</summary>

Every route goes through R **or** S, never both (mutually exclusive) — add the two cases. Within each case, the two legs must both happen — multiply.

$$\text{through R: } 3 \times 4 = 12, \qquad \text{through S: } 2 \times 5 = 10$$

$$12 + 10 = 22$$

The answer is **(B) 22**.

</details>

### Problem 3: Divisible by 6 or by 8

<details>
<summary>Solution</summary>

$$
\begin{aligned}
\text{div by } 6:\ & \lfloor 90/6 \rfloor = 15 \\
\text{div by } 8:\ & \lfloor 90/8 \rfloor = 11 \\
\text{div by } \text{lcm}(6,8)=24:\ & \lfloor 90/24 \rfloor = 3
\end{aligned}
$$

$$15 + 11 - 3 = 23$$

The answer is **(C) 23**.

</details>

### Problem 4: Three Overlapping Interests

<details>
<summary>Solution</summary>

$$(28 + 26 + 20) - (15 + 10 + 12) + 6 = 74 - 37 + 6 = 43$$

The answer is **(D) 43**.

</details>

### Problem 5: Electing Officers

<details>
<summary>Solution</summary>

Assigning three distinct roles is a permutation, not a combination — swapping two people between roles produces a different outcome.

$$P_9^3 = 9 \times 8 \times 7 = 504$$

The answer is **(E) 504**.

</details>

### Problem 6: Selecting a Jury

<details>
<summary>Solution</summary>

A jury is an unordered group — order doesn't matter, so this is a combination.

$$C_{12}^{5} = \frac{12!}{5! \, 7!} = 792$$

The answer is **(A) 792**.

</details>

### Problem 7: Arranging MISSISSIPPI

<details>
<summary>Solution</summary>

`MISSISSIPPI` has 11 letters: `M` (1), `I` (4), `S` (4), `P` (2).

$$\frac{11!}{1! \, 4! \, 4! \, 2!} = \frac{39{,}916{,}800}{1{,}152} = 34{,}650$$

The answer is **(B) 34,650**.

</details>

### Problem 8: Charm Bracelet

<details>
<summary>Solution</summary>

Circular arrangements of $n$ distinct items (rotations equivalent, reflections **not** merged) count $(n-1)!$:

$$(7-1)! = 6! = 720$$

The answer is **(C) 720**.

</details>

### Problem 9: Splitting Into Equal Study Groups

<details>
<summary>Solution</summary>

First split 12 students into 3 *labeled* groups of 4:

$$\frac{12!}{4! \, 4! \, 4!} = 34{,}650$$

Since the 3 groups are actually unlabeled and equal-sized, this overcounts every split by the $3! = 6$ ways to relabel the groups:

$$\frac{34{,}650}{3!} = \frac{34{,}650}{6} = 5{,}775$$

The answer is **(D) 5,775**.

</details>

### Problem 10: Mixed Committee, Then Roles

<details>
<summary>Solution</summary>

Forming the team is a combination in two independent parts (multiply):

$$C_6^2 \times C_5^2 = 15 \times 10 = 150$$

Assigning captain and co-captain from the 4 team members is a permutation:

$$P_4^2 = 4 \times 3 = 12$$

Both stages must happen, so multiply:

$$150 \times 12 = 1{,}800$$

The answer is **(E) 1,800**.

</details>

### Problem 11: Survey Form Combinations

<details>
<summary>Solution</summary>

Every one of the 4 questions must be answered, and the answer to one question doesn't restrict the others — multiply:

$$3^4 = 81$$

((E) $243 = 3^5$ uses one factor too many.)

The answer is **(A) 81**.

</details>

### Problem 12: Three-Hub Routes

<details>
<summary>Solution</summary>

Every route uses exactly one hub (mutually exclusive cases) — add the three cases. Within each case, both legs must happen — multiply.

$$2\times3 + 4\times2 + 3\times3 = 6 + 8 + 9 = 23$$

The answer is **(B) 23**.

</details>

### Problem 13: Divisible by 5 or by 9

<details>
<summary>Solution</summary>

$$
\begin{aligned}
\text{div by } 5:\ & \lfloor 120/5 \rfloor = 24 \\
\text{div by } 9:\ & \lfloor 120/9 \rfloor = 13 \\
\text{div by } \text{lcm}(5,9)=45:\ & \lfloor 120/45 \rfloor = 2
\end{aligned}
$$

$$24 + 13 - 2 = 35$$

The answer is **(C) 35**.

</details>

### Problem 14: Three Overlapping Languages

<details>
<summary>Solution</summary>

$$(32 + 28 + 25) - (15 + 12 + 14) + 7 = 85 - 41 + 7 = 51$$

The answer is **(D) 51**.

</details>

### Problem 15: Choosing and Ordering Books

<details>
<summary>Solution</summary>

Order matters (which book is leftmost vs. rightmost is a different outcome), so this is a permutation:

$$P_{10}^4 = 10 \times 9 \times 8 \times 7 = 5{,}040$$

The answer is **(E) 5,040**.

</details>

### Problem 16: Committee of Four

<details>
<summary>Solution</summary>

An unordered selection — a combination:

$$C_{15}^4 = \frac{15!}{4! \, 11!} = 1{,}365$$

The answer is **(A) 1,365**.

</details>

### Problem 17: Arranging ALABAMA

<details>
<summary>Solution</summary>

`ALABAMA` has 7 letters: `A` (4), `L` (1), `B` (1), `M` (1).

$$\frac{7!}{4!} = \frac{5{,}040}{24} = 210$$

The answer is **(B) 210**.

</details>

### Problem 18: Holding Hands in a Circle

<details>
<summary>Solution</summary>

Circular arrangements of 6 distinct people, ignoring rotation, number $(6-1)! = 120$. Since reflections are also treated as the same arrangement here, divide by an additional factor of 2:

$$\frac{(6-1)!}{2} = \frac{120}{2} = 60$$

The answer is **(C) 60**.

</details>

### Problem 19: Splitting Into Unequal Groups

<details>
<summary>Solution</summary>

Choosing which 6 students form the size-6 group automatically determines the size-4 group, and since the two groups have different sizes, neither can be confused with the other — no overcounting, so no division is needed:

$$C_{10}^6 = C_{10}^4 = 210$$

The answer is **(D) 210**.

</details>

### Problem 20: Committee With At Least One Woman

<details>
<summary>Solution</summary>

It's easier to count the complement: committees with **no** women (all 5 members are men) and subtract from the total.

$$C_{11}^5 = 462, \qquad C_6^5 = 6$$

$$462 - 6 = 456$$

The answer is **(E) 456**.

</details>

Back to [08-practice-set-1-foundations.md](./08-practice-set-1-foundations.md). Next: [09-practice-set-2-twisted-models.md](./09-practice-set-2-twisted-models.md).
