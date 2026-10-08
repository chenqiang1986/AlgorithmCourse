# Lesson 1: Random Variables, Joint Distributions, Expectation, Variance, and Covariance
*ML / M04 — Statistics*

## The question

Machine-learning data are not fixed in advance: a future customer's purchase,
the next measurement from a sensor, and the error on a new prediction can all
vary. **Probability** gives us a language for describing that uncertainty.

This lesson develops the core objects used throughout probability and machine
learning:

- a **random variable** turns an outcome into a number;
- a **distribution** describes which numerical values are likely;
- a **joint distribution** describes how several random variables occur
  together, including whether they are independent;
- an **expectation** is a probability-weighted average;
- **variance** measures spread; and
- **covariance** measures how two random variables move together.

These are population quantities: they describe an ideal probability model.
Later, we will estimate them from a finite data set using sample means,
variances, and covariance matrices.

## Learning goals

By the end of this lesson, you should be able to:

1. define a discrete random variable and its probability distribution;
2. work with a probability mass function (PMF) and cumulative distribution
   function (CDF);
3. find marginal distributions from a joint PMF and decide whether two
   discrete RVs are independent;
4. compute probabilities, expectations, and variances for discrete random
   variables;
5. use the rules for expectations and variances of transformed random
   variables; and
6. calculate and interpret covariance, including why independence implies zero
   covariance but the converse need not hold.

## 1. From outcomes to random variables

A **random experiment** has an outcome that is uncertain before it occurs.
For one roll of a fair six-sided die, the outcome space is

$$
\Omega=\{1,2,3,4,5,6\}.
$$

A **random variable** (RV) is a function that assigns a real number to each
outcome:

$$
X:\Omega\longrightarrow\mathbb R.
$$

The word “variable” does not mean that $X$ is an algebraic unknown. Once an
outcome occurs, $X$ has a definite numerical value. Before then, we describe
it with probabilities.

### Example: two rolls

Roll two fair dice. An outcome is an ordered pair $(d_1,d_2)$, not just the
sum. Define

$$
X(d_1,d_2)=d_1+d_2.
$$

Then $X$ is the sum of the dice. The value $X=7$ occurs for six of the $36$
equally likely outcomes, so

$$
P(X=7)=\frac6{36}=\frac16.
$$

Different outcomes can map to the same value of a random variable. The
distribution of $X$ records probabilities of its *values*, after grouping
together all outcomes that produce each value.

## 2. Discrete random variables and PMFs

A random variable is **discrete** when it takes values in a finite or
countably infinite set, such as $\{0,1,2,\ldots\}$. Its **probability mass
function** (PMF) is

$$
p_X(x)=P(X=x).
$$

Every PMF satisfies

$$
p_X(x)\ge0,
\qquad
\sum_x p_X(x)=1.
$$

The sum includes the possible values of $X$; values outside the support have
probability $0$.

### Example: the sum of two dice

For the $X$ above, the PMF is

$$
\begin{array}{c|ccccccccccc}
x&2&3&4&5&6&7&8&9&10&11&12\\ \hline
P(X=x)&\frac1{36}&\frac2{36}&\frac3{36}&\frac4{36}&\frac5{36}&
\frac6{36}&\frac5{36}&\frac4{36}&\frac3{36}&\frac2{36}&\frac1{36}
\end{array}
$$

For example,

$$
P(X\ge10)=P(X=10)+P(X=11)+P(X=12)=\frac{3+2+1}{36}=\frac16.
$$

