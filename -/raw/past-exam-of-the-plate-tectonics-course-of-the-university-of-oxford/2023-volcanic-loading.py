"""Local isostasy and flexural response; Python 3.14.4/NumPy 2.3.5/Matplotlib 3.10.7.

A periodic FFT solves w'''' + w = q for an isolated, smooth, positive load.
Coordinates are nondimensional. The PNG is written to CWD.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def response(x, width):
    q = np.exp(-0.5 * (x / width) ** 2)
    k = 2 * np.pi * np.fft.fftfreq(x.size, d=x[1] - x[0])
    w = np.fft.ifft(np.fft.fft(q) / (1 + k**4)).real
    assert abs(w.sum() - q.sum()) < 1e-9
    return q, w


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    x = np.linspace(-60, 60, 16384, endpoint=False)
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 4.8), dpi=100, sharey=True)
    fig.patch.set_facecolor("white")
    for ax, width, title in zip(axs, [0.6, 5.0], ["Narrow load: strong flexural support", "Broad load: near-local compensation"]):
        q, w = response(x, width)
        ax.set_facecolor("white")
        ax.axhline(0, color="#555555", lw=0.9)
        ax.plot(x, -q, ls="--", color="#ad5b3a", lw=2, label="Local-isostatic deflection")
        ax.plot(x, -w, color="#235b82", lw=2.5, label="Elastic deflection")
        ax.fill_between(x, 0, 0.3*q, facecolor="#d6c1a1", alpha=0.8, label="Load shape (scaled)")
        ax.set(xlim=(-13, 13), ylim=(-1.1, 0.48), xlabel=r"Distance / $(D/\Delta\rho g)^{1/4}$", title=title)
        ax.grid(alpha=0.2)
    axs[0].set_ylabel("Vertical displacement (arbitrary units)")
    axs[0].legend(loc="lower left", fontsize=8.7)
    fig.suptitle("Elastic bending spreads a volcanic load beyond its footprint", fontsize=13, y=0.98)
    fig.text(0.035, 0.025, "Same stiffness and peak load; only load width changes. Positive displacement is upward.", fontsize=9)
    fig.subplots_adjust(left=0.085, right=0.98, top=0.84, bottom=0.17, wspace=0.12)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
