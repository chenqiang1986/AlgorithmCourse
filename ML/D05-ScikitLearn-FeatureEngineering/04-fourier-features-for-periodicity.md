# Lesson 4: Fourier Features for Periodic Data
*ML / D05-ScikitLearn-FeatureEngineering*

Walmart's weekly sales are quasi-periodic: they rise every year around the same holiday season, then fall back, then rise again the next year. Lesson 3 modeled time using `Month` and raw polynomial terms — but polynomial terms are built to bend smoothly, not to repeat. This lesson introduces `FourierFeatures`, a transformer purpose-built for repeating patterns.

## 1. Why a Repeating Pattern Breaks Polynomial Features

A single polynomial term $x^d$ is smooth and, past low degrees, essentially monotonic — it doesn't turn around and come back down the way a real yearly sales cycle does. Approximating several full up-and-down cycles with polynomial terms alone would require pushing the degree very high, and Lesson 3 just showed what happens numerically once the degree climbs that far without care: unscaled high powers destabilize the fit, and even scaled ones don't naturally produce a repeating shape — they just bend more.

## 2. Fourier Series Theory

A **Fourier series** writes a periodic function as a sum of sine and cosine waves of increasing frequency:

$$
f(x) \approx \frac{a_0}{2} + \sum_{n=1}^{N} \left[ a_n \cos\left(\frac{2\pi n x}{L}\right) + b_n \sin\left(\frac{2\pi n x}{L}\right) \right]
$$

where $L$ is the period of $f$ and $a_n$, $b_n$ are coefficients (one pair per harmonic $n$) that say how much of that harmonic's wave is present in $f$. We won't derive the formulas for $a_n$ / $b_n$ here — that's a Real Analysis topic. The part that matters for this lesson: **almost any repeating shape can be built by adding up enough sine/cosine waves of the right frequencies and heights**, and the more harmonics $N$ you add, the closer the sum gets to $f$.

### Worked Example: The Square Wave

The square wave — flat at $+1$, then flat at $-1$, switching abruptly every half period — has a well-known Fourier series using only odd harmonics:

$$
\text{square}(x) = \frac{4}{\pi}\left(\sin x + \frac{1}{3}\sin 3x + \frac{1}{5}\sin 5x + \frac{1}{7}\sin 7x + \cdots\right)
$$

Two things to notice before even plotting it:

- Each term's height shrinks like $1/n$, so low harmonics ($n = 1, 3$) contribute far more than high ones ($n = 13, 15$).
- Only odd $n$ appear at all — the square wave's own symmetry cancels every even harmonic's coefficient to zero.

Partial sums, first few terms:

- $N=1$: $\frac{4}{\pi}\sin x$ — a single smooth sine wave. Rises, peaks, falls, roughly on schedule, but nothing square about it.
- $N=3$: $\frac{4}{\pi}\left(\sin x + \frac{1}{3}\sin 3x\right)$ — the top and bottom start flattening into plateaus.
- $N=5$: adds $\frac{1}{5}\sin 5x$ — flatter still, with a hint of the sharp corners forming.
- $N=15$ (all odd harmonics $1, 3, 5, \ldots, 15$): unmistakably square, with small ripples clinging to each corner that shrink but never fully vanish as $N$ grows (the Gibbs phenomenon).

### Class Practice: Build It in Desmos

