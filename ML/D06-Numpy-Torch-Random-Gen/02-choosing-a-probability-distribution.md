# Lesson 2: Choosing a Probability Distribution
*ML / D06-Numpy-Torch-Random-Gen*

The shape answers “how many values?” A probability distribution answers “what
kind of values?” Choosing a distribution is a modeling decision.

## 1. Distribution Guide

| Distribution | Values | Useful model |
|---|---|---|
| Uniform | any value in a fixed interval | random positions, bounded parameters |
| Normal (Gaussian) | any real value, concentrated near a mean | measurement noise, standardized features |
| Integer uniform | whole numbers in a fixed range | IDs, dice, random indices |
| Bernoulli | `0` or `1` | one yes/no event |
| Binomial | `0` through $m$ | successes in $m$ repeated trials |
| Poisson | nonnegative counts | arrivals or events per interval |
| Exponential | nonnegative real values | waiting time between events |
| Categorical | one label from several choices | class labels with chosen probabilities |

Do not select a distribution only because its API is convenient. Negative ages
from a normal distribution or fractional customer counts from a uniform
distribution are clues that the data model is mismatched.

## 2. Uniform and Normal

### NumPy

```python
import numpy as np

rng = np.random.default_rng(42)
shape = (1_000, 3)

uniform = rng.uniform(low=-2.0, high=2.0, size=shape)
normal = rng.normal(loc=10.0, scale=2.5, size=shape)
```

For the normal distribution, `loc` is the mean $\mu$ and `scale` is the
standard deviation $\sigma$, not the variance. Its variance is $\sigma^2$.

### PyTorch

```python
import torch

g = torch.Generator().manual_seed(42)
shape = (1_000, 3)

uniform = -2.0 + 4.0 * torch.rand(shape, generator=g)
normal = torch.normal(mean=10.0, std=2.5, size=shape, generator=g)
```

`torch.randn(shape)` is shorthand for a standard normal with mean $0$ and
standard deviation $1$:

```python
standard_normal = torch.randn(shape, generator=g)
normal_again = 10.0 + 2.5 * standard_normal
```

## 3. Bernoulli and Binomial

A Bernoulli random variable is $1$ with probability $p$ and $0$ with
probability $1-p$.

```python
# NumPy
clicked_np = rng.binomial(n=1, p=0.20, size=(1_000,))

# PyTorch
probabilities = torch.full((1_000,), 0.20)
clicked_torch = torch.bernoulli(probabilities, generator=g)
```

The sample mean should be near $p$ when the sample is large.

```python
print(clicked_np.mean())
print(clicked_torch.mean())
```

A binomial variable counts successes across $m$ independent trials:

```python
# Number of successes in 10 trials, with success probability 0.20
successes_np = rng.binomial(n=10, p=0.20, size=(1_000,))

binomial = torch.distributions.Binomial(total_count=10, probs=0.20)
successes_torch = binomial.sample((1_000,))
```

PyTorch distribution objects use the global random stream for `.sample()`.
Call `torch.manual_seed(seed)` before sampling when repeatability is needed.

## 4. Poisson Counts

A Poisson distribution is often used for counts observed during a fixed amount
of time or space. Its rate $\lambda$ is both its mean and its variance.

```python
# NumPy: calls received each hour, average rate 4.5
calls_np = rng.poisson(lam=4.5, size=(24,))

# PyTorch: one rate value for every desired output value
rates = torch.full((24,), 4.5)
calls_torch = torch.poisson(rates, generator=g)
```

Poisson samples are stored in a floating-point PyTorch tensor even though their
values are whole counts. Convert dtype only if the next operation requires it.

## 5. Exponential Waiting Times

When Poisson events occur at rate $\lambda$, the waiting time between events is
often modeled with an exponential distribution. Its mean is $1/\lambda$.

NumPy asks for `scale`, which is the mean waiting time:

```python
rate = 2.0
waiting_np = rng.exponential(scale=1.0 / rate, size=(1_000,))
```

PyTorch's in-place sampler asks for `lambd`, the rate:

```python
waiting_torch = torch.empty(1_000).exponential_(lambd=rate, generator=g)
```

This parameterization difference is easy to miss: NumPy uses $1/\lambda$ in
this call, while PyTorch uses $\lambda$.

## 6. Different Columns Can Use Different Distributions

Real feature matrices rarely have identically distributed columns.

```python
# NumPy
n = 500
age = rng.integers(18, 81, size=n)
income = rng.lognormal(mean=10.5, sigma=0.6, size=n)
visits = rng.poisson(lam=3.0, size=n)
is_member = rng.binomial(n=1, p=0.35, size=n)

X_np = np.column_stack([age, income, visits, is_member])
print(X_np.shape)  # (500, 4)
```

```python
# PyTorch
n = 500
age = torch.randint(18, 81, (n,), generator=g).float()
income = torch.empty(n).log_normal_(mean=10.5, std=0.6, generator=g)
visits = torch.poisson(torch.full((n,), 3.0), generator=g)
is_member = torch.bernoulli(torch.full((n,), 0.35), generator=g)

X_torch = torch.column_stack([age, income, visits, is_member])
print(X_torch.shape)  # torch.Size([500, 4])
```

Stacking promotes the columns to a common dtype. If the meaning of each column
matters, a pandas `DataFrame` may be more readable than a plain NumPy matrix.

## 7. Check That a Sample Resembles the Intended Distribution

```python
samples = rng.normal(loc=5.0, scale=2.0, size=100_000)

print(samples.mean())          # close to 5
print(samples.std(ddof=0))     # close to 2
print(np.quantile(samples, [0.01, 0.50, 0.99]))
```

“Close” is expected; exact equality would be suspicious. Small random samples
can differ substantially from theoretical values.

## 8. Class Practice

For each story, select a distribution and generate 10,000 observations in both
NumPy and PyTorch:

1. A sensor error centered at zero, usually between about `-0.3` and `0.3`.
2. Whether each visitor buys a product, with probability `0.08`.
3. The number of support tickets per hour, averaging `6`.
4. A randomized dosage between `2.5` and `5.0` units.
5. The waiting time between arrivals occurring at a rate of `3` per minute.

For each result, print its shape, minimum, maximum, mean, and standard deviation.

## 9. Key Takeaways

- Match support first: can the distribution produce only valid values?
- Normal APIs usually take standard deviation, not variance.
- NumPy exponential sampling uses a scale; PyTorch's `exponential_` uses a rate.
- Generate feature columns separately when they represent different processes.
- Use sample summaries to catch incorrect parameters early.

