"""Endpoint-to-interior-saddle transition; write an opaque PNG in cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.legendre import leggauss


def main():
    nodes, weights = leggauss(300)
    s = 5 * (nodes + 1)
    weights = 5 * weights
    ell = np.linspace(-4, 4, 321)
    c = np.cbrt(2)
    canonical = np.exp(-c * ell[:, None] * s - s**3 / 3) @ weights
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.3), dpi=100, facecolor="white")
    axes[0].semilogy(ell, canonical, color="#222222", lw=2.5, label="Uniform cubic integral")
    for nu, color in [(32, "#d87922"), (128, "#1766aa"), (512, "#38966b")]:
        a = 1 + ell[:, None] * nu ** (-2 / 3)
        t = c * nu ** (-1 / 3) * s
        phase = nu * ((a - 1) * t + a * (np.sinh(t) - t))
        scaled = np.exp(-phase) @ weights
        axes[0].semilogy(ell, scaled, color=color, lw=1.6, label=fr"Exact integral, $\nu={nu}$")
        axes[1].plot(ell, scaled / canonical, color=color, lw=2, label=fr"$\nu={nu}$")
    axes[1].axhline(1, color="0.4", ls="--", lw=1.2)
    axes[0].set(ylabel=r"Scaled integral $\nu^{1/3}A_\nu/2^{1/3}$",
                title="One formula connects three asymptotic regimes")
    axes[1].set(ylabel="Exact integral / uniform approximation",
                title="Convergence at fixed transition parameter")
    for ax in axes:
        ax.set_xlabel(r"Transition parameter $l$: $a=1+l\nu^{-2/3}$")
        ax.set_xlim(-4, 4)
        ax.grid(alpha=.2)
        ax.axvline(0, color="0.65", ls=":", lw=1)
        ax.legend(frameon=False, fontsize=9)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
