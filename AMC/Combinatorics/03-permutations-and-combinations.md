# Lesson 3: Permutations and Combinations

This lesson turns the multiplication principle from [01-sum-and-product-rules.md](./01-sum-and-product-rules.md) into two named formulas: **permutations**, for when order matters, and **combinations**, for when it does not. Almost every "standard" counting question on the AMC is really asking you to identify which of these two formulas applies.

## 1. Permutations: Order Matters

A permutation is an **ordered** arrangement of items. If you are choosing $r$ items out of $n$ distinct items and the order in which you pick them matters (first place vs. second place, leftmost seat vs. rightmost seat), you are counting permutations.

Build it with the multiplication principle: there are $n$ choices for the first slot, $n - 1$ remaining choices for the second slot (one item is used up), $n - 2$ for the third, and so on, for $r$ slots total:

$$P_n^r = n \times (n - 1) \times (n - 2) \times \cdots \times (n - r + 1) = \frac{n!}{(n - r)!}$$

When $r = n$ (arrange every item), this is just $n!$.

## 2. Combinations: Order Does Not Matter

A combination is an **unordered** selection of items — a committee, a subset, a hand of cards. If swapping the order of the chosen items still counts as the same outcome, you are counting combinations.

Every unordered group of $r$ items can be arranged in $r!$ different orders. So the ordered count $P_n^r$ counts each unordered group $r!$ times. Divide it out:

$$C_n^r = \frac{P_n^r}{r!} = \frac{n!}{r!(n - r)!}$$

**Non-obvious detail:** $C_n^r = C_n^{n-r}$ — choosing which $r$ items to include is the same act as choosing which $n - r$ items to leave out. This identity is a fast sanity check and often shortens a computation (e.g., $C_{20}^{18} = C_{20}^{2} = 190$, no need to expand $18!$).

## 3. Core Template

$$n! = n \times (n - 1) \times (n - 2) \times \cdots \times 1 \qquad (0! = 1 \text{ by convention})$$

$$P_n^r = \frac{n!}{(n - r)!} \quad \text{ordered selection of } r \text{ out of } n$$

$$C_n^r = \frac{n!}{r!(n - r)!} \quad \text{unordered selection of } r \text{ out of } n$$

$$C_n^r = C_n^{n-r}$$

Quick decision rule: read the problem statement and ask "if I swap two chosen items, is it a different outcome?" Yes → permutation. No → combination.

## 4. Reading Example: Race Placings (Permutation)

8 runners compete in a race. In how many ways can 1st, 2nd, and 3rd place be awarded?

Swapping who gets 1st vs. 2nd clearly changes the outcome, so order matters:

$$P_8^3 = 8 \times 7 \times 6 = 336$$

## 5. Reading Example: Committee Selection (Combination)

From a group of 10 people, how many ways can a 3-person committee be formed (no distinct roles)?

The committee $\{\text{Alice}, \text{Bob}, \text{Carol}\}$ is the same committee no matter what order the names are listed, so order does not matter:

$$C_{10}^{3} = \frac{10!}{3!7!} = 120$$

**Non-obvious detail:** if the problem instead said "a president, a secretary, and a treasurer chosen from 10 people," that *is* a permutation ($P_{10}^{3} = 720$), because assigning the same three people to different roles produces different outcomes. The people involved can be identical between two problems — only the "does order/role matter" question changes the formula.

## 6. Reading Example: Arrangements with Repeated Items

How many distinct ways can the letters of the word `LEVEL` be arranged?

`LEVEL` has 5 letters, but `L` repeats twice and `E` repeats twice. If all 5 letters were distinct, there would be $5! = 120$ arrangements. But swapping the two `L`s with each other produces an arrangement that looks identical, and likewise for the two `E`s — so $5!$ overcounts by a factor of $2!$ for the `L`s and $2!$ for the `E`s:

$$\frac{5!}{2!2!} = \frac{120}{4} = 30$$

General rule for a multiset with $n$ total items where one value repeats $k_1$ times, another repeats $k_2$ times, etc.:

