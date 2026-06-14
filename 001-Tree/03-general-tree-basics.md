# Lesson 3: General Tree Basics

In the first two lessons, we focused on binary trees, where each node has at most two children.

In this lesson, we move to a more general kind of tree:

- a node may have `0` children
- a node may have `1` child
- a node may have `2` children
- a node may have many children

This is usually called a **general tree**.

## 1. Binary Tree vs General Tree

A binary tree has at most:

- one left child
- one right child

A general tree only cares about the list of children.

Example:

```text
1
├── 2
│   ├── 5
│   └── 6
├── 3
└── 4
    └── 7
```

In this tree:

- node `1` has three children: `2`, `3`, `4`
- node `2` has two children: `5`, `6`
- node `3` has no children
- node `4` has one child: `7`

## 2. Why Do We Need a Different Structure?

For a binary tree, we can store:

- `left_child_id`
- `right_child_id`

But for a general tree, a node might have any number of children, so two fixed variables are not enough.

Instead, we store:

```cpp
vector<int> child_ids;
```

This means:

- if a node has no children, the vector is empty
- if a node has three children, the vector has three ids
- if a node has ten children, the vector has ten ids

## 3. Node Structure

We keep the same no-pointer idea from the earlier lessons.

```cpp
struct Node {
    int id;
    int parent_id;
    vector<int> child_ids;
};
```

Meaning:

- `id`: this node's own id
- `parent_id`: the parent's id
- `child_ids`: all children of this node

As before, we can use `-1` to mean "no parent", which is useful for the root.

## 4. Storing the Whole Tree

We still store all nodes in a `map`.

```cpp
map<int, Node> tree;
```

So:

- `tree[1]` means the node whose id is `1`
- `tree[4].child_ids` is the list of children of node `4`

## 5. Building a Small General Tree

Let us store this tree:

```text
1
├── 2
│   ├── 5
│   └── 6
├── 3
└── 4
    └── 7
```

Possible C++ code:

```cpp
#include <iostream>
#include <map>
#include <vector>
using namespace std;

struct Node {
    int id;
    int parent_id;
    vector<int> child_ids;
};

int main() {
    map<int, Node> tree;

    tree[1] = {1, -1, {2, 3, 4}};
    tree[2] = {2, 1, {5, 6}};
    tree[3] = {3, 1, {}};
    tree[4] = {4, 1, {7}};
    tree[5] = {5, 2, {}};
    tree[6] = {6, 2, {}};
    tree[7] = {7, 4, {}};

    int root_id = 1;

    cout << "Root id: " << root_id << '\n';
    cout << "Children of node 1: ";
    for (int child_id : tree[1].child_ids) {
        cout << child_id << ' ';
    }
    cout << '\n';

    return 0;
}
```

## 6. Traversal in a General Tree

For a general tree, the most natural traversals are:

- pre-order
- post-order

### 6.1 Pre-order

For a node `X`:

1. visit `X`
2. traverse each child from left to right

Pattern:

```text
Node -> Child 1 -> Child 2 -> Child 3 -> ...
```

For the example tree above, pre-order is:

```text
1 2 5 6 3 4 7
```

### 6.2 Post-order

For a node `X`:

1. traverse each child from left to right
2. visit `X`

Pattern:

```text
Child 1 -> Child 2 -> Child 3 -> ... -> Node
```

For the same tree, post-order is:

```text
5 6 2 3 7 4 1
```

## 7. Why Is There No In-order?

In-order traversal is special to binary trees because a binary tree has:

- a left subtree
- the node itself
- a right subtree

So the rule `Left -> Node -> Right` makes sense.

For a general tree, a node may have:

- zero children
- three children
- seven children

There is no single natural "middle" position for the node, so in-order traversal is usually not defined for a general tree.

## 8. Recursive Traversal Code

### Pre-order

```cpp
void preorder(const map<int, Node>& tree, int node_id) {
    cout << node_id << ' ';

    for (int child_id : tree.at(node_id).child_ids) {
        preorder(tree, child_id);
    }
}
```

The idea is very similar to binary tree recursion.

The only difference is that instead of:

- recurse on left child
- recurse on right child

we now:

- loop through all children
- recurse on each one

## 9. Reading a General Tree From Input

One possible input format is:

1. the number of nodes `n`
2. for each node:
   `node_id number_of_children child_1 child_2 ... child_k`

Example:

```text
7
1 3 2 3 4
2 2 5 6
3 0
4 1 7
5 0
6 0
7 0
```

This means:

- node `1` has `3` children: `2`, `3`, `4`
- node `2` has `2` children: `5`, `6`
- node `3` has `0` children
- node `4` has `1` child: `7`


## 10. Practice

Use the sample input below.

```text
8
10 3 20 30 40
20 2 50 60
30 0
40 1 70
50 0
60 1 80
70 0
80 0
```

Try to answer:

- Draw the tree diagram
- Write the code to read such data and construct the tree into a `map<int, Node>`
- Output its pre-order post-order traversal.

Then extend the program so it prints both traversals.

## 11. Summary

In this lesson, we learned that:

- a general tree allows any number of children
- `vector<int> child_ids` is a natural way to store those children
- pre-order and post-order work naturally on general trees
- in-order is usually not defined for general trees
