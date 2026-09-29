"""Original generator orbits in two cyclic-group products; PNG to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def arrow(ax, start, end, color, rad=.12):
    ax.add_patch(FancyArrowPatch(
        start, end, arrowstyle="-|>", mutation_scale=15,
        connectionstyle=f"arc3,rad={rad}", shrinkA=28, shrinkB=28,
        color=color, lw=1.8, zorder=1))


def node(ax, pos, label, color):
    ax.scatter(*pos, s=2200, facecolor="white", edgecolor=color,
               linewidth=2, zorder=2)
    ax.text(*pos, label, ha="center", va="center", fontsize=11, zorder=3)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.3, 5), dpi=120)
    fig.patch.set_facecolor("white")
    angles = np.pi/2-np.arange(6)*2*np.pi/6
    positions = np.column_stack([1.08*np.cos(angles), 1.08*np.sin(angles)])
    for q, pos in enumerate(positions):
        arrow(axes[0], pos, positions[(q+1) % 6], "#246a9b")
        node(axes[0], pos, f"n = {q}\n({q % 2}, {q % 3})", "#246a9b")
    axes[0].set_title(r"$C_2\times C_3$: six additions return to zero", fontsize=12)
    for y, labels, color in [
            (.6, ["(0, 0)", "(1, 1)"], "#246a9b"),
            (-.6, ["(0, 1)", "(1, 0)"], "#888888")]:
        p, q = (-.85, y), (.85, y)
        arrow(axes[1], p, q, color, .22)
        arrow(axes[1], q, p, color, .22)
        node(axes[1], p, labels[0], color)
        node(axes[1], q, labels[1], color)
    axes[1].text(0, .03, "Other coset: never reached from (0, 0)",
                 ha="center", va="center", fontsize=10, color="#666666")
    axes[1].set_title(r"$C_2\times C_2$: two additions return to zero", fontsize=12)
    for ax in axes:
        ax.set(xlim=(-1.55, 1.55), ylim=(-1.55, 1.55), aspect="equal")
        ax.axis("off")
    fig.suptitle("Repeat the step (1, 1): simultaneous return of both counters",
                 fontsize=14)
    fig.text(.5, .04,
             "Blue arrows show the orbit from the identity. Each arrow adds (1, 1) in the product.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.03, right=.97, top=.82, bottom=.13, wspace=.12)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
