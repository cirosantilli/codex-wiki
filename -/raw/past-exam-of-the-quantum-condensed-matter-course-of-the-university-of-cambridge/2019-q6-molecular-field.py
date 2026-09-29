"""Original molecular-field self-consistency and onset; write PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib; see root pyproject.toml.
Positive order is solved by bisection; no external data are used.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def order_parameter(temperature):
    if temperature <= 0:
        return 1.
    if temperature >= 1:
        return 0.
    lo, hi = 1e-12, 1.
    for _ in range(80):
        mid = (lo+hi)/2
        if np.tanh(mid/temperature) > mid:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.8), facecolor="white")
    trial = np.linspace(0, 1.15, 700)
    ax = axes[0]
    ax.plot(trial, trial, lw=1.3, ls="--", color="#697781", label=r"$y=m$")
    for temp, color in ((.75, "#1768ab"), (1.3, "#bd6426")):
        ax.plot(trial, np.tanh(trial/temp), color=color, lw=2, label=rf"$\tanh(m/t)$, $t={temp:g}$")
        if temp < 1:
            order = order_parameter(temp)
            ax.scatter([order], [order], s=28, color=color, zorder=3)
    ax.set(xlim=(0, 1.15), ylim=(0, 1.15), xlabel=r"$m$", ylabel=r"$y$")
    ax.set_title("Positive intersection only below the transition", fontsize=10)
    ax.legend(frameon=False, fontsize=9)
    ax = axes[1]
    temperature = np.linspace(0, 1.8, 1000)
    order = np.array([order_parameter(t) for t in temperature])
    near = np.linspace(.88, 1, 300)
    ax.plot(temperature, order, lw=2, color="#1768ab", label="Self-consistent order")
    ax.plot(near, near*np.sqrt(3*(1-near)), ls="--", lw=1.4, color="#bd6426",
            label=r"$t\sqrt{3(1-t)}$ near $t=1$")
    ax.axvline(1, color="#aeb7bf", ls=":", lw=.8)
    ax.set(xlim=(0, 1.8), ylim=(-.04, 1.05), xlabel=r"$t=T/T_C$", ylabel=r"$m=|M|/(n\mu_B)$")
    ax.set_title("Square-root onset of spontaneous magnetization", fontsize=10)
    ax.legend(frameon=False, fontsize=8.5)
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(w_pad=2)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
