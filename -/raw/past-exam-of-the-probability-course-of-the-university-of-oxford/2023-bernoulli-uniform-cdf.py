"""Generate the Q2(b)(iii) sketch. Tested with Python 3.14.4, matplotlib 3.10.7.

Run: MPLCONFIGDIR=/tmp/oxford-2023-probability-matplotlib python 2023-bernoulli-uniform-cdf.py
The PNG is written to the current directory; the background is opaque white.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    p = 0.4
    color = "#205c9d"
    fig, ax = plt.subplots(figsize=(6.2, 3.6), dpi=140, facecolor="white")
    ax.set_facecolor("white")
    for xs, ys in [([-1.45, -1], [0, 0]), ([-1, 0], [0, p / 2]),
                   ([0, 1], [1 - p / 2, 1]), ([1, 1.45], [1, 1])]:
        ax.plot(xs, ys, color=color, linewidth=2.3)
    ax.plot(0, p / 2, "o", color=color, markerfacecolor="white", markersize=7, zorder=4)
    ax.plot(0, 1 - p / 2, "o", color=color, markersize=7, zorder=4)
    ax.annotate("", xy=(0.15, 1 - p / 2), xytext=(0.15, p / 2),
                arrowprops={"arrowstyle": "<->", "color": "#555555"})
    ax.text(0.22, 0.5, r"jump $1-p$", va="center", fontsize=11)
    ax.set(xlim=(-1.45, 1.45), ylim=(-0.06, 1.08), xlabel=r"$z$",
           ylabel=r"$F_Z(z)$", title=r"Independent $B$ and $U$: $p=0.4$")
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([0, p / 2, 1 - p / 2, 1], ["0", r"$p/2$", r"$1-p/2$", "1"])
    ax.grid(alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    output = Path(Path(__file__).with_suffix(".png").name)
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(output)


if __name__ == "__main__":
    main()
