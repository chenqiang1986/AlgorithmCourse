# The Moore--Penrose Pseudoinverse
*ML / M02 — Linear Algebra*

An ordinary inverse solves $Ax=b$ only when $A$ is square and nonsingular.
Machine-learning matrices are often rectangular, rank-deficient, or both. The
**Moore--Penrose pseudoinverse** extends the idea of an inverse to every matrix.
Computed from an SVD, it gives the least-squares solution when an exact solution
does not exist and selects the smallest-norm solution when many exact solutions
exist.

## Learning Goals

By the end of this note, you should be able to:

- construct $A^+$ from the SVD of $A$;
- use $x=A^+b$ to solve least-squares problems;
- distinguish an exact solution, a least-squares solution, and a minimum-norm
  solution; and
- compute a pseudoinverse safely with NumPy.

## Why an Inverse Is Not Enough

For a square invertible matrix, $A^{-1}$ reverses the action of $A$:

$$
A^{-1}A=I,\qquad AA^{-1}=I.
$$

But a tall matrix $A\in\mathbb R^{m\times n}$ with $m>n$ has more equations
than unknowns. Usually $b$ is not in the column space of $A$, so $Ax=b$ has no
exact solution. A wide matrix with $m<n$ has more unknowns than equations; if
it has a solution, it usually has infinitely many. If $A$ is rank-deficient,
some input directions are collapsed to zero and cannot be reversed at all.

The pseudoinverse handles all three cases without pretending that lost
information can be recovered.

## Start with a Rectangular Diagonal Matrix

A diagonal matrix need not be square. For an $m\times n$ matrix, "diagonal"
means that entries away from the main diagonal are zero. For example,

$$
D=
\begin{pmatrix}
4&0&0\\
0&-2&0\\
0&0&0\\
0&0&0
\end{pmatrix}
\in\mathbb R^{4\times3}.
$$

The first coordinate is stretched by $4$, the second is reflected and stretched
by $2$, and the third is sent to $0$. Thus $D$ has rank $2$, not full rank
(which would be $3$ for a $4\times3$ matrix). We can undo the two nonzero
stretches, but we cannot undo the zero: every value of the third input
coordinate produces the same output. So we transpose the shape, invert only
the nonzero diagonal entries, and leave zero entries zero:

$$
D^+=
\begin{pmatrix}
1/4&0&0&0\\
0&-1/2&0&0\\
0&0&0&0
\end{pmatrix}
\in\mathbb R^{3\times4}.
$$

More generally, if $D$ has diagonal entries $d_1,\ldots,d_p$, define

$$
(D^+)_{ii}=
\begin{cases}
1/d_i, & d_i\ne0,\\
0, & d_i=0,
\end{cases}
$$

and set every off-diagonal entry to zero. This is the entire pseudoinverse
idea: **ignore the zero diagonal values and invert the nonzero ones.**

An SVD turns any matrix into exactly this kind of rectangular diagonal matrix,
up to rotations or reflections. That lets us apply the same rule to every
matrix.

## Definition from the SVD

Suppose the compact SVD of a rank-$r$ matrix is

$$
A=U_r\Sigma_rV_r^T,
$$

where $\Sigma_r=\operatorname{diag}(\sigma_1,\ldots,\sigma_r)$ and every
$\sigma_i>0$. Reverse the nonzero stretches and leave the zero directions out:

$$
\boxed{A^+=V_r\Sigma_r^{-1}U_r^T,}
\qquad
\Sigma_r^{-1}=\operatorname{diag}\left(\frac1{\sigma_1},\ldots,\frac1{\sigma_r}\right).
$$

Equivalently, using the full SVD

$$
A=U\Sigma V^T,
$$

where $U\in\mathbb R^{m\times m}$, $\Sigma\in\mathbb R^{m\times n}$, and
$V\in\mathbb R^{n\times n}$, the pseudoinverse is

$$
\boxed{A^+=V\Sigma^+U^T.}
$$

