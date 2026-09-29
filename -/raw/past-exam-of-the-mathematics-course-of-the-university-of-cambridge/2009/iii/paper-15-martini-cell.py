"""Draw the six-bond cell; tested with Python 3.14 / matplotlib 3.10.7.

The output is the script's PNG basename in the caller's working directory.
Matplotlib honors the caller's MPLCONFIGDIR without overriding it.
"""

from pathlib import Path
import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots(figsize=(6.2, 4.8), dpi=100, facecolor="white")
    ax.set_facecolor("white")
    angles = (math.pi / 2, 7 * math.pi / 6, 11 * math.pi / 6)
    inner = [(0.64 * math.cos(a), 0.64 * math.sin(a)) for a in angles]
    outer = [(1.65 * math.cos(a), 1.65 * math.sin(a)) for a in angles]
    for i in range(3):
        j = (i + 1) % 3
        for u, v, color in ((inner[i], inner[j], "#176b9c"),
                            (inner[i], outer[i], "#555555")):
            ax.plot([u[0], v[0]], [u[1], v[1]], color=color, lw=2.5)
            midpoint = ((u[0] + v[0]) / 2, (u[1] + v[1]) / 2)
            ax.text(*midpoint, "$p$", fontsize=15, ha="center", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=1.5))
    for positions, labels, color, offset in (
        (outer, "ABC", "#222222", 0.20),
        (inner, "abc", "#176b9c", 0.13),
    ):
        for (x, y), label, angle in zip(positions, labels, angles):
            ax.plot(x, y, "o", color=color, ms=7)
            ax.text(x + offset * math.cos(angle), y + offset * math.sin(angle),
                    f"${label}$", fontsize=17, ha="center", va="center")
    ax.set_title("Three terminal spokes and one inner triangle", fontsize=15, pad=14)
    ax.text(0, -1.30, "Six independent bonds, each open with probability p",
            ha="center", fontsize=11, color="#333333")
    ax.set_aspect("equal")
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-1.5, 2.0)
    ax.axis("off")
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.05, top=0.88)
    fig.savefig(Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
