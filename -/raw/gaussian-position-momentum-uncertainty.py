"""Plot probability densities, not amplitudes; save the basename PNG in CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dimensionless X=x/L and P=pL/hbar have [X,P]=i (effective hbar=1).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def density(q, width):
    return np.exp(-0.5 * (q / width) ** 2) / (np.sqrt(2 * np.pi) * width)


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.9), dpi=100)
    position = np.linspace(-6, 6, 2401)
    momentum = np.linspace(-3, 3, 2401)
    for sigma, color in zip((0.5, 1, 2), ("#b5531d", "#246bce", "#39834b")):
        label = rf"$\Delta X={sigma:g},\ \Delta P={1 / (2 * sigma):g}$"
        axes[0].plot(position, density(position, sigma), color=color, lw=2.5, label=label)
        axes[1].plot(momentum, density(momentum, 1 / (2 * sigma)), color=color, lw=2.5, label=label)
    axes[0].set(xlim=(-6, 6), ylim=(0, 0.87), xlabel=r"Position $X=x/L$ (dimensionless)",
                ylabel=r"Probability density $|\psi_X(X)|^2$ (per unit $X$)")
    axes[1].set(xlim=(-3, 3), ylim=(0, 1.74), xlabel=r"Momentum $P=pL/\hbar$ (dimensionless)",
                ylabel=r"Probability density $|\widetilde\psi_P(P)|^2$ (per unit $P$)")
    axes[0].set_title("Position densities", fontsize=13)
    axes[1].set_title("Momentum densities", fontsize=13)
    for ax in axes:
        ax.grid(alpha=0.17)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(frameon=False, fontsize=10, loc="upper right")
    fig.suptitle(r"Gaussian preparations: $\Delta X\,\Delta P=1/2$ in every case", fontsize=16, weight="bold", y=0.98)
    fig.text(0.5, 0.035, r"Effective $\hbar=1$. Same colors identify the same preparation; each full density has area 1.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.085, right=0.975, bottom=0.17, top=0.80, wspace=0.30)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
