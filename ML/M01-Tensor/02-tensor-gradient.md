# Lesson 2: Tensor Gradients
*ML / M01-Tensor*

Many ML quantities are tensors: a vector of model outputs, a matrix of attention scores, or a batch of images. To differentiate a tensor-valued function with respect to a tensor input, differentiate one output component with respect to one input component. The collection of all those derivatives is itself a tensor.

This lesson uses **output indices first, input indices second**. Keeping this convention fixed makes both the shape and the chain rule easy to read.

## 1. Gradient of a tensor-valued function

Let the input $X$ be an order-$p$ tensor with components

$$
X_{i_1\ldots i_p},
$$

and let the output $Y=f(X)$ be an order-$q$ tensor with components

$$
Y_{j_1\ldots j_q} = f_{j_1\ldots j_q}(X).
$$

The gradient of $Y$ with respect to $X$ is defined component by component:

$$
\boxed{
\left(\nabla_X Y\right)_{j_1\ldots j_q\,i_1\ldots i_p}
= \frac{\partial Y_{j_1\ldots j_q}}
        {\partial X_{i_1\ldots i_p}}
}
$$

There are $q$ output indices and $p$ input indices, so $\nabla_XY$ has order $p+q$. If

```text
X.shape == (d1, ..., dp)
Y.shape == (e1, ..., eq)
```

then, under this convention,

```text
grad_X_Y.shape == (e1, ..., eq, d1, ..., dp)
```

### Familiar special cases

| Function | Input order | Output order | Derivative | Shape idea |
| --- | ---: | ---: | --- | --- |
| $s=f(x)$ | 1 | 0 | $\partial s/\partial x_i$ | vector |
| $y_i=f_i(x)$ | 1 | 1 | $\partial y_i/\partial x_j$ | matrix (the Jacobian) |
| $Y_{ij}=f_{ij}(x)$ | 1 | 2 | $\partial Y_{ij}/\partial x_k$ | order-3 tensor |
| $s=f(X)$ | 2 | 0 | $\partial s/\partial X_{ij}$ | matrix |
| $Y_{ij}=f_{ij}(X)$ | 2 | 2 | $\partial Y_{ij}/\partial X_{kl}$ | order-4 tensor |

For example, the derivative of a matrix with respect to a matrix is generally an order-4 tensor—not a matrix. A matrix Jacobian appears only when both the input and output are vectors.

### The derivative is a linear map on a small change

For a small perturbation $dX$, the corresponding first-order change in $Y$ is obtained by contracting the input indices of the gradient with the indices of $dX$:

$$
dY_{j_1\ldots j_q}
=
\sum_{i_1,\ldots,i_p}
\frac{\partial Y_{j_1\ldots j_q}}
     {\partial X_{i_1\ldots i_p}}
\,dX_{i_1\ldots i_p}.
$$

In compact notation, $dY=(\nabla_XY)\mathbin{:}dX$, where $:$ means contraction over all input axes. This is the tensor version of $dy=J\,dx$ for a vector Jacobian $J$.

## 2. The delta tensor

The **Kronecker delta** is

$$
\delta_{ij}=
\begin{cases}
1,&i=j,\\
0,&i\ne j.
\end{cases}
$$

It acts like an identity under summation:

$$
\sum_j \delta_{ij}x_j=x_i.
$$

For an order-$p$ tensor, the identity—or **delta tensor**—has $2p$ indices:

$$
\Delta_{i_1\ldots i_p\,k_1\ldots k_p}
=\delta_{i_1k_1}\cdots\delta_{i_pk_p}.
$$

It is $1$ exactly when the input-index tuple equals the output-index tuple, and $0$ otherwise. It leaves a tensor unchanged when contracted with it:

$$
\sum_{k_1,\ldots,k_p}
\Delta_{i_1\ldots i_p\,k_1\ldots k_p}
X_{k_1\ldots k_p}
=X_{i_1\ldots i_p}.
$$

Most importantly, the derivative of a tensor with respect to itself is its delta tensor:

$$
\frac{\partial X_{i_1\ldots i_p}}
     {\partial X_{k_1\ldots k_p}}
