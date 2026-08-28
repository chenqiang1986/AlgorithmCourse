# Lesson 7: Balls Into Buckets — The Four Cases
*AMC / Combinatorics*

Every "distribute $n$ balls into $k$ buckets" problem hides the same two yes/no questions: **are the balls distinguishable from each other**, and **are the buckets distinguishable from each other**? Answering both questions picks out one of exactly four cases, and each case has its own tool — some you already know, and two brand-new ones this lesson introduces.

## 1. The Four Cases at a Glance

| # | Balls | Buckets | Method | Formula |
|---|-------|---------|--------|---------|
| 1 | distinct | distinct | product rule | $k^n$ |
| 2 | indistinct | distinct | stars and bars | $C_{n+k-1}^{k-1}$ |
| 3 | distinct | indistinct | recursive | $\sum_{j=0}^{k} S(n,j)$ |
| 4 | indistinct | indistinct | recursive | $p(n,k)$ |

"Distinct balls" means each ball is a separate, identifiable individual (numbered, named, colored differently). "Distinct buckets" means the ball's destination is identifiable — swapping the contents of two buckets produces a *different* outcome. Whenever you meet a distribution problem, ask both questions before reaching for a formula; the answer to each question independently changes which row of this table applies.

**Every case in this table allows empty buckets** — a bucket may end up holding zero balls unless a problem says otherwise. This matches the framing already used for stars and bars.

## 2. Case 1: Distinct Balls, Distinct Buckets (Product Rule)

Each of the $n$ balls independently picks one of $k$ buckets. No ball's choice depends on any other ball's choice, so this is a direct application of the multiplication principle from [01-sum-and-product-rules.md](./01-sum-and-product-rules.md):

$$\underbrace{k \times k \times \cdots \times k}_{n \text{ balls, each with } k \text{ choices}} = k^n$$

### Reading Example

3 distinct balls — red, green, blue — go into 2 distinct buckets, A and B. Each ball independently picks A or B:

$$2 \times 2 \times 2 = 2^3 = 8$$

The 8 outcomes are every possible assignment: e.g. (red→A, green→A, blue→A), (red→A, green→A, blue→B), … all the way to (red→B, green→B, blue→B).

**Non-obvious detail:** nothing stops a bucket from ending up empty or holding all $n$ balls — the exponent $k^n$ already counts those outcomes, since each ball's choice is completely unconstrained by the others.

## 3. Case 2: Indistinguishable Balls, Distinct Buckets (Stars and Bars)

This is exactly Question B of [05-stars-and-bars.md](./05-stars-and-bars.md) — "$n$ identical balls into $k$ distinct boxes" — so the full derivation (stars, bars, gaps) is not repeated here. The formula:

$$n \text{ balls}, k \text{ buckets, indistinct/distinct} \implies C_{n+k-1}^{\,k-1}$$

**Non-obvious detail:** compare with Case 1 — same $n$ balls, same $k$ buckets, but once the balls' identities stop mattering, the count drops from $k^n$ (which tracks *which* ball went where) to $C_{n+k-1}^{k-1}$ (which only tracks *how many* balls each bucket got). Losing information about the balls always shrinks the count.

## 4. Case 3: Distinct Balls, Indistinguishable Buckets (Recursive)

Now the balls keep their identities, but the buckets don't — swapping the contents of two buckets is *not* a new outcome. All that matters is: which balls ended up grouped together? This is exactly asking how many ways there are to **partition $n$ distinct items into unlabeled groups**.

### 4.1 Defining $S(n,j)$

Let $S(n,j)$ = the number of ways to partition $n$ distinct items into **exactly** $j$ nonempty, unlabeled groups. These are the **Stirling numbers of the second kind**.

Using the recursive-counting method from [06-recursive-counting.md](./06-recursive-counting.md), look at where the **last item** (item $n$) ends up:

- **Case A:** item $n$ joins one of the groups already formed by the other $n - 1$ items. Condition on those $n-1$ items already being split into $j$ groups ($S(n-1,j)$ ways) — once those $j$ groups exist, they're distinguishable *by their contents*, so item $n$ has $j$ choices of which group to join: $j \cdot S(n-1,j)$ ways.
- **Case B:** item $n$ forms a brand-new group by itself. The other $n-1$ items must form the remaining $j - 1$ groups: $S(n-1,j-1)$ ways.

