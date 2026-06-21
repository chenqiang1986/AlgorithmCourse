# Problem 3b: Count Numbers Not Greater Than `T`

You are given a list of numbers `A` and many queries.

Each query contains one number `T`.

For each query, output how many numbers in `A` are less than or equal to `T`.

## Input Format

The first line contains two integers:

```text
n q
```

The second line contains `n` integers:

```text
A1 A2 ... An
```

The next `q` lines each contain one integer:

```text
T
```

## Output Format

For each query, output one line containing the number of values in `A` that are less than or equal to `T`.

## Constraints

- `1 <= n, q <= 2 * 10^5`
- `-10^9 <= A[k], T <= 10^9`

## Sample Input

```text
7 5
5 1 2 2 8 10 3
0
2
4
8
100
```

## Sample Output

```text
0
3
4
6
7
```

## Explanation

- For `T = 0`, no numbers are `<= 0`
- For `T = 2`, the numbers are `1, 2, 2`
- For `T = 4`, the numbers are `1, 2, 2, 3`
- For `T = 8`, the numbers are `1, 2, 2, 3, 5, 8`
- For `T = 100`, all numbers are counted

## Suggested Topics

- ordered set or ordered map
- sorting
- binary search
