"""Compare unit and zero level sets of three real symmetric bilinear forms.

Save quadratic-form-level-sets.png to CWD on an opaque white background.
Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def main():
    blue, orange = "#235f9b", "#bb4e1d"
    t = np.linspace(0, 2 * np.pi, 401)
    y = np.linspace(-2, 2, 401)
    positive = np.column_stack((np.cos(t), np.sin(t)))
    indefinite = np.column_stack((np.sqrt(1 + y**2), y))
    assert np.allclose(np.sum(positive**2, axis=1), 1)
    assert np.allclose(indefinite[:, 0] ** 2 - indefinite[:, 1] ** 2, 1)
    assert np.allclose(y**2 - y**2, 0)
    matrices = (np.diag([1, 1]), np.diag([1, -1]), np.diag([1, 0]))
    assert [round(np.linalg.det(a)) for a in matrices] == [1, -1, 0]
    null = np.array([1, 1])
    assert null @ matrices[1] @ null == 0
    assert np.any(matrices[1] @ null != 0)
    assert np.array_equal(matrices[2] @ np.array([0, 1]), np.zeros(2))

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(10, 5.5), facecolor="white")
    fig.subplots_adjust(left=0.055, right=0.98, top=0.77, bottom=0.22, wspace=0.3)
    fig.suptitle("Zero self-pairing and degeneracy are different", fontsize=17, y=0.97)
    headings = ["Positive definite", "Indefinite, nondegenerate", "Degenerate"]
    formulas = [r"$q=x^2+y^2$", r"$q=x^2-y^2$", r"$q=x^2$"]
    for ax, heading, formula in zip(axes, headings, formulas):
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_xticks([-2, -1, 0, 1, 2])
        ax.set_yticks([-2, -1, 0, 1, 2])
        ax.grid(color="#e9e9e9", lw=0.6)
        ax.axhline(0, color="#999999", lw=0.8)
        ax.axvline(0, color="#999999", lw=0.8)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_xlabel("x", labelpad=1)
        ax.set_ylabel("y", labelpad=1)
        ax.set_title(heading + "\n" + formula, fontsize=12, pad=13)

    axes[0].plot(*positive.T, color=blue, lw=2.5)
    axes[0].plot(0, 0, "o", color=orange, ms=7, zorder=5)
    axes[0].annotate("Only the origin\nhas q = 0", (0, 0), (0.55, 1.3), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": orange})
    for sign in [-1, 1]:
        axes[1].plot(sign * indefinite[:, 0], y, color=blue, lw=2.5)
        axes[1].plot(y, sign * y, color=orange, lw=2, ls="--")
    axes[1].plot(1, 1, "o", mfc="white", mec=orange, ms=7, mew=2, zorder=5)
    axes[1].annotate("(1, 1): q = 0", (1, 1), (-1.8, 1.65), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": orange})
    for sign in [-1, 1]:
        axes[2].plot(np.full_like(y, sign), y, color=blue, lw=2.5)
    axes[2].plot(np.zeros_like(y), y, color=orange, lw=2, ls="--")
    axes[2].plot(0, 1, "o", mfc="white", mec=orange, ms=7, mew=2, zorder=5)
    axes[2].annotate("Radical:\nx = 0", (0, 1), (0.35, 1.45), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": orange})
    captions = [r"$\det A=1$; radical $=\{0\}$",
                r"$\det A=-1$; radical $=\{0\}$",
                r"$\det A=0$; radical $=\mathrm{span}\{(0,1)\}$"]
    for ax, caption in zip(axes, captions):
        ax.text(0.5, -0.27, caption, transform=ax.transAxes, ha="center", fontsize=10)
    handles = [Line2D([], [], color=blue, lw=2.5, label="q = 1"),
               Line2D([], [], color=orange, lw=2, ls="--", marker="o", markersize=5, label="q = 0")]
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.02), ncol=2,
               frameon=False, fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
