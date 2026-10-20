# M05: Optimizers
*ML / Mathematical Foundations*

An optimizer turns a loss gradient into a parameter update. This module starts
with gradient descent, distinguishes the examples used for each update, then
changes the step size over time, and finally adds memory and per-parameter
adaptation.

| Lesson | Topic | Practice |
|---|---|---|
| 1 | [Gradient descent and learning rates](01-gradient-descent-and-learning-rates.md) | [Manual gradient descent](01-gradient-descent-practice.md) |
| 2 | [Batch gradient descent](02-batch-gradient-descent.md) | — |
| 3 | [Learning-rate schedules](03-learning-rate-schedules.md) | [Manual schedules](03-learning-rate-schedules-practice.md) |
| 4 | [Momentum, Nesterov, and Adam](04-momentum-nesterov-and-adam.md) | [Manual optimizer variants](04-momentum-nesterov-and-adam-practice.md) |

The practice sets deliberately forbid `torch.optim` and similar optimizer
objects. Students should be able to see—and implement—the state and the update
rule before delegating it to a library.
