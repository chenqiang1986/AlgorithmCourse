# Practice Set 1: Foundations — Counting Principles, Inclusion–Exclusion, Permutations & Combinations

This set drills [01-sum-and-product-rules.md](./01-sum-and-product-rules.md), [02-inclusion-exclusion-principle.md](./02-inclusion-exclusion-principle.md), and [03-permutations-and-combinations.md](./03-permutations-and-combinations.md) — the basic toolkit every later lesson builds on. Attempt each problem before opening its solution.

## How to Use This Set

For every problem, first decide *which tool applies* (add vs. multiply, plain addition vs. inclusion–exclusion, permutation vs. combination) before computing anything — misidentifying the tool is the most common source of error at this level, not the arithmetic itself. For a quick self-check without spoiling the full reasoning, see the answer-only key in [11-practice-set-answer-keys.md](./11-practice-set-answer-keys.md); each problem's full worked solution is still collapsed below it.

## Problem 1: Restaurant Combos

### Problem

A restaurant's fixed-price menu has 6 appetizers, 5 main courses, and 3 desserts. A full meal consists of exactly one of each. How many different meals are possible?

### Answer Choices

(A) 90  (B) 108  (C) 120  (D) 150  (E) 180

<details>
<summary>Solution</summary>

Every meal needs an appetizer **and** a main **and** a dessert — three sequential, independent choices, so multiply:

$$6 \times 5 \times 3 = 90$$

The answer is **(A) 90**.

</details>

## Problem 2: Routes Between Towns

### Problem

To travel from town P to town Q, a traveler can go through town R (3 roads P→R, 4 roads R→Q) or through town S (2 roads P→S, 5 roads S→Q). No road connects R and S directly. How many total routes are there from P to Q?

### Answer Choices

(A) 14  (B) 22  (C) 24  (D) 26  (E) 30

<details>
<summary>Solution</summary>

Every route goes through R **or** S, never both (mutually exclusive) — add the two cases. Within each case, the two legs must both happen — multiply.

$$\text{through R: } 3 \times 4 = 12, \qquad \text{through S: } 2 \times 5 = 10$$

$$12 + 10 = 22$$

The answer is **(B) 22**.

</details>

## Problem 3: Divisible by 6 or by 8

### Problem

How many integers from 1 to 90 are divisible by 6 or by 8?

### Answer Choices

(A) 18  (B) 21  (C) 23  (D) 25  (E) 28

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

## Problem 4: Three Overlapping Interests

### Problem

In a survey of 50 students, 28 like math, 26 like science, and 20 like art. 15 like both math and science, 10 like both science and art, and 12 like both math and art. 6 students like all three subjects. How many students like at least one of the three subjects?

### Answer Choices

(A) 33  (B) 37  (C) 40  (D) 43  (E) 46

<details>
<summary>Solution</summary>

$$(28 + 26 + 20) - (15 + 10 + 12) + 6 = 74 - 37 + 6 = 43$$

The answer is **(D) 43**.

</details>

## Problem 5: Electing Officers

### Problem

A club has 9 members. In how many ways can a president, a vice-president, and a secretary be chosen, if no member holds more than one office?

### Answer Choices

(A) 72  (B) 168  (C) 252  (D) 336  (E) 504

<details>
<summary>Solution</summary>

Assigning three distinct roles is a permutation, not a combination — swapping two people between roles produces a different outcome.

$$P_9^3 = 9 \times 8 \times 7 = 504$$

The answer is **(E) 504**.

</details>

## Problem 6: Selecting a Jury

### Problem

A jury of 5 people is to be selected from a pool of 12 candidates, with no distinct roles among jurors. How many different juries are possible?

### Answer Choices

(A) 792  (B) 924  (C) 990  (D) 1,188  (E) 1,584

<details>
<summary>Solution</summary>

A jury is an unordered group — order doesn't matter, so this is a combination.

$$C_{12}^{5} = \frac{12!}{5! \, 7!} = 792$$

The answer is **(A) 792**.

</details>

## Problem 7: Arranging MISSISSIPPI

### Problem

