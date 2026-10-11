"""NST IB 2023 paper 2 Q5: plot the signal; write the PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib; dependencies are in pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    decay = 0.3
    t = np.linspace(-4.5 * np.pi, 4.5 * np.pi, 3000)
    envelope = np.exp(-decay * np.abs(t))
    signal = envelope * np.cos(np.where(t < 0, 2 * t, t))
    fig, ax = plt.subplots(figsize=(9.2, 3.5), facecolor="white")
    ax.set_facecolor("white")
    ax.plot(t, signal, color="#1768ab", lw=2, label=r"Signal ($\lambda=0.3$)")
    ax.plot(t, envelope, color="#a66b29", lw=1.1, ls="--", label="Envelopes")
    ax.plot(t, -envelope, color="#a66b29", lw=1.1, ls="--")
    ax.axhline(0, color="#aeb6c0", lw=0.7)
    ax.axvline(0, color="#aeb6c0", lw=0.8, ls=":")
    ax.text(-7, 0.78, r"Incoming: angular frequency $2$", ha="center", fontsize=10)
    ax.text(7, 0.78, r"Outgoing: angular frequency $1$", ha="center", fontsize=10)
    ax.set(ylim=(-1.12, 1.12), xlim=(t[0], t[-1]), xlabel=r"Time $t$", ylabel=r"$f(t)$")
    ax.set_xticks(np.arange(-4, 5, 2) * np.pi,
                  [r"$-4\pi$", r"$-2\pi$", "$0$", r"$2\pi$", r"$4\pi$"])
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="lower right", fontsize=9, frameon=False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
