# Linear Algebra Diagnostic Test — Solutions
*ML / M02 — Linear Algebra*

Worked solutions for [01-diagnostic-test.md](./01-diagnostic-test.md).

## Problem 1: Matrix Operations

$$
2A-B=
\begin{pmatrix}2&4\\-2&6\end{pmatrix}-
\begin{pmatrix}2&-1\\4&0\end{pmatrix}=
\begin{pmatrix}0&5\\-6&6\end{pmatrix}.
$$

$$
AB=
\begin{pmatrix}10&-1\\10&1\end{pmatrix},\qquad
BA=
\begin{pmatrix}3&1\\4&8\end{pmatrix}.
$$

Both $AC$ and $CA$ are defined, since all matrices are $2\times2$:

$$
AC=\begin{pmatrix}5&-2\\5&-3\end{pmatrix},\qquad
CA=\begin{pmatrix}1&2\\3&1\end{pmatrix}.
$$

Finally,

$$
A^TA=
\begin{pmatrix}1&-1\\2&3\end{pmatrix}
\begin{pmatrix}1&2\\-1&3\end{pmatrix}
=\begin{pmatrix}2&-1\\-1&13\end{pmatrix}.
$$

In general, matrix multiplication is not commutative: here $AB\ne BA$.

## Problem 2: Eigenvalues, Eigenvectors, and Diagonalization

$$
\det(M-\lambda I)=
\det\begin{pmatrix}4-\lambda&1\\2&3-\lambda\end{pmatrix}
=(4-\lambda)(3-\lambda)-2
=\lambda^2-7\lambda+10
=(\lambda-5)(\lambda-2).
$$

Thus the eigenvalues are $5$ and $2$. For $\lambda=5$,

$$
(M-5I)v=0\quad\Longrightarrow\quad -x+y=0,
$$

so one eigenvector is $v_5=(1,1)^T$. For $\lambda=2$,

$$
(M-2I)v=0\quad\Longrightarrow\quad 2x+y=0,
$$

so one eigenvector is $v_2=(1,-2)^T$. Taking these as columns gives

$$
P=\begin{pmatrix}1&1\\1&-2\end{pmatrix},\qquad
D=\begin{pmatrix}5&0\\0&2\end{pmatrix}.
$$

Since $P$ is invertible, $M=PDP^{-1}$.

## Problem 3: Principal Axes of an Ellipse

The symmetric quadratic-form matrix is

$$
Q=\begin{pmatrix}5&-3\\-3&5\end{pmatrix}.
$$

Its eigenpairs are

$$
\lambda=2,\ v=(1,1)^T;\qquad \lambda=8,\ v=(1,-1)^T.
$$

Normalize the eigenvectors and use them as columns of an orthogonal matrix:

$$
P=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
D=\begin{pmatrix}2&0\\0&8\end{pmatrix},
\qquad Q=PDP^T.
$$

The ellipse equation can now be written as

$$
\begin{pmatrix}x&y\end{pmatrix}PDP^T\begin{pmatrix}x\\y\end{pmatrix}=8.
$$

Combine the factors adjacent to $D$ by defining the new coordinate vector

$$
\begin{pmatrix}u\\v\end{pmatrix}
=P^T\begin{pmatrix}x\\y\end{pmatrix}
=\frac{1}{\sqrt2}\begin{pmatrix}x+y\\x-y\end{pmatrix}.
$$

Then the equation becomes

$$
\begin{pmatrix}u&v\end{pmatrix}D\begin{pmatrix}u\\v\end{pmatrix}=8,
\qquad\text{so}\qquad
2u^2+8v^2=8,
\qquad\text{or}\qquad
\frac{u^2}{4}+\frac{v^2}{1}=1.
$$

Thus, in the $(u,v)$-coordinate system, the semi-axis along the $u$-axis has length $2$ and the semi-axis along the $v$-axis has length $1$. The full major- and minor-axis lengths are respectively $4$ and $2$.

The major axis is the $u$-axis, whose equation is $v=0$. Since
$v=(x-y)/\sqrt2$, this is $x-y=0$, or $y=x$. The minor axis is the $v$-axis,
whose equation is $u=0$. Since $u=(x+y)/\sqrt2$, this is $x+y=0$, or $y=-x$.

