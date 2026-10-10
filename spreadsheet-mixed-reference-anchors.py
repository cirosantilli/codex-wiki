"""Draw an original mixed-reference multiplication table; emit PNG in CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


INK = "#233448"
LEFT = "#206dba"
TOP = "#8a43a2"
TARGET = "#288451"


def main():
    plt.rcParams["text.parse_math"] = False
    fig, ax = plt.subplots(figsize=(10, 6), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 7.2))
    ax.axis("off")
    ax.text(0.25, 6.89, "Mixed references: one anchor for each coordinate",
            fontsize=17, weight="bold", color=INK)
    ax.text(0.25, 6.48, "Fill =$A2*B$1 from B2 across and down through B2:D4", fontsize=12, color=INK)
    x0, top, width, height = 0.55, 5.76, 1.65, 0.95
    for c, letter in enumerate("ABCD"):
        ax.text(x0 + (c + 0.5) * width, top + 0.22, letter, ha="center", fontsize=12, weight="bold", color=INK)
    for r in range(1, 5):
        y = top - r * height
        ax.text(x0 - 0.2, y + height / 2, str(r), ha="center", va="center", fontsize=12, weight="bold", color=INK)
        for c in range(4):
            x = x0 + c * width
            colour, content, textcolour = "white", "", INK
            if r == 1 and c:
                colour, content, textcolour = "#f2e7f8", str(c + 4), TOP
            elif r > 1 and c == 0:
                colour, content, textcolour = "#e7f0fa", str(r), LEFT
            elif r > 1 and c:
                colour = "#e4f3e9"
                content = f"=$A{r}*{'ABCD'[c]}$1\nvalue: {r * (c + 4)}"
            ax.add_patch(Rectangle((x, y), width, height, facecolor=colour,
                                   edgecolor="#b8c3ce", linewidth=0.8))
            ax.text(x + width / 2, y + height / 2, content, ha="center", va="center",
                    fontsize=10.5 if r > 1 and c else 14, color=textcolour,
                    fontfamily="DejaVu Sans Mono" if r > 1 and c else "DejaVu Sans")
    for c, r, colour in [(0, 4, LEFT), (3, 1, TOP), (3, 4, TARGET), (1, 2, TARGET)]:
        ax.add_patch(Rectangle((x0 + c * width, top - r * height), width, height,
                               fill=False, edgecolor=colour, linewidth=2.5))
    bottom = top - 4 * height
    xa, xd = x0 + width / 2, x0 + 3.5 * width
    ax.plot([xd, xd, xa], [bottom - 0.02, bottom - 0.35, bottom - 0.35], color=LEFT, lw=2)
    ax.annotate("", xy=(xa, bottom - 0.02), xytext=(xa, bottom - 0.35),
                arrowprops={"arrowstyle": "->", "color": LEFT, "lw": 2})
    ax.text(3.85, bottom - 0.74, "$A4: stay in column A; follow row 4", ha="center", fontsize=11, color=LEFT)
    right = x0 + 4 * width
    y1, y4 = top - height / 2, top - 3.5 * height
    ax.plot([right + 0.02, right + 0.38, right + 0.38], [y4, y4, y1], color=TOP, lw=2)
    ax.annotate("", xy=(right + 0.02, y1), xytext=(right + 0.38, y1),
                arrowprops={"arrowstyle": "->", "color": TOP, "lw": 2})
    ax.text(8.08, 5.62, "COPY B2 → D4", fontsize=12, color=TARGET, weight="bold")
    ax.text(8.08, 5.14, "+2 columns, +2 rows", fontsize=11, color=INK)
    ax.text(8.08, 4.59, "$A2 → $A4", fontsize=14, color=LEFT, fontfamily="DejaVu Sans Mono")
    ax.text(8.08, 4.24, "Column fixed; row changes", fontsize=10.5, color=LEFT)
    ax.text(8.08, 3.70, "B$1 → D$1", fontsize=14, color=TOP, fontfamily="DejaVu Sans Mono")
    ax.text(8.08, 3.35, "Row fixed; column changes", fontsize=10.5, color=TOP)
    ax.text(8.08, 2.80, "D4: =$A4*D$1", fontsize=13, color=TARGET, fontfamily="DejaVu Sans Mono")
    ax.text(8.08, 2.39, "4 × 7 = 28", fontsize=14, color=TARGET, weight="bold")
    ax.text(0.55, 0.53, "The left boundary supplies each row factor.  The top boundary supplies each column factor.", fontsize=11, color=INK)
    ax.text(0.55, 0.15, "Without anchors, =A2*B1 copied from B2 to D4 becomes =C4*D3, which reads interior results.", fontsize=10.5, color=INK)
    fig.subplots_adjust(left=0.015, right=0.985, top=0.99, bottom=0.025)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
