# Homework: Eigenvalues, Eigenvectors, and Diagonalization
*ML / M02 — Linear Algebra, Class 4*

Use the [eigenvalues and diagonalization lesson](./04-eigenvalues-eigenvectors-and-diagonalization.md)
as a reference. For every eigenvalue, show the characteristic equation and a
basis for its eigenspace.

## 1. Find eigenpairs

For

$$
A=\begin{pmatrix}5&2\\2&5\end{pmatrix},
$$

find all eigenvalues and a corresponding eigenvector for each. Verify each
eigenpair directly.

## 2. Diagonalize and take a power

Let

$$
B=\begin{pmatrix}4&1\\2&3\end{pmatrix}.
$$

1. Find $P$ and $D$ such that $B=PDP^{-1}$.
2. Use the diagonalization to compute $B^5$.
3. Explain why this is preferable to multiplying $B$ by itself four times.

## 3. A repeated eigenvalue

Consider

$$
C=\begin{pmatrix}3&1\\0&3\end{pmatrix}.
$$

1. Find its algebraic multiplicity and the dimension of its eigenspace.
2. Is $C$ diagonalizable? Justify your answer from the number of linearly
   independent eigenvectors.
3. Find $C^n$ for a positive integer $n$ by looking for a pattern in the first
   few powers.

## 4. Orthogonal diagonalization

Orthogonally diagonalize the symmetric matrix

$$
S=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
$$

Give an orthogonal matrix $Q$ and a diagonal matrix $\Lambda$ such that

$$
S=Q\Lambda Q^T.
$$

Verify both that $Q^TQ=I$ and that the displayed factorization is correct.

## 5. Trace and determinant as eigenvalue checks

The matrix

$$
T=\begin{pmatrix}
4&1&0\\
0&2&0\\
0&0&-1
\end{pmatrix}
$$

is triangular.

1. List its eigenvalues without expanding a determinant.
2. Check that their sum equals $\operatorname{tr}(T)$ and their product equals
   $\det(T)$.
3. Is $T$ diagonalizable? Find enough eigenvectors to support your answer.

## 6. Symmetry matters

For each statement, decide whether it is always true, sometimes true, or never
true. Give a short justification or counterexample.

1. A real matrix with real eigenvalues is orthogonally diagonalizable.
2. A real symmetric matrix is diagonalizable over $\mathbb R$.
3. Eigenvectors for distinct eigenvalues of an arbitrary real matrix are
   perpendicular.
4. A $3\times3$ matrix with three distinct eigenvalues is diagonalizable.

## Challenge: a polynomial of a matrix

Let

$$
M=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
$$

Use an orthogonal diagonalization to find a closed formula for $M^n$. Your
answer should be a $2\times2$ matrix whose entries are written in terms of
$3^n$ and $1^n$.
