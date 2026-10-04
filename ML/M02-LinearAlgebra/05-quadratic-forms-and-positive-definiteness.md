# Real Symmetric Matrices, Quadratic Forms, and Positive Definiteness
*ML / M02 — Linear Algebra*

Quadratic forms turn a vector into a number using a matrix. They describe
curvature, squared distance, energy, and the local shape of many optimization
objectives. For real symmetric matrices, eigenvalues give a complete and clean
test for whether that shape is bowl-like, flat in some direction, or saddle-like.

## Learning Goals

By the end of this lesson, you should be able to:

- write and evaluate a quadratic form $x^TAx$;
- reduce a symmetric quadratic form to a sum of squares using orthogonal
  diagonalization;
- classify a symmetric matrix as positive definite, semidefinite, indefinite,
  or negative definite; and
- apply positive definiteness tests in two variables and optimization; and
- interpret the condition number of a positive-definite quadratic form.

## Quadratic Forms

Given a real symmetric $n\times n$ matrix $A$, the function

$$
q(x)=x^TAx
$$

is a **quadratic form**. For

$$
A=\begin{pmatrix}a&b\\b&c\end{pmatrix},
\qquad x=\begin{pmatrix}x_1\\x_2\end{pmatrix},
$$

we get

$$
q(x)=ax_1^2+2bx_1x_2+cx_2^2.
$$

Only the symmetric part of a matrix affects $x^TAx$, since

$$
x^TAx=x^T\left(\frac{A+A^T}{2}\right)x.
$$

So studying quadratic forms naturally leads to symmetric matrices.

## Principal Axes: A Sum of Squares

By the spectral theorem, write a real symmetric matrix as

$$
A=Q\Lambda Q^T.
$$

Use the rotated coordinates $y=Q^Tx$. Then

$$
q(x)=x^TQ\Lambda Q^Tx=y^T\Lambda y
=\lambda_1y_1^2+\cdots+\lambda_ny_n^2.
$$

Orthogonal diagonalization therefore removes cross terms by rotating to the
eigenvector axes. The eigenvalues determine the shape.

<svg viewBox="0 0 760 230" width="100%" role="img" aria-label="Positive definite quadratic form has elliptical contours, while an indefinite form has hyperbolic contours.">
  <style>.axis{stroke:#94a3b8;stroke-width:1.5}.pos{fill:none;stroke:#2563eb;stroke-width:2}.ind{fill:none;stroke:#dc2626;stroke-width:2}.t{font:16px sans-serif;fill:#0f172a}.s{font:14px sans-serif;fill:#334155}</style>
  <line class="axis" x1="25" y1="110" x2="350" y2="110"/><line class="axis" x1="185" y1="210" x2="185" y2="12"/>
  <ellipse class="pos" cx="185" cy="110" rx="48" ry="24" transform="rotate(-28 185 110)"/><ellipse class="pos" cx="185" cy="110" rx="88" ry="44" transform="rotate(-28 185 110)"/><ellipse class="pos" cx="185" cy="110" rx="128" ry="64" transform="rotate(-28 185 110)"/>
  <text class="t" x="82" y="225">positive definite: ellipses</text><text class="s" x="120" y="33">$q(x)=\text{constant}>0$</text>
  <line class="axis" x1="415" y1="110" x2="735" y2="110"/><line class="axis" x1="575" y1="210" x2="575" y2="12"/>
  <path class="ind" d="M440 25 C485 45 515 74 535 110 C515 146 485 175 440 195 M710 25 C665 45 635 74 615 110 C635 146 665 175 710 195"/><path class="ind" d="M460 5 C515 41 545 75 555 110 C545 145 515 179 460 215 M690 5 C635 41 605 75 595 110 C605 145 635 179 690 215"/>
  <text class="t" x="498" y="225">indefinite: hyperbolas</text><text class="s" x="511" y="33">positive and negative values</text>
</svg>

## Positive Definiteness

A real symmetric matrix $A$ is:

- **positive definite (PD)** if $x^TAx>0$ for every $x\ne0$;
- **positive semidefinite (PSD)** if $x^TAx\ge0$ for every $x$;
- **negative definite (ND)** if $x^TAx<0$ for every $x\ne0$; and
- **indefinite** if $x^TAx$ is positive for some nonzero vectors and negative
  for others.

### Theorem: Equivalent Tests for Positive (Semi)definiteness

Let $A$ be a real symmetric matrix. A **principal minor** is the determinant
of a submatrix formed by selecting the same set of rows and columns. A
**leading principal minor** uses the first $k$ rows and first $k$ columns for
some $k$.

The following statements are equivalent:

- $A$ is **positive definite**:
  1. $x^TAx>0$ for every $x\ne0$ (the definition);
  2. every eigenvalue of $A$ is positive;
  3. every principal minor of $A$ is positive;
  4. every leading principal minor of $A$ is positive.

- $A$ is **positive semidefinite**:
  1. $x^TAx\ge0$ for every $x$ (the definition);
  2. every eigenvalue of $A$ is nonnegative;
  3. every principal minor of $A$ is nonnegative.

The final PD criterion is **Sylvester's criterion**. There is no analogous
leading-principal-minor test for PSD matrices: nonnegative leading principal
minors alone do not guarantee PSD. For example,

$$
\begin{pmatrix}0&0\\0&-1\end{pmatrix}
$$

has nonnegative leading principal minors ($0$ and $0$), but it has a negative
eigenvalue and is not PSD.

### Proof of the Tests (apart from Sylvester's Criterion)

We prove the positive-definite tests. The positive-semidefinite version is
identical after replacing “positive” by “nonnegative.” The
leading-principal-minor characterization is Sylvester's criterion, which we
state without proof.

**1. Positive definite $\Rightarrow$ all eigenvalues are positive.** Suppose,
for a contradiction, that $A$ has an eigenvalue $\lambda\le0$, with
nonzero eigenvector $v$. Then

$$
v^TAv=v^T(\lambda v)=\lambda\lVert v\rVert^2\le0,
$$

contradicting positive definiteness. Thus every eigenvalue is positive.

**2. All eigenvalues positive $\Rightarrow$ positive definite.** Orthogonally
diagonalize $A$:

$$
A=Q\Lambda Q^T,
\qquad
\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n).
$$

