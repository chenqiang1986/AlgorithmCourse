# Lesson 14: Factoring Quadratic Equations and Finding Roots
*Fundamental Math / Algebra I*

Earlier quadratic lessons found roots by square roots and by completing the square. A
different method is often faster when the quadratic can be written as a product:

$$x^2+5x+6=(x+2)(x+3).$$

Factoring is not just a way to rewrite an expression. Once an equation is equal to zero,
each factor reveals a root. This lesson develops that connection and uses it to solve
quadratic equations.

## 1. The Zero-Product Property

The **zero-product property** says:

$$AB=0\quad\Longrightarrow\quad A=0\text{ or }B=0.$$

If neither $A$ nor $B$ were zero, their product could not be zero. This is the reason
factoring can solve an equation.

For example,

$$
(x-4)(x+1)=0
$$

is true when either factor is zero:

$$
x-4=0\quad\text{or}\quad x+1=0.
$$

Therefore, the roots are

$$\boxed{x=4\text{ or }x=-1}.$$

> The zero-product property applies only after one side of the equation is **zero**.
> You may not split $(x-4)(x+1)=12$ into $x-4=12$ or $x+1=12$.

## 2. Factors, Roots, and $x$-Intercepts

Suppose a quadratic function is written in factored form:

$$f(x)=a(x-r_1)(x-r_2),\qquad a\ne0.$$

To find its $x$-intercepts, set $f(x)=0$:

$$a(x-r_1)(x-r_2)=0.$$

The number $a$ is nonzero, so it cannot make the product zero. The product is zero when
$x-r_1=0$ or $x-r_2=0$. Thus:

- $r_1$ and $r_2$ are the **roots** (or solutions) of $f(x)=0$;
- $(r_1,0)$ and $(r_2,0)$ are the graph's **$x$-intercepts**;
- the signs in a factor are opposite the root: $(x-5)$ gives root $5$, while
  $(x+5)$ gives root $-5$.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 190" role="img" aria-labelledby="factor-roots-title factor-roots-desc" style="max-width:760px;width:100%;height:auto">
  <title id="factor-roots-title">Factored form reveals roots and x-intercepts</title>
  <desc id="factor-roots-desc">The equation f of x equals the product x minus 2 times x plus 3. Each factor is set to zero, giving roots 2 and negative 3, which are x-intercepts at 2 comma 0 and negative 3 comma 0.</desc>
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#34506b"/>
    </marker>
  </defs>
  <rect x="15" y="60" width="218" height="70" rx="10" fill="#eaf3fb" stroke="#34506b" stroke-width="2"/>
  <text x="124" y="90" text-anchor="middle" font-family="Arial, sans-serif" font-size="23" fill="#162b3d">f(x) = (x − 2)(x + 3)</text>
  <text x="124" y="113" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="#34506b">set f(x) equal to 0</text>
  <path d="M235,95 H305" stroke="#34506b" stroke-width="2.5" marker-end="url(#arrow)"/>
  <rect x="320" y="18" width="170" height="55" rx="8" fill="#fff6df" stroke="#926a18" stroke-width="2"/>
  <text x="405" y="51" text-anchor="middle" font-family="Arial, sans-serif" font-size="21" fill="#523d11">x − 2 = 0 → x = 2</text>
  <rect x="320" y="117" width="170" height="55" rx="8" fill="#fff6df" stroke="#926a18" stroke-width="2"/>
  <text x="405" y="150" text-anchor="middle" font-family="Arial, sans-serif" font-size="21" fill="#523d11">x + 3 = 0 → x = −3</text>
  <path d="M490,46 H555" stroke="#34506b" stroke-width="2.5" marker-end="url(#arrow)"/>
  <path d="M490,144 H555" stroke="#34506b" stroke-width="2.5" marker-end="url(#arrow)"/>
  <rect x="570" y="18" width="174" height="55" rx="8" fill="#e7f5eb" stroke="#317a4c" stroke-width="2"/>
  <text x="657" y="51" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" fill="#1f5132">x-intercept (2, 0)</text>
  <rect x="570" y="117" width="174" height="55" rx="8" fill="#e7f5eb" stroke="#317a4c" stroke-width="2"/>
  <text x="657" y="150" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" fill="#1f5132">x-intercept (−3, 0)</text>
</svg>

## 3. A Reliable Factoring-to-Roots Process

Use this order every time:

1. Move every term to one side so the equation is $0$ on the other side.
2. Factor the quadratic expression completely.
3. Set **each nonconstant factor** equal to $0$.
4. Solve the resulting linear equations.
5. Check by substituting the roots into the original equation, or by expanding the factors.

### Reading Example: A Monic Trinomial

Solve $x^2+x-12=0$.

We need two numbers with product $-12$ and sum $1$. They are $4$ and $-3$, so

$$
\begin{aligned}
x^2+x-12&=0\\
(x+4)(x-3)&=0.
\end{aligned}
$$

Now use the zero-product property:

$$
x+4=0\quad\text{or}\quad x-3=0.
$$

Therefore,

$$\boxed{x=-4\text{ or }x=3}.$$

For the function $y=x^2+x-12$, the roots give $x$-intercepts $(-4,0)$ and $(3,0)$.

