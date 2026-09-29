"""Original aggregate carbon/ATP ledger; Python 3.14, matplotlib 3.10.7.

Run from _media; writes glycolysis-carbon-atp-stages.png to the working directory.
The dots count carbon atoms and do not assign carbon positions or isotope labels.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(11, 6.4), dpi=100, facecolor="white")
    ax = fig.add_axes([0.025, 0.06, 0.95, 0.87])
    ax.set(xlim=(0, 11), ylim=(0, 6.4))
    ax.axis("off")
    blue, orange, green = "#256b93", "#a35713", "#23784f"

    def box(x, y, w, h, label, color):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                     boxstyle="round,pad=0.08", linewidth=1.4,
                     edgecolor=color, facecolor="white"))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center")

    def arrow(start, end, color=blue):
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "lw": 1.8, "color": color})

    def carbons(x, y, count):
        ax.scatter([x + i * 0.15 for i in range(count)], [y] * count,
                   s=34, color=blue, zorder=4)

    ax.text(5.5, 6.22, "One glucose: three ledgers, one doubled payoff", ha="center",
            fontsize=17, weight="bold")
    box(0.2, 4.50, 1.6, 0.95, "Glucose\n6 carbons", blue)
    carbons(0.63, 4.66, 6)
    box(2.45, 4.50, 2.0, 0.95, "Investment\n2 ATP → 2 ADP", orange)
    arrow((1.9, 4.98), (2.32, 4.98))
    ax.text(4.92, 5.83, "Split +\nrearrange", ha="center", fontsize=10)
    for y in (5.03, 3.46):
        arrow((4.54, 4.98), (5.42, y + 0.42))
        box(5.52, y, 1.58, 0.90, "G3P\n3 carbons", blue)
        carbons(6.10, y + 0.16, 3)
        arrow((7.21, y + 0.45), (8.90, y + 0.45), green)
        ax.text(8.07, y + 0.96, "+2 ATP", color=green, ha="center", weight="bold")
        ax.text(8.07, y + 0.03, "+1 NADH", color=green, ha="center", fontsize=11)
        box(9.03, y, 1.65, 0.90, "Pyruvate\n3 carbons", blue)
        carbons(9.64, y + 0.16, 3)
    ax.text(1.0, 3.78, "Carbon count", color=blue, ha="center", weight="bold")
    ax.text(1.0, 3.43, "6 = 3 + 3", ha="center", fontsize=16)
    ax.text(3.5, 3.80, "No CO₂ release\nwithin glycolysis", ha="center", fontsize=11)
    ax.text(5.5, 2.76, "ATP inventory change relative to the start", ha="center",
            fontsize=14, weight="bold")
    xs, levels = [1.2, 3.8, 6.4, 9.2], [0, -2, 0, 2]
    ys = [1.28 + 0.40 * v for v in levels]
    ax.plot(xs, ys, color=green, lw=2.3, marker="o", ms=7)
    for x, y, value in zip(xs, ys, levels):
        ax.text(x, y + 0.22, f"{value:+d}" if value else "0", ha="center",
                weight="bold", fontsize=14)
    for x, label in zip(xs, ("Start", "Invest 2", "First payoff pair\nforms 2", "Second payoff pair\nforms 2")):
        ax.text(x, 0.12, label, ha="center", va="bottom", fontsize=11)
    ax.text(5.5, 2.30, "Gross: 4 ATP     −     Investment: 2 ATP     =     Net: 2 ATP",
            ha="center", color=green, fontsize=12)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white",
                transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