=\Delta_{i_1\ldots i_p\,k_1\ldots k_p}.
$$

For a matrix $X$, this says

$$
\frac{\partial X_{ij}}{\partial X_{kl}}
=\delta_{ik}\delta_{jl}.
$$

This formula encodes an intuitive fact: changing $X_{kl}$ changes exactly one component of $X$, namely $X_{kl}$ itself.

## 3. Derivative examples

Unless stated otherwise, tensors other than the variable named in the derivative are constants.

### Example 1: Elementwise square

Let $Y$ have the same shape as $X$ and be defined by

$$Y_{ij}=X_{ij}^2.$$

Differentiate the component $Y_{ij}$ with respect to $X_{kl}$:

$$
\boxed{
(\nabla_X Y)_{ijkl}
=\frac{\partial Y_{ij}}{\partial X_{kl}}
=2X_{ij}\,\delta_{ik}\delta_{jl}
}
$$

The derivative has order 4. The two deltas say that $Y_{ij}$ depends only on the matching input component $X_{ij}$; all other partial derivatives are zero.

More generally, for an elementwise function $Y_{ij}=g(X_{ij})$,

$$
(\nabla_X Y)_{ijkl}
=\frac{\partial Y_{ij}}{\partial X_{kl}}
=g'(X_{ij})\delta_{ik}\delta_{jl}.
$$

### Example 2: Matrix-vector product

Let

$$y_i=\sum_j A_{ij}x_j.$$

With respect to the vector $x$, the output is a vector and the input is a vector, so the derivative is an order-2 tensor:

$$
\begin{aligned}
\frac{\partial y_i}{\partial x_k}
&=\frac{\partial}{\partial x_k}\sum_j A_{ij}x_j \\
&=\sum_j A_{ij}\delta_{jk} \\
&=A_{ik}.
\end{aligned}
$$

Therefore,

$$
\boxed{(\nabla_x y)_{ik}=\frac{\partial y_i}{\partial x_k}=A_{ik}.}
$$

Thus $\nabla_x y=A$: the familiar matrix $A$ is the Jacobian of the linear map $x\mapsto Ax$.

### Example 3: Outer product

Let

$$C_{ij}=x_i y_j.$$

Differentiate with respect to $x_k$:

$$
\boxed{
(\nabla_x C)_{ijk}
=\frac{\partial C_{ij}}{\partial x_k}
=\delta_{ik}y_j
}
$$

Here an order-2 output differentiated by an order-1 input gives an order-3 tensor. The component $x_k$ affects row $k$ of $C$ and no other row.

### Example 4: Matrix product with respect to a matrix

Let

$$C_{ij}=\sum_r A_{ir}B_{rj}.$$

Differentiate with respect to an entry $A_{kl}$:

$$
\begin{aligned}
\frac{\partial C_{ij}}{\partial A_{kl}}
&=\sum_r \frac{\partial}{\partial A_{kl}}(A_{ir}B_{rj})\\
&=\sum_r \delta_{ik}\delta_{rl}B_{rj}\\
&=\delta_{ik}B_{lj}.
\end{aligned}
$$

Therefore,

$$
\boxed{(\nabla_A C)_{ijkl}=\frac{\partial C_{ij}}{\partial A_{kl}}=\delta_{ik}B_{lj}.}
$$

The result has indices $(i,j,k,l)$ and is order 4. Changing $A_{kl}$ affects only row $k$ of $C$; within that row it contributes the row $l$ of $B$.

### Example 5: Trace

For a square matrix $X$,

$$s=\operatorname{trace}(X)=\sum_iX_{ii}.$$

The output is scalar, so its gradient with respect to the matrix is order 2:

$$
\frac{\partial s}{\partial X_{kl}}
=\sum_i\delta_{ik}\delta_{il}
=\delta_{kl}.
$$

Therefore,

$$
\boxed{(\nabla_X s)_{kl}=\frac{\partial s}{\partial X_{kl}}=\delta_{kl}.}
$$

Therefore $\nabla_X\operatorname{trace}(X)=I$: the gradient has ones on the diagonal and zeros elsewhere.

