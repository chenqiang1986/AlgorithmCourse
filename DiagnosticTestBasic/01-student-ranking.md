# Problem 1: Student Ranking

You are given a list of students.

Each student has:

- a name
- a score

Your task is to output the student names in order of their scores.

Students with higher scores should come first.

If two students have the same score, output the student with the lexicographically smaller name first.

## Input Format

The first line contains one integer:

```text
n
```

The next `n` lines each contain:

```text
name score
```

## Output Format

Output `n` lines.

Each line should contain one student name, in the required order.

## Constraints

- `1 <= n <= 10^5`
- each name contains only English letters, digits, or `_`
- `1 <= score <= 10^9`

## Sample Input

```text
5
alice 82
bob 91
charlie 82
diana 100
eric 91
```

## Sample Output

```text
diana
bob
eric
alice
charlie
```

## Explanation

- `diana` has the highest score: `100`
- `bob` and `eric` both have score `91`, so `bob` comes first
- `alice` and `charlie` both have score `82`, so `alice` comes first

## Suggested Topics

- `struct`
- `sort`
- custom comparator
