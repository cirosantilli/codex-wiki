"""Generate johnson-lindenstrauss-pairwise-distance-distortion.png in CWD.

Original synthetic data, not physical measurements. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7. The companion dimension plot imports this
model so that the point cloud is identical in both figures.
"""

import json

import matplotlib.pyplot as plt
import numpy as np


POINT_SEED = 20261013
MAP_SEED = 424242
N_POINTS = 40
AMBIENT_DIMENSION = 512
TARGET_DIMENSION = 32


def point_cloud():
    rng = np.random.Generator(np.random.PCG64(POINT_SEED))
    points = rng.standard_normal((N_POINTS, AMBIENT_DIMENSION)) / np.sqrt(AMBIENT_DIMENSION)
    points[np.arange(N_POINTS), np.arange(N_POINTS) // 10] += 2
    return points


def gaussian_map(points, dimension, seed):
    rng = np.random.Generator(np.random.PCG64(seed))
    matrix = rng.standard_normal((dimension, points.shape[1])) / np.sqrt(dimension)
    return points @ matrix.T


def pair_distances(points):
    i, j = np.triu_indices(len(points), 1)
    return np.linalg.norm(points[i] - points[j], axis=1)


def main():
    points = point_cloud()
    original = pair_distances(points)
    projected = pair_distances(gaussian_map(points, TARGET_DIMENSION, MAP_SEED))
    ratios = projected / original
    assert len(ratios) == 780 and np.all(original > 0)

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.9), facecolor="white")
    ax = axes[0]
    ax.scatter(original, projected, s=13, alpha=0.5, color="#2275a5", edgecolors="none")
    limit = max(original.max(), projected.max()) * 1.09
    line = np.array([0, limit])
    ax.plot(line, line, color="#31373b", lw=1.5, label="Unchanged distance")
    ax.plot(line, 0.8 * line, ls="--", color="#b66824", label="Illustrative ±20% distance band")
    ax.plot(line, 1.2 * line, ls="--", color="#b66824")
    ax.set(xlim=(0, limit), ylim=(0, limit), xlabel="Original Euclidean distance (512 coordinates)",
           ylabel="Projected Euclidean distance (32 coordinates)", title="All 780 unordered pairs; one Gaussian map")
    ax.set_aspect("equal", adjustable="box")
    ax.legend(loc="upper left", fontsize=8, frameon=False)

    ax = axes[1]
    ax.hist(ratios, bins=28, color="#2275a5", edgecolor="white", linewidth=0.5)
    ax.axvline(1, color="#31373b", lw=1.5)
    for value in [0.8, 1.2]:
        ax.axvline(value, color="#b66824", ls="--")
    ax.set(xlabel="Projected distance / original distance", ylabel="Number of pairs",
           title="Distance ratios, not squared-distance ratios")
    ax.text(0.98, 0.96, f"Observed range: {ratios.min():.3f}–{ratios.max():.3f}\n"
            f"Largest relative error: {np.max(np.abs(ratios - 1)):.3f}",
            transform=ax.transAxes, ha="right", va="top", fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.92})
    for ax in axes:
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.16)
        ax.set_axisbelow(True)
    fig.suptitle("A fixed 40-point cloud projected from 512 to 32 dimensions", fontsize=15)
    fig.text(0.5, 0.025, "Synthetic example • PCG64: point seed 20261013, map seed 424242 • T = G / √32",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.85, wspace=0.3)
    fig.savefig("johnson-lindenstrauss-pairwise-distance-distortion.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"point_seed": POINT_SEED, "map_seed": MAP_SEED, "rng": "PCG64",
                      "n": N_POINTS, "D": AMBIENT_DIMENSION, "k": TARGET_DIMENSION,
                      "pairs": len(ratios), "distance_ratio_min": float(ratios.min()),
                      "distance_ratio_max": float(ratios.max()),
                      "squared_distance_ratio_min": float((ratios ** 2).min()),
                      "squared_distance_ratio_max": float((ratios ** 2).max()),
                      "max_relative_distance_error": float(np.max(np.abs(ratios - 1))),
                      "max_relative_squared_distance_error": float(np.max(np.abs(ratios ** 2 - 1))),
                      "distance_band_success": bool(np.all(np.abs(ratios - 1) <= 0.2))}, indent=2))


if __name__ == "__main__":
    main()
