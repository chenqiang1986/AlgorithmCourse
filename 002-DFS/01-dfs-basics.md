# Lesson 1: DFS Basics

This lesson introduces the main idea of Depth First Search, the standard recursive code shape, and why generic DFS often needs a `visited` array.

## 1. What Is DFS?

DFS stands for **Depth First Search**.

The main idea is:

- start from one state
- go as deep as possible
- when we cannot continue, return
- then try the next choice

DFS is a very natural match for recursion because recursion already means:

- solve the current part
- call the same logic on a smaller next part

## 2. DFS Is Not Only for Trees

When students first see DFS, it is often on a tree.

For example:

- binary tree traversal
- general tree traversal

In a tree, if we always move from parent to child, there is no cycle, so we do not come back forever.

But DFS is much more general. It can be used on:

- graphs
- grids
- mazes
- permutations
- game states
- strings
- any "state space" where one state can move to several next states

That is why DFS is better understood as:

> "A way to explore a search space deeply."

## 3. Why Trees Usually Do Not Need `visited`

Suppose we have a rooted tree.

If DFS always goes:

- from a node
- to its children

then each edge is used in one direction only, so we will not get stuck in a loop.

Example:

```text
1
├── 2
│   ├── 4
│   └── 5
└── 3
```

Starting from `1`, we may visit:

```text
1 -> 2 -> 4
```

then return, then:

```text
2 -> 5
```

then return, then:

```text
1 -> 3
```

Everything is safe because the structure is already acyclic.

## 4. Why Generic Graph DFS Needs `visited`

Now look at a graph:

```text
1 -- 2
|    |
4 -- 3
```

If we start at `1` and always recurse to neighbors, this can happen:

```text
1 -> 2 -> 3 -> 4 -> 1 -> 2 -> 3 -> ...
```

This is an infinite loop.

So for a general graph, we usually need:

```cpp
visited[node] = true;
```

before exploring neighbors.

Then we only recurse to an unvisited neighbor.

## 5. The Smallest Recursive DFS Pattern

Here is the most important template:

```cpp
void dfs(State state) {
    visited[state] = true;

    for (State next_state : all possible next states) {
        if (visited[next_state] == false) {
            dfs(next_state);
        }
    }
}
```

You should remember this shape.

Most DFS problems are just this pattern with different meanings for:

- `state`
- `next_state`
- `visited`
- what we do before or after recursive calls


## 6. DFS on a Tree

The pre-order, in-order, post-order traversal on a tree is DFS.

Recall the code for pre-order 
```cpp
#include <iostream>
#include <map>
using namespace std;

struct Node {
    int id;
    int parent_id;
    vector<int> child_ids;
};

// Note: node_id is the state to start search.
void preorder(const map<int, Node>& tree, int node_id) {
    cout << node_id << ' ';

    // Note: enumeration of child_id is the
    // `Getting next state` from the current node_id.
    for (int child_id : tree.at(node_id).child_ids) {
        preorder(tree, child_id);
    }
}
```
As we explained that a valid Tree has no cycle, and thus we
do not need to keep visited.


## 7. A Full Example: Count Connected Components

This is one of the most common graph DFS tasks.

If the graph has several disconnected parts, we can run DFS from every unvisited node.

Each new DFS means:

- we found a new connected component

Let us study this graph:

```text
10 -- 20
|     |
35 ----

50 -- 80

100
```

This graph has three connected components:

- `{10, 20, 35}`
- `{50, 80}`
- `{100}`

This picture makes the task clearer:

- if DFS starts at `10`, it should visit `10`, `20`, and `35`
- if DFS starts at `50`, it should visit `50` and `80`
- if DFS starts at `100`, it should visit only `100`

Also notice that the first component contains a cycle:

```text
10 -> 20 -> 35 -> 10
```

Without `visited`, DFS could keep going around this cycle forever.

we will use:

- `map<int, vector<int>> graph`
- `map<int, bool> visited`

This makes the code work naturally even when node ids are like `10`, `20`, `35`, `100`, or any other values.

Code:

```cpp
#include <iostream>
#include <map>
#include <vector>
using namespace std;

void dfs(int u, const map<int, vector<int>>& graph, map<int, bool>& visited) {
    visited[u] = true;

    for (int v : graph[u]) {
        if (!visited[v]) {
            dfs(v, graph, visited);
        }
    }
}

int main() {
    map<int, vector<int>> graph;
    map<int, bool> visited;

    graph[10].push_back(20);
    graph[10].push_back(35);

    graph[20].push_back(10);
    graph[20].push_back(35);

    graph[35].push_back(10);
    graph[35].push_back(20);

    graph[50].push_back(80);
    graph[80].push_back(50);

    graph[100] = {};

    vector<int> all_nodes = {10, 20, 35, 50, 80, 100};

    int components = 0;

    for (int node : all_nodes) {
        if (!visited[node]) {
            components++;
            dfs(node, graph, visited);
        }
    }

    cout << components << '\n';
    return 0;
}
```

In this example:

- component 1 is `{10, 20, 35}`
- component 2 is `{50, 80}`
- component 3 is `{100}`

so the output is:

```text
3
```

## 8. Class Practice: Read Edges and Count Connected Components

Now let us turn the same idea into a small practice problem.

This time:

- do not hard-code the graph
- read the node ids and edges from the console
- build the graph using `map<int, vector<int>>`
- count how many connected components the graph has

### Problem

You are given:

- the number of nodes
- the number of undirected edges
- the list of node ids
- the list of edges

The node ids are not guaranteed to be continuous.

Your task is to output the number of connected components.

### Input Format

The first line contains two integers:

```text
n m
```

- `n` = number of nodes
- `m` = number of undirected edges

The second line contains `n` integers:

```text
node_id_1 node_id_2 ... node_id_n
```

The next `m` lines each contain two integers:

```text
u v
```

meaning there is an undirected edge between `u` and `v`.

### Output Format

Output one integer:

```text
number_of_connected_components
```

### Sample Input

```text
6 4
10 20 35 50 80 100
10 20
20 35
35 10
50 80
```

### Sample Output

```text
3
```

### Explanation

The graph is:

```text
10 -- 20
|     |
35 ----

50 -- 80

100
```

So the connected components are:

- `{10, 20, 35}`
- `{50, 80}`
- `{100}`
