# Finding a Percentile Value in a Normal Distribution

Let $X\sim N(\mu,\sigma^2)$, where $\mu$ is the mean and $\sigma$ is the standard deviation.

The $p-th$ percentile is the value $x_p$ with $p\%$ of the distribution at or below it:

$$
P(X\le x_p)=\frac{p}{100}.
$$

For example, the 90th percentile has left-tail probability $0.90$, not $90$.

Because a normal distribution is continuous and its CDF is increasing, each probability strictly between $0$ and $1$ has exactly one percentile value.

## Method 1: Work directly with the general CDF

Start from the percentile definition:

$$
P(X<x_p)=\frac{p}{100}.
$$

Because the normal distribution is continuous, $P(X<x_p)=P(X\le x_p)$. Thus, in terms of the general CDF,

$$
\operatorname{cdf}(\mu,\sigma^2,x_p)=\frac{p}{100}.
$$

Then apply the **inverse CDF** (also called the inverse normal, quantile function, or `invNorm`) to find $x_p$:

$$
x_p=\operatorname{cdf}^{-1}\!\left(\mu,\sigma^2,\frac{p}{100}\right).
$$

The superscript $-1$ means “inverse function”; it does **not** mean reciprocal. There is no simple elementary formula for the inverse of the normal CDF, so this step is normally done with technology or a table.

### Example

Suppose $X\sim N(70,4^2)$. Find the 90th percentile.

$$
\operatorname{cdf}(70,16,x_{90})=0.90
$$

Using the inverse CDF,

$$
x_{90}=\operatorname{cdf}^{-1}(70,16,0.90)\approx75.13.
$$

So about $90\%$ of values are at or below $75.13$.

## Method 2: Use a *z*-score

Start from the same percentile definition and standardize the random variable:

$$
P(X<x_p)
=P\!\left(\frac{X-\mu}{\sigma}<\frac{x_p-\mu}{\sigma}\right)
=P\!\left(Z<z(x_p)\right)
=\Phi\!\left(z(x_p)\right)
=\frac{p}{100},
$$

where

$$
z(x_p)=\frac{x_p-\mu}{\sigma}.
$$

Solving the equation $\Phi(z(x_p))=p/100$ gives

$$
z(x_p)=\Phi^{-1}\!\left(\frac{p}{100}\right)=:z_p.
$$

Now solve $\dfrac{x_p-\mu}{\sigma}=z_p$ for $x_p$:

$$
x_p=\mu+z_p\sigma.
$$

## Summary: move between a threshold, *z*-score, and probability

<svg viewBox="0 0 940 270" width="940" role="img" aria-labelledby="percentile-map-title percentile-map-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="percentile-map-title">Conversions between a normal-distribution threshold, z-score, and left-tail probability</title>
  <desc id="percentile-map-desc">A single row contains threshold x sub threshold, z-score, and P of X less than x sub threshold. Curved arrows above move from left to right using standardization and Phi. Curved arrows below move from right to left using inverse Phi and mu plus sigma z.</desc>
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 Z" fill="#0f766e"/></marker>
  </defs>
  <rect width="940" height="270" rx="14" fill="#fffdf8"/>
  <text x="470" y="35" text-anchor="middle" font-family="sans-serif" font-size="18" font-weight="600" fill="#1f2937">From a threshold to its left-tail probability</text>
  <g font-family="sans-serif" fill="#1f2937">
    <path d="M245 139 C280 69 322 69 357 139" fill="none" stroke="#0f766e" stroke-width="3" marker-end="url(#arrowhead)"/>
    <text x="301" y="79" text-anchor="middle" font-size="17" fill="#0f766e">(xₜ − μ) / σ</text>
    <path d="M575 139 C610 69 652 69 687 139" fill="none" stroke="#0f766e" stroke-width="3" marker-end="url(#arrowhead)"/>
    <text x="631" y="79" text-anchor="middle" font-size="18" fill="#0f766e">Φ</text>
    <path d="M357 159 C322 229 280 229 245 159" fill="none" stroke="#0f766e" stroke-width="3" marker-end="url(#arrowhead)"/>
    <text x="301" y="229" text-anchor="middle" font-size="17" fill="#0f766e">μ + σz</text>
    <path d="M687 159 C652 229 610 229 575 159" fill="none" stroke="#0f766e" stroke-width="3" marker-end="url(#arrowhead)"/>
    <text x="631" y="229" text-anchor="middle" font-size="18" fill="#0f766e">Φ⁻¹</text>
    <rect x="35" y="120" width="210" height="58" rx="10" fill="#e0f2fe" stroke="#0284c7"/>
    <text x="140" y="155" text-anchor="middle" font-size="21">threshold xₜ</text>
    <rect x="365" y="120" width="210" height="58" rx="10" fill="#f0fdf4" stroke="#16a34a"/>
    <text x="470" y="155" text-anchor="middle" font-size="21">z-score</text>
    <rect x="695" y="120" width="210" height="58" rx="10" fill="#fef3c7" stroke="#d97706"/>
    <text x="800" y="149" text-anchor="middle" font-size="18">probability</text>
    <text x="800" y="171" text-anchor="middle" font-size="17">P(X &lt; xₜ)</text>
  </g>
</svg>

### Same example

For the 90th percentile,

$$
z_{90}=\Phi^{-1}(0.90)\approx1.2816.
$$

Since $\mu=70$ and $\sigma=4$,

$$
x_{90}=70+(1.2816)(4)\approx75.13.
$$

This agrees with the general-CDF method.

## Choosing the correct tail probability

- “$p$th percentile” means **left-tail area** $p/100$.
- “The value with $q\%$ above it” means left-tail area $1-q/100$.
- The 50th percentile is the mean: $x_{50}=\mu$.
- Percentiles below 50 have negative *z*-scores; percentiles above 50 have positive *z*-scores.

For the meaning of the CDF and the standardization formula, see [Normal Distribution: PDF, CDF, and *z*-Scores](normal-distribution-pdf-cdf-and-z-scores.md).
