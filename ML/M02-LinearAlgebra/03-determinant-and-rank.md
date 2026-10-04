# Determinants and Rank
*ML / M02 — Linear Algebra*

Determinant and rank answer complementary questions about a matrix: does a
square transformation collapse space, and how many independent directions does
it preserve? They underlie invertibility, solution uniqueness, and the number
of useful directions in data.

## Learning Goals

By the end of this lesson, you should be able to:

- state the permutation definition of a determinant and compute one using row
  operations;
- track how each elementary row operation changes a determinant;
- define row rank, column rank, and determinant rank, and explain why they
  agree;
- define $\operatorname{Null}(A)$; and
- apply rank--nullity to predict the solution structure of a linear system.

## Gaussian Elimination for Homogeneous Systems

Before introducing determinants, consider the homogeneous system

$$
Ax=0,
$$

where $A$ is an $m\times n$ coefficient matrix and
$x=(x_1,\ldots,x_n)^T$. **Gaussian elimination** replaces the system with an
equivalent, simpler one by using these elementary row operations:

| Row operation | Equation-level meaning |
| --- | --- |
| $R_i\leftrightarrow R_j$ | reorder two equations |
| $R_i\leftarrow cR_i$, $c\ne0$ | multiply an equation by a nonzero constant |
| $R_i\leftarrow R_i+cR_j$, $i\ne j$ | add a multiple of one equation to another |

Each operation preserves exactly the same solution set. A **row-echelon
matrix** has all zero rows at the bottom, and each pivot lies strictly to the
right of the pivot in the row above. The first nonzero entry of a nonzero row
is a **pivot**. A column containing a pivot is a **pivot column**. The
variable in a pivot column is a **pivot variable**: after the free variables
have been chosen, the equations determine it. Variables in the remaining
columns are **free variables**.

### Example: Pivots, Free Variables, Null Space, and Row Rank

Solve $Ax=0$ for

$$
A=\begin{pmatrix}
1&2&0&-1\\
0&0&1&3\\
1&2&2&5
\end{pmatrix}.
$$

Elimination gives

$$
\begin{pmatrix}
1&2&0&-1\\
0&0&1&3\\
1&2&2&5
\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-R_1}
\begin{pmatrix}
1&2&0&-1\\
0&0&1&3\\
0&0&2&6
\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-2R_2}
\begin{pmatrix}
1&2&0&-1\\
0&0&1&3\\
0&0&0&0
\end{pmatrix}.
$$

Columns $1$ and $3$ are pivot columns, so $x_1,x_3$ are pivot variables.
Columns $2$ and $4$ have no pivot, so let $x_2=s$ and $x_4=t$ be free. The
reduced equations give

$$
x_1=-2s+t,\qquad x_3=-3t,
$$

and hence

$$
x=s\begin{pmatrix}-2\\1\\0\\0\end{pmatrix}
+t\begin{pmatrix}1\\0\\-3\\1\end{pmatrix}.
$$

The set of all solutions of $Ax=0$ is the **null space**:

$$
\operatorname{Null}(A)=\{x\in\mathbb{R}^4:Ax=0\}
=\operatorname{span}\left\{
\begin{pmatrix}-2\\1\\0\\0\end{pmatrix},
\begin{pmatrix}1\\0\\-3\\1\end{pmatrix}\right\}.
$$

For this system:

- There are two pivot rows, so although $A$ starts with three equations, it
  provides only **two independent equations**.
- There are two pivot columns, and hence two pivot variables: $x_1$ and
  $x_3$. The number of pivot columns equals the number of pivot rows.

  - Each pivot equation uniquely determines the value of its pivot variable
    once the free variables are chosen. Thus a pivot variable has no value of
    its own left to choose, and each pivot equation accounts for one such
    non-free variable.
- There are two free variables, $x_2$ and $x_4$, so
  $\dim\operatorname{Null}(A)=2$.
- Their sum is $2+2=4$, the number of columns (and therefore the number of
  variables): independent equations plus free variables equals the number of
  variables.

