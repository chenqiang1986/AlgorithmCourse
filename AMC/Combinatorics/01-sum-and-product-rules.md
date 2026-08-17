# Lesson 1: The Addition Principle and the Multiplication Principle

Every combinatorics problem, no matter how complicated, is eventually built out of two basic rules: the **addition principle** and the **multiplication principle**. Knowing when to add and when to multiply is the single most important skill in this module — every later lesson is really a more elaborate application of these two rules.

## 1. The Addition Principle (Sum Rule)

Use the addition principle when a task can be completed by exactly **one** of several separate methods, and no outcome can happen under two methods at once (the methods are mutually exclusive).

If method 1 has $n_1$ outcomes, method 2 has $n_2$ outcomes, …, method $k$ has $n_k$ outcomes, and no outcome belongs to two methods at once, then:

$$\text{total outcomes} = n_1 + n_2 + \cdots + n_k$$

The keyword to watch for is **"or"**: "I take a bus **or** a train **or** a bike" — pick exactly one category.

### Example

To go from home to school, you can either walk (3 possible routes) or bike (2 possible routes). You are not doing both, so the two sets of routes never overlap.

$$\text{total routes} = 3 + 2 = 5$$

## 2. The Multiplication Principle (Product Rule)

Use the multiplication principle when a task is completed by going through several **steps in sequence**, and the number of options at each step does not depend on which options were chosen earlier.

If step 1 has $n_1$ options, step 2 has $n_2$ options, …, step $k$ has $n_k$ options, then:

$$\text{total outcomes} = n_1 \times n_2 \times \cdots \times n_k$$

The keyword to watch for is **"and"**: "I choose a shirt **and** pants **and** shoes" — every step must happen.

### Example

A meal consists of one appetizer (4 choices), one main course (3 choices), and one dessert (2 choices).

$$\text{total meals} = 4 \times 3 \times 2 = 24$$

## 3. Core Template: Deciding Add vs. Multiply

Ask yourself: "Am I doing task A, **or** task B?" (add) vs. "Am I doing task A, **and then** task B?" (multiply).

```text
"or" between mutually exclusive cases  -> add
"and" / sequential independent steps   -> multiply
```

A more reliable test than the keyword itself:

- If a single finished outcome is only ever produced by **one** of the branches, the branches are cases to **add**.
- If a single finished outcome always needs **all** of the steps to happen together, the steps are stages to **multiply**.

## 4. Reading Example: Counting License Plates

A license plate has 2 letters followed by 3 digits (letters and digits may repeat).

- Step 1: choose letter 1 — 26 ways
- Step 2: choose letter 2 — 26 ways
- Step 3: choose digit 1 — 10 ways
- Step 4: choose digit 2 — 10 ways
- Step 5: choose digit 3 — 10 ways

All five steps must happen for every plate, and the number of choices at each step does not depend on earlier steps, so we multiply:

$$26 \times 26 \times 10 \times 10 \times 10 = 676{,}000$$

**Non-obvious detail:** if the problem instead said "no letter or digit repeats," step 2 would only have 25 options (one letter already used), step 4 would have 9, and step 5 would have 8. The multiplication principle still applies, but each factor shrinks because the *set of remaining options* now depends on earlier choices, even though the *procedure* (fill positions left to right) does not.

## 5. Class Practice 1: Outfit Choices

### Problem

A student has 5 shirts, 4 pairs of pants, and 2 pairs of shoes. Every outfit consists of exactly one shirt, one pair of pants, and one pair of shoes. How many different outfits are possible?

### Answer Choices

(A) 11  (B) 20  (C) 22  (D) 40  (E) 80

### Solution

Each outfit needs a shirt **and** pants **and** shoes — three sequential, independent choices. Multiply:

$$5 \times 4 \times 2 = 40$$

The answer is **(D) 40**.

## 6. Class Practice 2: Weekend Plans

### Problem

For a free afternoon, Maria will either go to the movies (6 movies are playing) or go hiking (3 trails she likes). She only has time for one activity, and no movie is also a trail. How many different afternoons can she have?

### Answer Choices

(A) 3  (B) 6  (C) 9  (D) 18  (E) 24

### Solution

"Movies **or** hiking" — she does exactly one, and the two lists never overlap, so the cases are mutually exclusive. Add:

$$6 + 3 = 9$$

The answer is **(C) 9**.

## 7. Common Mistakes

### 7.1 Adding when cases overlap

The addition principle requires the cases to be mutually exclusive. If two "or" cases can actually happen at the same time (e.g., "divisible by 3 or by 4," which overlap at multiples of 12), a plain sum double-counts the overlap. Always ask "can both happen at once?" before adding — if yes, plain addition does not apply; see [02-inclusion-exclusion-principle.md](./02-inclusion-exclusion-principle.md) for how to fix the count.

### 7.2 Multiplying without adjusting for used-up options

"No repeated letters" or "at least one vowel" changes how many options remain at later steps. Multiplying with the same count at every step silently assumes independence that may not hold.

### 7.3 Treating "and" problems as "or" problems

A common reflex is to add counts for every category mentioned in a problem instead of asking whether the outcome requires *all* of them together (multiply) or *only one* of them (add).

## 8. Key Takeaways

- Addition principle: mutually exclusive cases → add the counts.
- Multiplication principle: sequential, independent stages that must all happen → multiply the counts.
- The addition principle only works when the cases truly never overlap — if they can, see [02-inclusion-exclusion-principle.md](./02-inclusion-exclusion-principle.md).
- Always ask first: "does a finished outcome require every step, or does it come from exactly one branch?"

Next lesson: [02-inclusion-exclusion-principle.md](./02-inclusion-exclusion-principle.md) covers what to do when the addition principle's "or" cases overlap.
