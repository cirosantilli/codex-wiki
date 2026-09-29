"""Draw original latency-assay logic with explicitly chosen, nonexperimental rates.

Tested with Python 3.14 and matplotlib 3.10.7. Write PNG to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


INK = "#25384a"
PURPLE = "#8053a0"
ORANGE = "#c48632"


def panel(ax, x, title, disrupted=False):
    ax.text(x, 6.5, title, ha="center", weight="bold", fontsize=13, color=INK)
    if disrupted:
        for lo, hi in ((0.05, 0.22), (0.37, 0.55), (0.73, 0.9)):
            from matplotlib.patches import Arc
            ax.add_patch(Arc((x, 5.3), 1.75, 1.75, theta1=lo * 360,
                             theta2=hi * 360, linewidth=2.5, color=ORANGE))
    else:
        ax.add_patch(Circle((x, 5.3), 0.87, edgecolor=ORANGE,
                            facecolor="#fff6e9", linewidth=2.5))
    ax.plot(x, 5.3, marker="*", color=PURPLE, markersize=18)
    ax.plot(x - 1.1, 5.9, marker="s", color="#2875a8", markersize=9)
    end = (x - 0.15, 5.4) if disrupted else (x - 0.9, 5.7)
    ax.add_patch(FancyArrowPatch((x - 1.05, 5.85), end,
                                arrowstyle="-|>", mutation_scale=13,
                                color="#2875a8", linewidth=1.6))
    if not disrupted:
        ax.plot(x - 0.9, 5.7, marker="x", markersize=10, color="#a23c35", mew=2)
    ax.text(x, 3.95, "Access limited" if not disrupted else "Access exposed",
            ha="center", color=INK, fontsize=12)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(11.6, 7.2), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.035, right=0.97, top=0.86, bottom=0.05)
    ax.set(xlim=(0, 12), ylim=(0, 7))
    ax.axis("off")
    fig.suptitle("Latency tests accessibility, not the number of organelles", y=0.975,
                 fontsize=18, color=INK)
    fig.text(0.5, 0.91, "Same starting material, pH, substrate and assay duration",
             ha="center", fontsize=12, color=INK)
    panel(ax, 1.65, "Preserved membranes")
    panel(ax, 4.95, "Disrupted membranes", disrupted=True)
    ax.text(1.65, 3.4, "F = 10", ha="center", fontsize=17, color=INK)
    ax.text(4.95, 3.4, "T = 100", ha="center", fontsize=17, color=INK)
    ax.text(3.3, 2.85, "Chosen rates: apparent latency = 1 − 10/100 = 0.90",
            ha="center", fontsize=12, color=INK)

    ax.add_patch(FancyBboxPatch((7.05, 2.8), 4.5, 3.9,
                                boxstyle="round,pad=0.12", edgecolor="#aab8c3",
                                facecolor="#f5f8fb"))
    ax.text(9.3, 6.3, "Interpretation controls", ha="center", weight="bold", color=INK)
    ax.text(7.35, 5.7, "Blank: remove unrelated signal\n\nSoluble enzyme ± treatment:\ncheck direct assay effects\n\nTotal activity preserved?\nCheck for enzyme inactivation",
            va="top", fontsize=11.5, color=INK, linespacing=1.35)

    ax.add_patch(FancyBboxPatch((0.35, 0.55), 11.15, 1.5,
                                boxstyle="round,pad=0.12", edgecolor="#aab8c3",
                                facecolor="white"))
    ax.text(0.65, 1.75, "Chosen partial-damage example: F = 25, T = 100 → latency = 0.75",
            va="center", fontsize=12, color=INK)
    ax.text(0.65, 1.13, "More accessible activity; same total. Neither percentage counts intact lysosomes.",
            va="center", fontsize=11.5, color=INK)
    ax.text(6, 0.1, "All rates are invented blank-corrected units. ★ enzyme   ■ added substrate",
            ha="center", fontsize=10.5, color="#53616c")
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
