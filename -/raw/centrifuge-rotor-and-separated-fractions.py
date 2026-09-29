"""Conceptual rotor geometry and pelleting; no measured particle counts.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes the matching PNG to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle


def tube(ax, x, y, width, height, *, separated=False):
    shell = FancyBboxPatch(
        (x, y), width, height, boxstyle="round,pad=0,rounding_size=0.18",
        facecolor="#eaf4fc", edgecolor="#334155", linewidth=2,
    )
    ax.add_patch(shell)
    if separated:
        pellet = Rectangle((x + width - 0.28, y), 0.28, height,
                           facecolor="#be4933", edgecolor="none")
        pellet.set_clip_path(shell)
        ax.add_patch(pellet)
        points = [(0.45, 0.32), (0.85, 0.62), (1.2, 0.42), (width - 0.14, 0.5)]
        for px, py in points:
            ax.add_patch(Circle((x + px, y + py * height), 0.045, color="#2563a6"))
    else:
        for px, py in [(0.3, 0.3), (0.6, 0.65), (1.05, 0.3), (1.4, 0.65),
                       (1.8, 0.3), (2.1, 0.65)]:
            ax.add_patch(Circle((x + px, y + py * height), 0.09, color="#be4933"))
        for px, py in [(0.45, 0.72), (0.85, 0.3), (1.2, 0.65), (1.9, 0.65)]:
            ax.add_patch(Circle((x + px, y + py * height), 0.045, color="#2563a6"))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=120)
    fig.patch.set_facecolor("white")
    for ax in (left, right):
        ax.set(xlim=(-0.3, 5.8), ylim=(-0.65, 4.4), aspect="equal")
        ax.axis("off")
    left.set_title("A  Rotor geometry during rotation", loc="left", weight="bold")
    left.add_patch(Circle((0.65, 2.35), 0.38, facecolor="#e2e8f0", edgecolor="#334155"))
    left.plot([0.65, 0.65], [0.65, 3.4], linestyle="--", color="#64748b")
    left.text(0.65, 3.6, "rotation axis", ha="center")
    left.plot([1.03, 2.1], [2.35, 2.35], color="#94a3b8", linewidth=9, zorder=0)
    tube(left, 2.1, 1.9, 2.6, 0.9, separated=True)
    left.annotate("", (4.9, 3.2), (2.05, 3.2),
                  arrowprops={"arrowstyle": "->", "color": "#be4933", "lw": 2})
    left.text(3.5, 3.42, "outward centrifugal acceleration", ha="center", fontsize=10)
    for y, endpoint, label in [(1.55, 2.1, r"$r_{\min}$"), (0.8, 4.7, r"$r_{\max}$")]:
        left.annotate("", (endpoint, y), (0.65, y),
                      arrowprops={"arrowstyle": "<->", "color": "#334155"})
        left.text((0.65 + endpoint) / 2, y - 0.3, label, ha="center")
    left.text(2.7, -0.4, "One swung-out tube shown; geometry is schematic", ha="center", fontsize=9)
    right.set_title("B  Pelleting changes the collected fractions", loc="left", weight="bold")
    tube(right, 0.5, 2.8, 2.6, 0.9)
    right.text(3.4, 3.25, "starting\nsuspension", va="center")
    right.annotate("", (1.8, 1.8), (1.8, 2.6), arrowprops={"arrowstyle": "->", "lw": 2})
    tube(right, 0.5, 0.7, 2.6, 0.9, separated=True)
    right.annotate("supernatant\nretains slower particles", (1.35, 1.15), (3.4, 1.8),
                   fontsize=10, arrowprops={"arrowstyle": "->", "color": "#334155"})
    right.annotate("pellet\nmay trap other particles", (2.98, 1.1), (3.4, 0.55),
                   fontsize=10, arrowprops={"arrowstyle": "->", "color": "#334155"})
    right.text(2.6, -0.4, "Colors and particle counts are illustrative, not measured", ha="center", fontsize=9)
    fig.subplots_adjust(left=0.03, right=0.98, bottom=0.05, top=0.9, wspace=0.16)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
