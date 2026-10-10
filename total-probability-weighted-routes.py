"""Draw the weighted routes of an original two-component mixture.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the opaque PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, ax = plt.subplots(figsize=(10.8, 6.6), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ink, blue, orange, gray = "#193047", "#1976a3", "#d97721", "#687887"
    ax.text(0.5, 0.98, "Multiply within a route; add routes to A", ha="center",
            va="top", fontsize=21, weight="bold", color=ink)
    ax.text(0.5, 0.901, "Constructed model: group weights 0.6 and 0.4",
            ha="center", color=ink)
    ax.text(0.32, 0.826, "Choose group", ha="center", color=ink)
    ax.text(0.575, 0.826, "Conditional result", ha="center", color=ink)
    ax.text(0.88, 0.826, "Joint probability", ha="center", color=ink)
    root = (0.055, 0.47)
    groups = [(0.31, 0.65), (0.31, 0.29)]
    ends = [(0.65, 0.74), (0.65, 0.56), (0.65, 0.38), (0.65, 0.20)]

    def edge(a, b, label, color, offset=0):
        ax.annotate("", xy=b, xytext=a,
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 2.2,
                                "shrinkA": 10, "shrinkB": 15})
        ax.text((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + offset, label,
                ha="center", va="center", color=color, fontsize=14,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})

    edge(root, groups[0], "0.6", blue, 0.018)
    edge(root, groups[1], "0.4", orange, -0.018)
    edge(groups[0], ends[0], "0.1", blue, 0.022)
    edge(groups[0], ends[1], "0.9", gray, -0.022)
    edge(groups[1], ends[2], "0.25", orange, 0.022)
    edge(groups[1], ends[3], "0.75", gray, -0.022)
    ax.text(*root, "Start", ha="center", va="center", color=ink,
            bbox={"facecolor": "white", "edgecolor": ink, "boxstyle": "round,pad=0.4"})
    for loc, label, color in zip(groups, [r"$B_1$", r"$B_2$"], [blue, orange]):
        ax.text(*loc, label, ha="center", va="center", color=color, fontsize=17,
                bbox={"facecolor": "white", "edgecolor": color, "boxstyle": "round,pad=0.35"})
    labels = [r"$A$", r"$A^c$", r"$A$", r"$A^c$"]
    products = ["0.6 × 0.1 = 0.06", "0.6 × 0.9 = 0.54",
                "0.4 × 0.25 = 0.10", "0.4 × 0.75 = 0.30"]
    for loc, label, product, color in zip(ends, labels, products, [blue, gray, orange, gray]):
        ax.text(*loc, label, ha="center", va="center", color=color, fontsize=17,
                bbox={"facecolor": "white", "edgecolor": color, "boxstyle": "round,pad=0.3"})
        ax.text(0.79, loc[1], product, ha="left", va="center", color=color,
                fontsize=13, weight="bold" if label == r"$A$" else "normal")
    ax.text(0.5, 0.108, r"$P(A)=0.06+0.10=0.16$", ha="center", color=ink,
            fontsize=20, bbox={"facecolor": "#f0f6f9", "edgecolor": "none", "pad": 9})
    ax.text(0.5, 0.022, "All four routes: 0.06 + 0.54 + 0.10 + 0.30 = 1",
            ha="center", color=ink)
    fig.subplots_adjust(left=0.02, right=0.93, bottom=0.025, top=0.985)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
