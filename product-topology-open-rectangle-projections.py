"""Draw coordinate strips and their open-rectangle intersection (Python 3.14)."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.6), facecolor="white")
    blue, orange, purple = "#2878a3", "#c36d24", "#7556a6"
    for ax in axes:
        ax.set(xlim=(-0.35, 3.3), ylim=(-0.35, 4.7), aspect="equal")
        ax.spines[["top", "right"]].set_visible(False)
        ax.spines["bottom"].set_position("zero")
        ax.spines["left"].set_position("zero")
        ax.set_xticks([1, 2, 3])
        ax.set_yticks([1, 2, 3, 4])
        ax.set_xlabel(r"$x_1$", loc="right")
        ax.set_ylabel(r"$x_2$", loc="top", rotation=0)
    a, b, c = axes
    a.add_patch(Rectangle((1, -0.35), 1, 5.05, color=blue, alpha=0.16))
    for x in (1, 2):
        a.axvline(x, color=blue, ls="--", lw=1.5)
    for start, end in ((4.1, 4.65), (0.2, -0.32)):
        a.annotate("", (1.5, end), (1.5, start),
                   arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
    a.set_title(r"$\pi_1^{-1}((1,2))=(1,2)\times\mathbb{R}$", pad=17)
    b.add_patch(Rectangle((-0.35, 2), 3.65, 2, color=orange, alpha=0.16))
    for y in (2, 4):
        b.axhline(y, color=orange, ls="--", lw=1.5)
    for start, end in ((2.6, 3.25), (0.35, -0.3)):
        b.annotate("", (end, 3), (start, 3),
                   arrowprops={"arrowstyle": "->", "color": orange, "lw": 2})
    b.set_title(r"$\pi_2^{-1}((2,4))=\mathbb{R}\times(2,4)$", pad=17)
    c.add_patch(Rectangle((1, 2), 1, 2, facecolor=purple,
                         alpha=0.17, edgecolor=purple, ls="--", lw=2))
    # A separate border keeps the excluded boundary readable.
    c.add_patch(Rectangle((1, 2), 1, 2, fill=False,
                         edgecolor=purple, ls="--", lw=1.5))
    c.scatter([1.4], [3], color=purple, s=42, zorder=5)
    c.text(1.5, 3.12, "(1.4, 3)", color=purple, fontsize=10)
    c.annotate("", (1.4, 0), (1.4, 2.93),
               arrowprops={"arrowstyle": "->", "color": blue, "ls": ":"})
    c.annotate("", (0, 3), (1.34, 3),
               arrowprops={"arrowstyle": "->", "color": orange, "ls": ":"})
    c.plot([1, 2], [0, 0], color=blue, lw=4)
    c.plot([0, 0], [2, 4], color=orange, lw=4)
    c.scatter([1, 2], [0, 0], facecolor="white", edgecolor=blue, zorder=6)
    c.scatter([0, 0], [2, 4], facecolor="white", edgecolor=orange, zorder=6)
    c.set_title(r"Both tests: $(1,2)\times(2,4)$", pad=17)
    fig.suptitle("Two coordinate observations select an open rectangle", y=0.97)
    fig.text(0.5, 0.04, "Dashed boundaries are excluded; strip arrows indicate unbounded continuation.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.06, right=0.98, top=0.80, bottom=0.18, wspace=0.30)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
