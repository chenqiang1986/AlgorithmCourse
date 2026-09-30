# Linear Algebra Diagnostic Test
*ML / M02 — Linear Algebra*

This diagnostic checks the computational and proof skills used throughout this module.

## How to Use This Test

- Suggested time: **90 minutes**. You may use a scientific calculator, but show all algebraic work.
- For proof questions, state the theorem or definition you use and justify each implication.
- This is a diagnostic, not a graded exam. Work before consulting the [solutions](./02-diagnostic-test-solutions.md).

## Problem 1: Matrix Operations

Let

$$
A=\begin{pmatrix}1&2\\-1&3\end{pmatrix},\qquad
B=\begin{pmatrix}2&-1\\4&0\end{pmatrix},\qquad
C=\begin{pmatrix}1&0\\2&-1\end{pmatrix}.
$$

Compute each expression. For part (d), state whether the product is defined before computing it.

1. $2A-B$
2. $AB$
3. $BA$
4. $AC$ and $CA$
5. $A^T A$

What do your answers to parts (b) and (c) show about matrix multiplication?

## Problem 2: Eigenvalues, Eigenvectors, and Diagonalization

Let

$$
M=\begin{pmatrix}4&1\\2&3\end{pmatrix}.
$$

1. Find the eigenvalues of $M$.
2. Find an eigenvector for each eigenvalue.
3. Diagonalize $M$ by finding an invertible matrix $P$ and a diagonal matrix $D$ such that $M=PDP^{-1}$.

## Problem 3: Principal Axes of an Ellipse

Consider the ellipse

$$
5x^2-6xy+5y^2=8.
$$

1. Write its quadratic-form matrix $Q$ so that $\begin{pmatrix}x&y\end{pmatrix}Q\begin{pmatrix}x\\y\end{pmatrix}=5x^2-6xy+5y^2$.
2. Find the principal directions using the eigenvalues and eigenvectors of $Q$.
3. Find the lengths of the major (long) and minor (short) **semi-axes**, and hence the full major- and minor-axis lengths.
4. Give equations of the lines containing the major and minor axes in the original $xy$-coordinates.

## Problem 4: Matrix Exponential

For a square matrix $A$, the matrix exponential is defined by

$$
e^A=I+A+\frac{A^2}{2!}+\frac{A^3}{3!}+\cdots.
$$

Use an orthonormal diagonalization of $A$ and the defining series to calculate $e^A$
for the non-diagonal symmetric matrix

$$
A=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
$$

Find an orthogonal matrix $P$ and diagonal matrix $D$ with $A=PDP^T$, then express
$e^A$ as a concrete $2\times2$ matrix.

## Problem 5: Reality of Eigenvalues

Prove that every eigenvalue of a real symmetric matrix is real. You may allow eigenvectors to have complex entries.

## Problem 6: Orthogonality of Eigenvectors

Prove that eigenvectors of a real symmetric matrix belonging to distinct eigenvalues are orthogonal.

## Problem 7: Commuting Real Symmetric Matrices

Let $A$ and $B$ be real symmetric $n\times n$ matrices, each with $n$ distinct
(non-repeating) eigenvalues. Prove that

$$AB=BA$$

if and only if $A$ and $B$ have a **common orthonormal basis of eigenvectors** (equivalently, they are simultaneously orthogonally diagonalizable).

## Problem 8: Positive Semidefiniteness

Prove that $A^T A$ is positive semidefinite for every real $m\times n$ matrix $A$.

## Problem 9: Nonzero Eigenvalues of $A^T A$ and $AA^T$

Let $A$ be a real $m\times n$ matrix. Prove that if $k\ne0$ is an eigenvalue of $A^T A$, then $k$ is also an eigenvalue of $AA^T$.

## Skills Map

| Problem | Skill assessed |
|---|---|
| 1 | Addition, scalar multiplication, multiplication, transpose |
| 2 | Characteristic polynomial, eigenvectors, diagonalization |
| 3 | Quadratic forms, spectral decomposition, ellipse axes |
| 4 | Power-series definition of the matrix exponential |
| 5 | Spectral properties of real symmetric matrices |
| 6 | Orthogonality for distinct symmetric-matrix eigenspaces |
| 7 | Simultaneous orthogonal diagonalization |
| 8 | Positive semidefiniteness of a Gram matrix |
| 9 | Correspondence of nonzero Gram-matrix eigenvalues |
