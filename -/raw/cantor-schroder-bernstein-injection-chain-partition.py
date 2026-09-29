"""Draw the two rules in the injection-chain proof; emit the PNG in the CWD."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


BLUE = "#2069a5"
ORANGE = "#b65b18"
GRAY = "#75818a"


def node(ax, x, y, label, in_x, color):
    ax.add_patch(Circle((x, y), 0.29, facecolor="#edf3f7" if in_x else "white",
                        edgecolor=color, linewidth=1.8, zorder=3))
    ax.text(x, y, label, fontsize=15, ha="center", va="center", zorder=4)
    ax.text(x, y - 0.46, "$X$" if in_x else "$Y$", color=GRAY,
            ha="center", fontsize=12)


def arrow(ax, a, b, label, color, dashed=False, curved=False):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=15,
                                shrinkA=23, shrinkB=23, linewidth=2.4 if not dashed else 1.5,
                                color=color, linestyle="--" if dashed else "-",
                                connectionstyle="arc3,rad=0.42" if curved else "arc3",
                                zorder=2))
    ax.text((a[0] + b[0]) / 2, a[1] + (0.56 if curved else 0.33), label,
            color=color, ha="center", fontsize=12)


def main():
    fig, ax = plt.subplots(figsize=(10.4, 6.1), dpi=120, facecolor="white")
    ax.set(xlim=(-0.7, 9.6), ylim=(-1.15, 5.4))
    ax.axis("off")
    fig.suptitle("Two matching rules, disjoint output sets", fontsize=18, y=0.96)
    xs = [0.15 + 1.55 * i for i in range(6)]
    ax.text(-0.4, 4.76, r"Starts in $A_0=X\setminus g(Y)$: use $h=f$", fontsize=14,
            color=BLUE)
    for i, x in enumerate(xs):
        k = i // 2
        node(ax, x, 4.0, f"$a_{k}$" if i % 2 == 0 else f"$b_{k}$", i % 2 == 0, BLUE)
        if i % 2 == 0:
            ax.text(x, 3.15, f"$A_{k}$", ha="center", color=BLUE, fontsize=12)
        if i < 5:
            chosen = i % 2 == 0
            arrow(ax, (x, 4.0), (xs[i + 1], 4.0), "$h=f$" if chosen else "$g$",
                  BLUE if chosen else GRAY, dashed=not chosen)
    arrow(ax, (xs[-1], 4.0), (9.27, 4.0), "$g$", GRAY, dashed=True)
    ax.text(9.28, 4.0, r"$\cdots$", fontsize=20, va="center")

    ax.text(-0.4, 2.65, r"Starts in $Y$: use $h=g^{-1}$", fontsize=14, color=ORANGE)
    for i, x in enumerate(xs):
        k = i // 2
        node(ax, x, 1.55, f"$y_{k}$" if i % 2 == 0 else f"$x_{k}$", i % 2 == 1,
             ORANGE)
        if i < 5:
            arrow(ax, (x, 1.55), (xs[i + 1], 1.55), "$g$" if i % 2 == 0 else "$f$",
                  GRAY, dashed=True)
        if i % 2 == 0:
            arrow(ax, (xs[i + 1], 1.55), (x, 1.55), r"$h=g^{-1}$", ORANGE, curved=True)
    arrow(ax, (xs[-1], 1.55), (9.27, 1.55), "$f$", GRAY, dashed=True)
    ax.text(9.28, 1.55, r"$\cdots$", fontsize=20, va="center")
    ax.text(4.5, 0.56, "Chains with no start and closed loops also use the second rule.",
            ha="center", fontsize=12, color=GRAY)
    ax.plot([-0.4, 9.3], [0.2, 0.2], color="#d8dee3", linewidth=1)
    ax.text(1.6, -0.40, r"$A\ \longrightarrow\ f(A)$", ha="center", fontsize=17,
            color=BLUE)
    ax.text(1.6, -0.84, r"via $f$", ha="center", fontsize=12, color=BLUE)
    ax.text(6.25, -0.40, r"$X\setminus A\ \longrightarrow\ Y\setminus f(A)$",
            ha="center", fontsize=17, color=ORANGE)
    ax.text(6.25, -0.84, r"via $g^{-1}$", ha="center", fontsize=12, color=ORANGE)
    fig.text(0.5, 0.035, "Solid colored arrows define h; dashed arrows show the original injections.",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=0.04, right=0.98, top=0.87, bottom=0.09)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
