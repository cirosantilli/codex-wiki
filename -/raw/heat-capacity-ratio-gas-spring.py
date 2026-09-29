"""Original Ruchardt schematic and analytical gas-spring model, not data.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; the output basename follows this script's basename.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, (setup, model) = plt.subplots(1, 2, figsize=(10.8, 4.8), dpi=100,
                                      gridspec_kw={"width_ratios": [1, 1.2]})
    fig.subplots_adjust(left=0.04, right=0.98, top=0.80, bottom=0.19, wspace=0.32)
    fig.suptitle("Heat-capacity ratio: a gas becomes a spring", fontsize=17, y=0.97)
    fig.text(0.5, 0.89, "Original apparatus schematic and analytical curves — no measured data",
             ha="center", fontsize=11, color="#555555")

    setup.set(xlim=(0, 6), ylim=(0, 5.5))
    setup.axis("off")
    setup.set_title("Rüchardt piston apparatus", fontsize=13)
    setup.add_patch(Rectangle((1.2, 0.65), 2.2, 2.65, facecolor="#e4f1fb", edgecolor="none"))
    setup.plot([1.2, 1.2, 3.4, 3.4], [4.8, 0.65, 0.65, 4.8], color="#333333", lw=2.5)
    setup.add_patch(Rectangle((1.22, 3.30), 2.16, 0.35, facecolor="#a1a9b0", edgecolor="#333333"))
    setup.text(2.3, 2.0, "Sealed gas\n" + r"$p_0,\ V_0,\ T_0$", ha="center", va="center", fontsize=13)
    setup.text(2.3, 4.65, r"Ambient $p_{\rm atm}$", ha="center")
    setup.annotate("", xy=(2.3, 3.80), xytext=(2.3, 4.40),
                   arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#b45c23"})
    setup.text(2.55, 4.04, r"$Mg$", color="#b45c23")
    setup.annotate("", xy=(2.3, 3.23), xytext=(2.3, 2.65),
                   arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#2266a0"})
    setup.annotate("Piston\nmass M, area A", xy=(3.0, 3.5), xytext=(4.0, 2.85),
                   va="center", fontsize=10, arrowprops={"arrowstyle": "-", "color": "#555555"})
    setup.annotate("", xy=(3.75, 4.4), xytext=(3.75, 3.5),
                   arrowprops={"arrowstyle": "->", "lw": 1.8})
    setup.text(4.0, 4.0, "x > 0\nexpansion", fontsize=10, va="center")
    setup.text(2.5, 0.1, r"$p_0=p_{\rm atm}+Mg/A$", ha="center", fontsize=13)

    gamma = 1.4
    q = np.linspace(-0.10, 0.10, 601)
    adiabatic = np.expm1(-gamma * np.log1p(q))
    isothermal = np.expm1(-np.log1p(q))
    model.axvspan(-0.025, 0.025, color="#ecf4e8", label="Small displacement region")
    model.axhline(0, color="#999999", lw=0.8)
    model.axvline(0, color="#999999", lw=0.8)
    model.plot(q, adiabatic, color="#2266a0", lw=2.6, label=r"Adiabatic, $\gamma=1.4$")
    model.plot(q, -gamma * q, "--", color="#2266a0", lw=1.6, label=r"Tangent: $-\gamma q$")
    model.plot(q, isothermal, color="#b45c23", lw=2.3, label="Isothermal limit")
    model.set(xlabel=r"Fractional volume change $q=Ax/V_0$",
              ylabel=r"Net restoring force $F/(p_0 A)$", xlim=(-0.10, 0.10), ylim=(-0.16, 0.19))
    model.set_title(r"$F/(p_0 A)=(1+q)^{-\gamma}-1$", fontsize=13)
    model.legend(loc="upper right", fontsize=9, framealpha=1)
    model.grid(alpha=0.18)
    fig.text(0.50, 0.055, r"Small-amplitude adiabatic stiffness: $k=\gamma p_0 A^2/V_0$"
             "     •     Heat exchange changes the restoring response",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