<svg viewBox="0 0 720 300" width="720" role="img" aria-labelledby="pmf-title pmf-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="pmf-title">PMF for the sum of two fair dice</title>
  <desc id="pmf-desc">Eleven bars for sums two through twelve. The bar for seven is tallest, and the distribution is symmetric.</desc>
  <rect width="720" height="300" rx="12" fill="#fffdf8"/>
  <g stroke="#94a3b8" stroke-width="1.5"><path d="M65 245H680"/><path d="M65 245V35"/></g>
  <g fill="#0f766e">
    <rect x="91" y="210" width="34" height="35"/><rect x="143" y="175" width="34" height="70"/><rect x="195" y="140" width="34" height="105"/><rect x="247" y="105" width="34" height="140"/><rect x="299" y="70" width="34" height="175"/><rect x="351" y="35" width="34" height="210"/><rect x="403" y="70" width="34" height="175"/><rect x="455" y="105" width="34" height="140"/><rect x="507" y="140" width="34" height="105"/><rect x="559" y="175" width="34" height="70"/><rect x="611" y="210" width="34" height="35"/>
  </g>
  <g font-family="sans-serif" font-size="15" fill="#334155"><text x="46" y="49">1/6</text><text x="41" y="249">0</text><text x="101" y="268">2</text><text x="153" y="268">3</text><text x="205" y="268">4</text><text x="257" y="268">5</text><text x="309" y="268">6</text><text x="361" y="268">7</text><text x="413" y="268">8</text><text x="465" y="268">9</text><text x="513" y="268">10</text><text x="565" y="268">11</text><text x="617" y="268">12</text><text x="642" y="286">sum $x$</text><text x="72" y="26">$P(X=x)$</text></g>
</svg>

## 3. The cumulative distribution function

The **cumulative distribution function** (CDF) is

$$
\boxed{F_X(x)=P(X\le x).}
$$

It is nondecreasing, has values between $0$ and $1$, and satisfies

$$
P(a<X\le b)=F_X(b)-F_X(a).
$$

For a discrete RV, the CDF is a step function: it jumps by $P(X=x)$ at each
possible value $x$. For the sum of two dice, for example,

$$
F_X(6)=P(X\le6)=\frac{1+2+3+4+5}{36}=\frac{15}{36}.
$$

## 4. Joint distributions: describing RVs together

A one-variable PMF answers questions such as $P(X=3)$. When an experiment
produces several quantities, we also need probabilities for their combinations.
For two discrete RVs $X$ and $Y$, the **joint PMF** is

$$
\boxed{p_{X,Y}(x,y)=P(X=x,\,Y=y).}
$$

Its entries are nonnegative and add to $1$:

$$
p_{X,Y}(x,y)\ge0,
\qquad
\sum_x\sum_y p_{X,Y}(x,y)=1.
$$

The ordinary PMFs of $X$ and $Y$ are called their **marginal PMFs**. Obtain
one by summing the joint PMF over the other variable:

$$
\boxed{p_X(x)=\sum_y p_{X,Y}(x,y),\qquad
p_Y(y)=\sum_x p_{X,Y}(x,y).}
$$

**Example (Two fair coin flips).** Let $X$ indicate whether the first flip is
heads and $Y$ indicate whether the second flip is heads, where $1$ means heads
and $0$ means tails. The joint PMF is

$$
\begin{array}{c|cc|c}
 & Y=0 & Y=1 & p_X(x)\\ \hline
X=0 & 1/4 & 1/4 & 1/2\\
X=1 & 1/4 & 1/4 & 1/2\\ \hline
p_Y(y) & 1/2 & 1/2 & 1
\end{array}
$$

For instance, $p_{X,Y}(1,0)=P(X=1,Y=0)=1/4$. The rightmost column and
bottom row are the marginals.

$\square$

For $k$ discrete RVs $X_1,\ldots,X_k$, the same idea becomes a joint PMF on
tuples:

$$
p_{X_1,\ldots,X_k}(x_1,\ldots,x_k)
=P(X_1=x_1,\ldots,X_k=x_k).
$$

To obtain the distribution of only some variables, sum over every coordinate
you do not keep. For example,

$$
p_{X_1,X_3}(x_1,x_3)=\sum_{x_2}\cdots\sum_{x_k}
p_{X_1,\ldots,X_k}(x_1,\ldots,x_k).
$$

## 5. Independence

**Definition (Independence of two random variables).** Discrete random
variables $X$ and $Y$ are independent exactly when their joint PMF factors
into their marginal PMFs at every pair of possible values:

