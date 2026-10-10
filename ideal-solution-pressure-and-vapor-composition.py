"""Draw an invented binary ideal-liquid/ideal-vapor model.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from the desired output directory; writes this script's basename.png there.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, 1, 501)
    p_a = 80 * x
    p_b = 20 * (1 - x)
    pressure = p_a + p_b
    y = p_a / pressure
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.65))
    fig.suptitle("Invented A/B model at 300 K:  p*A = 80 kPa,  p*B = 20 kPa", fontsize=14)
    left, right = axes
    left.plot(x, pressure, color="#202e45", lw=2.5, label=r"Total $P=p_A+p_B$")
    left.plot(x, p_a, color="#1464b4", lw=2, label=r"$p_A=80x_A$ kPa")
    left.plot(x, p_b, color="#b55a00", lw=2, label=r"$p_B=20(1-x_A)$ kPa")
    left.axvline(.4, color=".6", ls=":", lw=1.3)
    left.scatter([.4]*3, [44, 32, 12], c=["#202e45", "#1464b4", "#b55a00"], s=38, zorder=4)
    left.annotate("44 kPa", (.4, 44), xytext=(.48, 44), fontsize=11)
    left.annotate("32 kPa", (.4, 32), xytext=(.48, 29), color="#1464b4", fontsize=10)
    left.annotate("12 kPa", (.4, 12), xytext=(.48, 10), color="#b55a00", fontsize=10)
    left.set(xlabel=r"Liquid mole fraction $x_A$", ylabel="Pressure (kPa)", xlim=(0, 1), ylim=(0, 87), title="Partial pressures add")
    left.legend(loc="upper left", frameon=False, fontsize=10)
    right.plot(x, y, color="#1464b4", lw=2.5, label=r"$y_A=4x_A/(1+3x_A)$")
    right.plot(x, x, color=".5", ls="--", lw=1.4, label=r"Equal compositions: $y_A=x_A$")
    right.plot([.4, .4, 0], [0, 8/11, 8/11], color=".6", ls=":", lw=1.3)
    right.scatter([.4], [8/11], c="#1464b4", s=45, zorder=4)
    right.annotate(r"$x_A=0.4$"+"\n"+r"$y_A=8/11\approx0.7273$", (.4, 8/11), xytext=(.55, .35), fontsize=11,
                   arrowprops={"arrowstyle": "-", "color": "#1464b4"})
    right.set(xlabel=r"Liquid mole fraction $x_A$", ylabel=r"Vapor mole fraction $y_A$", xlim=(0, 1), ylim=(0, 1.03), title="The vapor is enriched in A")
    right.legend(loc="lower right", frameon=False, fontsize=9.5)
    for axis in axes:
        axis.grid(alpha=.15)
        axis.set_xticks(np.linspace(0, 1, 6))
    fig.subplots_adjust(left=.075, right=.985, bottom=.19, top=.80, wspace=.25)
    fig.text(.5, .02, "Ideal liquid + ideal vapor; liquid pressure correction neglected. Chosen inputs, no measured data.", ha="center", fontsize=10, color=".3")
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
