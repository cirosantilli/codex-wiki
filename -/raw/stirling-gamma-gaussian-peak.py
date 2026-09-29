"""Peak-height-normalized factorial integrands, not probability densities.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7. Output to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def kernel(s, n):
    s = np.asarray(s, dtype=float)
    out = np.zeros_like(s)
    inside = s > -np.sqrt(n)
    z = s[inside] / np.sqrt(n)
    out[inside] = np.exp(n * (np.log1p(z) - z))
    return out


def main():
    s = np.linspace(-4.5, 5, 1500)
    fig, ax = plt.subplots(figsize=(8.2, 4.8), dpi=130)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    for n, color in [(4, "#ba5524"), (16, "#2768a6"), (64, "#238367")]:
        assert kernel([0], n)[0] == 1
        ax.plot(s, kernel(s, n), color=color, lw=2.1, label=f"n = {n}")
    ax.plot(s, np.exp(-s**2 / 2), color="#222222", ls="--", lw=2.1,
            label=r"Gaussian peak $e^{-s^2/2}$")
    ax.axvline(0, color="#aaaaaa", lw=1, zorder=0)
    ax.set(xlim=(-4.5, 5), ylim=(-0.015, 1.08),
           xlabel=r"Rescaled position $s=(t-n)/\sqrt{n}$",
           ylabel=r"Rescaled integrand $K_n(s)$ (peak height 1)",
           title="The factorial integral develops a Gaussian-shaped peak")
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    ax.grid(alpha=0.15)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
