"""Plot the computed principal axes; save the PNG in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from the corresponding _media directory with the repository environment.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def main():
    angle = np.arctan(2.0) / 2
    small_axis = np.array([np.cos(angle), np.sin(angle)])
    large_axis = np.array([-np.sin(angle), np.cos(angle)])
    inertia = np.array([[1.0, -1.0], [-1.0, 2.0]])
    assert np.allclose(inertia @ small_axis, (3 - np.sqrt(5)) / 2 * small_axis)
    assert np.allclose(inertia @ large_axis, (3 + np.sqrt(5)) / 2 * large_axis)

    fig, ax = plt.subplots(figsize=(6.5, 4.8))
    fig.set_facecolor("white")
    vertices = np.array([[-2, -1], [0, 1], [2, 1], [0, -1]])
    ax.add_patch(Polygon(vertices, facecolor="#dce7ed", edgecolor="#4c626f", linewidth=1.5))
    ax.axhline(0, color="0.7", linewidth=0.7, zorder=0)
    ax.axvline(0, color="0.7", linewidth=0.7, zorder=0)
    for direction, color, name in [(small_axis, "#1764ab", r"$I_-$"),
                                    (large_axis, "#b44720", r"$I_+$")]:
        extent = 2.1
        start, end = -extent * direction, extent * direction
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "<->", "color": color, "linewidth": 2.2})
        ax.text(*(1.08 * end), name, color=color, fontsize=13, ha="center", va="center")
    ax.scatter([0], [0], color="black", s=22, zorder=5)
    arc_angle = np.linspace(0, angle, 80)
    ax.plot(0.6 * np.cos(arc_angle), 0.6 * np.sin(arc_angle), color="#1764ab", linewidth=1)
    ax.text(0.69, 0.13, r"$31.7^\circ$", color="#1764ab", fontsize=10)
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.25, 2.25)
    ax.set_aspect("equal")
    ax.set_xlabel(r"$x_1/D$")
    ax.set_ylabel(r"$x_2/D$")
    ax.set_xticks([-2, -1, 0, 1, 2])
    ax.set_yticks([-2, -1, 0, 1, 2])
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Principal axes through the centre of mass", fontsize=12)
    fig.text(0.5, 0.018, r"$I_\pm=MD^2(3\pm\sqrt{5})/6$; normal axis: $I_3=MD^2$",
             ha="center", fontsize=11)
    fig.tight_layout(rect=(0, 0.055, 1, 1))
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
