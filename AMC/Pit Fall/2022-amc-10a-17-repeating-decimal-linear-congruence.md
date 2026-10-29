# AMC 10 2022 A, Problem 17 — Repeating Decimals and a Linear Congruence

> How many three-digit positive integers $\overline{abc}$ have nonzero digits
> $a,b,c$ and satisfy
>
> $$
> 0.\overline{abc}=\frac13\left(0.\overline a+0.\overline b+0.\overline c\right)?
> $$
>
> Here, a bar denotes repeating digits; for example,
> $0.\overline{abc}=0.abcabc\ldots$.

## Turn the decimal equation into an integer equation

Use the values of repeating decimals:

$$
0.\overline{abc}=\frac{100a+10b+c}{999}
\qquad\text{and}\qquad
0.\overline a=\frac a9.
$$

Substitution gives

$$
\frac{100a+10b+c}{999}
=\frac13\left(\frac a9+\frac b9+\frac c9\right).
$$

After clearing denominators and simplifying,

$$
63a=27b+36c,
\qquad\text{so}\qquad
7a=3b+4c.
$$

At this point, do **not** test all $9^3$ triples of nonzero digits. The useful feature of this equation is that its left side is a multiple of $7$.

## Method 1: Use divisibility to shrink the search

Since $7a=3b+4c$, the right side must be divisible by $7$:

$$
3b+4c\equiv0\pmod7.
$$

Because $-4\equiv3\pmod7$, this becomes

$$
3b\equiv-4c\equiv3c\pmod7.
$$

Cancel $3$ (it has inverse modulo $7$) to obtain

$$
b\equiv c\pmod7.
$$

Both $b$ and $c$ are digits from $1$ through $9$. Thus their difference can only be $0$, $7$, or $-7$. The only possible ordered pairs are

$$
(b,c)=(1,1),(2,2),\ldots,(9,9),(1,8),(8,1),(2,9),(9,2).
$$

There are only $13$ pairs to check, rather than $81$ possible pairs.

For each allowed pair, the equation determines $a$ uniquely:

$$
a=\frac{3b+4c}{7}.
$$


## Method 2: Compare each digit with $a$

Instead of reducing modulo $7$, rearrange

$$
7a=3b+4c
$$

as

$$
3(a-b)=4(c-a).
$$

Since $3$ and $4$ are relatively prime,

$$
3\mid(c-a)
\qquad\text{and}\qquad
4\mid(a-b).
$$

Because $a,b,c$ are nonzero digits, these divisibility restrictions leave only a few possible digit differences. It is then very easy to finish by checking those possibilities.

## Key Visualization

Once a digit problem becomes an integer-valued linear equation, look for a coefficient that forces a divisibility condition before enumerating digits. Here, reducing $7a=3b+4c$ modulo $7$ turns an $81$-case search for $(b,c)$ into just $13$ candidates.

Also, do not divide a congruence by a number automatically: cancellation modulo $n$ is valid only when that number is relatively prime to $n$. It is valid here because $\gcd(3,7)=1$.
