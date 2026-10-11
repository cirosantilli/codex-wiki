"""Plot the 2018 B3 radial potential; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def potential(x):
    """V_eff/c^2 at h/(mu*c) = 4, where x = r/mu."""
    return -1 / x + 8 / x**2 - 16 / x**3


def main():
    x = np.linspace(2.3, 26, 1400)
    fig, ax = plt.subplots(figsize=(8.8, 4.4), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.plot(x, potential(x), color="#17638d", linewidth=2.4)
    ax.axhline(0, color="#666666", linestyle="--", linewidth=1)
    for radius, label, color, offset in [
        (4.0, "Unstable circular orbit", "#b3422f", (54, -30)),
        (12.0, "Stable circular orbit", "#28764b", (28, -34)),
    ]:
        ax.scatter(radius, potential(radius), s=48, color=color, zorder=3)
        ax.annotate(
            label + "\n" + rf"$r={int(radius)}\mu$",
            (radius, potential(radius)),
            xytext=offset,
            textcoords="offset points",
            arrowprops={"arrowstyle": "->", "color": color},
            color=color,
            fontsize=10,
        )
    ax.text(21.2, 0.003, r"$k=1$ energy", color="#555555", fontsize=10)
    ax.set(
        xlim=(2.3, 26),
        ylim=(-0.087, 0.02),
        xlabel=r"Areal radius $r/\mu$",
        ylabel=r"Specific effective potential $V_{\rm eff}/c^2$",
        title=r"Schwarzschild radial potential: $h=4\mu c$",
    )
    ax.grid(alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path("2018-effective-potential.png"), dpi=160, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
