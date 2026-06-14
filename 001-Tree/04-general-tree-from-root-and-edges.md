# Lesson 4: Building a General Tree From Root and Edges

In the previous lesson, the input directly told us the children of each node.

In many contest problems, especially in USACO-style problems, the input is more indirect:

- you are told which node is the root
- you are given all edges of the tree
- but each edge is just a connection between two nodes

So for an edge like `3 7`, you do **not** immediately know:

- is `3` the parent of `7`?
- or is `7` the parent of `3`?

This lesson shows how to recover the parent-child structure from that kind of input.

## 1. Typical Input Format

For a tree with `n` nodes, the input often gives:

1. the number of nodes `n`
2. the root id `root_id`
3. `n - 1` edges

Example:

```text
7 
1
1 2
1 3
1 4
2 5
2 6
4 7
```

This means:

- there are `7` nodes
- the root is node `1`
- the edges are:
  - `1 - 2`
  - `1 - 3`
  - `1 - 4`
  - `2 - 5`
  - `2 - 6`
  - `4 - 7`

Notice that an edge like `2 5` only means:

- node `2` and node `5` are connected

It does **not** say which one is the parent.

## 2. Why Is This Enough?

Because the graph is a tree:

- it is connected
- it has no cycle

And because the root is given, we can start from the root and move outward.

Then:

- the node we came from is the parent
- the newly discovered node is the child

So even though the input edges are undirected, the root allows us to assign direction.

## 3. Step 1: Store the Edges as an Undirected Graph

Before we know the parent-child relationship, the safest representation is:

```cpp
map<int, vector<int>> graph;
```

Here:

- `graph[u]` stores all neighbors of `u`
- each edge `u v` is added twice
  - `v` goes into `graph[u]`
  - `u` goes into `graph[v]`

For the sample input:

```text
7 1
1 2
1 3
1 4
2 5
2 6
4 7
```

the undirected graph is:

- `1`: `2, 3, 4`
- `2`: `1, 5, 6`
- `3`: `1`
- `4`: `1, 7`
- `5`: `2`
- `6`: `2`
- `7`: `4`

## 4. Step 2: Traverse From the Root

Now we start from the given root.

During DFS or BFS:

- when we move from node `u` to a new node `v`
- we decide that `u` is the parent of `v`

So we can fill:

- `tree[v].parent_id = u`
- `tree[u].child_ids.push_back(v)`

This is the key idea of the whole lesson.

## 5. Node Structure

We keep the same node structure from lesson 3.

```cpp
struct Node {
    int id;
    int parent_id;
    vector<int> child_ids;
};
```

And we still store the final tree in:

```cpp
map<int, Node> tree;
```

## 6. Example Walkthrough

Suppose the root is `1`.

We start at node `1`.

Its neighbors are:

- `2`
- `3`
- `4`

Since `1` is the root, these become its children.

Then from node `2`, the neighbors are:

- `1`
- `5`
- `6`

But `1` is the node we came from, so it is the parent, not a child.

So the new children of `2` are:

- `5`
- `6`

The same logic continues for the whole tree.

At the end, we get:

```text
1
├── 2
│   ├── 5
│   └── 6
├── 3
└── 4
    └── 7
```

## 7. DFS Solution

One simple method is DFS.

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

void ensure_node_exists(map<int, Node>& tree, int node_id) {
    if (!tree.count(node_id)) {
        tree[node_id] = {node_id, -1, {}};
    }
}

void build_rooted_tree(
    int current_id,
    int parent_id,
    const map<int, vector<int>>& graph,
    map<int, Node>& tree
) {
    ensure_node_exists(tree, current_id);
    tree[current_id].id = current_id;
    tree[current_id].parent_id = parent_id;

    for (int neighbor_id : graph.at(current_id)) {
        // Here is the magic to tell apart parent from child in the
        // neighbor list.
        if (neighbor_id == parent_id) {
            continue;
        }

        ensure_node_exists(tree, neighbor_id);
        tree[current_id].child_ids.push_back(neighbor_id);
        build_rooted_tree(neighbor_id, current_id, graph, tree);
    }
}

int main() {
    int n, root_id;
    cin >> n >> root_id;

    map<int, vector<int>> graph;

    // Read the edges and store neighbor relation in `graph`
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    map<int, Node> tree;
    build_rooted_tree(root_id, -1, graph, tree);

    // The sample code to output the tree data we built.
    // You can replace it with other code to process the tree.
    cout << "Root: " << root_id << '\n';
    cout << "Children of root: ";
    for (int child_id : tree[root_id].child_ids) {
        cout << child_id << ' ';
    }
    cout << '\n';

    return 0;
}
```

## 8. Practice

Use this input:

```text
8
10
10 20
10 30
10 40
20 50
20 60
70 40
80 60
```

Try to answer:

- which nodes are the children of `10`?
- which node is the parent of `80`?
- what is the pre-order traversal?
- what is the post-order traversal?

Then extend the program so it prints:

- the pre-order traversal
- the post-order traversal

## 12. Summary

In this lesson, we learned how to:

- read a general tree from a root id and undirected edges
- first store the input as an undirected graph
- run DFS from the root to assign parent-child direction
- build the final `map<int, Node>` with `parent_id` and `child_ids`
- prepare the tree for later algorithms such as subtree problems and tree DP
