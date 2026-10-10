"""Compare products in the triangle symmetry group; output PNG to CWD.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def compose(p, q):
    """Apply q first, then p, to vertices indexed from zero."""
    return tuple(p[q[i]] for i in range(3))


def draw_triangle(ax, permutation, title):
    vertices = np.array([[0, 1], [-np.sqrt(3) / 2, -0.5],
                         [np.sqrt(3) / 2, -0.5]])
    ax.plot(*vertices[[0, 1, 2, 0]].T, color="#536375", lw=2)
    colors = ["#b43e39", "#1769a5", "#318445"]
    for original, destination in enumerate(permutation):
        x, y = vertices[destination]
        ax.scatter(x, y, s=620, color=colors[original], zorder=3)
        ax.text(x, y, str(original + 1), ha="center", va="center",
                color="white", fontsize=17, weight="bold")
    ax.set(xlim=(-1.2, 1.2), ylim=(-0.82, 1.3), aspect="equal")
    ax.set_title(title, fontsize=15, pad=4)
    ax.axis("off")


def main():
    e, r, s = (0, 1, 2), (1, 2, 0), (1, 0, 2)
    r2 = compose(r, r)
    assert compose(r, r2) == compose(r2, r) == e
    assert compose(r, s) == (2, 1, 0)
    assert compose(s, r) == (0, 2, 1)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(11, 7.2), facecolor="white")
    fig.suptitle("Triangle symmetries: does operation order matter?", fontsize=19, y=.97)
    fig.text(.5, .905, r"$r=(123)$: rotate counterclockwise 120°     $s=(12)$: reflect, fixing position 3",
             ha="center", fontsize=12)
    panels = [(.055, .53, compose(r, r2), r"$rr^2=e$"),
              (.335, .53, compose(r2, r), r"$r^2r=e$"),
              (.055, .13, compose(r, s), r"$rs=(13)$"),
              (.335, .13, compose(s, r), r"$sr=(23)$")]
    for x, y, permutation, title in panels:
        ax = fig.add_axes([x, y, .245, .275])
        draw_triangle(ax, permutation, title)
    fig.text(.32, .855, "Rotations commute: identical final labels", ha="center", color="#318445")
    fig.text(.32, .455, "Rotation and reflection: different final labels", ha="center", color="#b43e39")
    fig.text(.72, .79, r"$H=\langle r\rangle=\{e,r,r^2\}$", fontsize=15)
    table_ax = fig.add_axes([.64, .34, .335, .39])
    table_ax.axis("off")
    rows = [["e", "yes", "yes"], ["(123)", "yes", "yes"],
            ["(132)", "yes", "yes"], ["(12)", "no", "yes"],
            ["(23)", "no", "yes"], ["(13)", "no", "yes"]]
    table = table_ax.table(cellText=rows,
                          colLabels=["g", r"$g\in C_{S_3}(H)$", r"$g\in N_{S_3}(H)$"],
                          loc="center", cellLoc="center", colWidths=[.24, .38, .38])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 1.8)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#c2cbd4")
        cell.set_facecolor("#edf3f8" if row == 0 else "white")
    fig.text(.805, .265, r"$srs^{-1}=r^{-1}\ne r$", ha="center", fontsize=16)
    fig.text(.805, .205, "Reflection preserves H as a set,\nbut exchanges its two rotations.",
             ha="center", fontsize=12, linespacing=1.6)
    fig.text(.5, .045, "Colored labels track original vertices; the rightmost operation acts first.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