## 4. Factoring When the Leading Coefficient Is Not 1

For $ax^2+bx+c$, look for two binomials whose first terms multiply to $ax^2$ and whose
last terms multiply to $c$. Check the middle terms by expanding or by combining the
cross-products.

### Reading Example: Non-Monic Trinomial

Solve $2x^2+x-6=0$.

The factors of $2x^2$ can be $2x$ and $x$; the factors of $-6$ can be $3$ and $-2$.
Try $(2x-3)(x+2)$:

$$
(2x-3)(x+2)=2x^2+4x-3x-6=2x^2+x-6.
$$

So

$$
\begin{aligned}
(2x-3)(x+2)&=0\\
2x-3&=0\quad\text{or}\quad x+2=0\\
x&=\frac32\quad\text{or}\quad x=-2.
\end{aligned}
$$

The roots are $\boxed{x=\frac32\text{ or }x=-2}$. Notice that a factor like $2x-3$
can produce a fractional root.

## 5. Factor Out a Greatest Common Factor First

Before factoring a trinomial, check whether every term has a **greatest common factor
(GCF)**. Factoring it out can reveal a root immediately.

### Reading Example: A Root at Zero

Solve $3x^2-12x=0$.

Both terms have $3x$ as a common factor:

$$
3x^2-12x=3x(x-4).
$$

Then

$$
3x(x-4)=0.
$$

The constant factor $3$ is never zero, but the other factors can be:

$$
x=0\quad\text{or}\quad x-4=0.
$$

Thus $\boxed{x=0\text{ or }x=4}$. The factor $x$ is really $(x-0)$, so it signals an
$x$-intercept at $(0,0)$.

## 6. Special Factor Patterns

Two patterns appear often in quadratic equations.

### Difference of Squares

$$a^2-b^2=(a-b)(a+b).$$

For example, solve $9x^2-25=0$:

$$
(3x-5)(3x+5)=0.
$$

So $3x-5=0$ or $3x+5=0$, giving

$$\boxed{x=\frac53\text{ or }x=-\frac53}.$$

### Perfect-Square Trinomial and a Repeated Root

$$x^2-10x+25=(x-5)^2=(x-5)(x-5).$$

Solving $x^2-10x+25=0$ gives $x=5$ twice. We call $5$ a **repeated root** (or double
root). On the graph, the parabola touches the $x$-axis at $(5,0)$ rather than crossing it.
This agrees with the one-intercept case from Lesson 13.

## 7. Factoring Is a Method, Not a Requirement

Not every quadratic factors nicely over the integers. For example, $x^2+x-1=0$ has no
integer pair whose product is $-1$ and sum is $1$. It still has real roots, but completing
the square or the quadratic formula is a better method.

When a quadratic does factor, factoring is usually faster than completing the square. It
also makes the roots and $x$-intercepts visible immediately.

## 8. Common Errors to Avoid

- **Forgetting to make one side zero:** Rewrite $x^2+5x=14$ as
  $x^2+5x-14=0$ before factoring.
- **Getting a root's sign backward:** From $(x+6)=0$, the root is $x=-6$.
- **Stopping after factoring:** $(x-1)(x+7)=0$ is not yet the solution; set each factor
  equal to zero.
- **Ignoring a GCF:** In $4x^2+20x=0$, factor $4x$ first; otherwise the root $x=0$ can
  be missed.
- **Using the zero-product property on a nonzero product:** It works for $AB=0$, not for
  $AB=9$.

## 9. Class Practice 1: Factor and Solve

### Problem

Solve $x^2-7x+10=0$. Then state the $x$-intercepts of $y=x^2-7x+10$.

<details>
<summary>Solution</summary>

The numbers $-5$ and $-2$ have product $10$ and sum $-7$:

$$
(x-5)(x-2)=0.
$$

Thus $x=5$ or $x=2$. The roots are $\boxed{2\text{ and }5}$, and the $x$-intercepts
are $\boxed{(2,0)\text{ and }(5,0)}$.

</details>

## 10. Class Practice 2: Leading Coefficient and GCF

### Problem

Solve $6x^2-15x=0$.

<details>
<summary>Solution</summary>

First factor out the GCF:

$$6x^2-15x=3x(2x-5).$$

Then

$$3x(2x-5)=0.$$

So $x=0$ or $2x-5=0$, which gives $x=\frac52$. The roots are
$\boxed{x=0\text{ or }x=\frac52}$.

</details>

## 11. Class Practice 3: Put Zero on One Side First

### Problem

Solve $x^2-2x=15$.

<details>
<summary>Solution</summary>

First subtract $15$ from both sides:

$$x^2-2x-15=0.$$

Now factor:

$$
(x-5)(x+3)=0.
$$

Therefore, $\boxed{x=5\text{ or }x=-3}$.

</details>

## 12. Lesson Checklist

Before leaving a factored quadratic equation, verify that:

1. One side of the equation is zero.
2. The expression is completely factored, including any GCF.
3. Each variable-containing factor has been set equal to zero.
4. Every root has been solved correctly, including its sign.
5. For $y=f(x)$, each real root has been translated into an $x$-intercept $(r,0)$.
