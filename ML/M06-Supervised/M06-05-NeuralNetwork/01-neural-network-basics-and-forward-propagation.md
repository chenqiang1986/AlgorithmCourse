# Lesson 1: Neural-Network Basics and Forward Propagation
*ML / M06 — Supervised Learning*

## The question

Logistic regression turns a weighted sum of features into one prediction. How
can connected computations learn patterns that one straight decision boundary
cannot? A **neural network** stacks linear transformations with nonlinear
activation functions. This lesson follows data through that stack; learning
how to update parameters comes later.

## 1. From one neuron to a network

For input features $\mathbf{x}\in\mathbb{R}^d$, a neuron computes a
pre-activation,

$$
z=\mathbf{w}^T\mathbf{x}+b,
$$

then applies an activation function $g$:

$$
a=g(z).
$$

The weights $\mathbf w$ describe the feature contributions and $b$ is a bias.
Logistic regression is one neuron with a sigmoid activation,

$$
\sigma(z)=\frac{1}{1+e^{-z}}.
$$

For binary classification, sigmoid output can be read as a probability. A
network places many neurons in layers and feeds a layer's output into the next.

    input features       hidden layer              output layer
    x₁ ───────────────►  [ neuron ] ───────────►  prediction
    x₂ ───────────────►  [ neuron ]
    ⋮                    [ neuron ]
    x_d ──────────────►

The input layer only holds feature values; it has no learned weights. Hidden
layers are internal to the model, while the final layer produces its prediction.

## 2. Forward propagation

Suppose layer $\ell$ receives $\mathbf a^{[\ell-1]}$ and contains $n_\ell$
neurons. Its parameters are

$$
W^{[\ell]}\in\mathbb{R}^{n_\ell\times n_{\ell-1}},
\qquad
\mathbf b^{[\ell]}\in\mathbb{R}^{n_\ell}.
$$

Each row of $W^{[\ell]}$ contains the weights of one neuron. The layer
calculation is

$$
\boxed{
\begin{aligned}
\mathbf z^{[\ell]} &= W^{[\ell]}\mathbf a^{[\ell-1]}+\mathbf b^{[\ell]},\\
\mathbf a^{[\ell]} &= g^{[\ell]}\!\left(\mathbf z^{[\ell]}\right).
\end{aligned}}
$$

Begin with $\mathbf a^{[0]}=\mathbf x$. Repeating these two lines from the
first hidden layer through the output layer is **forward propagation** (a
forward pass).

For a network with $d$ inputs, $h$ hidden neurons, and one output,

$$
\begin{aligned}
\mathbf z^{[1]} &= W^{[1]}\mathbf x+\mathbf b^{[1]},
&\mathbf a^{[1]} &= g^{[1]}(\mathbf z^{[1]}),\\
z^{[2]} &= W^{[2]}\mathbf a^{[1]}+b^{[2]},
&\hat y &= g^{[2]}(z^{[2]}).
\end{aligned}
$$

The first-layer weight matrix has shape $(h,d)$, and the output weight matrix
has shape $(1,h)$. A layer with $n_{\ell-1}$ inputs and $n_\ell$ neurons has
$n_\ell(n_{\ell-1}+1)$ trainable parameters.

## 3. Why nonlinear activations are necessary

Without an activation between layers, stacked linear layers remain one linear
layer:

