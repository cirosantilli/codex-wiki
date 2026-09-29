"""Original condensate-mode comparison, with output PNG written to cwd."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    beta = gamma = 1.0
    k0 = 1.0
    omega = np.sqrt(k0**4 + 2 * beta * k0**2)
    tau = np.linspace(0, 2 * np.pi, 500)
    density_amplitude = 0.14
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.9), dpi=120,
                             facecolor="white")
    ax = axes[0]
    real = 1 + density_amplitude * np.cos(tau) / 2
    imag = -omega * density_amplitude * np.sin(tau) / (2 * k0**2)
    ax.plot(real, imag, color="#1c67a0", lw=2,
            label="First order: coupled")
    ax.plot([.91, 1.09], [0, 0], color="#c35724", lw=2.5,
            label="Second order: amplitude")
    angle = np.linspace(-.13, .13, 180)
    ax.plot(np.cos(angle), np.sin(angle), "--", color="#27834a", lw=2,
            label="Second order: phase")
    ax.scatter([1], [0], color="black", s=15, zorder=5)
    ax.text(1.005, -.025, r"$\psi_0=1$", fontsize=9)
    ax.set(xlim=(.82, 1.18), ylim=(-.18, .18), aspect="equal",
           xlabel=r"$\mathrm{Re}\,\psi$", ylabel=r"$\mathrm{Im}\,\psi$",
           title="Small motion about equilibrium")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.24),
              fontsize=8, frameon=False)
    k = np.linspace(0, 2, 500)
    axes[1].plot(k, np.sqrt(k**4 + 2 * beta * k**2),
                 color="#1c67a0", lw=2, label="One positive branch")
    axes[1].plot(k, np.sqrt(2 * beta) * k, ":", color="#56606b", lw=1.3,
                 label="Small-k sound limit")
    axes[1].set(title="First-order time dynamics", xlabel=r"$|k|$",
                ylabel=r"$\omega$", xlim=(0, 2), ylim=(0, 5.1))
    axes[1].legend(loc="upper left", fontsize=8, frameon=False)
    axes[2].plot(k, np.sqrt((k**2 + 2 * beta) / gamma),
                 color="#c35724", lw=2, label="Amplitude")
    axes[2].plot(k, k / np.sqrt(gamma), "--", color="#27834a", lw=2,
                 label="Phase")
    axes[2].set(title="Second-order time dynamics", xlabel=r"$|k|$",
                ylabel=r"$\omega$", xlim=(0, 2), ylim=(0, 2.7))
    axes[2].legend(loc="upper left", fontsize=8, frameon=False)
    for ax in axes:
        ax.grid(alpha=.18)
    fig.suptitle(r"Condensate amplitude and phase: $\beta=\gamma=1$", fontsize=14)
    fig.subplots_adjust(left=.065, right=.985, bottom=.28, top=.79, wspace=.4)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
