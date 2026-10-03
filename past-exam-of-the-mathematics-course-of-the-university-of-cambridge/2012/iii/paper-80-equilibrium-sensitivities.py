"""Original qualitative Maykut–Untersteiner sensitivity sketches.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Curves show competing mechanisms, not calculated model solutions or
coordinates traced from a published figure. The historical snow-depth
marker refers to the original model forcing. Only a basename PNG is
written, in the caller's cwd. A supplied MPLCONFIGDIR is left untouched.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(12.6001, 4.5001), dpi=100)
    x = np.linspace(0, 1, 250)
    axes[0].plot(x, 1.05 * (1 - x) ** 0.72, color="#225ea8", lw=2.7)
    axes[0].set_xlabel("Ocean heat flux →\n(forcing-dependent loss boundary)")
    axes[0].set_title("More ocean heat: thinner ice")
    axes[0].annotate("No perennial\nice beyond boundary", (1, 0), (0.46, 0.18),
                     arrowprops={"arrowstyle": "->"}, fontsize=9)
    snow = np.linspace(0, 1.08, 300)
    # Near cancellation below the historical marker; summer protection above.
    h = 0.69 + 0.025 * np.cos(snow * 6) + 3.0 * np.maximum(snow - 0.70, 0) ** 1.4
    axes[1].plot(snow, h, color="#238b45", lw=2.7)
    axes[1].axvline(0.70, color="0.5", ls=":", lw=1.4)
    axes[1].set_xticks([0, 0.7, 1.0], ["0", "0.7", "1.0"])
    axes[1].set_xlabel("Annual snow depth (m)\n(original forcing)")
    axes[1].set_title("Snow: two competing effects")
    axes[1].text(0.08, 0.25, "Winter insulation\nversus summer protection", fontsize=9)
    axes[1].text(0.73, 1.23, "Snow survives\ninto summer", fontsize=9)
    axes[2].plot(x, 1.25 * x ** 0.60, color="#cb181d", lw=2.7)
    axes[2].set_xlabel("Summer albedo →\n(forcing-dependent ice-loss boundary)")
    axes[2].set_title("Higher albedo: less solar melt")
    axes[2].text(0.08, 0.89, "Lower solar absorption\nprotects ice", fontsize=9)
    axes[2].annotate("Loss of perennial ice", (0, 0), (0.08, 0.18),
                     arrowprops={"arrowstyle": "->"}, fontsize=9)
    for i, ax in enumerate(axes):
        ax.set_ylim(0, 1.65)
        ax.set_yticks([])
        if i != 1:
            ax.set_xticks([])
        ax.set_ylabel("Equilibrium thickness (schematic)")
    fig.suptitle("Seasonal equilibrium: qualitative sensitivity sketches", fontsize=14)
    fig.text(0.5, 0.025, "Shapes illustrate mechanisms; no numerical thickness scale or universal loss threshold is implied.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.045, right=0.985, bottom=0.24, top=0.83, wspace=0.30)
    fig.savefig(Path("paper-80-equilibrium-sensitivities.png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
