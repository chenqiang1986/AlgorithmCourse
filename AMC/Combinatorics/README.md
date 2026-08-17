# AMC Combinatorics

This folder contains the combinatorics section of the AMC (competition math) course.

## Course Goals

In this module, we will learn:

1. The two fundamental counting principles: the addition principle and the multiplication principle.
2. The inclusion–exclusion principle for "or" cases that overlap, for two and three sets.
3. Standard permutation and combination formulas, and how to recognize which one a problem calls for.
4. The "bundling" and "gap" methods for arrangements where two people must (or must not) sit together.
5. The stars-and-bars method for distributing identical objects into groups.
6. How to set up and solve a recursive formula when a counting problem has no clean closed form.
7. The "balls into buckets" framework: how distinguishability of the balls and of the buckets determines which of four counting tools applies, including two new ones — Stirling numbers of the second kind and integer partitions.

## Lessons

1. [01-sum-and-product-rules.md](./01-sum-and-product-rules.md)
   The addition principle and multiplication principle, and how to tell "or" from "and".
2. [02-inclusion-exclusion-principle.md](./02-inclusion-exclusion-principle.md)
   What to do when the addition principle's "or" cases overlap, covering the two-set and three-set formulas.
3. [03-permutations-and-combinations.md](./03-permutations-and-combinations.md)
   Ordered arrangements ($P_n^r$) vs. unordered selections ($C_n^r$), plus repeated-item and circular arrangements.
4. [04-adjacency-constraints.md](./04-adjacency-constraints.md)
   Special model: counting arrangements where two specific items must be adjacent, or must never be adjacent.
5. [05-stars-and-bars.md](./05-stars-and-bars.md)
   Special model: distributing identical items into distinct groups using separators.
6. [06-recursive-counting.md](./06-recursive-counting.md)
   Building a recursive formula when direct counting is too hard, with tiling, no-consecutive-choice, and two-coordinate (knight-path) problems.
7. [07-balls-into-buckets.md](./07-balls-into-buckets.md)
   Unifying framework for distributing $n$ balls into $k$ buckets across all four combinations of distinct/indistinguishable balls and buckets: product rule, stars and bars, Stirling numbers of the second kind, and integer partitions.

## Practice Sets

Each 20-problem practice set is a pure problem sheet; its answer key and full worked solutions live in a separate companion file.

8. [08-practice-set-1-foundations.md](./08-practice-set-1-foundations.md)
   Drills Lessons 01–03: counting principles, inclusion–exclusion, permutations and combinations. Solutions: [11-practice-set-1-solutions.md](./11-practice-set-1-solutions.md).
9. [09-practice-set-2-twisted-models.md](./09-practice-set-2-twisted-models.md)
   Drills Lessons 04–05: the adjacency-constraint (bundling/gap) and stars-and-bars special models. Solutions: [12-practice-set-2-solutions.md](./12-practice-set-2-solutions.md).
10. [10-practice-set-3-recursive-methods.md](./10-practice-set-3-recursive-methods.md)
    Drills Lessons 06–07: building a recurrence from scratch, emphasizing the define-state/find-transition method over memorizing any specific formula. Solutions: [13-practice-set-3-solutions.md](./13-practice-set-3-solutions.md).

More lessons can be added later as the course grows.
