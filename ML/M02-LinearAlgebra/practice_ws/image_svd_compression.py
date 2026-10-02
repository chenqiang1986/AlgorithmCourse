"""Show low-rank SVD approximations of a grayscale image.

Example:
    python3 practice_ws/image_svd_compression.py path/to/photo.jpg --ranks 1 5 20 50
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def rank_k_approximation(
    u: np.ndarray, singular_values: np.ndarray, vt: np.ndarray, k: int
) -> np.ndarray:
    """Return the rank-k reconstruction from a compact SVD."""
    return (u[:, :k] * singular_values[:k]) @ vt[:k, :]


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compress a grayscale image using truncated SVD."
    )
    parser.add_argument("image", type=Path, help="Path to an image file.")
    parser.add_argument(
        "--ranks",
        type=int,
        nargs="+",
        default=[1, 5, 20, 50, 100],
        help="Ranks k to display (default: 1 5 20 50 100).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    if not args.image.is_file():
        raise FileNotFoundError(f"Image not found: {args.image}")

    # convert("L") gives one intensity value per pixel: a two-dimensional matrix.
    image = Image.open(args.image).convert("L")
    matrix = np.asarray(image, dtype=float)
    u, singular_values, vt = np.linalg.svd(matrix, full_matrices=False)

    max_rank = len(singular_values)
    ranks = [k for k in args.ranks if 1 <= k <= max_rank]
    if not ranks:
        raise ValueError(f"Choose at least one rank from 1 through {max_rank}.")

    total_energy = np.sum(singular_values**2)
    fig, axes = plt.subplots(1, len(ranks) + 1, figsize=(4 * (len(ranks) + 1), 4))
    axes[0].imshow(matrix, cmap="gray", vmin=0, vmax=255)
    axes[0].set_title("original")
    axes[0].axis("off")

    for axis, k in zip(axes[1:], ranks):
        approximation = rank_k_approximation(u, singular_values, vt, k)
        relative_error = np.linalg.norm(matrix - approximation, "fro") / np.linalg.norm(
            matrix, "fro"
        )
        energy_retained = np.sum(singular_values[:k] ** 2) / total_energy
        stored_values = k * (matrix.shape[0] + matrix.shape[1] + 1)
        original_values = matrix.size

        print(
            f"k={k:4d} | relative Frobenius error={relative_error:.4f} | "
            f"energy retained={energy_retained:.2%} | "
            f"storage={stored_values / original_values:.2%} of original"
        )
        axis.imshow(np.clip(approximation, 0, 255), cmap="gray", vmin=0, vmax=255)
        axis.set_title(f"rank {k}\n{energy_retained:.1%} energy")
        axis.axis("off")

    fig.suptitle("Grayscale image compression with truncated SVD")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
