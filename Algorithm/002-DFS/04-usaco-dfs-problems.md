# Lesson 4: USACO DFS Problem List

This file is a curated set of official USACO problems where DFS is a central idea.

Use this list as a progression:

- start from direct flood fill
- move to changing state grids
- then try graph component problems

For each problem, ask yourself:

- what is the DFS state?
- what are the neighbors?
- do I need a `visited` array?
- what extra information should be computed during DFS?

## Suggested Starting Set
1. `Bronze` - [Milk Factory](https://usaco.org/index.php?page=viewproblem2&cpid=940)
2. `Bronze` - [Livestock Lineup](https://usaco.org/index.php?page=viewproblem2&cpid=965)

## Silver Level
1. `Silver` - [Switching on the Lights](https://usaco.org/index.php?page=viewproblem2&cpid=570)
   Grid DFS with reachability and state changes. A room may become lit later, so you need to think carefully about when a newly lit room becomes reachable.
2. `Silver` - [Build Gates](https://usaco.org/index.php?page=viewproblem2&cpid=596)
   A very instructive flood-fill problem. The standard trick is to double the grid scale so fence crossings are represented correctly.
3. `Silver` - [Why Did the Cow Cross the Road III](https://usaco.org/index.php?page=viewproblem2&cpid=716)
   Usually known by the file name `countcross`. DFS finds connected regions of the farm when road crossings are blocked.
4. `Silver` - [Mooyo Mooyo](https://usaco.org/index.php?page=viewproblem2&cpid=860)
   Repeated flood fill on a game board. DFS identifies same-color components, then simulation applies gravity.
5. `Silver` - [Icy Perimeter](https://usaco.org/index.php?page=viewproblem2&cpid=895)
   A classic connected-component problem. During flood fill, compute both area and perimeter of each ice blob.
6. `Silver` - [Fence Planning](https://usaco.org/index.php?page=viewproblem2&cpid=944)
   Graph connected components. DFS collects all cows in one component, then compute the smallest enclosing rectangle.
