"""Original signed-filter schematic; all numbers are toy assumptions, not data.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Writes only orientation-selectivity-signed-bars.png to CWD.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


OUTPUT = Path("orientation-selectivity-signed-bars.png")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    weights = np.tile(np.array([-.5, -.5, 2., -.5, -.5]) / 10, (5, 1))
    central = np.zeros((5, 5)); central[:, 2] = 1
    horizontal = np.zeros((5, 5)); horizontal[2, :] = 1
    shifted = np.zeros((5, 5)); shifted[:, 3] = 1
    stimuli = [central, horizontal, np.ones((5, 5)), shifted, -shifted]
    titles = ["Centered bright bar", "Rotated bright bar", "Uniform bright patch",
              "Shifted bright bar", "Shifted dark bar"]
    drives = [round(float(np.sum(weights * stimulus)), 12) for stimulus in stimuli]
    assert np.allclose(drives, [1, 0, 0, -.25, .25], atol=1e-14)
    fig = plt.figure(figsize=(9, 6.3), dpi=120, facecolor="white")
    grid = fig.add_gridspec(2, 5, left=.045, right=.97, bottom=.14, top=.84,
                           hspace=.63, wspace=.35)
    fig.suptitle("Orientation, position and polarity: a signed-filter toy", fontsize=16,
                 weight="bold", y=.97)
    fig.text(.5, .91, "Original schematic • chosen weights • not measured receptive fields or spikes",
             ha="center", fontsize=10.5)
    ax = fig.add_subplot(grid[0, :2])
    ax.imshow(weights, cmap=ListedColormap(["#cee4f3", "#f6c8a2"]),
              vmin=-.05, vmax=.2, origin="lower")
    for y in range(5):
        for x in range(5):
            ax.text(x, y, "+" if x == 2 else "−", ha="center", va="center",
                    fontsize=16, color="#24364a")
    ax.set_title("A. Weight map K (5 × 5)", fontsize=11, weight="bold", pad=10)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("OFF-like flanks | ON-like center", fontsize=10, labelpad=8)
    ax = fig.add_subplot(grid[0, 2:])
    ax.axis("off")
    ax.text(.02, .94, "B. Multiply each contrast by its weight; add", weight="bold", va="top")
    ax.text(.02, .77, r"$D=\sum K_{ij}C_{ij}$       $R=\max(0,D)$", fontsize=15, va="top")
    ax.text(.02, .55, "Each + site: K = +0.20; each − site: K = −0.05\nC = +1: bright; C = 0: background; C = −1: dark",
            fontsize=10, linespacing=1.8, va="top")
    ax.text(.02, .20, "D is signed drive; R is rectified toy output.\nNeither is a measured firing rate.",
            fontsize=10, color="#42566b", va="top")
    for index, (stimulus, title, drive) in enumerate(zip(stimuli, titles, drives)):
        ax = fig.add_subplot(grid[1, index])
        ax.imshow(stimulus, cmap="gray", vmin=-1, vmax=1, origin="lower")
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_title(title.replace(" ", "\n", 1), fontsize=10, pad=10)
        ax.set_xlabel(f"D = {drive:g}\nR = {max(0, drive):g}", fontsize=11, labelpad=9)
    fig.text(.5, .035, "Each image uses the same background. Rotation preserves bar area; shifting preserves bar angle.",
             ha="center", fontsize=9.5)
    fig.savefig(OUTPUT, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