Here $\Sigma^+\in\mathbb R^{n\times m}$ is the rectangular diagonal
pseudoinverse defined above: transpose $\Sigma$, replace each nonzero diagonal
entry $\sigma_i$ by $1/\sigma_i$, and leave zero diagonal entries as zero.
Thus, if $A$ is $m\times n$, then $A^+$ is $n\times m$.

## Hand Calculation from an SVD

The following example follows the SVD construction step by step for a non-square
matrix. It also shows what the two products $A^+A$ and $AA^+$ look like.

**Example (Pseudoinverse of a full-column-rank $3\times2$ matrix).** Compute
the pseudoinverse of

$$
A=
\begin{pmatrix}
1&1\\
1&-1\\
1&1
\end{pmatrix}.
$$

**Solution:**

We use the compact SVD

$$
A=U_r\Sigma_rV_r^T,
$$

so that

$$
A^+=V_r\Sigma_r^{-1}U_r^T.
$$

The first step finds $V_r$ and the singular values; then we use them to
recover $U_r$.

**1. Diagonalize $A^TA$.** First,

$$
A^TA=
\begin{pmatrix}
3&1\\
1&3
\end{pmatrix}.
$$

Its eigenvalues and corresponding unit eigenvectors are

$$
\lambda_1=4,\quad v_1=\frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix},
\qquad
\lambda_2=2,\quad v_2=\frac1{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}.
$$

The eigenvalues are the squared singular values, so

$$
V_r=
\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
\sigma_1=2,\quad \sigma_2=\sqrt2.
$$

**2. Form $\Sigma_r$ and $\Sigma_r^{-1}$.** Since $A$ has rank $2$,

$$
\Sigma_r=
\begin{pmatrix}
2&0\\
0&\sqrt2\\
\end{pmatrix},
\qquad
\Sigma_r^{-1}=
\begin{pmatrix}
1/2&0\\
0&1/\sqrt2
\end{pmatrix}.
$$

**3. Calculate $AV_r\Sigma_r^{-1}$ to recover $U_r$.** Since
$A=U_r\Sigma_rV_r^T$ and $V_r^TV_r=I$, we have

$$
AV_r\Sigma_r^{-1}
=U_r\Sigma_rV_r^TV_r\Sigma_r^{-1}
=U_r.
$$

Its columns are

$$
u_1=\frac{Av_1}{\sigma_1}=
\frac1{\sqrt2}\begin{pmatrix}1\\0\\1\end{pmatrix},
\qquad
u_2=\frac{Av_2}{\sigma_2}=
\begin{pmatrix}0\\1\\0\end{pmatrix}.
$$

Therefore,

$$
U_r=
\begin{pmatrix}
1/\sqrt2&0\\
0&1\\
1/\sqrt2&0
\end{pmatrix}.
$$

The columns of $U_r$ are orthonormal, as required. Finally,
$A^+=V_r\Sigma_r^{-1}U_r^T$. Multiplication gives

$$
\boxed{
A^+=
\begin{pmatrix}
1/4&1/2&1/4\\
1/4&-1/2&1/4
\end{pmatrix}.}
$$

The two products are

$$
A^+A=
\begin{pmatrix}1&0\\0&1\end{pmatrix}=I_2,
$$

$$
AA^+=
\begin{pmatrix}
1/2&0&1/2\\
0&1&0\\
1/2&0&1/2
\end{pmatrix}.
$$

Here $A^+A$ is the $2\times2$ identity, while $AA^+$ is a $3\times3$
projection matrix rather than the identity.

$\square$

**Observation (The smaller product for a full-rank matrix).** If $A$ has full
rank, then the product with the smaller square shape is the identity:

- If $A$ is tall or square with full column rank, then $A^+A=I_n$.
- If $A$ is wide or square with full row rank, then $AA^+=I_m$.

For a square full-rank matrix, both products are the identity. The other
product, when $A$ is rectangular, is an orthogonal projection.

**Theorem (Pseudoinverse of an invertible matrix).** If $A$ is square and
invertible, then $A^+=A^{-1}$.

**Proof:**

