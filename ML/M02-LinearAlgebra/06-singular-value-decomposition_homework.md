# SVD Practice: Energy and Image Compression
*ML / M02 — Linear Algebra*

This practice connects one algebraic fact about SVD to a visible application:
compressing a grayscale image while retaining its most important patterns.

## Part 0: Guided Proof — Existence of the SVD

Let $A$ be an $m\times n$ real matrix. In this exercise, prove that $A$ has a
singular value decomposition by building it from the eigenvalues and
eigenvectors of $A^TA$. You may use the spectral theorem for real symmetric
matrices: a real symmetric matrix has an orthonormal basis of eigenvectors.

Let $r$ be the number of positive eigenvalues of $A^TA$. Choose orthonormal
eigenvectors $v_1,\ldots,v_n$ of $A^TA$ so that their eigenvalues are

$$
\sigma_1^2,\ldots,\sigma_r^2,0,\ldots,0,
$$

where $\sigma_i>0$ for $1\le i\le r$. Let

$$
V_r=[v_1\ v_2\ \cdots\ v_r],
\qquad
U_r=\left[\frac{Av_1}{\sigma_1}\ \frac{Av_2}{\sigma_2}\ \cdots\ \frac{Av_r}{\sigma_r}\right],
$$

and let $V=[v_1\ v_2\ \cdots\ v_n]=[V_r\ V_{\mathrm{extra}}]$.

### Exercise 0

Complete the following steps.

1. Show that $A^TA$ is symmetric. Then show that every eigenvalue of $A^TA$
   is nonnegative. *(Hint: evaluate $x^TA^TAx$.)*

2. For $1\le i,j\le r$, show that the vectors

   $$
   u_i=\frac{Av_i}{\sigma_i}
   $$

   are orthonormal; that is, prove $u_i^Tu_j=\delta_{ij}$.

3. Let $\Sigma_r=\operatorname{diag}(\sigma_1,\ldots,\sigma_r)$. Show that

   $$
   AV_rV_r^T=U_r\Sigma_rV_r^T.
   $$

4. Show that $Av_i=0$ for every $i>r$. *(Hint: compute $\|Av_i\|^2$.)*

5. Use $V=[V_r\ V_{\mathrm{extra}}]$, $V^TV=I$, and the result of step 4 to
   show that

   $$
   A=AVV^T=AV_rV_r^T.
   $$

6. Combine steps 3 and 5 to conclude that

   $$
   A=U_r\Sigma_rV_r^T.
   $$

   Explain why this is a reduced SVD of $A$. Finally, explain how extending
   the orthonormal columns of $U_r$ to an orthonormal basis of $\mathbb{R}^m$
   gives the full SVD $A=U\Sigma V^T$.

## Part 1: Frobenius Norm and Singular Values

For an $m\times n$ matrix $A=(a_{ij})$, the **Frobenius norm** is

$$
\|A\|_F=\sqrt{\sum_{i=1}^m\sum_{j=1}^n a_{ij}^2}.
$$

Suppose that

$$
A=U\Sigma V^T
$$

is an SVD of $A$, with singular values $\sigma_1,\ldots,\sigma_r$.

### Exercise 1

Prove that

$$
\boxed{\|A\|_F^2=\sigma_1^2+\sigma_2^2+\cdots+\sigma_r^2.}
$$

Use these facts:

$$
\|A\|_F^2=\operatorname{tr}(A^TA),
\qquad \operatorname{tr}(BC)=\operatorname{tr}(CB)
$$

whenever both products are defined.

### Exercise 2

Let the singular values of a matrix be $10$, $4$, $1$, and $0.5$.

1. Find $\|A\|_F^2$ and $\|A\|_F$.
2. A rank-$1$ approximation keeps only the singular value $10$. What fraction of
   the squared Frobenius norm does it retain?
3. What is the squared Frobenius-norm error after this rank-$1$ approximation?

### Why this matters

The quantity $\sigma_i^2$ is often called the **energy** contributed by singular
direction $i$. Because the singular values are sorted, the first few terms tell
us how much of the matrix can be retained by a low-rank approximation.

<details>
<summary>Solution</summary>

Since $A^T=V\Sigma^TU^T$ and $U^TU=I$,

$$
\begin{aligned}
\|A\|_F^2
&=\operatorname{tr}(A^TA)\\
&=\operatorname{tr}\left(V\Sigma^TU^TU\Sigma V^T\right)\\
&=\operatorname{tr}\left(V\Sigma^T\Sigma V^T\right)\\
&=\operatorname{tr}\left(\Sigma^T\Sigma V^TV\right)\\
&=\operatorname{tr}(\Sigma^T\Sigma)\\
&=\sum_{i=1}^r\sigma_i^2.
\end{aligned}
$$

For Exercise 2,

$$
\|A\|_F^2=10^2+4^2+1^2+0.5^2=117.25,
\qquad \|A\|_F\approx10.828.
$$

The rank-$1$ approximation retains $100/117.25\approx85.3\%$ of the squared
Frobenius norm. Its squared error is $17.25$, the sum of the squares of the
discarded singular values.

</details>

## Part 2: Classic Lab — Compress a Grayscale Image

An $m\times n$ grayscale image is a matrix: each entry is a pixel intensity from
black ($0$) to white ($255$). If

$$
A=U\Sigma V^T,
$$

then its rank-$k$ compressed version is

$$
A_k=U_k\Sigma_kV_k^T.
$$

The code in [`practice_ws/image_svd_compression.py`](./practice_ws/image_svd_compression.py)
loads an image, converts it to grayscale, reconstructs it using several values
of $k$, prints reconstruction errors, and displays the results.

### Run It

Install the required packages if needed:

```bash
python3 -m pip install numpy pillow matplotlib
```

Then supply any image file:

```bash
python3 practice_ws/image_svd_compression.py path/to/photo.jpg
```

You can choose the ranks shown in the figure:

```bash
python3 practice_ws/image_svd_compression.py path/to/photo.jpg --ranks 1 5 20 50 100
```

### Investigate

1. Start with $k=1$, then increase $k$. Which visual features appear first?
2. Find the smallest $k$ for which the image looks acceptably close to the
   original. What percentage of the original $mn$ entries does the rank-$k$
   representation store? Use $k(m+n+1)/(mn)$.
3. Compare the script's relative error with

   $$
   \frac{\sqrt{\sum_{i=k+1}^r\sigma_i^2}}
        {\sqrt{\sum_{i=1}^r\sigma_i^2}}.
   $$

   Explain why they agree.
4. Try an image with a plain background and one with detailed texture. Which
   compresses more effectively, and what do their singular-value curves show?

## Extension: Color Images

A color image has three channels (red, green, blue), not one matrix. Apply the
same SVD procedure separately to each channel, then stack the three compressed
channels back together. Does using the same $k$ for each channel look balanced?
