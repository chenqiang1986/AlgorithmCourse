# Problem 3a: Lower Bound and Upper Bound Practice

You are given a set of distinct integers `A` and many queries.

Each query contains one integer `T`.

For each query, output these four values in order:

1. the smallest number in `A` that is greater than or equal to `T`
2. the smallest number in `A` that is greater than `T`
3. the biggest number in `A` that is less than or equal to `T`
4. the biggest number in `A` that is less than `T`

If a required number does not exist, output `N` in that position.

## Input Format

The first line contains two integers:

```text
n q
```

The second line contains `n` distinct integers:

```text
A1 A2 ... An
```

The next `q` lines each contain one integer:

```text
T
```

## Output Format

For each query, output one line containing four values separated by spaces.

The four values should be printed in the order described in the problem statement.

If one answer does not exist, print `N` in that position.

## Constraints

- `1 <= n, q <= 2 * 10^5`
- all values in `A` are distinct
- `-10^9 <= A[k], T <= 10^9`

## Sample Input

```text
5 4
2 5 8 12 20
8
6
1
25
```

## Sample Output

```text
8 12 8 5
8 8 5 5
2 2 N N
N N 20 20
```

## Explanation

- For `T = 8`:
  - the smallest number `>= 8` is `8`
  - the smallest number `> 8` is `12`
  - the biggest number `<= 8` is `8`
  - the biggest number `< 8` is `5`
- For `T = 6`:
  - the smallest number `>= 6` is `8`
  - the smallest number `> 6` is `8`
  - the biggest number `<= 6` is `5`
  - the biggest number `< 6` is `5`
- For `T = 1`, there are no numbers `<= 1` or `< 1`
- For `T = 25`, there are no numbers `>= 25` or `> 25`

## Suggested Topics

- `set`
- `lower_bound`
- `upper_bound`
- predecessor and successor
