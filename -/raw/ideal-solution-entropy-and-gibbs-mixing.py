"""Draw mixing functions for the same invented binary model as the VLE figure.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from the desired output directory; writes this script's basename.png there.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    gas_constant = 8.31446261815324
    temperature = 300.0
    amount = 1.0
    x = np.linspace(0, 1, 501)
    s = np.zeros_like(x)
    middle = (x > 0) & (x < 1)
    s[middle] = -x[middle]*np.log(x[middle]) - (1-x[middle])*np.log1p(-x[middle])
    entropy = amount * gas_constant * s
    gibbs = -temperature * entropy / 1000
    selected_entropy = -gas_constant*(.4*np.log(.4)+.6*np.log(.6))
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.65))
    fig.suptitle("Invented A/B ideal solution: mixing 1 mol at 300 K", fontsize=14)
    left, right = axes
    left.plot(x, entropy, color="#217a54", lw=2.5)
    left.scatter([.4], [selected_entropy], c="#217a54", s=45, zorder=4)
    left.annotate(r"$x_A=0.4$"+f"\n{selected_entropy:.3f} J/K", (.4, selected_entropy), xytext=(.12, 3.6),
                  arrowprops={"arrowstyle": "-", "color": "#217a54"})
    left.annotate(r"Maximum: $R\ln 2$", (.5, gas_constant*np.log(2)), xytext=(.53, 6.05), fontsize=10)
    left.set(ylabel=r"$\Delta_{\rm mix}S$ (J/K)", ylim=(0, 6.6), title="Entropy increases")
    right.plot(x, gibbs, color="#7853a6", lw=2.5)
    right.scatter([.4], [-temperature*selected_entropy/1000], c="#7853a6", s=45, zorder=4)
    right.annotate(r"$x_A=0.4$"+f"\n{-temperature*selected_entropy/1000:.3f} kJ", (.4, -temperature*selected_entropy/1000), xytext=(.12, -.8),
                   arrowprops={"arrowstyle": "-", "color": "#7853a6"})
    right.text(.51, -1.91, r"Minimum: $-RT\ln 2$", fontsize=10)
    right.set(ylabel=r"$\Delta_{\rm mix}G$ (kJ)", ylim=(-2.05, .12), title=r"Gibbs energy decreases: $\Delta G=-T\Delta S$")
    for axis in axes:
        axis.axvline(.5, color=".65", ls="--", lw=1)
        axis.axvline(.4, color=".65", ls=":", lw=1)
        axis.axhline(0, color=".6", lw=1)
        axis.set(xlim=(0, 1), xlabel=r"Liquid mole fraction $x_A$")
        axis.set_xticks(np.linspace(0, 1, 6))
        axis.grid(alpha=.15)
    fig.subplots_adjust(left=.075, right=.985, bottom=.19, top=.80, wspace=.25)
    fig.text(.5, .02, "Initially separate pure liquids at a common T and P. Chosen model, no measured data.", ha="center", fontsize=10, color=".3")
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