$$\frac{n!}{k_1!k_2!\cdots}$$

## 7. Reading Example: Circular Permutations

In how many distinct ways can 5 people be seated around a circular table, if seatings that are rotations of each other count as the same arrangement?

A straight-line arrangement of 5 people has $5! = 120$ orders. But around a circle, rotating everyone by one seat produces a "different" linear listing that is actually the same physical seating. Each circular arrangement corresponds to exactly $5$ linear arrangements (one for each rotation), so divide by $5$:

$$\frac{5!}{5} = (5 - 1)! = 24$$

General rule: $n$ distinct people around a circle (rotations equivalent, reflections counted as different) →

$$(n - 1)!$$

**Non-obvious detail:** this only removes rotational duplicates. If the problem also treats a clockwise seating and its mirror-image (counterclockwise) as the same — common when seats aren't physically distinguishable, e.g., people holding hands in a circle — divide by an additional factor of $2$, giving $(n - 1)!/2$.

## 8. Class Practice 1: Choosing a Snack

### Problem

A vending machine has 12 different snacks. Jamal wants to buy 2 different snacks to share with a friend (the two snacks are just "his purchase," with no distinction between them). How many different purchases are possible?

### Answer Choices

(A) 24  (B) 66  (C) 132  (D) 144  (E) 156

<details>
<summary>Solution</summary>

Buying snack A and snack B is the same purchase as buying snack B and snack A — order does not matter, so this is a combination:

$$C_{12}^{2} = \frac{12!}{2!10!} = 66$$

The answer is **(B) 66**.

</details>

## 9. Class Practice 2: Password Digits

### Problem

A password consists of 4 different digits chosen from `0` through `9`, and the order of the digits matters. How many such passwords are possible?

### Answer Choices

(A) 210  (B) 720  (C) 2,520  (D) 5,040  (E) 10,000

<details>
<summary>Solution</summary>

Order matters (`1234` and `4321` are different passwords) and digits cannot repeat, so this is a permutation of 4 out of 10 digits:

$$P_{10}^{4} = 10 \times 9 \times 8 \times 7 = 5{,}040$$

The answer is **(D) 5,040**.

</details>

## 10. Class Practice 3: Arranging a Word

### Problem

How many distinct arrangements are there of the letters in the word `BANANA`?

### Answer Choices

(A) 60  (B) 120  (C) 360  (D) 720  (E) 5,040

<details>
<summary>Solution</summary>

`BANANA` has 6 letters: `B` (1 time), `A` (3 times), `N` (2 times).

$$\frac{6!}{3!2!1!} = \frac{720}{12} = 60$$

The answer is **(A) 60**.

</details>

## 11. Common Mistakes

### 11.1 Using $C_n^r$ when order actually matters

Assigning distinct roles (president/secretary/treasurer, 1st/2nd/3rd place) is a permutation even though the underlying group of chosen people looks like a "selection." Ask whether swapping two chosen items changes the outcome.

### 11.2 Forgetting to divide out repeated items

When arranging a word or a set of objects with duplicates, dividing by $r!$ once (as in a normal combination) is not enough — you must divide by the factorial of *each* repeated value's count.

### 11.3 Treating circular arrangements like linear ones

Forgetting to divide by $n$ (for rotations) or by an extra $2$ (for reflections, when applicable) is the most common circular-permutation error.

## 12. Key Takeaways

- $P_n^r = \dfrac{n!}{(n - r)!}$ counts ordered selections; $C_n^r = \dfrac{n!}{r!(n - r)!}$ counts unordered selections.
- $C_n^r = C_n^{n-r}$.
- Arrangements of a multiset with repeated items divide $n!$ by the factorial of each repeat count.
- Circular arrangements of $n$ distinct items: $(n - 1)!$, or $(n - 1)!/2$ if reflections are also equivalent.

Next lesson: [04-adjacency-constraints.md](./04-adjacency-constraints.md) covers what to do when a permutation problem adds the extra condition that two specific items must (or must not) sit next to each other.
