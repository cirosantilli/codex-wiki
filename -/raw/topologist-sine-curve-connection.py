"""Write topologist-sine-curve-connection.png to the current directory.

Tested with Python 3.14.4, Matplotlib 3.10.7, and NumPy 2.3.5.
Run from _media to generate the repository image. The phase 1/x is sampled
uniformly, resolving every visible oscillation; 0 < x < 0.005 is omitted.
The finite drawing is illustrative and is not a proof of a topological property.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def main():
    xmin = 0.005
    # At least 100 samples per sine period, including the true right endpoint.
    phase = np.linspace(1, 1 / xmin, int(np.ceil((1 / xmin - 1) * 100 / (2 * np.pi))) + 1)
    x, y = 1 / phase, np.sin(phase)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.4), facecolor="white")
    blue, orange = "#246a93", "#a9571c"
    for ax in axes:
        ax.set_facecolor("white")
        ax.axvspan(0, xmin, facecolor="#ececec", hatch="///", edgecolor="#bbbbbb", linewidth=0)
        ax.plot(x, y, color=blue, lw=1.4, label=r"$G$: sampled graph")
        # Draw L separately: never join it to a sampled graph point.
        ax.plot([0, 0], [-1, 1], color=orange, lw=4, label=r"$L$: vertical segment")
        ax.scatter([0, 0], [-1, 1], color=orange, s=35, zorder=4)
        ax.set(ylim=(-1.3, 1.3), yticks=[-1, 0, 1], xlabel=r"$x$", ylabel=r"$y$")
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set(xlim=(-0.045, 1.06), xticks=[0, 0.25, 0.5, 0.75, 1])
    axes[0].set_title("One connected component; two path components", pad=14)
    axes[0].scatter([1], [np.sin(1)], color=blue, s=45, zorder=4)
    axes[0].annotate(r"Included: $(1,\sin 1)$", xy=(1, np.sin(1)), xytext=(0.47, 1.12),
                     fontsize=11, arrowprops={"arrowstyle": "->", "color": "#555555"})
    axes[0].legend(loc="lower right", fontsize=10, framealpha=1)

    axes[1].set(xlim=(-0.006, 0.145), xticks=[0, 0.04, 0.08, 0.12])
    axes[1].set_title("Zoom: oscillations persist towards x = 0", pad=14)
    p, q = 2 / (5 * np.pi), 2 / (7 * np.pi)
    axes[1].scatter([p, q], [1, -1], color=blue, s=40, zorder=4)
    axes[1].annotate(r"$(2/(5\pi),1)$", xy=(p, 1), xytext=(0.067, 1.16),
                     fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"})
    axes[1].annotate(r"$(2/(7\pi),-1)$", xy=(q, -1), xytext=(0.025, -1.22),
                     fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"})
    fig.text(0.5, 0.065, r"Hatched strip: $0<x<0.005$ omitted in both panels; infinitely many oscillations continue there.",
             ha="center", fontsize=11, color="#454545")
    fig.text(0.5, 0.025, "The drawing illustrates the formulas. Connectedness and absence of a crossing path require the arguments in the text.",
             ha="center", fontsize=10, color="#454545")
    fig.subplots_adjust(left=0.065, right=0.98, top=0.88, bottom=0.19, wspace=0.25)
    fig.savefig("topologist-sine-curve-connection.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
