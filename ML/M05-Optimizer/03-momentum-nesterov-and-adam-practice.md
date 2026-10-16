# Practice Set 3: Implement Momentum, Nesterov, and Adam
*ML / M05 — Optimizer*

Implement every optimizer yourself with NumPy. Do not call `torch.optim`,
`jaxopt`, or an optimizer from another library. Initialize every state
variable explicitly and log enough values to debug the first few updates.

## Problem 1: One-dimensional momentum trace

For $f(x)=x^2$, start at $x_0=5$ with $v_0=0$, $\eta=0.1$, and $\beta=0.8$.
Compute the first four momentum updates by hand and confirm them in code. Make
a table with $t$, $x_t$, gradient, and $v_t$. Which update first crosses zero?

## Problem 2: Zigzag valley comparison

Minimize $f(x,y)=x^2+50y^2$ from $(6,6)$. Implement gradient descent and
classical momentum for 100 updates. Pick a stable rate for each and use
$\beta=0.9$ for momentum. Store every point and compare paths, final losses,
and updates needed to reach loss below $10^{-4}$.

## Problem 3: Momentum-state bug hunt

This code is intended to use momentum:

~~~python
for step in range(100):
    velocity = np.zeros_like(w)
    grad = gradient(w)
    velocity = 0.9 * velocity + grad
    w = w - 0.01 * velocity
~~~

Explain the bug, repair it, and demonstrate the difference on a
two-dimensional quadratic. Also explain why putting the velocity assignment
before gradient computation does not by itself make the implementation wrong.

## Problem 4: Nesterov at the correct point

Write `nesterov_step(theta, velocity, lr, beta, grad_fn)` for a vector
parameter. It must evaluate `grad_fn` at the look-ahead position. Test it for
$f(x)=3x^2$ from $x=2$, $v=1$, $\eta=0.1$, and $\beta=0.9$. Print look-ahead,
gradient there, next velocity, and next parameter.

## Problem 5: Compare classical and Nesterov

Use the same quadratic, start point, rate, and $\beta$ for both methods. Run
50 steps, and compare final loss and maximum loss after step 0. Does Nesterov
win for your chosen setup? Report the setup rather than claiming a universal
winner.

## Problem 6: Adam's first two steps

For scalar gradients $g_1=4$ and $g_2=2$, calculate the first two Adam updates
by hand with $\eta=0.01$, $\beta_1=0.9$, $\beta_2=0.999$, and
$\epsilon=10^{-8}$. Show $m_t$, $s_t$, $\hat m_t$, $\hat s_t$, and update
size. Confirm the values in code.

## Problem 7: Bias-correction ablation

Implement Adam twice on the linear-regression task from Practice Set 1: once
correctly and once using $m_t$ and $s_t$ directly. Use the same initialization
and data order. Log the first ten effective updates for one coefficient and
explain the difference.

## Problem 8: Coordinate-scale twist

Create a regression dataset where the second feature is 1,000 times larger than
the first. Train the same linear model with gradient descent, momentum, and
Adam. Tune each method over a small declared learning-rate grid. Compare best
validation loss and selected settings. Then standardize inputs and repeat.
What changes, and what does not?

## Problem 9: One reusable interface

Design a manual optimizer interface with `init(params)` and
`step(params, grads, state, step_number)`. Implement gradient descent,
momentum, and Adam behind it. Verify correct parameter shapes and that the
methods do not mutate gradient arrays. Use it for a fair 500-update comparison.

## Problem 10: Mini-batch experiment report

Train a small synthetic regression model with shuffled mini-batches for a fixed
number of updates. Compare SGD, momentum, Nesterov, and Adam. For each, report
learning rate, other hyperparameters, final training loss, validation loss, and
one observation from the loss curve. Include an honest conclusion tied to this
specific budget and dataset.