$$
W^{[2]}(W^{[1]}\mathbf x+\mathbf b^{[1]})+\mathbf b^{[2]}
=
\underbrace{W^{[2]}W^{[1]}}_{W'}\mathbf x+
\underbrace{W^{[2]}\mathbf b^{[1]}+\mathbf b^{[2]}}_{\mathbf b'}.
$$

Nonlinear activations prevent this collapse and let networks create curved or
piecewise-linear decision regions.

| Activation | Formula | Typical role |
| --- | --- | --- |
| ReLU | $\max(0,z)$ | Default starting choice for hidden layers. |
| Sigmoid | $1/(1+e^{-z})$ | Binary probability at an output layer. |
| Tanh | $(e^z-e^{-z})/(e^z+e^{-z})$ | Zero-centered hidden activation. |
| Softmax | $e^{z_j}/\sum_k e^{z_k}$ | Multiclass probabilities that sum to one. |

ReLU turns negative inputs into $0$ and leaves positive inputs unchanged. It
is normally used in hidden layers, not as a classifier's final activation.

## 4. Worked forward pass

Consider two features, a two-neuron ReLU hidden layer, and a sigmoid output:

$$
\mathbf x=\begin{bmatrix}2\\1\end{bmatrix},\quad
W^{[1]}=\begin{bmatrix}0.5&-1\\1&0.5\end{bmatrix},\quad
\mathbf b^{[1]}=\begin{bmatrix}0\\-1\end{bmatrix}.
$$

The hidden layer is

$$
\mathbf z^{[1]}=
\begin{bmatrix}0.5&-1\\1&0.5\end{bmatrix}
\begin{bmatrix}2\\1\end{bmatrix}+
\begin{bmatrix}0\\-1\end{bmatrix}
=\begin{bmatrix}0\\1.5\end{bmatrix},
\qquad
\mathbf a^{[1]}=\operatorname{ReLU}(\mathbf z^{[1]})
=\begin{bmatrix}0\\1.5\end{bmatrix}.
$$

With $W^{[2]}=\begin{bmatrix}2&-1\end{bmatrix}$ and $b^{[2]}=0.5$,

$$
z^{[2]}=\begin{bmatrix}2&-1\end{bmatrix}
\begin{bmatrix}0\\1.5\end{bmatrix}+0.5=-1,
\qquad
\hat y=\sigma(-1)\approx0.269.
$$

This network assigns the positive class a probability of about $26.9\%$.
Training will later adjust these parameters to reduce prediction error.

## 5. Forward propagation for a batch

Put $m$ examples into $X\in\mathbb{R}^{m\times d}$, one example per row. In
this row-example convention, the first layer becomes

$$
Z^{[1]}=X(W^{[1]})^T+\mathbf b^{[1]},
\qquad A^{[1]}=g^{[1]}(Z^{[1]}).
$$

| Quantity | Shape for a $d\rightarrow h\rightarrow c$ network |
| --- | --- |
| Input batch $X$ | $(m,d)$ |
| First-layer weights $W^{[1]}$ | $(h,d)$ |
| First-layer output $A^{[1]}$ | $(m,h)$ |
| Output-layer weights $W^{[2]}$ | $(c,h)$ |
| Final output $A^{[2]}$ | $(m,c)$ |

The same weights and biases are used for every row. Biases broadcast across the
batch; a batch does not give each example its own model.

## 6. Match the output to the task

| Task | Output units and final activation | Prediction |
| --- | --- | --- |
| Regression | One unit; usually no activation | A real-valued estimate. |
| Binary classification | One unit; sigmoid | $P(y=1\mid\mathbf x)$. |
| Single-label multiclass classification | One unit per class; softmax | A distribution over classes. |

Many libraries return raw scores, called **logits**, then combine sigmoid or
softmax with a numerically stable loss function. The conceptual forward pass
is unchanged.

## 7. A small NumPy forward pass

    import numpy as np

    def relu(z):
        return np.maximum(0, z)

    def sigmoid(z):
        return 1 / (1 + np.exp(-z))

    X = np.array([[2.0, 1.0], [0.0, 3.0]])  # shape: (2, 2)
    W1 = np.array([[0.5, -1.0], [1.0, 0.5]])
    b1 = np.array([0.0, -1.0])
    W2 = np.array([[2.0, -1.0]])
    b2 = np.array([0.5])

    Z1 = X @ W1.T + b1
    A1 = relu(Z1)
    Z2 = A1 @ W2.T + b2
    probability = sigmoid(Z2)

    print(probability.shape)  # (2, 1)

Keeping $Z1$, $A1$, and $Z2$ makes the computation inspectable now and will be
essential when learning backpropagation.

## 8. Class practice

A network accepts four input features and has a hidden layer with six neurons,
followed by a three-class softmax output layer.

1. What are the shapes of $W^{[1]}$, $\mathbf b^{[1]}$, $W^{[2]}$, and
   $\mathbf b^{[2]}$?
2. How many trainable parameters are in the network?
3. For a batch of 32 examples, what is the final-output shape?

<details>
<summary>Solution</summary>

1. The shapes are $(6,4)$, $(6,)$, $(3,6)$, and $(3,)$.
2. The hidden layer has $6(4+1)=30$ parameters; the output layer has
   $3(6+1)=21$, for $51$ total.
3. The final output has shape $(32,3)$: one score/probability vector per
   example.

</details>

## Key takeaways

- A neuron computes a weighted sum plus bias, then an activation.
- Forward propagation repeats linear transformation then activation from input
  to output.
- Nonlinear hidden activations are necessary; otherwise all layers collapse
  into one linear transformation.
- Matrix shapes encode the architecture and make batch computation efficient.
- The final activation depends on whether the task is regression, binary
  classification, or multiclass classification.

Next, we will measure prediction error with a loss function and use
backpropagation to determine which parameters should change.