## 4. A small numerical check

For $C=AB$, Example 4 predicts

$$
\frac{\partial C_{ij}}{\partial A_{kl}}=\delta_{ik}B_{lj}.
$$

The following finite-difference check perturbs one entry of $A$. It should affect only the corresponding row of `C`, with derivative equal to the selected row of `B`.

```python
import numpy as np

A = np.array([[1.0, 2.0], [3.0, 4.0]])
B = np.array([[5.0, 6.0], [7.0, 8.0]])

k, l = 0, 1                 # differentiate with respect to A[k, l]
eps = 1e-6
E = np.zeros_like(A)
E[k, l] = 1.0

finite_difference = ((A + eps * E) @ B - A @ B) / eps
print(finite_difference)
# [[7. 8.]
#  [0. 0.]]

expected = np.zeros_like(A @ B)
expected[k, :] = B[l, :]
np.allclose(finite_difference, expected)  # True
```

## 5. Practical ML note: full gradients versus scalar-loss gradients

The full derivative $\nabla_XY$ can be very large. For example, if `X` and `Y` are both `(n, n)` matrices, then $\partial Y_{ij}/\partial X_{kl}$ has $n^4$ entries.

Training normally differentiates a **scalar loss** $L$ with respect to parameters $W$. Then $\nabla_WL$ has the same shape as $W$, because the output order is zero. Automatic-differentiation systems exploit the chain rule to compute this scalar-loss gradient without explicitly constructing every intermediate high-order derivative tensor.

## 6. Summary

- If an order-$q$ output is differentiated with respect to an order-$p$ input, the full derivative has order $p+q$.
- Its components are $\partial Y_{j_1\ldots j_q}/\partial X_{i_1\ldots i_p}$; this lesson places output indices before input indices.
- A delta tensor is the identity map for tensor components and expresses $\partial X/\partial X$.
- Delta factors reveal which input components affect which output components.
- Full tensor derivatives are useful for derivations; scalar-loss gradients are the common object in ML optimization.

## 7. Practice

For each problem, find the requested gradient tensor (or gradient vector). You may use component notation and partial derivatives while deriving it.

1. Let $Y_{ijk}=X_{ijk}^3$. Find $\nabla_XY$. State its order.

2. Let $z_i=\sum_j A_{ij}x_j$. Find $\nabla_Az$. State its order.

3. Let $s=\sum_{ij}X_{ij}^2$. Find $\nabla_Xs$.

4. Let $Y_{ij}=X_{ji}$ (matrix transpose). Find $\nabla_XY$. Which input component changes $Y_{ij}$?

For Questions 5–8, also find the **second-order gradient**, meaning the gradient of the first gradient with respect to the same input. For a tensor-valued output, this is generally a higher-order tensor rather than a matrix Hessian.

5. **Exponential and a transposed sine input.** Let $Y$ have the same shape as the square matrix $X$ and be defined by

   $$Y_{ij}=e^{X_{ij}}\sin(X_{ji}).$$

   a. Find $\nabla_XY$. State its order.

   b. Find $\nabla_X(\nabla_XY)$. State its order.

6. **A scalar logarithmic reduction.** Let

   $$s=\sum_{ij}\ln\bigl(1+X_{ij}^2\bigr).$$

   a. Find $\nabla_Xs$.

   b. Find $\nabla_X(\nabla_Xs)$.

7. **Composition through a matrix product.** Let $A$ have shape `(m, n)` and $B$ have shape `(n, p)`. Define

   $$u_{ij}=\sum_kA_{ik}B_{kj},\qquad y_i=\sum_j\cos(u_{ij}).$$

   a. Find both $\nabla_Ay$ and $\nabla_By$. When differentiating with respect to one input, hold the other input constant. Express your answers in terms of $A$, $B$, and $u$.

   b. Find the same-input second-order gradients $\nabla_A(\nabla_Ay)$ and $\nabla_B(\nabla_By)$, as well as the mixed second-order gradients $\nabla_B(\nabla_Ay)$ and $\nabla_A(\nabla_By)$. Again, hold the other input constant in each calculation.

