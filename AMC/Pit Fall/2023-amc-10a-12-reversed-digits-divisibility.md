# AMC 10 2023 A, Problem 12 — Reversed Digits and Divisibility

> How many three-digit positive integers $N$ satisfy both of the following?
>
> - $N$ is divisible by $7$.
> - The number formed by reversing the digits of $N$ is divisible by $5$.

## Key observation

A number is divisible by $5$ exactly when its last digit is $0$ or $5$.

The last digit of the reversed number is the first (hundreds) digit of $N$. Since $N$ is a three-digit number, that digit cannot be $0$. Therefore, $N$ must begin with $5$:

$$500 \le N \le 599.$$

## Count the multiples of $7$

The first and last multiples of $7$ in this interval are

$$
504=7\cdot72
\qquad\text{and}\qquad
595=7\cdot85.
$$

Thus the possible values of $N$ are

$$7\cdot72,7\cdot73,\ldots,7\cdot85,$$

so their number is

$$85-72+1=\boxed{14}.$$

## Pitfall

1. When counting an inclusive arithmetic sequence, remember the $+1$:

   $$\#\text{ terms}=\frac{\text{max}-\text{min}}{\text{stride}}+1.$$

   Here, that is $(595-504)/7+1=14$, not $13$.

2. Find the actual smallest and largest qualifying multiples before applying the count formula. Do not simply divide the width of a range by the stride (for example, use $100/7$ for the interval from $500$ to $599$). That shortcut happens to give the same numerical answer here, but it is unreliable: endpoint remainders can make the correct count one smaller or one larger than such an estimate.
