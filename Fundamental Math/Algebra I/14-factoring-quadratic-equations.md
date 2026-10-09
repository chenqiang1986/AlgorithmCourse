# Lesson 14: Factoring Quadratic Equations and Finding Roots
*Fundamental Math / Algebra I*

Factoring rewrites a quadratic as a product. Once the equation is equal to zero,
the zero-product property turns its factors into roots:

$$x^2+5x+6=(x+2)(x+3).$$

This lesson uses a dependable order: recognize a special case first, use a
cross-product chart for a general trinomial next, and use the quadratic formula
to force a factorization when integer factoring does not work.

## 1. The Zero-Product Property

**Theorem (Zero-Product Property).** If $AB=0$, then $A=0$ or $B=0$.

For example, from $(x-4)(x+1)=0$, either $x-4=0$ or $x+1=0$. Therefore,
$x=4$ or $x=-1$.

> The zero-product property applies only after one side of the equation is $0$.
> You may not split $(x-4)(x+1)=12$ into two separate equations.

## 2. Factors, Roots, and $x$-Intercepts

If

$$f(x)=a(x-r_1)(x-r_2),\qquad a\ne0,$$

then $f(x)=0$ when $x=r_1$ or $x=r_2$. The roots are also the $x$-coordinates of
the $x$-intercepts: $(r_1,0)$ and $(r_2,0)$. Remember that the sign reverses in
a factor: $(x-5)$ has root $5$, while $(x+5)$ has root $-5$.

## 3. The Factoring Decision Order

Before trying random pairs, use this order:

1. Move all terms to one side so the other side is $0$.
2. Factor out a GCF, if there is one.
3. Look for a special pattern: difference of squares or a perfect-square trinomial.
4. For a remaining trinomial, use the cross-product chart and try factor pairs.
5. If it will not factor conveniently, find the roots with the quadratic formula and
   write the factors from those roots.

After any factorization, set every variable-containing factor equal to $0$.

## 4. Special Cases First

These cases should be checked before the general method because they are usually
visible immediately.

### 4.1 Factor Out a Greatest Common Factor

**Example (A Root at Zero).** Solve $3x^2-12x=0$.

**Solution:**

Both terms share $3x$:

$$3x^2-12x=3x(x-4).$$

Thus $3x(x-4)=0$, so $x=0$ or $x-4=0$. The roots are
$\boxed{x=0\text{ or }x=4}$.

$\square$

The factor $x$ is $(x-0)$, so it reveals the intercept $(0,0)$.

### 4.2 Difference of Squares

$$a^2-b^2=(a-b)(a+b).$$

**Example (Difference of Squares).** Solve $9x^2-25=0$.

**Solution:**

$$9x^2-25=(3x)^2-5^2=(3x-5)(3x+5).$$

So $3x-5=0$ or $3x+5=0$. Therefore,
$\boxed{x=\frac53\text{ or }x=-\frac53}$.

$\square$

### 4.3 Perfect-Square Trinomial

$$a^2-2ab+b^2=(a-b)^2,\qquad a^2+2ab+b^2=(a+b)^2.$$

**Example (Repeated Root).** Solve $x^2-10x+25=0$.

**Solution:**

$$x^2-10x+25=(x-5)^2.$$

Then $(x-5)^2=0$, so $\boxed{x=5}$. This is a repeated (or double) root;
the graph touches the $x$-axis at $(5,0)$ rather than crossing it.

$\square$

## 5. General Trinomials: Cross-Product Chart and Try

For $ax^2+bx+c$, seek binomials $(px+q)(rx+s)$. Their products must satisfy

$$pr=a,\qquad qs=c,\qquad ps+qr=b.$$

The cross-products $psx$ and $qrx$ must add to the middle term $bx$. A chart keeps
this check organized:

| | First terms | Last terms |
|---|---:|---:|
| Choose factors | $px$ and $rx$ multiply to $ax^2$ | $q$ and $s$ multiply to $c$ |
| Cross-products | $psx$ | $qrx$ |
| Check | Together, they must equal $bx$ | |

Try factor pairs systematically. The signs of $q$ and $s$ must multiply to the sign
of $c$, and their cross-products must have the sign and size of $b$.

**Example (Monic Trinomial).** Solve $x^2+x-12=0$.

**Solution:**

The first terms must be $x$ and $x$. For $-12$, try $4$ and $-3$:

| Factor choice | Cross-products | Sum |
|---|---:|---:|
| $(x+4)(x-3)$ | $-3x$ and $4x$ | $x$ |

Since the cross-products sum to $x$, the factorization is correct:

$$x^2+x-12=(x+4)(x-3).$$

So $x+4=0$ or $x-3=0$. Hence $\boxed{x=-4\text{ or }x=3}$.

$\square$

**Example (Non-Monic Trinomial).** Solve $2x^2+x-6=0$.

**Solution:**

Choose $2x$ and $x$ for the first terms. For $-6$, try $-3$ and $2$:

| Factor choice | Cross-products | Sum |
|---|---:|---:|
| $(2x-3)(x+2)$ | $4x$ and $-3x$ | $x$ |

The cross-products add to the required middle term, so

$$2x^2+x-6=(2x-3)(x+2).$$

Thus $2x-3=0$ or $x+2=0$, giving
$\boxed{x=\frac32\text{ or }x=-2}$.

$\square$

## 6. Guaranteed Fallback: Use the Roots to Force the Factors

