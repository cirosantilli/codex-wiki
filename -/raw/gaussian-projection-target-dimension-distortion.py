"""Generate gaussian-projection-target-dimension-distortion.png in CWD.

Same original cloud as the pairwise plot; fresh independent Gaussian maps at
every dimension and draw, never prefixes of a larger matrix. Tested with
Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

import importlib.util
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


DIMENSIONS = [8, 16, 32, 64, 128]
DRAWS = 48
MAP_ROOT_SEED = 314159


def load_model():
    path = Path(__file__).with_name("johnson-lindenstrauss-pairwise-distance-distortion.py")
    spec = importlib.util.spec_from_file_location("jl_pairwise_model", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sample_errors():
    model = load_model()
    points = model.point_cloud()
    original = model.pair_distances(points)
    seeds = np.random.SeedSequence(MAP_ROOT_SEED).spawn(len(DIMENSIONS) * DRAWS)
    errors = np.empty((len(DIMENSIONS), DRAWS))
    for row, dimension in enumerate(DIMENSIONS):
        for draw in range(DRAWS):
            image = model.gaussian_map(points, dimension, seeds[row * DRAWS + draw])
            ratios = model.pair_distances(image) / original
            errors[row, draw] = np.max(np.abs(ratios - 1))
    return errors


def main():
    errors = sample_errors()
    lower, median, upper = np.quantile(errors, [0.1, 0.5, 0.9], axis=1)
    successes = np.sum(errors <= 0.2, axis=1)
    plt.rcParams.update({"font.size": 11})
    fig, ax = plt.subplots(figsize=(9.2, 5.3), facecolor="white")
    x = np.arange(len(DIMENSIONS))
    offsets = np.linspace(-0.16, 0.16, DRAWS)
    for row in x:
        ax.scatter(row + offsets, errors[row], s=20, color="#2275a5", alpha=0.45,
                   edgecolors="none", label="Each independently drawn map" if row == 0 else None)
    ax.vlines(x, lower, upper, color="#173e58", lw=3, label="Empirical 10th–90th percentiles")
    ax.plot(x, median, "o-", color="#173e58", lw=1.8, label="Empirical median")
    ax.axhline(0.2, ls="--", color="#b66824", label="20% maximum distance error")
    for position, count in zip(x, successes):
        ax.text(position, 1.01, f"{count}/{DRAWS}", transform=ax.get_xaxis_transform(),
                ha="center", fontsize=10, color="#b66824")
    ax.set(xticks=x, xticklabels=DIMENSIONS, xlim=(-0.45, len(x) - 0.55),
           ylim=(0, errors.max() * 1.08), xlabel="Target dimension k (ambient dimension fixed at 512)",
           ylabel="Maximum over all 780 pairs of |distance ratio − 1|")
    ax.set_title("Above each column: draws with every pair within 20%", fontsize=11, pad=27)
    ax.set_facecolor("white")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.18)
    ax.legend(loc="upper right", frameon=False, fontsize=9)
    fig.suptitle("More target dimensions: less distortion, with variation between maps", fontsize=14, y=0.98)
    fig.text(0.5, 0.025,
             "Fixed synthetic cloud • 48 fresh maps per k • PCG64, SeedSequence(314159).spawn(240)\n"
             "Empirical spread across draws; no confidence interval or optimal dimension bound",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=0.1, right=0.98, bottom=0.2, top=0.81)
    fig.savefig("gaussian-projection-target-dimension-distortion.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"root_seed": MAP_ROOT_SEED, "rng": "PCG64", "draws_per_dimension": DRAWS,
                      "independent_child_streams": len(DIMENSIONS) * DRAWS,
                      "dimensions": DIMENSIONS, "distance_tolerance": 0.2,
                      "success_counts": successes.tolist(), "median_max_errors": median.tolist(),
                      "empirical_10th_percentiles": lower.tolist(), "empirical_90th_percentiles": upper.tolist(),
                      "all_max_errors": errors.tolist()}, indent=2))


if __name__ == "__main__":
    main()
