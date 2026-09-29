"""Compare a reversible gas path with a constant external-load work rectangle.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes an opaque white reversible-versus-constant-load-work.png to cwd.
The irreversible gas path and its time dependence are deliberately unspecified.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    volume = np.linspace(1.0, 2.0, 1001)  # L
    reversible_pressure = 1.0 / volume  # MPa
    external_pressure = np.full_like(volume, 0.5)  # MPa
    reversible_work = np.log(2.0)  # kJ
    load_work = 0.5 * (volume[-1] - volume[0])  # kJ
    extra_work = reversible_work - load_work
    assert abs(np.trapezoid(reversible_pressure - external_pressure, volume)
               - extra_work) < 1e-7
    assert load_work == 0.5 and extra_work > 0
    # Total entropy divided by nR: reservoir at T, ideal work store.
    assert np.isclose(np.log(2) - reversible_work, 0)
    assert np.isclose(np.log(2) - load_work, extra_work)
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.2, 5.8), dpi=120)
    fig.subplots_adjust(left=0.11, right=0.97, bottom=0.22, top=0.82)
    blue, orange = "#216a99", "#b8531c"
    ax.fill_between(volume, 0, external_pressure, color="#f7dfc7")
    ax.fill_between(volume, external_pressure, reversible_pressure, color="#d7eaf5")
    ax.plot(volume, reversible_pressure, color=blue, lw=3,
            label="Reversible equilibrium gas pressure")
    ax.plot(volume, external_pressure, color=orange, lw=2.5, ls="--",
            label="Constant external pressure (load)")
    ax.vlines([1, 2], 0, 0.5, color=orange, lw=1.5)
    ax.plot([1, 1], [0.5, 1], color="#626262", ls=":", lw=1.8)
    ax.plot([1, 2], [1, 0.5], "o", color="#232a30", ms=7, zorder=5)
    ax.plot(1, 0.5, "o", color=orange, mfc="white", ms=8, mew=2, zorder=6)
    ax.annotate("Initial gas state\n1 L, 1 MPa", (1, 1), xytext=(1.11, 1.13),
                fontsize=11, arrowprops={"arrowstyle": "-", "color": "#555555"})
    ax.annotate("Final gas state\n2 L, 0.5 MPa", (2, 0.5), xytext=(1.87, 0.84),
                ha="center", fontsize=11,
                arrowprops={"arrowstyle": "-", "color": "#555555"})
    ax.annotate("Finite initial\nimbalance", (1, 0.75), xytext=(1.23, 0.9),
                ha="center", fontsize=10, color="#555555",
                arrowprops={"arrowstyle": "->", "color": "#626262"})
    ax.text(1.56, 0.22, "External-load rectangle\nWork out = 0.500000 kJ",
            ha="center", fontsize=12, color=orange)
    ax.annotate("Extra reversible work\n0.193147 kJ", (1.3, 0.63),
                xytext=(1.47, 1.02), ha="center", fontsize=11, color=blue,
                arrowprops={"arrowstyle": "->", "color": blue})
    ax.set(xlim=(0.8, 2.13), ylim=(0, 1.35), xlabel="Gas volume V (L)",
           ylabel="Pressure (MPa)")
    ax.set_xticks([1, 1.25, 1.5, 1.75, 2])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1, 1.25])
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Same gas endpoints; different work delivered", fontsize=15, pad=30)
    ax.text(0.5, 1.06, r"$nRT=1$ kJ; reversible work = 0.693147 kJ",
            transform=ax.transAxes, ha="center", fontsize=11)
    ax.legend(loc="upper right", fontsize=10, frameon=False)
    fig.text(0.55, 0.09, "Dashed line = external load, not the irreversible gas pressure path",
             ha="center", fontsize=11)
    fig.text(0.55, 0.045, "Gas temperature may change during motion; the bath restores T at the endpoint",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)
    print(f"Load work = {load_work:.9f} kJ; extra reversible work = {extra_work:.9f} kJ")
    print(f"Entropy production / (nR): reversible = 0; constant load = {extra_work:.9f}")


if __name__ == "__main__":
    main()
