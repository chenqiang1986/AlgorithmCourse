# Lesson 1: BFS Basics

This lesson introduces the main idea of Breadth First Search, the queue-based code shape, and why generic graph BFS usually needs a `visited` structure.

## 1. What Is BFS?

BFS stands for **Breadth First Search**.

The main idea is:

- start from one state
- visit all states that are one move away
- then visit all states that are two moves away
- continue layer by layer

So BFS is a search that expands outward in rings.

## 2. BFS Thinks in Layers

Consider this graph:

```text
1 -- 2 -- 5
|    |
3 -- 4
```

If we start from node `1`, then the BFS layers are:

- distance `0`: `{1}`
- distance `1`: `{2, 3}`
- distance `2`: `{4, 5}`

This level-by-level idea is the most important mental model for BFS.

## 3. Why BFS Uses a Queue

A queue is perfect for BFS because it is **first in, first out**.

That means:

- the earliest discovered state is processed first
- older layer states are processed before newer layer states

So the queue naturally preserves BFS order.

## 4. The Smallest BFS Pattern

Here is the most important template:

```cpp
void bfs(State start_state) {
    queue<State> q;
    visited[start_state] = true;
    q.push(start_state);

    while (!q.empty()) {
        State current = q.front();
        q.pop();

        for (State next_state : all possible next states) {
            if (visited[next_state]) {
                continue;
            }

            visited[next_state] = true;
            q.push(next_state);
        }
    }
}
```

You should remember this shape.

Compared with DFS:

- DFS usually uses recursion or an explicit stack
- BFS usually uses a queue

## 5. Reading Example: BFS Order on a Graph

In this example:

- the graph is stored as `map<int, set<int>>`
- neighbors are processed in increasing order
- every node is created in the map in advance, so even an isolated node can have an empty set
- the function returns the visit order

```cpp
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;

vector<int> bfs_order(const map<int, set<int>>& node_to_neighbors, int start) {
    map<int, bool> visited;
    queue<int> q;
    vector<int> order;

    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        order.push_back(u);

        for (int v : node_to_neighbors.at(u)) {
            if (visited[v]) {
                continue;
            }

            visited[v] = true;
            q.push(v);
        }
    }

    return order;
}
```

Notice one important detail:

- we mark `visited[v] = true` when we push `v`
- not later when we pop `v`

This prevents the same node from being added to the queue many times.

## 6. Class Practice 1: Output BFS Traversal Order

You are given an undirected graph with nodes labeled `1` to `n`.

Start BFS from node `s`.

When a node has several neighbors, always visit the smaller-numbered neighbor first.

Output the order in which nodes are removed from the queue.

Only output nodes that are reachable from `s`.

### Input Format

The first line contains three integers:

```text
n m s
```

- `n` = number of nodes
- `m` = number of undirected edges
- `s` = starting node

The next `m` lines each contain two integers:

```text
u v
```

meaning there is an undirected edge between `u` and `v`.

### Output Format

Output one line containing the BFS traversal order:

```text
node_1 node_2 node_3 ...
```

### Sample Input

```text
6 5 1
1 2
1 3
2 4
2 5
3 6
```

### Sample Output

```text
1 2 3 4 5 6
```

### Explanation

From node `1`:

- layer `0` is `1`
- layer `1` is `2, 3`
- layer `2` is `4, 5, 6`

So the BFS order is:

```text
1 2 3 4 5 6
```

## 7. Why Generic Graph BFS Needs `visited`

Now look at this graph:

```text
1 -- 2
|    |
4 -- 3
```

If we do not record visited nodes, the queue may keep receiving the same nodes again and again:

```text
1 -> 2 -> 3 -> 4 -> 1 -> 2 -> ...
```

So for a general graph, `visited` is essential.

## 8. Reading Example: Count Connected Components with BFS

If a graph has several disconnected parts, we can run BFS from every unvisited node.

Each new BFS means:

- we found one new connected component

```cpp
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;

void bfs_component(
    int start,
    const map<int, set<int>>& graph,
    map<int, bool>& visited
) {
    queue<int> q;
    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : graph.at(u)) {
            if (visited[v]) {
                continue;
            }

            visited[v] = true;
            q.push(v);
        }
    }
}

int count_components(const map<int, set<int>>& graph) {
    map<int, bool> visited;
    int components = 0;

    for (const auto& [node, neighbors] : graph) {
        if (visited[node]) {
            continue;
        }

        components++;
        bfs_component(node, graph, visited);
    }

    return components;
}
```

This pattern is very common in graph problems.

## 9. Class Practice 2: Count Connected Components

You are given:

- the number of nodes
- the number of undirected edges
- the list of node ids
- the list of edges

The node ids are not guaranteed to be continuous.

Your task is to output the number of connected components.

Before reading the edges, create every node in the map first.

That means if a node has no neighbor at all, it should still exist in the graph as:

```text
graph[node_id] = {}
```

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

The graph has these connected components:

- `{10, 20, 35}`
- `{50, 80}`
- `{100}`

So the answer is:

```text
3
```

## 10. Class Practice 3: Print the Size of All Connected Components

You are given:

- the number of nodes
- the number of undirected edges
- the list of node ids
- the list of edges

The node ids are not guaranteed to be continuous.

Your task is to find the size of every connected component.

Output all component sizes in increasing order.

Before reading the edges, create every node in the map first.

That means if a node has no neighbor at all, it should still exist in the graph as:

```text
graph[node_id] = {}
```

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

Output one line containing all connected-component sizes in increasing order:

```text
size_1 size_2 size_3 ...
```

### Sample Input

```text
7 4
10 20 35 50 80 100 200
10 20
20 35
35 10
50 80
```

### Sample Output

```text
1 1 2 3
```

### Explanation

The graph has these connected components:

- `{10, 20, 35}` with size `3`
- `{50, 80}` with size `2`
- `{100}` with size `1`
- `{200}` with size `1`

After sorting the component sizes, we print:

```text
1 1 2 3
```

## 11. Common BFS Mistakes

### 11.1 Marking visited too late

In BFS, mark a node visited when you push it into the queue.

### 11.2 Forgetting to build both directions

For an undirected graph, if the input says `u v`, you usually need:

- `graph[u].insert(v)`
- `graph[v].insert(u)`

### 11.3 Assuming the graph is connected

If the problem asks about the whole graph, one BFS from one start node may not be enough.

### 11.4 Forgetting the required neighbor order

Some traversal-order problems require neighbors to be processed in increasing order.

## 12. Key Takeaways

- BFS explores states layer by layer
- the core data structure is a queue
- `visited` prevents repeated work and infinite loops
- one BFS can traverse one connected component
- repeated BFS can count connected components

In the next lesson, we will study the most common contest use of BFS: **shortest path in unweighted graphs and grids**.