<svg viewBox="0 0 720 300" width="100%" role="img" aria-label="The row-echelon matrix with pivot columns one and three, free columns two and four, and the first nonzero entry in each nonzero row circled.">
  <style>
    .label{font:600 15px sans-serif;letter-spacing:.06em}
    .pivot-label{fill:#166534}.free-label{fill:#9a3412}
    .entry{font:22px sans-serif;fill:#0f172a;text-anchor:middle;dominant-baseline:middle}
    .bracket{fill:none;stroke:#334155;stroke-width:3}
    .grid{stroke:#cbd5e1;stroke-width:1.5}
    .pivot-cell{fill:#dcfce7}.free-cell{fill:#ffedd5}
    .pivot-ring{fill:none;stroke:#15803d;stroke-width:3}
    .caption{font:16px sans-serif;fill:#334155;text-anchor:middle}
  </style>
  <text class="label pivot-label" x="210" y="32" text-anchor="middle">PIVOT</text>
  <text class="label free-label" x="330" y="32" text-anchor="middle">FREE</text>
  <text class="label pivot-label" x="450" y="32" text-anchor="middle">PIVOT</text>
  <text class="label free-label" x="570" y="32" text-anchor="middle">FREE</text>
  <path d="M210 42v18 M330 42v18 M450 42v18 M570 42v18" stroke="#94a3b8" stroke-width="1.5"/>
  <rect class="pivot-cell" x="150" y="70" width="120" height="55" rx="4"/><rect class="free-cell" x="270" y="70" width="120" height="55" rx="4"/><rect class="pivot-cell" x="390" y="70" width="120" height="55" rx="4"/><rect class="free-cell" x="510" y="70" width="120" height="55" rx="4"/>
  <rect class="pivot-cell" x="150" y="125" width="120" height="55" rx="4"/><rect class="free-cell" x="270" y="125" width="120" height="55" rx="4"/><rect class="pivot-cell" x="390" y="125" width="120" height="55" rx="4"/><rect class="free-cell" x="510" y="125" width="120" height="55" rx="4"/>
  <rect class="pivot-cell" x="150" y="180" width="120" height="55" rx="4"/><rect class="free-cell" x="270" y="180" width="120" height="55" rx="4"/><rect class="pivot-cell" x="390" y="180" width="120" height="55" rx="4"/><rect class="free-cell" x="510" y="180" width="120" height="55" rx="4"/>
  <path class="grid" d="M270 70v165 M390 70v165 M510 70v165 M150 125h480 M150 180h480"/>
  <path class="bracket" d="M132 70h-12v165h12 M648 70h12v165h-12"/>
  <text class="entry" x="210" y="97">1</text><text class="entry" x="330" y="97">2</text><text class="entry" x="450" y="97">0</text><text class="entry" x="570" y="97">−1</text>
  <text class="entry" x="210" y="152">0</text><text class="entry" x="330" y="152">0</text><text class="entry" x="450" y="152">1</text><text class="entry" x="570" y="152">3</text>
  <text class="entry" x="210" y="207">0</text><text class="entry" x="330" y="207">0</text><text class="entry" x="450" y="207">0</text><text class="entry" x="570" y="207">0</text>
  <circle class="pivot-ring" cx="210" cy="97" r="23"/><circle class="pivot-ring" cx="450" cy="152" r="23"/>
  <text class="caption" x="390" y="278">Circled entries are the pivots: the first nonzero coefficient in each nonzero row.</text>
</svg>

## Determinant: the Full Definition

Suppose $A$ is an $n\times n$ square matrix. Generically, the homogeneous
system $Ax=0$ has the unique solution $x=0$. But, as the elimination example
showed, if $A$ provides fewer than $n$ independent equations, some entries of
$x$ are free variables and $Ax=0$ has nonzero solutions. Is there a universal
way to tell these two cases apart? Yes: the determinant.

Let $A=(a_{ij})$ be an $n\times n$ matrix. A **permutation** $\sigma$ of
$\{1,\ldots,n\}$ chooses exactly one entry from every row and every column:

$$
a_{1,\sigma(1)}a_{2,\sigma(2)}\cdots a_{n,\sigma(n)}.
$$

Its sign, $\operatorname{sgn}(\sigma)$, is $+1$ when $\sigma$ is even and
$-1$ when it is odd; equivalently, it is $(-1)^k$, where $k$ is the number of
pairwise swaps needed to put the list
$\bigl(\sigma(1),\ldots,\sigma(n)\bigr)$ back in order. The **determinant**
is

$$
\boxed{\det(A)=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
\prod_{i=1}^n a_{i,\sigma(i)}.}
$$

Here $S_n$ is the set of all $n!$ permutations. Thus the formula sums all
ways to select one entry per row and column, adding even selections and
subtracting odd selections.

**Row--column symmetry.** The formula treats rows and columns symmetrically:
every term selects one entry from each of both. Transposing $A$ merely
exchanges those roles, so

$$
\det(A^T)=\det(A).
$$

### A $2\times2$ Determinant

For $A=(a_{ij})\in\mathbb{R}^{2\times2}$, there are exactly two
permutations:

| $\sigma$ as a list | Selected product | Parity | Contribution |
| --- | --- | --- | --- |
| $(1,2)$ | $a_{11}a_{22}$ | even | $+a_{11}a_{22}$ |
| $(2,1)$ | $a_{12}a_{21}$ | odd | $-a_{12}a_{21}$ |

For the first product, $\sigma(1)=1$ and $\sigma(2)=2$: choose column $1$
from row $1$ and column $2$ from row $2$. This is the identity permutation,
so it is even. For the second, $\sigma(1)=2$ and $\sigma(2)=1$; one swap
changes $(1,2)$ to $(2,1)$, so it is odd and its product is subtracted.
Therefore,

$$
\det\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}
=a_{11}a_{22}-a_{12}a_{21}.
$$

### A $3\times3$ Determinant

For $A=(a_{ij})\in\mathbb{R}^{3\times3}$, the six permutations select the
following products:

| $\sigma$ as a list | Selected product | Parity |
| --- | --- | --- |
| $(1,2,3)$ | $a_{11}a_{22}a_{33}$ | even |
| $(2,3,1)$ | $a_{12}a_{23}a_{31}$ | even |
| $(3,1,2)$ | $a_{13}a_{21}a_{32}$ | even |
| $(1,3,2)$ | $a_{11}a_{23}a_{32}$ | odd |
| $(3,2,1)$ | $a_{13}a_{22}a_{31}$ | odd |
| $(2,1,3)$ | $a_{12}a_{21}a_{33}$ | odd |

For example, $(2,3,1)$ is even because it can be reached from $(1,2,3)$ by
two swaps, while $(1,3,2)$ is odd because it needs one swap. Adding the three
even products and subtracting the three odd products gives

$$
\begin{aligned}
\det\begin{pmatrix}
a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}
\end{pmatrix}
={}&a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}\\
&-a_{11}a_{23}a_{32}-a_{13}a_{22}a_{31}-a_{12}a_{21}a_{33}.
\end{aligned}
$$

The formula reveals two essential features: the determinant is linear in each
row when the other rows are fixed, and it is alternating—if two rows are
equal, it is zero; interchanging two rows reverses its sign. Those facts give
the practical calculation rules below.

## Determinant: Signed Scaling for Square Matrices

For a $2\times2$ matrix, $|\det(A)|$ is the factor by which $A$ scales area.
Its sign records whether orientation is preserved or reversed. Thus
$\det(A)=0$ means that $A$ flattens the plane into a line (or a point), so it
cannot be reversed. For an $n\times n$ matrix, the analogous meaning is signed
$n$-dimensional volume scaling.

<svg viewBox="0 0 740 210" width="100%" role="img" aria-label="A unit square transformed into a parallelogram of signed area determinant A.">
  <style>.axis{stroke:#94a3b8;stroke-width:1.5}.edge{fill:#bfdbfe;stroke:#2563eb;stroke-width:2.5}.arrow{stroke:#334155;stroke-width:2;marker-end:url(#detArrow)}.t{font:16px sans-serif;fill:#0f172a}.s{font:14px sans-serif;fill:#334155}</style>
  <defs><marker id="detArrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#334155"/></marker></defs>
  <line class="axis" x1="35" y1="165" x2="225" y2="165"/><line class="axis" x1="80" y1="195" x2="80" y2="20"/>
  <rect class="edge" x="80" y="75" width="75" height="90"/><text class="t" x="76" y="205">unit square</text><text class="s" x="44" y="62">area 1</text>
  <line class="arrow" x1="250" y1="112" x2="335" y2="112"/><text class="t" x="279" y="92">A</text>
  <line class="axis" x1="375" y1="165" x2="700" y2="165"/><line class="axis" x1="425" y1="195" x2="425" y2="20"/>
  <polygon class="edge" points="425,165 590,165 650,67 485,67"/><text class="t" x="486" y="205">parallelogram</text><text class="s" x="502" y="54">area $|\det(A)|$</text>
</svg>

## Row Operations Make Determinants Computable

The definition of $\det(A)$ has $n!$ terms, which is inconvenient to compute
directly except for very small matrices. Real determinant calculation relies
on row operations instead. These are exactly the elementary operations used in
Gaussian elimination; the only extra task is to track how each operation
changes the determinant. The definition immediately implies the following
rules for a row operation on a square matrix:

| Operation | Effect on the determinant |
| --- | --- |
| $R_i\leftrightarrow R_j$ | multiply by $-1$ |
| $R_i\leftarrow cR_i$ | multiply by $c$ |
| $R_i\leftarrow R_i+cR_j$ ($i\ne j$) | unchanged |

The last rule follows from row-linearity: the extra term has two copies of
$R_j$ and therefore has determinant zero. A triangular matrix has determinant
equal to the product of its diagonal entries, since all other permutation
products contain a zero.

When using elimination, record the operations. For example,

$$
\begin{aligned}
\det\begin{pmatrix}1&2&1\\2&5&3\\1&0&1\end{pmatrix}
&=\det\begin{pmatrix}1&2&1\\0&1&1\\0&-2&0\end{pmatrix}
&&\bigl(R_2\leftarrow R_2-2R_1,\;R_3\leftarrow R_3-R_1\bigr)\\
&=\det\begin{pmatrix}1&2&1\\0&1&1\\0&0&2\end{pmatrix}
&&\bigl(R_3\leftarrow R_3+2R_2\bigr)\\
&=1\cdot1\cdot2=2.
\end{aligned}
$$

All operations here preserve the determinant. If instead a row had been
scaled by $c$, divide the final diagonal product by $c$; if rows had been
swapped $s$ times, multiply the result by $(-1)^s$.

## Linear Independence

Vectors $a_1,\ldots,a_n$ are **linearly independent** when the equation

$$
k_1a_1+k_2a_2+\cdots+k_na_n=0
$$

has only the trivial solution

$$
k_1=k_2=\cdots=k_n=0.
$$

In other words, no vector in the collection can be made by combining the
others. If there is a solution with at least one $k_i\ne0$, the vectors are
**linearly dependent**.

### Determinant Criterion for Dependence

For a square matrix $A\in\mathbb{R}^{n\times n}$,

$$
\boxed{\det(A)=0
\iff \text{the rows of }A\text{ are linearly dependent}
\iff \text{the columns of }A\text{ are linearly dependent}.}
$$

Row-reduce $A$ to an echelon matrix $R$. The elementary row operations preserve
the solution set of $Ax=0$, so $Ax=0$ and $Rx=0$ have the same solutions. As
seen in the Gaussian-elimination section,

$$
Ax=0\text{ has a nonzero solution}
\iff \text{there is a free variable}.
$$

Because $A$ is square, a free variable occurs exactly when $R$ has fewer than
$n$ pivots—equivalently, when its triangular diagonal contains a zero. The
row-operation rules preserve whether a determinant is zero, and the determinant
of $R$ is the product of its diagonal entries. Therefore,

$$
\det(A)=0\iff Ax=0\text{ has a nonzero solution}.
$$

Now write $A$ as its column vectors:

$$
A=[a_1\ a_2\ \cdots\ a_n].
$$

Then

$$
Ax=0
\iff x_1a_1+x_2a_2+\cdots+x_na_n=0.
$$

Thus a nonzero solution $x$ is precisely a nontrivial linear combination of
the columns that equals zero—the definition of linearly dependent columns.
This proves the column statement. Finally, $\det(A^T)=\det(A)$, and the
columns of $A^T$ are the rows of $A$, which proves the row statement.

## Three Definitions of Rank

Let $A$ be an $m\times n$ matrix.

- The **row rank** is the largest number of linearly independent row vectors
  of $A$; equivalently, it is the size of a largest linearly independent subset
  of the rows of $A$.
- The **column rank** is the largest number of linearly independent column
  vectors of $A$; equivalently, it is the size of a largest linearly
  independent subset of the columns of $A$.
- The **determinant rank** is the largest integer $r$ for which $A$ has an
  $r\times r$ submatrix with nonzero determinant. Such a square submatrix is
  called a nonzero $r$-minor. By convention, its value is $0$ when $A$ is the
  zero matrix.

### Rank Theorem

$$
\boxed{\operatorname{rowrank}(A)=\operatorname{colrank}(A)
=\operatorname{detrank}(A)=\operatorname{rank}(A).}
$$

**Proof.**

1. **$\operatorname{detrank}(A)\le\operatorname{rowrank}(A)$.** Let $s$
   be the determinant rank. Then $A$ has an $s\times s$ minor with nonzero
   determinant. By the determinant criterion for dependence, the $s$ rows of
   that square minor are linearly independent. If the corresponding full row
   vectors of $A$ were dependent, restricting their linear relation to the
   selected $s$ columns would make the minor's rows dependent—a contradiction.
   Thus extending these rows from $s$ selected entries back to all $n$ entries
   preserves their independence. Hence $A$ has $s$ independent rows, so
   $s\le\operatorname{rowrank}(A)$.

2. **$\operatorname{detrank}(A)\ge\operatorname{rowrank}(A)$.** Let $r$
   be the row rank, and select $r$ linearly independent rows of $A$. Treat
   them as an $r\times n$ matrix $B$ and row-reduce $B$. Row operations
   preserve the independence of these $r$ rows, so the echelon form has a
   pivot in every row. Select its $r$ pivot columns. The resulting $r\times r$
   submatrix is triangular with nonzero diagonal, hence has nonzero
   determinant. Each row operation on $B$ preserves whether any of its
   $r\times r$ minors has determinant zero (it changes a minor only by a sign,
   a nonzero factor, or no change). Therefore the corresponding $r\times r$
   minor in the original rows of $A$ is also nonzero, and
   $\operatorname{detrank}(A)\ge r$.

3. The two inequalities give

   $$
   \operatorname{detrank}(A)=\operatorname{rowrank}(A).
   $$

4. **Column rank follows by symmetry.** Transposition turns columns of $A$
   into rows of $A^T$, and transposing a minor preserves whether its
   determinant is zero. Hence

   $$
   \operatorname{colrank}(A)=\operatorname{rowrank}(A^T)
   =\operatorname{detrank}(A^T)=\operatorname{detrank}(A).
   $$

Consequently, rank can safely mean any of these quantities. In practice it is
usually found as the number of pivots after row reduction, and

$$
0\le\operatorname{rank}(A)\le\min(m,n).
$$

For example,

$$
\begin{pmatrix}1&2&3\\2&4&6\\1&1&1\end{pmatrix}
\longrightarrow
\begin{pmatrix}1&2&3\\0&0&0\\0&-1&-2\end{pmatrix}
\longrightarrow
\begin{pmatrix}1&0&-1\\0&1&2\\0&0&0\end{pmatrix}.
$$

There are two pivots, so all three ranks equal $2$. For instance, the minor
formed by rows $1,3$ and columns $1,2$ has determinant $-1\ne0$, while no
$3\times3$ minor can be nonzero.

## The Invertible Matrix Test

For an $n\times n$ matrix $A$, these statements are equivalent:

$$
\det(A)\ne0
\iff A\text{ is invertible}
\iff \operatorname{rank}(A)=n
\iff Ax=b\text{ has exactly one solution for every }b.
$$

So a zero determinant means at least one input direction is lost: some right
hand sides give no solution and others give infinitely many.

## Null Space and Rank--Nullity

Recall that for $A\in\mathbb{R}^{m\times n}$,
$\operatorname{Null}(A)=\{x\in\mathbb{R}^n:Ax=0\}$. It is a subspace of
$\mathbb{R}^n$, not merely the zero vector; $\operatorname{Null}(A)=\{0\}$
exactly when the columns of $A$ are independent.

The **rank--nullity theorem** states

$$
\boxed{\operatorname{rank}(A)+\dim\operatorname{Null}(A)=n.}
$$

Here $n$ is the number of columns—the dimension of the input space. Thus an
$m\times n$ matrix of rank $r$ has $n-r$ free input directions (one for each
free variable in $Ax=0$).

## Rank and Linear Systems

For $Ax=b$, compare the coefficient matrix $A$ with the augmented matrix
$[A\mid b]$.

- If $\operatorname{rank}(A)\ne\operatorname{rank}([A\mid b])$, the system is inconsistent.
- If the ranks agree and equal the number of variables, there is one solution.
- If the ranks agree but are smaller than the number of variables, there are infinitely many solutions; their homogeneous directions are $\operatorname{Null}(A)$.

## Quick Check

1. In the permutation formula, what does each product select from a matrix?
2. What is the determinant effect of $R_2\leftarrow R_2-4R_1$?
3. Define $\operatorname{Null}(A)$ for $A\in\mathbb{R}^{m\times n}$.
4. A consistent system has four variables and coefficient rank $3$. How many
   free variables does it have?

### Answers

1. One entry from every row and every column; the sign is set by the parity of
   the associated permutation.
2. None: this row replacement leaves the determinant unchanged.
3. $\{x\in\mathbb{R}^n:Ax=0\}$.
4. One, by rank--nullity.