$$
\boxed{X\perp Y
\quad\Longleftrightarrow\quad
p_{X,Y}(x,y)=p_X(x)p_Y(y)\quad\text{for every }x,y.}
$$

Equivalently, learning the value of one variable does not change the
probabilities for the other. A single failed equality proves dependence; to
prove independence, the equality must hold for **every** pair.

In the two-coin example,

$$
P(X=1,Y=0)=\frac14=\frac12\cdot\frac12
=P(X=1)P(Y=0),
$$

and the same factorization holds for all four cells, so $X$ and $Y$ are
independent.

**Example (Dependent variables from one die).** Roll one fair die. Let
$X=1$ when the result is even (and $0$ otherwise), and let $Y=1$ when the
result exceeds $3$ (and $0$ otherwise). Then

$$
P(X=1)=\frac12,\qquad P(Y=1)=\frac12,
$$

but both conditions hold only for rolls $4$ and $6$, so

$$
P(X=1,Y=1)=\frac{2}{6}=\frac13
\ne\frac14=P(X=1)P(Y=1).
$$

Thus $X$ and $Y$ are dependent. They come from the same die roll, but the
important conclusion comes from the factorization test—not merely from sharing
an experiment.

$\square$

For more than two RVs, **mutual independence** means that every subcollection
factors into the product of its marginals. In particular, the full joint PMF
must satisfy

$$
p_{X_1,\ldots,X_k}(x_1,\ldots,x_k)
=\prod_{i=1}^k p_{X_i}(x_i),
$$

and the analogous condition must hold for every smaller subcollection.
Pairwise independence alone is not enough to guarantee mutual independence.

## 6. Expectation: a probability-weighted average

The **expectation** or **mean** of $X$, written $E[X]$ or $\mu_X$, is its
long-run average across repeated independent trials.

For a discrete RV,

$$
\boxed{E[X]=\sum_x x\,p_X(x).}
$$

Expectation need not be a value that $X$ can actually take. A fair die has
$E[X]=3.5$, even though no single roll produces $3.5$.

### Example: expectation of a Bernoulli variable

Let $Y$ equal $1$ for a success and $0$ for a failure, with
$P(Y=1)=p$. Then $Y\sim\operatorname{Bernoulli}(p)$, and

$$
E[Y]=0\cdot(1-p)+1\cdot p=p.
$$

This is why probabilities often appear as expected values: the indicator of
an event $A$, written $\mathbf1_A$, has expectation $P(A)$.

### The law of the unconscious statistician

To find the expectation of a transformation $g(X)$, use the distribution of
$X$ directly:

$$
\boxed{E[g(X)]=\sum_x g(x)p_X(x).}
$$

For a fair die $D$,

$$
E[D^2]=\frac{1^2+2^2+3^2+4^2+5^2+6^2}{6}=\frac{91}{6}.
$$

### Linearity of expectation

For constants $a,b$ and random variables $X,Y$,

$$
\boxed{E[aX+bY]=aE[X]+bE[Y].}
$$

This rule does **not** require $X$ and $Y$ to be independent. More generally,

$$
E\left[\sum_{i=1}^n a_iX_i+c\right]
=\sum_{i=1}^n a_iE[X_i]+c.
$$

For example, if a delivery's duration is $D=4+2X+Y$ minutes, then

$$
E[D]=4+2E[X]+E[Y],
$$

even if weather $X$ and traffic $Y$ are related.

## 7. Variance: distance from the mean

The **variance** of $X$ is its expected squared distance from its mean:

$$
\boxed{\operatorname{Var}(X)=E\left[(X-E[X])^2\right].}
$$

It is always nonnegative. Its square root,

$$
\operatorname{SD}(X)=\sqrt{\operatorname{Var}(X)},
$$

is the **standard deviation**, which has the same units as $X$.

Expanding the square gives a particularly useful computational identity:

$$
\begin{aligned}
\operatorname{Var}(X)
&=E[X^2-2XE[X]+(E[X])^2]\\
&=E[X^2]-2(E[X])^2+(E[X])^2\\
&=\boxed{E[X^2]-(E[X])^2.}
\end{aligned}
$$

