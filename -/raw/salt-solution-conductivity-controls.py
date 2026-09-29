"""Original qualitative conductivity schematic, not experimental data.

Python 3.14 / matplotlib 3.10.7 / numpy 2.3.5. Run from _media; writes
its matching PNG basename to CWD. Ion arrows depict one AC half-cycle.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def main():
    plt.rcParams.update({"font.size": 12})
    fig, ax = plt.subplots(figsize=(11.6, 6.4), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.84, bottom=0.08)
    ax.set(xlim=(0, 12), ylim=(-0.6, 5.5))
    ax.axis("off")
    blue, orange = "#276897", "#b45419"

    for x, title, lit in [(1.6, "Water blank", False),
                          (5.9, "Sucrose solution", False),
                          (10.2, "NaCl solution", True)]:
        ax.text(x, 5.18, title, ha="center", fontsize=15, weight="bold")
        ax.add_patch(Rectangle((x - 0.72, 4.05), 1.05, 0.42, facecolor="white", edgecolor="#333333"))
        ax.text(x - 0.2, 4.26, "AC supply", fontsize=10, ha="center", va="center")
        ax.plot([x - 0.72, x - 0.97, x - 0.97], [4.26, 4.26, 2.15], color="#333333", lw=1.8)
        ax.plot([x + 0.33, x + 0.97], [4.26, 4.26], color="#333333", lw=1.8)
        ax.plot([x + 0.97, x + 0.97], [4.26, 2.15], color="#333333", lw=1.8)
        lamp_x, lamp_y = x + 0.97, 3.72
        ax.add_patch(Circle((lamp_x, lamp_y), 0.22,
                            facecolor="#ffda58" if lit else "white", edgecolor="#333333", lw=1.5, zorder=4))
        ax.plot([lamp_x - 0.12, lamp_x + 0.12], [lamp_y - 0.12, lamp_y + 0.12], color="#333333", zorder=5)
        ax.plot([lamp_x - 0.12, lamp_x + 0.12], [lamp_y + 0.12, lamp_y - 0.12], color="#333333", zorder=5)
        ax.add_patch(Rectangle((x - 1.35, 1.68), 2.7, 1.32, facecolor="#e8f2f7", edgecolor="none"))
        ax.plot([x - 1.35, x - 1.35, x + 1.35, x + 1.35], [3.24, 1.68, 1.68, 3.24], color="#444444", lw=1.5)
        ax.plot([x - 1.35, x + 1.35], [3.0, 3.0], color="#9dc0ce", lw=1)
        for offset in [-0.97, 0.97]:
            ax.add_patch(Rectangle((x + offset - 0.045, 2.15), 0.09, 1.0,
                                  facecolor="#555555", edgecolor="#333333", zorder=3))
        if title == "Sucrose solution":
            for dx, dy in [(-0.45, 2.3), (0.38, 2.65), (0.4, 2.05)]:
                ax.add_patch(Circle((x + dx, dy), 0.13, facecolor="#768961", edgecolor="white"))
            ax.text(x, 1.38, "neutral molecules", ha="center", fontsize=11)
        elif lit:
            for dx, dy, positive in [(-0.35, 2.55, True), (0.37, 2.25, False),
                                     (-0.33, 2.03, False), (0.36, 2.77, True)]:
                ax.add_patch(Circle((x + dx, dy), 0.14, facecolor=blue if positive else orange))
                ax.text(x + dx, dy, "+" if positive else "−", color="white", va="center", ha="center", fontsize=12)
            ax.text(x, 1.38, "mobile ions", ha="center", fontsize=11)
        else:
            ax.text(x, 1.38, "small ionic background", ha="center", fontsize=11)
        ax.text(x, 0.92, "lamp lights" if lit else ("little / no visible light" if title == "Sucrose solution" else "below visible threshold"), ha="center", fontsize=12,
                color="#806000" if lit else "#444444", weight="bold")

    ax.text(0.25, 0.28, "One half-cycle:", weight="bold", fontsize=12, va="center")
    for label, x1, x2, color in [("Na⁺ drift", 3.8, 5.0, blue), ("Cl⁻ drift", 7.9, 6.7, orange)]:
        ax.annotate("", (x2, 0.3), (x1, 0.3), arrowprops={"arrowstyle": "->", "lw": 2, "color": color})
        ax.text((x1 + x2) / 2, -0.08, label, ha="center", color=color, fontsize=11)
    ax.annotate("", (11.55, 0.3), (9.5, 0.3), arrowprops={"arrowstyle": "->", "lw": 2, "color": "#222222"})
    ax.text(10.5, -0.08, "field and conventional current", ha="center", fontsize=11)
    fig.suptitle("Salt-solution conductivity: compare charge carriers", fontsize=18, weight="bold", y=0.965)
    fig.text(0.5, 0.885, "Same probe geometry • rinse between samples • qualitative outcomes, not measured brightness",
             ha="center", fontsize=11, color="#444444")
    fig.text(0.5, 0.025, "Original schematic • water molecules omitted • all drift arrows reverse next half-cycle",
             ha="center", fontsize=11, color="#444444")
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
