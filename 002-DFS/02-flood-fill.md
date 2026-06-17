# Lesson 2: Flood Fill

Flood fill is one of the most important applications of DFS.

It appears in:

- counting islands
- maze exploration
- region size problems
- connected-component problems on grids
- many USACO Bronze and Silver problems

## 1. What Is Flood Fill?

Imagine we pour water into one cell of a grid.

The water spreads:

- up
- down
- left
- right

as long as the next cell is allowed.

DFS can simulate this spreading process.

That is why this technique is called **flood fill**.

## 2. A Typical Grid Problem

Suppose we have a grid of `'.'` and `'#'`:

```text
##...
#.#..
..##.
..##.
```

We may want to answer:

- how many connected `'#'` regions are there?
- what is the size of each region?
- what is the largest region?

This is exactly a DFS problem.

Each cell is a state:

- state = `(row, col)`

Each cell can move to up to four neighbors.

We can represent one cell with a small struct:

```cpp
struct Position {
    int row;
    int col;
};
```

## 3. The Core Flood Fill Idea

When we find a cell that belongs to a region and has not been visited:

1. start DFS from that cell
2. mark it visited
3. recursively expand to all valid neighbors
4. all reached cells belong to the same connected component

## 4. Directions in a Grid

In C++, a common pattern is:

```cpp
struct Position {
    int row;
    int col;
};

const Position directions[4] = {
    {-1, 0},
    {1, 0},
    {0, -1},
    {0, 1}
};
```

This means:

- `(-1, 0)`: up
- `(1, 0)`: down
- `(0, -1)`: left
- `(0, 1)`: right

Then we can loop through all four neighbors in one small loop.

## 5. Basic Flood Fill Code

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct Position {
    int row;
    int col;
};

const Position directions[4] = {
    {-1, 0},
    {1, 0},
    {0, -1},
    {0, 1}
};

bool in_bounds(const vector<string>& grid, Position pos) {
    int n = grid.size();
    int m = grid[0].size();
    int r = pos.row;
    int c = pos.col;
    return 0 <= r && r < n && 0 <= c && c < m;
}

void dfs(const vector<string>& grid, vector<vector<bool>>& visited, Position pos) {
    visited[pos.row][pos.col] = true;

    for (int dir = 0; dir < 4; dir++) {
        Position next{
            pos.row + directions[dir].row,
            pos.col + directions[dir].col
        };

        if (!in_bounds(grid, next)) {
            continue;
        }
        if (visited[next.row][next.col]) {
            continue;
        }
        if (grid[next.row][next.col] != '#') {
            continue;
        }

        dfs(grid, visited, next);
    }
}
```

This DFS visits all `'#'` cells connected to the starting cell.

## 6. Counting the Number of Regions

If we want the number of connected `'#'` components:

```cpp
int components = 0;

for (int r = 0; r < n; r++) {
    for (int c = 0; c < m; c++) {
        if (grid[r][c] == '#' && !visited[r][c]) {
            components++;
            dfs(grid, visited, {r, c});
        }
    }
}
```

Every time we start a new DFS:

- we found one new region

## 7. Counting the Size of One Region

Often we want more than just the number of regions.

We may want:

- area
- population
- connected empty cells
- perimeter

A common trick is to let DFS return the component size.

```cpp
int dfs_size(const vector<string>& grid, vector<vector<bool>>& visited, Position pos) {
    visited[pos.row][pos.col] = true;
    int size = 1;

    for (int dir = 0; dir < 4; dir++) {
        Position next{
            pos.row + directions[dir].row,
            pos.col + directions[dir].col
        };

        if (!in_bounds(grid, next)) {
            continue;
        }
        if (visited[next.row][next.col]) {
            continue;
        }
        if (grid[next.row][next.col] != '#') {
            continue;
        }

        size += dfs_size(grid, visited, next);
    }

    return size;
}
```

Now if we call `dfs_size(grid, visited, {r, c})`, it returns the number of cells in that whole connected component.

## 8. Example: Largest Region Size

```cpp
int best = 0;

for (int r = 0; r < n; r++) {
    for (int c = 0; c < m; c++) {
        if (grid[r][c] == '#' && !visited[r][c]) {
            best = max(best, dfs_size(grid, visited, {r, c}));
        }
    }
}
```

This is the core pattern behind many contest problems.

## 9. Flood Fill Is DFS on an Implicit Graph

Even though a grid does not look like a normal graph, it really is one.

Think of it like this:

- each cell is a node
- neighboring cells are edges

So flood fill is just graph DFS where:

- we do not store all edges explicitly
- we generate neighbors using the `directions` array

## 10. Four-Direction vs Eight-Direction

Sometimes connected means only:

- up
- down
- left
- right

Sometimes diagonal movement is also allowed.

Then we need eight directions instead of four.

So always check the problem statement carefully.

## 11. Practice

Try this flood fill problem:

Given an `n x m` grid of `'.'` and `'#'`, find every connected `'#'` region using four-direction movement:

- up
- down
- left
- right

For each region, compute its size.

Output all region sizes in increasing order.

If there is no `'#'` cell at all, print `0`.

### Example

Input:

```text
4 5
##...
#.#..
...##
...##
```

Output:

```text
1 3 4
```

Explanation:

- one region has size `3`
- one region has size `1`
- one region has size `4`

After sorting, we print:

```text
1 3 4
```

### Solution Idea

We scan every cell in the grid.

Whenever we find an unvisited `'#'` cell:

1. start flood fill from that cell
2. compute the size of that whole region
3. store the size in a list

At the end:

1. sort the list
2. print all sizes in increasing order


## 12. Common Flood Fill Mistakes

### 12.1 Forgetting the boundary check

Without `in_bounds`, your code may access invalid indices.

### 12.2 Mixing up row and column

Be consistent:

- row changes with `directions[dir].row`
- column changes with `directions[dir].col`

### 12.3 Marking `visited` too late

As in graph DFS, we usually mark immediately when entering the cell.

### 12.4 Forgetting to rebuild state between test cases

If the problem has multiple test cases, make sure to rebuild:

- `visited`
- counters
- sometimes the grid itself

### 12.5 Using the wrong definition of connectivity

Always check whether diagonal cells count.

## 13. What Else Can Flood Fill Compute?

Flood fill is not only for counting cells.

During DFS, we can also compute:

- perimeter of a shape
- sum of values in a region
- whether a region touches the boundary
- number of cows inside a component
- whether a region contains a special cell

So flood fill is often:

- DFS
- plus some local counting logic

## 14. Key Takeaways

- flood fill is DFS on a grid
- each cell is a state
- directions generate the neighbors
- one DFS call covers one whole connected component
- we can count area, perimeter, and many other properties while filling

In the next lesson, we will study a different style of DFS: using recursion as a **dynamic number of nested loops**.
