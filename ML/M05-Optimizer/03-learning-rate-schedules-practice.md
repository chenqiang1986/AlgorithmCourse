# Practice Set 3: Implement Learning-Rate Schedules
*ML / M05 — Optimizer*

Use your hand-written gradient and update code from Practice Set 1. Do not use
library schedulers. Every schedule should be a function returning the rate for
a supplied integer step.

## Problem 1: Schedule table

Implement with initial rate $0.08$:

1. step decay with $\gamma=0.5$ every 25 steps;
2. smooth exponential decay that is also multiplied by $0.5$ every 25 steps;
3. cosine decay from $0.08$ to $0.002$ over 100 steps.

Create a table of values at steps 0, 24, 25, 50, 75, and 100. Verify the step
and smooth exponential schedules agree at steps 0, 25, 50, 75, and 100.

## Problem 2: Guard the endpoints

Write `cosine_decay(step, max_lr, min_lr, total_steps)` that never returns
below `min_lr`, including after the horizon. Add assertions at step 0, at
`total_steps`, and beyond the horizon.

## Problem 3: Schedule a quadratic

Minimize $f(x)=4x^2$ from $x_0=5$ for 100 updates. Compare constant rate
$0.20$ with cosine decay from $0.20$ to $0.005$. Store iterates and losses.
Which reaches $f(x)<10^{-8}$ first? Explain why decay is not automatically
faster on this simple quadratic.

## Problem 4: Refactor a training loop

Take your full-batch linear-regression loop from Practice Set 1. Change it so
the loop accepts a function `lr_at_step(step)`. Run 300 steps with constant,
step, smooth exponential, and cosine decay. Print step, rate, and loss at
steps 0, 50, 100, 200, and 299.

## Problem 5: Deliberately mismatched clock

Suppose one epoch contains 10 mini-batch updates and a schedule was designed to
halve the rate every 5 epochs. Implement it incorrectly as “every 5 updates,”
then correctly as “every 50 updates.” List the rate after epochs 0 through 6
in both versions and explain the practical difference.

## Problem 6: Noisy mini-batches

Using synthetic regression data from Practice Set 1, train with batches of 16
for 1,000 updates. Compare constant rate $0.03$ and cosine decay from $0.03$
to $0.001$. Use the same shuffled batch sequence. Plot or tabulate a rolling
loss average and compare final full-dataset loss.

## Problem 7: Schedule parameter search

Hold model, initialization, and update budget fixed. Test at least six
configurations spanning constant, step, exponential, and cosine schedules.
For each, report initial rate, final rate, final training loss, and validation
loss. Choose using validation loss, not training loss.

## Problem 8: Warmup extension

Implement a schedule that rises linearly from $0$ to $0.05$ in 20 steps, then
uses cosine decay from $0.05$ to $0.001$ for 180 steps. Verify continuity at
the boundary and use it in the mini-batch experiment. State what the evidence
supports, including “not helpful on this dataset” if that is the result.