How many distinct ways can the letters of the word `MISSISSIPPI` be arranged?

### Answer Choices

(A) 17,325  (B) 34,650  (C) 69,300  (D) 103,950  (E) 138,600

<details>
<summary>Solution</summary>

`MISSISSIPPI` has 11 letters: `M` (1), `I` (4), `S` (4), `P` (2).

$$\frac{11!}{1! \, 4! \, 4! \, 2!} = \frac{39{,}916{,}800}{1{,}152} = 34{,}650$$

The answer is **(B) 34,650**.

</details>

## Problem 8: Charm Bracelet

### Problem

In how many ways can 7 distinct charms be arranged on a circular bracelet, if rotations are considered the same arrangement but reflections (flipping the bracelet over) are considered **different**?

### Answer Choices

(A) 360  (B) 540  (C) 720  (D) 1,440  (E) 2,520

<details>
<summary>Solution</summary>

Circular arrangements of $n$ distinct items (rotations equivalent, reflections **not** merged) count $(n-1)!$:

$$(7-1)! = 6! = 720$$

The answer is **(C) 720**.

</details>

## Problem 9: Splitting Into Equal Study Groups

### Problem

12 students are split into 3 unlabeled study groups of 4 students each. How many ways can this be done?

### Answer Choices

(A) 1,925  (B) 2,887  (C) 4,620  (D) 5,775  (E) 9,625

<details>
<summary>Solution</summary>

First split 12 students into 3 *labeled* groups of 4:

$$\frac{12!}{4! \, 4! \, 4!} = 34{,}650$$

Since the 3 groups are actually unlabeled and equal-sized, this overcounts every split by the $3! = 6$ ways to relabel the groups:

$$\frac{34{,}650}{3!} = \frac{34{,}650}{6} = 5{,}775$$

The answer is **(D) 5,775**.

</details>

## Problem 10: Mixed Committee, Then Roles

### Problem

A team of 4 is chosen from 6 boys and 5 girls, and must include exactly 2 boys and 2 girls. From that team of 4, a captain and a co-captain (two distinct roles) are then chosen. In how many total ways can this be done?

### Answer Choices

(A) 150  (B) 450  (C) 900  (D) 1,350  (E) 1,800

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

## Problem 11: Survey Form Combinations

### Problem

A survey form has 4 questions; each question has 3 possible answers. How many different completed forms are possible?

### Answer Choices

(A) 81  (B) 108  (C) 144  (D) 162  (E) 243

<details>
<summary>Solution</summary>

Every one of the 4 questions must be answered, and the answer to one question doesn't restrict the others — multiply:

$$3^4 = 81$$

((E) $243 = 3^5$ uses one factor too many.)

The answer is **(A) 81**.

</details>

## Problem 12: Three-Hub Routes

### Problem

To travel from City X to City Y, a traveler can go through Hub A (2 routes X→A, 3 routes A→Y), Hub B (4 routes X→B, 2 routes B→Y), or Hub C (3 routes X→C, 3 routes C→Y). No two hubs are directly connected. How many total routes are there from X to Y?

### Answer Choices

(A) 17  (B) 23  (C) 25  (D) 28  (E) 32

<details>
<summary>Solution</summary>

Every route uses exactly one hub (mutually exclusive cases) — add the three cases. Within each case, both legs must happen — multiply.

$$2\times3 + 4\times2 + 3\times3 = 6 + 8 + 9 = 23$$

The answer is **(B) 23**.

</details>

## Problem 13: Divisible by 5 or by 9

### Problem

How many integers from 1 to 120 are divisible by 5 or by 9?

### Answer Choices

(A) 26  (B) 31  (C) 35  (D) 40  (E) 46

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

## Problem 14: Three Overlapping Languages

### Problem

In a group of 60 people, 32 speak English, 28 speak French, and 25 speak Spanish. 15 speak both English and French, 12 speak both French and Spanish, and 14 speak both English and Spanish. 7 people speak all three languages. How many people speak at least one of the three languages?

### Answer Choices

(A) 38  (B) 42  (C) 47  (D) 51  (E) 55