### Example: variance of a Bernoulli variable

For $Y\sim\operatorname{Bernoulli}(p)$, $Y^2=Y$ because $Y$ is either $0$
or $1$. Since $E[Y]=p$,

$$
\operatorname{Var}(Y)=E[Y^2]-(E[Y])^2=p-p^2=p(1-p).
$$

The variance is largest at $p=1/2$, where the outcome is most uncertain, and
is $0$ when $p=0$ or $p=1$, where the outcome is certain.

### Transforming a random variable

If $Z=aX+b$, then

$$
\boxed{E[Z]=aE[X]+b,\qquad \operatorname{Var}(Z)=a^2\operatorname{Var}(X).}
$$

Adding $b$ shifts every outcome and the mean but does not change the spread.
Multiplying by $a$ stretches distances by $|a|$, so squared distances and
variance are multiplied by $a^2$.

For instance, converting a temperature from Celsius to Fahrenheit uses
$F=\frac95C+32$. Thus

$$
E[F]=\frac95E[C]+32,
\qquad
\operatorname{Var}(F)=\left(\frac95\right)^2\operatorname{Var}(C).
$$

## 8. Covariance: joint variation

Variance concerns one RV. **Covariance** compares two:

$$
\boxed{\operatorname{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])].}
$$

An equivalent and often faster form is

$$
\boxed{\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y].}
$$

Interpret the product of centered values:

- if $X$ and $Y$ tend to be above their means together, or below their means
  together, covariance tends to be positive;
- if one tends to be above its mean when the other is below, covariance tends
  to be negative; and
- covariance near zero means no *linear* co-movement is apparent.

Covariance has mixed units: if height is measured in centimeters and weight in
kilograms, their covariance has units cm·kg. Its scale makes it poor for
comparing relationships across different units; correlation will fix that in a
later lesson.

### Essential covariance rules

For constants $a,b,c,d$,

$$
\begin{aligned}
\operatorname{Cov}(X,Y)&=\operatorname{Cov}(Y,X),\\
\operatorname{Cov}(X,X)&=\operatorname{Var}(X),\\
\operatorname{Cov}(aX+b,cY+d)&=ac\operatorname{Cov}(X,Y).
\end{aligned}
$$

The variance of a sum follows immediately:

$$
\boxed{\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)
+2\operatorname{Cov}(X,Y).}
$$

More generally,

$$
\operatorname{Var}(aX+bY)
=a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y)
+2ab\operatorname{Cov}(X,Y).
$$

### Independence and covariance

If $X$ and $Y$ are independent, then $E[XY]=E[X]E[Y]$, so

$$
X\text{ and }Y\text{ independent}\quad\Longrightarrow\quad
\operatorname{Cov}(X,Y)=0.
$$

The reverse implication is false. Let $X$ be equally likely to be $-1$, $0$,
or $1$, and define $Y=X^2$. Knowing $X$ determines $Y$, so they are certainly
not independent. Yet symmetry gives $E[X]=0$ and $E[X^3]=0$, hence

$$
\operatorname{Cov}(X,Y)=\operatorname{Cov}(X,X^2)
=E[X^3]-E[X]E[X^2]=0.
$$

Zero covariance rules out a linear relationship, not every possible
relationship.

## 9. Covariance matrices and ML

For a feature vector $\mathbf X=(X_1,\ldots,X_d)^T$, the **covariance
matrix** is

$$
\boxed{\Sigma=\operatorname{Cov}(\mathbf X)
=E\left[(\mathbf X-E[\mathbf X])(\mathbf X-E[\mathbf X])^T\right].}
$$

Its $(i,j)$ entry is $\operatorname{Cov}(X_i,X_j)$; its diagonal entries are
the feature variances:

$$
\Sigma=
\begin{bmatrix}
\operatorname{Var}(X_1)&\operatorname{Cov}(X_1,X_2)&\cdots\\
\operatorname{Cov}(X_2,X_1)&\operatorname{Var}(X_2)&\cdots\\
\vdots&\vdots&\ddots
\end{bmatrix}.
$$

