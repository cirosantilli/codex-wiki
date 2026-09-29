"""Plot addition by 1, 2, and 3 modulo six; write the PNG to the CWD."""

from pathlib import Path
from math import gcd

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


def cycles(n, step):
    """Disjoint cycles of the permutation x -> x + step (mod n)."""
    unseen = set(range(n))
    result = []
    while unseen:
        start = min(unseen)
        orbit = []
        x = start
        while x in unseen:
            unseen.remove(x)
            orbit.append(x)
            x = (x + step) % n
        assert x == start
        result.append(orbit)
    assert len(result) == gcd(n, step)
    assert all(len(cycle) == n // gcd(n, step) for cycle in result)
    return result


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(12, 5.3), dpi=100)
    palette = ["#246bce", "#bf5520", "#23855b"]
    angles = np.pi / 2 - 2 * np.pi * np.arange(6) / 6
    positions = np.column_stack((np.cos(angles), np.sin(angles)))
    for ax, step in zip(axes, (1, 2, 3), strict=True):
        orbits = cycles(6, step)
        for color, orbit in zip(palette, orbits):
            for x in orbit:
                y = (x + step) % 6
                # Opposite arrows use different sides of the chord for step 3.
                bend = 0.10 if step == 3 else -0.09
                ax.add_patch(
                    FancyArrowPatch(
                        positions[x], positions[y],
                        arrowstyle="-|>", mutation_scale=17,
                        shrinkA=15, shrinkB=15,
                        connectionstyle=f"arc3,rad={bend}",
                        linewidth=2.0, color=color, zorder=1,
                    )
                )
            for x in orbit:
                ax.add_patch(Circle(positions[x], 0.14, facecolor="white",
                                    edgecolor=color, linewidth=2.5, zorder=2))
                ax.text(*positions[x], str(x), ha="center", va="center",
                        color=color, weight="bold", zorder=3)
        ax.set_title(f"Add {step} modulo 6", weight="bold", pad=13)
        ax.text(0, -1.44,
                f"{len(orbits)} cycle{'s' if len(orbits) > 1 else ''}, "
                f"length {len(orbits[0])}\n"
                + ("Visits all six from 0" if step == 1
                   else "Visits only part of the group from 0"),
                ha="center", va="top", fontsize=11)
        ax.set(xlim=(-1.3, 1.3), ylim=(-1.95, 1.3), aspect="equal")
        ax.axis("off")
    fig.suptitle("A repeated step can split the same six-element group into cycles",
                 fontsize=16, weight="bold", y=0.965)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.80, bottom=0.10, wspace=0.16)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
