# M06: Supervised Learning — Linear Regression
*ML / Supervised Learning*

Linear regression is both a practical prediction method and a compact example
of optimization, linear algebra, regularization, automatic differentiation,
and statistical inference. This module develops it from each of those angles.

| Lesson | Topic |
| --- | --- |
| 1 | [The linear model, squared loss, and normal equations](01-linear-model-loss-and-normal-equations.md) |
| 2 | [Ridge and lasso regularization](02-ridge-and-lasso-regularization.md) |
| 3 | [Linear regression from scratch with NumPy](03-linear-regression-from-scratch-numpy.md) |
| 4 | [Linear regression from scratch with PyTorch](04-linear-regression-from-scratch-torch.md) |
| 5 | [Advanced: residual variance and degrees of freedom](05-residual-variance-and-degrees-of-freedom.md) |

The symbol $p$ denotes the number of fitted coefficients **including an
intercept column** when one is present. Code that uses a separate scalar bias
therefore has $p=d+1$ for $d$ input features.
