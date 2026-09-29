"""Plot an original normalized cold-section enthalpy budget, not helium data.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5. Run from _media;
output is liquefaction-enthalpy-fraction-model.png in the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def liquid_fraction(eta, heat):
    return 1 - np.asarray(eta) - heat


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(8.8, 5.6), dpi=110, facecolor="white")
    fig.subplots_adjust(left=.11, right=.97, bottom=.20, top=.83)
    eta = np.linspace(0, 1.10, 551)
    for heat, color in [(0, "#185b9b"), (.05, "#087f8c"), (.20, "#b85a20")]:
        y = liquid_fraction(eta, heat)
        valid = (y >= 0) & (y <= 1)
        ax.plot(eta[valid], y[valid], color=color, lw=2.4,
                label=rf"Heat input $q/L={heat:g}$")
        ax.plot(eta[~valid], y[~valid], color=color, lw=1.4, ls="--")
    ax.axhspan(-.32, 0, facecolor="#f2f2f2", hatch="///", edgecolor="#cccccc", lw=0)
    ax.axhline(0, color="#555555", lw=1)
    ax.scatter([.70], [.25], s=62, color="#087f8c", zorder=5)
    ax.annotate("Chosen example\nη = 0.70, q/L = 0.05\ny = 0.25", (.70, .25),
                xytext=(.25, .11), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#087f8c"},
                bbox={"boxstyle": "round,pad=.4", "fc": "white", "ec": "#087f8c"})
    ax.text(.55, -.20, "Negative algebraic y: no saturated two-phase outlet solution",
            fontsize=10, ha="center", va="center", bbox={"fc": "white", "ec": "none"})
    ax.set(xlim=(0, 1.1), ylim=(-.32, 1.04),
           xlabel=r"Inlet enthalpy above saturated liquid:  $\eta=(h_{\rm in}-h_l)/L$",
           ylabel=r"Liquid mass fraction $y$")
    ax.legend(loc="upper right", framealpha=1, fontsize=10)
    ax.grid(alpha=.18)
    ax.set_axisbelow(True)
    fig.suptitle("How enthalpy and incoming heat limit liquid production", fontsize=15, y=.97)
    fig.text(.5, .885, r"$h_{\rm in}+q=yh_l+(1-y)h_g$     •     $L=h_g-h_l>0$",
             ha="center", fontsize=13)
    fig.text(.5, .055, "Dimensionless chosen model • no helium property fit or historical yield\n"
             "Steady cold section; equilibrium outlet phases at one pressure; negligible work and motion",
             ha="center", fontsize=10, color="#45515e")
    # Independently check conservation with a dimensional enthalpy reference.
    h_liquid, h_gas, h_in, q = 17., 217., 157., 10.
    y = float(liquid_fraction((h_in-h_liquid)/(h_gas-h_liquid), q/(h_gas-h_liquid)))
    assert abs(y - .25) < 1e-14
    assert abs((h_in+q) - (y*h_liquid + (1-y)*h_gas)) < 1e-12
    assert abs(float(liquid_fraction(.70, .30))) < 1e-14
    assert float(liquid_fraction(.70, .31)) < 0
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
