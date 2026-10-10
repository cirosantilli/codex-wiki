"""Draw a functional STM loop; Python 3.14, matplotlib 3.10.7.

Run from _media; writes scanning-tunneling-microscope-feedback.png to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Polygon


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(11, 6.5), dpi=120, facecolor="white")
    ax.set(xlim=(0, 12), ylim=(0, 7))
    ax.axis("off")
    blue, orange, green = "#23629a", "#aa4d13", "#28735d"

    def box(x, y, w, h, label, color=blue):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                   facecolor="white", edgecolor=color, linewidth=1.7))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", color=color)

    def arrow(points, color=blue):
        for start, end in zip(points[:-2], points[1:-1]):
            ax.plot([start[0], end[0]], [start[1], end[1]], color=color, lw=1.6)
        ax.annotate("", xy=points[-1], xytext=points[-2],
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 1.6})

    ax.text(6, 6.75, "Scanning tunneling microscopy: current controls tip height",
            ha="center", va="center", fontsize=16, weight="bold")
    # A junction sketch, deliberately schematic rather than an atomic photograph.
    ax.add_patch(Polygon([(1.5, 5.85), (2.5, 5.85), (2, 4.45)],
                         facecolor="#b5c6d4", edgecolor=blue, lw=1.7))
    ax.text(0.7, 5.65, "Metal tip", color=blue)
    ax.plot([1.62, 0.75, 0.75], [5.5, 5.5, 4.73], color=orange, lw=1.4)
    ax.add_patch(Circle((0.75, 4.5), 0.23, facecolor="white", edgecolor=orange, lw=1.4))
    ax.text(0.75, 4.5, "V", ha="center", va="center", color=orange)
    ax.plot([0.75, 0.75], [4.27, 3.6], color=orange, lw=1.4)
    ax.plot([0.6, 3.7], [3.6, 3.6], color="#66513f", lw=3)
    ax.fill_between([0.6, 3.7], 3.2, 3.6, color="#ece2d7")
    ax.text(0.65, 3.36, "Conducting sample", fontsize=11)
    ax.annotate("", xy=(2, 4.38), xytext=(2, 3.67),
                arrowprops={"arrowstyle": "<->", "color": orange, "lw": 1.5})
    ax.text(2.2, 4.02, "Vacuum gap", va="center", color=orange)
    ax.text(0.7, 2.83, "Fixed tip–sample bias V", color=orange)
    ax.plot([0.6, 3.7], [2.45, 2.45], color=green, lw=4)
    ax.text(2.15, 2.1, "Vibration isolation", color=green, ha="center")
    box(4.65, 5.0, 2.6, 0.95, "Measure current I")
    box(8.25, 5.0, 2.9, 0.95, "Compare with target I₀")
    box(8.25, 2.9, 2.9, 1.15, "Feedback controller\nI > I₀: retract\nI < I₀: approach")
    box(4.65, 2.9, 2.6, 1.15, "Vertical piezo drive\nsets z", orange)
    box(0.6, 0.45, 3.1, 0.95, "Lateral piezo drives\nscan x and y", green)
    box(4.65, 0.45, 6.5, 0.95, "Record calibrated z(x, y) → image\nBoth geometry and electronic response contribute")
    arrow([(2, 5.85), (2, 6.15), (4.05, 6.15), (4.05, 5.48), (4.6, 5.48)])
    arrow([(7.33, 5.48), (8.17, 5.48)])
    arrow([(9.7, 4.92), (9.7, 4.13)])
    arrow([(8.17, 3.48), (7.33, 3.48)], orange)
    arrow([(4.57, 3.48), (4.15, 3.48), (4.15, 4.9), (2.42, 4.9)], orange)
    arrow([(5.95, 2.82), (5.95, 1.48)], orange)
    arrow([(2.15, 1.48), (2.15, 1.8), (0.28, 1.8), (0.28, 6.3), (2, 6.3), (2, 5.9)], green)
    ax.text(6, 0.05, "Functional schematic • not to scale • image is a feedback readout, not an atom photograph",
            ha="center", fontsize=10, color="#444444")
    fig.subplots_adjust(left=0.025, right=0.985, bottom=0.04, top=0.98)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
