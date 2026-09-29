"""Draw the exact three-product trace; write a matching PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10.8, 6.6), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 10), ylim=(0, 8))
    ax.axis("off")
    ink = "#24364b"

    def box(x, y, w, h, label, color="#edf2f7", size=13):
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                     boxstyle="round,pad=0.09", facecolor=color,
                     edgecolor=ink, linewidth=1.2, zorder=2))
        ax.text(x, y, label, ha="center", va="center", fontsize=size,
                color=ink, linespacing=1.45, zorder=3)

    def arrow(start, end, label=None, label_at=None):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                     mutation_scale=14, color=ink, linewidth=1.35, zorder=1))
        if label:
            ax.text(*label_at, label, ha="center", va="center", fontsize=11,
                    color=ink, bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})

    ax.text(5, 7.65, "Karatsuba: recover both cross terms with one product",
            ha="center", fontsize=17, color=ink, weight="bold")
    ax.text(5, 7.12, r"$x=12\cdot100+34,\quad y=56\cdot100+78,\quad q=100$",
            ha="center", fontsize=15, color=ink)
    ax.text(5, 6.52, "Three product calls (recursion or a small-input base case)",
            ha="center", fontsize=12, color=ink)
    box(1.7, 5.45, 2.35, 1.2, r"$p_2=ac$" + "\n" + r"$12\cdot56=672$", "#dceefa")
    box(5, 5.45, 2.65, 1.2, r"$p_s=(a+b)(c+d)$" + "\n" + r"$46\cdot134=6164$", "#fcebc8")
    box(8.3, 5.45, 2.35, 1.2, r"$p_0=bd$" + "\n" + r"$34\cdot78=2652$", "#ddf2e3")
    box(5, 3.3, 4.25, 1.2,
        "$h=p_s-p_2-p_0=ad+bc$\n$6164-672-2652=2840$")
    arrow((5, 4.76), (5, 4.0))
    arrow((2.65, 4.76), (3.65, 4.0), "$-p_2$", (2.82, 4.30))
    arrow((7.35, 4.76), (6.35, 4.0), "$-p_0$", (7.18, 4.30))
    box(5, 1.2, 7.1, 1.25,
        r"$xy=p_2q^2+hq+p_0$" + "\n" + r"$6\,720\,000+284\,000+2652=7\,006\,652$", size=14)
    arrow((5, 2.6), (5, 1.91), r"$\times q$", (5.6, 2.23))
    arrow((1.7, 4.76), (1.7, 1.91), r"$\times q^2$", (1.13, 3.30))
    arrow((8.3, 4.76), (8.3, 1.91), "$p_0$", (8.85, 3.30))
    ax.text(5, 0.16, "Shift and add exact integer values; normalize carries when storing digits.",
            ha="center", fontsize=12, color=ink)
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.035, top=0.98)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
