"""Original redshift-drift sketches. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes only paper-72-redshift-drift.png to the caller's current directory.
Uses the caller's MPLCONFIGDIR without overriding it.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def drift(z):
    s = 1 + np.asarray(z)
    return s - np.sqrt(0.3 * s**3 + 0.7)


def main():
    crossing = (1 + np.sqrt(133)) / 6
    # Include the exact crossing and observer root in both grids.
    z = np.unique(np.r_[np.linspace(0, 5, 800), 0, crossing])
    zoom = np.unique(np.r_[np.linspace(0, 3, 600), 0, crossing])
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.1), facecolor="white")
    ax = axes[0]
    ax.plot(z, (1 + z) - (1 + z)**1.5, label=r"Matter only: $\Omega_m=1$", color="#365f9c")
    ax.plot(z, z, label=r"Vacuum only: $\Omega_\Lambda=1$", color="#a65722")
    ax.plot(z, drift(z), label=r"$\Omega_m=0.3,\ \Omega_\Lambda=0.7$", color="#268565")
    ax.set_title("Three flat expansion histories")
    ax.set_ylim(-9, 5.5)
    ax.legend(loc="lower left", fontsize=9)
    ax = axes[1]
    ax.plot(zoom, drift(zoom), color="#268565", lw=2)
    ax.scatter([0, crossing], [0, 0], color="#268565", zorder=4)
    ax.axvline(crossing, color="#777777", linestyle=":")
    ax.annotate(r"$z_*\simeq2.089$", xy=(crossing, 0), xytext=(1.65, .25),
                arrowprops={"arrowstyle": "->", "color": "#444444"})
    ax.set_title("Matter-vacuum model: crossing detail")
    ax.set_ylim(-.55, .36)
    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="#555555", linewidth=.8)
        ax.set_xlabel(r"Observed redshift $z$")
        ax.set_ylabel(r"$\dot z/H_0$")
        ax.grid(alpha=.2)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "paper-72-redshift-drift.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
