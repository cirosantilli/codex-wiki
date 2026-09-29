"""Draw analytical finite-bath and fixed-bath histories; Python 3.14,
NumPy 2.3.5, Matplotlib 3.10.7. Run from the image output directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    t = np.linspace(0, 240, 600)
    t1 = 296 + 54 * np.exp(-t / 45)
    t2 = 296 - 6 * np.exp(-t / 45)
    ideal = 290 + 60 * np.exp(-t / 50)
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.8, 4.8),
                                    facecolor="white")
    fig.suptitle("Newton cooling model: finite bath versus fixed bath", fontsize=15, y=0.97)
    left.plot(t, t1, color="#b64e24", lw=2.5, label="Finite bath: τ = 45 s")
    left.plot(t, ideal, color="#333333", lw=2, ls="--",
              label="Fixed bath: τ = 50 s")
    left.axhline(296, color="#b64e24", lw=1, ls=":")
    left.axhline(290, color="#333333", lw=1, ls=":")
    left.text(155, 299, "Finite endpoint: 296 K", color="#b64e24", fontsize=10)
    left.text(155, 286.8, "Fixed endpoint: 290 K", color="#333333", fontsize=10)
    left.set(title="Body 1 cooling", ylabel="Body 1 temperature (K)", ylim=(285, 355))
    right.plot(t, t2, color="#176aa0", lw=2.5, label="Finite bath warms")
    right.plot(t, np.full_like(t, 290), color="#333333", lw=2, ls="--",
               label="Ideal bath stays fixed")
    right.axhline(296, color="#176aa0", lw=1, ls=":")
    right.text(135, 295.3, "Finite endpoint: 296 K", color="#176aa0", fontsize=10)
    right.text(135, 289.5, "Fixed endpoint: 290 K", color="#333333", fontsize=10)
    right.set(title="Bath 2 response (expanded scale)",
              ylabel="Bath 2 temperature (K)", ylim=(289, 297))
    right.set_yticks([290, 292, 294, 296])
    for ax in (left, right):
        ax.set(xlabel="Time (s)", xlim=(0, 240))
        ax.set_xticks([0, 45, 90, 150, 240])
        ax.grid(alpha=0.18)
        ax.legend(loc="upper right", fontsize=10, frameon=False)
    right.legend(loc="lower right", bbox_to_anchor=(1, 0.18), fontsize=10, frameon=False)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.20, top=0.84, wspace=0.27)
    fig.text(0.5, 0.025, "Model predictions, not observations • G = 2 W/K • C₁ = 100 J/K • C₂ = 900 J/K",
             ha="center", fontsize=10, color="#444444")
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
