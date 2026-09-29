"""Generate brownian-paths-scaling.png in the caller's working directory.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Only finite Gaussian grid samples are generated; segments are interpolation.
Run from _media: MPLCONFIGDIR=/tmp/brownian-mpl python3 ../brownian-paths-scaling.py
"""

from math import erf, sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    seed = 20261010
    rng = np.random.default_rng(seed)
    horizon, n, c = 4.0, 4096, 4.0
    times = np.linspace(0.0, horizon, n + 1)
    increments = rng.normal(0.0, sqrt(horizon / n), size=(4, n))
    paths = np.column_stack((np.zeros(4), np.cumsum(increments, axis=1)))
    scaled_times, scaled_paths = times / c, paths / sqrt(c)
    assert np.allclose(np.diff(scaled_paths), increments / sqrt(c))
    assert np.isclose((horizon / n) / c, scaled_times[1])

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), dpi=120,
                             facecolor="white")
    colors = ["#2878ad", "#c05a2a", "#24805e", "#8655a4"]
    for ax, t, samples in zip(axes, [times, scaled_times], [paths, scaled_paths]):
        ax.set_facecolor("white")
        for sample, color in zip(samples, colors):
            ax.plot(t, sample, color=color, lw=1.0)
        ax.plot(t, np.sqrt(t), "--", color="#333333", lw=1.25,
                label=r"Pointwise SD guides: $\pm\sqrt{t}$")
        ax.plot(t, -np.sqrt(t), "--", color="#333333", lw=1.25)
        ax.axhline(0, color="#bbbbbb", lw=0.7)
        ax.set_xlim(0, t[-1])
        ax.set_xlabel("Time t")
        ax.grid(alpha=0.16)
    axes[0].set(title=r"Four sampled paths $B_t$ on [0, 4]", ylabel=r"$B_t$")
    axes[1].set(title=r"Rescaled samples $B_{4t}/2$ on [0, 1]",
                ylabel=r"$B_{4t}/2$")
    low = min(paths.min(), -sqrt(horizon)) - 0.15
    high = max(paths.max(), sqrt(horizon)) + 0.15
    axes[0].set_ylim(low, high)
    axes[1].set_ylim(low / sqrt(c), high / sqrt(c))
    axes[0].legend(loc="lower left", fontsize=9, framealpha=0.95)
    fig.suptitle("Brownian scaling: time divided by 4, displacement divided by 2")
    fig.text(0.5, 0.025,
             f"Seed {seed}; 4,096 independent Gaussian increments per path. "
             "Connecting lines interpolate a finite grid.",
             ha="center", fontsize=9)
    fig.tight_layout(rect=(0, 0.055, 1, 0.94))
    fig.savefig(Path.cwd() / "brownian-paths-scaling.png", facecolor="white",
                transparent=False)
    plt.close(fig)

    phi = lambda z: (1.0 + erf(z / sqrt(2.0))) / 2.0
    print(f"P(|B_4| <= 1) = {2 * phi(0.5) - 1:.10f}")
    print(f"P(B_4 > 2) = {1 - phi(1):.10f}")
    print(f"P(|B_1| <= 1) = {2 * phi(1) - 1:.10f}")
    print("Increment SDs for h=1, 0.01, 0.0001: 1, 0.1, 0.01")
    print("Difference quotient SDs for those h: 1, 10, 100")
    print(f"Cov(B_1,B_4)=1; Corr(B_1,B_4)={1/sqrt(4):.1f}")
    assert abs((2 * phi(0.5) - 1) - 0.38292492254802624) < 1e-14
    assert abs((1 - phi(1)) - 0.15865525393145707) < 1e-14


if __name__ == "__main__":
    main()
