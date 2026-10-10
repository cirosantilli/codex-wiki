"""Compare ideal electron-domain bookkeeping with three molecular geometries.

Original constructions, not measured atom positions or electron densities.
Angles: ideal tetrahedron exactly; NH3 106.67 degrees and H2O 104.4776
degrees from the NIST CCCBDB experimental entries cited in chemistry.bigb.
Lengths and sphere sizes are arbitrary; orthographic projections alter angles.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Write the opaque white same-basename PNG to the current working directory.
"""

from itertools import combinations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

BLUE = "#2868a5"
ORANGE = "#b45d16"
INK = "#243342"
GREY = "#a4adb7"


def pyramid(angle):
    """Three unit bonds with equal pair angles; nitrogen is at the origin."""
    c = np.sqrt((1 + 2 * np.cos(np.deg2rad(angle))) / 3)
    radius = np.sqrt(1 - c * c)
    phi = np.deg2rad([10, 130, 250])
    return np.column_stack((radius * np.cos(phi), radius * np.sin(phi),
                            np.full(3, -c)))


def projection(points, elevation=38):
    # Looking slightly down on the triangular base retains its depth.
    elevation = np.deg2rad(elevation)
    return np.column_stack((points[:, 0], points[:, 2] * np.cos(elevation)
                            - points[:, 1] * np.sin(elevation)))


def atom(ax, xy, label, colour, radius=0.14):
    ax.add_patch(Circle(xy, radius, fc="white", ec=colour, lw=2.2, zorder=5))
    ax.text(*xy, label, ha="center", va="center", color=colour,
            fontsize=11, weight="bold", zorder=6)


def draw(ax, points, labels, centre, guides=False, colour=BLUE, elevation=38):
    xy = projection(points, elevation)
    if guides:
        for i, j in combinations(range(len(xy)), 2):
            ax.plot(xy[[i, j], 0], xy[[i, j], 1], ":", color=GREY, lw=1)
    for point, label in zip(xy, labels):
        lp = label == "LP"
        ax.plot([0, point[0]], [0, point[1]], color=ORANGE if lp else BLUE,
                lw=1.5 if lp else 2.3, ls="--" if lp else "-", zorder=2)
        atom(ax, point, label, ORANGE if lp else BLUE,
             radius=0.145 if lp else 0.13)
    atom(ax, (0, 0), centre, colour, radius=0.16)
    ax.set(xlim=(-1.28, 1.28), ylim=(-1.16, 1.25), aspect="equal")
    ax.axis("off")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "text.color": INK})
    ideal = np.vstack(([0, 0, 1], pyramid(np.rad2deg(np.arccos(-1 / 3)))))
    ammonia = pyramid(106.67)
    half = np.deg2rad(104.4776 / 2)
    # Water uses a face-on view so its one labelled angle is undistorted.
    water = np.array([[-np.sin(half), 0, -np.cos(half)],
                      [np.sin(half), 0, -np.cos(half)]])
    fig, axes = plt.subplots(2, 3, figsize=(10, 6.8), facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.13, top=0.82,
                        hspace=0.28, wspace=0.15)
    fig.suptitle("Count electron domains; name the arrangement of atoms", y=0.97,
                 fontsize=17, weight="bold")
    fig.text(0.53, 0.91, "Four domains in each column: bonding regions + lone pairs",
             ha="center", fontsize=11)
    titles = ["Methane  CH₄", "Ammonia  NH₃", "Water  H₂O"]
    centres = ["C", "N", "O"]
    domain_labels = [["H"] * 4, ["LP", "H", "H", "H"],
                     ["LP", "LP", "H", "H"]]
    counts = ["4 bonding · 0 lone pairs", "3 bonding · 1 lone pair",
              "2 bonding · 2 lone pairs"]
    geometries = [ideal, ammonia, water]
    names = ["Tetrahedral", "Trigonal pyramidal", "Bent"]
    angles = ["109.4712°  (exact ideal angle)", "106.7°  (approximate)",
              "104.5°  (approximate)"]
    for col in range(3):
        draw(axes[0, col], ideal, domain_labels[col], centres[col], guides=True)
        axes[0, col].set_title(titles[col], fontsize=14, weight="bold", pad=13)
        axes[0, col].text(0, -1.12, counts[col], ha="center", fontsize=10)
        draw(axes[1, col], geometries[col], ["H"] * len(geometries[col]),
             centres[col], guides=col < 2, elevation=[38, 12, 0][col])
        axes[1, col].text(0, 1.14, names[col], ha="center", weight="bold", fontsize=12)
        axes[1, col].text(0, -1.12, angles[col], ha="center", fontsize=10)
    fig.text(0.025, 0.66, "IDEAL DOMAIN\nSCAFFOLD", rotation=90,
             ha="center", va="center", fontsize=10, weight="bold")
    fig.text(0.025, 0.34, "ATOMS ONLY", rotation=90,
             ha="center", va="center", fontsize=10, weight="bold")
    fig.text(0.53, 0.065, "Orange LP markers are bookkeeping, not atoms or measured electron clouds.",
             ha="center", fontsize=10, color=ORANGE)
    fig.text(0.53, 0.028, "Schematic sizes and lengths · 3D projections · dotted outlines are not chemical bonds",
             ha="center", fontsize=9, color=INK)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
