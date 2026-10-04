# Homework: Quadratic Forms and Positive Definiteness
*ML / M02 — Linear Algebra, Class 5*

Use the [quadratic forms and positive definiteness lesson](./05-quadratic-forms-and-positive-definiteness.md)
as a reference. When classifying a symmetric matrix, state the test you use and
show enough work to support the conclusion.

## 1. Write and evaluate a quadratic form

Let

$$
A=\begin{pmatrix}3&-2\\-2&4\end{pmatrix}.
$$

1. Write $q(x)=x^TAx$ as a polynomial in $x_1$ and $x_2$.
2. Evaluate $q$ at $x=(1,2)^T$ and at $x=(2,1)^T$.
3. Does the cross-term coefficient agree with the two off-diagonal entries?
   Explain.

## 2. The symmetric part

Let

$$
B=\begin{pmatrix}1&4\\-2&3\end{pmatrix}.
$$

1. Find the symmetric part $S=(B+B^T)/2$.
2. Verify directly that $x^TBx=x^TSx$ for $x=(x_1,x_2)^T$.
3. Why is it enough to study $S$ when analyzing the quadratic form?

## 3. Classify using eigenvalues

Classify each symmetric matrix as positive definite, positive semidefinite, or
indefinite. Use its eigenvalues.

$$
A_1=\begin{pmatrix}4&0\\0&1\end{pmatrix},
\qquad
A_2=\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
A_3=\begin{pmatrix}1&2\\2&-1\end{pmatrix}.
$$

For the indefinite matrix, give one nonzero vector where the quadratic form is
positive and one where it is negative.

## 4. The $2\times2$ positive-definiteness test

For which values of $t$ is

$$
C_t=\begin{pmatrix}t&2\\2&5\end{pmatrix}
$$

positive definite? Use the leading-principal-minor test

$$
a>0,\qquad ac-b^2>0.
$$

## 5. Principal axes

The symmetric matrix

$$
D=\begin{pmatrix}2&0\\0&8\end{pmatrix}
$$

already uses its eigenvector coordinates.

1. Write the equation of the level set $x^TDx=8$.
2. Identify the lengths of its two semiaxes.
3. Which direction has greater curvature, and how do you see it from the
   eigenvalues?

## 6. Hessians and critical points

At a critical point, a twice-differentiable function has the following Hessian
matrices. Classify the critical point as a strict local minimum, a strict local
maximum, saddle point, or inconclusive from this test.

$$
H_1=\begin{pmatrix}6&1\\1&3\end{pmatrix},
\qquad
H_2=\begin{pmatrix}-2&0\\0&-5\end{pmatrix},
\qquad
H_3=\begin{pmatrix}1&0\\0&-4\end{pmatrix},
\qquad
H_4=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
$$

## Challenge: conditioning

Let

$$
E=\begin{pmatrix}1&0\\0&100\end{pmatrix}.
$$

1. Find its spectral condition number.
2. Compare the level set $x^TEx=100$ with the level set $x^TIx=100$.
3. In two or three sentences, explain why a large condition number can make
   gradient descent zig-zag.
