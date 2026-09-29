"""Draw two permutation maps; tested with Python 3.14.4 and matplotlib 3.10.7+dfsg1.

Write permutation-cycle-structure.png in the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def draw_map(ax, mapping, positions, colors, paired=False):
    for label, image in mapping.items():
        ax.add_patch(FancyArrowPatch(
            positions[label], positions[image], arrowstyle="-|>", mutation_scale=19,
            connectionstyle="arc3,rad=0.28" if paired else "arc3,rad=0",
            shrinkA=23, shrinkB=23, linewidth=2, color=colors[label], zorder=1))
    for label, (x, y) in positions.items():
        ax.scatter(x, y, s=1150, color="white", edgecolor=colors[label],
                   linewidth=2, zorder=2)
        ax.text(x, y, str(label), ha="center", va="center", fontsize=19,
                color=colors[label], zorder=3)
    ax.set(xlim=(-1.45, 1.45), ylim=(-1.4, 1.4), aspect="equal")
    ax.axis("off")


def main():
    sigma = {1: 3, 2: 1, 3: 4, 4: 2}
    rho = {1: 3, 2: 4, 3: 1, 4: 2}
    fig, axes = plt.subplots(1, 2, figsize=(8.5, 4.6), dpi=120, facecolor="white")
    draw_map(axes[0], sigma,
             {1: (-0.8, 0.8), 3: (0.8, 0.8), 4: (0.8, -0.8), 2: (-0.8, -0.8)},
             {label: "#246d9a" for label in sigma})
    draw_map(axes[1], rho,
             {1: (-0.8, 0.8), 3: (0.8, 0.8), 2: (-0.8, -0.8), 4: (0.8, -0.8)},
             {1: "#b45925", 3: "#b45925", 2: "#388363", 4: "#388363"}, paired=True)
    axes[0].set_title(r"$\sigma=(1\;3\;4\;2)$" + "\nOne loop of length four", fontsize=13)
    axes[1].set_title(r"$\rho=(1\;3)(2\;4)$" + "\nTwo loops of length two", fontsize=13)
    for ax, mapping in zip(axes, [sigma, rho]):
        images = "    ".join(f"{label} → {mapping[label]}" for label in sorted(mapping))
        ax.text(0.5, -0.04, images, transform=ax.transAxes, ha="center",
                fontsize=11, color="#344454")
    fig.suptitle("Cycle notation follows the arrows", fontsize=16, y=0.98)
    fig.text(0.5, 0.035, "Each label has one outgoing arrow and one incoming arrow.",
             ha="center", fontsize=11, color="#344454")
    fig.subplots_adjust(left=0.04, right=0.96, top=0.76, bottom=0.13, wspace=0.22)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