Let $y=Q^Tx$. This is only a change of coordinates: because $Q$ is
orthogonal, $x\ne0$ exactly when $y\ne0$. Therefore

$$
x^TAx=y^T\Lambda y
=\lambda_1y_1^2+\cdots+\lambda_ny_n^2>0
$$

for every nonzero $x$, since each $\lambda_i>0$.

**3. Positive definite $\Rightarrow$ all principal minors are positive.**
Let $B$ be any principal submatrix of $A$. Given a nonzero vector $z$
of the appropriate size, place its entries in the corresponding coordinates
of $x$ and put zeros elsewhere. Then $x\ne0$ and

$$
z^TBz=x^TAx>0.
$$

So $B$ is positive definite. By the first result, all eigenvalues of $B$
are positive, and hence

$$
\det(B)=\prod_i\lambda_i(B)>0.
$$

Thus every principal minor of $A$ is positive.

**4. All principal minors positive $\Rightarrow$ all eigenvalues are
positive.** Let $M_j$ be the sum of all $j\times j$ principal minors of
$A$. Since every principal minor is positive, $M_j>0$ for every $j$.
The characteristic polynomial is

$$
\det(kI-A)=k^n-M_1k^{n-1}+M_2k^{n-2}-\cdots+(-1)^nM_n.
$$

For $k<0$, every term on the right has sign $(-1)^n$, so their sum cannot
be zero. Hence $A$ has no negative eigenvalues. Also,
$\det(A)=M_n>0$, so zero is not an eigenvalue. Every eigenvalue is
therefore positive.

For the PSD statement, make the same replacements throughout: use
$\lambda\ge0$, nonnegative quadratic forms, and nonnegative principal
minors. In the final step, the same sign argument rules out negative
eigenvalues; zero eigenvalues are allowed.

For $2\times2$ symmetric $A=\begin{pmatrix}a&b\\b&c\end{pmatrix}$,

$$
\boxed{A\text{ is PD}\iff a>0\text{ and }\det(A)=ac-b^2>0.}
$$

### Example

Let

$$
A=\begin{pmatrix}3&1\\1&2\end{pmatrix}.
$$

Here $a=3>0$ and $\det(A)=6-1=5>0$, so $A$ is positive definite. Therefore
$q(x)=3x_1^2+2x_1x_2+2x_2^2$ is strictly positive except at the origin.

## Conditioning and Curvature

For a symmetric positive-definite matrix, let $\lambda_{\max}$ and
$\lambda_{\min}$ be its largest and smallest eigenvalues. Its

$$
\boxed{\kappa(A)=\frac{\lambda_{\max}}{\lambda_{\min}}}
$$

is called its **condition number**—more precisely, its spectral (or
2-norm) condition number. In machine learning and optimization, it measures
how uneven the curvature of the quadratic form is. A large $\kappa(A)$ means
the level-set ellipses are very stretched: the objective is **ill-conditioned**
and gradient descent can make slow progress by zig-zagging across the narrow
direction. A value near $1$ means the curvature is nearly the same in every
direction.

For a positive-semidefinite matrix with $\lambda_{\min}=0$, this ratio is
infinite (or undefined); the quadratic form is flat in at least one direction.

## Why Optimization Cares

For a twice-differentiable function, a positive-definite Hessian at a critical
point signals a strict local minimum; a negative-definite Hessian signals a
strict local maximum; and an indefinite Hessian signals a saddle point. This
connects the geometry of quadratic forms to gradient-based machine learning.

## Quick Check

1. If a symmetric matrix has eigenvalues $2$, $0$, and $5$, how is it classified?
2. What does a negative eigenvalue imply about $x^TAx$?
3. Is $\begin{pmatrix}1&2\\2&1\end{pmatrix}$ positive definite?

### Answers

1. Positive semidefinite.
2. Along its eigenvector direction, the quadratic form is negative.
3. No. Its determinant is $1-4=-3$, so it is indefinite.
