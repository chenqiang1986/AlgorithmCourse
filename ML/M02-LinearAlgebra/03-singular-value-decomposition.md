# Singular Value Decomposition (SVD)
*ML / M02 — Linear Algebra*

Singular value decomposition is a way to describe **every** real matrix as a
sequence of simple geometric actions: rotate or reflect, stretch independently
along perpendicular directions, then rotate or reflect again. It is one of the
main tools behind dimensionality reduction, image compression, and principal
component analysis.

## Learning Goals

By the end of this note, you should be able to:

- state the SVD and identify the shapes of its matrices;
- find singular values and singular vectors from $A^TA$;
- interpret an SVD as a rotate–stretch–rotate transformation;
- build a best rank-$k$ approximation by truncating an SVD; and
- compute and use an SVD with NumPy.

## The Factorization

For every real $m\times n$ matrix $A$, there are orthogonal matrices

$$
U\in\mathbb R^{m\times m},\qquad V\in\mathbb R^{n\times n}
$$

and an $m\times n$ diagonal (possibly rectangular) matrix $\Sigma$ such that

$$
\boxed{A=U\Sigma V^T.}
$$

The entries on the diagonal of $\Sigma$ are the **singular values**:

$$
\sigma_1\ge\sigma_2\ge\cdots\ge\sigma_r>0,
\qquad r=\operatorname{rank}(A).
$$

All other entries of $\Sigma$ are zero. Orthogonal means $U^TU=I$ and
$V^TV=I$, so multiplying by $U$, $U^T$, $V$, or $V^T$ preserves lengths and
angles.

If $u_i$ is column $i$ of $U$ and $v_i$ is column $i$ of $V$, then

$$
Av_i=\sigma_i u_i \qquad (i=1,\ldots,r).
$$

Thus $v_i$ is a **right singular vector** (an input direction), $u_i$ is a
**left singular vector** (the corresponding output direction), and
$\sigma_i$ is the amount by which that input direction is stretched.

## Geometry: Rotate, Stretch, Rotate

Reading matrix multiplication from right to left,

$$
x\xrightarrow{\;V^T\;}\text{new perpendicular coordinates}
\xrightarrow{\;\Sigma\;}\text{axis-by-axis stretching}
\xrightarrow{\;U\;}Ax.
$$

<svg viewBox="0 0 780 210" width="100%" role="img" aria-label="The SVD transforms a unit circle into an axis-aligned ellipse, then rotates it into its final orientation.">
  <defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#334155"/></marker></defs>
  <style>.axis{stroke:#94a3b8;stroke-width:1.5}.shape{fill:#bfdbfe;stroke:#2563eb;stroke-width:2.5}.arr{stroke:#334155;stroke-width:2;marker-end:url(#arrow)}.label{font:16px sans-serif;fill:#0f172a}.small{font:14px sans-serif;fill:#334155}</style>
  <line class="axis" x1="38" y1="105" x2="182" y2="105"/><line class="axis" x1="110" y1="33" x2="110" y2="177"/><circle class="shape" cx="110" cy="105" r="48"/><text class="label" x="75" y="202">unit circle</text>
  <line class="arr" x1="195" y1="105" x2="258" y2="105"/><text class="small" x="211" y="85">Vᵀ</text>
  <line class="axis" x1="292" y1="105" x2="468" y2="105"/><line class="axis" x1="380" y1="27" x2="380" y2="183"/><ellipse class="shape" cx="380" cy="105" rx="74" ry="30"/><text class="label" x="310" y="202">axis-aligned ellipse</text><text class="small" x="348" y="50">Σ stretches</text>
  <line class="arr" x1="480" y1="105" x2="545" y2="105"/><text class="small" x="501" y="85">U</text>
  <line class="axis" x1="571" y1="38" x2="737" y2="172"/><line class="axis" x1="587" y1="170" x2="721" y2="36"/><ellipse class="shape" cx="654" cy="105" rx="74" ry="30" transform="rotate(-35 654 105)"/><text class="label" x="592" y="202">final ellipse Ax</text>
</svg>

The unit circle is a useful picture: $V^T$ changes its coordinate directions
but leaves it a circle; $\Sigma$ turns it into an axis-aligned ellipse with
semi-axis lengths $\sigma_i$; $U$ gives that ellipse its final orientation.
In particular,

$$
\max_{\|x\|=1}\|Ax\|=\sigma_1.
$$

The largest singular value is the greatest stretching factor of $A$.

## Finding an SVD from Eigenvalues

The matrix $A^TA$ is symmetric and positive semidefinite, because

$$
x^T(A^TA)x=\|Ax\|^2\ge0.
$$

Therefore its eigenvalues are nonnegative. The key relationship is

$$
\boxed{\text{eigenvalues of }A^TA=\sigma_i^2.}
$$

For a nonzero eigenpair $A^TAv_i=\lambda_i v_i$, take $v_i$ to have length
one. Then set

$$
\sigma_i=\sqrt{\lambda_i},\qquad u_i=\frac{Av_i}{\sigma_i}.
$$

The vectors $v_i$ become the columns of $V$, and the corresponding $u_i$ become
the columns of $U$. Complete either set to an orthonormal basis if a full SVD is
needed. Similarly, $AA^T$ has the same nonzero eigenvalues and its eigenvectors
are the left singular vectors.

### Worked Example

Let

$$
A=\begin{pmatrix}3&0\\4&0\end{pmatrix}.
$$

First compute

$$
A^TA=\begin{pmatrix}25&0\\0&0\end{pmatrix}.
$$

Its eigenvalues are $25$ and $0$, so the singular values are $\sigma_1=5$ and
$\sigma_2=0$. We may take $v_1=(1,0)^T$ and $v_2=(0,1)^T$, hence $V=I$. The
nonzero left singular vector is

$$
u_1=\frac{Av_1}{5}=\begin{pmatrix}3/5\\4/5\end{pmatrix}.
$$

Choose the perpendicular unit vector $u_2=(-4/5,3/5)^T$. Then

$$
U=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix},\qquad
\Sigma=\begin{pmatrix}5&0\\0&0\end{pmatrix},\qquad V=I,
$$

