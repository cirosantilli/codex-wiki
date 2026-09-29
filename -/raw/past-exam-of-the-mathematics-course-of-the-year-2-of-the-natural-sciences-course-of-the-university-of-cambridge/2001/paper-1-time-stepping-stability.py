"""Stability regions for decay y'=-Lambda*y, z=h*Lambda.

Python 3.14, NumPy 2.3, Matplotlib 3.10. Write PNG into cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})
    real = np.linspace(-3.5, 4.5, 650)
    imag = np.linspace(-3.5, 3.5, 600)
    xx, yy = np.meshgrid(real, imag)
    z = xx+1j*yy
    # The second panel uses the equivalent nonsingular condition |1+z| >= 1.
    levels = [np.abs(1-z), -np.abs(1+z), np.abs(1-z+z*z/2)]
    limits = [1, -1, 1]
    titles = ["Forward Euler", "Backward Euler", "Heun predictor-corrector"]
    formulas = [r"$|1-z|\leq1$", r"$|1+z|\geq1$", r"$|1-z+z^2/2|\leq1$"]
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.1), dpi=110, layout="constrained")
    for ax, values, limit, title, formula in zip(axes, levels, limits, titles, formulas):
        ax.contourf(xx, yy, values, levels=[-100, limit], colors=["#c8e1ed"])
        ax.contour(xx, yy, values, levels=[limit], colors=["#216b96"], linewidths=1.5)
        ax.axvline(0, color="0.4", lw=0.75, ls="--")
        ax.axhline(0, color="0.4", lw=0.75)
        ax.set(xlim=(-3.5, 4.5), ylim=(-3.5, 3.5), xlabel=r"Re $z$", ylabel=r"Im $z$",
               title=title+"\n"+formula)
        ax.set_aspect("equal")
        ax.set_xticks([-2, 0, 2, 4])
        ax.set_yticks([-2, 0, 2])
        ax.grid(alpha=0.12)
    fig.suptitle(r"Shaded: bounded amplification for $y'=-\Lambda y$, $z=h\Lambda$", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
