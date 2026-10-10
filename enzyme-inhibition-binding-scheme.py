"""Draw an original inhibition branching scheme; emit basename.png in cwd.

Tested with Python 3.14, Matplotlib 3.10.7; repository dependencies only.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots(figsize=(9.4, 4.8))
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 10), ylim=(0, 5))
    ax.axis("off")
    blue, orange, gray = "#176b92", "#ae571c", "#4b5964"

    def arrow(start, end, color, reversible=True):
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "<->" if reversible else "->",
                                "lw": 2.2, "color": color,
                                "mutation_scale": 16})

    for x, y, text in [(1.6, 3.5, r"$E+S$"), (5.2, 3.5, r"$ES$"),
                       (8.5, 3.5, r"$E+P$"), (1.6, 1.55, r"$EI+S$"),
                       (5.2, 1.55, r"$ESI$")]:
        ax.text(x, y, text, fontsize=23, ha="center", va="center",
                color=orange if y < 2 else blue)
    arrow((2.45, 3.5), (4.55, 3.5), blue)
    arrow((5.85, 3.5), (7.65, 3.5), blue, False)
    ax.text(6.75, 3.92, r"$k_{\rm cat}$", fontsize=15, ha="center", color=blue)
    arrow((1.6, 3.06), (1.6, 2.0), orange)
    arrow((5.2, 3.06), (5.2, 2.0), orange)
    ax.text(1.94, 2.55, r"$+I$" + "\n" + r"$K_i$", fontsize=15,
            ha="left", va="center", color=orange)
    ax.text(5.55, 2.55, r"$+I$" + "\n" + r"$K_i'$", fontsize=15,
            ha="left", va="center", color=orange)
    ax.text(1.6, 0.95, "Inactive", fontsize=12, ha="center", color=orange)
    ax.text(5.2, 0.95, "Inactive", fontsize=12, ha="center", color=orange)
    ax.text(7.2, 2.25, "Competitive: omit right branch\n\n"
            + r"Pure noncompetitive: $K_i=K_i'$" + "\n\n"
            + r"Unequal mixed: $K_i\ne K_i'$", fontsize=11,
            ha="left", va="center", color=gray)
    ax.text(5, 4.65, "Only ES makes product in this model", fontsize=16,
            ha="center", weight="bold", color=blue)
    ax.text(5, 0.25, "Vertical arrows: reversible inhibitor binding  •  "
            "S remains free on the EI branch", fontsize=11,
            ha="center", color=gray)
    fig.subplots_adjust(left=0.015, right=0.985, top=0.98, bottom=0.02)
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
