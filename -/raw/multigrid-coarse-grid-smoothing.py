"""Original analytic Poisson diagram; write the PNG basename to CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
The curves are mathematical constructions, not experimental measurements.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    n = 63
    x = np.arange(n + 2) / (n + 1)
    k = np.arange(1, n + 1)
    mu = 1 - (4 / 3) * np.sin(k * np.pi / (2 * (n + 1))) ** 2
    plain = np.cos(k * np.pi / (n + 1))
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(10, 7.2), layout="constrained")
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.12])
    colors = {"before": "#858d98", "weighted": "#166b9a", "plain": "#b34b19"}
    for col, mode in enumerate([1, 63]):
        ax = fig.add_subplot(gs[0, col])
        w = np.sin(mode * np.pi * x)
        w[[0, -1]] = 0
        ax.plot(x, w, color=colors["before"], lw=1.1, label="Initial error")
        ax.plot(x, mu[mode - 1] ** 4 * w, color=colors["weighted"], lw=2,
                marker=".", ms=3, label=r"4 sweeps, $\omega=2/3$")
        ax.plot(x, plain[mode - 1] ** 4 * w, color=colors["plain"], lw=1.4,
                ls="--", label=r"4 sweeps, $\omega=1$")
        ax.axhline(0, color="#cccccc", lw=0.6)
        ax.set(xlim=(0, 1), ylim=(-1.12, 1.12), xlabel="Position x",
               ylabel="Signed error amplitude",
               title=(("Lowest sine mode: k = 1" if mode == 1 else
                       "Nearly alternating sine mode: k = 63") +
                      f"\nWeighted amplitude retained: {abs(mu[mode-1])**4:.2%}"))
        ax.legend(loc="lower left", fontsize=9, framealpha=1)
    ax = fig.add_subplot(gs[1, :])
    freq = k / (n + 1)
    ax.axvspan(0.5, 1, facecolor="#e7f1f6", label="High-frequency half")
    ax.plot(freq, abs(plain), color=colors["plain"], lw=2, ls="--",
            label=r"Plain Jacobi: $|\cos(k\pi/64)|$")
    ax.plot(freq, abs(mu), color=colors["weighted"], lw=2, marker=".", ms=3,
            label=r"Weighted Jacobi: $|1-\frac{4}{3}\sin^2(k\pi/128)|$")
    ax.axhline(1 / 3, color="#647887", lw=1, ls=":")
    ax.text(0.99, 0.36, "Weighted high-frequency bound: 1/3", fontsize=10, ha="right")
    ax.set(xlim=(0, 1), ylim=(0, 1.07), xlabel=r"Normalized sine frequency $k/(n+1)$",
           ylabel="Magnitude retained per sweep",
           title="One-sweep attenuation: convergence and smoothing are different")
    ax.legend(loc="upper center", fontsize=9, framealpha=1)
    fig.suptitle("Multigrid smoothing on the 1D Dirichlet Poisson model", fontsize=16)
    fig.supxlabel("Analytic model • n = 63, h = 1/64 • nodes joined for visibility • no measured data",
                  fontsize=10)
    out = Path(Path(__file__).stem + ".png")
    fig.savefig(out, dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
