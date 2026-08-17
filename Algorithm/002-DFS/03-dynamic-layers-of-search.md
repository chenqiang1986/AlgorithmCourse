# Lesson 3: DFS as Dynamic Layers of Search

This lesson studies a very important idea:

- DFS is not only for graphs and grids
- DFS can also generate combinations of choices

This is the pattern behind:

- permutations
- subsets
- combinations
- N-Queens
- many backtracking problems

You can think of it as:

> DFS replaces a changing number of nested loops.

## 1. Why "Dynamic Layers of Loop"?

Suppose we want to print all 3-digit strings using digits `1` to `3`.

We could write:

```cpp
for (int a = 1; a <= 3; a++) {
    for (int b = 1; b <= 3; b++) {
        for (int c = 1; c <= 3; c++) {
            cout << a << b << c << '\n';
        }
    }
}
```

This works because the number of layers is fixed: exactly `3`.

But what if the number of layers is:

- `n`, read from input
- not known in advance
- different for different branches

Then hard-coded nested loops are impossible.

DFS solves this naturally.

## 2. The Recursive Search Tree

Imagine every step makes one choice.

Example: build a length-3 sequence using digits `1..3`.

At layer 0:

- choose the first digit

At layer 1:

- choose the second digit

At layer 2:

- choose the third digit

This forms a search tree.

DFS means:

- choose one option
- go to the next layer
- continue until the sequence is complete
- backtrack and try the next option

## 3. Generic Backtracking Template

```cpp
void dfs(int depth) {
    if (depth == target_depth) {
        output the current answer;
        return;
    }

    for (each candidate choice) {
        if (this choice is allowed) {
            make the choice;
            dfs(depth + 1);
            undo the choice;
        }
    }
}
```

This template is the heart of backtracking DFS.

The key new idea is:

- after recursion returns
- we must undo the choice

That is called **backtracking**.

## 4. Example: Print All Binary Strings of Length `n`

```cpp
#include <iostream>
#include <vector>
using namespace std;

void print_binary_string(const vector<int>& path) {
    for (int x : path) {
        cout << x;
    }
    cout << '\n';
}

void dfs(int depth, int n, vector<int>& path) {
    if (depth == n) {
        print_binary_string(path);
        return;
    }

    for (int bit = 0; bit <= 1; bit++) {
        path.push_back(bit);
        dfs(depth + 1, n, path);
        path.pop_back();
    }
}

int main() {
    int n;
    cin >> n;

    vector<int> path;
    dfs(0, n, path);
    return 0;
}
```

Why this works:

- each recursion layer decides one position
- `path` stores the current partial answer
- `push_back` means choose
- `pop_back` means undo

## 5. Example: Print All Permutations of `1..n`

Now each number can be used only once.

So we need a `used` array.

```cpp
#include <iostream>
#include <vector>
using namespace std;

void print_permutation(const vector<int>& path) {
    for (int x : path) {
        cout << x << ' ';
    }
    cout << '\n';
}

void dfs(int depth, int n, vector<int>& path, vector<bool>& used) {
    if (depth == n) {
        print_permutation(path);
        return;
    }

    for (int num = 1; num <= n; num++) {
        if (used[num]) {
            continue;
        }

        used[num] = true;
        path.push_back(num);

        dfs(depth + 1, n, path, used);

        path.pop_back();
        used[num] = false;
    }
}

int main() {
    int n;
    cin >> n;
    
    vector<int> path;
    vector<bool> used;
    used.assign(n + 1, false);
    dfs(0, n, path, used);
    return 0;
}
```

This pattern is extremely common.

The meaning of `visited` has changed:

- in graph DFS, `visited` prevents cycles
- here, `used` prevents reusing the same number in one permutation

So the deeper idea is the same:

- record which states or choices are already occupied

## 6. Practice: Subsets

For subsets, each element has two choices:

- take it
- do not take it

Try this on your own:

Given an array `a` of `n` integers, print all subsets of the array.

### Input Format

- the first line contains `n`
- the second line contains `n` integers: `a[0], a[1], ..., a[n - 1]`

### Output Format

- print every subset on its own line
- inside one line, print the chosen elements in the same order as in the array
- if a subset is empty, print an empty line

### Example

Input:

```text
3
5 7 9
```

One valid output:

```text

9
7
7 9
5
5 9
5 7
5 7 9
```

The order of subsets depends on your DFS order.

For each element, your DFS should decide:

- skip it
- include it

Think about:

- what parameter should represent the current position?
- what container should store the current subset?
- when is one subset complete and ready to print?

This is still DFS.

But now the branching rule is:

- skip current element
- take current element

## 7. Example: N-Queens

The classic problem is usually called **8 queens**, not "8 queues".

