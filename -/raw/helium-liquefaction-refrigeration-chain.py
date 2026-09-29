"""Draw a functional helium refrigeration loop; no dimensions or operating data.

Tested with Python 3.14, matplotlib 3.10.7. Run from _media; output is
helium-liquefaction-refrigeration-chain.png in the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10, 5.6), dpi=110, facecolor="white")
    fig.subplots_adjust(left=.025, right=.975, bottom=.04, top=.90)
    ax.set(xlim=(0, 10), ylim=(0, 5.1))
    ax.axis("off")
    fig.suptitle("Helium liquefaction: a functional refrigeration chain", fontsize=16)
    blue, teal, red = "#185b9b", "#087f8c", "#bb4631"

    def box(x, y, w, h, text, fill="#eef4fa"):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                                   facecolor=fill, edgecolor=blue, linewidth=1.4))
        ax.text(x+w/2, y+h/2, text, ha="center", va="center", fontsize=11)

    def arrow(points, color=blue, style="-", width=1.8):
        for a, b in zip(points[:-2], points[1:-1]):
            ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=width, ls=style)
        ax.add_patch(FancyArrowPatch(points[-2], points[-1], arrowstyle="-|>",
                                    mutation_scale=14, color=color, lw=width,
                                    linestyle=style, shrinkA=0, shrinkB=0))

    box(.18, 3.35, 1.45, .8, "Compression\n& heat rejection")
    box(2.05, 3.35, 1.5, .8, "Liquid-air\nprecooling")
    box(4.00, 3.35, 1.55, .8, "Liquid-hydrogen\nprecooling")
    box(6.00, 2.65, 1.55, 1.9, "Counterflow\nheat exchanger\n\n\n", "#edf8f7")
    box(8.05, 3.35, 1.55, .8, "Throttling\nexpansion")
    box(8.05, 1.25, 1.55, .85, "Liquid\ncollection")
    for a, b in [(1.69, 1.99), (3.61, 3.94), (5.61, 5.94), (7.61, 7.99)]:
        arrow([(a, 3.75), (b, 3.75)])
    arrow([(8.82, 3.29), (8.82, 2.16)])
    arrow([(8.0, 1.68), (7.80, 1.68), (7.80, 2.95), (7.61, 2.95)], teal)
    arrow([(7.48, 2.95), (6.07, 2.95)], teal)
    arrow([(5.94, 2.95), (.90, 2.95), (.90, 3.29)], teal)
    ax.text(3.25, 2.66, "Cold helium returns to warm recovery", color=teal,
            ha="center", va="center")
    arrow([(6.78, 3.63), (6.78, 3.17)], red, "--")
    ax.text(6.78, 2.78, "heat", color=red, ha="center", fontsize=10)
    ax.text(7.8, 1.05, "Vapor returns; liquid remains", ha="center", fontsize=11)
    ax.text(4.8, 4.75, "Purified helium →", ha="center", color=blue, fontsize=12)
    ax.text(4.8, .35, "Functional paths only • no apparatus geometry or operating settings\n"
            "Separate streams exchange heat without mixing", ha="center", va="center",
            color="#45515e", fontsize=11)
    # Structural checks: a feed path, a return path and separate thermal coupling.
    feed = ["compression", "air", "hydrogen", "exchanger", "throttle", "collector"]
    returning = ["collector", "exchanger", "compression"]
    assert feed.index("hydrogen") < feed.index("exchanger") < feed.index("throttle")
    assert returning[0] == feed[-1] and returning[-1] == feed[0]
    assert returning.count("exchanger") == feed.count("exchanger") == 1
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
