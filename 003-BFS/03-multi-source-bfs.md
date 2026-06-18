# Lesson 3: Multi-Source BFS

This lesson studies a very useful BFS variation:

- the search does not start from one state
- the search starts from many states at the same time

This is called **multi-source BFS**.

## 1. What Is Multi-Source BFS?

In ordinary BFS:

- one start state goes into the queue first

In multi-source BFS:

- many start states go into the queue first

All of them begin at distance `0`.

After that, the algorithm is the same:

- pop from the queue
- expand neighbors
- assign distance `current + 1`

## 2. When Should We Use It?

Multi-source BFS is a natural fit when many positions are already active at time `0`.

Common examples:

- several fire sources spread through a grid
- several hospitals are all valid starting points
- several already-infected cells spread to neighbors
- several water sources fill nearby cells

The key trick is:

- push every starting state into the queue first
- give all of them distance `0`
- then run one normal BFS

## 3. Reading Example: Multi-Source Spread

### Problem

Suppose we have a grid where:

- `1` means the cell is already active
- `0` means the cell is inactive
- `-1` means the cell is blocked

Every minute, an active cell activates its four-direction neighbors if they are inactive.

We want to compute:

- the minimum number of minutes needed to activate every reachable inactive cell
- or `-1` if some inactive cell can never be activated

This is a standard multi-source BFS problem because all active cells are starting states at time `0`.

### Reading Example Code

```cpp
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

struct Cell {
    int row;
    int col;
};

bool in_bounds(int n, int m, Cell cell) {
    return 0 <= cell.row && cell.row < n && 0 <= cell.col && cell.col < m;
}

int minutes_to_activate_all(vector<vector<int>> grid) {
    int n = static_cast<int>(grid.size());
    int m = static_cast<int>(grid[0].size());
    vector<vector<int>> dist(n, vector<int>(m, -1));
    vector<Cell> directions = {
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1}
    };
    queue<Cell> q;

    for (int r = 0; r < n; r++) {
        for (int c = 0; c < m; c++) {
            if (grid[r][c] == 1) {
                dist[r][c] = 0;
                q.push({r, c});
            }
        }
    }

    int answer = 0;

    while (!q.empty()) {
        Cell current = q.front();
        q.pop();
        answer = max(answer, dist[current.row][current.col]);

        for (Cell delta : directions) {
            Cell next{
                current.row + delta.row,
                current.col + delta.col
            };

            if (!in_bounds(n, m, next)) {
                continue;
            }
            if (grid[next.row][next.col] != 0) {
                continue;
            }
            if (dist[next.row][next.col] != -1) {
                continue;
            }

            dist[next.row][next.col] = dist[current.row][current.col] + 1;
            q.push(next);
        }
    }

    for (int r = 0; r < n; r++) {
        for (int c = 0; c < m; c++) {
            if (grid[r][c] == 0 && dist[r][c] == -1) {
                return -1;
            }
        }
    }

    return answer;
}
```

Notice what changed compared with single-source BFS:

- we push many starting cells before the loop begins
- all of those cells get distance `0`

Everything else is just ordinary BFS.

## 4. Class Practice 1: Activation Time

You are given an `n x m` grid of integers.

Each cell is:

- `1` = already active
- `0` = inactive
- `-1` = blocked

Every minute, an active cell activates its four-direction neighbors if they are inactive.

Your task is to compute the minimum number of minutes needed to activate every reachable inactive cell.

If at least one inactive cell can never be activated, print `-1`.

### Input Format

The first line contains two integers:

```text
n m
```

The next `n` lines each contain `m` integers.

### Output Format

Output one integer:

```text
minimum_minutes
```

If some inactive cell can never be activated, output:

```text
-1
```

### Sample Input

```text
4 5
1 0 0 -1 0
0 -1 0 0 0
0 0 0 -1 0
-1 0 0 0 0
```

### Sample Output

```text
7
```

## 5. Key Takeaways

- multi-source BFS starts with many states in the queue at distance `0`
- after the initialization, the algorithm is the same as ordinary BFS
- this pattern is common in spread, infection, fire, and distance-to-nearest-source problems
- a `dist` array often works as both distance and visited

In the next lesson, we will study BFS on state spaces where one state can be a whole configuration.
