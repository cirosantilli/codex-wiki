"""Show a computed rank-one approximation; write an opaque PNG to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    row = np.array([1, 2, 3, 4, 4, 3, 2, 1], dtype=float)
    column = np.array([1, 2, 3, 4, 5, 5, 4, 3, 2, 1], dtype=float)
    a = (-1.) ** np.arange(8)
    b = (-1.) ** np.arange(10)
    approximation = np.outer(row, column)
    residual = np.outer(a, b) / 2
    matrix = approximation + residual
    assert row @ a == column @ b == 0
    assert row @ row == 60 and column @ column == 110
    left, singular, right_t = np.linalg.svd(matrix, full_matrices=False)
    assert np.allclose(singular[:2], np.sqrt([6600, 20]))
    assert np.allclose(singular[2:], 0, atol=1e-12)
    assert np.allclose(singular[0] * np.outer(left[:, 0], right_t[0]), approximation)
    error = np.linalg.norm(residual, "fro")
    relative = error / np.linalg.norm(matrix, "fro")
    assert np.isclose(error, np.sqrt(20))
    assert np.isclose(relative, np.sqrt(20 / 6620))
    assert np.isclose(np.linalg.norm(residual, 2), np.sqrt(20))
    assert np.allclose(matrix[0, :2], [1.5, 1.5])

    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.8))
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.31, top=0.76, wspace=0.20)
    titles = [r"Original $B$: 80 scalars", r"Rank one $B_1$: 19 scalars",
              r"Discarded $B-B_1$"]
    for ax, data, title in zip(axes, [matrix, approximation, residual], titles):
        ax.set_facecolor("white")
        if ax is axes[2]:
            residual_image = ax.imshow(data, cmap="RdBu_r", vmin=-0.5, vmax=0.5,
                                       interpolation="nearest")
        else:
            brightness_image = ax.imshow(data, cmap="gray", vmin=0, vmax=21,
                                         interpolation="nearest")
        ax.set_title(title, fontsize=13, pad=10)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticks(np.arange(-0.5, 10, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, 8, 1), minor=True)
        ax.grid(which="minor", color="#aaaaaa", lw=0.3, alpha=0.35)
        ax.tick_params(which="minor", length=0)
    brightness_bar = fig.add_axes([0.095, 0.245, 0.475, 0.025])
    fig.colorbar(brightness_image, cax=brightness_bar, orientation="horizontal", ticks=[0, 7, 14, 21])
    brightness_bar.set_xlabel("Same brightness scale for both images", fontsize=10)
    residual_bar = fig.add_axes([0.738, 0.245, 0.18, 0.025])
    fig.colorbar(residual_image, cax=residual_bar, orientation="horizontal", ticks=[-0.5, 0, 0.5])
    residual_bar.set_xlabel("Error scale: magnified contrast", fontsize=10)
    fig.suptitle("Keep the broad patch; discard the small checkerboard", fontsize=17, y=0.97)
    fig.text(0.5, 0.855, r"$B=pq^T+\frac{1}{2}ab^T$     $\sigma_1=\sqrt{6600}\approx81.24$     $\sigma_2=\sqrt{20}\approx4.47$",
             ha="center", fontsize=13)
    fig.text(0.5, 0.11, r"Frobenius error: $\sqrt{20}$     Relative error: $\sqrt{20/6620}=5.50\%$",
             ha="center", fontsize=13)
    fig.text(0.5, 0.035, "All 80 entries change by ±0.5. Scalar counts assume equal precision and exclude overhead.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Checked: singular values {singular[:2]}; rank-one SVD equals pqᵀ; Frobenius/operator error {error:.9f}; relative error {100*relative:.9f}%; scalar count 80 → 19.")


if __name__ == "__main__":
    main()
