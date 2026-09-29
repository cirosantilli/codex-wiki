"""Draw an original XOR square and its quadratic feature slice.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib
python3 ../kernel-quadratic-xor-feature-separation.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch


def main():
    points = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
    labels = -points[:, 0] * points[:, 1]
    features = np.column_stack(
        [points[:, 0] ** 2, np.sqrt(2) * points[:, 0] * points[:, 1], points[:, 1] ** 2]
    )
    assert np.array_equal(labels, [-1, 1, 1, -1])
    assert np.all(features[:, 2] == 1)
    np.testing.assert_allclose(-features[:, 1] / np.sqrt(2), labels)

    positive, negative = "#147d92", "#be4b27"
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.8, 5.3), facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.23, top=0.83, wspace=0.33)
    fig.suptitle("A product feature separates the XOR square", fontsize=17, y=0.96)

    grid = np.linspace(-1.6, 1.6, 241)
    xx, yy = np.meshgrid(grid, grid)
    left.contourf(xx, yy, -xx * yy, levels=[-3, 0, 3], colors=[negative, positive], alpha=0.09)
    left.plot([-1, 1], [-1, 1], "--", color=negative, alpha=0.55, linewidth=1.6)
    left.plot([-1, 1], [1, -1], "--", color=positive, alpha=0.55, linewidth=1.6)
    left.axhline(0, color="#59636c", linewidth=1)
    left.axvline(0, color="#59636c", linewidth=1)
    left.scatter([0], [0], color="#222222", s=20, zorder=4)
    left.annotate("shared midpoint", (0, 0), xytext=(0.15, 0.32), fontsize=10,
                  arrowprops={"arrowstyle": "->", "color": "#555555"})
    for index, (point, label) in enumerate(zip(points, labels), 1):
        color, marker = (positive, "o") if label == 1 else (negative, "s")
        left.scatter(*point, c=color, marker=marker, s=105, edgecolors="white", linewidths=1.1, zorder=5)
        left.annotate(rf"$p_{index}$: {label:+d}", point, xytext=(0, 14 if point[1] > 0 else -25),
                      textcoords="offset points", ha="center", color=color, fontsize=11)
    left.set(title="Input plane: no affine separator", xlabel=r"$x_1$", ylabel=r"$x_2$",
             xlim=(-1.6, 1.6), ylim=(-1.6, 1.6), xticks=[-1, 0, 1], yticks=[-1, 0, 1])
    left.set_aspect("equal")

    right.axhspan(0, 2.05, color=negative, alpha=0.09)
    right.axhspan(-2.05, 0, color=positive, alpha=0.09)
    right.axhline(0, color="#333333", linewidth=1.8)
    right.text(0.37, 0.12, r"separator: $\phi_2=0$", fontsize=11)
    for indices, color, marker, vertical in [([0, 3], negative, "s", np.sqrt(2)),
                                              ([1, 2], positive, "o", -np.sqrt(2))]:
        right.scatter(1, vertical, c=color, marker=marker, s=120, edgecolors="white", linewidths=1.1, zorder=5)
        names = ", ".join(rf"$p_{i+1}$" for i in indices)
        right.annotate(names + " coincide\n" + rf"$y={labels[indices[0]]:+d}$", (1, vertical),
                       xytext=(15, 0), textcoords="offset points", va="center", fontsize=11, color=color)
    right.set(title=r"Feature slice: $\phi_3=x_2^2=1$", xlabel=r"$\phi_1=x_1^2$",
              ylabel=r"$\phi_2=\sqrt{2}\,x_1x_2$", xlim=(0.25, 1.9), ylim=(-2.05, 2.05),
              xticks=[1], yticks=[-np.sqrt(2), 0, np.sqrt(2)],
              yticklabels=[r"$-\sqrt{2}$", "0", r"$\sqrt{2}$"])
    right.set_box_aspect(1)
    fig.legend(handles=[Patch(color=positive, label="+1: signs differ"),
                        Patch(color=negative, label="−1: signs agree")],
               loc="lower center", bbox_to_anchor=(0.5, 0.105), ncol=2, frameon=False)
    fig.text(0.5, 0.055, r"$\phi(x)=(x_1^2,\sqrt{2}\,x_1x_2,x_2^2)$     "
             r"$f(x)=-\phi_2/\sqrt{2}=-x_1x_2$", ha="center", fontsize=13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=115, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
