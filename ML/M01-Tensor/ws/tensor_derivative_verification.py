import numpy as np

# Implementation of a tensor function
# that maps X into output tensor Y
def f(X):
    return np.einsum("i,i->", X, X)

# Hand formula of a tensor to get its gradient
# tensor
def df(X):
    return X * 2

def direction_derivative_numerical(f, X, dX, episilon):
    return (f(X + dX * episilon) - f(X)) / episilon

def direction_derivative_hand(df, X, dX):
    # If you are not familiar with this abastract code,
    # You can simply hard code the contraction index based on the shape of X
    last_n_indices_df = range(-len(dX.shape), 0 , 1)

    return np.tensordot(df(X), dX, axes=[last_n_indices_df, last_n_indices_df])


rng = np.random.default_rng(seed=43)

X = rng.normal(size=[8])
dX = np.array([1,1,1,-1,0,0,1,0])

print(direction_derivative_numerical(f, X, dX, 1e-6))

print(direction_derivative_hand(df, X, dX))