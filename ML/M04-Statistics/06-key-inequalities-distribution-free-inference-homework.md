# Lesson 6 Homework: Distribution-Free Confidence Bounds
*ML / M04 — Statistics*

Use the [Lesson 6 notes](./06-key-inequalities-distribution-free-inference.md)
as a reference. State the assumptions before using a bound, and distinguish a
guaranteed coverage lower bound from an exact confidence coefficient.

## Written analysis

1. **Markov and a risk threshold.** A nonnegative daily loss $L$ satisfies
   $E[L]=18$ dollars.

   - Use Markov's inequality to bound $P(L\ge120)$.
   - Find a threshold $c$ for which Markov guarantees $P(L<c)\ge0.95$.
   - Explain in one sentence why this result is not a confidence interval
     constructed from a sample mean.

2. **Chebyshev confidence interval.** Independent delivery times have an
   unknown distribution and variance known to be at most 36 minutes$^2$.
   A sample of $n=900$ deliveries has $\bar x=42$ minutes.

   - Construct a Chebyshev interval with coverage at least 95%.
   - Repeat for coverage at least 99%.
   - Explain why the 99% interval is wider.

3. **Chebyshev sample-size plan.** A measurement has variance at most 25.
   How many independent observations are sufficient for a Chebyshev interval
   with coverage at least 90% and margin at most 0.5? Show the inequality and
   round correctly.

4. **Hoeffding confidence interval.** A satisfaction score is guaranteed by
   the survey design to lie in $[0,10]$. From $n=1{,}000$ independent
   responses, $\bar x=7.4$.

   - Construct a 95% Hoeffding interval.
   - Intersect it with the feasible range if necessary.
   - State precisely what the 95% claim means in repeated sampling.

5. **Hoeffding sample-size plan.** A Bernoulli conversion indicator lies in
   $[0,1]$. Find the smallest $n$ that guarantees, by Hoeffding, a 99%
   confidence interval for the conversion probability with margin at most
   0.02.

6. **Method choice.** For each situation, choose the most appropriate
   starting method and justify your choice in 2–3 sentences: Markov,
   Chebyshev, Hoeffding, or the $t$ interval from Lesson 5.

   - A bounded quiz score from 0 to 20, with a population distribution of
     unknown shape.
   - A continuous laboratory measurement believed Normal after a diagnostic
     check, with unknown standard deviation.
   - A nonnegative insurance payout for which only an expected payout is
     known.

   End by stating one advantage and one limitation of distribution-free
   inequalities relative to $z$/$t$ methods.

## Challenge: guided proof of Hoeffding's inequality

This challenge develops the concentration bound used above. The individual
steps are deliberately guided; write a complete justification for each one.
You may use Markov's inequality and the factorization of moment-generating
functions for independent random variables.

### Part A: Hoeffding's lemma

Let $Y$ be a random variable such that $\mathbb E[Y]=0$ and $Y\in[a,b]$
almost surely, where $a<b$. (The case $a=b$ is immediate.) Prove

$$
\boxed{\mathbb E[e^Y]\leq\exp\left(\frac{(b-a)^2}{8}\right).}
$$

1. Verify that $e^x$ is convex.
2. Use the chord property of a convex function to show that, for every
   $y\in[a,b]$,

   $$
   e^y\leq\frac{b-y}{b-a}e^a+\frac{y-a}{b-a}e^b.
   $$

3. Take expectations and use $\mathbb E[Y]=0$ to obtain

   $$
   \mathbb E[e^Y]\leq\frac{b}{b-a}e^a+\frac{-a}{b-a}e^b.
   $$

4. Let $L=b-a$ and $t=b/L$. Check that $0\leq t\leq1$, that
   $a=(t-1)L$ and $b=tL$, and rewrite the preceding bound as

   $$
   \mathbb E[e^Y]\leq te^{(t-1)L}+(1-t)e^{tL}.
   $$

5. Define

   $$
   J(t,L)=\ln\!\left(te^{(t-1)L}+(1-t)e^{tL}\right).
   $$

   Compute $\partial J/\partial L$ and $\partial^2J/\partial L^2$.
6. Show that

   $$
   \frac{\partial^2J}{\partial L^2}
   =\frac{t(1-t)e^{-L}}{\bigl(1-t+te^{-L}\bigr)^2}\leq\frac14
   $$

   for all $0\leq t\leq1$ and $L\geq0$. Hint: apply
   $2AB\leq A^2+B^2$ with a useful choice of $A$ and $B$.
7. Check that $\frac{\partial J}{\partial L}(t,0)=0$. Integrate the bound
   from step 6 to show that

   $$
   \frac{\partial J}{\partial L}(t,L)\leq\frac L4.
   $$

8. Check that $J(t,0)=0$, then integrate once more to prove

   $$
   J(t,L)\leq\frac{L^2}{8}.
   $$

9. Return to step 5 and substitute $L=b-a$ to conclude Hoeffding's lemma.

### Part B: Hoeffding's inequality

Let $X_1,\ldots,X_n$ be independent random variables with
$X_i\in[a_i,b_i]$ almost surely. Write

$$
\mu_i=\mathbb E[X_i],\qquad
\overline X=\frac1n\sum_{i=1}^nX_i,\qquad
\mu=\mathbb E[\overline X]=\frac1n\sum_{i=1}^n\mu_i.
$$

Prove the two-sided bound

$$
\boxed{\Pr\bigl(|\overline X-\mu|>\epsilon\bigr)
\leq2\exp\!\left(-\frac{2n^2\epsilon^2}
{\sum_{i=1}^n(b_i-a_i)^2}\right).}
$$