<details>
<summary>Solution</summary>

$$(32 + 28 + 25) - (15 + 12 + 14) + 7 = 85 - 41 + 7 = 51$$

The answer is **(D) 51**.

</details>

## Problem 15: Choosing and Ordering Books

### Problem

In how many ways can 4 different books be chosen from a set of 10 different books and arranged in order on a shelf?

### Answer Choices

(A) 720  (B) 1,260  (C) 2,520  (D) 3,024  (E) 5,040

<details>
<summary>Solution</summary>

Order matters (which book is leftmost vs. rightmost is a different outcome), so this is a permutation:

$$P_{10}^4 = 10 \times 9 \times 8 \times 7 = 5{,}040$$

The answer is **(E) 5,040**.

</details>

## Problem 16: Committee of Four

### Problem

How many ways can a committee of 4 be chosen from 15 people, with no distinct roles?

### Answer Choices

(A) 1,365  (B) 1,560  (C) 2,002  (D) 3,003  (E) 5,005

<details>
<summary>Solution</summary>

An unordered selection — a combination:

$$C_{15}^4 = \frac{15!}{4! \, 11!} = 1{,}365$$

The answer is **(A) 1,365**.

</details>

## Problem 17: Arranging ALABAMA

### Problem

How many distinct arrangements are there of the letters in the word `ALABAMA`?

### Answer Choices

(A) 105  (B) 210  (C) 315  (D) 420  (E) 840

<details>
<summary>Solution</summary>

`ALABAMA` has 7 letters: `A` (4), `L` (1), `B` (1), `M` (1).

$$\frac{7!}{4!} = \frac{5{,}040}{24} = 210$$

The answer is **(B) 210**.

</details>

## Problem 18: Holding Hands in a Circle

### Problem

In how many distinct ways can 6 people hold hands around a circle, where arrangements that are rotations *or* reflections (mirror images) of each other count as the same arrangement?

### Answer Choices

(A) 30  (B) 48  (C) 60  (D) 72  (E) 90

<details>
<summary>Solution</summary>

Circular arrangements of 6 distinct people, ignoring rotation, number $(6-1)! = 120$. Since reflections are also treated as the same arrangement here, divide by an additional factor of 2:

$$\frac{(6-1)!}{2} = \frac{120}{2} = 60$$

The answer is **(C) 60**.

</details>

## Problem 19: Splitting Into Unequal Groups

### Problem

10 students are split into an unlabeled group of 6 and an unlabeled group of 4. How many ways can this be done?

### Answer Choices

(A) 45  (B) 120  (C) 168  (D) 210  (E) 252

<details>
<summary>Solution</summary>

Choosing which 6 students form the size-6 group automatically determines the size-4 group, and since the two groups have different sizes, neither can be confused with the other — no overcounting, so no division is needed:

$$C_{10}^6 = C_{10}^4 = 210$$

The answer is **(D) 210**.

</details>

## Problem 20: Committee With At Least One Woman

### Problem

A 5-person committee is chosen from 6 men and 5 women. In how many ways can the committee include at least one woman?

### Answer Choices

(A) 252  (B) 330  (C) 420  (D) 450  (E) 456

<details>
<summary>Solution</summary>

It's easier to count the complement: committees with **no** women (all 5 members are men) and subtract from the total.

$$C_{11}^5 = 462, \qquad C_6^5 = 6$$

$$462 - 6 = 456$$

The answer is **(E) 456**.

</details>

## Key Reminders

- "Or" between mutually exclusive cases → add. "And" / sequential independent steps → multiply.
- Plain addition only works when the "or" cases don't overlap — otherwise use inclusion–exclusion.
- Ask "does swapping two chosen items change the outcome?" — yes → permutation, no → combination.
- Repeated letters, circular seating, and unlabeled group splits all divide down from a base factorial count — identify *what* is being overcounted before dividing.
- "At least one" is often easiest as a complement: total minus "none."

Next: [09-practice-set-2-twisted-models.md](./09-practice-set-2-twisted-models.md) drills the adjacency-constraint and stars-and-bars special models from Lessons 04–05.