These cases are mutually exclusive (item $n$ either joins an existing group or doesn't) and exhaustive, so:

$$S(n,j) = j \cdot S(n-1,j) + S(n-1,j-1)$$

Base cases: $S(0,0) = 1$ (the empty partition), $S(n,0) = 0$ for $n > 0$, and $S(n,j) = 0$ whenever $j > n$ (you can't split $n$ items into more than $n$ nonempty groups).

Building the triangle row by row:

| $n \backslash j$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | 1 | | | | | |
| 1 | 0 | 1 | | | | |
| 2 | 0 | 1 | 1 | | | |
| 3 | 0 | 1 | 3 | 1 | | |
| 4 | 0 | 1 | 7 | 6 | 1 | |
| 5 | 0 | 1 | 15 | 25 | 10 | 1 |

For example, $S(4,2) = 2 \cdot S(3,2) + S(3,1) = 2(3) + 1 = 7$.

### 4.2 From "Exactly $j$ Groups" to "At Most $k$ Buckets"

A problem asks for $n$ distinct balls into (at most) $k$ **indistinguishable** buckets — buckets may be empty, and since the buckets are indistinguishable, all the empty ones are interchangeable and contribute nothing new. So sum $S(n,j)$ over every possible number of *nonempty* buckets, from $j = 0$ up to $k$:

$$n \text{ balls}, k \text{ buckets, distinct/indistinct} \implies \sum_{j=0}^{k} S(n,j)$$

(Terms with $j > n$ are automatically $0$, so the sum never needs more than $\min(n,k)$ nonzero terms.)

**Non-obvious detail:** this "sum over $j$" step is exactly why Case 3 needs indistinguishable buckets — with *distinct* buckets (Case 1's setting, if the balls were also distinct), leaving different buckets empty would count as different outcomes, and a single $S(n,k)$ term wouldn't capture that. Indistinguishable buckets collapse all those variants into one.

### Reading Example

4 distinct balls, labeled 1–4, go into **at most 3** indistinguishable buckets (some buckets may be left empty). How many ways?

Read $S(4,j)$ off row $n=4$ of the table above: $S(4,0)=0$, $S(4,1)=1$, $S(4,2)=7$, $S(4,3)=6$.

$$\sum_{j=0}^{3} S(4,j) = 0 + 1 + 7 + 6 = 14$$

(For reference: if the "at most 3" restriction were lifted entirely — i.e., unlimited indistinguishable buckets — you'd sum all the way to $j=4$ and add $S(4,4)=1$, giving $15$. That total, the number of ways to partition $n$ items into *any* number of unlabeled nonempty groups, is called the $n$-th **Bell number**.)

### 4.3 A Detour: Why Not Recurse Directly on "$j$ Buckets, Empty Allowed"?

Section 4.2 reached $\sum_{j=0}^{k} S(n,j)$ by summing over the *exact* number of nonempty buckets. Why not skip that step and define the target quantity directly?

$$F(n,j) = \text{number of ways to put } n \text{ distinct balls into } j \text{ indistinguishable buckets, empty buckets allowed}$$

Try the same recursive-counting method: look at where the last ball (ball $n$) goes, on top of some already-distributed arrangement of the other $n-1$ balls counted by $F(n-1,j)$.

Here's where it breaks: to place ball $n$, we need to know how many of the $j$ buckets are already occupied. If $m$ buckets are nonempty, ball $n$ has $m$ choices to join an existing bucket, plus one more choice to start a new bucket (only if $m < j$). But $F(n-1,j)$ lumps together *every* arrangement using at most $j$ buckets, mixing together all values of $m$ from $0$ to $j$ at once. There's no single multiplier that works for the whole count $F(n-1,j)$ — the recurrence has no way to "look inside" it and recover $m$.

**Tip for future investigations:** when a definition phrased as "at most $j$ ..." resists a clean recursive formula because the recursive step needs to know an internal detail that "at most" throws away, try tightening the definition to "**exactly** $j$ ..." instead. Pinning the count exactly often hands the recursive step the missing piece of information. That's precisely why $S(n,j)$ is defined as *exactly* $j$ nonempty groups rather than *at most* $j$: fixing $j$ exactly is what makes "item $n$ has $j$ choices to join an existing group" a true statement. Once the exact-count version has a formula, sum over it to recover the "at most" version — as Section 4.2 already did.

## 5. Case 4: Indistinguishable Balls, Indistinguishable Buckets (Recursive)

Neither the balls nor the buckets are distinguishable now, so all that survives is the **multiset of bucket sizes** — e.g. "one bucket got 3 balls, another got 2, another got 1" is a complete description of the outcome, with no further detail to track. This is exactly an **integer partition** of $n$ into at most $k$ parts (one part per nonempty bucket; empty buckets add nothing, by the same reasoning as Case 3).

### 5.1 Defining $p(n,k)$

Let $p(n,k)$ = the number of ways to write $n$ as a sum of at most $k$ positive integers, where order doesn't matter — a **partition of $n$ into at most $k$ parts**.

Apply the same recursive-counting method, this time splitting on **how many parts the partition actually uses**:

- **Case A:** fewer than $k$ parts are used. This is just a partition of $n$ into at most $k-1$ parts: $p(n, k-1)$ ways.
- **Case B:** exactly $k$ parts are used, each part $\ge 1$. Subtract $1$ from every one of the $k$ parts — each new part is $\ge 0$, and the parts still sum to $n - k$. This is a partition of $n-k$ into at most $k$ parts (a part that dropped to $0$ just means that slot is unused): $p(n-k, k)$ ways.

These two cases are mutually exclusive (a partition either uses exactly $k$ parts or fewer) and exhaustive, so:

$$p(n,k) = p(n,k-1) + p(n-k,k)$$

Base cases: $p(0,k) = 1$ for every $k \ge 0$ (zero balls have exactly one distribution — everything empty), $p(n,0) = 0$ for $n > 0$ (positive balls can't fit into zero buckets), and $p(n,k) = 0$ whenever $n < 0$ (a guard for the recurrence — this case never actually occurs).

Building the table row by row (rows are $k$, columns are $n$):

| $k \backslash n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 |
| 3 | 1 | 1 | 2 | 3 | 4 | 5 | 7 | 8 | 10 |

For example, $p(6,3) = p(6,2) + p(3,3) = 4 + 3 = 7$.

### Reading Example

6 identical balls go into **at most 3** indistinguishable buckets. How many ways?

Read $p(6,3) = 7$ directly from the table. As a check, list every partition of 6 into at most 3 parts by hand:

$$6, \quad 5+1, \quad 4+2, \quad 4+1+1, \quad 3+3, \quad 3+2+1, \quad 2+2+2$$

That's 7 partitions, matching the table.

**Non-obvious detail:** unlike Cases 1–3, there is no closed-form formula for $p(n,k)$ — integer partitions genuinely require building up a table via the recurrence (or, for small cases, direct enumeration). This is the same situation Lesson 6 warned about: not every counting problem has a clean formula.

### 5.2 Why "At Most $k$" Wasn't a Problem Here

Contrast this with the detour in Section 4.3. There, recursing directly on "$j$ buckets, empty allowed" broke down because placing the last (identifiable) ball required knowing how many buckets were already nonempty — a detail the "at most" framing didn't expose. Section 5.1's $p(n,k)$ recurrence works entirely inside the "at most $k$" framing, with no detour through an "exactly $k$" version and a sum. Why does it work here but not there?

The balls are indistinguishable now, so there is no "last ball" to place and no "which bucket does it join?" question to ask. Section 5.1's case split never looks at a single ball — it asks a structural question about the partition itself: does it use all $k$ available parts, or fewer? That question is already fully answered by "at most $k$"; there is no hidden per-arrangement detail (like Case 3's count of nonempty buckets) it needs to recover. Case B's "subtract $1$ from every part" step applies uniformly to *every* arrangement $p(n-k,k)$ counts, regardless of how many of the $k$ slots end up nonzero — so nothing about the "at most" framing gets lost.

**Moral:** whether "at most" resists a direct recurrence isn't about the phrase "at most" itself — it depends on whether the natural recursive step needs a detail that "at most" hides. When it does (Case 3's per-ball placement), tighten to "exactly." When the recursive step never needs that detail (Case 4's parts-based split), "at most" recurses just fine on its own.

### 5.3 A Parallel Exercise: Partitions Into Exactly $k$ Parts

Even though Case 4 didn't need it, the "exactly" version is worth deriving too, to see the same pattern from Section 4.1 play out on parts instead of buckets:

$$q(n,k) = \text{number of ways to write } n \text{ as a sum of exactly } k \text{ positive integers, order not mattering}$$

Recursive-count $q(n,k)$ by casing on whether the partition contains a part equal to $1$:

- **Case A:** at least one part equals $1$. Remove one copy of it. What remains is a partition of $n-1$ into exactly $k-1$ positive parts: $q(n-1,k-1)$ ways.
- **Case B:** no part equals $1$ — every one of the $k$ parts is $\ge 2$. Subtract $1$ from every part; each stays $\ge 1$, and the parts still sum to $n-k$. This is a partition of $n-k$ into exactly $k$ positive parts: $q(n-k,k)$ ways.

These cases are mutually exclusive and exhaustive (a partition either has a part equal to $1$ or it doesn't), so:

$$q(n,k) = q(n-1,k-1) + q(n-k,k)$$

Base cases: $q(0,0) = 1$, $q(n,0) = 0$ for $n>0$, $q(0,k) = 0$ for $k>0$, and $q(n,k) = 0$ whenever $k>n$ (a sum of $k$ positive integers is at least $k$).

**Non-obvious detail:** $q(n,k)$'s recurrence splits on a *value* (is the smallest part equal to $1$?), while $p(n,k)$'s recurrence in Section 5.1 splits on a *count* (are all $k$ slots used?) — two different valid ways to case-split the same object. Both stay clean because neither one needs to look inside a fixed collection of indistinguishable, unlabeled parts and recover a lost per-item detail, the way Case 3's $F(n,j)$ did. And just as in Case 3, summing the exact version recovers the at-most version: $p(n,k) = \sum_{i=1}^{k} q(n,i)$ for $n \ge 1$ (the $n=0$ case, $p(0,k)=1$, is the empty partition and isn't covered by $q$, which requires $k \ge 1$ positive parts).

## 6. Class Practice 1: Case 1 — Distinct Gifts, Distinct Kids

### Problem

5 distinct gifts are given out to 3 distinct kids. A kid may receive any number of gifts, including zero. In how many ways can the gifts be given out?

### Answer Choices

(A) 15  (B) 125  (C) 216  (D) 243  (E) 3,125

<details>
<summary>Solution</summary>

Balls (gifts) are distinct, buckets (kids) are distinct — Case 1, the product rule. Each of the 5 gifts independently picks one of 3 kids:

$$3^5 = 243$$

((B) $125 = 5^3$ swaps which quantity is the base and which is the exponent — a common error. (A) $15 = 3 \times 5$ mistakenly adds instead of multiplying.)

The answer is **(D) 243**.

</details>

## 7. Class Practice 2: Case 2 — Identical Balls, Distinct Buckets

### Problem

7 identical balls are distributed into 4 distinct buckets. A bucket may be empty. In how many ways can this be done?

### Answer Choices

(A) 84  (B) 120  (C) 165  (D) 210  (E) 220

<details>
<summary>Solution</summary>

Balls are indistinguishable, buckets are distinct — Case 2, stars and bars:

$$C_{7+4-1}^{4-1} = C_{10}^{3} = 120$$

The answer is **(B) 120**.

</details>

## 8. Class Practice 3: Case 3 — Distinct Balls, Indistinguishable Buckets

### Problem

5 distinct balls are placed into at most 3 indistinguishable buckets (some buckets may be left empty). In how many ways can this be done?

### Answer Choices

(A) 25  (B) 40  (C) 41  (D) 51  (E) 52

<details>
<summary>Solution</summary>

Balls are distinct, buckets are indistinguishable — Case 3, sum the Stirling numbers of the second kind for $j = 0$ to $3$. Extending the triangle from Section 4.1 to row $n=5$: $S(5,1)=1$, $S(5,2)=15$, $S(5,3)=25$.

$$\sum_{j=0}^{3} S(5,j) = 0 + 1 + 15 + 25 = 41$$

((D) $51$ mistakenly includes $S(5,4)=10$, i.e. sums one bucket too far. (E) $52$ is the 5th Bell number — the total over *all* possible numbers of nonempty groups, with no "at most 3" restriction.)

The answer is **(C) 41**.

</details>

## 9. Class Practice 4: Case 4 — Identical Balls, Indistinguishable Buckets

### Problem

8 identical balls are placed into at most 3 indistinguishable buckets (some buckets may be left empty). In how many ways can this be done?

### Answer Choices

(A) 8  (B) 10  (C) 15  (D) 18  (E) 22

<details>
<summary>Solution</summary>

Balls and buckets are both indistinguishable — Case 4, integer partitions of $8$ into at most $3$ parts, $p(8,3)$. Extending the table from Section 5.1: $p(7,2)=4$, $p(4,3)=4$, so $p(7,3) = p(7,2)+p(4,3) = 8$; then $p(8,2) = p(8,1)+p(6,2) = 1+4 = 5$, $p(5,3)=5$, so:

$$p(8,3) = p(8,2) + p(5,3) = 5 + 5 = 10$$

As a check, list all partitions of 8 into at most 3 parts: $8,\ 7{+}1,\ 6{+}2,\ 6{+}1{+}1,\ 5{+}3,\ 5{+}2{+}1,\ 4{+}4,\ 4{+}3{+}1,\ 4{+}2{+}2,\ 3{+}3{+}2$ — 10 partitions.

((C) $15 = p(8,4)$ uses one bucket too many. (E) $22 = p(8)$, the *unrestricted* partition count of 8, ignoring the "at most 3" limit.)

The answer is **(B) 10**.

</details>

## 10. Common Mistakes

### 10.1 Answering the wrong "distinct/indistinct" question

The single most common error is solving the balls' distinguishability correctly but forgetting to check the buckets' (or vice versa). Always answer both questions from Section 1 explicitly before picking a formula — a problem that looks like Case 2 (stars and bars) with distinct balls is actually Case 1, and $k^n \ne C_{n+k-1}^{k-1}$ in general.

### 10.2 Forgetting to sum over $j$ in Case 3

Using $S(n,k)$ alone answers "distribute into **exactly** $k$ nonempty groups," not "at most $k$." If the problem allows empty buckets (the default in this lesson), sum $S(n,j)$ for $j = 0$ to $k$, as in Section 4.2.

### 10.3 Confusing Case 3's "at most $k$" with Case 4's "at most $k$"

Both cases sum/accumulate over bucket counts up to $k$, but Case 3 sums Stirling numbers over the number of nonempty groups, while Case 4 uses a single two-argument recurrence $p(n,k)$ that already bakes in the "at most $k$" condition — don't try to sum $p(n,j)$ over $j$, that would double count.

### 10.4 Off-by-one errors in the Stirling and partition recurrences

Both $S(n,j) = j \cdot S(n-1,j) + S(n-1,j-1)$ and $p(n,k) = p(n,k-1) + p(n-k,k)$ reference two different smaller states — double-check which index shrinks in each term before filling in a table, exactly as warned in [06-recursive-counting.md](./06-recursive-counting.md)'s common mistakes.

## 11. Key Takeaways

- Every "$n$ balls into $k$ buckets" problem is decided by two independent yes/no questions — are the balls distinct, are the buckets distinct — giving four cases total.
- **Distinct/distinct:** product rule, $k^n$.
- **Indistinct/distinct:** stars and bars, $C_{n+k-1}^{k-1}$ (full derivation in [05-stars-and-bars.md](./05-stars-and-bars.md)).
- **Distinct/indistinct:** Stirling numbers of the second kind, $\sum_{j=0}^{k} S(n,j)$, built from the recurrence $S(n,j) = j \cdot S(n-1,j) + S(n-1,j-1)$.
- **Indistinct/indistinct:** integer partitions of $n$ into at most $k$ parts, $p(n,k)$, built from the recurrence $p(n,k) = p(n,k-1) + p(n-k,k)$ — this case has no closed-form formula.
- Losing distinguishability (on either axis) only ever shrinks the count relative to the fully-distinct case — a useful sanity check on your final answer.
- Both new recurrences in this lesson reuse the exact "define the count, split on the last piece, build a table" method from [06-recursive-counting.md](./06-recursive-counting.md) — the same idea keeps reappearing under new names.

This concludes the introductory sequence of this module. Later lessons can extend these ideas to inclusion–exclusion with more than two sets, generating functions, and probability built on top of these counting techniques.
