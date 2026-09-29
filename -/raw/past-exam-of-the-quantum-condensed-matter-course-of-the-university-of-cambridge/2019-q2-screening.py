"""Original bare and screened potential curves; save PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib; see root pyproject.toml.
Both curves are normalized model functions, not measured screening data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    radius = np.linspace(.06, 5, 1200)
    fig, ax = plt.subplots(figsize=(6.2, 3.8), facecolor="white")
    ax.plot(radius, 1/radius, color="#697781", lw=1.8, ls="--", label=r"Bare: $1/r$")
    ax.plot(radius, np.exp(-radius)/radius, color="#1768ab", lw=2, label="Thomas-Fermi screened")
    ax.axvline(1, lw=.8, ls=":", color="#aeb7bf")
    ax.set(xlim=(0, 5), ylim=(0, 6), xlabel=r"$r/\lambda_{\rm TF}$",
           ylabel=r"$V/[Q/(4\pi\varepsilon_b\lambda_{\rm TF})]$")
    ax.set_title("One screening length suppresses the potential by a factor e", fontsize=10)
    ax.legend(frameon=False, fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
