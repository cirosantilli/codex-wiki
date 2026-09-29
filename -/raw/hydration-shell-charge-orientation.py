"""Original qualitative hydration schematic; positions are not molecular data.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the opaque PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def water_geometry(angle, positive, radius=1.65):
    """Return arbitrary 2D atom coordinates with the appropriate polar end inward."""
    radial = np.array([np.cos(angle), np.sin(angle)])
    tangent = np.array([-np.sin(angle), np.cos(angle)])
    oxygen = radius * radial
    direction = radial if positive else -radial
    half_angle = np.deg2rad(52.25)
    hydrogens = np.array([
        oxygen + 0.40 * (np.cos(half_angle) * direction + sign * np.sin(half_angle) * tangent)
        for sign in [-1, 1]
    ])
    return oxygen, hydrogens


def draw_water(ax, oxygen, hydrogens):
    for hydrogen in hydrogens:
        ax.plot(*np.array([oxygen, hydrogen]).T, color="#7b8490", lw=2, zorder=2)
        ax.add_patch(Circle(hydrogen, 0.10, facecolor="white", edgecolor="#677382", lw=1.2, zorder=4))
    ax.add_patch(Circle(oxygen, 0.16, facecolor="#d64945", edgecolor="#a73131", lw=1, zorder=5))


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 6.0), facecolor="white")
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.22, top=0.75, wspace=0.12)
    for ax, positive in zip(axes, [True, False]):
        ax.set_aspect("equal")
        ax.set_xlim(-2.7, 2.7)
        ax.set_ylim(-2.55, 2.55)
        ax.axis("off")
        ax.add_patch(Circle((0, 0), 2.13, fill=False, edgecolor="#a4aebb", ls=(0, (4, 4)), lw=1.3))
        ax.add_patch(Circle((0, 0), 0.55, facecolor="#e8f0fb" if positive else "#f1eafb", edgecolor="#526780", lw=1.5))
        ax.text(0, 0, "$+e$" if positive else "$-e$", ha="center", va="center", fontsize=25)
        # Five selected glyphs illustrate polarity; this is not a coordination count.
        for angle in np.deg2rad([18, 90, 162, 234, 306]):
            oxygen, hydrogens = water_geometry(angle, positive)
            oxygen_r = np.linalg.norm(oxygen)
            hydrogen_r = np.linalg.norm(hydrogens, axis=1)
            assert np.all(hydrogen_r > oxygen_r) if positive else np.all(hydrogen_r < oxygen_r)
            draw_water(ax, oxygen, hydrogens)
        ax.set_title("Cation: oxygen end inward" if positive else "Anion: hydrogen end inward", fontsize=14, pad=16)
        ax.text(0, -2.50, "Ion retains its positive charge" if positive else "Ion retains its negative charge", ha="center", fontsize=12)
    fig.suptitle("Hydration changes the surroundings of an ion", fontsize=18, y=0.95)
    fig.text(0.5, 0.86, "Selected water molecules in a schematic first shell", ha="center", color="#4d5968", fontsize=13)
    fig.text(0.5, 0.15, r"Red: oxygen ($\delta^-$)     White: hydrogen ($\delta^+$)     Each water molecule is neutral", ha="center", fontsize=12)
    fig.text(0.5, 0.08, "Positions and distances are illustrative; five glyphs do not specify a coordination number.", ha="center", fontsize=11)
    fig.text(0.5, 0.035, "Real shells fluctuate and exchange molecules with the surrounding water.", ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
