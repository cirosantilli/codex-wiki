"""Draw the active symplectic shear; output the matching PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    identity = np.eye(2, dtype=int)
    zero = np.zeros((2, 2), dtype=int)
    c = np.array([[1, 1], [1, 0]])
    s = np.block([[identity, c], [zero, identity]])
    j = np.block([[zero, identity], [-identity, zero]])
    v, w = np.array([1, 1, 1, 1]), np.array([0, 0, 0, 1])
    assert np.array_equal(s.T @ j @ s, j)
    assert v @ j @ w == (s @ v) @ j @ (s @ w) == 1
    fig, axes = plt.subplots(2, 2, figsize=(10.4, 6.6))
    fig.set_facecolor("white")
    for col, (x, y, names) in enumerate([(v, w, ("$v$", "$w$")),
                                         (s @ v, s @ w, ("$Sv$", "$Sw$"))]):
        areas = []
        for row in range(2):
            ax = axes[row, col]
            a, b = x[[row, row + 2]], y[[row, row + 2]]
            area = int(a[0] * b[1] - a[1] * b[0])
            areas.append(area)
            ax.add_patch(Polygon([np.zeros(2), a, a + b, b],
                                 facecolor="#e7d8eb" if area < 0 else "#d3e9df",
                                 edgecolor="#666666", linewidth=1.2))
            for z, color, name, offset in [(a, "#176397", names[0], (5, 6)),
                                           (b, "#b74a28", names[1], (8, -15))]:
                if np.any(z):
                    ax.annotate("", z, (0, 0), arrowprops={"arrowstyle": "->", "color": color, "lw": 2.3})
                ax.annotate(name + (" = 0" if not np.any(z) else ""), z,
                            xytext=offset, textcoords="offset points", color=color)
            ax.set(xlim=(-.4, 4.55), ylim=(-.3, 2.55), aspect="equal",
                   xlabel=rf"$q_{row + 1}$", ylabel=rf"$p_{row + 1}$",
                   title=f"Pair {row + 1}: signed area {area:+d}")
            ax.set_xticks(range(5)); ax.set_yticks(range(3))
            ax.grid(alpha=.17)
            ax.spines[["top", "right"]].set_visible(False)
        assert areas == ([0, 1] if col == 0 else [-1, 2])
    fig.suptitle(r"Symplectic shear: $(q,p)\mapsto(q+Cp,p)$,  C = [[1, 1], [1, 0]]",
                 fontsize=16, y=.98)
    fig.text(.28, .89, "Before: total pairing 0 + 1 = 1", ha="center", fontsize=13)
    fig.text(.76, .89, "After: total pairing −1 + 2 = 1", ha="center", fontsize=13)
    fig.text(.5, .035, r"$v=(1,1,1,1)^T,\quad w=(0,0,0,1)^T,\quad S^TJS=J$", ha="center", fontsize=13)
    fig.subplots_adjust(left=.08, right=.98, bottom=.14, top=.81, wspace=.25, hspace=.58)
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