and direct multiplication verifies $A=U\Sigma V^T$.

## Compact SVD and Rank-One Pieces

When $r=\operatorname{rank}(A)$, the **compact SVD** keeps only the nonzero
singular directions:

$$
A=U_r\Sigma_rV_r^T,
$$

where $U_r$ is $m\times r$, $\Sigma_r$ is $r\times r$, and $V_r$ is $n\times r$.
Equivalently,

$$
\boxed{A=\sum_{i=1}^r\sigma_i u_i v_i^T.}
$$

Each $u_iv_i^T$ has rank one. SVD says that any matrix is a sum of mutually
perpendicular rank-one patterns, ordered from most important ($\sigma_1$) to
least important.

## Low-Rank Approximation and Compression

Keep only the first $k<r$ singular values:

$$
A_k=\sum_{i=1}^k\sigma_i u_i v_i^T
=U_k\Sigma_kV_k^T.
$$

This is not merely a convenient approximation. The Eckart–Young theorem says
that $A_k$ is the closest rank-$k$ matrix to $A$ in Frobenius norm:

$$
\|A-A_k\|_F^2=\sum_{i=k+1}^r\sigma_i^2.
$$

For a grayscale image stored as an $m\times n$ pixel matrix, a rank-$k$
approximation stores $U_k$, $\Sigma_k$, and $V_k^T$: about

$$
k(m+n+1)
$$

numbers instead of $mn$. Compression works well when the singular values drop
quickly, since a few large-scale patterns then capture most of the image.

## SVD in NumPy

```python
import numpy as np

A = np.array([[3.0, 0.0],
              [4.0, 0.0]])

# full_matrices=False returns the compact-shaped factors when A is rectangular.
U, s, Vt = np.linalg.svd(A, full_matrices=False)
Sigma = np.diag(s)

assert np.allclose(A, U @ Sigma @ Vt)

# Best rank-1 approximation.
k = 1
A1 = U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]
```

Two details prevent common mistakes:

- NumPy returns `Vt`, which is $V^T$, **not** $V$.
- It returns singular values as a one-dimensional array `s`; use `np.diag(s)`
  when you need the diagonal matrix $\Sigma$.

## Connection to PCA

Let $X$ be a data matrix whose rows are observations and whose columns are
features, after each column has been centered. If

$$
X=U\Sigma V^T,
$$

then the columns of $V$ are the principal directions in feature space. The
principal-component scores are

$$
XV=U\Sigma.
$$

Keeping the first $k$ columns of $V$ projects the data onto its $k$ strongest
directions of variation. PCA is therefore SVD applied to centered data.

## Quick Check

1. If $A$ is $8\times5$, what are the shapes of $U$, $\Sigma$, and $V$ in a full SVD?
2. If the eigenvalues of $A^TA$ are $36$, $9$, and $0$, what are the singular values of $A$?
3. Why is $A_k$ lower rank than $A$ when $k<r$?
4. In `np.linalg.svd(A)`, what mathematical matrix is returned as the third value?

### Answers

1. $U$ is $8\times8$, $\Sigma$ is $8\times5$, and $V$ is $5\times5$.
2. $6$, $3$, and $0$.
3. It is the sum of only $k$ rank-one matrices, so its rank is at most $k$.
4. $V^T$.

## Practice

Continue with [SVD Practice: Energy and Image Compression](./04-svd-practice.md)
to prove the Frobenius-norm identity and use a truncated SVD to compress a
grayscale image.
