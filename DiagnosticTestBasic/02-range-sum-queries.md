# Problem 2: Range Sum Queries

## Expected Submission Filename

Upload your solution as:

```text
dtb_range_sum_queries.cpp
```

You are given an array of numbers and many queries.

Each query gives two indices `i` and `j`.

For each query, output:

```text
a[i] + a[i + 1] + ... + a[j]
```

## Input Format

The first line contains two integers:

```text
n q
```

The second line contains `n` integers:

```text
a1 a2 ... an
```

The next `q` lines each contain one query:

```text
i j
```

In this problem, indices are **1-based**.

## Output Format

For each query, output one line containing the required sum.

## Constraints

- `1 <= n, q <= 2 * 10^5`
- `-10^9 <= a[k] <= 10^9`
- `1 <= i <= j <= n`

## Sample Input

```text
6 4
3 1 4 1 5 9
1 3
2 5
4 4
3 6
```

## Sample Output

```text
8
11
1
19
```

## Explanation

- Query `(1, 3)` asks for `3 + 1 + 4 = 8`
- Query `(2, 5)` asks for `1 + 4 + 1 + 5 = 11`
- Query `(4, 4)` asks for `1`
- Query `(3, 6)` asks for `4 + 1 + 5 + 9 = 19`

## Suggested Topics

- prefix sums
- partial sum maintenance
- fast query answering
