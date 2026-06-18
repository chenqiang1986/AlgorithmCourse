# Lesson 2: Common BFS Problems

This lesson focuses on the most common situations where BFS is the right tool.

The big theme is:

> If every move has the same cost, BFS is often the correct shortest-path algorithm.

## 1. Common Use 1: Shortest Path in an Unweighted Graph

Suppose every edge has cost `1`.

Then BFS discovers nodes in this order:

- first all nodes at distance `0`
- then all nodes at distance `1`
- then all nodes at distance `2`
- and so on

So the first time BFS reaches a node, we already know the minimum number of edges needed to get there.

## 2. Reading Example: Distance from One Start Node

```cpp
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;

map<int, int> shortest_distances(
    const map<int, set<int>>& graph,
    int start
) {
    map<int, int> dist;
    queue<int> q;

    dist[start] = 0;
    q.push(start);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : graph.at(u)) {
            if (dist.count(v)) {
                continue;
            }

            dist[v] = dist[u] + 1;
            q.push(v);
        }
    }

    return dist;
}
```

Here:

- the graph is stored as `map<int, set<int>>`
- every node is assumed to already have a key in `graph`
- `dist.count(x) == 0` means node `x` has not been reached
- `dist[x] = k` means the shortest path uses exactly `k` edges

## 3. Class Practice 1: Minimum Number of Edges

You are given an undirected graph with nodes labeled `1` to `n`.

Find the minimum number of edges needed to travel from node `s` to node `t`.

If `t` is unreachable from `s`, print `-1`.

### Input Format

The first line contains four integers:

```text
n m s t
```

- `n` = number of nodes
- `m` = number of undirected edges
- `s` = start node
- `t` = target node

The next `m` lines each contain two integers:

```text
u v
```

meaning there is an undirected edge between `u` and `v`.

### Output Format

Output one integer:

```text
minimum_number_of_edges
```

If there is no path from `s` to `t`, output:

```text
-1
```

### Sample Input

```text
7 7 1 7
1 2
1 3
2 4
3 5
4 6
5 6
6 7
```

### Sample Output

```text
4
```

### Explanation

One shortest path is:

```text
1 -> 2 -> 4 -> 6 -> 7
```

It uses `4` edges.

## 4. Common Question: How Do We Print the Actual Path?

So far, BFS tells us the shortest distance.

A very common next question is:

> How do we print one actual shortest path?

The standard idea is:

- keep a `dist` map and a `parent` map
- when BFS first reaches `v` from `u`, record `parent[v] = u`
- after BFS finishes, walk backward from the target to the start
- reverse that sequence

Because BFS reaches each node for the first time along a shortest path, this parent chain gives us one shortest path.

## 5. Reading Example: Print One Shortest Path in a Graph

```cpp
#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;

vector<int> shortest_path(
    const map<int, set<int>>& graph,
    int start,
    int goal
) {
    map<int, int> dist;
    map<int, int> parent;
    queue<int> q;

    dist[start] = 0;
    parent[start] = -1;
    q.push(start);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (u == goal) {
            break;
        }

        for (int v : graph.at(u)) {
            if (dist.count(v)) {
                continue;
            }

            dist[v] = dist[u] + 1;
            parent[v] = u;
            q.push(v);
        }
    }

    if (!dist.count(goal)) {
        return {};
    }

    vector<int> path;
    for (int current = goal; current != -1; current = parent[current]) {
        path.push_back(current);
    }

    reverse(path.begin(), path.end());
    return path;
}
```

Here:

- if `dist.count(x) == 0`, then node `x` has not been reached yet
- `parent[v] = u` means we first reached `v` from `u`

That means:

- `u` is the node we used to first reach `v`
- so when we start at `goal` and keep following `parent`, we walk backward along a shortest path

## 6. Common Use 2: Shortest Path in a Grid

A grid can also be viewed as a graph:

- each cell is a node
- moving up, down, left, or right is an edge

If each move costs `1`, BFS gives the shortest number of steps.

## 7. Reading Example: Grid BFS

```cpp
#include <map>
#include <queue>
#include <string>
#include <vector>
using namespace std;

struct Position {
    int row;
    int col;

    bool operator<(const Position& other) const {
        if (row != other.row) {
            return row < other.row;
        }
        return col < other.col;
    }
};

bool in_bounds(int n, int m, Position pos) {
    return 0 <= pos.row && pos.row < n && 0 <= pos.col && pos.col < m;
}

int shortest_path_in_grid(
    const vector<string>& grid,
    Position start,
    Position goal
) {
    int n = static_cast<int>(grid.size());
    int m = static_cast<int>(grid[0].size());
    map<Position, int> dist;
    vector<Position> directions = {
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1}
    };
    queue<Position> q;

    dist[start] = 0;
    q.push(start);

    while (!q.empty()) {
        Position current = q.front();
        q.pop();

        if (current.row == goal.row && current.col == goal.col) {
            return dist[current];
        }

        for (Position delta : directions) {
            Position next{
                current.row + delta.row,
                current.col + delta.col
            };

            if (!in_bounds(n, m, next)) {
                continue;
            }
            if (grid[next.row][next.col] == '#') {
                continue;
            }
            if (dist.count(next)) {
                continue;
            }

            dist[next] = dist[current] + 1;
            q.push(next);
        }
    }

    return -1;
}
```

The same BFS pattern still works.

The only difference is:

- neighbors are generated from directions
- invalid cells and wall cells are skipped

## 8. Class Practice 2: Maze Shortest Path and Print One Route

You are given an `n x m` grid.

Each cell is one of:

- `S` = start
- `E` = exit
- `.` = open cell
- `#` = wall

You may move only:

- up
- down
- left
- right

Find the minimum number of steps needed to move from `S` to `E`.

Also print one shortest route.

If `E` is unreachable, print `-1`.

### Input Format

The first line contains two integers:

```text
n m
```

The next `n` lines each contain a string of length `m`, describing the grid.

### Output Format

If no path exists, output:

```text
-1
```

Otherwise output two lines:

```text
minimum_number_of_steps
path_string
```

Here `path_string` should use:

- `U` for up
- `D` for down
- `L` for left
- `R` for right

Its length should equal the minimum number of steps.

If there are several shortest routes, output any one of them.

### Sample Input

```text
5 6
S..#..
##.#..
...#..
.#...E
......
```

### Sample Output

```text
8
RRDDDRRR
```

The route `RRDDDRRR` means:

- right
- right
- down
- down
- down
- right
- right
- right

## 9. Key Takeaways

- BFS is the standard tool for shortest path when every move costs the same
- on graphs, distance usually means number of edges
- to print a path, record `parent` when you first discover a node or cell
- on grids, distance usually means number of steps
- a `dist` array often plays the role of both distance and visited

In the next lesson, we will study **multi-source BFS**, where the search begins from many starting states at the same time.
