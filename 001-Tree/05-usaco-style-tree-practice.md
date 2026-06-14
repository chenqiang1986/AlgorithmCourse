# Lesson 5: USACO-Style Tree Practice

This lesson gives three practice problems in a contest style.

For each problem:

- read the statement carefully
- follow the input format exactly
- print the output in the required format exactly

In contest problems, a correct algorithm is not enough. The input and output format must also match perfectly.

## Problem 1: Tree Height

You are given a rooted general tree.

The input gives:

- the number of nodes
- the root id
- all `n - 1` edges

Each edge is undirected in the input, so you must first recover the parent-child relationship from the root.

Your task is to compute the **height** of the tree.

In this lesson, we define:

- the height of a leaf node as `0`
- the height of any other node as:
  `1 + max(height of each child)`
- the height of the whole tree as the height of the root

### Input Format

The first line contains two integers:

```text
n root_id
```

The next `n - 1` lines each contain two integers:

```text
u v
```

meaning there is an edge between node `u` and node `v`.

### Output Format

Output one integer:

```text
height
```

the height of the rooted tree.

### Sample Input

```text
8 10
10 20
10 30
10 40
20 50
20 60
40 70
60 80
```

### Sample Output

```text
3
```

### Explanation

One longest path from the root is:

```text
10 -> 20 -> 60 -> 80
```

This path has `3` edges, so the height is `3`.


## Problem 2: Pre-order + In-order -> Post-order

You are given a binary tree, but the tree itself is not directly provided.

Instead, you are given:

- its pre-order traversal
- its in-order traversal

Your task is to output the post-order traversal.

You may assume:

- all node values are distinct
- the input always describes a valid binary tree

### Input Format

The first line contains one integer:

```text
n
```

The second line contains `n` integers, the pre-order traversal.

The third line contains `n` integers, the in-order traversal.

### Output Format

Output one line containing `n` integers:

```text
postorder_traversal
```

Print the values in post-order, separated by spaces.

### Sample Input

```text
6
1 2 4 5 3 6
4 2 5 1 3 6
```

### Sample Output

```text
4 5 2 6 3 1
```

### Divide-and-Conquer Hint

This problem is a classic divide-and-conquer problem.

Think about one recursive step:

1. In pre-order, the first value is always the root of the current subtree.
2. Find that root in the in-order array.
3. Everything to the left of it in in-order belongs to the left subtree.
4. Everything to the right of it in in-order belongs to the right subtree.
5. Use the subtree sizes to split the pre-order array into:
   - root
   - left subtree part
   - right subtree part

Then solve the left subtree recursively, solve the right subtree recursively, and print:

```text
Left -> Right -> Root
```

That is exactly post-order.

### Small Example of the Split

Suppose:

```text
pre-order: 1 2 4 5 3 6
in-order:  4 2 5 1 3 6
```

For the whole tree:

- pre-order starts with `1`, so `1` is the root
- in in-order, `1` splits the array into:
  - left subtree: `4 2 5`
  - right subtree: `3 6`

So:

- left subtree size is `3`
- right subtree size is `2`

Then the pre-order array becomes:

- root: `1`
- left subtree part: `2 4 5`
- right subtree part: `3 6`

Now recursively solve:

- left subtree from `2 4 5` and `4 2 5`
- right subtree from `3 6` and `3 6`


## Problem 3: Lowest Common Ancestor Queries

You are given a rooted tree.

The input gives:

- the number of nodes
- the root id
- all `n - 1` edges
- `k` queries

Each edge is undirected in the input, so you must first recover the parent-child relationship from the root.

Each query contains two node ids. For each query, output their **lowest common ancestor (LCA)**, meaning the deepest node that is an ancestor of both nodes.

### Input Format

The first line contains two integers:

```text
n root_id
```

The next `n - 1` lines each contain two integers:

```text
u v
```

meaning there is an edge between node `u` and node `v`.

The next line contains one integer:

```text
k
```

The next `k` lines each contain two integers:

```text
a b
```

representing one query.

### Output Format

Output `k` lines.

For each query, print one integer:

```text
lca(a, b)
```

the lowest common ancestor of nodes `a` and `b`.

### Sample Input

```text
8 10
10 20
10 30
10 40
20 50
20 60
40 70
60 80
4
50 80
30 70
50 30
80 70
```

### Sample Output

```text
20
10
10
10
```

### Explanation

From the root `10`, the tree becomes:

- `10` is the parent of `20`, `30`, `40`
- `20` is the parent of `50`, `60`
- `40` is the parent of `70`
- `60` is the parent of `80`

Then:

- `LCA(50, 80) = 20`
- `LCA(30, 70) = 10`
- `LCA(50, 30) = 10`
- `LCA(80, 70) = 10`
