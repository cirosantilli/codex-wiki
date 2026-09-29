"""Exact angular integrals for a single rigid collective orientation.

Run from _media; tested with Python 3.14, matplotlib 3.10.7, NumPy 2.3.5.
These curves are a toy model, not data or a spatial ordering calculation.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def response(x):
    theta = 2 * np.pi * np.arange(4096) / 4096
    cosine = np.cos(theta)
    x = np.asarray(x)
    weights = np.exp(x[..., None] * cosine - np.abs(x[..., None]))
    return (weights * cosine).sum(axis=-1) / weights.sum(axis=-1)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), layout="constrained")
    u = np.linspace(-0.4, 0.4, 801)
    for n, color in ((1, "#137b70"), (10, "#2279af"), (100, "#a93226")):
        axes[0].plot(u, response(n * u), lw=2.3, color=color, label=rf"$N={n}$")
    axes[0].axhline(0, color="0.65", lw=0.7)
    axes[0].axvline(0, color="0.65", lw=0.7)
    axes[0].plot(0, 0, "ko", ms=5, zorder=5)
    axes[0].set(xlabel=r"source $u=h/(k_BT)$", ylabel=r"$\langle\cos\theta\rangle$",
                title="Every finite system has zero mean at h = 0", ylim=(-1.05, 1.05))
    axes[0].legend(loc="upper left")
    theta = np.linspace(-np.pi, np.pi, 1001)
    for x, color in ((0, "#137b70"), (1, "#2279af"), (8, "#a93226")):
        weight = np.exp(x * (np.cos(theta) - 1))
        density = weight / np.trapezoid(weight, theta)
        axes[1].plot(theta, density, lw=2.3, color=color, label=rf"$x=Nu={x}$")
    axes[1].set(xlabel=r"collective angle $\theta$", ylabel=r"probability density $p_x(\theta)$",
                title="Fixed positive source selects one direction", xlim=(-np.pi, np.pi))
    axes[1].set_xticks([-np.pi, 0, np.pi], [r"$-\pi$", "0", r"$\pi$"])
    axes[1].legend(loc="upper right")
    fig.suptitle("One rigid orientation: removing the source and taking size to infinity", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