1. First assume the upper-tail bound

   $$
   \Pr(\overline X-\mu>\epsilon)
   \leq\exp\!\left(-\frac{2n^2\epsilon^2}
   {\sum_{i=1}^n(b_i-a_i)^2}\right).
   $$

   Show that it implies the two-sided bound. Hint: apply the upper-tail bound
   to $-X_1,\ldots,-X_n$ to obtain the lower-tail bound, then use the union
   bound.

   Now let us prove the upper-tail bound.
2. For any $s>0$, show that

   $$
   \Pr(\overline X-\mu>\epsilon)
   =\Pr\!\left(e^{s(\overline X-\mu)}>e^{s\epsilon}\right).
   $$

3. Apply Markov's inequality to prove

   $$
   \Pr\!\left(e^{s(\overline X-\mu)}>e^{s\epsilon}\right)
   \leq e^{-s\epsilon}\mathbb E\!\left[e^{s(\overline X-\mu)}\right].
   $$

4. Use independence to show

   $$
   \mathbb E\!\left[e^{s(\overline X-\mu)}\right]
   =\prod_{i=1}^n\mathbb E\!\left[e^{(s/n)(X_i-\mu_i)}\right].
   $$

5. Apply Hoeffding's lemma to each factor and deduce

   $$
   \Pr(\overline X-\mu>\epsilon)
   \leq\exp\!\left(-s\epsilon+
   \frac{s^2}{8n^2}\sum_{i=1}^n(b_i-a_i)^2\right).
   $$

6. The bound holds for every $s>0$. Find the minimizing value $s^*$ and use
   it to derive the displayed upper-tail bound.
7. Complete the proof using step 1. Finally, simplify the result when the
   $X_i$ are i.i.d. and each lies in $[a,b]$.

## Coding: a distribution-free interval planner

Write three functions. Assume `data` is a nonempty list of independent
observations and every value is in the known, externally justified interval
`[lower_bound, upper_bound]`. Do **not** use the observed minimum and maximum
as these bounds.

```python
def hoeffding_interval(
    data: list[float], confidence: float,
    lower_bound: float, upper_bound: float
) -> tuple[float, float]:
    ...

def hoeffding_required_sample_size(
    confidence: float, margin: float,
    lower_bound: float, upper_bound: float
) -> int:
    ...

def chebyshev_required_sample_size(
    confidence: float, margin: float, sigma_squared: float
) -> int:
    ...
```

Validate that `0 < confidence < 1`, `margin > 0`,
`lower_bound < upper_bound`, and `sigma_squared > 0`. Also reject
data outside the supplied bounds.

1. `hoeffding_interval` returns the interval

   $$
   [\bar x-E_H,\bar x+E_H]\cap[a,b],
   \qquad
   E_H=(b-a)\sqrt{\frac{\ln(2/\alpha)}{2n}},
   \quad\alpha=1-C.
   $$

   The intersection with $[a,b]$ is valid because the true mean must itself
   be in that interval.

2. `hoeffding_required_sample_size` returns the smallest integer satisfying

   $$
   n\ge\frac{(b-a)^2\ln(2/\alpha)}{2E^2}.
   $$

3. `chebyshev_required_sample_size` returns the smallest integer satisfying

   $$
   n\ge\frac{\sigma^2}{\alpha E^2},
   $$

   where `sigma_squared` is the known population variance $\sigma^2$.

Test with:

```python
ratings = [3, 4, 5, 3, 4, 4, 2, 5, 4, 3]
print(hoeffding_interval(ratings, 0.95, 1, 5))
print(hoeffding_required_sample_size(0.95, 0.25, 1, 5))
print(chebyshev_required_sample_size(0.95, 0.25, 4))
```

For each printed result, give a one-sentence interpretation of the guarantee
and name the assumptions that make it valid.

## Simulation verification and comparison

Let $X\sim\operatorname{Bernoulli}(p)$ with $p=0.30$. This variable is
bounded in $[0,1]$, has mean $p$, and variance $p(1-p)=0.21$. Compare a 95%
Hoeffding interval, a 95% Chebyshev interval using the valid variance bound
$\sigma^2\le0.25$, and a 95% $z$ interval using the known true standard deviation
$\sqrt{0.21}$.

Use $n=200$ and $B=20{,}000$ independent batches. For every batch, form all
three intervals and record whether it contains the true $p$. Then report:

1. empirical coverage for each method;
2. the theoretical radius used by each method;
3. the mean interval width for each method; and
4. why all three coverages may be at least or near 95% while the widths are
   very different.

```python
import math
import numpy as np
from scipy.stats import norm

rng = np.random.default_rng(2028)
p = 0.30
n = 200
batches = 20_000
confidence = 0.95
alpha = 1 - confidence

samples = rng.binomial(1, p, size=(batches, n))
means = samples.mean(axis=1)

# TODO: calculate the three radii. For Chebyshev use sigma_squared = 0.25.
# For the z interval use the known population SD sqrt(p * (1 - p)).
radius_hoeffding = ...
radius_chebyshev = ...
radius_z = ...

# TODO: form lower/upper endpoints and calculate coverage.
# Clipping the Hoeffding interval to [0, 1] is allowed but not required.
coverage_hoeffding = ...
coverage_chebyshev = ...
coverage_z = ...

print(f"Hoeffding radius: {radius_hoeffding:.4f}; coverage: {coverage_hoeffding:.2%}")
print(f"Chebyshev radius: {radius_chebyshev:.4f}; coverage: {coverage_chebyshev:.2%}")
print(f"Known-sigma z radius: {radius_z:.4f}; coverage: {coverage_z:.2%}")
```

Finally, explain why the known-$\sigma$ $z$ interval is included only as a
benchmark here: in a real Bernoulli study, $p$ and hence its exact standard
deviation are unknown. Contrast that modeling issue with the distribution-free
guarantee supplied by Hoeffding.
