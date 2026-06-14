# Lesson 2: Reading a Tree From Input

In real contest problems such as USACO, the tree is usually not already built for you in memory. Instead, you must read the input, build the tree yourself, and then run the algorithm.

In this lesson, we will learn how to:

1. read a binary tree from input
2. build the `map<int, Node>`
3. find the root
4. output pre-order, in-order, and post-order traversal

## 1. Input Format

We will start with a simple format.

The input gives:

1. the number of nodes `n`
2. for each node: `node_id left_child_id right_child_id`

Example:

```text
6
1 2 3
2 4 5
3 -1 6
4 -1 -1
5 -1 -1
6 -1 -1
```

This means:

- node `1` has left child `2` and right child `3`
- node `2` has left child `4` and right child `5`
- node `3` has no left child and has right child `6`
- nodes `4`, `5`, and `6` are leaves

We still use `-1` to mean "no child".

## 2. Our Goal

After reading the input, we want to print:

- pre-order traversal
- in-order traversal
- post-order traversal

For the sample input above, the output should be:

```text
1 2 4 5 3 6
4 2 5 1 3 6
4 5 2 6 3 1
```

## 3. Data Structure

We keep using the same node structure from the first lesson.

```cpp
struct Node {
    int id;
    int parent_id;
    int left_child_id;
    int right_child_id;
};
```

And we store all nodes in:

```cpp
map<int, Node> tree;
```

## 4. Why Do We Need `parent_id`?

The input format gives:

- node id
- left child id
- right child id

But it does not directly tell us the parent of each node.

We still want to fill `parent_id` because it helps us:

- keep the tree representation complete
- find the root more easily
- use the same structure consistently in future lessons

## 5. Building the Tree From Input

Suppose we read one line:

```text
2 4 5
```

That means node `2` has:

- left child `4`
- right child `5`

So we should:

1. create or update node `2`
2. store its `left_child_id` and `right_child_id`
3. if child `4` exists, set its `parent_id` to `2`
4. if child `5` exists, set its `parent_id` to `2`

## 6. Important Implementation Detail

Sometimes a child node is mentioned before its own full line appears in the input.

For example, after reading:

```text
1 2 3
```

we already know nodes `2` and `3` exist, even if their own lines have not been read yet.

So when we see a child id that is not `-1`, we should make sure that node exists in the `map`.

## 7. Complete C++ Example

```cpp
#include <iostream>
#include <map>
using namespace std;

struct Node {
    int id;
    int parent_id;
    int left_child_id;
    int right_child_id;
};

void ensure_node_exists(map<int, Node>& tree, int node_id) {
    if (node_id == -1) {
        return;
    }

    if (!tree.count(node_id)) {
        tree[node_id] = {node_id, -1, -1, -1};
    }
}


int main() {
    int n;
    cin >> n;

    map<int, Node> tree;

    for (int i = 0; i < n; i++) {
        int node_id, left_child_id, right_child_id;
        cin >> node_id >> left_child_id >> right_child_id;

        ensure_node_exists(tree, node_id);
        tree[node_id].id = node_id;
        tree[node_id].left_child_id = left_child_id;
        tree[node_id].right_child_id = right_child_id;

        if (left_child_id != -1) {
            ensure_node_exists(tree, left_child_id);
            tree[left_child_id].parent_id = node_id;
        }

        if (right_child_id != -1) {
            ensure_node_exists(tree, right_child_id);
            tree[right_child_id].parent_id = node_id;
        }
    }

    int root_id = -1;
    for (const auto& [node_id, node] : tree) {
        if (node.parent_id == -1) {
            root_id = node_id;
            break;
        }
    }

    // Further Code Here to Use the Tree, e.g. Traverse the tree.

    return 0;
}
```

## 8. Practice

How can we find the root of the tree?

Complete the program above, such that after constructing the tree, print the pre-order, in-order and post-order traversal.


### Practice Input

```text
7
10 4 15
4 2 7
15 -1 20
2 -1 -1
7 -1 -1
20 -1 -1
30 -1 -1
```

Before coding, think carefully:

- which node is the root?
- is every node connected to the root?

This is a good reminder that in contest problems, the input is often guaranteed to be valid, but when you practice on your own, you should still think about unusual cases.

### Better Practice Input

Here is a valid tree input for traversal practice:

```text
6
10 4 15
4 2 7
15 -1 20
2 -1 -1
7 -1 -1
20 -1 -1
```

Try to compute the three traversal orders by hand first, then test your code.

## 9. Summary

In this lesson, we learned how to:

- read a tree from input instead of hard-coding it
- build the `map<int, Node>` step by step
- set `parent_id` while reading children
- find the root by checking which node has no parent
- print pre-order, in-order, and post-order traversal

