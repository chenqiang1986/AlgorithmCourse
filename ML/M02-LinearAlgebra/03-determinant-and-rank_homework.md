# Homework: Determinants and Rank
*ML / M02 — Linear Algebra, Class 3*

Use the [determinants and rank lesson](./03-determinant-and-rank.md) as a
reference. Show row operations, identify pivots and free variables, and justify
each conclusion about rank or invertibility.

## 1. Determinants by row reduction

Compute the determinant of

$$
A=\begin{pmatrix}
2&1&-1\\
4&3&0\\
-2&1&5
\end{pmatrix}
$$

by row reduction. Record the effect of every row operation on the determinant.

## 2. A parameter and invertibility

For

$$
B_t=\begin{pmatrix}
1&1&0\\
0&t&1\\
2&3&1
\end{pmatrix},
$$

1. compute $\det(B_t)$;
2. find every value of $t$ for which $B_t$ is singular; and
3. state the rank of $B_t$ when $t=1$ and when $t=2$.

## 3. Null space and rank--nullity

Row-reduce

$$
C=\begin{pmatrix}
1&2&-1&3\\
2&4&1&7\\
1&2&2&6
\end{pmatrix}.
$$

Then find:

1. $\operatorname{rank}(C)$;
2. a basis for $\operatorname{Null}(C)$; and
3. $\dim\operatorname{Null}(C)$, checking rank--nullity explicitly.

## 4. Read solution structure from an augmented matrix

Each matrix below is an RREF augmented matrix for a system with variables
$x_1,x_2,x_3$.

$$
R_1=
\begin{pmatrix}
1&0&2&\mid&3\\
0&1&-1&\mid&4\\
0&0&0&\mid&0
\end{pmatrix},
\qquad
R_2=
\begin{pmatrix}
1&0&0&\mid&2\\
0&1&0&\mid&-1\\
0&0&1&\mid&5
\end{pmatrix},
$$

$$
R_3=
\begin{pmatrix}
1&0&1&\mid&0\\
0&0&0&\mid&1
\end{pmatrix}.
$$

For each system, decide whether it has no solution, one solution, or infinitely
many solutions. When solutions exist, give the solution set and explain your
decision using ranks and free variables.

## 5. Independence and minors

Let

$$
u_1=\begin{pmatrix}1\\2\\1\end{pmatrix},
\qquad
u_2=\begin{pmatrix}0\\1\\1\end{pmatrix},
\qquad
u_3=\begin{pmatrix}2\\5\\3\end{pmatrix}.
$$

Are $u_1,u_2,u_3$ linearly independent? Answer using the determinant of the
matrix with these vectors as columns. Then explain what your answer says about
the rank of that matrix and the solution of $Ax=0$.

## 6. Rank in a data matrix

Suppose a $5\times8$ data matrix has rank $5$.

1. What is the dimension of its null space?
2. Can all eight columns be linearly independent? Explain.
3. What does a nonzero vector in its null space say about the columns?

## Challenge: dependence without calculating a determinant

Let $D$ be a $4\times4$ matrix whose rows satisfy

$$
r_4=3r_1-r_2+2r_3.
$$

Prove that $\det(D)=0$. Then explain why $Dx=b$ cannot have exactly one
solution for every $b\in\mathbb R^4$.

## Challenge: prove a rank inequality for a product

Let $A$ be an $m\times n$ matrix and $B$ an $n\times p$ matrix. Prove
that

$$
\operatorname{rank}(AB)\leq \min\bigl(\operatorname{rank}(A),\operatorname{rank}(B)\bigr).
$$

Use the following steps as guidance:

**Part A.** Let $M$ be an $m\times n$ matrix with $n>m$. Explain why
$Mx=0$ must have a nontrivial solution, using rank--nullity and the fact that
$\operatorname{rank}(M)\leq m$.

**Part B.** Suppose $a_1,\ldots,a_m$ are vectors and each of
$v_1,\ldots,v_n$ is a linear combination of $a_1,\ldots,a_m$, where $n>m$.
Use Part A (or its dependence principle) to explain why
$v_1,\ldots,v_n$ must be linearly dependent.

**Part C.** Write $A$ as a horizontal concatenation of its column vectors,
$A=[a_1\ \cdots\ a_n]$, and display the entries of $B$ as

$$
B=\begin{pmatrix}
b_{11}&b_{12}&\cdots&b_{1p}\\
b_{21}&b_{22}&\cdots&b_{2p}\\
\vdots&\vdots&\ddots&\vdots\\
b_{n1}&b_{n2}&\cdots&b_{np}
\end{pmatrix}.
$$

Use matrix multiplication to express each column of $AB$ as a linear
combination of $a_1,\ldots,a_n$ (for example, its j-th column is
$b_{1j}a_1+\cdots+b_{nj}a_n$). What does this tell you about the span of the
columns of $AB$ and therefore about $\operatorname{rank}(AB)$ compared with
$\operatorname{rank}(A)$? Then apply the same conclusion to
$(AB)^T=B^TA^T$ and use $\operatorname{rank}(X^T)=\operatorname{rank}(X)$ to
obtain the bound involving $\operatorname{rank}(B)$.
