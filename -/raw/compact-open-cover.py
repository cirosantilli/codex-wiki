"""Draw compact-open-cover.png in cwd.

Tested with Python 3.14.4, Matplotlib 3.10.7, and NumPy 2.3.5.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def interval(ax, left, right, row, color, closed=False):
    ax.plot([left, right], [row, row], color=color, lw=7,
            solid_capstyle="butt", zorder=2)
    ax.scatter([left, right], [row, row], s=72, edgecolors=color,
               facecolors=color if closed else "white", linewidths=2, zorder=3)


def main():
    covers = np.array([[-0.1, 0.45], [0.35, 0.8], [0.7, 1.1]])
    grid = np.linspace(0, 1, 10001)
    membership = (grid[:, None] > covers[:, 0]) & (grid[:, None] < covers[:, 1])
    assert np.all(membership.any(axis=1))
    assert np.allclose(covers[:-1, 1] - covers[1:, 0], [0.1, 0.1])
    witnesses = np.array([0, 0.5, 1])
    for index, witness in enumerate(witnesses):
        remaining = np.delete(covers, index, axis=0)
        assert not np.any((witness > remaining[:, 0]) & (witness < remaining[:, 1]))
    largest_index = 10
    missed = 1 / (largest_index + 1)
    assert 0 < missed < 1 / largest_index

    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    fig, axes = plt.subplots(2, 1, figsize=(10, 8), facecolor="white")
    colors = ["#247393", "#7251a0", "#c47426"]
    top, bottom = axes
    interval(top, 0, 1, 3, "#263b46", closed=True)
    for index, ((left, right), color) in enumerate(zip(covers, colors)):
        interval(top, left, right, 2 - index, color)
    top.set(yticks=[3, 2, 1, 0],
            yticklabels=["Covered set [0, 1]", "(−0.1, 0.45)", "(0.35, 0.8)", "(0.7, 1.1)"],
            ylim=(-0.65, 3.8))
    top.set_title("Three open intervals cover every point of [0, 1]", pad=16)
    top.text(0.5, 3.53, "Solid endpoints included; hollow endpoints excluded",
             ha="center", fontsize=11, color="#47545d")

    bottom.axvspan(0, 0.1, color="#b74440", alpha=0.12, zorder=0)
    for row, index in zip([4, 3, 2, 1], [2, 3, 5, 10]):
        interval(bottom, 1 / index, 1, row, "#247393")
    bottom.scatter([missed], [0.15], color="#b74440", s=55, zorder=4)
    bottom.annotate(r"Missed point $1/11$: still in $(0,1)$",
                    xy=(missed, 0.15), xytext=(0.32, 0.15),
                    arrowprops={"arrowstyle": "->", "color": "#b74440"},
                    color="#983b37", va="center", fontsize=12)
    bottom.set(yticks=[4, 3, 2, 1],
               yticklabels=[r"$U_2=(1/2,1)$", r"$U_3=(1/3,1)$",
                            r"$U_5=(1/5,1)$", r"$U_{10}=(1/10,1)$"],
               ylim=(-0.45, 4.7))
    bottom.set_title(r"Infinite cover $U_n=(1/n,1)$: every finite selection misses points", pad=17)
    bottom.set_xlabel("Position on the real line", labelpad=9)
    for ax in axes:
        ax.set_facecolor("white")
        ax.set(xlim=(-0.15, 1.15), xticks=[0, 0.25, 0.5, 0.75, 1])
        ax.tick_params(axis="y", length=0, pad=12)
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.spines["bottom"].set_color("#a7b1b7")
        ax.grid(axis="x", color="#dde2e5", lw=0.7, zorder=0)
    fig.subplots_adjust(left=0.24, right=0.975, bottom=0.11, top=0.92, hspace=0.47)
    fig.text(0.60, 0.025, "For any finite selection with largest index N, the union is (1/N, 1).",
             ha="center", fontsize=11)
    fig.savefig("compact-open-cover.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
