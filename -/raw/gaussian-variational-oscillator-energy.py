"""Gaussian oscillator energy versus position standard deviation.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; writes an opaque white PNG in cwd.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    sigma = np.linspace(0.30, 1.55, 700)
    kinetic = 1 / (8 * sigma**2)
    potential = sigma**2 / 2
    fig, ax = plt.subplots(figsize=(8, 4.8), dpi=130)
    ax.plot(sigma, kinetic + potential, color="#235f91", lw=2.8,
            label=r"Trial energy $E=1/(8\sigma^2)+\sigma^2/2$")
    ax.plot(sigma, kinetic, color="#af5714", lw=2, ls="--",
            label=r"Kinetic $1/(8\sigma^2)$")
    ax.plot(sigma, potential, color="#238367", lw=2, ls="-.",
            label=r"Potential $\sigma^2/2$")
    ax.axhline(0.5, color="#545454", lw=1.3, ls=":",
               label=r"Exact ground energy $E_0=1/2$")
    ax.scatter([0.5, 1], [0.625, 0.625], color="#235f91", s=40, zorder=5)
    ax.annotate(r"$\sigma=0.5$: $E=0.625$", (0.5, 0.625),
                xytext=(0.32, 0.88), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#545454"})
    ax.annotate(r"$\sigma=1$: $E=0.625$", (1, 0.625),
                xytext=(1.03, 0.85), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#545454"})
    ax.scatter([1 / np.sqrt(2)], [0.5], color="#792f86", s=60, zorder=6)
    ax.annotate(r"$\sigma=1/\sqrt{2}$, $E=0.5$", (1 / np.sqrt(2), 0.5),
                xytext=(0.73, 0.18), fontsize=11, color="#792f86",
                arrowprops={"arrowstyle": "->", "color": "#792f86"})
    ax.set(xlim=(0.30, 1.55), ylim=(0, 1.6),
           xlabel=r"Position standard deviation $\sigma$",
           ylabel=r"Energy (units of $\hbar\omega$)",
           title=r"Gaussian oscillator trials: $\hbar=m=\omega=1$")
    ax.legend(frameon=False, fontsize=10, loc="upper center")
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
