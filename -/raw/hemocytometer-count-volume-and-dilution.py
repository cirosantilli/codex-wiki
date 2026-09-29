"""Original counting-volume example; Python 3.14, matplotlib 3.10.7.

Run from _media to write hemocytometer-count-volume-and-dilution.png.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    fig, ax = plt.subplots(figsize=(10, 5.8), dpi=110, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 5.8))
    ax.axis("off")
    ink, blue, orange = "#203047", "#27649a", "#a74e16"
    ax.text(5, 5.43, "Count a known volume, then undo dilution", ha="center",
            fontsize=17, weight="bold", color=ink)
    ax.text(5, 5.05, "Constructed counts · standard 0.1 mm chamber depth",
            ha="center", fontsize=11, color=ink)
    counts = [(36, 4), (44, 6), (40, 5), (40, 5)]
    for i, (live, stained) in enumerate(counts):
        x, y = 0.55 + 1.5 * (i % 2), 2.63 - 1.35 * (i // 2)
        ax.add_patch(Rectangle((x, y), 1.5, 1.35, facecolor="#f4f7fb",
                               edgecolor=ink, linewidth=1.3))
        ax.text(x + 0.75, y + 0.82, f"{live} excluding", ha="center",
                fontsize=11, color=blue, weight="bold")
        ax.text(x + 0.75, y + 0.4, f"{stained} stained", ha="center",
                fontsize=11, color=orange)
    ax.annotate("1 mm", xy=(0.55, 4.16), xytext=(2.05, 4.16),
                arrowprops=dict(arrowstyle="|-|", color=ink), ha="center",
                va="center", fontsize=10, color=ink)
    ax.text(2.05, 0.97, r"Each square: $1\,\mathrm{mm}^2\times0.1\,\mathrm{mm}$",
            ha="center", fontsize=11, color=ink)
    ax.text(2.05, 0.62, r"Sample volume = $10^{-4}$ mL", ha="center",
            fontsize=12, color=ink)
    ax.text(4.2, 4.24, "Equal volumes of preparation and stain → D = 2",
            fontsize=11, color=ink)
    rows = [(3.69, "Mean per square", "40 excluding; 45 total", ink),
            (2.95, "Undo the 1:1 stain dilution", "800,000 excluding cells/mL", blue),
            (2.2, "Same correction for the total", "900,000 total cells/mL", ink),
            (1.45, "Fraction stays unchanged", "160 / 180 = 8 / 9 ≈ 88.9%", orange),
            (0.7, "In a well-mixed 3 mL preparation", "2,400,000 excluding cells", blue)]
    for y, label, value, color in rows:
        ax.text(4.35, y, label, fontsize=10, color=ink)
        ax.text(4.35, y - 0.32, value, fontsize=13, weight="bold", color=color)
    fig.subplots_adjust(left=0.015, right=0.985, top=0.985, bottom=0.015)
    fig.savefig(Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
