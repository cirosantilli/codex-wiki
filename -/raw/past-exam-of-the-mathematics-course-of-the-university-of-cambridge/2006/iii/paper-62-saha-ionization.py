"""Hydrogen-only Saha curve: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.

Writes an opaque PNG basename to the caller's CWD. Honors MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ETA = 5.36e-10
M_E = 511000.0
IONIZATION_ENERGY = 13.6
ZETA_THREE = 1.202056903159594


def ionized_fraction(temperature):
    temperature = np.asarray(temperature)
    log_a = (np.log(2 * ZETA_THREE / np.pi**2 * ETA)
             + 1.5 * np.log(2 * np.pi * temperature / M_E)
             + IONIZATION_ENERGY / temperature)
    return 2 / (1 + np.sqrt(1 + 4 * np.exp(log_a)))


def main():
    left, right = .25, .34
    for _ in range(60):
        mid = (left + right) / 2
        if ionized_fraction(mid) < .03:
            left = mid
        else:
            right = mid
    crossing = (left + right) / 2
    samples = np.unique(np.r_[np.linspace(.25, .40, 700), crossing, .30, .28, .27])
    fig, ax = plt.subplots(figsize=(6.0, 3.8), dpi=160, facecolor="white")
    ax.set_facecolor("white")
    ax.plot(samples, ionized_fraction(samples), color="#225ea8", lw=2)
    ax.axhline(.03, color="#a63603", ls=":", lw=1)
    ax.scatter([crossing], [.03], color="#a63603", zorder=5)
    ax.annotate(fr"$X_e=0.03$ at $T\simeq{crossing:.3f}$ eV",
                xy=(crossing, .03), xytext=(.338, .009), fontsize=9, color="#a63603",
                arrowprops={"arrowstyle": "->", "color": "#a63603"})
    ax.annotate("Cooling", xy=(.262, .50), xytext=(.305, .50), fontsize=9,
                arrowprops={"arrowstyle": "->", "color": "0.4"})
    ax.text(.393, .0021, r"$\eta=5.36\times10^{-10}$", fontsize=9)
    ax.set(xlim=(.40, .25), ylim=(.0015, 1.15), yscale="log",
           xlabel="Radiation temperature T (eV)", ylabel=r"Ionization fraction $X_e$",
           title="Equilibrium hydrogen ionization during cooling")
    ax.grid(alpha=.18, which="both")
    fig.tight_layout()
    fig.savefig(Path("paper-62-saha-ionization.png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
