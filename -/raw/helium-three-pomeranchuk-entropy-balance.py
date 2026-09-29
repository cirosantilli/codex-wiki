"""Independent local entropy-balance toy model, in arbitrary units, not data.

Tested with Python 3.14, numpy 2.3.5, matplotlib 3.10.7. Run from _media.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.8), facecolor="white")
    temperature = np.linspace(0.05, 0.40, 300)
    left, right = axes
    left.plot(temperature, np.ones_like(temperature), color="#914f13", label=r"Solid: $S_s/b=1$")
    left.plot(temperature, temperature, color="#245d9b", label=r"Liquid: $S_l/b=T/T_0$")
    left.fill_between(temperature, temperature, 1, color="#eef3e6")
    left.annotate("Freezing needs heat input\nat fixed temperature", xy=(0.245, 0.68),
                  xytext=(0.245, 0.68), ha="center", va="center", fontsize=11)
    left.annotate("", xy=(0.35, 0.99), xytext=(0.35, 0.36),
                  arrowprops={"arrowstyle": "<->", "color": "#37473b", "lw": 1.4})
    left.text(0.37, 0.67, r"$S_s-S_l>0$", rotation=90, va="center", ha="center")
    left.set(xlim=(0.05, 0.4), ylim=(0, 1.25), xlabel=r"Temperature $T/T_0$ (arbitrary units)",
             ylabel=r"Molar entropy $S/b$", title="1. Higher entropy in the solid")
    left.legend(loc="upper left", fontsize=10, frameon=False)
    fraction = np.linspace(0, 1 / 8, 301)
    temp_path = (0.25 - fraction) / (1 - fraction)
    right.plot(fraction, temp_path, color="#245d9b", linewidth=2.5)
    right.scatter([0, 1 / 8], [1 / 4, 1 / 7], color="#245d9b", s=35, zorder=4)
    right.annotate(r"Start: $T/T_0=1/4$", xy=(0, 0.25), xytext=(0.012, 0.265), fontsize=11)
    right.annotate(r"$x=1/8, T/T_0=1/7$", xy=(1 / 8, 1 / 7), xytext=(0.025, 0.115),
                   arrowprops={"arrowstyle": "->", "color": "#444444"}, fontsize=11)
    right.annotate("", xy=(0.09, (0.25 - 0.09) / (1 - 0.09)),
                   xytext=(0.055, (0.25 - 0.055) / (1 - 0.055)),
                   arrowprops={"arrowstyle": "->", "color": "#245d9b", "lw": 2.5})
    right.text(0.02, 0.18, r"$S_{\mathrm{total}}/(nb)=1/4$", fontsize=11)
    right.set(xlim=(-0.006, 0.136), ylim=(0.09, 0.29), xlabel=r"Solid mole fraction $x$",
              ylabel=r"Temperature $T/T_0$", title="2. Isolated reversible compression")
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.18)
    fig.suptitle("Pomeranchuk cooling: idealized local model, not data", fontsize=15, weight="bold")
    fig.text(0.5, 0.025, r"Arbitrary units • $T_0=b/a$ • $S_l=aT$, $S_s=b$ • ignore cell heat capacity and losses",
             ha="center", fontsize=10, color="#555555")
    fig.tight_layout(rect=(0, 0.065, 1, 0.93), w_pad=2.7)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
