"""Seven-triangle drums; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Emit the matching opaque PNG basename into the caller's current directory.
MPLBACKEND and MPLCONFIGDIR remain caller-controlled.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.lines import Line2D

POINT_EDGES = (((2, 3), (6, 7)), ((4, 6), (5, 7)), ((1, 5), (3, 7)))
LINE_EDGES = (((1, 3), (5, 7)), ((2, 6), (3, 7)), ((4, 5), (6, 7)))


def reflected_tiles(edges, triangle):
    result = {7: np.array(triangle, dtype=float)}
    while len(result) < 7:
        for colour, pairs in enumerate(edges):
            for first, second in pairs:
                if first not in result and second in result:
                    first, second = second, first
                if first in result and second not in result:
                    vertices = result[first]
                    origin = vertices[(colour + 1) % 3]
                    direction = vertices[(colour + 2) % 3] - origin
                    unit = direction / np.linalg.norm(direction)
                    reflection = 2 * np.outer(unit, unit) - np.eye(2)
                    result[second] = origin + (vertices - origin) @ reflection
    return result


def main():
    triangle = np.array(((0.0, 0.0), (1.0, 0.0), (0.47, 0.84)))
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 6.2), dpi=100, facecolor="white")
    colours = ("#bb3439", "#13805e", "#356db7")
    for ax, edges, heading in zip(axes, (POINT_EDGES, LINE_EDGES), ("Point domain", "Line domain")):
        triangles = reflected_tiles(edges, triangle)
        for number, vertices in sorted(triangles.items()):
            ax.add_patch(Polygon(vertices, closed=True, facecolor="#e1ebf5" if number != 7 else "#bed3ea", edgecolor="none"))
            for colour in range(3):
                ends = vertices[[(colour + 1) % 3, (colour + 2) % 3]]
                ax.plot(ends[:, 0], ends[:, 1], color=colours[colour], linewidth=1.8)
            centre = vertices.mean(axis=0)
            ax.text(*centre, str(number), ha="center", va="center", fontsize=14, fontweight="bold")
        for name, vertex, offset in zip("ABC", triangle, ((-0.05, 0.055), (0.06, 0.055), (0.0, 0.095))):
            ax.text(*(vertex + offset), name, ha="center", va="center", fontsize=10,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
        ax.set_title(heading, fontsize=16)
        ax.set_aspect("equal")
        ax.set_xlim(-1.1, 2.1)
        ax.set_ylim(-1.05, 1.95)
        ax.axis("off")
    fig.suptitle("Noncongruent drums with identical Dirichlet spectra", fontsize=17, y=0.94)
    handles = [Line2D((0,), (0,), color=colour, lw=3, label=f"Side {name} (opposite {name.upper()})") for colour, name in zip(colours, "abc")]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, fontsize=11, bbox_to_anchor=(0.5, 0.06))
    fig.subplots_adjust(left=0.025, right=0.975, top=0.86, bottom=0.17, wspace=0.03)
    fig.savefig(Path.cwd() / "paper-22-propeller-drums.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