8. **Composition of tensor functions.** Define two elementwise tensor functions:

   $$U_{ij}=\sin(X_{ij}),\qquad Y_{ij}=\ln\bigl(1+e^{U_{ij}}\bigr).$$

   a. Find $\nabla_XY$. In your derivation, use the intermediate tensor $U$.

   b. Find $\nabla_X(\nabla_XY)$.

9. **Linear regression: SSE.** A data matrix $X$ has components $X_{ij}$, where $i$ indexes $n$ examples and $j$ indexes $d$ features. Let the target be $t_i$, the weights be $w_j$, and

   $$\hat{y}_i=\sum_jX_{ij}w_j,\qquad L(w)=\sum_i(\hat{y}_i-t_i)^2.$$

   a. Find $\nabla_wL$. Write the gradient vector in matrix form, then set it to zero and derive the closed-form minimizing weight vector $w^\star$. State the condition required for your inverse to exist.

   b. Find the Hessian $H=\nabla_w(\nabla_wL)$ and prove that it is positive semidefinite (non-negative definite).

   There is no bias term or regularization in this problem.

10. **Logistic regression: binary cross-entropy.** Use the same feature matrix $X_{ij}$ and weights $w_j$. For binary label $t_i\in\{0,1\}$, define

   $$z_i=\sum_jX_{ij}w_j,\qquad p_i=\sigma(z_i)=\frac{1}{1+e^{-z_i}},$$

   $$L(w)=-\sum_i\left[t_i\log p_i+(1-t_i)\log(1-p_i)\right].$$

   a. Find $\nabla_wL$. Write the gradient vector in matrix form.

   b. Find the Hessian $H=\nabla_w(\nabla_wL)$ and prove that it is positive semidefinite (non-negative definite).

11. **Trace of a matrix product.** Let $A\in\mathbb{R}^{m\times n}$ and $B\in\mathbb{R}^{n\times m}$, and define the scalar

    $$s=\operatorname{trace}(AB).$$

    Find both $\nabla_A s$ and $\nabla_B s$. Derive each answer in component notation, and state the shape of each gradient.

<details>
<summary>Suggested answers</summary>

1. $(\nabla_XY)_{ijkabc}=\frac{\partial Y_{ijk}}{\partial X_{abc}}=3X_{ijk}^2\delta_{ia}\delta_{jb}\delta_{kc}$. The gradient tensor has order $3+3=6$.

2. $(\nabla_Az)_{ikl}=\frac{\partial z_i}{\partial A_{kl}}=\delta_{ik}x_l$. The gradient tensor has order $1+2=3$.

3. $(\nabla_Xs)_{kl}=\frac{\partial s}{\partial X_{kl}}=2X_{kl}$.

4. $(\nabla_XY)_{ijkl}=\frac{\partial Y_{ij}}{\partial X_{kl}}=\delta_{jk}\delta_{il}$. The output entry $Y_{ij}$ is changed only by the input entry $X_{ji}$.

5. **(a)** Each output component depends on both $X_{ij}$ and $X_{ji}$. Apply the product rule:

   $$
   (\nabla_XY)_{ijkl}
   =\frac{\partial Y_{ij}}{\partial X_{kl}}
   =e^{X_{ij}}\sin(X_{ji})\delta_{ik}\delta_{jl}
   +e^{X_{ij}}\cos(X_{ji})\delta_{jk}\delta_{il}.
   $$

   The gradient tensor has order $2+2=4$.

   **(b)** Differentiating the first gradient again gives

   $$
   \begin{aligned}
   \bigl(\nabla_X(\nabla_XY)\bigr)_{ijklmn}
   &=\frac{\partial (\nabla_XY)_{ijkl}}{\partial X_{mn}}\\
   &=e^{X_{ij}}\Big[
      \bigl(\sin(X_{ji})\delta_{im}\delta_{jn}
            +\cos(X_{ji})\delta_{jm}\delta_{in}\bigr)\delta_{ik}\delta_{jl}\\
   &\qquad\quad+
      \bigl(\cos(X_{ji})\delta_{im}\delta_{jn}
            -\sin(X_{ji})\delta_{jm}\delta_{in}\bigr)\delta_{jk}\delta_{il}
      \Big].
   \end{aligned}
   $$

   It has order $2+2+2=6$.

