# Lesson 1: Binary Tree Basics

This lesson introduces the binary tree, three classic traversal orders, and a simple way to store a tree in C++ without using pointers.

## 1. What Is a Tree?

A tree is a data structure made of nodes connected in a parent-child relationship.

Important terms:

- `root`: the top node of the tree
- `parent`: a node directly above another node
- `child`: a node directly below another node
- `leaf`: a node with no children
- `subtree`: a smaller tree starting from a node

A tree has no cycles. That means if we keep moving downward from a node, we will never come back to the same node again.

## 2. What Is a Binary Tree?

A binary tree is a tree where each node has at most:

- one left child
- one right child

Example:

```text
        1
      /   \
     2     3
    / \     \
   4   5     6
```

In this tree:

- `1` is the root
- `2` is the left child of `1`
- `3` is the right child of `1`
- `4`, `5`, and `6` are leaves

## 3. Why Do We Study Traversal?

Traversal means visiting every node in the tree in a certain order.

For binary trees, the most important traversal orders are:

- pre-order
- in-order
- post-order

These are the foundation for many later topics such as recursion, expression trees, searching, and tree-based dynamic programming.

## 4. Pre-order, In-order, and Post-order

For a node `X`, we can think about three actions:

- visit `X`
- traverse the left subtree
- traverse the right subtree

The difference between the three traversal methods is the position of `visit X`.

### 4.1 Pre-order

Order:

1. visit current node
2. traverse left subtree
3. traverse right subtree

Pattern:

```text
Node -> Left -> Right
```

For the example tree:

```text
        1
      /   \
     2     3
    / \     \
   4   5     6
```

Pre-order result:

```text
1 2 4 5 3 6
```

### 4.2 In-order

Order:

1. traverse left subtree
2. visit current node
3. traverse right subtree

Pattern:

```text
Left -> Node -> Right
```

For the same tree, in-order result:

```text
4 2 5 1 3 6
```

### 4.3 Post-order

Order:

1. traverse left subtree
2. traverse right subtree
3. visit current node

Pattern:

```text
Left -> Right -> Node
```

For the same tree, post-order result:

```text
4 5 2 6 3 1
```

## 5. A Simple Way to Store the Tree in C++

In many textbooks, trees are implemented with pointers. For this course, we will start with a simpler design:

- store all nodes in a `map`
- use node ids to represent connections
- store parent and child ids inside each node

This lets us focus on algorithms before dealing with pointer syntax and memory management.

## 6. Node Structure

We give every node a unique integer id.

```cpp
struct Node {
    int id;
    int parent_id;
    int left_child_id;
    int right_child_id;
};
```

Suggested meaning:

- `id`: this node's own id
- `parent_id`: the parent's id
- `left_child_id`: the left child's id
- `right_child_id`: the right child's id

When a parent or child does not exist, we can use `-1`.

Example:

```cpp
struct Node {
    int id;
    int parent_id;
    int left_child_id;
    int right_child_id;
};
```

```cpp
map<int, Node> tree;
```

Here:

- the key of the `map` is the node id
- the value is the full `Node`

So `tree[3]` means "the node whose id is 3".

## 7. Building a Small Tree

Let us store this tree:

```text
        1
      /   \
     2     3
    / \     \
   4   5     6
```

Possible C++ code:

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

int main() {
    map<int, Node> tree;

    tree[1] = {1, -1, 2, 3};
    tree[2] = {2, 1, 4, 5};
    tree[3] = {3, 1, -1, 6};
    tree[4] = {4, 2, -1, -1};
    tree[5] = {5, 2, -1, -1};
    tree[6] = {6, 3, -1, -1};

    int root_id = 1;

    cout << "Root id: " << root_id << '\n';
    cout << "Root left child: " << tree[root_id].left_child_id << '\n';
    cout << "Root right child: " << tree[root_id].right_child_id << '\n';

    return 0;
}
```

## 8. How Traversal Works with This Storage

Even though we are not using pointers, traversal is still easy.

For example, during pre-order traversal:

1. start from the root id
2. visit the current node
3. look up its left child id
4. look up its right child id
5. continue recursively

The main idea is:

- instead of moving through pointers
- we move through ids
- and use the `map` to find the next node

## 9. Pre-order Traversal Example in C++

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

void preorder(const map<int, Node>& tree, int node_id) {
    if (node_id == -1) {
        return;
    }

    const Node& node = tree.at(node_id);

    cout << node.id << ' ';
    preorder(tree, node.left_child_id);
    preorder(tree, node.right_child_id);
}

int main() {
    map<int, Node> tree;

    tree[1] = {1, -1, 2, 3};
    tree[2] = {2, 1, 4, 5};
    tree[3] = {3, 1, -1, 6};
    tree[4] = {4, 2, -1, -1};
    tree[5] = {5, 2, -1, -1};
    tree[6] = {6, 3, -1, -1};

    preorder(tree, 1);
    cout << '\n';

    return 0;
}
```

Output:

```text
1 2 4 5 3 6
```

## 10. Summary

In this lesson, we learned:

- a binary tree has at most two children per node
- pre-order is `Node -> Left -> Right`
- in-order is `Left -> Node -> Right`
- post-order is `Left -> Right -> Node`
- we can store a tree without pointers by using `map<int, Node>`
- each node stores ids instead of direct links

## 11. Practice Questions

1. Implement in-order and post-order traversal


