# AMC 10 2019 A, Problem 10 — Counting Cells Along a Diagonal

## Question
A rectangular floor that is 10 feet wide and 17 feet long is tiled with 170 one-foot square tiles. A
bug walks from one corner to the opposite corner in a straight line. Including the first and the last
tile, how many tiles does the bug visit? 

## Key visualization

Imagine following the diagonal from the cell containing the bug.

1. The diagonal does not pass through an intersection of internal grid lines; it crosses only horizontal or vertical sides of cells.
2. Each time it crosses one of those sides, it enters exactly one new cell.
3. There are $9$ internal horizontal lines and $16$ internal vertical lines for the diagonal to cross.

The initial cell already counts, so the total number of cells visited is

$$
1+9+16=\boxed{26}.
$$

## Pitfall

1. Have to make sure the diagonal does not pass through the grid points. Otherwise we should decompose it into multiple small matrix problem.

2. No need to do the detailed counting by figuring out between each verical line how many horizontal cross overs happen.
