"""Plot the creeping-limit approximation; write an opaque PNG to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    reynolds = np.logspace(-4, -1, 401)
    toy_re = np.array([0.002, 0.004])
    fig, ax = plt.subplots(figsize=(7.4, 4.7), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.loglog(reynolds, 24 / reynolds, color="#246a9b", lw=2.5,
              label=r"Creeping-limit approximation: $C_D=24/\mathrm{Re}_d$")
    ax.scatter(toy_re, 24 / toy_re, color=["#ba5739", "#754c9b"], s=55, zorder=4)
    for re, cd, label, offset in [(0.002, 12000, r"$U_0$: (0.002, 12000)", (-90, 28)),
                                  (0.004, 6000, r"$2U_0$: (0.004, 6000)", (18, -5))]:
        ax.annotate(label, (re, cd), xytext=offset, textcoords="offset points",
                    fontsize=10, arrowprops={"arrowstyle": "-", "color": "#555555"})
    ax.set(xlim=(1e-4, 1e-1), ylim=(180, 3e5),
           xlabel=r"Diameter-based Reynolds number $\mathrm{Re}_d=2a\rho U/\mu$",
           ylabel=r"Drag coefficient $C_D$ (frontal area $A=\pi a^2$)",
           title="Sphere drag coefficient in the creeping-flow approximation")
    ax.grid(True, which="both", alpha=0.18)
    ax.legend(loc="upper right", fontsize=9)
    fig.text(0.5, 0.035, "Mathematical small-Re approximation; not empirical data or an all-Re law.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.075, 1, 1))
    fig.savefig(Path.cwd() / "sphere-drag-coefficient-stokes-limit.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
