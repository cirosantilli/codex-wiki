"""Original reciprocal thin-screen example, with unwrapped spatial phases.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from the output directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    xi = np.linspace(-1, 1, 501)
    phase = np.pi * (0.5 * xi**2 + 0.25 * xi**3)
    blue, orange, green = "#2463a8", "#bb4d12", "#168064"
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), sharex=True, sharey=True)
    axes[0].plot(xi, phase / np.pi, color=blue, lw=2.5, label="Outward: ψ")
    axes[0].plot(xi, -phase / np.pi, color=green, lw=2.5, ls="--",
                 label="Just after conjugation: −ψ")
    axes[0].set_title("At the return surface")
    axes[1].plot(xi, 2 * phase / np.pi, color=orange, lw=2.5,
                 label="Ordinary mirror: 2ψ")
    axes[1].plot(xi, np.zeros_like(xi), color=green, lw=3,
                 label="Conjugate mirror: 0")
    axes[1].set_title("After the second plate passage")
    for ax in axes:
        ax.set(xlim=(-1, 1), ylim=(-0.85, 1.65), xlabel="Transverse position ξ = x/a")
        ax.set_yticks([-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5])
        ax.grid(alpha=0.18)
        ax.legend(loc="upper center", fontsize=10, framealpha=1)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Unwrapped phase / π")
    fig.suptitle(r"A reciprocal plate adds ψ = πξ²/2 + πξ³/4 on each passage", fontsize=14)
    fig.text(0.5, 0.075, "Flat input • Lossless stationary screen • Corresponding transverse positions • Constant mirror phase omitted",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.21, top=0.81, wspace=0.13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