Covariance matrices are symmetric and positive semidefinite. In ML, they
describe feature scale and redundancy, motivate feature standardization, and
are central to principal component analysis (PCA).

## 10. Worked example: total score from correlated components

Suppose a student's project score $P$ and exam score $E$ have

$$
E[P]=80,\quad E[E]=75,\quad
\operatorname{Var}(P)=36,\quad \operatorname{Var}(E)=64,
\quad \operatorname{Cov}(P,E)=24.
$$

Their course score is $S=0.4P+0.6E$. Linearity gives

$$
E[S]=0.4(80)+0.6(75)=77.
$$

For the variance, retain the covariance term:

$$
\begin{aligned}
\operatorname{Var}(S)
&=(0.4)^2(36)+(0.6)^2(64)+2(0.4)(0.6)(24)\\
&=5.76+23.04+11.52=40.32.
\end{aligned}
$$

Dropping the positive covariance would incorrectly report too little spread.
The scores tend to rise and fall together, so combining them does not average
away as much variation as independent scores would.

## 11. Common pitfalls

1. **$E[g(X)]$ is usually not $g(E[X])$.** For example,
   $E[X^2]=\operatorname{Var}(X)+(E[X])^2$, not generally $(E[X])^2$.
2. **Variance does not distribute linearly.** In general,
   $\operatorname{Var}(X+Y)\ne\operatorname{Var}(X)+\operatorname{Var}(Y)$;
   include $2\operatorname{Cov}(X,Y)$.
3. **Zero covariance does not imply independence.** It only excludes linear
   association under this measure.
4. **Sharing a source does not settle independence.** Use the joint-PMF
   factorization criterion.

## Check your understanding

1. A discrete RV $X$ has $P(X=0)=0.2$, $P(X=1)=0.5$, and $P(X=2)=0.3$.
   Find $E[X]$, $E[X^2]$, and $\operatorname{Var}(X)$.
2. A fair six-sided die is rolled once. Find $P(D>4)$, $E[D]$, and
   $\operatorname{Var}(D)$.
3. Let $A=3X-2$ and $B=-Y+7$. Express $E[A]$,
   $\operatorname{Var}(A)$, and $\operatorname{Cov}(A,B)$ in terms of
   $E[X]$, $\operatorname{Var}(X)$, and $\operatorname{Cov}(X,Y)$.
4. If $\operatorname{Var}(X)=4$, $\operatorname{Var}(Y)=9$, and
   $\operatorname{Cov}(X,Y)=-3$, find $\operatorname{Var}(2X-Y)$.
5. Two binary RVs have $P(X=1)=0.6$, $P(Y=1)=0.5$, and
   $P(X=1,Y=1)=0.3$. Are $X$ and $Y$ independent?

### Answers

1. $E[X]=1.1$, $E[X^2]=1.7$, and
   $\operatorname{Var}(X)=1.7-(1.1)^2=0.49$.
2. $P(D>4)=2/6=1/3$, $E[D]=3.5$, and
   $\operatorname{Var}(D)=91/6-(3.5)^2=35/12$.
3. $E[A]=3E[X]-2$,
   $\operatorname{Var}(A)=9\operatorname{Var}(X)$, and
   $\operatorname{Cov}(A,B)=-3\operatorname{Cov}(X,Y)$.
4. $\operatorname{Var}(2X-Y)=4(4)+9-4(-3)=37$.
5. Yes. The joint probability is $0.3=0.6(0.5)$. For binary RVs, this one
   equality together with the marginals determines the other three joint
   probabilities, so the joint PMF factors in every cell.

## Takeaway

A distribution tells us how a random variable behaves; a joint distribution
tells us how several behave together. Independence is the factorization of a
joint distribution into marginals. Expectation locates a variable's center,
variance measures its spread, and covariance measures linear co-movement.
These quantities turn uncertain observations into objects we can calculate
with—the foundation for probabilistic models, loss functions, feature scaling,
and many algorithms to come.
