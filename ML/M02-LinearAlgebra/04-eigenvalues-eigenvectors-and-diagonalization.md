# Eigenvalues, Eigenvectors, and Diagonalization
*ML / M02 — Linear Algebra*

Eigenvectors are the special directions a transformation does not turn away
from themselves. A matrix may stretch, shrink, or reverse such a direction;
the associated eigenvalue records that scaling. For real symmetric matrices,
these directions form an orthonormal coordinate system, which makes the matrix
especially easy to understand.

## Learning Goals

By the end of this lesson, you should be able to:

- find eigenvalues and eigenvectors from the characteristic equation;
- decide when a matrix is diagonalizable;
- diagonalize a real symmetric matrix with an orthogonal matrix; and
- use a diagonalization to compute powers of a matrix efficiently.

## Eigenpairs

A nonzero vector $v$ is an **eigenvector** of $A$ if

$$
Av=\lambda v,
$$

for some scalar $\lambda$, called its **eigenvalue**. To find candidates for
$\lambda$, rearrange:

$$
(A-\lambda I)v=0.
$$

This homogeneous system has a nonzero solution exactly when

$$
\boxed{\det(A-\lambda I)=0.}
$$

For each root $\lambda$, solve $(A-\lambda I)v=0$ to obtain its eigenspace.

### Worked Example

Let $A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$. Then

$$
\det(A-\lambda I)
=\det\begin{pmatrix}4-\lambda&1\\2&3-\lambda\end{pmatrix}
=\lambda^2-7\lambda+10.
$$

The eigenvalues are $5$ and $2$. For $\lambda=5$, an eigenvector is
$v_1=(1,1)^T$; for $\lambda=2$, an eigenvector is $v_2=(1,-2)^T$.

### Trace and Determinant from Eigenvalues

> **Theorem.** Let $A$ be an $n\times n$ matrix with eigenvalues
> $\lambda_1,\ldots,\lambda_n$, counted with algebraic multiplicity. Then
>
> $$
> \boxed{\operatorname{tr}(A)=\lambda_1+\cdots+\lambda_n}
> \qquad\text{and}\qquad
> \boxed{\det(A)=\lambda_1\cdots\lambda_n.}
> $$

> This holds even when $A$ is not diagonalizable; if necessary, include its
> complex eigenvalues.

Indeed, the characteristic polynomial can be written as

$$
\det(\lambda I-A)
=\lambda^n-M_1\lambda^{n-1}+M_2\lambda^{n-2}-\cdots+(-1)^nM_n
=\prod_{i=1}^n(\lambda-\lambda_i).
$$

Here $M_k$ is the sum of all $k\times k$ **principal minors** of $A$:

$$
M_k=\sum_{\substack{S\subseteq\{1,\ldots,n\}\\|S|=k}}\det(A_{S,S}),
$$

where $A_{S,S}$ is formed by retaining the same indexed rows and columns in
$S$. In particular, $M_1=\operatorname{tr}(A)$ and $M_n=\det(A)$.
Comparing the coefficients of $\lambda^{n-1}$ and the constant terms gives
the two formulas; equivalently, the theorem follows from Vieta's formulas
applied to the characteristic polynomial.

### Algebraic and Geometric Multiplicity

An eigenvalue can occur more than once. Its **algebraic multiplicity** is its
multiplicity as a root of the characteristic polynomial. For example, if

$$
\det(\lambda I-A)=(\lambda-2)^3(\lambda+1),
$$

then $2$ has algebraic multiplicity $3$, while $-1$ has algebraic
multiplicity $1$.

For an eigenvalue $\lambda$, its **eigenspace** is

$$
E_\lambda=\operatorname{Null}(A-\lambda I).
$$

The **geometric multiplicity** of $\lambda$ is

$$
\dim(E_\lambda),
$$

the number of linearly independent eigenvectors associated with $\lambda$.

> **Theorem.** If $\lambda$ is an eigenvalue of $A$, then
>
> $$
> \boxed{1\le\text{geometric multiplicity of }\lambda
> \le\text{algebraic multiplicity of }\lambda.}
> $$

**Proof.** Because $\lambda$ is an eigenvalue, its eigenspace contains a
nonzero eigenvector. Thus its dimension, its geometric multiplicity, is at
least $1$.

Let the geometric multiplicity be $g$. Choose a basis
$v_1,\ldots,v_g$ for $E_\lambda$, and extend it to a basis of the whole
space,

$$
\mathcal B=(v_1,\ldots,v_g,b_1,\ldots,b_{n-g}).
$$

Put $P=[\,v_1\ \cdots\ v_g\ b_1\ \cdots\ b_{n-g}\,]$. Since
$Av_i=\lambda v_i$, put $u_j=Ab_j$. Expressing the vectors $u_j$ in the
basis $\mathcal B$ gives matrices $C$ and $B$ such that

$$
A[\,v_1\ \cdots\ v_g\ b_1\ \cdots\ b_{n-g}\,]
= [\,\lambda v_1\ \cdots\ \lambda v_g\ u_1\ \cdots\ u_{n-g}\,]
= P\begin{pmatrix}
\lambda I_g & C\\
0 & B
\end{pmatrix}.
$$

