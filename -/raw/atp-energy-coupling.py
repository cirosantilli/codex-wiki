"""Draw cumulative reaction free-energy changes, not activation barriers.

Tested with Python 3.14.4 and the repository's Matplotlib/NumPy environment.
Write an opaque white same-basename PNG to cwd, as required by Makefile.
All contributions use the same stipulated biochemical standard conditions.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    uphill, hydrolysis = 20.0, -30.5
    net = uphill + hydrolysis
    ink, orange, blue = "#24333d", "#ad5516", "#19678d"
    fig, ax = plt.subplots(figsize=(7.6, 5.4))
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    fig.subplots_adjust(left=0.14, right=0.96, top=0.78, bottom=0.30)
    levels = [0.0, uphill, net]
    for x, value, color in zip(range(3), levels, [ink, orange, blue]):
        ax.plot([x - 0.26, x + 0.26], [value, value], color=color,
                linewidth=3.5, solid_capstyle="round")
        ax.text(x, value + 2.0, f"{value:+g}" if value else "0",
                ha="center", va="bottom", fontsize=13, color=color,
                weight="bold")
    for x, start, end, color in [
        (0.55, 0.0, uphill, orange),
        (1.55, uphill, net, blue),
    ]:
        ax.annotate("", xy=(x, end), xytext=(x, start),
                    arrowprops={"arrowstyle": "-|>", "color": color,
                                "lw": 2, "mutation_scale": 15})
    ax.plot([0.26, 0.74], [0, 0], ":", color="#8d989f", lw=1.1)
    ax.plot([1.26, 1.74], [uphill, uphill], ":", color="#8d989f", lw=1.1)
    ax.text(0.61, 10, "+20", color=orange, ha="left", va="center", fontsize=12)
    ax.text(1.61, 5, "−30.5", color=blue, ha="left", va="center", fontsize=12)
    ax.axhline(0, color="#b3bdc3", linewidth=0.7, zorder=0)
    ax.set(xlim=(-0.4, 2.4), ylim=(-16, 27),
           ylabel="Cumulative ΔG°′ (kJ/mol)", yticks=[-10.5, 0, 10, 20],
           xticks=[0, 1, 2],
           xticklabels=["Reference", "Add A → B", "Add ATP hydrolysis"])
    ax.tick_params(axis="both", labelsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.55, 0.94, "Free-energy changes add", ha="center", fontsize=16,
             color=ink, weight="bold")
    fig.text(0.55, 0.875, "Same stipulated conditions: +20 − 30.5 = −10.5 kJ/mol",
             ha="center", fontsize=11.5, color=ink)
    fig.text(0.55, 0.17, "A shared reaction mechanism must couple the transformations",
             ha="center", fontsize=11, color=ink,
             bbox={"facecolor": "#edf5f8", "edgecolor": blue, "pad": 7})
    fig.text(0.55, 0.07, "Bookkeeping steps only: no pathway, intermediates, or barriers shown",
             ha="center", fontsize=9.5, color="#53616a")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Stipulated ΔG°′ contributions: {uphill:+g}, {hydrolysis:+g}; net: {net:+g} kJ/mol")


if __name__ == "__main__":
    main()
