"""Drude conductivity and real-time lag; Python 3.14 and pinned repo libraries.

Run from _media; the PNG is written to the working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def conductivity(x):
    """sigma/sigma_0, with physical fields Re[E_hat exp(-i omega t)]."""
    return 1 / (1 - 1j * np.asarray(x))


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    x = np.logspace(-2, 2, 900)
    s = conductivity(x)
    fig, (value, lag) = plt.subplots(1, 2, figsize=(10, 4.7), layout="constrained")
    fig.suptitle(r"Drude frequency response: $\sigma(\omega)=\sigma_0/(1-i\omega\tau)$", fontsize=15)
    value.semilogx(x, s.real, color="#1263a0", lw=2.5, label=r"$\mathrm{Re}\,\sigma/\sigma_0$")
    value.semilogx(x, s.imag, color="#b24720", lw=2.5, label=r"$\mathrm{Im}\,\sigma/\sigma_0$")
    value.semilogx(x, np.abs(s), color="#297343", lw=2, ls="--", label=r"$|\sigma|/\sigma_0$")
    value.scatter([1, 1], [0.5, 2**-0.5], color=["#1263a0", "#297343"], zorder=3)
    value.text(1.5, 0.56, r"$\omega\tau=1$: components $=1/2$", fontsize=10)
    value.set(ylabel="normalized conductivity", ylim=(0, 1.08))
    value.legend(loc="upper right", fontsize=10)
    lag.semilogx(x, np.degrees(np.angle(s)), color="#7b4397", lw=2.5)
    lag.scatter([1], [45], color="#7b4397", zorder=3)
    lag.annotate(r"$45^\circ$", xy=(1, 45), xytext=(0.07, 62),
                 arrowprops={"arrowstyle": "->", "color": "#7b4397"})
    lag.text(0.025, 82, r"$J_x\propto\cos(\omega t-\phi)$", fontsize=12)
    lag.set(ylabel=r"current lag $\phi=\arctan(\omega\tau)$ (degrees)",
            ylim=(0, 95), yticks=[0, 30, 45, 60, 90])
    for ax in (value, lag):
        ax.set(xlim=(0.01, 100), xlabel=r"angular frequency $\omega\tau$")
        ax.axvline(1, color="#aaaaaa", ls=":", lw=1)
        ax.grid(alpha=0.18)
    fig.text(0.5, -0.025, r"Convention: $\mathrm{Re}[\widehat E e^{-i\omega t}]$. Exact model curves; no measured data.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