6. **(a)** The output is scalar, so $\nabla_Xs$ has the same order and shape as $X$. Its components are

   $$
   (\nabla_Xs)_{kl}
   =\frac{\partial s}{\partial X_{kl}}
   =\frac{2X_{kl}}{1+X_{kl}^2}.
   $$

   **(b)** The second-order gradient is the matrix-input Hessian:

   $$
   \bigl(\nabla_X(\nabla_Xs)\bigr)_{klmn}
   =\frac{\partial (\nabla_Xs)_{kl}}{\partial X_{mn}}
   =\frac{2(1-X_{kl}^2)}{(1+X_{kl}^2)^2}\delta_{km}\delta_{ln}.
   $$

7. **(a)** When differentiating with respect to $A$, hold $B$ constant. By the chain rule,

   $$
   \begin{aligned}
   (\nabla_Ay)_{ikl}
   &=\frac{\partial y_i}{\partial A_{kl}} \\
   &=-\sum_j\sin(u_{ij})\frac{\partial u_{ij}}{\partial A_{kl}} \\
   &=-\delta_{ik}\sum_j\sin(u_{ij})B_{lj}.
   \end{aligned}
   $$

   When differentiating with respect to $B$, hold $A$ constant:

   $$
   \begin{aligned}
   (\nabla_By)_{ikl}
   &=\frac{\partial y_i}{\partial B_{kl}} \\
   &=-\sum_j\sin(u_{ij})\frac{\partial u_{ij}}{\partial B_{kl}} \\
   &=-A_{ik}\sin(u_{il}).
   \end{aligned}
   $$

   Since the output is order 1 while each input is order 2, both $\nabla_Ay$ and $\nabla_By$ are order-3 tensors.

   **(b)** Differentiating each first gradient with respect to the same matrix gives

   $$
   \bigl(\nabla_A(\nabla_Ay)\bigr)_{iklmn}
   =\frac{\partial (\nabla_Ay)_{ikl}}{\partial A_{mn}}
   =-\delta_{ik}\delta_{im}\sum_j\cos(u_{ij})B_{lj}B_{nj},
   $$

   $$
   \bigl(\nabla_B(\nabla_By)\bigr)_{iklmn}
   =\frac{\partial (\nabla_By)_{ikl}}{\partial B_{mn}}
   =-A_{ik}A_{im}\cos(u_{il})\delta_{ln}.
   $$

   The mixed second-order gradients are

   $$
   \begin{aligned}
   \bigl(\nabla_B(\nabla_Ay)\bigr)_{iklmn}
   &=\frac{\partial (\nabla_Ay)_{ikl}}{\partial B_{mn}}\\
   &=-\delta_{ik}\left[
       A_{im}B_{ln}\cos(u_{in})
       +\delta_{lm}\sin(u_{in})
     \right],
   \end{aligned}
   $$

   $$
   \begin{aligned}
   \bigl(\nabla_A(\nabla_By)\bigr)_{iklmn}
   &=\frac{\partial (\nabla_By)_{ikl}}{\partial A_{mn}}\\
   &=-\delta_{im}\left[
       \delta_{kn}\sin(u_{il})
       +A_{ik}B_{nl}\cos(u_{il})
     \right].
   \end{aligned}
   $$

   These two tensors contain the same mixed partial derivatives, but their final four index positions follow the order in which the gradients were taken.

   Each second-order gradient has order $1+2+2=5$.