Thus the matrix of $A$ relative to $\mathcal B$ is

$$
M=P^{-1}AP=
\begin{pmatrix}
\lambda I_g & C\\
0 & B
\end{pmatrix},
$$

a block upper-triangular matrix. This change-of-basis matrix has the same
characteristic polynomial as $A$, because

$$
\det(tI-M)=\det\bigl(P^{-1}(tI-A)P\bigr)=\det(tI-A).
$$

On the other hand, the block upper-triangular form gives

$$
\det(tI-M)
=\det\begin{pmatrix}
(t-\lambda)I_g & -C\\
0 & tI-B
\end{pmatrix}
=(t-\lambda)^g\det(tI-B).
$$

So $(t-\lambda)^g$ is a factor of the characteristic polynomial:
$\lambda$ has algebraic multiplicity at least $g$. Hence geometric
multiplicity is at most algebraic multiplicity.

In general, there is no guarantee that the geometric multiplicity of an
eigenvalue equals its algebraic multiplicity. When they agree for every
eigenvalue, however, there are enough independent eigenvectors to diagonalize
the matrix, as the next section explains.

## Diagonalization

If an $n\times n$ matrix has $n$ linearly independent eigenvectors
$v_1,\ldots,v_n$, place them in the columns of $P$ and place their eigenvalues
in a diagonal matrix $D$:

$$
P=\begin{pmatrix}\vert&&\vert\\v_1&\cdots&v_n\\\vert&&\vert\end{pmatrix},
\qquad D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n).
$$

Then

$$
\boxed{A=PDP^{-1}.}
$$

Here is why this factorization follows. Since the columns of $P$ are the
eigenvectors of $A$, multiplying $A$ by $P$ applies $A$ to one eigenvector at
a time:

$$
\begin{aligned}
AP
&=A[v_1\;v_2\;\cdots\;v_n]\\
&=[Av_1\;Av_2\;\cdots\;Av_n]\\
&=[\lambda_1v_1\;\lambda_2v_2\;\cdots\;\lambda_nv_n]\\
&=[v_1\;v_2\;\cdots\;v_n]\operatorname{diag}(\lambda_1,\ldots,\lambda_n)\\
&=PD.
\end{aligned}
$$

The eigenvectors are linearly independent, so $P$ is invertible. Multiply
$AP=PD$ on the right by $P^{-1}$ to get

$$
APP^{-1}=PDP^{-1},
$$

and, because $PP^{-1}=I$, this becomes $A=PDP^{-1}$.

In the eigenvector coordinates, applying $A$ is just independent scaling:

$$
A^k=PD^kP^{-1}.
$$

## The Spectral Theorem for Real Symmetric Matrices

A real matrix is **symmetric** when $A^T=A$. The spectral theorem states:

> Every real symmetric $n\times n$ matrix has real eigenvalues and an
> orthonormal basis of eigenvectors.

### Why the Spectral Theorem Holds

The result follows from three theorems.

#### Theorem 1: Eigenvalues of a Real Symmetric Matrix Are Real

Let $Av=\lambda v$ with $v\ne0$; such a possibly complex eigenpair exists
because the characteristic polynomial has a complex root. Using conjugate
transpose $v^*$ and the fact that $A^T=A$ (so $A^*=A$),

$$
\lambda v^*v=v^*Av=(v^*Av)^*
              =(\lambda v^*v)^*=\overline{\lambda}\,v^*v.
$$

Because $v^*v>0$, we have $\lambda=\overline{\lambda}$, so every eigenvalue
is real. For a real eigenvalue, the real system $(A-\lambda I)v=0$ has a
nonzero real solution, so we may choose its eigenvector to be real.

#### Theorem 2: Eigenvectors for Distinct Eigenvalues Are Perpendicular

Next, suppose $Av=\lambda v$ and $Aw=\mu w$, where $\lambda\ne\mu$. Then

$$
\lambda v^Tw=(Av)^Tw=v^TAw=\mu v^Tw.
$$

Thus $(\lambda-\mu)v^Tw=0$, which gives $v^Tw=0$: eigenvectors belonging to
different eigenvalues are perpendicular.

#### Theorem 3: Every Real Symmetric Matrix Is Orthogonally Diagonalizable

We prove this theorem by induction on $n$. For the inductive step, choose a
unit eigenvector $v$ with eigenvalue $a$ and extend $v$ to an orthonormal
basis.

Let $Q=[v\;q_2\;\cdots\;q_n]$ be the orthogonal matrix formed from that basis.
In these coordinates,

$$
Q^{-1}AQ=Q^TAQ=
\begin{pmatrix}
a & u^T\\
0 & A'
\end{pmatrix}.
$$

The zero in the lower-left block follows from $Av=av$. Since $Q^TAQ$ is also
symmetric, its upper-right block must be the transpose of its lower-left
block, so $u^T=0$; moreover, $A'$ is symmetric. Hence

$$
Q^TAQ=
\begin{pmatrix}
a & 0\\
0 & A'
\end{pmatrix}.
$$

