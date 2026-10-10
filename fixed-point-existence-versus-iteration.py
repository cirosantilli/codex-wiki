"""Draw fixed-point-existence-versus-iteration.png in cwd.

Uses NumPy/Matplotlib; tested with Python 3.14.4 and repository dependencies.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def disk_axes(ax):
    ax.set_facecolor("white")
    ax.add_patch(Circle((0, 0), 1, facecolor="#f4f6f8", edgecolor="#475569", lw=1.5))
    ax.axhline(0, color="#94a3b8", lw=0.6)
    ax.axvline(0, color="#94a3b8", lw=0.6)
    ax.set(xlim=(-1.20, 1.20), ylim=(-1.20, 1.20), xticks=[-1, 0, 1], yticks=[-1, 0, 1])
    ax.set_aspect("equal")
    ax.spines[["top", "right"]].set_visible(False)


def main():
    rotation = np.array([[0.0, -1.0], [1.0, 0.0]])
    offset = np.array([0.3, 0.1])
    fixed = np.array([13 / 58, 11 / 58])
    path = [np.array([1.0, 0.0])]
    for _ in range(10):
        path.append(0.4 * rotation @ path[-1] + offset)
    errors = np.linalg.norm(np.array(path) - fixed, axis=1)
    assert np.allclose(errors, errors[0] * 0.4 ** np.arange(11))
    assert np.allclose(np.linalg.matrix_power(rotation, 4), np.eye(2))

    plt.rcParams.update({"font.size": 11})
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.6), facecolor="white")
    left, middle, right = axes
    disk_axes(left)
    orbit = np.array([[1, 0], [0, 1], [-1, 0], [0, -1], [1, 0]])
    for start, end in zip(orbit[:-1], orbit[1:]):
        left.annotate("", end, xytext=start, arrowprops={"arrowstyle": "->", "color": "#426ca1", "lw": 2})
    left.scatter(orbit[:-1, 0], orbit[:-1, 1], color="#426ca1", s=30, zorder=4)
    left.scatter(0, 0, marker="*", s=130, color="#d05c16", zorder=5)
    left.text(0.05, 0.08, "only fixed point", color="#a94712", fontsize=10)
    left.set_title("Quarter-turn rotation\nOne fixed point; a four-step cycle", fontsize=12)

    disk_axes(middle)
    middle.plot([-1, 1], [0, 0], color="#d05c16", lw=4, label="all fixed points")
    pair = np.array([[0.5, 0.65], [0.5, -0.65]])
    middle.scatter(pair[:, 0], pair[:, 1], color="#426ca1", s=36, zorder=4)
    middle.annotate("", pair[1], xytext=pair[0], arrowprops={"arrowstyle": "<->", "color": "#426ca1", "lw": 2})
    middle.text(-0.92, 0.11, "fixed diameter", color="#a94712", fontsize=10)
    middle.text(-1.06, -0.82, "Off the diameter:\nan alternating pair", color="#426ca1", fontsize=10)
    middle.set_title("Reflection across v = 0\nInfinitely many fixed points", fontsize=12)

    right.set_facecolor("white")
    right.semilogy(np.arange(11), errors, "o-", color="#147d64", lw=2, markersize=4, label="affine disk map F")
    right.semilogy(np.arange(11), np.ones(11), "s--", color="#426ca1", lw=1.5, markersize=3, label="quarter-turn from (1, 0)")
    right.set(xlabel="iteration k", ylabel="distance to the unique fixed point", xlim=(-0.2, 10.2), ylim=(5e-5, 2))
    right.set_xticks([0, 2, 4, 6, 8, 10])
    right.grid(alpha=0.25)
    right.spines[["top", "right"]].set_visible(False)
    right.set_title("Iteration needs extra information\nF shrinks error by 0.4 each step", fontsize=12)
    right.legend(loc="lower left", fontsize=9, framealpha=1)

    fig.suptitle("Brouwer guarantees existence; iteration can behave very differently", fontsize=16, y=0.96)
    fig.text(0.5, 0.035, "All three maps are continuous and send the closed unit disk into itself.", ha="center", fontsize=11)
    fig.subplots_adjust(left=0.045, right=0.985, top=0.77, bottom=0.19, wspace=0.40)
    fig.savefig("fixed-point-existence-versus-iteration.png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
