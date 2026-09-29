"""Compare length and area scaling of similar right triangles; output in cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Both triangles share the same plotting scale; the grid has unit spacing.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Polygon
import numpy as np


def main():
    original = np.array([[0, 0], [4, 0], [0, 3]])
    scaled = 2 * original
    lengths = np.linalg.norm(np.roll(original, -1, axis=0) - original, axis=1)
    scaled_lengths = np.linalg.norm(np.roll(scaled, -1, axis=0) - scaled, axis=1)
    assert sorted(lengths) == [3, 4, 5]
    assert sorted(scaled_lengths) == [6, 8, 10]
    assert np.all(scaled_lengths / lengths == 2)
    areas = [abs(np.linalg.det((v[1:] - v[0]).T)) / 2
             for v in (original, scaled)]
    assert np.allclose(areas, [6, 24])
    acute = np.degrees(np.arctan2(3, 4))
    assert np.isclose(acute, 36.86989764584402)
    assert np.isclose(np.degrees(np.arctan2(6, 8)), acute)

    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.2, 5.7), facecolor="white")
    fig.subplots_adjust(left=0.045, right=0.98, bottom=0.24, top=0.81)
    ax.set_facecolor("white")
    ax.set_aspect("equal")
    for scale, shift, face, color, area in [
        (1, 0, "#e5eefb", "#245b9b", 6),
        (2, 7, "#e1f2e9", "#287551", 24),
    ]:
        v = scale * original + np.array([shift, 0])
        ax.add_patch(Polygon(v, facecolor=face, edgecolor=color, linewidth=2.2))
        ax.plot([shift + 0.35, shift + 0.35, shift], [0, 0.35, 0.35],
                color=color, linewidth=1.5)
        ax.text(shift + 0.48, 0.28, "90°", fontsize=10, color=color)
        ax.text(shift - 0.25, 1.5 * scale, str(3 * scale),
                ha="right", va="center", color=color, fontsize=16)
        ax.text(shift + 2 * scale, -0.35, str(4 * scale),
                ha="center", va="top", color=color, fontsize=16)
        ax.text(shift + 2 * scale + 0.28, 1.5 * scale + 0.33,
                str(5 * scale), ha="center", color=color, fontsize=16)
        ax.text(shift + 1.1 * scale, 1.05 * scale, f"Area = {area}",
                ha="center", fontsize=13, color=color)
        # Equal angle arcs retain the same visual radius in both triangles.
        ax.add_patch(Arc((shift + 4 * scale, 0), 1.6, 1.6,
                         theta1=180 - acute, theta2=180, edgecolor=color, lw=1.5))
        ax.text(shift + 4 * scale + 0.05, -0.3, "36.87°",
                ha="center", color=color, fontsize=10)
        ax.text(shift, 3 * scale + 0.25, "53.13°",
                ha="center", va="bottom", color=color, fontsize=10)

    ax.set_xlim(-0.8, 15.7)
    ax.set_ylim(-0.8, 6.6)
    ax.set_xticks(np.arange(0, 16))
    ax.set_yticks(np.arange(0, 7))
    ax.grid(color="#e6e6e6", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(length=0, labelbottom=False, labelleft=False)
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.suptitle("Similar triangles: lengths ×2, area ×4", fontsize=20, y=0.97)
    fig.text(0.5, 0.89, "Same angles • Same plotting scale • Grid spacing = 1 length unit",
             ha="center", fontsize=12)
    fig.text(0.5, 0.155, "Corresponding lengths: 6/3 = 8/4 = 10/5 = 2",
             ha="center", fontsize=14)
    fig.text(0.5, 0.085, "Areas: 24/6 = 4 = 2²", ha="center", fontsize=15,
             fontweight="bold")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=140, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Saved {output.name}; lengths ×2, areas 6 → 24 and angles checked.")


if __name__ == "__main__":
    main()
