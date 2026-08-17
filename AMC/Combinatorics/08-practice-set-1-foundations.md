# Practice Set 1: Foundations — Counting Principles, Inclusion–Exclusion, Permutations & Combinations

This set drills [01-sum-and-product-rules.md](./01-sum-and-product-rules.md), [02-inclusion-exclusion-principle.md](./02-inclusion-exclusion-principle.md), and [03-permutations-and-combinations.md](./03-permutations-and-combinations.md) — the basic toolkit every later lesson builds on. Attempt each problem before checking your answer.

## How to Use This Set

For every problem, first decide *which tool applies* (add vs. multiply, plain addition vs. inclusion–exclusion, permutation vs. combination) before computing anything — misidentifying the tool is the most common source of error at this level, not the arithmetic itself. This file holds problems only; the answer key and full worked solutions live in [11-practice-set-1-solutions.md](./11-practice-set-1-solutions.md).

## Problem 1: Restaurant Combos

A restaurant's fixed-price menu has 6 appetizers, 5 main courses, and 3 desserts. A full meal consists of exactly one of each. How many different meals are possible?

(A) 90  (B) 108  (C) 120  (D) 150  (E) 180

## Problem 2: Routes Between Towns

To travel from town P to town Q, a traveler can go through town R (3 roads P→R, 4 roads R→Q) or through town S (2 roads P→S, 5 roads S→Q). No road connects R and S directly. How many total routes are there from P to Q?

(A) 14  (B) 22  (C) 24  (D) 26  (E) 30

## Problem 3: Divisible by 6 or by 8

How many integers from 1 to 90 are divisible by 6 or by 8?

(A) 18  (B) 21  (C) 23  (D) 25  (E) 28

## Problem 4: Three Overlapping Interests

In a survey of 50 students, 28 like math, 26 like science, and 20 like art. 15 like both math and science, 10 like both science and art, and 12 like both math and art. 6 students like all three subjects. How many students like at least one of the three subjects?

(A) 33  (B) 37  (C) 40  (D) 43  (E) 46

## Problem 5: Electing Officers

A club has 9 members. In how many ways can a president, a vice-president, and a secretary be chosen, if no member holds more than one office?

(A) 72  (B) 168  (C) 252  (D) 336  (E) 504

## Problem 6: Selecting a Jury

A jury of 5 people is to be selected from a pool of 12 candidates, with no distinct roles among jurors. How many different juries are possible?

(A) 792  (B) 924  (C) 990  (D) 1,188  (E) 1,584

## Problem 7: Arranging MISSISSIPPI

How many distinct ways can the letters of the word `MISSISSIPPI` be arranged?

(A) 17,325  (B) 34,650  (C) 69,300  (D) 103,950  (E) 138,600

## Problem 8: Charm Bracelet

In how many ways can 7 distinct charms be arranged on a circular bracelet, if rotations are considered the same arrangement but reflections (flipping the bracelet over) are considered **different**?

(A) 360  (B) 540  (C) 720  (D) 1,440  (E) 2,520

## Problem 9: Splitting Into Equal Study Groups

12 students are split into 3 unlabeled study groups of 4 students each. How many ways can this be done?

(A) 1,925  (B) 2,887  (C) 4,620  (D) 5,775  (E) 9,625

## Problem 10: Mixed Committee, Then Roles

A team of 4 is chosen from 6 boys and 5 girls, and must include exactly 2 boys and 2 girls. From that team of 4, a captain and a co-captain (two distinct roles) are then chosen. In how many total ways can this be done?

(A) 150  (B) 450  (C) 900  (D) 1,350  (E) 1,800

## Problem 11: Survey Form Combinations

A survey form has 4 questions; each question has 3 possible answers. How many different completed forms are possible?

(A) 81  (B) 108  (C) 144  (D) 162  (E) 243

## Problem 12: Three-Hub Routes

To travel from City X to City Y, a traveler can go through Hub A (2 routes X→A, 3 routes A→Y), Hub B (4 routes X→B, 2 routes B→Y), or Hub C (3 routes X→C, 3 routes C→Y). No two hubs are directly connected. How many total routes are there from X to Y?

(A) 17  (B) 23  (C) 25  (D) 28  (E) 32

## Problem 13: Divisible by 5 or by 9

How many integers from 1 to 120 are divisible by 5 or by 9?

(A) 26  (B) 31  (C) 35  (D) 40  (E) 46

## Problem 14: Three Overlapping Languages

In a group of 60 people, 32 speak English, 28 speak French, and 25 speak Spanish. 15 speak both English and French, 12 speak both French and Spanish, and 14 speak both English and Spanish. 7 people speak all three languages. How many people speak at least one of the three languages?

(A) 38  (B) 42  (C) 47  (D) 51  (E) 55

## Problem 15: Choosing and Ordering Books

In how many ways can 4 different books be chosen from a set of 10 different books and arranged in order on a shelf?

(A) 720  (B) 1,260  (C) 2,520  (D) 3,024  (E) 5,040

## Problem 16: Committee of Four

How many ways can a committee of 4 be chosen from 15 people, with no distinct roles?

(A) 1,365  (B) 1,560  (C) 2,002  (D) 3,003  (E) 5,005

## Problem 17: Arranging ALABAMA

How many distinct arrangements are there of the letters in the word `ALABAMA`?

(A) 105  (B) 210  (C) 315  (D) 420  (E) 840

## Problem 18: Holding Hands in a Circle

In how many distinct ways can 6 people hold hands around a circle, where arrangements that are rotations *or* reflections (mirror images) of each other count as the same arrangement?

(A) 30  (B) 48  (C) 60  (D) 72  (E) 90

## Problem 19: Splitting Into Unequal Groups

10 students are split into an unlabeled group of 6 and an unlabeled group of 4. How many ways can this be done?

(A) 45  (B) 120  (C) 168  (D) 210  (E) 252

## Problem 20: Committee With At Least One Woman

A 5-person committee is chosen from 6 men and 5 women. In how many ways can the committee include at least one woman?

(A) 252  (B) 330  (C) 420  (D) 450  (E) 456

## Key Reminders

- "Or" between mutually exclusive cases → add. "And" / sequential independent steps → multiply.
- Plain addition only works when the "or" cases don't overlap — otherwise use inclusion–exclusion.
- Ask "does swapping two chosen items change the outcome?" — yes → permutation, no → combination.
- Repeated letters, circular seating, and unlabeled group splits all divide down from a base factorial count — identify *what* is being overcounted before dividing.
- "At least one" is often easiest as a complement: total minus "none."

Check your work against [11-practice-set-1-solutions.md](./11-practice-set-1-solutions.md). Next: [09-practice-set-2-twisted-models.md](./09-practice-set-2-twisted-models.md) drills the adjacency-constraint and stars-and-bars special models from Lessons 04–05.