Some quadratics do not factor using integer pairs. The quadratic formula always finds
their roots (real or complex):

$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.$$

If its roots are $r_1$ and $r_2$, then the quadratic factors as

$$ax^2+bx+c=a(x-r_1)(x-r_2).$$

This is factorization by force: find the roots first, then build the factors from them.

**Example (Formula-Factored Quadratic).** Factor and solve $x^2+x-1=0$.

**Solution:**

Here $a=1$, $b=1$, and $c=-1$. The quadratic formula gives

$$
x=\frac{-1\pm\sqrt{1^2-4(1)(-1)}}{2(1)}
=\frac{-1\pm\sqrt5}{2}.
$$

Let $r_1=\frac{-1+\sqrt5}{2}$ and $r_2=\frac{-1-\sqrt5}{2}$. Therefore,

$$
x^2+x-1=
\left(x-\frac{-1+\sqrt5}{2}\right)
\left(x-\frac{-1-\sqrt5}{2}\right).
$$

The roots are $\boxed{x=\frac{-1\pm\sqrt5}{2}}$.

$\square$

If $b^2-4ac<0$, the same procedure factors the quadratic over the complex numbers.
If you are working only with real numbers, say that there are no real roots instead.

## 7. Common Errors to Avoid

- **Forgetting to make one side zero:** Rewrite $x^2+5x=14$ as
  $x^2+5x-14=0$ first.
- **Skipping the special-case check:** Factor a GCF before using a chart, or the root
  $x=0$ may be missed.
- **Getting a root's sign backward:** From $x+6=0$, the root is $x=-6$.
- **Stopping after factoring:** $(x-1)(x+7)=0$ still requires setting both factors to $0$.
- **Forcing integer pairs forever:** When no pair works, use the quadratic formula and
  write $a(x-r_1)(x-r_2)$.

## 8. Class Practice

**Problem (Special Case).** Solve $6x^2-15x=0$.

<details>
<summary>Solution</summary>

$$6x^2-15x=3x(2x-5)=0.$$

Thus $x=0$ or $2x-5=0$, so $\boxed{x=0\text{ or }x=\frac52}$.

$\square$

</details>

**Problem (Cross-Product Chart).** Solve $x^2-7x+10=0$, then state the $x$-intercepts.

<details>
<summary>Solution</summary>

Try $(x-5)(x-2)$. The cross-products are $-2x$ and $-5x$, which add to $-7x$:

$$x^2-7x+10=(x-5)(x-2)=0.$$

Thus $\boxed{x=5\text{ or }x=2}$, with intercepts $\boxed{(5,0)}$ and $\boxed{(2,0)}$.

$\square$

</details>

### More Cross-Product Chart Practice

For each problem, choose factors for the first and last terms, record the two
cross-products, and make sure their sum is the middle term before solving.

**Problem (Positive Middle Term).** Solve $3x^2+11x+6=0$.

<details>
<summary>Solution</summary>

Try $(3x+2)(x+3)$. Its cross-products are $9x$ and $2x$, and
$9x+2x=11x$:

$$3x^2+11x+6=(3x+2)(x+3)=0.$$

Therefore, $\boxed{x=-\frac23\text{ or }x=-3}$.

$\square$

</details>

**Problem (Mixed Signs).** Solve $4x^2-4x-15=0$.

<details>
<summary>Solution</summary>

Try $(2x-5)(2x+3)$. Its cross-products are $6x$ and $-10x$, and
$6x-10x=-4x$:

$$4x^2-4x-15=(2x-5)(2x+3)=0.$$

Therefore, $\boxed{x=\frac52\text{ or }x=-\frac32}$.

$\square$

</details>

**Problem (Different First-Term Pairs).** Solve $6x^2+7x-3=0$.

<details>
<summary>Solution</summary>

Try $(3x-1)(2x+3)$. Its cross-products are $9x$ and $-2x$, and
$9x-2x=7x$:

$$6x^2+7x-3=(3x-1)(2x+3)=0.$$

Therefore, $\boxed{x=\frac13\text{ or }x=-\frac32}$.

$\square$

</details>

**Problem (Challenge: Both Coefficients Matter).** Solve $12x^2-7x-10=0$.

<details>
<summary>Solution</summary>

Try $(3x+2)(4x-5)$. Its cross-products are $-15x$ and $8x$, and
$-15x+8x=-7x$:

$$12x^2-7x-10=(3x+2)(4x-5)=0.$$

Therefore, $\boxed{x=-\frac23\text{ or }x=\frac54}$.

$\square$

</details>

**Problem (Formula Fallback).** Factor and solve $x^2-2x-1=0$.

<details>
<summary>Solution</summary>

The quadratic formula gives $x=\frac{2\pm\sqrt{(-2)^2-4(1)(-1)}}2=1\pm\sqrt2$.
Therefore,

$$x^2-2x-1=(x-(1+\sqrt2))(x-(1-\sqrt2)),$$

and the roots are $\boxed{x=1\pm\sqrt2}$.

$\square$

</details>

## 9. Lesson Checklist

1. Put $0$ on one side of the equation.
2. Check a GCF, a difference of squares, and a perfect-square trinomial first.
3. For a general trinomial, choose factor pairs and verify them with the cross-products.
4. If no convenient pairs work, use the quadratic formula and write $a(x-r_1)(x-r_2)$.
5. Set each variable-containing factor equal to $0$ and check every root's sign.