Open [desmos.com/calculator](https://www.desmos.com/calculator) and reconstruct the square wave one harmonic at a time.

1. Define a slider: type `N=1` and let Desmos turn it into a draggable slider (integer steps, range roughly 0 to 20).
2. Type the partial sum directly using Desmos's summation notation:
   ```
   y = sum_{n=0}^{N} (1/(2n+1)) sin((2n+1)x)
   ```
   Desmos autocompletes `sum_{...}^{...}` into a summation template as you type it.
3. Start with $N=0$ (just the $n=1$ harmonic) and drag the slider up one step at a time, pausing at $N=1, 2, 4, 7, 14$.
4. Watch where each increase in $N$ changes the picture: early on (small $N$), the curve's overall *outline* — where it's high, where it's low, how fast it flips — reshapes with every added term. Past roughly $N=7$, the outline stops moving; each further term instead sharpens the corners and shrinks the ripples around them.

That's the general pattern, not a square-wave-only quirk: **low-frequency terms ($n$ small) set the coarse shape; high-frequency terms ($n$ large) refine the fine detail.** Keep that picture in mind for Section 3 — it's exactly why `FourierFeatures(degree=...)` lets a model trade a few low harmonics for a rough fit against many harmonics for a tight one.

## 3. From Series to Features

For a column with training-data range (period) $L$ and a chosen number of harmonics `degree`, `FourierFeatures` builds:

$$
\sin\left(\frac{2\pi n x}{L}\right), \quad \cos\left(\frac{2\pi n x}{L}\right), \qquad n = 1, \ldots, \text{degree}
$$

This is exactly the truncated Fourier series from Section 2, with `degree` playing the role of $N$: each harmonic $n$ adds one more $\sin$ / $\cos$ "wiggle" that `LinearRegression` weights with a learned coefficient (standing in for $a_n$ / $b_n$), instead of the fixed formula a hand-derived Fourier series would use. Combining enough wiggles can approximate any periodic-ish shape — low harmonics for the coarse outline, high harmonics for detail, same as the square wave in Desmos. Crucially, $\sin$ and $\cos$ always stay in $[-1, 1]$ no matter how large `degree` gets, so raising the number of harmonics does **not** reintroduce the magnitude blowup from Lesson 3 — there is no equivalent of "scale after expanding" required here.

## 4. Where period_ Comes From

`FourierFeatures.fit` (see [Lesson 2](./02-writing-a-custom-transformer.md#3-reading-example-fourierfeatures)) sets `period_` to the training column's own range (`max - min + 1`), not a fixed calendar length like `365`. That has a real consequence for the Walmart data: the training `DaysSince` span covers roughly 2.7 years, so:

- the $n=1$ harmonic's period equals the *entire* training span (~2.7 years) — a very slow wiggle,
- higher harmonics divide that span into smaller cycles, down to about `span / degree` for the largest `n`.

No single harmonic lands exactly on "365 days." Instead, with `degree=12` the model gets a mix of cycle lengths from about 2.7 years down to a couple of months, and `LinearRegression` decides how much weight to put on each one to best match the yearly bumps actually present in the data. That's a reasonable default when you don't want to hardcode a real-world period — the trade-off is that no individual harmonic is "the annual one" by itself.

## 5. Reading Example: FourierFeatures on Walmart Sales

From `practice_ws/2_training_fourier.py`:

```python
df["DaysSince"] = (df["Date"] - start_date).dt.days

categorical_features = ["Store", "Year"]
numeric_features = ["Holiday_Flag", "Temperature", "Fuel_Price", "CPI", "Unemployment"]
fourier_features = ["DaysSince"]

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
    ("num", StandardScaler(), numeric_features),
    ("fourier", FourierFeatures(degree=12), fourier_features),
])
```

`FourierFeatures` sits in its own `ColumnTransformer` slot, right next to `OneHotEncoder` and `StandardScaler`, exactly like `PolynomialFeatures` did in Lesson 3 — because it follows the same `fit`/`transform` contract from Lesson 1.

## 6. Comparing to the Polynomial Model

Running both scripts as-is on the same train/test split:

| Model | Time feature | Test $R^2$ | Test MAPE |
|---|---|---|---|
| Polynomial (Lesson 3, degree 3, scaled) | `Month`, degree 3 | 0.9338 | 7.83% |
| Fourier (this lesson, degree 12) | `DaysSince`, 12 harmonics | 0.9404 | 7.57% |

The Fourier model fits the repeating sales pattern more closely than a degree-3 polynomial in `Month` — encoding the *periodic structure* directly gives the model a better basis than approximating a wave with a handful of polynomial bends. (The two scripts don't featurize `Year` identically — the polynomial script treats it as numeric, the Fourier script as categorical — so this isn't a perfectly controlled comparison, but the gap is consistent with the underlying idea.)

## 7. Class Practice

### Practice 1

Run `practice_ws/2_training_fourier.py` as-is and confirm the testing metrics above.

### Practice 2 — More harmonics, no blowup

Sweep `FourierFeatures(degree=...)` through `1, 2, 4, 8, 12, 24` and record the testing metrics each time. Recorded result:

| degree | Test $R^2$ | Test MAPE |
|---|---|---|
| 1 | 0.9214 | 8.28% |
| 2 | 0.9246 | 8.18% |
| 4 | 0.9274 | 8.18% |
| 8 | 0.9365 | 7.79% |
| 12 | 0.9404 | 7.57% |
| 24 | 0.9480 | 7.17% |

Unlike the polynomial degree sweep in Lesson 3, this one improves *steadily* with no sudden collapse. Why does adding more harmonics stay safe here when adding more polynomial powers wasn't?

## 8. Key Takeaways

- A Fourier series approximates a periodic function as a weighted sum of $\sin$ / $\cos$ harmonics; low harmonics set the coarse outline, high harmonics add fine detail (see the square wave in Desmos, Section 2).
- Periodic or quasi-periodic signals (like a yearly retail sales cycle) are a poor fit for a handful of polynomial terms, which bend smoothly instead of repeating.
- `FourierFeatures` builds `sin`/`cos` harmonics of a column, with the period learned from the training data's own range — the same construction as a truncated Fourier series, with `LinearRegression` learning the coefficients.
- Because `sin`/`cos` are bounded in $[-1, 1]$, increasing the number of harmonics does not cause the magnitude blowup that increasing a polynomial's degree does.
- On the Walmart dataset, Fourier features on `DaysSince` out-performed a degree-3 polynomial on `Month`.

Lesson 5 introduces `GroupInteraction`, which lets different stores learn different coefficients for the same numeric features, and can be combined with `FourierFeatures` in the same model.
