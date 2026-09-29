"""Draw the sparse-shift bijection; emit the matching PNG in the CWD."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


BLUE = "#2069a5"
GRAY = "#75818a"
ORANGE = "#b65b18"


def node(ax, x, y, label, in_x, color=BLUE):
    ax.add_patch(Circle((x, y), 0.30, facecolor="#e8f2fa" if in_x else "white",
                        edgecolor=color, linewidth=1.8, zorder=3))
    ax.text(x, y, str(label), fontsize=15, ha="center", va="center", zorder=4)
    ax.text(x, y - 0.48, "$X$" if in_x else "$Y$", ha="center", fontsize=12,
            color=GRAY)


def arrow(ax, x1, x2, y, label, color, dashed=False):
    ax.add_patch(FancyArrowPatch((x1, y), (x2, y), arrowstyle="-|>",
                                mutation_scale=15, shrinkA=24, shrinkB=24,
                                linewidth=1.7 if dashed else 2.5,
                                linestyle="--" if dashed else "-", color=color,
                                zorder=2))
    ax.text((x1 + x2) / 2, y + 0.35, label, ha="center", fontsize=12, color=color)


def main():
    fig, ax = plt.subplots(figsize=(10.4, 5.3), dpi=120, facecolor="white")
    ax.set(xlim=(-0.7, 10.7), ylim=(-0.65, 4.5))
    ax.axis("off")
    fig.suptitle("Repair the missing zero along one chain", fontsize=18, y=0.96)
    ax.text(5, 4.03, r"$f(n)=2n+2,\quad g(m)=m,\quad A=\{0,2,6,14,30,\ldots\}$",
            fontsize=15, ha="center")

    xs = [0.05 + 1.35 * i for i in range(8)]
    values = [0, 2, 2, 6, 6, 14, 14, 30]
    ax.text(-0.45, 3.53, r"On $A$: follow $f$", fontsize=13, color=BLUE)
    for i, (x, n) in enumerate(zip(xs, values)):
        node(ax, x, 2.9, n, i % 2 == 0)
        if i < 7:
            chosen = i % 2 == 0
            arrow(ax, x, xs[i + 1], 2.9, "$h=f$" if chosen else "$g$",
                  BLUE if chosen else GRAY, dashed=not chosen)
    ax.text(10.20, 2.9, r"$\cdots$", fontsize=20, va="center")
    ax.text(5, 1.95, r"$h(0)=2,\quad h(2)=6,\quad h(6)=14,\quad h(14)=30$",
            ha="center", fontsize=14, color=BLUE)
    ax.plot([-0.45, 10.45], [1.65, 1.65], color="#d8dee3", linewidth=1)

    ax.text(-0.45, 1.23, r"Outside $A$: reverse $g$, keeping the number", fontsize=13,
            color=ORANGE)
    for j, n in enumerate([1, 3, 4, 5]):
        x1 = 0.05 + 2.75 * j
        x2 = x1 + 1.35
        node(ax, x1, 0.55, n, True, ORANGE)
        node(ax, x2, 0.55, n, False, ORANGE)
        arrow(ax, x1, x2, 0.55, r"$h=g^{-1}$", ORANGE)
    fig.text(0.5, 0.045, "Chain outputs: A without 0.   Fixed outputs: all positive integers outside A.",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=0.04, right=0.99, top=0.87, bottom=0.10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
