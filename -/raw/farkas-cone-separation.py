"""Illustrate Farkas' alternatives; save an opaque PNG to cwd (Python 3.14)."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


def main():
    a = np.eye(2, dtype=int)
    b = np.array([-1, 1])
    certificate = np.array([1, 0])
    projection = np.array([0, 1])
    feasible = np.array([1, 1])
    assert np.all(a.T @ certificate >= 0)
    assert b @ certificate == -1
    assert np.array_equal(a @ feasible, feasible)
    assert np.array_equal(projection - b, certificate)
    assert certificate @ projection == 0
    assert certificate @ b == -np.sum((projection - b) ** 2)

    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig = plt.figure(figsize=(8.8, 5.8), dpi=120, facecolor="white")
    ax = fig.add_axes((0.09, 0.15, 0.54, 0.72), facecolor="white")
    ax.add_patch(Rectangle((0, 0), 2.1, 2.2, color="#dbeaf4", zorder=0))
    ax.axhline(0, color="#a4abb1", lw=1)
    ax.axvline(0, color="#75519b", lw=2.3, linestyle="--")
    for end in a.T:
        ax.annotate("", xy=end, xytext=(0, 0),
                    arrowprops={"arrowstyle": "->", "color": "#22658d", "lw": 2.8})
    ax.text(1.04, -0.22, r"$a_1=y=(1,0)$", fontsize=11, color="#22658d")
    ax.text(0.12, 0.83, r"$a_2=(0,1)$", fontsize=11, color="#22658d")
    ax.text(0.57, 1.88, r"$K=\{Az:z\geq0\}$", color="#22658d")
    ax.scatter(*b, s=95, color="#bc4938", zorder=5)
    ax.text(-1.55, 1.2, r"$b=(-1,1)$", color="#bc4938")
    ax.scatter(*feasible, s=80, color="#22658d", zorder=5)
    ax.text(0.95, 1.16, r"$(1,1)=a_1+a_2$", fontsize=11, color="#22658d")
    ax.plot([b[0], projection[0]], [b[1], projection[1]],
            color="#bc4938", linestyle=":", lw=2)
    ax.scatter(*projection, s=80, marker="s", facecolors="white",
               edgecolors="#75519b", zorder=6)
    ax.annotate(r"$p=(0,1)$", xy=projection, xytext=(-1.4, 1.73),
                arrowprops={"arrowstyle": "->", "color": "#75519b"}, color="#75519b")
    ax.text(-1.52, 0.25, r"$y^Tv<0$", color="#bc4938")
    ax.text(0.46, 0.25, r"$y^Tv\geq0$", color="#22658d")
    ax.set(xlim=(-1.7, 2.1), ylim=(-0.48, 2.2), aspect="equal",
           xlabel=r"First coordinate $v_1$", ylabel=r"Second coordinate $v_2$")
    ax.set_xticks([-1, 0, 1, 2])
    ax.set_yticks([0, 1, 2])
    ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Build a target from columns, or certify that it is outside", y=0.96)
    fig.text(0.68, 0.79, "Nonnegative combinations", weight="bold", fontsize=12)
    fig.text(0.68, 0.71, "$A=I_2$\n$Az=(z_1,z_2)$\n" + r"$z_1,z_2\geq0$", linespacing=1.7, va="top")
    fig.text(0.68, 0.51, "Separating certificate", weight="bold", fontsize=12)
    fig.text(0.68, 0.42, "$y=(1,0)$\n" + r"$A^Ty=(1,0)\geq0$" + "\n$b^Ty=-1<0$", linespacing=1.7, va="top")
    fig.text(0.68, 0.21, "Dashed boundary:\n$y^Tv=0$\n(the vertical axis)",
             color="#75519b", fontsize=11, linespacing=1.5, va="top")
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
