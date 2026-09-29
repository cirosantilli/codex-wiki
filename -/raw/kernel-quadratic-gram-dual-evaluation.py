"""Draw the exact quadratic Gram matrix and an original dual prediction.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib
python3 ../kernel-quadratic-gram-dual-evaluation.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    points = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
    labels = -points[:, 0] * points[:, 1]
    gram = (points @ points.T) ** 2
    beta = labels / 8
    test_point = np.array([1, 0.5])
    evaluations = (points @ test_point) ** 2
    contributions = beta * evaluations
    np.testing.assert_allclose(np.linalg.eigvalsh(gram), [0, 0, 8, 8], atol=1e-14)
    np.testing.assert_allclose(gram @ beta, labels)
    np.testing.assert_allclose(evaluations, [9 / 4, 1 / 4, 1 / 4, 9 / 4])
    assert contributions.sum() == -0.5

    plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
    fig = plt.figure(figsize=(10.8, 5.4), facecolor="white")
    fig.suptitle("Kernel evaluations replace explicit feature vectors", fontsize=17, y=0.965)
    ax = fig.add_axes([0.075, 0.245, 0.35, 0.62])
    ax.imshow(gram, cmap="Blues", vmin=0, vmax=5, interpolation="nearest")
    for i in range(4):
        for j in range(4):
            ax.text(j, i, str(gram[i, j]), ha="center", va="center", fontsize=18,
                    color="white" if gram[i, j] else "#283b47")
    ticks = [rf"$p_{i}$" for i in range(1, 5)]
    ax.set(xticks=range(4), yticks=range(4), xticklabels=ticks, yticklabels=ticks,
           ylabel="training input", title=r"$K_{ij}=(p_i^T p_j)^2$")
    ax.set_xticks(np.arange(-0.5, 4), minor=True)
    ax.set_yticks(np.arange(-0.5, 4), minor=True)
    ax.grid(which="minor", color="white", linewidth=2)
    ax.tick_params(which="minor", bottom=False, left=False)
    fig.text(0.25, 0.135, "Eigenvalues: 8, 8, 0, 0\nPositive semidefinite; rank 2", ha="center", fontsize=12)

    table_ax = fig.add_axes([0.49, 0.30, 0.48, 0.51])
    table_ax.axis("off")
    table_ax.set_title(r"New input $z=(1,\frac{1}{2})$", fontsize=14, pad=15)
    rows = [[ticks[i], r"$-1/8$" if labels[i] < 0 else r"$+1/8$",
             r"$9/4$" if evaluations[i] > 1 else r"$1/4$",
             r"$-9/32$" if labels[i] < 0 else r"$+1/32$"] for i in range(4)]
    table = table_ax.table(cellText=rows, colLabels=["Input", r"$\beta_i$", r"$k(p_i,z)$", "Contribution"],
                          cellLoc="center", bbox=[0, 0, 1, 1], colWidths=[0.16, 0.22, 0.27, 0.35])
    table.auto_set_font_size(False)
    table.set_fontsize(13)
    for (row, column), cell in table.get_celld().items():
        cell.set_edgecolor("#d8e0e6")
        if row == 0:
            cell.set_facecolor("#edf1f5")
            cell.get_text().set_fontsize(12)
        else:
            cell.set_facecolor("#fff4ef" if labels[row - 1] < 0 else "#eef9fb")
    fig.text(0.73, 0.215, r"$f(z)=\sum_i\beta_i k(p_i,z)=-\frac{1}{2}$", ha="center", fontsize=16)
    fig.text(0.73, 0.135, "Predicted label: −1 (signs agree)", ha="center", fontsize=12, color="#9c3a22")
    fig.text(0.5, 0.035, r"$p_1=(1,1),\ p_2=(1,-1),\ p_3=(-1,1),\ p_4=(-1,-1)$"
             r"     $\beta=y/8,\quad K\beta=y$", ha="center", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=115, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