The goal:

- place 8 queens on an `8 x 8` chessboard
- no two queens attack each other

A queen attacks along:

- the same row
- the same column
- the same diagonal

The standard DFS idea is:

- place exactly one queen in each row
- at row `r`, try every column `c`
- if `(r, c)` is safe, place the queen and recurse to row `r + 1`

## 8. N-Queens Safety Recording

We can store:

- `used_col[c]`
- `used_diag1[r - c]`
- `used_diag2[r + c]`

If we use `map<int, bool>`, then diagonal ids can be negative, so no offset is needed.

Then safety checking becomes very fast.

## 9. N-Queens Code Skeleton

```cpp
#include <iostream>
#include <map>
#include <vector>
using namespace std;

void dfs(
    int row,
    int n,
    vector<int>& queen_col,
    map<int, bool>& used_col,
    map<int, bool>& used_diag1,
    map<int, bool>& used_diag2,
    int& answer_count
) {
    if (row == n) {
        answer_count++;
        return;
    }

    for (int col = 0; col < n; col++) {
        int d1 = row - col;
        int d2 = row + col;

        if (used_col[col] || used_diag1[d1] || used_diag2[d2]) {
            continue;
        }

        used_col[col] = true;
        used_diag1[d1] = true;
        used_diag2[d2] = true;
        queen_col[row] = col;

        dfs(row + 1, n, queen_col, used_col, used_diag1, used_diag2, answer_count);

        used_col[col] = false;
        used_diag1[d1] = false;
        used_diag2[d2] = false;
    }
}

int main() {
    int n = 8;
    vector<int> queen_col;
    map<int, bool> used_col;
    map<int, bool> used_diag1;
    map<int, bool> used_diag2;
    int answer_count = 0;

    queen_col.assign(n, -1);

    dfs(0, n, queen_col, used_col, used_diag1, used_diag2, answer_count);
    cout << answer_count << '\n';
    return 0;
}
```

This is a classic backtracking DFS.

## 10. Practice: Print All N-Queens Patterns

Now try a harder version on your own.

Instead of only counting the number of valid placements, print every valid board pattern.

Use:

- `Q` for a queen
- `.` for an empty cell

Each solution should be printed as an `n x n` board.

### Input Format

- one line containing `n`

### Output Format

- print every valid N-Queens board
- each solution should contain exactly `n` lines
- each line should contain exactly `n` characters
- print a blank line after each solution
- if there is no valid solution, print `0`

### Example

Input:

```text
4
```

One valid output:

```text
.Q..
...Q
Q...
..Q.

..Q.
Q...
...Q
.Q..
```

The order of solutions may be different, but every printed board must be valid.

Think about:

- how can `queen_col[row]` help you print one full board?
- what should the DFS do when `row == n`?
- how can you print one solution without changing the search logic too much?

## 11. Why Backtracking Works

At one recursion layer:

- we try one choice
- mark its effects
- go deeper

When we return:

- that branch is finished
- we must restore the old state
- then try the next choice

That restore step is why `pop_back` and unmarking arrays are necessary.

## 12. DFS as "Search Over Partial Answers"

For graph DFS, the state is often:

- current node

For backtracking DFS, the state is often:

- how much of the answer is already built
- which choices are already used

Examples:

- current permutation prefix
- current board placement
- current subset

This viewpoint is very important.

A lot of difficult problems become easier if you ask:

> "What is the current partial answer, and what are the next legal choices?"

## 13. Common Backtracking Mistakes

### 13.1 Forgetting to undo changes

If we `push_back` but never `pop_back`, later branches use the wrong state.

### 13.2 Using the wrong base case

You must clearly define:

- when is the answer complete?

Examples:

- `depth == n`
- `row == n`
- `index == a.size()`

### 13.3 Reusing a value that should be unique

Permutation problems usually need:

- `used[num]`

Without it, repeated values appear in the same permutation.

### 13.4 Not pruning impossible branches

If a partial answer is already invalid, stop early.

That is one of the main powers of backtracking.

For N-Queens:

- if a queen attacks another queen
- do not recurse deeper

## 14. When Should You Think of This DFS Style?

Think of backtracking DFS when the problem says:

- print all possibilities
- count all valid arrangements
- choose positions one by one
- fill slots one by one
- place objects under constraints

Keywords often include:

- all permutations
- all subsets
- all arrangements
- valid placements
- search all possibilities

## 15. Key Takeaways

- DFS can represent a dynamic number of nested loops
- recursion layers often correspond to positions, rows, or steps
- `path` stores the current partial answer
- `used` or marker arrays record occupied choices
- backtracking means: choose, recurse, undo

In the next lesson, we will look at real contest practice: a curated set of official USACO problems where DFS is the key tool.