8. **(a)** First differentiate each stage:

   $$
   \frac{\partial U_{ij}}{\partial X_{kl}}
   =\cos(X_{ij})\delta_{ik}\delta_{jl},
   $$

   $$
   \frac{\partial Y_{ij}}{\partial U_{kl}}
   =\frac{e^{U_{ij}}}{1+e^{U_{ij}}}\delta_{ik}\delta_{jl}.
   $$

   Contracting the intermediate $U$ indices in the chain rule gives

   $$
   (\nabla_XY)_{ijkl}
   =\frac{e^{U_{ij}}}{1+e^{U_{ij}}}\cos(X_{ij})
   \delta_{ik}\delta_{jl}.
   $$

   Equivalently, substitute $U_{ij}=\sin(X_{ij})$.

   **(b)** Let $q_{ij}=\frac{e^{U_{ij}}}{1+e^{U_{ij}}}$. Differentiating the first gradient gives

   $$
   \bigl(\nabla_X(\nabla_XY)\bigr)_{ijklmn}
   =\left[q_{ij}(1-q_{ij})\cos^2(X_{ij})
           -q_{ij}\sin(X_{ij})\right]
     \delta_{ik}\delta_{jl}\delta_{im}\delta_{jn}.
   $$

   This second-order gradient has order $2+2+2=6$.

9. **(a)** First, $(\nabla_w\hat y)_{ik}=\frac{\partial \hat{y}_i}{\partial w_k}=X_{ik}$. Applying the chain rule gives

   $$
   (\nabla_wL)_k=\frac{\partial L}{\partial w_k}
   =2\sum_i(\hat{y}_i-t_i)X_{ik}.
   $$

   In matrix form, $\nabla_wL=2X^T(Xw-t)$. Setting it to zero yields the normal equations $X^TXw=X^Tt$. If $X$ has full column rank,

   $$\boxed{w^\star=(X^TX)^{-1}X^Tt.}$$

   Otherwise, the minimum-norm solution is $w^\star=X^+t$.

   **(b)**

   $$
   H_{k\ell}=\bigl(\nabla_w(\nabla_wL)\bigr)_{k\ell}
   =2\sum_iX_{ik}X_{i\ell},
   \qquad H=2X^TX.
   $$

   For every $v\in\mathbb{R}^d$,

   $$v^THv=2\lVert Xv\rVert_2^2\ge0,$$

   so $H$ is positive semidefinite (and positive definite when $X$ has full column rank).

10. **(a)** The sigmoid derivative is $\frac{\partial p_i}{\partial z_i}=p_i(1-p_i)$, so

   $$
   (\nabla_wL)_k=\frac{\partial L}{\partial w_k}
   =\sum_i(p_i-t_i)X_{ik}.
   $$

   Thus $\nabla_wL=X^T(p-t)=X^T\bigl(\sigma(Xw)-t\bigr)$.

   **(b)** Let $D=\operatorname{diag}\bigl(p_i(1-p_i)\bigr)$. Then

   $$
   H_{k\ell}=\bigl(\nabla_w(\nabla_wL)\bigr)_{k\ell}
   =\sum_iX_{ik}p_i(1-p_i)X_{i\ell},
   \qquad H=X^TDX.
   $$

   Since $p_i(1-p_i)\ge0$,

   $$v^THv=\sum_i p_i(1-p_i)\bigl((Xv)_i\bigr)^2\ge0,$$

   so the Hessian is positive semidefinite and the binary cross-entropy loss is convex in $w$.

11. Write the trace as a sum over the shared index:

   $$
   s=\operatorname{trace}(AB)
   =\sum_i(AB)_{ii}
   =\sum_{ij}A_{ij}B_{ji}.
   $$

   Holding $B$ constant,

   $$
   (\nabla_A s)_{k\ell}
   =\frac{\partial s}{\partial A_{k\ell}}
   =\sum_{ij}\delta_{ik}\delta_{j\ell}B_{ji}
   =B_{\ell k}.
   $$

   Thus $\boxed{\nabla_A s=B^T}$, which has shape $(m,n)$, the same shape as $A$.

   Holding $A$ constant,

   $$
   (\nabla_B s)_{k\ell}
   =\frac{\partial s}{\partial B_{k\ell}}
   =\sum_{ij}A_{ij}\delta_{jk}\delta_{i\ell}
   =A_{\ell k}.
   $$

   Thus $\boxed{\nabla_B s=A^T}$, which has shape $(n,m)$, the same shape as $B$.

</details>
