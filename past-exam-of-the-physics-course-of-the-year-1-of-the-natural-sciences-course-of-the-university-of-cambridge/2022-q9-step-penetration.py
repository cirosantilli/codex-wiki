"""Original matched potential-step state. Python 3.14.4; root pyproject.toml deps.

Choose E=V0/2, k=kappa, incoming amplitude 1; xi=kappa*x.
Run from the desired output directory; writes the PNG basename into cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    xi = np.linspace(-9, 4, 2001)
    # r=-i, t=1-i; both psi and psi' agree at the interface.
    psi = np.where(xi <= 0, np.exp(1j*xi) - 1j*np.exp(-1j*xi), (1-1j)*np.exp(-xi))
    fig, axes = plt.subplots(1, 2, figsize=(10.1, 4.3), layout="constrained")
    fig.patch.set_facecolor("white")
    ax = axes[0]
    ax.plot(xi, psi.real, label=r"$\operatorname{Re}\psi$", color="#205b9e", lw=2)
    ax.plot(xi, psi.imag, label=r"$\operatorname{Im}\psi$", color="#bf5b1d", ls="--", lw=2)
    ax.set(xlim=(-9, 4), ylim=(-1.8, 1.8), xlabel=r"Position $\xi=\kappa x$", ylabel="Wavefunction / incident amplitude", title=r"Matched state: $E=V_0/2$, $k=\kappa$")
    ax.axhline(0, color="0.6", lw=0.7)
    ax.legend(loc="lower left")
    x = np.linspace(0, 3, 501)
    ax = axes[1]
    ax.plot(x, np.exp(-2*x), color="#205b9e", lw=2, label=r"$|\psi(x)|^2/|\psi(0)|^2=e^{-2\kappa x}$")
    ax.axhline(1/np.e, color="0.4", ls=":")
    ax.axvline(0.5, color="0.4", ls=":")
    ax.plot(0.5, 1/np.e, "o", color="#bf5b1d")
    ax.text(0.62, 0.43, r"$x=1/(2\kappa)$" + "\nDensity has fallen to $1/e$")
    ax.set(xlim=(0, 3), ylim=(0, 1.05), xlabel=r"Position $\xi=\kappa x$", ylabel="Relative probability density", title="Probability density decays twice as fast")
    ax.legend(loc="upper right", fontsize=9)
    for ax in axes:
        ax.set_facecolor("white")
        ax.axvline(0, color="0.25", lw=1)
        ax.axvspan(0, ax.get_xlim()[1], color="#f0d791", alpha=0.23, zorder=-2)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.15)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
