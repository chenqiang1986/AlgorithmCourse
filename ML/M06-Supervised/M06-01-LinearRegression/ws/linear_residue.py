import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot

batch = 1000
m = 20
n = 4
sigma = 3

rng = np.random.default_rng(seed=45)

def generate_data():
    X = rng.normal(loc=5, scale=3, size=[batch, m, n])
    X = np.append(X, np.ones(shape=[batch, m, 1]), axis = 2)

    true_w = np.array([1,2,-1,-2,6])
    y_mean = X @ true_w

    noise = rng.normal(loc=0, scale=sigma, size=[batch, m])
    y = y_mean + noise
    return X, y, true_w

def get_w(X, y):
    model = LinearRegression(fit_intercept=False)  

    w =  np.empty(shape = [0, 5])
    for b in range(X.shape[0]):
        model.fit(X[b], y[b])
        w = np.append(w, model.coef_[None, :], axis=0)

    return w

def get_pred(X, w):
    return np.einsum("bij,bj->bi", X, w)

def main():
    X, y, true_w = generate_data()
    w = get_w(X, y)
    print(w.shape)
    pred_y = get_pred(X, w)
    residue = y - pred_y

    est_std = np.sqrt((residue * residue).sum(axis = 1) / (m-n-1)) 
    est_var = (residue * residue).sum(axis = 1) / (m-n-1)

    count = (est_std < sigma).mean()
    print(count)

    print(est_var.mean())

    pyplot.hist(est_var, bins=50)

    pyplot.show()


if __name__ == "__main__":
    main()