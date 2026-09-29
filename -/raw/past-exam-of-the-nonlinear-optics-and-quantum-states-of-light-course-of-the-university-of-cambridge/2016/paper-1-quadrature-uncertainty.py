"""Vacuum/one-photon quadrature uncertainties; write PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    eps = np.linspace(-1, 1, 1001)
    x2 = np.sqrt(1 + 2 * eps**2) / 2
    x1 = np.sqrt(.25 - eps**2 / 2 + eps**4)
    fig, ax = plt.subplots(figsize=(6, 3.5), dpi=150, facecolor="white")
    ax.plot(eps, x2, color="#165d9b", lw=2, label=r"Requested $\Delta X_2$")
    ax.plot(eps, x1, "--", color="#a75716", lw=1.8,
            label=r"Comparison: $\Delta X_1$")
    ax.axhline(.5, color="#4b5560", ls=":", lw=1.5, label="Vacuum: 1/2")
    ax.scatter([0], [.5], color="#165d9b", s=20, zorder=5)
    ax.fill_between(eps, x1, .5, where=x1 < .5, color="#a75716", alpha=.1)
    ax.set(xlim=(-1, 1), ylim=(.39, .91), xlabel=r"Real amplitude $\epsilon$",
           ylabel="Quadrature standard deviation",
           title=r"$X_2$ is never squeezed for this real superposition")
    ax.legend(loc="upper center", fontsize=9, frameon=False)
    ax.grid(alpha=.2)
    fig.text(.5, .022, "The quadrature orientation changes which noise can fall below vacuum.",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=.12, right=.975, bottom=.2, top=.86)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
