"""Plot physical chemostat equilibria; save basename PNG to the CWD.

Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Run from _media: MPLCONFIGDIR=/tmp/chemostat-mpl python3 ../chemostat-washout-equilibria.py
The algebraic positive branch is plotted only where biomass is nonnegative.
At D=0 the positive-branch limit is shown open: the flow-free model is different.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    mu_max, k_s, feed, yield_coefficient = 1.0, 1.0, 9.0, 0.5
    critical = mu_max * feed / (k_s + feed)
    dilution = np.linspace(0.0, critical, 451)
    nutrient = dilution * k_s / (mu_max - dilution)
    biomass = yield_coefficient * (feed - nutrient)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.8), dpi=100,
                             layout="constrained")
    fig.patch.set_facecolor("white")
    for ax, branch, washout, title, ylabel in zip(
            axes, (nutrient, biomass), (feed, 0.0),
            ("Residual nutrient", "Biomass in the vessel"),
            (r"$s_*$ (g nutrient/L)", r"$x_*$ (g dry biomass/L)")):
        ax.set_facecolor("white")
        ax.plot(dilution[1:], branch[1:], color="#17679b", lw=2.5,
                label="Stable positive culture")
        ax.scatter([0], [branch[0]], s=38, facecolors="white",
                   edgecolors="#17679b", zorder=6)
        ax.plot([0, critical], [washout, washout], color="#c56a16", ls="--",
                lw=2, label="Unstable washout")
        ax.plot([critical, 1.15], [washout, washout], color="#c56a16", lw=2.5,
                label="Stable washout")
        ax.axvline(critical, color="#777777", ls=":", lw=1.5)
        ax.scatter([critical], [washout], color="#444444", s=42, zorder=7)
        example = k_s * 0.5 / (mu_max - 0.5)
        if ax is axes[1]:
            example = yield_coefficient * (feed - example)
        ax.scatter([0.5], [example], color="#17679b", s=42, zorder=7)
        ax.annotate(f"D = 0.5: {example:g} g/L", (0.5, example),
                    xytext=(0.12, 2.7 if ax is axes[0] else 2.2),
                    arrowprops={"arrowstyle": "->", "color": "#17679b"})
        ax.set(xlim=(-0.025, 1.15), xlabel=r"Dilution $D$ (h$^{-1}$)",
               ylabel=ylabel, title=title)
        ax.set_xticks([0, 0.3, 0.5, 0.7, 0.9, 1.1])
        ax.grid(alpha=0.18)
    axes[0].set_ylim(-0.25, 10.0)
    axes[1].set_ylim(-0.15, 5.0)
    axes[0].legend(loc="upper left", fontsize=9, framealpha=1,
                   facecolor="white")
    fig.suptitle("Chemostat washout at D = 0.9 h⁻¹\n"
                 "μmax = 1 h⁻¹, Ks = 1 g/L, feed = 9 g/L, yield = 0.5 g/g")
    destination = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(destination, facecolor="white", transparent=False)
    plt.close(fig)
    print(destination)


if __name__ == "__main__":
    main()
