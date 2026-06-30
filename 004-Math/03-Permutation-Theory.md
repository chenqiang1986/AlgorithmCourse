# Permutation Theory

We only cover the very basic but very useful facts here.

A permutation of `1..n` means each number is mapped to exactly one number, and every number appears exactly once.

In this note, we interpret `p[i]` as:

- the thing currently at position `i`
- moves to position `p[i]`

For example, if

```text
p = [2, 3, 1, 5, 4]
```

it means:

- the thing at position `1` goes to position `2`
- the thing at position `2` goes to position `3`
- the thing at position `3` goes to position `1`
- the thing at position `4` goes to position `5`
- the thing at position `5` goes to position `4`

## Cycle Decomposition

If we keep applying the permutation from one starting point, eventually we must come back to a number we have seen before.
Because a permutation is one-to-one, we actually come back to the starting point and form a cycle.

For the above example:

- starting from `1`: `1 -> 2 -> 3 -> 1`, so we get cycle `(1 2 3)`
- starting from `4`: `4 -> 5 -> 4`, so we get cycle `(4 5)`

So the permutation can be written as

```text
(1 2 3)(4 5)
```

This is called decomposition into disjoint cycles.

### How to find the cycles

1. Start from a number not visited yet.
2. Keep jumping with the permutation.
3. Stop when you come back to the starting number.
4. Mark all numbers in this cycle as visited.
5. Repeat.

Example:

```text
p = [2, 1, 4, 5, 3, 6]
```

- `1 -> 2 -> 1`, so one cycle is `(1 2)`
- `3 -> 4 -> 5 -> 3`, so one cycle is `(3 4 5)`
- `6 -> 6`, so one cycle is `(6)`

Hence

```text
(1 2)(3 4 5)(6)
```

Usually we may omit cycles of length `1`, so this is often written as

```text
(1 2)(3 4 5)
```

## Order of a Permutation

The order of a permutation means:

- the smallest positive integer `k`
- such that applying the permutation `k` times gives the identity permutation

The key fact is:

- a cycle of length `m` returns to itself after exactly `m` applications
- disjoint cycles work independently

Therefore:

```text
order of permutation = lcm of all cycle lengths
```

### Example 1

```text
(1 2 3)(4 5)
```

The cycle lengths are `3` and `2`, so the order is

```text
lcm(3, 2) = 6
```

### Example 2

```text
(1 4 2 5 3)
```

There is only one cycle of length `5`, so the order is `5`.

### Example 3

```text
(1 2)(3 4 5)(6 7 8 9)
```

The cycle lengths are `2`, `3`, `4`, so the order is

```text
lcm(2, 3, 4) = 12
```

## How to Compute It in Code

If the permutation is given as an array `p`, where the thing at position `i` moves to position `p[i]`,
we can find every cycle length with a `visited` array.

```cpp
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int get_cycle_length(int start, const vector<int>& p, vector<bool>& visited) {
    int x = start;
    int len = 0;

    while (!visited[x]) {
        visited[x] = true;
        x = p[x];
        len++;
    }

    return len;
}

int main() {
    int n;
    cin >> n;

    vector<int> p(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> p[i];
    }

    vector<bool> visited(n + 1, false);
    long long order = 1;

    for (int i = 1; i <= n; i++) {
        if (visited[i]) {
            continue;
        }

        int len = get_cycle_length(i, p, visited);
        order = lcm(order, (long long)len);
    }

    cout << order << '\n';
    return 0;
}
```

The important idea is:

- each node belongs to exactly one cycle
- so total work is `O(n)`

## Composition of Two Permutations

Composition of permutations is exactly the same as function composition.

If we have two permutations `p` and `q`, then `p o q` means:

- apply `q` first
- then apply `p`

So for every number `x`,

```text
(p o q)(x) = p(q(x))
```

If we store permutations as arrays, then the composed permutation `r = p o q` satisfies

```text
r[i] = p[q[i]]
```

### Important Pitfall: Person vs Position

This is the most important thing to keep straight during composition.

For a permutation

```text
[a, b, c, d]
```

it does **not** mean:

- `person_1` goes to position `a`
- `person_2` goes to position `b`
- `person_3` goes to position `c`
- `person_4` goes to position `d`

That interpretation breaks during composition, because after one permutation, `person_i` is usually no longer at position `i`.

The correct interpretation is:

- the person currently at position `1` goes to position `a`
- the person currently at position `2` goes to position `b`
- the person currently at position `3` goes to position `c`
- the person currently at position `4` goes to position `d`

So when you apply another permutation in the middle, always track:

- which person is currently at each position

not:

- where the original `person_i` started

This is exactly why composition is function composition.
The first permutation changes the positions, and the second permutation acts on those new positions.

### Example

Let

```text
p = [2, 3, 1]
q = [3, 1, 2]
```

Then:

- `r[1] = p[q[1]] = p[3] = 1`
- `r[2] = p[q[2]] = p[1] = 2`
- `r[3] = p[q[3]] = p[2] = 3`

So

```text
r = p o q = [1, 2, 3]
```

which is the identity permutation.

One common mistake is the order:

- `p o q` is usually not the same as `q o p`

just like ordinary functions.

## Practice

1. Write a program to print the cycle decomposition of a given permutation.
2. 2023 Open Bronze 3rd: https://usaco.org/index.php?page=viewproblem2&cpid=1325
