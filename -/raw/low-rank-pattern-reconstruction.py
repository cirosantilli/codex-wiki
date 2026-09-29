"""Draw stipulated low-rank patterns; output PNG basename in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
All arrays are constructed examples, not measurements.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    signs = np.array([
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, -1, -1, -1, -1],
        [1, 1, -1, -1, 1, 1, -1, -1],
        [1, -1, 1, -1, 1, -1, 1, -1],
    ], dtype=float)
    weights = np.array([1, 3 / 8, 1 / 8, 1 / 16])
    components = weights[:, None, None] * signs[:, :, None] * signs[:, None, :]
    matrix = components.sum(axis=0)
    rank_one = components[0]
    rank_two = components[:2].sum(axis=0)
    residual = matrix - rank_two
    np.testing.assert_allclose(signs @ signs.T, 8 * np.eye(4))
    np.testing.assert_allclose(np.linalg.svd(matrix, compute_uv=False)[:4], [8, 3, 1, 0.5])
    np.testing.assert_allclose(np.linalg.norm(residual, "fro"), np.sqrt(5) / 2)

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig = plt.figure(figsize=(11.8, 4.8), dpi=110, facecolor="white")
    grid = fig.add_gridspec(
        1, 6, width_ratios=[1, 1, 1, 0.055, 1, 0.055],
        left=0.035, right=0.945, bottom=0.38, top=0.81, wspace=0.32,
    )
    axes = [fig.add_subplot(grid[0, j]) for j in [0, 1, 2, 4]]
    labels = ["Original A (rank 4)", "A₁: uniform (rank 1)", "A₂: blocks (rank 2)", "Residual A − A₂"]
    for i, (ax, array, label) in enumerate(zip(axes, [matrix, rank_one, rank_two, residual], labels)):
        if i < 3:
            im = ax.imshow(array, cmap="gray", vmin=0, vmax=1.6, interpolation="nearest")
        else:
            im = ax.imshow(array, cmap="RdBu_r", vmin=-3 / 16, vmax=3 / 16, interpolation="nearest")
        ax.set_title(label, pad=10)
        ax.set_xticks([0, 3, 7], [1, 4, 8])
        ax.set_yticks([0, 3, 7], [1, 4, 8])
        ax.tick_params(length=0)
        if i == 0:
            ax.set_ylabel("row")
        ax.set_xlabel("column")
        if i == 2:
            cb = fig.colorbar(im, cax=fig.add_subplot(grid[0, 3]), ticks=[0, 0.8, 1.6])
            cb.ax.tick_params(labelsize=9)
        if i == 3:
            cb = fig.colorbar(im, cax=fig.add_subplot(grid[0, 5]), ticks=[-0.1875, 0, 0.1875])
            cb.ax.set_yticklabels(["−3/16", "0", "+3/16"])
            cb.ax.tick_params(labelsize=9)

    fig.suptitle("Four shared patterns → 64 brightness entries", fontsize=17, y=0.975)
    fig.text(0.5, 0.89, "Stipulated singular values: 8, 3, 1, ½  •  Constructed example, not measured data", ha="center", fontsize=11)
    flow = fig.add_axes([0.07, 0.015, 0.86, 0.215], frameon=False)
    flow.set(xlim=(0, 1), ylim=(0, 1))
    flow.axis("off")
    for xpos, label in [(0.11, "8 input\ncoordinates"), (0.5, "r shared\ncoordinates"), (0.89, "8 output\ncoordinates")]:
        flow.text(xpos, 0.64, label, ha="center", va="center", fontsize=12,
                  bbox={"boxstyle": "round,pad=0.45", "facecolor": "#f0f4f8", "edgecolor": "#547087"})
    for left, right, label in [(0.22, 0.395, "Yᵀ"), (0.605, 0.78, "X")]:
        flow.annotate("", xy=(right, 0.64), xytext=(left, 0.64), arrowprops={"arrowstyle": "->", "lw": 1.7})
        flow.text((left + right) / 2, 0.88, label, ha="center", fontsize=13)
    flow.text(0.5, 0.08, "Bz = X(Yᵀz)    •    rank ≤ r    •    store 16r scalars in two factors, rather than 64", ha="center", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
