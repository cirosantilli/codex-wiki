"""Original qualitative phase diagram; output PNG basename in cwd.

This schematic is not a fit to, or reproduction of, the source data plot.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Dependencies are declared in the repository's top-level pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    triple_t, triple_p = 1.0, 1.2
    critical_t, critical_p = 3.6, 3.1
    fig, ax = plt.subplots(figsize=(7.5, 4.9), layout="constrained")
    fig.patch.set_facecolor("white")
    sub_t = np.linspace(0.10, triple_t, 160)
    sub_p = triple_p * np.exp(2.2 * (sub_t - triple_t))
    fraction = np.linspace(0, 1, 180)
    vap_t = triple_t + (critical_t - triple_t) * fraction
    vap_p = triple_p + (critical_p - triple_p) * (0.7 * fraction + 0.3 * fraction**3)
    melt_p = np.linspace(triple_p, 4.75, 160)
    melt_t = triple_t + 0.055 * (melt_p - triple_p)
    ax.plot(sub_t, sub_p, color="#845b38", lw=2.3)
    ax.plot(vap_t, vap_p, color="#2463a5", lw=2.3)
    ax.plot(melt_t, melt_p, color="#a33d46", lw=2.3)
    ax.plot([triple_t, critical_t], [triple_p, critical_p], "o", color="black", ms=5)
    ax.vlines([triple_t, critical_t], [0, 0], [triple_p, critical_p],
              color="#aaaaaa", lw=0.8, linestyles=":")
    ax.hlines([triple_p, critical_p], [0, 0], [triple_t, critical_t],
              color="#aaaaaa", lw=0.8, linestyles=":")
    ax.annotate("Triple point", xy=(triple_t, triple_p), xytext=(1.35, 0.76),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.annotate("Critical point", xy=(critical_t, critical_p), xytext=(3.76, 2.64),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.text(0.37, 2.9, "SOLID", ha="center", fontsize=12)
    ax.text(2.15, 3.65, "LIQUID", ha="center", fontsize=12)
    ax.text(2.5, 0.65, "GAS", ha="center", fontsize=12)
    ax.text(4.24, 4.0, "Supercritical\nfluid", ha="center", fontsize=11)
    ax.text(0.17, 0.62, "Sublimation", rotation=33, fontsize=9, color="#845b38")
    ax.text(1.03, 2.15, "Melting", rotation=85, fontsize=9, color="#a33d46")
    ax.text(2.1, 2.25, "Vaporization", rotation=24, fontsize=9, color="#2463a5")
    ax.set_xticks([triple_t, critical_t], [r"$T_t$", r"$T_c$"])
    ax.set_yticks([triple_p, critical_p], [r"$p_t$", r"$p_c$"])
    ax.set(xlabel=r"Temperature $T$ (schematic)",
           ylabel=r"Pressure $p$ (schematic)",
           title="Mercury: phase-boundary topology, not to scale",
           xlim=(0, 4.95), ylim=(0, 4.95))
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=145,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
