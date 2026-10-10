"""Show redundancy and a complete family of representations; PNG goes to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run: make _media/linear-dependence-redundancy.png
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, start, end, color, width=2.8, style="-"):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", color=color, lw=width,
                                linestyle=style, shrinkA=0, shrinkB=0,
                                mutation_scale=16), zorder=4)


def main():
    v1, v2, v3 = np.array([1., 1.]), np.array([1., -1.]), np.array([2., 0.])
    basis = np.column_stack((v1, v2))
    generators = np.column_stack((v1, v2, v3))
    target = np.array([3., 1.])
    relation = np.array([-1., -1., 1.])
    assert np.allclose(v1 + v2, v3)
    assert np.allclose(generators @ relation, [0, 0])
    assert np.linalg.matrix_rank(basis) == 2
    assert np.linalg.matrix_rank(generators) == 2
    assert np.allclose(np.linalg.solve(basis, target), [2, 1])
    t = np.linspace(-2, 3, 201)
    family = np.vstack((2-t, 1-t, t))
    assert np.allclose(generators @ family, target[:, None])
    # Both coordinate equations force this family when c3 is selected freely.
    assert np.allclose(family[0] + family[2], 2)
    assert np.allclose(family[1] + family[2], 1)
    assert np.allclose(generators @ [2, 1, 0], target)
    assert np.allclose(generators @ [1, 0, 1], target)
    assert np.allclose(generators @ [0, -1, 2], target)
    assert np.allclose(1j * 1 + (-1) * 1j, 0)
    assert np.linalg.matrix_rank([[1, 0], [0, 1]]) == 2

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 5.5), facecolor="white")
    fig.subplots_adjust(left=.055, right=.98, bottom=.28, top=.75, wspace=.35)
    blue, orange, purple, green = "#2466a3", "#c15a16", "#8753a1", "#217346"
    for ax in axes[:2]:
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xlim(-.4, 4.)
        ax.set_ylim(-1.5, 2.6)
        ax.set_xticks([0, 1, 2, 3])
        ax.set_yticks([-1, 0, 1, 2])
        ax.grid(color="#eeeeee", lw=.8)
        ax.axhline(0, color="#999999", lw=.8)
        ax.axvline(0, color="#999999", lw=.8)
        arrow(ax, [0, 0], target, green, width=2)
        ax.plot(*target, "o", color=green, ms=5, zorder=5)
        ax.text(2.75, 1.24, r"$w=(3,1)$", color=green)
        ax.set_xlabel("x")
        ax.set_ylabel("y", rotation=0, labelpad=4)
    left, middle, right = axes
    left.set_title("Independent pair", fontsize=13, pad=12)
    arrow(left, [0, 0], 2*v1, blue)
    arrow(left, 2*v1, target, orange)
    arrow(left, [0, 0], v2, orange, width=1.8, style="--")
    left.text(.18, 1.25, r"$2v_1$", color=blue)
    left.text(2.6, 1.85, r"$+v_2$", color=orange)
    left.text(.8, -1.3, r"$v_2$", color=orange)
    middle.set_title("Add a redundant arrow", fontsize=13, pad=12)
    arrow(middle, [0, 0], v1, blue)
    arrow(middle, v1, target, purple)
    arrow(middle, [0, 0], v3, purple, style="--", width=1.8)
    middle.text(.1, .85, r"$v_1$", color=blue)
    middle.text(1.8, 1.20, r"$+v_3$", color=purple)
    middle.text(1.15, -.38, r"$v_3=(2,0)$", color=purple)
    middle.text(.25, -1.15, r"$v_3=v_1+v_2$", color=purple)

    right.set_facecolor("white")
    right.set_title("A family of coefficients", fontsize=13, pad=12)
    right.set_xlim(-.6, 2.6)
    right.set_ylim(-1.9, 2.9)
    right.set_xlabel(r"$t=c_3$")
    right.set_ylabel("coefficient")
    right.set_xticks([0, 1, 2])
    right.set_yticks([-1, 0, 1, 2])
    right.grid(color="#eeeeee", lw=.8)
    for row, color, label in zip(family, [blue, orange, purple],
                                  [r"$c_1=2-t$", r"$c_2=1-t$", r"$c_3=t$"]):
        right.plot(t, row, color=color, lw=2, label=label)
    for sample in [0, 1, 2]:
        for value, color in zip([2-sample, 1-sample, sample], [blue, orange, purple]):
            right.plot(sample, value, "o", color=color, ms=5)
    right.legend(loc="upper center", bbox_to_anchor=(.5, -.27),
                 ncol=1, frameon=False, fontsize=10)
    fig.suptitle("Redundancy changes the coefficients, not the target", fontsize=17, y=.97)
    fig.text(.5, .87, r"$v_1=(1,1),\quad v_2=(1,-1),\quad v_3=(2,0)$",
             ha="center", fontsize=13)
    for ax, line in zip(axes[:2], [r"Unique: $(c_1,c_2)=(2,1)$",
                                  r"Also: $(c_1,c_2,c_3)=(1,0,1)$"]):
        box = ax.get_position()
        fig.text((box.x0 + box.x1)/2, .145, line, ha="center", fontsize=11)
    fig.text(.34, .045, r"$(2,1,0),\ (1,0,1),\ (0,-1,2)$ all give $(3,1)$",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                dpi=140, facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified relation, ranks, 201 representations, and real/complex example.")


if __name__ == "__main__":
    main()
