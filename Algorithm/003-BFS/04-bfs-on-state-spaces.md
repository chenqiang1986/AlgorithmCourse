# Lesson 4: BFS on State Spaces

This lesson studies an important idea:

- in BFS, a state does not need to be a graph node
- a state does not need to be one grid cell
- a state can be a whole configuration

Examples:

- the amount of water in several cups
- the on/off pattern of a light board
- the arrangement of tiles in a puzzle
- the positions of multiple objects at the same time

The key question is always:

> What information completely describes one state?

If we can describe a state clearly, and if every operation costs `1`, then BFS can often find the minimum number of operations.

## 1. What Changes in State-Space BFS?

The main BFS idea stays the same:

- put the start state into the queue
- expand all possible next states
- use `visited` or `dist` to avoid repeats
- the first time we reach a state is the minimum number of steps

What changes is the meaning of "state".

For example:

- in a graph problem, state might be `node = 7`
- in a grid problem, state might be `(row, col)`
- in a cup problem, state might be `(2, 5, 1)`
- in a light-board problem, state might be a `LightPattern`

So state-space BFS is still BFS.

We are just exploring a different kind of graph:

- the nodes are configurations
- the edges are legal operations

## 2. Reading Example 1: Measure 1 Unit of Water

### Problem

You are given `n` cups.

Cup `i` has capacity `capacity[i]`.

At the beginning, every cup is empty.

You may perform these operations:

- fill one cup completely from an unlimited water source
- empty one cup completely into a drain
- pour water from one cup into another until:
  - the first cup becomes empty, or
  - the second cup becomes full

Each operation costs `1` step.

Your task is to find the minimum number of steps needed so that **at least one cup contains exactly `1` unit of water**.

If it is impossible, return `-1`.

### Main BFS Idea

Here, one state is:

```text
(amount in cup 0, amount in cup 1, ..., amount in cup n - 1)
```

For example, if capacities are `[8, 5, 3]`, then:

```text
(0, 0, 0)
```

is the start state, and:

```text
(0, 5, 1)
```

is a state where the answer has already been reached.

### Reading Example Code

```cpp
#include <algorithm>
#include <map>
#include <queue>
#include <vector>
using namespace std;

vector<vector<int>> get_next_states(
    const vector<int>& current,
    const vector<int>& capacities
) {
    int n = static_cast<int>(current.size());
    vector<vector<int>> next_states;

    for (int i = 0; i < n; i++) {
        if (current[i] != capacities[i]) {
            vector<int> next = current;
            next[i] = capacities[i];
            next_states.push_back(next);
        }
    }

    for (int i = 0; i < n; i++) {
        if (current[i] != 0) {
            vector<int> next = current;
            next[i] = 0;
            next_states.push_back(next);
        }
    }

    for (int from = 0; from < n; from++) {
        for (int to = 0; to < n; to++) {
            if (from == to) {
                continue;
            }
            if (current[from] == 0) {
                continue;
            }
            if (current[to] == capacities[to]) {
                continue;
            }

            int moved = min(current[from], capacities[to] - current[to]);
            vector<int> next = current;
            next[from] -= moved;
            next[to] += moved;
            next_states.push_back(next);
        }
    }

    return next_states;
}

int min_steps_to_measure_one(const vector<int>& capacities) {
    vector<int> start(capacities.size(), 0);
    map<vector<int>, int> dist;
    queue<vector<int>> q;

    dist[start] = 0;
    q.push(start);

    while (!q.empty()) {
        vector<int> current = q.front();
        q.pop();

        for (int amount : current) {
            if (amount == 1) {
                return dist[current];
            }
        }

        for (const vector<int>& next : get_next_states(current, capacities)) {
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

The important lesson is:

- the queue stores whole cup configurations
- `dist[state]` means the minimum number of operations to reach that configuration

## 3. Class Practice 1: Minimum Steps to Measure 1 Unit

You are given `n` cup capacities.

Initially, all cups are empty.

You may:

- fill one cup completely
- empty one cup completely
- pour water from one cup into another until the source is empty or the destination is full

Each operation costs `1` step.

Find the minimum number of steps needed so that at least one cup contains exactly `1` unit of water.

If it is impossible, print `-1`.

### Input Format

The first line contains one integer:

```text
n
```

The second line contains `n` integers:

```text
capacity_1 capacity_2 ... capacity_n
```

### Output Format

Output one integer:

```text
minimum_number_of_steps
```

If it is impossible, output:

```text
-1
```

### Sample Input

```text
3
8 5 3
```

### Sample Output

```text
4
```

### Explanation

One optimal sequence is:

```text
fill the 3-unit cup
pour from the 3-unit cup into the 5-unit cup
fill the 3-unit cup
pour from the 3-unit cup into the 5-unit cup
```

After these `4` steps, one cup contains exactly `1` unit.

## 4. Reading Example 2: 3 x 3 Lights

### Problem

You are given a `3 x 3` board of lights.

Each light is either:

- `0` = off
- `1` = on

One operation chooses:

- one whole row, or
- one whole column

and flips all three lights in that row or column.

Flipping means:

- `0` becomes `1`
- `1` becomes `0`

Given a starting board, find the minimum number of operations needed to reach the state where **only the center light is on**.

If it is impossible, return `-1`.

### Main BFS Idea

Here, one state is the whole board.

A natural way to represent it is with a struct:

```cpp
struct LightPattern {
    vector<vector<int>> lights;
};
```

For example, this state:

```text
0 0 0
0 0 0
0 0 0
```

means all lights are off, and:

```text
0 0 0
0 1 0
0 0 0
```

means only the center light is on.

### Reading Example Code

```cpp
#include <map>
#include <queue>
#include <vector>
using namespace std;

