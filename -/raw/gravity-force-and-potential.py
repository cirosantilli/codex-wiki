"""Generate gravity-force-and-potential.png in the current directory.

Analytic point-mass curves; tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    radius = np.linspace(1, 6, 501)
    field = radius**-2
    potential = -radius**-1
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.3), dpi=120,
                             facecolor="white", layout="constrained")
    fig.suptitle("One point mass: field and potential decay differently", fontsize=15)
    axes[0].plot(radius, field, color="#236b9c", lw=2.5)
    axes[1].plot(radius, potential, color="#b3502a", lw=2.5)
    axes[0].set(title=r"Field magnitude: $g/g_0=1/z^2$",
                ylabel=r"$g/g_0$", ylim=(0, 1.2))
    axes[1].set(title=r"Potential: $\Phi/(GM/r_0)=-1/z$",
                ylabel=r"$\Phi/(GM/r_0)$", ylim=(-1.2, .12))
    for value, field_label, potential_label in (
        (1, "1", "−1"), (2, "1/4", "−1/2"), (4, "1/16", "−1/4")
    ):
        axes[0].scatter(value, value**-2, color="#236b9c", s=35, zorder=4)
        axes[1].scatter(value, -value**-1, color="#b3502a", s=35, zorder=4)
        axes[0].annotate(field_label, (value, value**-2), xytext=(8, 9),
                         textcoords="offset points", fontsize=11)
        axes[1].annotate(potential_label, (value, -value**-1), xytext=(8, -21),
                         textcoords="offset points", fontsize=11)
    axes[0].text(.39, .78, "Double the radius:\nfield magnitude ÷ 4",
                 transform=axes[0].transAxes, fontsize=11,
                 bbox={"facecolor": "white", "edgecolor": "none"})
    axes[1].text(.37, .26, "Double the radius:\npotential magnitude ÷ 2",
                 transform=axes[1].transAxes, fontsize=11,
                 bbox={"facecolor": "white", "edgecolor": "none"})
    for ax in axes:
        ax.set(xlabel=r"Radius $z=r/r_0$", xlim=(.9, 6.1))
        ax.set_xticks([1, 2, 3, 4, 5, 6])
        ax.set_facecolor("white")
        ax.grid(alpha=.18)
        ax.axhline(0, color="#555555", lw=.8)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / "gravity-force-and-potential.png",
                facecolor="white", transparent=False)
    plt.close(fig)
    print("At z=1,2,4: g/g0=1,0.25,0.0625; Phi/(GM/r0)=-1,-0.5,-0.25")


if __name__ == "__main__":
    main()
