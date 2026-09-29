"""Draw labeled square symmetries; save square-symmetry-composition.png in cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Products act rightmost first: rs = r after s.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    identity = np.eye(2, dtype=int)
    rotation = np.array([[0, -1], [1, 0]])
    reflection = np.array([[-1, 0], [0, 1]])
    vertices = np.array([[1, 1], [-1, 1], [-1, -1], [1, -1]])
    rs = rotation @ reflection
    sr = reflection @ rotation
    assert np.array_equal(rs, [[0, -1], [-1, 0]])
    assert np.array_equal(sr, [[0, 1], [1, 0]])
    assert np.array_equal(rs @ vertices[0], [-1, -1])
    assert np.array_equal(sr @ vertices[0], [1, 1])
    assert np.array_equal(np.linalg.matrix_power(rotation, 4), identity)
    assert np.array_equal(reflection @ reflection, identity)
    assert np.array_equal(reflection @ rotation @ reflection, rotation.T)

    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10, 6.3), facecolor="white")
    grid = fig.add_gridspec(
        2, 5, width_ratios=[1, 0.42, 1, 0.42, 1],
        left=0.04, right=0.98, bottom=0.13, top=0.77,
        wspace=0.06, hspace=0.47,
    )
    colors = ["#b32929", "#2766a5", "#276945", "#7656a5"]
    rows = [
        ([identity, reflection, rs], ["Start", "After s", "After rs"],
         ["s", "r"], r"$rs(A)=(-1,-1)$"),
        ([identity, rotation, sr], ["Start", "After r", "After sr"],
         ["r", "s"], r"$sr(A)=(1,1)$"),
    ]
    for row, (matrices, titles, operations, result) in enumerate(rows):
        for col, (matrix, title) in enumerate(zip(matrices, titles)):
            ax = fig.add_subplot(grid[row, 2 * col])
            ax.set_facecolor("white")
            ax.set_aspect("equal")
            ax.set_xlim(-1.6, 1.6)
            ax.set_ylim(-1.6, 1.6)
            ax.axis("off")
            ax.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1],
                    color="#48515c", linewidth=2)
            ax.axhline(0, color="#c9cdd2", linewidth=0.8, zorder=0)
            ax.axvline(0, color="#c9cdd2", linewidth=0.8, zorder=0)
            transformed = vertices @ matrix.T
            for label, color, point in zip("ABCD", colors, transformed):
                x, y = point
                ax.scatter(x, y, s=120 if label == "A" else 55,
                           color=color, edgecolors="white", linewidths=1.2,
                           zorder=3)
                ax.text(1.3 * x, 1.3 * y, label, color=color,
                        ha="center", va="center", fontsize=15,
                        fontweight="bold")
            ax.set_title(title, fontsize=13, pad=5)
            if col == 2:
                ax.text(0.5, -0.11, result, transform=ax.transAxes,
                        ha="center", fontsize=13, color="#b32929")
        for col, operation in enumerate(operations):
            ax = fig.add_subplot(grid[row, 2 * col + 1])
            ax.axis("off")
            ax.annotate("", xy=(0.98, 0.52), xytext=(0.02, 0.52),
                        arrowprops={"arrowstyle": "->", "lw": 2,
                                    "color": "#48515c"})
            ax.text(0.5, 0.68, operation, ha="center", va="center",
                    fontsize=18, fontstyle="italic")

    fig.suptitle("Square symmetries: order matters", fontsize=20, y=0.97)
    fig.text(0.5, 0.88,
             r"$r(x,y)=(-y,x)$: rotate 90° counterclockwise    "
             r"$s(x,y)=(-x,y)$: reflect in the y-axis",
             ha="center", fontsize=12)
    fig.text(0.5, 0.055,
             r"Products act rightmost first: $rs=r\circ s$.  "
             r"Labels track vertices; red A starts at $(1,1)$.  $rs\ne sr$.",
             ha="center", fontsize=12)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Saved {output.name}; square composition identities checked.")


if __name__ == "__main__":
    main()