When $A$ is invertible, its rank is full, so all of its singular values are
nonzero. From $A=U\Sigma V^T$,

$$
A^+=V\Sigma^{-1}U^T.
$$

Multiplying gives $A^+A=V\Sigma^{-1}\Sigma V^T=I$ and
$AA^+=U\Sigma\Sigma^{-1}U^T=I$. Thus $A^+$ is the ordinary inverse.

$\square$

## Least Squares: The Tall-Matrix Case

When $Ax=b$ cannot be solved exactly, choose $x$ to make the residual as small
as possible:

$$
\boxed{\widehat{x}=\arg\min_x\|Ax-b\|_2.}
$$

**Question.** What if $A^TA$ is singular?

Then $(A^TA)^{-1}$ does not exist, so the familiar inverse formula cannot be
used. The normal equations themselves are still valid, however. The
pseudoinverse supplies a solution without inverting $A^TA$.

**Theorem (The pseudoinverse solves the normal equations).** For every real
matrix $A$ and vector $b$, the vector

$$
\boxed{\widehat{x}=A^+b}
$$

is a least-squares solution.

**Proof:**

The derivative condition for the least-squares objective, developed earlier in
the Tensor lesson, gives the normal equations

$$
A^TA\widehat{x}=A^Tb.
$$

Let $A=U_r\Sigma_rV_r^T$ be a compact SVD. Then
$A^+=V_r\Sigma_r^{-1}U_r^T$. Substitute $\widehat{x}=A^+b$ into the
left-hand side:

$$
\begin{aligned}
A^TA\widehat{x}
&=A^TAA^+b\\
&=\left(V_r\Sigma_rU_r^T\right)
  \left(U_r\Sigma_rV_r^T\right)
  \left(V_r\Sigma_r^{-1}U_r^T\right)b\\
&=V_r\Sigma_r\Sigma_r\Sigma_r^{-1}U_r^Tb\\
&=V_r\Sigma_rU_r^Tb\\
&=A^Tb.
\end{aligned}
$$

Here $U_r^TU_r=I_r$, $V_r^TV_r=I_r$, and
$\Sigma_r\Sigma_r^{-1}=I_r$. Thus $\widehat{x}$ satisfies the normal
equations and is a least-squares solution.

$\square$

If $A^TA$ is singular, there may be many least-squares solutions. The SVD
definition of $A^+$ still works: it ignores the zero singular values and
returns the unique least-squares solution with minimum Euclidean norm.

For a general matrix with compact SVD $A=U_r\Sigma_rV_r^T$, that solution is

$$
\widehat{x}=A^+b
=\sum_{i=1}^r\frac{u_i^Tb}{\sigma_i}v_i.
$$

First, $U_r^Tb$ measures $b$ along the output singular directions. Then
$\Sigma_r^{-1}$ undoes each nonzero stretch, and $V_r$ expresses the answer in
the original input coordinates.

The fitted vector is

$$
A\widehat{x}=AA^+b.
$$

It is the orthogonal projection of $b$ onto $\operatorname{col}(A)$, the
column space of $A$. To see this we start from the normal equations:

$$
A^T(A\widehat{x}-b)=0.
$$
Consequently, the residual $b-A\widehat{x}$ is
perpendicular to every column of $A$. 

In numerical work, however, forming $(A^TA)^{-1}$ is usually less stable than
using an SVD or a least-squares solver.

**Example (Fitting a constant to inconsistent data).** Find the least-squares
solution of

$$
\begin{pmatrix}1\\1\\1\end{pmatrix}x
\approx
\begin{pmatrix}1\\2\\6\end{pmatrix}.
$$

**Solution:**

Here $A=(1,1,1)^T$ has one unit left singular vector
$u_1=(1,1,1)^T/\sqrt3$, right singular vector $v_1=1$, and singular value
$\sigma_1=\sqrt3$. Therefore

$$
A^+=\frac{1}{3}\begin{pmatrix}1&1&1\end{pmatrix},
\qquad
\widehat{x}=A^+b=\frac{1+2+6}{3}=3.
$$

