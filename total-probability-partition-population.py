"""Draw an original constructed finite-population total-probability model.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the opaque PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, ax = plt.subplots(figsize=(10.4, 6.2), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ink, blue, orange = "#193047", "#1976a3", "#d97721"
    ax.text(0.5, 0.965, "One event, two disjoint parts", ha="center",
            va="top", fontsize=21, weight="bold", color=ink)
    ax.text(0.5, 0.887, "Constructed population: 1,000 equally likely items",
            ha="center", color=ink)
    left, bottom, width, height = 0.08, 0.34, 0.84, 0.41
    parts = [(0.6, 0.1, blue, "#e8f2f7", r"$B_1$: 600 items", 60),
             (0.4, 0.25, orange, "#fcf0e6", r"$B_2$: 400 items", 100)]
    x = left
    for weight, rate, color, pale, label, marked in parts:
        w = width * weight
        ax.add_patch(Rectangle((x, bottom), w, height, facecolor=pale,
                               edgecolor="none"))
        ax.add_patch(Rectangle((x, bottom), w, height * rate,
                               facecolor=color, edgecolor="none"))
        ax.text(x + w / 2, 0.793, label, ha="center", color=ink,
                fontsize=15, weight="bold")
        ax.text(x + w / 2, 0.59, f"Group weight = {weight:g}",
                ha="center", color=ink, fontsize=14)
        ax.text(x + w / 2, 0.526, f"Marked within group = {rate:g}",
                ha="center", color=ink)
        ax.annotate(f"{marked} marked items", xy=(x + w / 2, bottom + height * rate / 2),
                    xytext=(x + w / 2, 0.235), ha="center", color=color,
                    fontsize=15, weight="bold",
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 1.7})
        x += w
    ax.add_patch(Rectangle((left, bottom), width, height, fill=False,
                           edgecolor=ink, linewidth=1.5))
    ax.plot([left + 0.6 * width] * 2, [bottom, bottom + height], color=ink, lw=1.5)
    ax.text(0.5, 0.125, r"$P(A)=0.6(0.1)+0.4(0.25)=0.16$",
            ha="center", fontsize=19, color=ink)
    ax.text(0.5, 0.047, "Shaded area = (60 + 100) / 1,000 = 160 / 1,000",
            ha="center", color=ink)
    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.025, top=0.985)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