## Problem 4: Matrix Exponential

The eigenvalues of

$$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$$

are $3$ and $1$, with corresponding orthonormal eigenvectors

$$
q_1=\frac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix},\qquad
q_2=\frac{1}{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}.
$$

Thus

$$
A=PDP^T,\qquad
P=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
D=\begin{pmatrix}3&0\\0&1\end{pmatrix}.
$$

Because $P^TP=I$, powers of $A$ satisfy $A^r=PD^rP^T$. Applying the series
definition gives

$$
e^A=P\left(I+D+\frac{D^2}{2!}+\cdots\right)P^T
=P\begin{pmatrix}e^3&0\\0&e\end{pmatrix}P^T.
$$

Therefore

$$
e^A=\frac12\begin{pmatrix}e^3+e&e^3-e\\e^3-e&e^3+e\end{pmatrix}.
$$

## Problem 5: Reality of Eigenvalues

Let $Av=\lambda v$ for a nonzero complex vector $v$. Because $A$ is real symmetric, it is Hermitian: $A^*=A^T=A$. Hence

$$
v^*Av=\lambda v^*v.
$$

The scalar $v^*Av$ is real, since

$$
\overline{v^*Av}=(v^*Av)^*=v^*A^*v=v^*Av.
$$

Also $v^*v>0$ is real. Therefore

$$
\lambda=\frac{v^*Av}{v^*v}
$$

is real.

## Problem 6: Orthogonality of Eigenvectors

Let $Av=\lambda v$ and $Aw=\mu w$, where $\lambda\ne\mu$. By Problem 5, both eigenvalues are real. Using symmetry,

$$
v^TAw=(Av)^Tw.
$$

The left-hand side is $\mu v^Tw$, while the right-hand side is $\lambda v^Tw$. Thus

$$
(\lambda-\mu)v^Tw=0.
$$

Since $\lambda\ne\mu$, it follows that $v^Tw=0$, so $v$ and $w$ are orthogonal.

## Problem 7: Commuting Real Symmetric Matrices

**($\Leftarrow$)** Suppose $A$ and $B$ have a common orthonormal eigenbasis $q_1,\ldots,q_n$. Let $Aq_i=\alpha_iq_i$ and $Bq_i=\beta_iq_i$. Then

$$ABq_i=\alpha_i\beta_iq_i=BAq_i$$

for every basis vector $q_i$. Therefore $AB=BA$.

**($\Rightarrow$)** Suppose $AB=BA$. Let $v$ be an eigenvector of $A$ with
eigenvalue $\lambda$. Since the eigenvalues of $A$ do not repeat, its eigenspace
$E_\lambda(A)$ is one-dimensional. Also, this eigenspace is invariant under $B$:

$$
A(Bv)=B(Av)=B(\lambda v)=\lambda Bv.
$$

Thus $Bv\in E_\lambda(A)=\operatorname{span}\{v\}$, so $Bv=\mu v$ for some
real number $\mu$. Therefore every eigenvector of $A$ is also an eigenvector of
$B$. Since a real symmetric matrix with distinct eigenvalues has an orthonormal
basis of eigenvectors, the eigenvectors of $A$ form a common orthonormal eigenbasis.

## Problem 8: Positive Semidefiniteness

For every $x\in\mathbb R^n$,

$$
x^T(A^TA)x=(Ax)^T(Ax)=\|Ax\|^2\ge0.
$$

Also $(A^TA)^T=A^TA$, so $A^TA$ is symmetric. Hence it is positive semidefinite.

## Problem 9: Nonzero Eigenvalues of $A^T A$ and $AA^T$

Let $A^TAv=kv$, where $v\ne0$ and $k\ne0$. We first show that $Av\ne0$: otherwise $A^TAv=0$, contradicting $kv\ne0$.

Now apply $A$ to both sides of the eigenvalue equation:

$$
AA^T(Av)=A(A^TAv)=A(kv)=k(Av).
$$

Because $Av\ne0$, this shows that $Av$ is an eigenvector of $AA^T$ with eigenvalue $k$. Thus every nonzero eigenvalue of $A^TA$ is also an eigenvalue of $AA^T$.
