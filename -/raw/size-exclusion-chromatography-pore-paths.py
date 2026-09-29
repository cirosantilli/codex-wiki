"""Draw conceptual SEC pore excursions; run from _media with Python 3.14.

Routes are illustrative, not streamlines, measured paths, or residence times.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(3, 1, figsize=(9.2, 6.8), facecolor="white")
    colors = ["#c34831", "#247ba0", "#278453"]
    labels = ["Large: excluded", "Intermediate: partial access", "Small: extensive access"]
    paths = [
        [(0.5, 0.38), (9.5, 0.38)],
        [(0.5, 0.38), (2.0, 0.38), (2.0, 1.10), (2.8, 1.10),
         (2.8, 0.38), (6.3, 0.38), (6.3, 1.10), (7.1, 1.10),
         (7.1, 0.38), (9.5, 0.38)],
        [(0.5, 0.38), (2.0, 0.38), (2.0, 1.1), (2.25, 1.1),
         (2.25, 1.65), (2.55, 1.65), (2.55, 1.1), (2.8, 1.1),
         (2.8, 0.38), (6.3, 0.38), (6.3, 1.1), (6.55, 1.1),
         (6.55, 1.65), (6.85, 1.65), (6.85, 1.1), (7.1, 1.1),
         (7.1, 0.38), (9.5, 0.38)],
    ]
    for i, (ax, color, label, path) in enumerate(zip(axes, colors, labels, paths)):
        ax.set(xlim=(0, 10), ylim=(0, 2.2), aspect="equal")
        ax.axis("off")
        ax.add_patch(Rectangle((0.3, 0.03), 9.4, 0.68, color="#eaf4fb", zorder=0))
        for x in (1.4, 5.7):
            ax.add_patch(Rectangle((x, 0.70), 2.1, 1.18, fc="#dedbd5", ec="#929087"))
            # Open branches of pore liquid within a schematic packing particle.
            for opening in (0.42, 1.22):
                ax.add_patch(Rectangle((x + opening, 0.70), 0.36, 0.60, fc="#eaf4fb", ec="none"))
            ax.add_patch(Rectangle((x + 0.42, 0.90), 1.16, 0.40, fc="#eaf4fb", ec="none"))
            for neck in (0.76, 1.06):
                ax.add_patch(Rectangle((x + neck, 1.20), 0.18, 0.54, fc="#eaf4fb", ec="none"))
            ax.add_patch(Rectangle((x + 0.76, 1.55), 0.48, 0.19, fc="#eaf4fb", ec="none"))
        xs, ys = zip(*path)
        ax.plot(xs, ys, color=color, lw=2.8, solid_capstyle="round")
        ax.add_patch(FancyArrowPatch(path[-2], path[-1], arrowstyle="-|>", mutation_scale=15,
                                    color=color, lw=2.8))
        ax.add_patch(Circle((0.60, 0.38), [0.27, 0.16, 0.07][i], fc=color, ec="white", lw=1.2, zorder=5))
        ax.text(0.35, 2.03, label, color=color, weight="bold")
        ax.text(8.45, 1.30, ["earlier", "between", "later"][i], color=color, ha="center", weight="bold")
        if i == 0:
            ax.annotate("solid\nmatrix", (3.22, 1.48), (4.4, 1.49), ha="center", fontsize=10,
                        arrowprops={"arrowstyle": "->", "color": "#555555"})
            ax.annotate("pore liquid", (2.40, 1.66), (3.72, 1.96), fontsize=10,
                        arrowprops={"arrowstyle": "->", "color": "#555555"})
    axes[-1].text(4.7, 0.10, "interparticle liquid: through-flow →", ha="center", fontsize=10,
                  bbox={"fc": "white", "ec": "none", "alpha": 0.95, "pad": 1.3})
    fig.suptitle("Size exclusion: less pore access means earlier elution", weight="bold", y=0.98)
    fig.text(0.5, 0.025, "Original schematic • pore visits are random and reversible • no adsorption • not to scale",
             ha="center", fontsize=10)
    fig.subplots_adjust(top=0.91, bottom=0.09, hspace=0.24, left=0.04, right=0.98)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
