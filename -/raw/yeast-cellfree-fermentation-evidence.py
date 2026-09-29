"""Original historical evidence schematic; no measured curves or copied artwork.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../yeast-cellfree-fermentation-evidence.py
Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
Sources: Buchner (1897), https://web.lemoyne.edu/~giunta/buchner.html;
Harden, Alcoholic Fermentation (1914), chapter II,
https://www.gutenberg.org/files/44985/44985-h/44985-h.htm.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def box(ax, x, y, w, h, label, color="#eaf2fa", fontsize=11):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01",
                              facecolor=color, edgecolor="#39516b", linewidth=1.2))
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=fontsize,
            color="#172c42", linespacing=1.35)


def arrow(ax, start, end):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "color": "#39516b", "lw": 1.5})


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(10, 6.6), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.6))
    ax.axis("off")
    ax.text(5, 6.27, "Yeast fermentation: remove cells, retain activity", fontsize=17,
            weight="bold", ha="center", color="#172c42")
    ax.text(5, 5.88, "Historical observations — schematic, not quantitative data", ha="center", color="#526477")
    box(ax, 0.2, 4.62, 2.65, 0.95, "Brewers’ yeast\nGrind with sand + diatomite")
    box(ax, 3.63, 4.62, 2.65, 0.95, "Press + clarify\nExtract cell contents")
    box(ax, 7.06, 4.62, 2.65, 0.95, "Press juice\nTest separate preparations")
    arrow(ax, (2.85, 5.1), (3.63, 5.1))
    arrow(ax, (6.28, 5.1), (7.06, 5.1))
    ax.text(0.2, 4.15, "Buchner’s 1897 preliminary report", fontsize=12, weight="bold", color="#172c42")
    rows = [
        (3.20, "Juice + cane sugar", "CO₂ evolution\nStarts after 15–60 min", "Activity survives extraction", "#edf7ee"),
        (2.12, "Cell-retaining filter\nFiltrate + sterile cane sugar", "Fermentation persists\nIcebox: about one day delay", "Intact yeast cells not required", "#edf7ee"),
        (1.04, "Juice + saturated lactose", "No fermentation observed", "Changing substrate changes result", "#fff4df"),
    ]
    for y, preparation, observation, interpretation, color in rows:
        box(ax, 0.2, y, 3.1, 0.85, preparation, fontsize=10.5)
        arrow(ax, (3.3, y + 0.425), (3.67, y + 0.425))
        box(ax, 3.67, y, 3.0, 0.85, observation, color, fontsize=10.5)
        ax.text(6.95, y + 0.425, interpretation, va="center", fontsize=10.5, color="#172c42")
    ax.text(0.2, 0.54, "Later summary (Harden, 1914): heating juice to 50 °C destroyed activity.", fontsize=10.5)
    ax.text(0.2, 0.18, "Cell removal and heat treatment test different requirements; gas alone does not identify ethanol.", fontsize=10,
            color="#526477")
    fig.subplots_adjust(left=0.015, right=0.985, bottom=0.02, top=0.99)
    fig.savefig(Path.cwd() / "yeast-cellfree-fermentation-evidence.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
