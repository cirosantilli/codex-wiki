"""Enumerate every proper three-palette coloring of P3; write PNG to CWD."""
from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    colorings = [
        c for c in product(range(3), repeat=3)
        if c[0] != c[1] and c[1] != c[2]
    ]
    assert len(colorings) == 12
    palette = ["#246a9b", "#ce8434", "#7c458a"]
    fig, axes = plt.subplots(3, 4, figsize=(10, 6.5), dpi=120)
    fig.patch.set_facecolor("white")
    for ax, colors in zip(axes.flat, colorings):
        ax.plot([0, 1, 2], [0, 0, 0], color="#444444", lw=2, zorder=1)
        for x, color in enumerate(colors):
            ax.scatter(x, 0, s=850, color=palette[color],
                       edgecolor="white", linewidth=1.5, zorder=2)
            ax.text(x, 0, str(color + 1), color="white",
                    ha="center", va="center", weight="bold", fontsize=13)
            ax.text(x, -0.3, "ABC"[x], ha="center", va="top", fontsize=11)
        ax.set(xlim=(-0.5, 2.5), ylim=(-0.65, 0.55))
        ax.axis("off")
    fig.suptitle("Three named palette colours: twelve proper path colourings",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.035,
             "Adjacent colours differ; A and C may agree. Numbers identify palette colours.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.88,
                        bottom=0.12, hspace=0.3, wspace=0.1)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
