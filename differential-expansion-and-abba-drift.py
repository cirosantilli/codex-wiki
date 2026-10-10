"""Original stipulated rod and ABBA drift examples; no historical data.

Run from the desired output directory. Output has this script's basename.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.6), dpi=110, facecolor="white")
    fig.suptitle("Relative length and drift cancellation: chosen models", fontsize=16)
    theta = np.linspace(0, 10, 201)
    ax = axes[0]
    ax.plot(theta, theta, label="Test: +1 μm/K", color="#b44c30", lw=2.4)
    ax.plot(theta, 9 * theta, label="Reference: +9 μm/K", color="#2f698b", lw=2.4)
    ax.plot(theta, -8 * theta, label="Test − reference: −8 μm/K", color="#71438e", lw=2.4)
    ax.axhline(0, color="#777777", lw=.8)
    ax.set(xlabel="Temperature increase (K)", ylabel="Length change from initial value (μm)",
           title="Both rods expand; their difference falls")
    ax.legend(fontsize=10, loc="upper left")
    ax.grid(alpha=.2)
    ax.text(.04, .05, "L₀ = 1 m; coefficients stipulated\nNot historical material measurements", transform=ax.transAxes, fontsize=10)
    ax = axes[1]
    t = np.linspace(0, 3, 201)
    ti = np.arange(4)
    affine = 2 + 3 * t
    curved = affine + .5 * t**2
    ax.plot(t, affine, color="#2f698b", lw=2.4, label="Drift 2 + 3t")
    ax.plot(t, curved, color="#b44c30", lw=2.4, label="Drift 2 + 3t + 0.5t²")
    for i, letter in enumerate("ABBA"):
        ax.scatter(i, 2 + 3*i, color="#2f698b", s=48, zorder=3)
        ax.scatter(i, 2 + 3*i + .5*i*i, color="#b44c30", s=48, zorder=3)
        ax.text(i, 2 + 3*i + .5*i*i + .6, letter, ha="center", fontsize=12)
    affine_contrast = np.dot([-1, 1, 1, -1], 2 + 3*ti) / 2
    curved_contrast = np.dot([-1, 1, 1, -1], 2 + 3*ti + .5*ti**2) / 2
    assert abs(affine_contrast) < 1e-12
    assert abs(curved_contrast + 1) < 1e-12
    ax.set(xlabel="Time / chosen reading interval", ylabel="Instrument drift (μm)",
           title="ABBA rejects affine drift, not curvature", xticks=ti)
    ax.text(.04, .72, "Drift contribution to B − A:\nlinear: 0 μm; curved: −1 μm", transform=ax.transAxes, fontsize=10)
    ax.legend(fontsize=10, loc="lower right")
    ax.grid(alpha=.2)
    fig.tight_layout(rect=(0, .02, 1, .94), w_pad=2)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
