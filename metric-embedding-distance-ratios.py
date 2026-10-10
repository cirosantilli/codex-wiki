"""Draw metric-embedding-distance-ratios.png in the current working directory.

Uses the repository's NumPy/Matplotlib environment; tested with Python 3.14.4.
Every unordered pair of the four corners is checked before plotting.
"""

from itertools import combinations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def distance_ratios(points, image, pairs):
    return np.array([
        np.linalg.norm(image[j] - image[i]) / np.linalg.norm(points[j] - points[i])
        for i, j in pairs
    ])


def main():
    points = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float)
    labels = "ABCD"
    pairs = list(combinations(range(4), 2))
    images = [points, 3 * points, points * [2, 1]]
    ratios = [distance_ratios(points, image, pairs) for image in images]
    assert len(pairs) == 6
    assert np.allclose(ratios[0], 1)
    assert np.allclose(ratios[1], 3)
    assert np.allclose(ratios[2], [2, np.sqrt(2.5), 1, 1, np.sqrt(2.5), 2])
    assert np.allclose([r.max() / r.min() for r in ratios], [1, 1, 2])

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig = plt.figure(figsize=(11, 6.9), facecolor="white")
    grid = fig.add_gridspec(2, 3, height_ratios=[1.05, 1], hspace=0.65)
    colors = ["#296b91", "#65944b", "#bd602d"]
    titles = ["Original square", "Uniform: f(x, y) = (3x, 3y)", "Anisotropic: f(x, y) = (2x, y)"]
    offsets = [(-11, -13), (9, -13), (9, 7), (-11, 7)]
    for column, (image, color, title) in enumerate(zip(images, colors, titles)):
        ax = fig.add_subplot(grid[0, column])
        for i, j in pairs:
            ax.plot(image[[i, j], 0], image[[i, j], 1], color=color,
                    lw=1.8, ls="--" if j - i == 2 else "-", alpha=0.8)
        ax.scatter(image[:, 0], image[:, 1], color=color, s=35, zorder=3)
        for label, point, offset in zip(labels, image, offsets):
            ax.annotate(label, point, xytext=offset, textcoords="offset points")
        # Identical bounds and equal aspect make the overall rescaling visible.
        ax.set(xlim=(-0.4, 3.4), ylim=(-0.4, 3.4), xticks=[0, 1, 2, 3], yticks=[0, 1, 2, 3])
        ax.set_aspect("equal")
        ax.set_title(title, pad=14)
        ax.set_xlabel("x")
        ax.set_ylabel("y", rotation=0, labelpad=10)
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)

    ax = fig.add_subplot(grid[1, :])
    positions = np.arange(len(pairs))
    for shift, r, color, name in zip([-0.23, 0, 0.23], ratios, colors,
                                    ["Original: distortion 1", "Uniform: distortion 1", "Anisotropic: distortion 2"]):
        ax.bar(positions + shift, r, width=0.22, color=color, label=name)
    for p, r in zip(positions, ratios[2]):
        value = r"$\sqrt{5/2}$" if np.isclose(r, np.sqrt(2.5)) else str(int(r))
        ax.text(p + 0.23, r + 0.07, value, ha="center", color=colors[2], fontsize=10)
    ax.set(xticks=positions, xticklabels=[labels[i] + labels[j] for i, j in pairs],
           ylim=(0, 3.7), ylabel="Image distance / original distance", xlabel="All six unordered pairs")
    ax.set_title("A common multiplier changes the ratios together; distortion is max / min", pad=12)
    ax.grid(axis="y", alpha=0.2)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper center", ncol=3, frameon=False, fontsize=10)
    fig.suptitle("Metric embeddings: scale versus distortion", fontsize=18, y=0.985)
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.09, top=0.88, wspace=0.3)
    fig.savefig("metric-embedding-distance-ratios.png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
