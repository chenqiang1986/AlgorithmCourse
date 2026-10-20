# Lesson 2: Batch Gradient Descent
*ML / M05 — Optimizer*

## The question

The gradient-descent rule is always

$$
\theta \leftarrow \theta-\eta\nabla L(\theta),
$$

but which training examples should be used to estimate that gradient for one
update? The answer determines whether training is full-batch gradient descent,
stochastic gradient descent (SGD), or mini-batch gradient descent.

## Learning goals

By the end of this lesson, you should be able to:

1. distinguish an epoch from an optimizer step;
2. state how many examples each gradient-descent variant uses per step; and
3. implement a shuffled mini-batch training loop with the correct loss
   normalization.

## 1. One dataset, three update sizes

Suppose the training set is $D=\{(x_i,y_i)\}_{i=1}^n$, and an individual
example has loss $\ell_i(\theta)$. The empirical training loss is the mean

$$
L(\theta)=\frac{1}{n}\sum_{i=1}^{n}\ell_i(\theta).
$$

For any selected batch $B$, compute its mean loss and use its gradient:

$$
L_B(\theta)=\frac{1}{|B|}\sum_{i\in B}\ell_i(\theta),
\qquad
\theta \leftarrow \theta-\eta\nabla L_B(\theta).
$$

The update rule has not changed. Only the number of examples in $B$ has.

| Method | Examples used in one step | Steps in one epoch | Character of the gradient |
|---|---:|---:|---|
| **Full-batch gradient descent** | all $n$ | 1 | exact gradient of the training loss |
| **Stochastic gradient descent (SGD)** | 1 | $n$ | very noisy estimate |
| **Mini-batch gradient descent** | preset batch size $b$ | about $\lceil n/b\rceil$ | less noisy estimate |

An **optimizer step** means one parameter update. An **epoch** means one pass
through all $n$ training examples. Thus, with full-batch gradient descent,
one step is one epoch. With SGD, one step processes one sample, so an epoch
contains $n$ steps. With mini-batches, one step processes one batch of the
preset size $b$ (except that the final batch may be smaller), so an epoch
contains roughly $n/b$ steps.

For example, with $n=1{,}000$ and $b=64$:

| Method | Examples per step | Steps per epoch |
|---|---:|---:|
| Full batch | 1,000 | 1 |
| SGD | 1 | 1,000 |
| Mini-batch | 64 | 16 (15 batches of 64 and one batch of 40) |

## 2. Why mini-batches are the usual default

Full-batch updates are stable and directly optimize the entire training loss,
but each update must wait for every example. SGD updates immediately, but its
single-example gradients vary substantially from sample to sample. A
mini-batch is a practical compromise: it makes many updates per epoch while
using enough examples for efficient vectorized computation and a less noisy
gradient estimate.

The word *stochastic* emphasizes that the update is based on a sample rather
than the whole dataset. In common deep-learning usage, people often say
“SGD” even when the implementation uses mini-batches. When precision matters,
state the batch size.

## 3. A mini-batch loop

Shuffle the training examples before each epoch, then form disjoint batches.
Every example is used once in that epoch. This NumPy-style sketch uses a mean
squared error loss and updates once per batch:

~~~python
batch_size = 32
lr = 0.05

for epoch in range(num_epochs):
    order = rng.permutation(len(X_train))
    X_epoch = X_train[order]
    y_epoch = y_train[order]

    for start in range(0, len(X_epoch), batch_size):
        X_batch = X_epoch[start : start + batch_size]
        y_batch = y_epoch[start : start + batch_size]

        residual = X_batch @ w + b - y_batch
        grad_w = 2 / len(X_batch) * X_batch.T @ residual
        grad_b = 2 * residual.mean()

        w -= lr * grad_w
        b -= lr * grad_b
~~~

The denominator is `len(X_batch)`, not `len(X_train)`: this gradient is for
the **mean batch loss**. That also correctly handles the smaller final batch.
For full-batch gradient descent, set `batch_size = len(X_train)`; the inner
loop then makes exactly one update per epoch. For SGD, set `batch_size = 1`.

## 4. Compare training budgets carefully

“Train for 10 epochs” and “train for 10,000 steps” are different budgets.
Changing the batch size changes how many steps fit in an epoch. It can also
change the appropriate learning rate and the noisiness of the loss observed
after each step.

When comparing batch sizes, say which quantity is fixed:

- **Fixed epochs:** each method sees the same number of examples, but performs
  a different number of updates.
- **Fixed steps:** each method performs the same number of updates, but may
  see a very different number of examples.

Report both epochs and optimizer steps in experiments. For a smooth,
comparable training curve, evaluate the full training or validation loss at an
epoch boundary rather than treating a single mini-batch loss as the entire
dataset's loss.

## Key takeaways

- A step is one parameter update; an epoch is one pass over the training set.
- Full batch uses all examples per step: one step per epoch.
- SGD uses one example per step: $n$ steps per epoch for $n$ examples.
- Mini-batch gradient descent uses the preset batch size per step and has
  about $\lceil n/b\rceil$ steps per epoch.
- Normalize gradients by the current batch size, and shuffle before forming
  batches for each epoch.
