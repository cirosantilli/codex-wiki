"""Original equal-rms model comparison; no experimental data.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def sphere_form_factor(x):
    x = np.asarray(x, dtype=float)
    result = np.empty_like(x)
    small = np.abs(x) < 0.05
    y = x[small] ** 2
    result[small] = 1 - y / 10 + y**2 / 280 - y**3 / 15120
    z = x[~small]
    result[~small] = 3 * (np.sin(z) - z * np.cos(z)) / z**3
    return result


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    x = np.linspace(0, 10, 2401)
    sphere = sphere_form_factor(x)
    gaussian = np.exp(-x*x/10)
    first_zero = 4.493409457909064
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), layout="constrained", facecolor="white")
    colors = ("#236aaf", "#ca6730")
    for ax in axes:
        ax.set(xlim=(0, 10), xlabel=r"$x=qR$ (dimensionless)")
        ax.grid(alpha=0.2)
        ax.axvline(first_zero, color="#65727b", linewidth=1, linestyle=":")
    axes[0].plot(x, sphere, color=colors[0], label="Uniform sphere")
    axes[0].plot(x, gaussian, color=colors[1], linestyle="--", label="Gaussian, same rms radius")
    axes[0].axhline(0, color="#65727b", linewidth=0.7)
    axes[0].set(ylim=(-0.16, 1.08), ylabel=r"Charge form factor $F(q)$", title="Same initial curvature, different shapes")
    axes[0].legend(loc="upper right", frameon=False, fontsize=10)
    axes[0].annotate(r"First zero: $qR=4.4934\ldots$", xy=(first_zero, 0),
                     xytext=(2.2, 0.35), arrowprops={"arrowstyle": "->", "color": "#65727b"}, fontsize=10)
    axes[0].text(0.45, -0.115, r"$\langle r^2\rangle=3R^2/5$ for both models", fontsize=10)
    axes[1].semilogy(x, sphere**2, color=colors[0])
    axes[1].semilogy(x, gaussian**2, color=colors[1], linestyle="--")
    axes[1].set(ylim=(1e-7, 1.3), ylabel=r"Born charge factor $|F(q)|^2$", title="Diffraction minima distinguish the models")
    axes[1].text(0.5, 3e-7, "Exact sphere zeros lie below the log scale", fontsize=9, color="#47545f")
    fig.suptitle("Calculated models only: a uniform sphere and a smooth Gaussian charge cloud", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
