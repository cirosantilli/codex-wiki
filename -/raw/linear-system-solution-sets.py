"""Draw the three solution-set examples in linear-algebra.bigb; output to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    unique = np.array([[1, 1], [1, -1]])
    answer = np.linalg.solve(unique, [3, 1])
    assert np.allclose(answer, [2, 1])
    parameters = np.array([0, 1, 3])
    family = np.column_stack((3 - parameters, parameters))
    assert np.allclose(family.sum(axis=1), 3)
    incompatible = np.array([[1, 1, 3], [2, 2, 7]])
    assert np.array_equal(incompatible[1] - 2 * incompatible[0], [0, 0, 1])
    assert np.linalg.matrix_rank(incompatible[:, :2]) == 1
    assert np.linalg.matrix_rank(incompatible) == 2

    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 5.0), facecolor="white")
    fig.subplots_adjust(left=0.055, right=0.985, bottom=0.24, top=0.80, wspace=0.30)
    blue, orange, ink = "#2365a0", "#c05621", "#183a2a"
    samples = np.linspace(-1, 4.5, 300)
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xlim(-1, 4.5)
        ax.set_ylim(-1, 4.5)
        ax.set_xticks(range(-1, 5))
        ax.set_yticks(range(-1, 5))
        ax.grid(color="#e5e5e5", lw=0.6)
        ax.axhline(0, color="#999999", lw=0.9)
        ax.axvline(0, color="#999999", lw=0.9)
        ax.set_axisbelow(True)
        ax.set_xlabel("x", labelpad=1)
        ax.set_ylabel("y", rotation=0, labelpad=8)
        ax.tick_params(labelsize=10)
        for spine in ax.spines.values():
            spine.set_color("#cccccc")

    axes[0].set_title("One solution", pad=12, fontsize=15)
    axes[0].plot(samples, 3 - samples, color=blue, lw=2.4, label=r"$x+y=3$")
    axes[0].plot(samples, samples - 1, color=orange, lw=2.4, label=r"$x-y=1$")
    axes[0].scatter(*answer, color=ink, s=55, zorder=5)
    axes[0].annotate("(2, 1)", answer, xytext=(0.35, 1.15), fontsize=12,
                     arrowprops={"arrowstyle": "-", "color": ink})
    axes[0].legend(loc="upper right", fontsize=10, framealpha=1)

    axes[1].set_title("A line of solutions", pad=12, fontsize=15)
    axes[1].plot(samples, 3 - samples, color=blue, lw=2.4, label=r"$x+y=3$")
    axes[1].scatter(family[:, 0], family[:, 1], color=ink, s=40, zorder=5)
    for xy, offset, label in zip(family, [(8, 10), (8, 10), (8, 10)],
                                  ["t = 0", "t = 1", "t = 3"]):
        axes[1].annotate(label, xy, xytext=offset, textcoords="offset points",
                         color=ink, fontsize=11)
    axes[1].legend(loc="upper right", fontsize=10, framealpha=1)

    axes[2].set_title("No solutions", pad=12, fontsize=15)
    axes[2].plot(samples, 3 - samples, color=blue, lw=2.4, label=r"$x+y=3$")
    axes[2].plot(samples, 3.5 - samples, color=orange, lw=2.4,
                 linestyle="--", label=r"$2x+2y=7$")
    axes[2].legend(loc="upper right", fontsize=10, framealpha=1)

    fig.suptitle("Linear equations: three possible solution sets", y=0.97, fontsize=19)
    for ax, text in zip(axes, ["Both equations hold at (2, 1)",
                               r"$(x,y)=(3-t,t)$ for any real $t$",
                               r"Row subtraction gives $0=1$"]):
        bounds = ax.get_position()
        fig.text((bounds.x0 + bounds.x1) / 2, 0.095, text,
                 ha="center", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Checked: unique (2,1); family t=0,1,3; incompatible row (0,0|1), ranks 1 and 2.")


if __name__ == "__main__":
    main()
