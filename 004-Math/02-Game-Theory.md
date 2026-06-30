# Game Theory

We won't touch very deep on game theory, but it is necessary for us to understand the basics.

1. A Game system can be abstracted to a set of states $S$.
2. Each move is a transition from one state to another state.
3. The rule of the game essentially defines the valid transitions, namely from a given state, what states are valid to be transitioned to.

Easy to understand:
1. We say a state is Win condition if there exists a move to transition the state to a Lose condition.
2. We say a state is Lose condition if for all moves, the state will be transitioned to a Win condition.

## Simple example:
### Take 1 or 2 matches.
The game is like this, we have a pile of N matches. Each player is allowed to take either 1 or 2 matches, and the one who took the last match is the winner.

- By definition, easy to see N=1 or 2 is win condition.
- Then N=3 is a lose condition, because it can transition to either 1 or 2, both of them are win condition.
- Then N=4 is a win condition, because it can transition to N=3 which is lose condition.
- etc.

We can summarize that the win condition is that N mod 3 is not zero.

## Practice
In practice, the problem isn't that obvious and simple, and typically brute forcely using the win condition definition to check states is very inefficient.
Let's look at case by case:

2024 Feb Bronze 1st: https://usaco.org/index.php?page=viewproblem2&cpid=1395
2024 Dec Silver 1st: https://usaco.org/index.php?page=viewproblem2&cpid=1446