struct LightPattern {
    vector<vector<int>> lights;

    bool operator<(const LightPattern& other) const {
        return lights < other.lights;
    }
};

void flip_one_light(LightPattern& pattern, int row, int col) {
    pattern.lights[row][col] = 1 - pattern.lights[row][col];
}

LightPattern flip_row(const LightPattern& pattern, int row) {
    LightPattern next = pattern;

    for (int col = 0; col < 3; col++) {
        flip_one_light(next, row, col);
    }

    return next;
}

LightPattern flip_col(const LightPattern& pattern, int col) {
    LightPattern next = pattern;

    for (int row = 0; row < 3; row++) {
        flip_one_light(next, row, col);
    }

    return next;
}

vector<LightPattern> get_next_states(const LightPattern& pattern) {
    vector<LightPattern> next_states;

    for (int row = 0; row < 3; row++) {
        next_states.push_back(flip_row(pattern, row));
    }
    for (int col = 0; col < 3; col++) {
        next_states.push_back(flip_col(pattern, col));
    }

    return next_states;
}

bool is_center_only_on(const LightPattern& pattern) {
    vector<vector<int>> target = {
        {0, 0, 0},
        {0, 1, 0},
        {0, 0, 0}
    };
    return pattern.lights == target;
}

int min_steps_to_center_only(const LightPattern& start) {
    map<LightPattern, int> dist;
    queue<LightPattern> q;

    dist[start] = 0;
    q.push(start);

    while (!q.empty()) {
        LightPattern current = q.front();
        q.pop();

        if (is_center_only_on(current)) {
            return dist[current];
        }

        for (const LightPattern& next : get_next_states(current)) {
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

Again, notice the important BFS idea:

- we are not moving on a board
- the whole board is the state

## 5. Class Practice 2: Reach the Center-Only Pattern

You are given a `3 x 3` light board.

Each cell contains:

- `0` for off
- `1` for on

One operation chooses one entire row or one entire column and flips all three lights in it.

Find the minimum number of operations needed to reach the configuration where only the center light is on.

If it is impossible, print `-1`.

### Input Format

The input contains `3` lines.

Each line contains a string of length `3` consisting only of `0` and `1`.

### Output Format

Output one integer:

```text
minimum_number_of_operations
```

If it is impossible, output:

```text
-1
```

### Sample Input

```text
111
010
111
```

### Sample Output

```text
2
```

### Explanation

One optimal sequence is:

```text
flip the top row
flip the bottom row
```

After these `2` operations, only the center light remains on.

## 6. Key Takeaways

- in BFS, a state can be a whole configuration
- the queue can store vectors, strings, boards, or other structured states
- the edges of the search graph are the legal operations
- if each operation costs `1`, BFS finds the minimum number of operations
- many puzzle and simulation problems are really state-space BFS problems
