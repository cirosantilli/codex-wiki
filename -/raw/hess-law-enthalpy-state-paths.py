"""Draw original abstract enthalpy states; Python 3.14, matplotlib 3.10.

Run from _media; writes hess-law-enthalpy-state-paths.png to the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, ax = plt.subplots(figsize=(9.6, 5.6), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.12, right=0.97, bottom=0.16, top=0.80)
    fig.suptitle("Hess's law: the endpoints fix the change", fontsize=19, y=0.96)
    fig.text(0.5, 0.865, "Abstract states · same material amount, temperature and pressure",
             ha="center", color="#475569", fontsize=12)
    blue, orange, green = "#2463A6", "#C36B13", "#16805D"
    states = [(1.1, 0, "A", blue), (3.8, 18, "B", orange), (6.5, -7, "C", green)]
    for x, h, label, color in states:
        ax.plot([x - 0.52, x + 0.52], [h, h], color=color, lw=4, solid_capstyle="round")
        ax.text(x, h + 2.3, f"{label}: {h:+d}" if h else "A: 0",
                ha="center", color=color, fontsize=15, weight="bold")
    arrow = {"arrowstyle": "-|>", "lw": 2.5, "mutation_scale": 18}
    ax.annotate("", xy=(3.25, 17.5), xytext=(1.5, 0.7),
                arrowprops={**arrow, "color": blue})
    ax.text(1.25, 11.0, r"$A\to B$" + "\n" + r"$+18\ \mathrm{kJ\,mol^{-1}}$",
            ha="center", color=blue, fontsize=14)
    ax.annotate("", xy=(6.0, -6.4), xytext=(4.3, 17.4),
                arrowprops={**arrow, "color": orange})
    ax.text(6.5, 10.5, r"$B\to C$" + "\n" + r"$-25\ \mathrm{kJ\,mol^{-1}}$",
            ha="center", color=orange, fontsize=14)
    ax.annotate("", xy=(5.9, -7), xytext=(1.7, -0.4),
                arrowprops={**arrow, "color": green})
    ax.text(3.5, -8.8, r"Direct $A\to C$: $-7\ \mathrm{kJ\,mol^{-1}}$",
            ha="center", va="top", color=green, fontsize=14)
    ax.set(xlim=(0, 7.6), ylim=(-13, 24), xticks=[], yticks=[-7, 0, 18],
           ylabel=r"Molar enthalpy $h$ ($\mathrm{kJ\,mol^{-1}}$)")
    ax.spines[["top", "right", "bottom"]].set_visible(False)
    ax.spines["left"].set_color("#94A3B8")
    ax.tick_params(axis="y", colors="#475569")
    fig.text(0.5, 0.065, r"Two steps: $18-25=-7$     |     Closed cycle: $18-25+7=0$",
             ha="center", fontsize=15)
    fig.text(0.5, 0.015, "Chosen values; arrows are state differences, not activation barriers or time traces.",
             ha="center", color="#475569", fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
