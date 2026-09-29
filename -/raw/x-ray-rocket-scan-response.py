"""Generate a functional scanning schematic; curves are invented, not flight data.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the output is written to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(10, 6.5), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=[1.15, 1])
    rocket = fig.add_subplot(grid[0, 0])
    rocket.set(xlim=(0, 10), ylim=(0, 7))
    rocket.axis("off")
    rocket.set_title("Rotating counter: functional view", loc="left", weight="bold")
    rocket.add_patch(Rectangle((3.7, 0.6), 2, 4.9, color="#e8edf2", ec="#364e62"))
    rocket.plot([3.7, 4.7, 5.7], [5.5, 6.7, 5.5], color="#364e62")
    rocket.annotate("spin axis", (4.7, 6.3), (1, 6.4), arrowprops={"arrowstyle": "->"})
    rocket.plot([4.7, 4.7], [0.4, 6.6], ls="--", color="gray")
    rocket.add_patch(Rectangle((5.1, 2.2), 1.6, 1.6, fc="#f0c8a1", ec="#9d5515"))
    rocket.add_patch(Rectangle((5.35, 2.5), 1.1, 1, fc="#fff4d7", ec="#9d5515"))
    rocket.text(7, 3.0, "counter", va="center")
    rocket.annotate("surrounding veto", (5.2, 2.25), (0.1, 1.1),
                    arrowprops={"arrowstyle": "->"})
    rocket.annotate("sky photons", (6.45, 3.3), (8.8, 5.7),
                    ha="center", arrowprops={"arrowstyle": "->", "color": "#2468a2"})
    rocket.add_patch(FancyArrowPatch((3.6, 4.6), (5.9, 4.6),
                     connectionstyle="arc3,rad=-.6", arrowstyle="->", mutation_scale=13))
    rocket.text(0.1, 0.0, "Orientation + accepted pulses → angular bins", fontsize=10)

    col = fig.add_subplot(grid[0, 1])
    col.set(xlim=(0, 10), ylim=(0, 7))
    col.axis("off")
    col.set_title("Separate teaching collimator", loc="left", weight="bold")
    for y in (2, 4):
        col.plot([2.5, 7], [y, y], lw=7, color="#526b79")
    col.plot([7.3, 7.3], [2, 4], lw=6, color="#b16624")
    col.annotate("", (7.1, 3), (0.4, 3), arrowprops={"arrowstyle": "->", "lw": 2, "color": "#2468a2"})
    col.annotate("", (4.5, 4), (1.0, 6.3), arrowprops={"arrowstyle": "->", "lw": 2, "color": "#bb4545"})
    col.text(5, 5.5, "oblique ray blocked", ha="center")
    col.text(7.2, 1.2, "detector", ha="center")
    col.text(0.2, 0, "No mechanical collimator on the 1962 rocket", fontsize=10)

    ax = fig.add_subplot(grid[1, :])
    angle = np.linspace(-180, 180, 1441)
    broad = np.maximum(0, np.cos(np.deg2rad(angle)))
    narrow = np.maximum(0, 1 - abs(angle) / 20)
    ax.plot(angle, 4 + 6*broad, label="Broad model: max(0, cos φ)", lw=2.3)
    ax.plot(angle, 4 + 6*narrow, label="Collimated model: max(0, 1 − |φ|/20°)", lw=2.3)
    ax.axhline(4, color="gray", ls="--", label="Chosen background: 4 counts/s")
    ax.set(xlim=(-180, 180), ylim=(3, 11), xlabel="Scan angle relative to source (degrees)",
           ylabel="Expected counts/s", title="Invented scan: same peak source rate, different angular acceptance")
    ax.legend(loc="upper right", fontsize=9)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