The closest vector of the form $(x,x,x)^T$ is $(3,3,3)^T$: the best constant
prediction is the mean of the observations.

$\square$

## Minimum Norm: The Wide or Rank-Deficient Case

If $Ax=b$ has many solutions, the pseudoinverse selects the one closest to the
origin:

$$
\boxed{A^+b=\arg\min_{Ax=b}\|x\|_2.}
$$

It removes any component in $\operatorname{null}(A)$, because those directions
do not change $Ax$ but do increase the length of $x$.

**Example (Choosing among infinitely many solutions).** Let

$$
A=\begin{pmatrix}1&1\end{pmatrix},
\qquad b=2.
$$

**Solution:**

Every vector $(x_1,x_2)^T$ satisfying $x_1+x_2=2$ is an exact solution. The
compact SVD has $u_1=1$, $v_1=(1,1)^T/\sqrt2$, and $\sigma_1=\sqrt2$. Hence

$$
A^+=\frac12\begin{pmatrix}1\\1\end{pmatrix},
\qquad
A^+b=\begin{pmatrix}1\\1\end{pmatrix}.
$$

Among all points on the line $x_1+x_2=2$, $(1,1)^T$ has the smallest Euclidean
norm.

$\square$

## Four Defining Identities

The Moore--Penrose pseudoinverse is uniquely characterized by

$$
AA^+A=A,\qquad A^+AA^+=A^+,
$$

$$
(AA^+)^T=AA^+,\qquad (A^+A)^T=A^+A.
$$

The symmetric matrices $AA^+$ and $A^+A$ are orthogonal projectors:

$$
AA^+=U_rU_r^T \quad\text{projects onto }\operatorname{col}(A),
$$

$$
A^+A=V_rV_r^T \quad\text{projects onto }\operatorname{row}(A).
$$

These identities explain why $AA^+b$ is the closest attainable vector to $b$.

## Small Singular Values and Regularization

The formula for $A^+$ divides by each nonzero $\sigma_i$. If a singular value
is extremely small, $1/\sigma_i$ is extremely large: tiny measurement errors
in $b$ can produce huge changes in the solution. This is the signature of an
ill-conditioned problem.

Numerical software therefore treats singular values below a tolerance as zero.
This is called a **truncated pseudoinverse**. It deliberately discards unstable
directions instead of amplifying noise. Ridge regression makes a related, but
smooth, adjustment by replacing $1/\sigma_i$ with

$$
\frac{\sigma_i}{\sigma_i^2+\lambda}.
$$

## Pseudoinverse in NumPy

```python
import numpy as np

A = np.array([[1.0, 1.0],
              [1.0, 1.0],
              [1.0, 1.0]])
b = np.array([1.0, 2.0, 6.0])

# Computes an SVD internally and discards tiny singular values.
A_plus = np.linalg.pinv(A)
x_hat = A_plus @ b

# Direct least-squares interface; it returns the same minimum-norm solution.
x_lstsq, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

assert np.allclose(x_hat, x_lstsq)
assert np.allclose(A @ x_hat, A @ A_plus @ b)
```

Use `np.linalg.pinv` when the pseudoinverse itself is needed. If you only need
to solve $Ax\approx b$, `np.linalg.lstsq` communicates that intent directly and
avoids explicitly constructing $A^+$.

## Quick Check

1. If $A$ is $7\times3$, what is the shape of $A^+$?
2. In an SVD-based pseudoinverse, what happens to a zero singular value?
3. What vector does $AA^+b$ represent geometrically?
4. If $Ax=b$ has many solutions, which one does $A^+b$ select?

### Answers

1. $A^+$ is $3\times7$.
2. It remains zero in $\Sigma^+$; it is never inverted.
3. The orthogonal projection of $b$ onto $\operatorname{col}(A)$.
4. The exact solution with minimum Euclidean norm.

## Practice

For further practice, derive the four pseudoinverse identities from the compact
SVD, solve a least-squares line-fitting problem, and compare `pinv` with
`lstsq` on a nearly rank-deficient matrix.
