import numpy as np

rng = np.random.default_rng(seed=42)

perm = rng.permutation(5)
print(perm)

X = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [9,8,7],
        [6,5,4]
    ]
)

print(X[[True, True, False, False, False]])