By the induction hypothesis, $A'$ is orthogonally diagonalizable: there are
an orthogonal $Q'$ and a diagonal $\Lambda'$ such that

$$
A'=Q'\Lambda'Q'^T.
$$

Therefore,

$$
\begin{aligned}
A
&=Q\begin{pmatrix}a&0\\0&A'\end{pmatrix}Q^T\\
&=Q
\begin{pmatrix}1&0\\0&Q'\end{pmatrix}
\begin{pmatrix}a&0\\0&\Lambda'\end{pmatrix}
\begin{pmatrix}1&0\\0&Q'^T\end{pmatrix}Q^T\\
&=\left[Q\begin{pmatrix}1&0\\0&Q'\end{pmatrix}\right]
\begin{pmatrix}a&0\\0&\Lambda'\end{pmatrix}
\left[Q\begin{pmatrix}1&0\\0&Q'\end{pmatrix}\right]^T.
\end{aligned}
$$

The bracketed matrix is orthogonal, and the middle matrix is diagonal, so
$A$ is orthogonally diagonalizable. The $1\times1$ case starts the induction,
proving the theorem.

So a real symmetric matrix has the stronger factorization

$$
\boxed{A=Q\Lambda Q^T,}
$$

where $Q$ is orthogonal ($Q^TQ=I$) and $\Lambda$ is diagonal. This is called
**orthogonal diagonalization**. Unlike a general change-of-basis matrix,
$Q^{-1}=Q^T$, so changing coordinates preserves lengths and angles.

<svg viewBox="0 0 760 220" width="100%" role="img" aria-label="A symmetric matrix acts by scaling perpendicular eigenvector directions.">
  <style>.axis{stroke:#94a3b8;stroke-width:1.5}.line{stroke:#2563eb;stroke-width:3}.arr{stroke:#334155;stroke-width:2;marker-end:url(#eigArrow)}.t{font:16px sans-serif;fill:#0f172a}.s{font:14px sans-serif;fill:#334155}</style>
  <defs><marker id="eigArrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#334155"/></marker></defs>
  <line class="axis" x1="40" y1="110" x2="250" y2="110"/><line class="axis" x1="145" y1="205" x2="145" y2="15"/>
  <line class="line" x1="78" y1="165" x2="212" y2="55"/><line class="line" x1="94" y1="58" x2="196" y2="162"/><text class="s" x="203" y="50">$v_1$</text><text class="s" x="198" y="180">$v_2$</text><text class="t" x="66" y="214">perpendicular eigen-directions</text>
  <line class="arr" x1="275" y1="110" x2="390" y2="110"/><text class="t" x="319" y="91">A</text>
  <line class="axis" x1="435" y1="110" x2="720" y2="110"/><line class="axis" x1="575" y1="205" x2="575" y2="15"/>
  <line class="line" x1="447" y1="216" x2="704" y2="5"/><line class="line" x1="532" y1="66" x2="622" y2="156"/><text class="s" x="695" y="18">$\lambda_1v_1$</text><text class="s" x="625" y="163">$\lambda_2v_2$</text><text class="t" x="478" y="214">scale each direction</text>
</svg>

### Symmetric Example

For

$$
A=\begin{pmatrix}2&1\\1&2\end{pmatrix},
$$

the eigenvalues are $3$ and $1$, with unit eigenvectors

$$
q_1=\frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix},
\qquad
q_2=\frac1{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}.
$$

Thus $A=Q\operatorname{diag}(3,1)Q^T$, where $Q=(q_1\ q_2)$. The diagonal
form says directly that $A$ triples the $q_1$ direction and leaves the $q_2$
direction unchanged.

## What Can Go Wrong Without Symmetry?

The conclusions of the spectral theorem need not hold for a nonsymmetric real
matrix. For example, the two-dimensional rotation matrix

$$
R_\theta=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix}
$$

has eigenvalues $e^{i\theta}$ and $e^{-i\theta}$. For a $90^\circ$ rotation,
these are $i$ and $-i$, so there are no real eigenvalues or real eigenvectors.

Also, some matrices are not diagonalizable at all. Consider

$$
J=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
$$

Its only eigenvalue is $1$, with algebraic multiplicity $2$, since
$\det(tI-J)=(t-1)^2$. But

$$
(J-I)v=0
\quad\Longrightarrow\quad
\begin{pmatrix}0&1\\0&0\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}=0
\quad\Longrightarrow\quad y=0.
$$

Thus its eigenspace is only the line spanned by $(1,0)^T$. Therefore $1$ has
geometric multiplicity $1$, so $J$ has just one linearly independent
eigenvector and cannot be diagonalized.

## Quick Check

1. What equation finds the eigenvalues of $A$?
2. What additional property does $Q$ have in $A=Q\Lambda Q^T$?
3. Why is every real symmetric matrix diagonalizable?

### Answers

1. $\det(A-\lambda I)=0$.
2. Its columns are orthonormal, so $Q^{-1}=Q^T$.
3. The spectral theorem supplies an orthonormal eigenvector basis.
