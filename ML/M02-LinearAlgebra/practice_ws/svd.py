import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def compress(A: np.ndarray, k: int):
    # A == U @ diag @ V
    U, sv, V = np.linalg.svd(A, full_matrices=False)

    # The first k singular value
    # reduced_sv = np.append(sv[0:k], [0] * (sv.shape[0] - k))

    # return U @ np.diag(reduced_sv) @ V

    reduced_sv = sv[0:k]
    reduced_U = U[:, 0:k]
    reduced_V = V[0:k, :]
    return reduced_U @ np.diag(reduced_sv) @ reduced_V, reduced_sv.size + reduced_U.size + reduced_V.size


def main():
    rng = np.random.default_rng(seed=34)
       
    A = rng.normal(loc=10, scale=5, size=[100,50])

    A = np.asarray(Image.open("/Users/qiangchen/Desktop/duck.avif").convert('L'))

    U, sv, V = np.linalg.svd(A, full_matrices=False)
    print(sv)

    A_norm = np.linalg.norm(A)
    A_size = A.size
    df = pd.DataFrame({
        "k": [],
        "error": [],
        "size": [],
    })


    fig, ax = plt.subplots(1, 8)
    ax[0].imshow(A, cmap='gray', vmin=0, vmax=255)
    i=1
  

    for k in [1, 5, 10, 25, 40, 100]:
        print("Preserve ", k," singular values")
        reduced_A, reduced_size = compress(A, k)
        print("Compressed: ", reduced_A)
        print("Storage size:", reduced_size, " vs theoretical value: ", k*(A.shape[0] + A.shape[1]+1))
        print("Size pct:", reduced_size / A_size)

        print("Diff Norm: ", np.linalg.norm(A-reduced_A))
        print("Diff Norm Pct: ", np.linalg.norm(A-reduced_A) / A_norm)

        df.loc[len(df)] = {
            "k": k,
            "error": np.linalg.norm(A-reduced_A) / A_norm,
            "size": reduced_size / A_size,
        }

        ax[i].imshow(reduced_A, cmap='gray',vmin=0, vmax=255)
        i+=1

      

    print(df)
    sns.lineplot(data=df, x="k", y="error", ax=ax[7])
    sns.lineplot(data=df, x="k", y="size", ax=ax[7])
    plt.show()


if __name__ == "__main__":
    main()