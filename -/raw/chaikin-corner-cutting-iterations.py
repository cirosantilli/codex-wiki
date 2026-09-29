"""Original closed Chaikin illustration; write the matching PNG basename to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media to create the repository's image asset.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def cut_closed(points):
    """Return two points per cyclic edge, using the entire old array."""
    following = np.roll(points, -1, axis=0)
    refined = np.empty((2 * len(points), points.shape[1]))
    refined[0::2] = 0.75 * points + 0.25 * following
    refined[1::2] = 0.25 * points + 0.75 * following
    return refined


def close(points):
    return np.vstack((points, points[0]))


def main():
    rectangle = np.array([[0., 0.], [4., 0.], [4., 2.], [0., 2.]])
    stages = {0: rectangle}
    for step in range(1, 6):
        stages[step] = cut_closed(stages[step - 1])

    fig, axes = plt.subplots(2, 2, figsize=(9, 6.8), dpi=120)
    fig.patch.set_facecolor("white")
    for ax, step in zip(axes.flat, (0, 1, 2, 5)):
        ax.set_facecolor("white")
        old = close(rectangle)
        current = close(stages[step])
        ax.plot(old[:, 0], old[:, 1], "--", color="#999999", lw=1.5,
                label="Original polygon / hull", zorder=1)
        ax.plot(current[:, 0], current[:, 1], color="#17679b", lw=2,
                label="Current polygon", zorder=2)
        ax.scatter(stages[step][:, 0], stages[step][:, 1],
                   s=24 if step < 3 else 7, color="#17679b", zorder=3)
        ax.set_title(f"Iteration {step}: {len(stages[step])} vertices", fontsize=12)
        ax.set(xlim=(-0.45, 4.45), ylim=(-0.4, 2.4), aspect="equal")
        ax.set_xticks(range(5))
        ax.set_yticks([0, 1, 2])
        ax.set_xlabel("x" if step >= 2 else "", labelpad=1)
        ax.set_ylabel("y", labelpad=1)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(color="#eeeeee", lw=0.6)
        ax.set_axisbelow(True)
    fig.suptitle("Chaikin corner cutting: replace each edge by its quarter points",
                 fontsize=14, y=0.98)
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2,
               bbox_to_anchor=(0.5, 0.045), frameon=False, fontsize=10)
    fig.text(0.5, 0.025, "Every panel is a finite polygon, including iteration 5.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0.01, 0.11, 0.99, 0.94), h_pad=3.5, w_pad=2)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
