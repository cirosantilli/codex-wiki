"""Draw a two-rotation QR example; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def draw_matrix(ax, entries, title, active_rows=(), target=None, zeros=()):
    for row in active_rows:
        ax.add_patch(Rectangle((-0.42, 1.62 - row), 1.84, 0.76,
                               facecolor="#e7effa", edgecolor="none"))
    for row, values in enumerate(entries):
        for col, value in enumerate(values):
            color = "#1c7254" if (row, col) in zeros else "#172b42"
            if (row, col) == target:
                ax.add_patch(Rectangle((col - 0.35, 1.66 - row), 0.7, 0.68,
                                       facecolor="#ffe0ba", edgecolor="#d57d24", lw=1.2))
            ax.text(col, 2 - row, value, ha="center", va="center", fontsize=19, color=color)
    for x, side in [(-0.6, 1), (1.6, -1)]:
        ax.plot([x + 0.15 * side, x, x, x + 0.15 * side],
                [2.48, 2.48, -0.48, -0.48], color="#172b42", lw=1.8)
    ax.set(xlim=(-0.85, 1.85), ylim=(-1.2, 3.4))
    ax.text(0.5, 3.04, title, ha="center", va="center", fontsize=15)
    ax.axis("off")


def main():
    a = np.array([[3., 0.], [4., 5.], [0., 2.]])
    g1 = np.array([[0.6, 0.8, 0.], [-0.8, 0.6, 0.], [0., 0., 1.]])
    t = np.hypot(3., 2.)
    g2 = np.array([[1., 0., 0.], [0., 3/t, 2/t], [0., -2/t, 3/t]])
    assert np.allclose(g1 @ a, [[5., 4.], [0., 3.], [0., 2.]])
    assert np.allclose(g2 @ g1 @ a, [[5., 4.], [0., t], [0., 0.]])
    fig, axes = plt.subplots(1, 3, figsize=(9, 4.3), dpi=120, facecolor="white")
    draw_matrix(axes[0], [["3", "0"], ["4", "5"], ["0", "2"]], r"$A$",
                active_rows=(0, 1), target=(1, 0), zeros=((2, 0),))
    draw_matrix(axes[1], [["5", "4"], ["0", "3"], ["0", "2"]], r"$G_1A$",
                active_rows=(1, 2), target=(2, 1), zeros=((1, 0), (2, 0)))
    draw_matrix(axes[2], [["5", "4"], ["0", r"$\sqrt{13}$"], ["0", "0"]],
                r"$R=G_2G_1A$", zeros=((1, 0), (2, 0), (2, 1)))
    notes = ["Mix rows 1 and 2\nEliminate the 4", "Mix rows 2 and 3\nEliminate the 2",
             "Zeros below the diagonal\nEarlier zeros survive"]
    for ax, note in zip(axes, notes):
        ax.text(0.5, -0.85, note, ha="center", va="center", fontsize=11, linespacing=1.5)
    fig.suptitle("QR by local row rotations", fontsize=16, y=0.98)
    fig.subplots_adjust(top=0.85, bottom=0.2, left=0.02, right=0.98, wspace=0.24)
    for x, label in [(0.337, r"$G_1$"), (0.666, r"$G_2$")]:
        fig.text(x, 0.53, r"$\longrightarrow$", fontsize=22, ha="center")
        fig.text(x, 0.60, label, fontsize=12, ha="center")
    fig.text(0.5, 0.055, "Blue: rows mixed next    Orange: entry eliminated next    Green: zero",
             ha="center", fontsize=10, color="#33465b")
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
